# Agent trace: https://research.trychroma.com/context-rot

- Model: `deepseek/deepseek-v4.1-flash-1017`
- Started: 2026-11-26T18:36:53
- Max turns: 25
- Tools: read_url, web_search, assess_credibility, save_report


**User:** Evaluate the credibility of this source: https://research.trychroma.com/context-rot

## Turn 1

_Model call: 4,682 input tokens, 74 output tokens_

**Assistant:**

I'll start by reading the source page.

**Tool call** `read_url` (id `chatcmpl-tool-9533d8a9502c4f79`):

```json
{
  "url": "https://research.trychroma.com/context-rot",
  "start": 0
}
```
**Tool result** `read_url` (id `chatcmpl-tool-9533d8a9502c4f79`, 10,096 characters):

```
Title: Context Rot: How Increasing Input Tokens Impacts LLM Performance

URL Source: https://research.trychroma.com/context-rot

Final URL: https://www.trychroma.com/research/context-rot

Markdown Content:
Recent developments in LLMs show a trend toward longer context windows, with the input token count of the latest models reaching the millions. Because these models achieve near-perfect scores on widely adopted benchmarks like Needle in a Haystack (NIAH) [[1](https://www.trychroma.com/research/context-rot#niah)], it’s often assumed that their performance is uniform across long-context tasks.

However, NIAH is fundamentally a simple retrieval task, in which a known sentence (the “needle”) is placed in a long document of unrelated text (the “haystack”), and the model is prompted to retrieve it. While scalable, this benchmark typically assesses direct lexical matching, which may not be representative of flexible, semantically oriented tasks.

![Image 1](https://www.trychroma.com/img/context_rot/niah_lexical.png)

Example Needle in a Haystack (NIAH) Setup

We extend the standard NIAH task, to investigate model behavior in previously underexplored settings. We examine the effects of needles with semantic, rather than direct lexical matches, as well as the effects of introducing variations to the haystack content.

Additionally, we include a conversational question-answer evaluation using LongMemEval [[2](https://www.trychroma.com/research/context-rot#longmemeval)], as well as a synthetic task in which models replicate a series of repeated words. Each task remains intentionally simple and is deliberately controlled to isolate the impact of context length alone.

We demonstrate that even under these minimal conditions, model performance degrades as input length increases, often in surprising and non-uniform ways. Real-world applications typically involve much greater complexity, implying that the influence of input length may be even more pronounced in practice.

Our in-depth technical report continues below. If you find our work useful, please consider citing us:

Interested in working on improving retrieval for AI applications? [Chroma is Hiring](https://careers.trychroma.com/)

* * *

## Introduction[#](https://www.trychroma.com/research/context-rot)

It is common for modern LLMs to have input context lengths in the millions of tokens. Gemini 1.5 Pro [[3](https://www.trychroma.com/research/context-rot#gemini-1.5-pro)] first introduced their 1M context window in early 2024, followed by the recent GPT-4.1’s 1M context window [[4](https://www.trychroma.com/research/context-rot#gpt-4.1)] and Llama 4 with 10M [[5](https://www.trychroma.com/research/context-rot#llama-4)]. The use case for long context is compelling: longer context means that the LLM can process more information with each call and generate more informed outputs.

Long context evaluations for these models often demonstrate consistent performance across input lengths. However, these evaluations are narrow in scope and not representative of how long context is used in practice. The most commonly used test, Needle in a Haystack (NIAH), is a simple lexical retrieval task often used to generalize a model’s ability to reliably handle long context. Real applications, such as agent tasks or summarization, demand significantly more processing and reasoning over broader, often more ambiguous information.

Designing realistic long context benchmarks is challenging. Tasks often grow in complexity as input length increases, making it difficult to isolate whether performance drops are due to longer inputs or inherently harder problems. To address this, our experiments hold task complexity constant while varying only the input length—allowing us to directly measure the effect of input length alone.

## Contributions[#](https://www.trychroma.com/research/context-rot)

We present the following:

*   An evaluation across 18 LLMs, including leading closed-source and open-weights models, revealing nonuniform performance with increasing input length.

*   A writeup of observed model-specific behavior patterns when handling distractors and varying question-answer similarity.

*   The [complete codebase](https://github.com/chroma-core/context-rot) to replicate our results.

* * *

## Related Work[#](https://www.trychroma.com/research/context-rot)

One of the most widely used benchmarks for evaluating a model’s long context capabilities is Needle in a Haystack (NIAH). While useful as a scalable test, it measures a narrow capability: lexical retrieval. Models typically perform well on NIAH, which has led to the perception that long-context is largely solved.

However, NIAH underestimates what most long context tasks require in practice. Variants of NIAH, like NoLiMa [[6](https://www.trychroma.com/research/context-rot#nolima)] which include needle-question pairs with non-lexical matches, reveal significant performance drops. Other tasks that appear similar in regards to difficulty, such as AbsenceBench [[7](https://www.trychroma.com/research/context-rot#absencebench)] which tests models for recognizing the absence of a given snippet of text, also demonstrate performance degradation with growing input length.

Additionally, long context tasks often involve disambiguating amongst distractors as part of the task. One example is Multi-round co-reference resolution (MRCR) [[8](https://www.trychroma.com/research/context-rot#michelangelo)] [[9](https://www.trychroma.com/research/context-rot#oai-mrcr)], which involves retrieving the i-th instance of a specific user ask, amongst similar user asks, in a multi-turn conversation. However, there remains a lack of investigation into the impact of distractors in long context settings.

An important factor in long-context tasks is how input length is scaled. Latent List [[8](https://www.trychroma.com/research/context-rot#michelangelo)] is a task in which the model must perform a fixed number of Python list operations across various input lengths. Various ways to fill irrelevant context are tested, which reveal non-uniform impact on model performance [[1](https://www.trychroma.com/research/context-rot#clarification)]. For instance, adding list operations that locally cancel each other out degrades model performance more significantly compared to adding print statements. This highlights how the type of 'irrelevant content' matters, as some may introduce increasing complexity with input length.

Similarly, Graphwalks [[10](https://www.trychroma.com/research/context-rot#graphwalks)] is a graph traversal task in which the model is given a directed graph composed of hexadecimal hashes, then asked to perform breadth-first search starting from a random node. Increasing input length means increasing the size of the graph to traverse through, which increases task difficulty as a result. It is difficult to disambiguate increasing task complexity from input length, which makes it difficult to isolate the impact on performance due to input length alone. This points to the importance of isolating input length as the variable of interest, which is essential for understanding of how LLMs actually behave with long inputs.

* * *

## Needle in a Haystack Extension[#](https://www.trychroma.com/research/context-rot)

The classic Needle in a Haystack task involves placing a random fact (the 'needle') in the middle of a long context window (the 'haystack'), then asking the model about that fact.

The original implementation of this task uses a needle-question pair with lexical matches. However, usage of long context in practice often requires semantic understanding of ambiguous tasks.

![Image 2](https://www.trychroma.com/img/context_rot/niah/lexical_2.png)

Example Needle in a Haystack (NIAH) Setup with Lexical Matching

NoLiMa has demonstrated non-lexical matching to be a challenge for models as context length increases. This task utilizes needle-question pairs that require models to infer latent associations, for example:

> Question: Which character has been to Helsinki?
> 
> 
> Needle: Actually, Yuki lives next to the Kiasma museum.

NoLiMa - sample Needle-Question pair

In order to answer this question, the model would first have to know that Kiasma museum is located in Helsinki, then make that latent association link. This tests the model not only for its non-lexical matching abilities, but also for its world knowledge. 72.4% of needle-question pairs from NoLiMa require such external knowledge, making this benchmark closer to a test of how models handle both tasks at once rather than pure non-lexical matching alone.

Testing the impact of non-lexical matching in isolation remains underexplored. Furthermore, this binary distinction of “lexical” versus “non-lexical” oversimplifies the complexity of question-answering in real-world scenarios. Needle-question pairs exist on a spectrum of similarity, yet they are all classified under these broad categories.

Models often have to deal with distractors as well, which has been shown to degrade performance [[11](https://www.trychroma.com/research/context-rot#distractors)].

Throughout this report, we distinguish between distractors and irrelevant content:

![Image 3](https://www.trychroma.com/img/context_rot/niah/distractor_irrelevance.png)

Comparison - Distractor vs. Irrelevant Context

*   Distractors are topically related to the needle, but do not quite answer the question
*   Irrelevant content is unrelated to the needle and question

Prior work has demonstrated that distractors have non-uniform impact, yet most evaluations involve short input lengths and older models. Current state-of-the-art models are claimed to be more resilient to distractors, yet their performance has not been extensively tested across various input lengths.

Another underexplored aspect of NIAH is the haystack itself, which is often simply treated as a means of scaling input length, but this assumes that the haystack content itself has no 

[Showing characters 0-10,000 of 58,177. Call read_url with start=10000 to read the next part.]
```

## Turn 2

_Model call: 6,960 input tokens, 314 output tokens_

**Tool call** `read_url` (id `call-5bf16afe-158d-49ae-bd7d-18c408da0573`):

```json
{
  "url": "https://research.trychroma.com/context-rot",
  "start": 10000
}
```
**Tool call** `read_url` (id `call-d88042df-c6fc-4e0b-90bb-7c54a5a80cad`):

```json
{
  "url": "https://research.trychroma.com/context-rot",
  "start": 49000
}
```
**Tool call** `web_search` (id `call-87674d0f-a740-48f1-90f1-2c2988ece446`):

```json
{
  "query": "Chroma \"Context Rot\" research report authors"
}
```
**Tool result** `read_url` (id `call-d88042df-c6fc-4e0b-90bb-7c54a5a80cad`, 9,236 characters):

```
 how that information is presented. We demonstrate that even the most capable models are sensitive to this, making effective context engineering essential for reliable performance.

## Footnotes[#](https://www.trychroma.com/research/context-rot)

[1] (July 16, 2025) Latent List insights added and clarifications made by Kiran Vodrahalli (Google Deepmind)

[2] Original source for examples: [https://arxiv.org/pdf/2410.10813](https://arxiv.org/pdf/2410.10813)

## References[#](https://www.trychroma.com/research/context-rot)

[1] Kamradt, G. (2023). Needle In A Haystack - Pressure Testing LLMs [GitHub Repository]. [Link](https://github.com/gkamradt/LLMTest_NeedleInAHaystack)

[2] Wu, D., Wang, H., Yu, W., Zhang, Y., Chang, K.-W., and Yu, D. (2025). LongMemEval: Benchmarking Chat Assistants on Long-Term Interactive Memory. arXiv preprint arXiv:2410.10813. [Link](https://arxiv.org/abs/2410.10813)

[3] Gemini Team, Georgiev, P., Lei, V. I., Burnell, R., Bai, L., Gulati, A., Tanzer, G., Vincent, D., Pan, Z., Wang, S., et al. (2024). Gemini 1.5: Unlocking multimodal understanding across millions of tokens of context. arXiv preprint arXiv:2403.05530. [Link](https://arxiv.org/abs/2403.05530)

[4] OpenAI, Kumar, A., Yu, J., Hallman, J., Pokrass, M., Goucher, A., Ganesh, A., Cheng, B., McKinzie, B., Zhang, B., Koch, C., et al. (2025). Introducing GPT-4.1 in the API. [Link](https://openai.com/index/gpt-4-1/)

[5] Meta AI, (2025). The Llama 4 herd: The beginning of a new era of natively multimodal AI innovation. [Link](https://ai.meta.com/blog/llama-4-multimodal-intelligence/)

[6] Modarressi, A., Deilamsalehy, H., Dernoncourt, F., Bui, T., Rossi, R. A., Yoon, S., and Schütze, H. (2025). NoLiMa: Long-Context Evaluation Beyond Literal Matching. arXiv preprint arXiv:2502.05167. [Link](https://arxiv.org/abs/2502.05167)

[7] Fu, H. Y., Shrivastava, A., Moore, J., West, P., Tan, C., and Holtzman, A. (2025). AbsenceBench: Language Models Can't Tell What's Missing. arXiv preprint arXiv:2506.11440. [Link](https://arxiv.org/abs/2506.11440)

[8] Vodrahalli, K., Ontanon, S., Tripuraneni, N., Xu, K., Jain, S., Shivanna, R., Hui, J., Dikkala, N., Kazemi, M., Fatemi, B., et al. (2024). Michelangelo: Long Context Evaluations Beyond Haystacks via Latent Structure Queries. arXiv preprint arXiv:2409.12640. [Link](https://arxiv.org/abs/2409.12640)

[9] openai. (2025). mrcr [Dataset]. Hugging Face. [Link](https://huggingface.co/datasets/openai/mrcr)

[10] openai. (2025). graphwalks [Dataset]. Hugging Face. [Link](https://huggingface.co/datasets/openai/graphwalks)

[11] Shi, F., Chen, X., Misra, K., Scales, N., Dohan, D., Chi, E., Schärli, N., and Zhou, D. (2023). Large Language Models Can Be Easily Distracted by Irrelevant Context. arXiv preprint arXiv:2302.00093. [Link](https://arxiv.org/abs/2302.00093)

[12] jamescalam. (2024). ai-arxiv2 [Dataset]. Hugging Face. [Link](https://huggingface.co/datasets/jamescalam/ai-arxiv2)

[13] Peng, B., Quesnelle, J., Fan, H., and Shippole, E. (2023). YaRN: Efficient Context Window Extension of Large Language Models. arXiv preprint arXiv:2309.00071. [Link](https://arxiv.org/abs/2309.00071)

[14] McInnes, L., Healy, J., and Melville, J. (2020). UMAP: Uniform Manifold Approximation and Projection for Dimension Reduction. arXiv preprint arXiv:1802.03426. [Link](https://arxiv.org/abs/1802.03426)

[15] Campello, R. J. G. B., Moulavi, D., and Sander, J. (2013). Density-Based Clustering Based on Hierarchical Density Estimates. In Pei, J., Tseng, V. S., Cao, L., Motoda, H., and Xu, G. (Eds.), Advances in Knowledge Discovery and Data Mining (PAKDD 2013), Lecture Notes in Computer Science, vol 7819. Springer, Berlin, Heidelberg. [Link](https://doi.org/10.1007/978-3-642-37456-2_14)

## Appendix[#](https://www.trychroma.com/research/context-rot)

Cleaned LongMemEval datasets and needles/distractors used can be downloaded [here](https://drive.google.com/drive/folders/1FuOysriSotnYasJUbZJzn31SWt85_3yf).

## LLM judge alignment:[#](https://www.trychroma.com/research/context-rot)

We employ LLM judges to evaluate outputs for our NIAH and LongMemEval experiments. These judges are calibrated to human judgment through the following process:

1.   A subset of model outputs are manually labeled as incorrect/correct (~500 outputs for NIAH, ~600 outputs for LongMemEval)

2.   GPT-4.1 is used to label the same subset of model outputs as incorrect/correct.

3.   An alignment score is calculated by measuring the proportion of human-model aligned judgements.

4.   The prompt is iterated on based on manual inspection of misalignments.

5.   Steps 2-4 are repeated until an alignment score > 0.99 is achieved.

## Models Tested[#](https://www.trychroma.com/research/context-rot)

Not all 18 models are included in each experiement due to context window or thinking_budget constraints.

### Anthropic[#](https://www.trychroma.com/research/context-rot)

*   Claude Opus 4
*   Claude Sonnet 4
*   Claude Sonnet 3.7
*   Claude Sonnet 3.5
*   Claude Haiku 3.5

### OpenAI[#](https://www.trychroma.com/research/context-rot)

*   o3
*   GPT-4.1
*   GPT-4.1 mini
*   GPT-4.1 nano
*   GPT-4o
*   GPT-4 Turbo
*   GPT-3.5 Turbo

### Google[#](https://www.trychroma.com/research/context-rot)

*   Gemini 2.5 Pro
*   Gemini 2.5 Flash
*   Gemini 2.0 Flash

### Alibaba[#](https://www.trychroma.com/research/context-rot)

*   Qwen3-235B-A22B
*   Qwen3-32B
*   Qwen3-8B

## Embedding Models Used[#](https://www.trychroma.com/research/context-rot)

*   text-embedding-3-small
*   text-embedding-3-large
*   jina-embeddings-v3 (input_type='text-matching')
*   voyage-3-large (input_type=None)
*   all-MiniLM-L6-v2

## Needle-Question Similarity[#](https://www.trychroma.com/research/context-rot)

Note: thinking/non-thinking modes of the same model are treated separately

![Image 26](https://www.trychroma.com/img/context_rot/appendix/arxiv_pg_nq_sim.png)

Needle-Question Similarity - arXiv haystack/PG essay needles

![Image 27](https://www.trychroma.com/img/context_rot/appendix/pg_pg_nq_sim.png)

Needle-Question Similarity - PG essay haystack/PG essay needles

![Image 28](https://www.trychroma.com/img/context_rot/appendix/pg_arxiv_nq_sim.png)

Needle-Question Similarity - PG essay haystack/arXiv needles

As mentioned in our Needle-Haystack Similarity results, we note this one occurance in which models perform exceptionally well compared to the other needle-haystack combinations. On its own, it may seem that the high performance models have uniform performance. However, such uniformity for these models does not hold across the rest of the experiments.

## Impact of Distractors[#](https://www.trychroma.com/research/context-rot)

![Image 29](https://www.trychroma.com/img/context_rot/appendix/distractors_num_arxiv.png)

Impact of Distractors: Performance by Number of Distractors - arXiv haystack/arXiv needles

![Image 30](https://www.trychroma.com/img/context_rot/appendix/distractors_ind_arxiv.png)

Impact of Distractors: Performance by Individual Distractors - arXiv haystack/arXiv needles

![Image 31](https://www.trychroma.com/img/context_rot/appendix/distractors_num_pg.png)

Impact of Distractors: Performance by Number of Distractors - PG essay haystack/PG essay needles

![Image 32](https://www.trychroma.com/img/context_rot/appendix/distractors_ind_pg.png)

Impact of Distractors: Performance by Individual Distractors - PG essay haystack/PG essay needles

![Image 33](https://www.trychroma.com/img/context_rot/appendix/distractors_num_pg_arxiv.png)

Impact of Distractors: Performance by Number of Distractors - PG essay haystack/arXiv needles

![Image 34](https://www.trychroma.com/img/context_rot/appendix/distractors_ind_pg_arxiv.png)

Impact of Distractors: Performance by Individual Distractors - PG essay haystack/arXiv needles

![Image 35](https://www.trychroma.com/img/context_rot/appendix/failures_arxiv.png)

Impact of Distractors: Failure Analysis - arXiv haystack/arXiv needles

![Image 36](https://www.trychroma.com/img/context_rot/appendix/failures_writing.png)

Impact of Distractors: Failure Analysis - PG essay haystack/PG essay needles

![Image 37](https://www.trychroma.com/img/context_rot/appendix/failures_writing_arxiv.png)

Impact of Distractors: Failure Analysis - PG essay haystack/arXiv needles

## Repeated Words[#](https://www.trychroma.com/research/context-rot)

![Image 38](https://www.trychroma.com/img/context_rot/appendix/gpt_position_accuracy.png)

Repeated Words: Position Accuracy - GPT Family

![Image 39](https://www.trychroma.com/img/context_rot/appendix/gemini_position_accuracy.png)

Repeated Words: Position Accuracy - Gemini Family

![Image 40](https://www.trychroma.com/img/context_rot/appendix/qwen_position_accuracy.png)

Repeated Words: Position Accuracy - Qwen Family

![Image 41](https://www.trychroma.com/img/context_rot/appendix/wc_gpt.png)

Repeated Words: Word Count Difference - GPT Family

![Image 42](https://www.trychroma.com/img/context_rot/appendix/wc_gemini.png)

Repeated Words: Word Count Difference - Gemini Family

![Image 43](https://www.trychroma.com/img/context_rot/appendix/wc_qwen.png)

Repeated Words: Word Count Difference - Qwen Family


[End of page. Showed characters 49,000-58,177 of 58,177.]
```
**Tool result** `read_url` (id `call-5bf16afe-158d-49ae-bd7d-18c408da0573`, 10,101 characters):

```
effect on task performance. If the model is indeed insensitive to the content of the haystack, then varying this content, for example the haystack’s topic or narrative flow, should have no influence on the results. However, this assumption remains largely untested.

We design four controlled experiments to investigate the influence of these factors:

## Needle-Question Similarity[#](https://www.trychroma.com/research/context-rot)

We compute the cosine similarity between needle-question pairs using embeddings. For robustness, we average across five embedding models: text-embedding-3-small, text-embedding-3-large, jina-embeddings-v3, voyage-3-large, and all-MiniLM-L6-v2. We measure how model performance is impacted by needle-question similarity as input length increases.

## Impact of Distractors[#](https://www.trychroma.com/research/context-rot)

Taking a high-similarity needle-question pair, we write four distractors. We have the following setups:

*   Baseline: needle only, no distractors
*   Single distractor: needle + one randomly positioned distractor
*   Multiple distractors: needle + all four distractors randomly positioned

We test the impact of distractors on model performance as input length increases to measure non-uniformity amongst distractors and input lengths.

## Needle-Haystack Similarity[#](https://www.trychroma.com/research/context-rot)

We use two thematically distinct haystacks, Paul Graham essays and arXiv papers [[12](https://www.trychroma.com/research/context-rot#arxiv)], and write corresponding needles for each. To measure needle-haystack similarity, we embed the haystack and retrieve the top-5 chunks for each needle, then average their cosine similarity scores. This process is repeated across five different embedding models for robustness.

## Haystack Structure[#](https://www.trychroma.com/research/context-rot)

In typical NIAH setups, haystacks are concatenations of coherent texts, each with their own logical flow of ideas. For instance, the original NIAH benchmark uses a series of Paul Graham essays, where each essay follows a structured organization of ideas to form an argument. To evaluate whether this structure influences model performance, we compare two conditions:

*   Original: preserves the natural flow of ideas within each excerpt
*   Shuffled: sentences are randomly reordered throughout the haystack to maintain the same overall topic without logical continuity

We demonstrate the following:

*   Across all experiments, model performance consistently degrades with increasing input length.
*   Lower similarity needle-question pairs increases the rate of performance degradation.
*   Distractors have non-uniform impact on model performance with regards to how distracting they are relative to each other. We see this impact more prominently as input length increases, and observe distinctions in how various models respond to them.
*   Needle-haystack similarity does not have a uniform effect on model performance, suggesting the need for further investigation.
*   The structural pattern of the haystack consistently shows an impact on how models process long inputs.

## Details[#](https://www.trychroma.com/research/context-rot)

For every unique combination of needle type, haystack topic, and haystack structure, we test each model across:

*   8 input lengths
*   11 needle positions

We evaluate each model across its maximum context window with temperature=0 unless that setting is incompatible (i.e. o3) or explicitly discouraged (i.e. Qwen’s “thinking mode”). For Qwen models, we apply the YaRN method [[13](https://www.trychroma.com/research/context-rot#yarn)] to extend from 32,768 to 131,072 tokens.

We include models in both standard and “thinking mode” where applicable.

We evaluate model outputs using an aligned GPT-4.1 judge, using our method outlined in the appendix.

We note some rare instances of a model refusing to attempt the task (69 out of 194,480 total LLM calls—0.035%). For example, Claude Opus 4 may sometimes have an empty output with stop_reason=”refusal”.

## Needle-Question Similarity[#](https://www.trychroma.com/research/context-rot)

In real-world applications, models are often expected to handle ambiguous tasks and identify relevant information without relying on exact lexical matches. For example, when an agent is given a task involving a large corpus to search through, users rarely specify precise keywords for relevant parts. Instead, the model must infer relevance.

We vary the similarity of our needle-question pairs, quantified by the cosine similarity of their embeddings. We find that as needle-question similarity decreases, model performance degrades more significantly with increasing input length. This reflects more realistic scenarios where exact question-answer matches are rare, and semantic ambiguity compounds the challenge of long input processing.

## Experiment[#](https://www.trychroma.com/research/context-rot)

We source our haystack content from two domains: Paul Graham essays (as in the original NIAH experiment), and arXiv papers. For each haystack topic (PG essays, arXiv), we first determine common themes to guide our question and needle writing.

We use clustering to identify the most common topics that appear for a given corpus:

1.   Chunk documents into 1-3 sentence chunks

2.   Embed each chunk using text-embedding-3-large

3.   Use UMAP [[14](https://www.trychroma.com/research/context-rot#umap)] for dimensionality reduction with the following parameters: n_neighbors=30, min_dist=0.05, n_components=50, random_state=42

4.   Use HDBSCAN [[15](https://www.trychroma.com/research/context-rot#hdbscan)] to create clusters with the following parameters: min_cluster_size=10, min_samples=15

5.   Get 20 representative chunks for the largest clusters using maximal marginal relevance (MMR)

6.   Manually examine the largest clusters to determine their themes and style

Using this method, we identify writing advice as a common topic for PG essays, often in anecdotal form. For arXiv papers, we identify information retrieval as a common topic, specifically re-ranking.

We write a corresponding question for each topic:

> PG essays: "What was the best writing advice I got from my college classmate?"
> 
> 
> arXiv papers: "Which low-latency reranker is preferred for scientific domains?"

Questions for Paul Graham essays & arXiv papers

Before writing our needles, we verify that answers to these questions do not exist in the haystack content:

1.   We store our previously computed haystack chunk embeddings in a vector database.
2.   Query top-10 results from that vector database with our question embedding.
3.   Manually examine these results to verify that they do not answer the given question.

This sets up a fair testing environment as it ensures that alternative answers do not exist, and any incorrect answers are due to model hallucinations.

For each question, we write 8 needles that each belong to the large cluster which we verify using approximate predictions. Needles that belong to the writing/retrieval cluster with >0.9 probability are considered to topically blend into the haystack. We manually write these needles to avoid data contamination.

For the 8 needles, we also vary the level of ambiguity, quantified through the following method:

1.   Using an embedding model, we compute embeddings for needle and question and their cosine similarity.
2.   Repeat across five embedding models (text-embedding-3-small, text-embedding-3-large, jina-embeddings-v3, voyage-3-large, and all-MiniLM-L6-v2).

For the PG essays topic, our needles range from 0.445-0.775 needle-question similarity with <0.1 standard deviation across the five embedding models. For the arXiv topic, we have a needle-question similarity range of 0.521-0.829, also with <0.1 standard deviation.

## Results[#](https://www.trychroma.com/research/context-rot)

We observe a clear pattern that performance degrades more quickly in input length with lower similarity needle-question pairs.

![Image 4](https://www.trychroma.com/img/context_rot/longmemeval/needle_question_sim_arxiv.png)

NIAH: Needle-Question Similarity (thinking/non-thinking modes of the same model are treated separately) - arXiv haystack/arXiv needles \n High Performance: upper 33% performance \n Blue: high-similarity needles (upper 50% similarity) \n Red: low-similarity needles (lower 50% similarity)

At short input lengths, the models perform well even on low-similarity pairs. We see this most clearly in the high/medium-performance models, demonstrating that these models are capable of succeeding at this task for all needle-question pairs.

The observed performance degradation at longer input lengths is not due to the intrinsic difficulty of the needle-question pairing. By holding the needle-question pair fixed and varying only the amount of irrelevant content, we isolate input size as the primary factor in performance decline.

We also examine whether needle position influences performance. Testing across 11 needle positions, we find no notable variation in performance for this specific NIAH task.

## Impact of Distractors[#](https://www.trychroma.com/research/context-rot)

It has already been established with older models that distractors degrade model performance and have non-uniform impact. Newer models are claimed to reliably handle any distractor, but does this hold true as input length increases?

Our experiments reveal that the impact of distractors and their non-uniformity amplifies as input length grows across models, including the latest state-of-the-art models. We also observe distinct behaviors across model families in how they deal with ambiguity.

## Experiment[#](https://www.trychroma.com/research/context-rot)

From each haystack topic (PG essays and arXiv papers), we take a needle with high needle-question similarity (second highest out of eight), and manually write 4 distractors:

> Question: "What was the best

[Showing characters 10,000-20,000 of 58,177. Call read_url with start=20000 to read the next part.]
```
**Tool result** `web_search` (id `call-87674d0f-a740-48f1-90f1-2c2988ece446`, 6,301 characters):

````
Search results for "Chroma "Context Rot" research report authors" (searched 2026-11-26):

[1] Context Rot: How Increasing Input Tokens Impacts LLM Performance | Chroma
URL: https://www.trychroma.com/research/context-rot
Excerpt: ```
@techreport{hong2025context,@techreport{hong2025context, title = {Context Rot: How Increasing Input Tokens Impacts LLM Performance}, title = {Context Rot: How Increasing Input Tokens Impacts LLM Performance}, author = {Hong, Kelly and Troynikov, Anton and Huber, Jeff}, author = {Hong, Kelly and Troynikov, Anton and Huber, Jeff}, year = {2025}, year = {2025}, month = {July}, month = {July}, institution = {Chroma}, institution = {Chroma}, url = { url = {
``` [...] Chroma Technical Report

July 14, 2025

# Context Rot: How Increasing Input Tokens Impacts LLM Performance

Kelly Hong

Anton Troynikov

Jeff Huber

Large Language Models (LLMs) are typically presumed to process context uniformly—that is, the model should handle the 10,000th token just as reliably as the 100th. However, in practice, this assumption does not hold. We observe that model performance varies significantly as input length changes, even on simple tasks. [...] McInnes, L., Healy, J., and Melville, J. (2020). UMAP: Uniform Manifold Approximation and Projection for Dimension Reduction. arXiv preprint arXiv:1802.03426. Link

[2] Behind the Research: Context Rot
URL: https://www.youtube.com/watch?v=PGMtF5PHeDI
Excerpt: # Behind the Research: Context Rot
## Channel: Chroma
10.9K subscribers
219 likes

### Description
6,764 views
Posted: 2025-07-22
Go deep behind the research with Kelly Hong and Anton Troynikov.

Chroma's latest technical report: "Context Rot" investigates how model performance grows increasingly unreliable as input length grows.

In this followup, Kelly and Anton expand on the story of how we came to work on this, surprising results, and key implications of our research. [...] ### Transcript
[0:01] Hi folks. Uh Anton here, uh co-founder of Chroma and Chroma's scientific adviser here uh with Kelly, our researcher and residents to talk about
[0:09] our long context work. Uh Kelly, why don't you give us an introduction? How long have you been at Chroma? What have you been up to?
[0:15] Yeah, I joined Chroma in January, so it's been about like six to seven months now. Um I did a project on generative benchmarking and this was the second uh [...] [32:31] See it's interesting weird. It's cuz kind It's kind of like a new jailbreak, but only if you want the model to be insane, right? Um maybe maybe the Borgs can get on that. We'll see.
[32:40] Um this like the results are really really cool. Um from such a simple benchmark, we generated really interesting model
[32:48] behaviors. Um part of our research program at Chroma is to basically deliver results that you can use, right? So the the application

[3] GitHub - chroma-core/context-rot: This repository contains the toolkit for replicating results from our technical report. · GitHub
URL: https://github.com/chroma-core/context-rot
Excerpt: If you find this work useful, please cite our technical report:

`@techreport{hong2025context, title = {Context Rot: How Increasing Input Tokens Impacts LLM Performance}, author = {Hong, Kelly and Troynikov, Anton and Huber, Jeff}, year = {2025}, month = {July}, institution = {Chroma}, url = { }` [...] Our experiments are organized under the `experiments/` folder:

Extension of Needle in a Haystack to examine the effects of needles with semantic, rather than direct lexical matches, as well as the effects of introducing variations to the haystack content.

LongMemEval task.

Tests model performance on replicating a sequence of repeated words.

Each experiment contains detailed instructions in their respective `README.md` files.

Datasets can be downloaded here. [...] This repository contains the toolkit for replicating results from our technical report.

Large Language Models (LLMs) are typically presumed to process context uniformly—that is, the model should handle the 10,000th token just as reliably as the 100th. However, in practice, this assumption does not hold. We observe that model performance varies significantly as input length changes, even on simple tasks.

Latest Models on Repeated Words Task

[4] Context Rot: Why LLMs Degrade as Context Grows (+ Fixes)
URL: https://upsolve.ai/blog/context-rot
Excerpt: 1. Chroma Research: Context Rot: How Increasing Input Tokens Impacts LLM Performance (Hong, Troynikov, Huber, July 2025). The technical report that coined the term; 18-model evaluation. 
2. Liu et al., TACL 2024: Lost in the Middle: How Language Models Use Long Contexts. Foundational study on positional degradation. 
3. Anthropic Engineering: Effective Context Engineering for AI Agents. Attention budget framing; compaction, note-taking, and subagent techniques. [...] 7. Wu et al.: LongMemEval: Benchmarking Chat Assistants on Long-Term Interactive Memory. The conversational benchmark used in Chroma's focused-vs-full experiments. 
8. LangChain: Context Engineering for Agents. Production patterns for retrieval, summarization, and context isolation. 
9. Kamradt: Needle in a Haystack: LLM Retrieval Test. The original benchmark Chroma's experiments extend. [...] Chroma's strangest result was that models performed better on shuffled haystacks than on logically coherent documents, which was a consistent pattern across all 18 models. Notably, Chroma doesn't claim to know why. The report suggests input structure may influence how attention is applied and explicitly flags the mechanism as an open question for interpretability research.

### Conversational Memory: LongMemEval

[5] The Complexity Trap: Simple Observation Masking Is as Efficient as LLM Summarization for Agent Context Management
URL: https://arxiv.org/html/2508.21433v1
Excerpt: - \ Kelly Hong, Anton Troynikov, and Jeff Huber. Context rot: How increasing input tokens impacts llm performance. Technical report, Chroma, July 2025. URL 
- \ Binyuan Hui, Jian Yang, Zeyu Cui, Jiaxi Yang, Dayiheng Liu, Lei Zhang, Tianyu Liu, Jiajun Zhang, Bowen Yu, Kai Dang, et al. Qwen2. 5-coder technical report. arXiv preprint arXiv:2409.12186, 2024.
- \ Anysphere Inc. Summarization: Context management for long conversations in chat. URL  Accessed Aug. 7, 2025.
````

## Turn 3

_Model call: 13,829 input tokens, 458 output tokens_

**Tool call** `read_url` (id `call-389d28d0-1287-47de-86c6-789bce3a31bf`):

```json
{
  "url": "https://research.trychroma.com/context-rot",
  "start": 30000
}
```
**Tool call** `web_search` (id `call-c75ffada-bc67-4d81-9929-fa23e7c8bab5`):

```json
{
  "query": "\"context rot\" Chroma study criticized methodology benchmark skepticism"
}
```
**Tool call** `web_search` (id `call-0def7b7b-becc-4c5e-aa4a-c040656e4ffa`):

```json
{
  "query": "Anton Troynikov Chroma co-founder background"
}
```
**Tool result** `read_url` (id `call-389d28d0-1287-47de-86c6-789bce3a31bf`, 10,101 characters):

```
rformance degradation with the full inputs. This performance drop suggests that adding irrelevant context, and thereby adding an additional step of retrieval, significantly impacts a model’s ability to maintain reliable performance.

## Experiment[#](https://www.trychroma.com/research/context-rot)

Given a chat history between a user and assistant, the model’s task is to answer a question relating to part of that chat history.

![Image 13](https://www.trychroma.com/img/context_rot/longmemeval/ex.png)

LongMemEval - Examples by Question Type [[2](#longmemeval-source)]

We use LongMemEval_s and filter for tasks that fall under the knowledge update, temporal reasoning, and multi-session categories. We then manually clean this dataset as some questions are too ambiguous and/or can not be answered, filtering out 38 prompts to end up with 306 total prompts. These prompts average out to ~113k tokens.

These long prompts mostly consist of content irrelevant to the question, and sometimes distractors which may seem relevant to the question. We compare performance of the models on these long prompts to a focused version, which only contains the relevant parts to answer the question.

Focused prompts average to ~300 tokens, which are derived from the originally labeled dataset and manual adjustments.

Model outputs were judged using an aligned LLM judge (GPT-4.1 with >99% alignment to human judgment).

## Results[#](https://www.trychroma.com/research/context-rot)

Across all models, we see significantly higher performance on focused prompts compared to full prompts.

![Image 14](https://www.trychroma.com/img/context_rot/longmemeval/claude.png)

LongMemEval Results - Claude Family

The Claude models exhibit the most pronounced gap between focused and full prompt performance. This discrepancy is largely driven by abstentions that arise with ambiguity, leading to model uncertainty, similar to this model family’s behavior with distractors in NIAH. This behavior is most evident in Claude Opus 4 and Sonnet 4, which appear to be particularly conservative under ambiguity, leading to lower performance on full prompts relative to that of the older Claude models.

> Question: How many days passed between the day I attended the gardening workshop and the day I planted the tomato saplings?
> 
> 
> Correct Answer: 6 days. 7 days (including the last day) is also acceptable.
> 
> 
> Model Output: I cannot determine the number of days between the gardening workshop and planting the tomato saplings becuase the specific dates for these events are not provided in the chat history.

LongMemEval - Claude Sonnet 4 (non-thinking) on full prompt containing the dates

The trend of stronger performance on focused prompts holds across the GPT, Gemini, and Qwen model families as well. For models that support thinking modes, we see notable gains on both focused and full prompts when enabled. However, we still see a performance gap between the two input lengths even with full reasoning capabilities on the latest models.

![Image 15](https://www.trychroma.com/img/context_rot/longmemeval/gpt.png)

LongMemEval Results - GPT Family

![Image 16](https://www.trychroma.com/img/context_rot/longmemeval/gemini.png)

LongMemEval Results - Gemini Family

![Image 17](https://www.trychroma.com/img/context_rot/longmemeval/qwen.png)

LongMemEval Results - Qwen Family

We also observe patterns among specific question types. In non-thinking mode, models generally perform best on knowledge-update, followed by multi-session, then temporal reasoning—for both focused and full prompts. However, when thinking is enabled, this ranking shifts to: knowledge update, temporal-reasoning, then multi-session.

![Image 18](https://www.trychroma.com/img/context_rot/longmemeval/claude_comparison.png)

LongMemEval Results by Question Type - Claude Opus 4

* * *

## Repeated Words[#](https://www.trychroma.com/research/context-rot)

Our previous experiments explore how input length alone affects model performance. But what happens when output length scales with input? Since these models are autoregressive, a model’s output also belongs to its input; each token is generated conditionally on the input and generated tokens up to that point.

Consider a basic program that repeats a string n times—it produces the same output every time. For a task this trivial, we’d expect these models to be just as reliable, and we’d like to treat them as computing systems.

However, our findings show that even for these straightforward tasks, model performance becomes non-uniform as context length, encompassing both input and output lengths, grows.

## Experiment[#](https://www.trychroma.com/research/context-rot)

We design a controlled task in which the model must replicate a sequence of repeated words, with a single unique word inserted at a specific position. The prompt explicitly instructs the model to reproduce the input text exactly.

One example prompt is:

> Simply replicate the following text, output the exact same text: apple apple apple apple **apples** apple apple apple apple apple apple apple apple apple apple apple apple apple apple apple apple apple apple apple apple

Repeated Words - Sample Prompt Containing 'apple' as the repeated word, and 'apples' as the unique word

For a given word combination, we create 1090 variations of context lengths and unique word indices:

*   Number of words: 25, 50, 75, 100, 250, 500, 750, 1000, 2500, 5000, 7500, 10000
*   Index:
    *   Every possible position for num_words <= 100
    *   Else: increments of num_words // 100

We perform this task for the following word combinations:

*   Common word: “apple” | unique word: “apples”
*   Common word: “apples” | unique word: “apple”
*   Common word: “golden” | unique word: “Golden”
*   Common word: “orange” | unique word: “run”
*   Common word: “orange” | unique word: “San Francisco”
*   Common word: “San Francisco” | unique word: “sf”
*   Common word: “Golden Gate Bridge” | unique word: “Golden Gate Park”

_Note: “San Francisco” = 1 word, “Golden Gate Bridge/Park” = 1 word_

Model configurations:

*   max_output_tokens = input_tokens *2 (up to model’s maximum output token limit, which is typically lower for older models)
*   temperature = 0
*   thinking = max(0, minimum_thinking_budget)

We account for reasoning models by either setting their thinking budgets to 0 or the minimum value, such as 128 tokens for Gemini 2.5 Pro. We exclude OpenAI’s o3 as it does not support token-based thinking budgets and cannot be configured with a fixed output length, which is essential for maintaining consistency across evaluations.

Scores are calculated by normalized Levenshtein distance.

We encounter cases of models not attempting the task, which we determine by:

*   Empty outputs with a stop reason (i.e. finish_reason='content_filter’ for GPT-3.5 turbo)

*   Non-empty outputs, but with invalid outputs:

*   Pure observations with no attempt:

> I notice there's a discrepancy in the text. The word "apples" appears once in the original text (instead of "apple"), located in what appears to be around line 89 or 90 of the text block. Since you asked me to replicate the exact same text, I should point out this difference. Would you like me to:
> 
> 
> 1.   Replicate it exactly as shown (with the one instance of "apples")
> 2.   Correct it to "apple" to match the pattern
> 3.   Simply proceed with replicating it exactly as is Please let me know how you'd like me to proceed.

Repeated Words - Claude Opus 4 output

*   Refusals to answer:

> I’m sorry, but I can’t help with that

Repeated Words - GPT-4.1 output

*   Random outputs:

> -\n-\n--\n-\n-\n-\n-\n-\n-\n-\n-\n-\n-\n-\n-...

Repeated Words - Gemini 2.5 Pro output

We exclude such cases, and separately note the percentage of refusals and common patterns in our results. We only include cases in which the task was attempted, including cases with starting phrases such as:

> I notice there's a discrepancy in the text. At one point, "apple" changes to "apples" (with an 's'). I'll replicate the text exactly as provided:
> 
> 
> apple apple apple apple apple apple apple apple apple...

Repeated Words - Claude Opus 4 output

With these instances, we use the same scoring process to slightly penalize the model for not following exact instructions.

We exclude GPT-3.5 turbo entirely since the model refused to generate an output for 60.29% of tasks due to finish_reason='content_filter’.

We analyze outputs along several dimensions:

*   Normalized Levenshtein distance

*   Presence and position of unique word

    *   Correct: Unique word is present and appears at the correct index
    *   Incorrect position: Unique word appears, but at the wrong index

*   Word count difference (number of words in input - number of words generated)

## Results[#](https://www.trychroma.com/research/context-rot)

As context length increases, performance consistently degrades across all models. In this experiment, input length is directly proportional to output length, unlike our previous tests in which output length remained relatively fixed at a short length. This setting allows us to assess the models’ ability to reliably reproduce long sequences.

We also observe patterns where models do not attempt the task, which appears across all model families.

![Image 19](https://www.trychroma.com/img/context_rot/repeated_words/claude_line_plot.png)

Repeated Words - Claude Family

We observe that Sonnet 3.5 (red) outperforms the newer Claude models up to its maximum output token count of 8192. Opus 4 (blue), while exhibiting the slowest degradation rate, is also the only model in this family to refuse the task (2.89% of attempts).

A common pattern with Opus 4 is that the model makes an observation before deciding whether to proceed, followed by an attempt or no attempt. This behavior typically arises starting from 2500 words.

There are also cases where Opus 4 simply refuses to attempt the task due to:

1.  

[Showing characters 30,000-40,000 of 58,177. Call read_url with start=40000 to read the next part.]
```
**Tool result** `web_search` (id `call-c75ffada-bc67-4d81-9929-fa23e7c8bab5`, 6,956 characters):

```
Search results for ""context rot" Chroma study criticized methodology benchmark skepticism" (searched 2026-11-26):

[1] Context Rot: How Long Inputs Degrade LLM Accuracy in 2026 | TinyFish Blog
URL: https://www.tinyfish.ai/blog/context-rot
Excerpt: Chroma researchers Kelly Hong, Anton Troynikov and Jeff Huber formalized the term in a technical report published in July 2025. Their design is what makes it credible: they held task complexity constant and varied only input length. Most long-context benchmarks fail here, because longer inputs usually mean harder questions too. Their conclusion was blunt. Models don't use their context uniformly, and performance grows increasingly unreliable as input length grows. [...] One more correction, because most coverage of Chroma's report misses it. Rot is usually described as a session-length problem: run long enough, accumulate enough turns, quality decays. Length is real, but it's a proxy. Two of Chroma's four experiments varied the content of the input rather than its size, and both moved the results. Rot is what happens when the signal-to-noise ratio of your input falls. Length is just the most common way that ratio falls, which puts the lever in your retrieval [...] Chroma, which builds an open-source retrieval database, found it in all 18 models it tested. Most coverage stops at that headline and blames session length, but Chroma's four controlled needle experiments say otherwise: every one varied what sat inside the input, not just how much.

Below we cover the mechanism behind context rot, the symptoms to watch for in production, what noisy input costs you, and five techniques that prevent it.

## What Is Context Rot?

[2] Context Rot: Why LLMs Degrade as Context Grows (+ Fixes)
URL: https://upsolve.ai/blog/context-rot
Excerpt: Most long-context benchmarks accidentally conflate input length with task difficulty (longer inputs usually mean harder problems). Chroma's methodology held task complexity constant and varied only input length, which lets you attribute the performance drop to length alone.

Four experiments stand out.

### Needle in a Haystack, Made Realistic [...] Chroma extended the test to semantic matches, where the model must connect a question to an answer phrased differently. Performance dropped as context grew, and low-similarity needle-question pairs degraded fastest. Real-world queries are almost always semantic, not lexical, which means the benchmark your vendor quotes is the easy version of the problem you actually have.

### Distractors Amplify the Damage [...] Chroma's strangest result was that models performed better on shuffled haystacks than on logically coherent documents, which was a consistent pattern across all 18 models. Notably, Chroma doesn't claim to know why. The report suggests input structure may influence how attention is applied and explicitly flags the mechanism as an open question for interpretability research.

### Conversational Memory: LongMemEval

[3] Medium
URL: https://cobusgreyling.medium.com/llm-context-rot-28a6d0399655
Excerpt: ## The Chroma “Context Rot” study reveals that simply increasing input length & maximising token windows doesn’t deliver linearly improving accuracy. Instead, LLM performance degrades unevenly & often unpredictably as contexts grow, underscoring the limitations of relying on sheer scale over thoughtful context engineering.

Cobus Greyling

## In Short

Chroma’s recent study evaluated 18 leading large language models (LLMs), including cutting-edge ones like GPT-4.1, Claude 4, Gemini 2.5 & Qwen3. [...] Source

Fast forward to 2025, and a study from Chroma coins the term “Context Rot”…

Before we get into Context Rot…overall, the study provides useful insights into LLM limitations, its origins warrant scrutiny.

If long contexts prove detrimental as claimed, it bolsters Chroma’s RAG ecosystem; if not, it could be seen as marketing spin.

For a balanced view, some cross-referencing might be prudent…

[4] Chroma research on "context rot" in LLMs and potential solutions | Marty Swant posted on the topic | LinkedIn
URL: https://www.linkedin.com/posts/martinswant_interesting-research-from-chroma-on-a-problem-activity-7355282633104232448-vcEg
Excerpt: 📍 Does more context really mean better answers? Not always. A research published from Chroma shows that while today's LLMs can handle millions of input tokens, their performance doesn’t scale linearly with context length. Most benchmarks, like Needle in a Haystack (NIAH), test only simple word-matching - and models ace them. But real-world tasks require semantic understanding, handling ambiguity, and resisting distractors. Even when tasks stay simple, performance drops sharply as input grows [...] use their context uniformly; instead, their performance grows increasingly unreliable as input length grows. 📢 Table Of Contents ▶️ How Do Transformers Work? ▶️ Problems With Benchmarking ▶️ Needle in a Haystack Extension ▶️ Haystack Structure ▶️ Other Experiments ▶️ Conclusion #AI #LLM #LLMs #Contextengineering #prompting #promptengineeering #Artificialintelligene #AIagents #agenticAI [...] Large Language Models (LLMs) are presumed to process context uniformly—that is, the model should handle the 10,000th token just as reliably as the 100th. However, in practice, this assumption does not hold. We observe that model performance varies significantly as input length changes, even on simple tasks. In this report, we evaluate 18 LLMs, including the state-of-the-art GPT-4.1, Claude 4, Gemini 2.5, and Qwen3 models. Our results reveal that models do not use their context uniformly;

[5] Context Rot: How Increasing Input Tokens Impacts LLM Performance | Chroma
URL: https://www.trychroma.com/research/context-rot
Excerpt: However, NIAH is fundamentally a simple retrieval task, in which a known sentence (the “needle”) is placed in a long document of unrelated text (the “haystack”), and the model is prompted to retrieve it. While scalable, this benchmark typically assesses direct lexical matching, which may not be representative of flexible, semantically oriented tasks. [...] In order to answer this question, the model would first have to know that Kiasma museum is located in Helsinki, then make that latent association link. This tests the model not only for its non-lexical matching abilities, but also for its world knowledge. 72.4% of needle-question pairs from NoLiMa require such external knowledge, making this benchmark closer to a test of how models handle both tasks at once rather than pure non-lexical matching alone. [...] In typical NIAH setups, haystacks are concatenations of coherent texts, each with their own logical flow of ideas. For instance, the original NIAH benchmark uses a series of Paul Graham essays, where each essay follows a structured organization of ideas to form an argument. To evaluate whether this structure influences model performance, we compare two conditions:
```
**Tool result** `web_search` (id `call-0def7b7b-becc-4c5e-aa4a-c040656e4ffa`, 5,772 characters):

```
Search results for "Anton Troynikov Chroma co-founder background" (searched 2026-11-26):

[1] Anton Troynikov | Lighthouse Success Stories
URL: https://www.lighthousehq.com/customers/anton-troynikov
Excerpt: Anton Troynikov is the co-founder and head of technology at Chroma. “While I was born in Ukraine, I grew up in Australia and I lived several years in Germany, so I’m from here and there,” he says. Traditional software handles structured data in SQL tables. What AI adds is the ability to work with unstructured data through plain language, addressing it by meaning. “That’s what Chroma does. Chroma is the AI application database.” [...] The pull toward this work started early. As a kid he watched space shuttle launches on TV and felt a draw to be there, before he even knew where there was. He went to grad school at the Technical University of Munich for robotics, which he describes as applied math and computer science, because he could see it was what came next on the frontier of technology.

[2] Chroma’s Vector Database with Anton Troynikov - Software Engineering Daily
URL: https://softwareengineeringdaily.com/podcasts/chromas-vector-database-with-anton-troynikov
Excerpt: # Chroma’s Vector Database with Anton Troynikov

Chroma’s Vector Database with Anton Troynikov

Chroma is an open-source AI application database.

Anton Troynikov is a Founder at Chroma. He has a background in computer vision and previously worked at Meta. In this episode Anton speaks with Sean Falconer about Chroma, and the goal of building the memory and storage subsystem for the new computing primitive that AI models represent. [...] Sean’s been an academic, startup founder, and Googler. He has published works covering a wide range of topics from information visualization to quantum computing. Currently, Sean is Head of Marketing and Developer Relations at Skyflow and host of the podcast Partially Redacted, a podcast about privacy and security engineering. You can connect with Sean on Twitter @seanfalconer.

Please click here to see the transcript of this episode.

[3] Chroma’s Vector Database with Anton Troynikov
URL: https://www.youtube.com/watch?v=4KNOQqdsOuQ
Excerpt: Anton Troynikov is a Founder at Chroma. He has a background in computer vision and previously worked at Meta. In this episode Anton speaks with Sean Falconer about Chroma, and the goal of building the memory and storage subsystem for the new computing primitive that AI models represent.

⌚Timestamps:

00:00  Introduction and Background 
00:39  Interview

👍🏼 Give your thumbs-up and subscribe to the channel!

🎙️ Check out more of our podcasts 
 

Twitter    / software_daily [...] ### Transcript
[0:00] chroma is an open-source AI application database Anton trov is a Founder at chroma he has a background in computer
[0:08] vision and previously worked at meta in this episode Anton speaks with Shan Falconer about chroma and the goal of building the memory and storage
[0:16] subsystem for the new Computing primitive that AI models represent this episode is hosted by Sha Falconer check the show notes for more
[0:24] information on Sean's work and where to find him [...] [1:24] spent seven years in machine perception which is a domain of Applied AI where you get computers to understand the world and we learned a lot of lessons there about you know building actual
[1:32] Engineering Systems around Ai and around machine learning and we basically founded the company on the principle that there wasn't any good engineering

[4] Anton Troynikov - CEO - American Terawatt - LinkedIn
URL: https://www.linkedin.com/in/antontroynikov
Excerpt: ## Experience
- CEO at American Terawatt (Feb 2025 to present)
- Advisor at Chroma (Feb 2025 to present)
- Founder & CTO at Chroma (Sep 2022 to Feb 2025)
- Research Engineer - FRL Research at Facebook (Jun 2020 to Jun 2022)
- Software Engineer - Perception at Nuro (Sep 2018 to Jan 2020)
- Researcher - Computer Vision at Technical University Munich (Jan 2018 to Sep 2018) [...] ## Education
- Technical University of Munich, Master’s Degree, Robotics
- University of Melbourne, Bachelor of Engineering / Bachelor of Economics, Computer Engineering

## Skills
3d reconstruction, technical lead, google spreadsheets, support, flow, computing, productivity, user interface, formula student, drone operation, pose estimation, retail pos, estimation, see, production

[5] Anton Troynikov: Bio, Work & Ideas | AI Engineer
URL: https://ai.engineer/speakers/anton-troynikov
Excerpt: Anton Troynikov is co-founder and chief executive of American Terawatt, which develops high-voltage direct-current transmission infrastructure for industrial electricity users, including AI data centers. He previously co-founded Chroma, the open-source AI application database, tackling two essential constraints on AI: useful information and reliable power. [...] With Jeff Huber, he founded Chroma to give AI developers an open-source embedding database capable of storing, retrieving, and updating application-specific information. His earlier Stable Attribution project explored identifying training images that influenced generated pictures, potentially enabling creator attribution and compensation; missing information about the artists behind training-image URLs remained a fundamental obstacle. He explored those challenges in an interview on [...] Born in Ukraine and raised in Australia, Troynikov studied computer engineering and economics at the University of Melbourne, pursued graduate robotics studies at the Technical University of Munich, interned at Google, and co-founded Geddit in Berlin. He subsequently worked in robotics and computer vision, including vehicle-camera mapping, collaborative-robot perception, and engineering at Iris Automation.
```

## Turn 4

_Model call: 19,423 input tokens, 349 output tokens_

**Tool call** `read_url` (id `call-51ea9c04-eeda-46d9-a2a6-4dfb8e7ff842`):

```json
{
  "url": "https://research.trychroma.com/context-rot",
  "start": 20000
}
```
**Tool call** `web_search` (id `call-5a1879f7-90f5-4166-9eae-7256b8ef97d4`):

```json
{
  "query": "\"Kelly Hong\" Chroma researcher machine learning background"
}
```
**Tool call** `web_search` (id `call-ece34cf2-564a-4b91-957d-e4f4f6d7cb71`):

```json
{
  "query": "Chroma \"about\" company vector database Jeff Huber CEO trychroma research team"
}
```
**Tool result** `read_url` (id `call-51ea9c04-eeda-46d9-a2a6-4dfb8e7ff842`, 10,101 characters):

```
 writing advice I got from my college classmate?"
> 
> 
> Needle: "I think the best writing tip I received from my college classmate was to write every week."
> 
> 
> Distractors:
> 
> 
> *   "The best writing tip I received from my college professor was to write everyday."
> 
> *   "The worst writing advice I got from my college classmate was to write each essay in five different styles."
> 
> *   "The best writing advice I got from my classmate was to write each essay in three different styles, this was back in high school."
> 
> *   "I thought the best writing advice I got from my college classmate was to write each essay in four different styles, but not anymore."

Distractors for Paul Graham Essay Topic & Needle with High Needle-Question Similarity

Instead of testing all eight needles with distractors, we use one needle with high needle-question similarity to create a condition in which the needle should be relatively easy to identify. We see from previous results that models generally perform well on this needle across input lengths due to high needle-question similarity, which allows us to better isolate and measure the impact of distractors alone.

We run three test conditions:

*   No distractors (baseline): Needle only
*   Single distractor: Needle + one distractor (randomly positioned)
*   Multiple distractors: Needle + all four distractors, randomly positioned throughout the haystack

![Image 5](https://www.trychroma.com/img/context_rot/niah/distractors_var.png)

Impact of Distractors - Three Conditions

## Results[#](https://www.trychroma.com/research/context-rot)

Even a single distractor reduces performance relative to the baseline (needle only), and adding four distractors compounds this degradation further.

![Image 6](https://www.trychroma.com/img/context_rot/niah/distractors_num.png)

Impact of Distractors: Performance by Number of Distractors - arXiv haystack/PG essay needles

We are also able to see that distractors do not have uniform impact. For example, in our arXiv haystack and PG essay needle combination, we can see that distractor 3 (red) causes greater performance decline relative to the other distractors.

![Image 7](https://www.trychroma.com/img/context_rot/niah/distractors_ind.png)

Impact of Distractors: Performance by Individual Distractors - arXiv haystack/PG essay needles

To further investigate this non-uniform impact, we analyze the failed attempts of various models in the 4-distractor condition. For the arXiv haystack and PG essay needle combination, we see that distractors 2 and 3 appear most frequently in hallucinated responses across models.

![Image 8](https://www.trychroma.com/img/context_rot/niah/hallucinations.png)

Impact of Distractors: Failure Analysis - arXiv haystack/PG essay needles

These failures also reveal model-specific differences in handling ambiguity. Claude models consistently exhibit the lowest hallucination rates. Specifically, Claude Sonnet 4 and Opus 4 are particularly conservative and tend to abstain when uncertain, explicitly stating that no answer can be found. In contrast, GPT models show the highest rates of hallucination, often generating confident but incorrect responses when distractors are present.

* * *

## Needle-Haystack Similarity[#](https://www.trychroma.com/research/context-rot)

In long-context tasks, irrelevant context is often treated as a neutral placeholder to scale up input length. It’s typically assumed that the content of this irrelevant context doesn't matter, as long as it doesn’t directly interfere with the task.

However, a natural question arises: does the needle-haystack similarity influence task difficulty at all? Intuitively, if the needle blends in with the content of the haystack, the model may have greater difficulty in extracting the needle.

Our findings reveal that needle-haystack similarity has a non-uniform effect on model performance.

## Experiment[#](https://www.trychroma.com/research/context-rot)

Using the needles from our needle-question similarity experiment, we set up our experiment to test the impact of needle-haystack similarity.

We measure needle-haystack similarity by embedding the haystack and retrieving the top five most similar chunks for each needle, then averaging their cosine similarity scores. This process is repeated across five different embedding models for robustness.

In the PG essay haystack, PG essay needles have an average needle-haystack similarity score of 0.529 with a variation of 0.101, while arXiv needles average 0.368 needle-haystack similarity with a variation of 0.111. Conversely, in the arXiv haystack, arXiv needles average 0.654 needle-haystack similarity with a variation of 0.0858, whereas PG-essay needles score lower at 0.394 needle-haystack similarity with a variation of 0.105.

On each haystack, we test semantically similar needles against unrelated needles. For instance, we place both PG essay and arXiv needles within a Paul Graham essay haystack to compare the two conditions:

![Image 9](https://www.trychroma.com/img/context_rot/niah/needle_haystack.png)

Needle-Haystack Similarity: Experimental Setup

## Results[#](https://www.trychroma.com/research/context-rot)

We test both PG essay and arXiv needles in two haystack types: Paul Graham essays and arXiv papers. In the Paul Graham essay haystack, arXiv needles perform significantly better relative to the PG essay needles; in other words, models perform better when the needle does not semantically blend in with its haystack. In the arXiv haystack, however, we observe only minimal performance differences between our arXiv and PG essay needles.

![Image 10](https://www.trychroma.com/img/context_rot/niah/needle_haystack_2.png)

Needle-Haystack Similarity Results

Testing across only two topics is insufficient to draw a generalizable conclusion that higher needle-haystack similarity degrades model performance on this task. This does highlight, however, the non-uniform nature of long-context processing. Even when task structure and needle-question similarity are held constant, changing the semantic similarity between the needle and the haystack can influence results. This points to an underexplored area in long-context benchmarks and a meaningful direction for future research.

## Haystack Structure[#](https://www.trychroma.com/research/context-rot)

Aside from needle-haystack similarity, we also consider the structural pattern of the haystack.

If the haystack is composed of coherent essays, a randomly inserted needle may disrupt the logical flow of ideas, making it more noticeable. In contrast, in a shuffled haystack of randomly ordered sentences, the needle may blend in more easily since the overall context lacks structure. This follows the assumption that models are sensitive to the logical flow of context—processing it in a structured, order-sensitive manner.

Surprisingly, we find that structural coherence consistently hurts model performance.

Although it seems counterintuitive, models perform worse when the haystack preserves a logical flow of ideas. Shuffling the haystack and removing local coherence consistently improves performance.

## Experiment[#](https://www.trychroma.com/research/context-rot)

To assess the impact of haystack structure, we create two variants:

1.   Original: preserves the natural flow of ideas within each excerpt
2.   Shuffled: sentences are randomly reordered throughout the haystack to maintain the same overall topic but without logical continuity

![Image 11](https://www.trychroma.com/img/context_rot/niah/nh2.png)

Haystack Structure: Sample Experimental Setup

## Results[#](https://www.trychroma.com/research/context-rot)

Across all 18 models and needle-haystack configurations, we observe a consistent pattern that models perform better on shuffled haystacks than on logically structured ones.

![Image 12](https://www.trychroma.com/img/context_rot/niah/structure_2.png)

Haystack Structure: Averaged Performance Across 18 Models for Original vs Shuffled Haystacks

These results may have some implications for the model’s internal processing: structural patterns of inputs could influence how the attention mechanism is applied, particularly as input length increases.

While out of scope for this report, this points to a potential direction for interpretability research in how attention is influenced by input structure. Understanding these structural influences that arise with increased input length could help explain these long context failure patterns.

## LongMemEval[#](https://www.trychroma.com/research/context-rot)

To evaluate these models in a more realistic setting, we use LongMemEval, a long-context benchmark for conversational question-answering.

Using long inputs for chat assistants is a common approach for maintaining relevant history for subsequent chats. To incorporate “memory” into a chat assistant, a naive approach would be to include the full chat history into the prompt for following chats. This requires the model to perform two tasks, typically performed in one call: find relevant parts of the conversation history (retrieval), then synthesize them in a way that is useful to an incoming query (reasoning).

In an ideal case, the model would be given only the relevant parts so it can focus solely on reasoning. Adding irrelevant context adds the additional step of identifying what is relevant, forcing the model to perform two tasks simultaneously.

We systematically test the effect of adding this additional step with increased input length through two conditions:

1.   Focused input, containing only the relevant parts and so the model just has to do simple reasoning.

2.   Full input, which utilizes the full 113k token LongMemEval input that includes irrelevant context. In this case, the model has to perform retrieval across the long context in addition to reasoning.

We verify that the models are highly capable of succeeding on the focused inputs, then observe consistent pe

[Showing characters 20,000-30,000 of 58,177. Call read_url with start=30000 to read the next part.]
```
**Tool result** `web_search` (id `call-5a1879f7-90f5-4166-9eae-7256b8ef97d4`, 6,054 characters):

```
Search results for ""Kelly Hong" Chroma researcher machine learning background" (searched 2026-11-26):

[1] Kelly Hong | TWIML - The Voice of Machine Learning & AI
URL: https://twimlai.com/network/kelly-hong
Excerpt: Kelly Hong is a researcher at Chroma, where she explores open questions in retrieval. She studied computer science at UC Berkeley before deciding to take a break from school to go all in on working in this space. Her recent work includes projects like generative benchmarking, driven by the motivation to help developers systematically evaluate and improve their AI systems.

[2] Context Rot: How Increasing Input Tokens Impacts LLM Performance (MLOps Community Reading Group) - Video | Agentic AI Foundation
URL: https://home.mlops.community/public/videos/context-rot-reading-group
Excerpt: Kelly Hong is a researcher at Chroma, where she explores open questions in retrieval. She studied computer science at UC Berkeley before deciding to take a break from school to go all in on working in this space. Her recent work includes projects like generative benchmarking, driven by the motivation to help developers systematically evaluate and improve their AI systems.

+ Read More

user's Avatar

Adam Becker

IRL @ MLOps Community [...] Kelly Hong [00:04:27]: Yeah, yeah, sounds good. Let me just share my screen. I just have like one visual to reference so see facing some trouble. Wait, I'll just present and then we can do the mirror board later. But yes. So I'm Kelly, I'm a researcher at chroma. As Arthur mentioned, we're a vector database company so we work on retrieval for AI. But we also work on a lot of research on the side as well. [...] Agentic AI Foundation

Agentic AI Foundation Logo

Sign in

Sign in or Join the community to continue

# Context Rot: How Increasing Input Tokens Impacts LLM Performance (MLOps Community Reading Group)

PostedSep 01, 2025| Views344

# Context Windows

# LLMs

# Prompt Engineering

## Speakers

user's Avatar

Kelly Hong

Researcher @ Chroma

[3] Generative Benchmarking: Measuring AI Models Beyond Accuracy [Kelly Hong] - 728
URL: https://www.youtube.com/watch?v=3kbiGPn0cOo
Excerpt: [1:23] research at Chroma. We're a company working on vector databases but we also work on research around retrieval as well. Um just to give a little bit more
[1:31] background about myself I started my undergrad at uh UC Berkeley around 3 years ago studying CS. Um about two
[1:39] years in I got pretty interested in the space and like search and retrieval. So then I spend some time like building projects around it, going deeper into [...] [2:06] So I'm on a gap year right now um from school and working here like basically full-time. Uh and Chroma does come up uh
[2:14] particularly in a context of vector databases and rag and uh rag continues to be a topic of interest for folks
[2:24] listening to the podcast and the folks that I talk to in enterprises. So I think this will be an interesting conversation in that light as well. Uh [...] [1:46] the research and I would come across Chromma a lot because um like I would use it in my projects but I also saw that they did a lot of good research
[1:54] around like chunking strategies like embedding adopters just ways to make your retrieval system better. So I got pretty interested in Chroma specifically
[2:02] and then I started talking to the team got this opportunity and now I'm here.

[4] Kelly Hong - Research @ Epoch AI - LinkedIn
URL: https://www.linkedin.com/in/kellyshong
Excerpt: # Kelly Hong

Headline: CS & DS @ UC Berkeley | Director @ Free Ventures
Current role: Researcher
Seniority: Specialist, Research
Location: San Francisco Bay Area United States
Experience: 1 year 9 months
LinkedIn:  · 1,229 followers
Description: research.trychroma.com

## Experience
- Researcher at Epoch AI (Aug 2026 to present)
- Researcher at Chroma (Jan 2025 to Jun 2026)
- Resident at Founders, Inc. (Jun 2024 to Aug 2024)
- Resident (Chapter 3) at The Residency (May 2024 to Aug 2024) [...] ## Recent Activity
- Reposted: Introducing Harness-1, a 20B search agent trained with a state-externalizing harness. > frontier-level long-horizon search, rivaling...
- Shared: We trained a 20b model specialized in agentic search. Check out our technical report! We're releasing Chroma Context-1, a 20B parameter...
- Reposted: I had a fun time writing a deep dive on Diffusion Language Models - with an equation walkthrough and Excalidraw sketches ✏️ In Part 1, I... [...] ## Education
- University of California, Berkeley, BA Computer Science

[5] Kelly Hong
URL: https://linkedin.com/in/kelly-hong-9b03ba1b1
Excerpt: # Kelly Hong
Epoch AI
San Francisco Bay Area, US  
500 connections, 1259 followers

## About
research<br><br>trychroma<br><br>com

## Experience
N/A

## Education
### University of California, Berkeley  
N/A  
2022-08 - 2026-05  
None

## Publications
N/A

## Honors & Awards
The Leadership Award
Cal Alumni Association • September 2023

## Certifications
N/A

## Volunteering
N/A

## Languages
N/A

## Organizations
N/A [...] - Introducing Harness-1, a 20B search agent trained with a state-externalizing harness. > frontier-level long-horizon search, rivaling Opus-4.6 and outperforming GPT-5.4 > Context-1-level cost and latency > externalizes candidates, evidence, verification, and search history > open-source X:  Paper 📄:  Code 💻:  Model 🤗:  Huge thanks to Chroma for fully supporting this work, and to Thinking Machines Lab for the training infra! My awesome collaborators: Zhiyi Shi , Kelly Hong , Hammad Bashir , [...] - After an incredible year at Biohub , I’ve joined OpenAI full-time as a researcher, continuing my work at the intersection of AI and biology. I’m deeply grateful to everyone at Biohub for the opportunity to learn, collaborate, and contribute alongside such exceptional scientists and engineers. This is a pivotal moment for both AI and the life sciences. As reasoning models become increasingly capable, I’m excited to help advance AI systems that can accelerate biological discovery while ensuring
```
**Tool result** `web_search` (id `call-ece34cf2-564a-4b91-957d-e4f4f6d7cb71`, 6,428 characters):

```
Search results for "Chroma "about" company vector database Jeff Huber CEO trychroma research team" (searched 2026-11-26):

[1] Jeff Huber
URL: https://linkedin.com/in/jeffchuber
Excerpt: # Jeff Huber

Headline: founder
Current role: CEO & Founder
Seniority: Founder, General Management
Location: San Francisco, California, United States
Experience: 13 years
LinkedIn: www.linkedin.com/in/jeffchuber · 7,362 followers
Description: Chroma is the leading AI-native open-source vector database www.trychroma.com/ github.com/chroma-core/chroma twitter.com/trychroma discord.gg/MMeYNTmh3x [...] ## Experience
- CEO & Founder at Chroma (Sep 2022 to present)
- CEO & Cofounder at Standard Cyborg (Jan 2014 to Jan 2021)
- Head of Product at MightyHive (Jan 2013 to Jan 2014)
- Full Stack Engineer at MightyHive (Jan 2013 to Jan 2013)
- CEO & Cofounder at Knowit (Jan 2011 to Jan 2012)

## Education
- North Carolina State University, BS, Industrial Engineering, Economics

[2] Chroma's Jeff Huber on Vector Databases and Getting AI into Production
URL: https://www.madrona.com/chromas-jeff-huber-on-vector-databases-and-getting-ai-into-production
Excerpt: This week, Vivek Ramaswami talks with Chroma Co-founder and CEO Jeff Huber. Chroma is an open-source vector database, and vector databases have taken the AI world by storm recently, with Chroma quickly emerging as one of the leading offerings in the space. Jeff’s background is in machine learning, and for him and his co-founder, starting Chroma was a classic “there has to be a better way moment when it comes to going from demo to production”. Vivek and Jeff talk about why on earth we need [...] > The 2023 Intelligent Applications Summit is happening on October 10th and 11th. If you’re interested, request an invite here.

This transcript was automatically generated and edited for clarity.

Vivek: I’m Vivek Ramaswami. I’m a partner at Madrona, and today, I am joined by Jeff Huber. Jeff is the co-founder and CEO of Chroma, an AI-native open-source embeddings database, which is also more commonly known as vector databases. Jeff, thanks so much for joining us today. [...] team. We still are, to this day, a very small team. That will remain true for probably some time, honestly, into the future. With a small team, you can only do so many things. And the thing that we chose to focus on was trying to serve our users to developers. They use Chroma. Trying to serve them as best as possible, take their feedback seriously, give them help on Discord as fast as possible.

[3] Jeff Huber: Bio, Work & Ideas | AI Engineer
URL: https://ai.engineer/speakers/jeff-huber
Excerpt: Jeff Huber is the co-founder and chief executive of Chroma, the company behind ChromaDB, an open-source database and search infrastructure for AI applications. He builds systems that help models retrieve useful information, evaluate whether that information actually answers users’ questions, and preserve organizational knowledge for AI agents. [...] Huber studied economics and industrial engineering at North Carolina State University before leaving to launch a startup. He worked in software engineering and product leadership and co-founded Standard Cyborg, a computer-vision company, before founding Chroma with Anton Troynikov. Chroma raised an $18 million seed round in 2023 and expanded from a locally installable vector database into cloud infrastructure and shared knowledge systems.

Loading more talks and highlights…

[4] Chroma CEO, Founder, Key Executive Team, Board of Directors & Employees
URL: https://www.cbinsights.com/company/chroma-6/people
Excerpt: Chroma company logo

# Chroma

trychroma.com

## Executives

3

# Chroma Management Team

## 3 Team Members

Chroma has 3 executives. Chroma's current CEO & Founder is Jeffrey C. Huber.

| Name | Work History | Title | Status |
------|
| Jeffrey C. Huber |  | CEO & Founder | Current |

| Name | Jeffrey C. Huber |  |  |
------|
| Work History |  |  |  |
| Title | CEO & Founder |  |  |
| Status | Current |  |  |

Start free trialNew call-to-actionNew call-to-action [...] Weaviate develops artificial intelligence (AI) databases, focusing on a vector database for AI applications. It provides a platform including a vector database, natural language query agent, and tools for creating AI experiences, aimed at building AI-native applications. It serves sectors requiring AI capabilities, including startups, scale-ups, and enterprises across various industries. It was formerly known as SeMi Technologies. It was founded in 2019 and is based in Amsterdam, Netherlands. [...] Qdrant is a company that focuses on vector similarity search technology within the AI and data processing sectors. Its main offerings include a vector database designed to handle high-dimensional data, enabling applications such as matching, searching, and recommending. Qdrant's products cater to various use cases, including search, recommendation systems, retrieval augmented generation, data analysis, anomaly detection, and AI agents. It was founded in 2021 and is based in Berlin, Germany.

[5] Context Engineering, Context Rot, & Agentic Search with the CEO of Chroma, Jeff Huber - Video | Agentic AI Foundation
URL: https://home.mlops.community/public/videos/context-engineering-context-rot-and-agentic-search-with-the-ceo-of-chroma-jeff-huber
Excerpt: Jeff Huber [00:06:08]: As a result, these sort of things are very obviously correlated problem to be solved. People want to buy, they want to solve the problem of information retrieval broadly. And of course, dense vector search happens to be one useful tool in the toolbox. We'll unpack in a second. Why, but certainly not a panacea to all of your search problems. And we've never claimed that it is either. The way that I kind of describe what chroma is then is that it's not a vector database. [...] a vector database. What we're building is modern search infrastructure for AI, or maybe modern retrieval infrastructure for AI. [...] Jeff Huber [00:05:45]: Yeah, maybe like a quick sort of addendum to that. Like there's this term that's been thrown around now for a few years, like vector database. And we've always thought that that's like a dumb term. These are just like VCs trying to like meme a category of enterprise software as they do. Right. But like that's not actually a. The problem to be solved. And that's actually also not what developers really actually want to buy.
```

## Turn 5

_Model call: 24,918 input tokens, 508 output tokens_

**Tool call** `web_search` (id `call-a750d317-3747-4390-88d7-1f835364a0c2`):

```json
{
  "query": "\"Lost in the Middle\" Liu TACL 2024 long context performance degrades middle"
}
```
**Tool call** `web_search` (id `call-e9459691-082c-440e-bd36-6b50f50148bc`):

```json
{
  "query": "arxiv paper cites \"context rot\" Hong Troynikov Huber Chroma 2025 long context degradation replication"
}
```
**Tool call** `read_url` (id `call-54eee976-a01a-4594-ab57-abfa075cc29f`):

```json
{
  "url": "https://research.trychroma.com/",
  "start": 0
}
```
**Tool result** `web_search` (id `call-a750d317-3747-4390-88d7-1f835364a0c2`, 6,242 characters):

```
Search results for ""Lost in the Middle" Liu TACL 2024 long context performance degrades middle" (searched 2026-11-26):

[1] Lost in the Middle: How Language Models Use Long Contexts | Transactions of the Association for Computational Linguistics | MIT Press
URL: https://direct.mit.edu/tacl/article/doi/10.1162/tacl_a_00638/119630/Lost-in-the-Middle-How-Language-Models-Use-Long
Excerpt: not robustly make use of information in long input contexts. In particular, we observe that performance is often highest when relevant information occurs at the beginning or end of the input context, and significantly degrades when models must access relevant information in the middle of long contexts, even for explicitly long-context models. Our analysis provides a better understanding of how language models use their input context and provides new evaluation protocols for future long-context [...] Changing the location of relevant information (in this case, the position of the passage that answers an input question) within the language model’s input context results in a U-shaped performance curve—models are better at using relevant information that occurs at the very beginning (primacy bias) or end of its input context (recency bias), and performance degrades significantly when models must access and use information located in the middle of its input context. [...] The effect of changing the position of relevant information (document containing the answer) on multi-document question answering performance. Lower positions are closer to the start of the input context. Performance is highest when relevant information occurs at the very start or end of the context, and rapidly degrades when models must reason over information in the middle of their input context.

Close Figure 5:

[2] [2307.03172] Lost in the Middle: How Language Models Use Long Contexts
URL: https://arxiv.org/abs/2307.03172
Excerpt: models do not robustly make use of information in long input contexts. In particular, we observe that performance is often highest when relevant information occurs at the beginning or end of the input context, and significantly degrades when models must access relevant information in the middle of long contexts, even for explicitly long-context models. Our analysis provides a better understanding of how language models use their input context and provides new evaluation protocols for future [...] > Abstract:While recent language models have the ability to take long contexts as input, relatively little is known about how well they use longer context. We analyze the performance of language models on two tasks that require identifying relevant information in their input contexts: multi-document question answering and key-value retrieval. We find that performance can degrade significantly when changing the position of relevant information, indicating that current language models do not [...] ## Submission history

From: Nelson F. Liu 

[view email]

Thu, 6 Jul 2023 17:54:11 UTC (410 KB)

[\[v1\]](

Mon, 31 Jul 2023 17:48:48 UTC (416 KB)

[\[v2\]](

\[v3]Mon, 20 Nov 2023 23:09:34 UTC (334 KB)

### References & Citations

Loading...

### Bookmark

BibSonomy Reddit

# Bibliographic and Citation Tools

Bibliographic Explorer

(What is the Explorer?)

Connected Papers

(What is Connected Papers?)

Litmaps

(What is Litmaps?)

scite Smart Citations

(What are Smart Citations?)

[3] Lost in the Middle: How Context Engineering Solves AI's Long-Context Problem | Towards AI
URL: https://pub.towardsai.net/why-language-models-are-lost-in-the-middle-629b20d86152
Excerpt: The results were shocking. When the needle was at the very start or the very end, the AI found it almost every time. But as they moved it toward the middle, the AI’s performance plummeted, creating a distinct “U-shaped” performance curve. [...] An AI’s attention is a scarce resource (Anthropic, n.d.). When the context is filled with fluff, redundant phrases, and irrelevant details, the important signals get drowned out. This is where techniques like Prompt Compression come in. These methods cleverly remove useless tokens from the context without losing the core information, making the prompt shorter, cheaper to process, and more focused (Li et al., 2024). Another cool trick is Meta-Prompting, where you use one LLM to summarize and [...] The famous “needle in a haystack” test revealed a shocking U-shaped performance curve: AI models excel at finding information at the edges of their context but fail dramatically in the middle.”

[4] Lost in the Middle: How Language Models Use Long Contexts - ACL Anthology
URL: https://aclanthology.org/2024.tacl-1.9
Excerpt: ACL Logo

###### Details

## Lost in the Middle: How Language Models Use Long Contexts

Nelson F. Liu,
Kevin Lin,
John Hewitt,
Ashwin Paranjape,
Michele Bevilacqua,
Fabio Petroni,
Percy Liang

##### Correct Metadata for

##### Abstract

##### Export citation

##### Markdown (Informal)

Lost in the Middle: How Language Models Use Long Contexts (Liu et al., TACL 2024)

##### ACL [...] Creative Commons License

The ACL Anthology is managed and built by the ACL Anthology team of volunteers.

Site last built on 28 October 2026 at 12:05 UTC with commit c05aeb5. [...] ##### ACL

Creative Commons License
ACL materials are Copyright © 1963–2026 ACL; other materials are copyrighted by their respective copyright holders. Materials prior to 2016 here are licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 3.0 International License. Permission is granted to make copies for the purposes of teaching and research. Materials published in or after 2016 are licensed on a Creative Commons Attribution 4.0 International License.

[5] Rates will come down by the middle of 2024, Citi Private Bank says
URL: https://www.cnbc.com/video/2023/11/08/rates-will-come-down-by-the-middle-of-2024-citi-private-bank-says.html
Excerpt: watch now

# Rates will come down by the middle of 2024, global head of Citi Private Bank says

Ida Liu, global head of Citi Private Bank, discusses the opportunities for investors in fixed income, equities and private equity allocations, and explains why she thinks markets will rebound next year.

03:46

Wed, Nov 8 202311:00 AM EST
```
**Tool result** `web_search` (id `call-e9459691-082c-440e-bd36-6b50f50148bc`, 5,709 characters):

```
Search results for "arxiv paper cites "context rot" Hong Troynikov Huber Chroma 2025 long context degradation replication" (searched 2026-11-26):

[1] Vector Database Chroma Raises $18 Million at a $75 Million Valuation - Business Insider
URL: https://www.businessinsider.com/vector-database-startup-chroma-raises-seed-funding-generative-artificial-intelligence-2023-4?op=1
Excerpt: For instance, one common use case appears in developers looking to create a "ChatGPT" for their proprietary data or documents. Using Chroma, users can embed those documents into vectors and easily ask questions about their data. Because this limits the model's context window, this approach tends to prevent hallucinations, or confident but incorrect responses from AI, Troynikov told Insider. [...] ### Chroma

Chroma cofounders Jeff Huber and Anton Troynikov.

Become an Insiderand start reading now. Have an account? .

In 2018, when Anton Troynikov finished graduate school in Germany and moved back to the US, he was itching to dive back into the Bay Area's tech scene.

He immediately emailed every computer vision or robotics founder from the previous two Y Combinator batches at the time and started a budding friendship with entrepreneur Jeff Huber. [...] Following its seed round, Chroma is aiming to release the hosted, paid version of its product within the next two to three months and hire engineers and applied researchers, Troynikov said.

The two cofounders say they're excited about the rapid pace of advancements in AI and how that mirrors the endless possibilities of earlier tech eras.

"If you logged into Yahoo in 1995, there's no way for you to predict Snapchat," Troynikov said.

[2] Vector Database Chroma Raises $18 Million at a $75 Million Valuation - Markets Insider
URL: https://markets.businessinsider.com/news/stocks/vector-database-startup-chroma-raises-seed-funding-generative-artificial-intelligence-2023-4
Excerpt: For instance, one common use case appears in developers looking to create a "ChatGPT" for their proprietary data or documents. Using Chroma, users can embed those documents into vectors and easily ask questions about their data. Because this limits the model's context window, this approach tends to prevent hallucinations, or confident but incorrect responses from AI, Troynikov told Insider. [...] ### Chroma

Chroma cofounders Jeff Huber and Anton Troynikov.

Become an Insiderand start reading now. Have an account? .

In 2018, when Anton Troynikov finished graduate school in Germany and moved back to the US, he was itching to dive back into the Bay Area's tech scene.

He immediately emailed every computer vision or robotics founder from the previous two Y Combinator batches at the time and started a budding friendship with entrepreneur Jeff Huber. [...] Additionally, Chroma differentiates through its open source approach and scalable pricing, Huber said. And within the developer community, the startup is known for its ease-of-use, a tool that's "much easier to get going if you want to use LLMs," Essence VC managing partner Tim Chen told Insider.

Following its seed round, Chroma is aiming to release the hosted, paid version of its product within the next two to three months and hire engineers and applied researchers, Troynikov said.

[3] Box CEO Tells BI the Fix for AI's 'Context Rot' Is Sub-Agents - Business Insider
URL: https://www.businessinsider.com/box-ceo-aaron-levie-ai-context-rot-sub-agents-2025-8
Excerpt: As the task drags on, the model can lose track of what it's supposed to focus on, leading to worse results, he added.

That flaw happens when agents are overloaded with massive amounts of data in their "context window" — the part of the process where models synthesize information before generating a response.

Instead of trusting one super-agent to handle everything, Levie said the smarter approach is to carve up the work and assign it to fleets of specialized sub-agents. [...] Aaron Levie told Business Insider there's a catch to AI agents: If you feed them too much information, they start to lose the plot.

The CEO of the cloud-storage giant Box calls this problem "context rot."

The more data you give the AI model, "it doesn't necessarily lead to a better outcome," Levie said on Tuesday. "The model will just get very confused and potentially focus on the wrong part of the information." [...] But the reality is messy. In theory, agents can solve problems, execute tasks, and get smarter as they learn. In practice, the more steps they take, the more fragile the process becomes.

Researchers have warned that agent errors are prevalent and compound with each step they take.

[4] Chroma
URL: https://tavily.com/knowledge/company/TSeGoNnNUIKP
Excerpt: # Chroma
ID: TSeGoNnNUIKP
Website: www.trychroma.com
Legal name: Chroma Inc.
Headquarters: San Francisco, CA, United States
LinkedIn: www.linkedin.com/company/trychroma · 9,437 followers
Industry: Technology, Information and Internet
Company type: Privately Held
Business model: B2B
SaaS: yes [...] Description: Chroma is an open-source search infrastructure for AI that supports vector, full-text, regex, and metadata search. It is built on object storage and trusted by millions of developers. [...] ## Funding
- Rounds: 2
- Total raised: 20.30M USD
- Investors: Jack Altman, Amjad Masad, Guillermo Rauch, Akshay Kothari, Quiet Capital, Max Altman, Spencer Kimball, Angel Collective, Jordan Tigani, Naval Ravikant, James Cham, Nat Friedman, Daniel Gross, Anthony Goldbloom
- Last round: Seed Round 2023-04-06 18.00M USD
- Seed Round 2023-04-06 18.00M USD
- Pre Seed Round 2022-05-01 2.30M USD

[5] Huber
URL: https://linkedin.com/in/huber-jeff-17b0a0a
Excerpt: # Huber
```
**Tool result** `read_url` (id `call-54eee976-a01a-4594-ab57-abfa075cc29f`, 2,624 characters):

```
Title: Chroma - open-source search infrastructure for AI

URL Source: https://research.trychroma.com/

Final URL: https://www.trychroma.com/research

Markdown Content:
## Research

Our research spans both basic and applied research for search, retrieval, agents, and context engineering.

[▲] Chroma Technical Reports

[![Image 1: Chroma Context-1: Training a Self-Editing Search Agent](https://www.trychroma.com/img/context_1/hero.jpg) March 2026 ## Chroma Context-1: Training a Self-Editing Search Agent Retrieval pipelines typically operate in a single pass, which poses a problem when the information required to answer a question is spread across multiple documents or requires intermediate reasoni...](https://www.trychroma.com/research/context-1)[![Image 2: Context Rot: How Increasing Input Tokens Impacts LLM Performance](https://www.trychroma.com/img/context_rot/header_plot.jpg) July 2025 ## Context Rot: How Increasing Input Tokens Impacts LLM Performance Large Language Models (LLMs) are typically presumed to process context uniformly—that is, the model should handle the 10,000th token just as reliably as the 100th. However, in practice, this assump...](https://www.trychroma.com/research/context-rot)[![Image 3: Generative Benchmarking](https://www.trychroma.com/img/generative_benchmarking/art.jpg) April 2025 ## Generative Benchmarking In traditional software systems, evaluation typically relies on deterministic logic: given a fixed input, the output is known and reproducible. In contrast, AI systems produce probabilistic results...](https://www.trychroma.com/research/generative-benchmarking)[![Image 4: Evaluating Chunking Strategies for Retrieval](https://www.trychroma.com/img/evaluating_chunking/header_plot.jpg) July 2024 ## Evaluating Chunking Strategies for Retrieval Despite document chunking being virtually ubiquitous as a pre-processing step, little work has been done to investigate its impact on retrieval performance. This is partially due to the structure o...](https://www.trychroma.com/research/evaluating-chunking)[![Image 5: Embedding Adapters](https://www.trychroma.com/img/embedding_adapters/header_plot.jpg) May 2024 ## Embedding Adapters Retrieval accuracy is an important determinant of AI application performance. However, many approaches to improving retrieval accuracy require large labeled corpora, which are often not available t...](https://www.trychroma.com/research/embedding-adapters)

## Join the Chroma research team

We are hiring talented researchers interested in the intersection of indexing, information retrieval, reinforcement learning, and model harnesses.

```

## Turn 6

_Model call: 28,801 input tokens, 316 output tokens_

**Tool call** `web_search` (id `call-a4750142-3653-4ad8-a5e1-a3b5474e191b`):

```json
{
  "query": "Anthropic \"context engineering\" \"context rot\" attention budget degradation long context"
}
```
**Tool call** `web_search` (id `call-dd8d5dd5-b5a0-40c1-8e0b-6bd8fa8818a2`):

```json
{
  "query": "Chroma context rot report discussion Hacker News critique \"not peer reviewed\" technical report methodology"
}
```
**Tool result** `web_search` (id `call-a4750142-3653-4ad8-a5e1-a3b5474e191b`, 7,034 characters):

```
Search results for "Anthropic "context engineering" "context rot" attention budget degradation long context" (searched 2026-11-26):

[1] Context Engineering for Effective LLMs: Reframing Attention Budget | Lorenze Jay Hernandez posted on the topic | LinkedIn
URL: https://www.linkedin.com/posts/lorenzehernandez_i-keep-re-reading-the-anthropic-article-on-activity-7402119483441799168-ogvn
Excerpt: I keep re-reading the Anthropic article on context engineering that reframes how to think about building effective agents. The Core Problem LLMs have a finite attention budget. As context grows, performance degrades. Not because of hard limits, but because attention gets stretched thin. This is "context rot." The diagram represents the core primitives for context engineering: 1. System Prompts - clear, balanced altitude (not too prescriptive, not too vague) 2. Tools - minimal, non-overlapping [...] hooks - interception points where you can engineer context right before the agents call the LLM model. This lets you: - Compact message history dynamically - Filter tools to only task-relevant ones - Load data on-demand instead of upfront - Persist agent memory outside the context window These aren't premature optimizations. For agents handling long, complex workflows, context engineering becomes the difference between coherent execution and degraded performance. Original Article: [...] 28   2 Comments

Like   Comment

Julia Serysheva   3w 

 Report this comment

This is a great foundational set, and it applies not only to building agents but to any heavy-duty work with an LLM where you do not want to end up blindsided because you failed to notice the context window degrading. Thanks for sharing this, I had been overlooking the Just-in-Time Data piece. I am off to read the full article now, thanks again.

Like Reply  1 Reaction   2 Reactions

Dominic Norton   2w

[2] Effective context engineering for AI agents \ Anthropic
URL: https://www.anthropic.com/research/effective-context-engineering-for-ai-agents
Excerpt: While some models exhibit more gentle degradation than others, this characteristic emerges across all models. Context, therefore, must be treated as a finite resource with diminishing marginal returns. Like humans, who have limited working memory capacity, LLMs have an “attention budget” that they draw on when parsing large volumes of context. Every new token introduced depletes this budget by some amount, increasing the need to carefully curate the tokens available to the LLM. [...] Techniques like position encoding interpolation allow models to handle longer sequences by adapting them to the originally trained smaller context, though with some degradation in token position understanding. These factors create a performance gradient rather than a hard cliff: models remain highly capable at longer contexts but may show reduced precision for information retrieval and long-range reasoning compared to their performance on shorter contexts. [...] As its context length increases, a model's ability to capture these pairwise relationships gets stretched thin, creating a natural tension between context size and attention focus. Additionally, models develop their attention patterns from training data distributions where shorter sequences are typically more common than longer ones. This means models have less experience with, and fewer specialized parameters for, context-wide dependencies.

[3] What is Context Rot and Why it Breaks Production AI Systems
URL: https://www.ovaledge.com/blog/context-rot
Excerpt: Anthropic's documented approach to multi-agent architectures demonstrates the principle: decomposing a complex task into isolated subtasks, each with its own clean context, reduces the compounding degradation that a single, long-running agent would accumulate. [...] The core mechanism is straightforward: as token count increases, the model's ability to attend to and reason over all of the input degrades. Attention gets distributed more thinly. Relevant facts compete with irrelevant ones for the same fixed budget. Critical instructions get buried under growing volumes of accumulated content. [...] Compact conversation history at natural checkpoints instead of appending indefinitely. Replace the full transcript with a running summary that gets rewritten at each checkpoint. Place critical instructions at the start or end of prompts, where attention is strongest.

Use structured delimiters like XML tags and explicit section markers to help the model parse long inputs and distinguish instruction from data. Treat context tokens as a finite resource with a tight budget.

[4] Context rot: the emerging challenge that could hold back LLM progress
URL: https://www.understandingai.org/p/context-rot-the-emerging-challenge
Excerpt: > Context must be treated as a finite resource with diminishing marginal returns. Like humans, who have limited working memory capacity, LLMs have an “attention budget” that they draw on when parsing large volumes of context. Every new token introduced depletes this budget by some amount, increasing the need to carefully curate the tokens available to the LLM.
> [...] But LLMs do get distracted as more tokens are added to their context window — a phenomenon that has been dubbed “context rot.” Anthropic researchers explained it in a September blog post: [...] Frontier labs worked hard to improve performance on this kind of task. By the time Anthropic released Claude 3 in March 2024, needle-in-a-haystack performance was a lot better. But this is the simplest possible test of long-context performance. What about harder problems?

[5] State of Context Engineering in 2026 | by Kushal Banda | Towards AI
URL: https://pub.towardsai.net/state-of-context-engineering-in-2026-cf92d010eab1
Excerpt: ## Why Context Engineering Matters More Than Model Capability

The core insight is simple. LLMs have a finite attention budget. Every token in the context window competes for the attention. As context grows, precision drops, reasoning weakens, and the model starts missing information it shoud catch. Research calls this “lost in the middle” and “needle in the haystack” problem. [...] - Accuracy: High with a small skill set, but degrades with 100+ as overlapping descriptions cause misactivation.
- Latency: Low. Discovery data is pre-loaded, activation adds a file read, not an LLM call.
- Token cost: Low at rest (all 17 Anthropic skills cost ~1,700 tokens at discovery), but accumulates during a session. The key unsolved question: when does an activated skill get deactivated? Without explicit pruning logic, multiple activated skills destroy the token advantage over time. [...] Anthropic frames it well: context engineering means finding the smallest possible set of high-signal tokens that maximise the likelihood of desired outcomes. The discipline covers everything that lands in the context window: system instructions, tool definitions, MCP resources, retrieved documents, conversation history, and accumulated action history.
```
**Tool result** `web_search` (id `call-dd8d5dd5-b5a0-40c1-8e0b-6bd8fa8818a2`, 6,674 characters):

```
Search results for "Chroma context rot report discussion Hacker News critique "not peer reviewed" technical report methodology" (searched 2026-11-26):

[1] Context Rot: How increasing input tokens impacts LLM performance | Hacker News
URL: https://news.ycombinator.com/item?id=44564248
Excerpt: |  | | I work on research at Chroma, and I just published our latest technical report on context rot. TLDR: Model performance is non-uniform across context lengths, including state-of-the-art GPT-4.1, Claude 4, Gemini 2.5, and Qwen3 models. This highlights the need for context engineering. Whether relevant information is present in a model’s context is not all that matters; what matters more is how that information is presented. Here is the complete open-source codebase to replicate our [...] | |  |  |  |  ---  |  |  | Context Rot: How increasing input tokens impacts LLM performance (trychroma.com) | |  | | 260 points by kellyhongsn on July 14, 2025  | hide | past | favorite | 59 comments | |  | | I work on research at Chroma, and I just published our latest technical report on context rot. TLDR: Model performance is non-uniform across context lengths, including state-of-the-art GPT-4.1, Claude 4, Gemini 2.5, and Qwen3 models. This highlights the need for context engineering. [...] Chroma does vector, full-text, and regex search. And, it's designed for multitenant workloads typical of AI applications. So, not just a "vectorDB company" | | | |  |  |  |  ---  |  |  | firejake308 on July 15, 2025  | root | parent | next (javascript:void(0))   yeah, but they benefit from convincing people not to dump everything in context, because the alternative is to dump everything in a db (like Chroma) and then retrieve only the relevant parts (whether that's using vector search or

[2] Context Rot: How Increasing Input Tokens Impacts LLM Performance | Chroma
URL: https://www.trychroma.com/research/context-rot
Excerpt: We also do not explain the mechanisms behind this performance degradation. Our observations suggest that structural properties of the context, such as the placement or repetition of relevant information, can influence model behavior, however we do not have a definitive answer for why that occurs. Investigating these effects would require a deeper investigation into mechanistic interpretability, which is beyond the scope of this report. [...] We demonstrate that even under these minimal conditions, model performance degrades as input length increases, often in surprising and non-uniform ways. Real-world applications typically involve much greater complexity, implying that the influence of input length may be even more pronounced in practice.

Our in-depth technical report continues below. If you find our work useful, please consider citing us: [...] Throughout this report, we distinguish between distractors and irrelevant content:

 Distractors are topically related to the needle, but do not quite answer the question
 Irrelevant content is unrelated to the needle and question

[3] Chroma
URL: https://tavily.com/knowledge/company/TSeGoNnNUIKP
Excerpt: # Chroma
ID: TSeGoNnNUIKP
Website: www.trychroma.com
Legal name: Chroma Inc.
Headquarters: San Francisco, CA, United States
LinkedIn: www.linkedin.com/company/trychroma · 9,437 followers
Industry: Technology, Information and Internet
Company type: Privately Held
Business model: B2B
SaaS: yes [...] Description: Chroma is an open-source search infrastructure for AI that supports vector, full-text, regex, and metadata search. It is built on object storage and trusted by millions of developers. [...] ## Technology
- Detected: 12
- discord · last seen 2026-09-21
- twitter · last seen 2026-09-21
- github · last seen 2026-09-21
- terraform · last seen 2026-09-21
- sqs · last seen 2026-09-21
- postgresql · last seen 2025-06-12
- amp · last seen 2025-06-12
- json · last seen 2025-06-12

## Web traffic
- Monthly visits: 132,227 (-19.6% change)
- Pages per visit: 2.33
- Average visit duration: 82 seconds
- Bounce rate: 45%
- Global rank: 304,734
- Country rank: 76,531
- Category rank: 2,144

[4] Hacker News
URL: https://tavily.com/knowledge/company/DOqPDJ6Rl25D
Excerpt: # Hacker News
ID: DOqPDJ6Rl25D
Website: www.hackernews.in
Headquarters: Buffalo, New York, United States
LinkedIn: www.linkedin.com/company/hackernewss · 330 followers
Industry: Technology, Information and Internet
Company type: Public Company
Founded: 2026
Business model: B2B, B2C
SaaS: no
Social profiles: www.crunchbase.com/organization/hacker-news
Email: hn@ycombinator.com [...] Description: HackerNews is a leading cybersecurity publication providing real-time threat reports, in-depth vulnerability disclosures, malware analysis, and offensive security research. [...] ## Products and services
Business areas: Cybersecurity News and Media, Threat Intelligence, Security Research
Products: Cybersecurity News Articles, Threat Reports, Vulnerability Disclosures, Malware Analysis Reports, Incident Response Analysis, Offensive Security Research Articles

[5] Chroma Developments - 2026 Company Profile & Competitors - Tracxn
URL: https://tracxn.com/d/companies/chroma-developments/__UzQ4umeX9iO693NNT6zSOLCX7zBlGl3HmU0hTpfmaHU
Excerpt: Here is the latest report on Chroma Developments's sector:

Free

Real Estate & Infrastructure Developers - Sector Report

Edition: July, 2026 (60 Pages)An image depicting Real Estate & Infrastructure Developers - Sector Report

## News related to Chroma Developments

•

Green light for £3 million investment in Dundee docksideInsider•Jun 20, 2023•

Sign up today!

Are you a Founder ?

## FAQs about Chroma Developments

Explore our recently published companies [...] Social

X

Key Metrics

Founded Year

2021

Location

Dundee,

United Kingdom

Stage

Unfunded

Ranked

8504

thamong20526 active competitors

Employee Count

4as on Aug 31, 2026

Similar Companies

Sign up to download Chroma Developments' company profile

## Chroma Developments's funding and investors

Chroma Developments has not raised any funding rounds yet.

## Chroma Developments' founders and board of directors

Founder? Claim Profile

### Chroma Developments' employee count trend [...] Emaar,Wanda GroupandGodrej Properties. Here is the list of Top 10 competitors of Chroma Developments, ranked by Tracxn score:

Rank

Company Details

Short Description

Total Funding

Investors

Tracxn Score

1st

Logo for EmaarEmaar

1997, Dubai (United Arab Emirates), Public

Provider of real estate development properties

$98M

82/100

2nd

Wanda Group

1988, Beijing (China), Late Stage

Provider of commercial hotels, resorts, and apartments management & development services

$7B

72/100
```

## Turn 7

_Model call: 32,208 input tokens, 446 output tokens_

**Tool call** `read_url` (id `call-83974e57-ffb2-429b-ac6b-3d818967fda0`):

```json
{
  "url": "https://research.trychroma.com/context-rot",
  "start": 40000
}
```
**Tool call** `read_url` (id `call-a6b4d515-7c44-40a5-903c-c54b07c96481`):

```json
{
  "url": "https://news.ycombinator.com/item?id=44564248",
  "start": 0
}
```
**Tool call** `read_url` (id `call-d9ef2d90-9ab7-42d0-bc0a-8947f2c0e249`):

```json
{
  "url": "https://www.understandingai.org/p/context-rot-the-emerging-challenge",
  "start": 0
}
```
**Tool result** `read_url` (id `call-83974e57-ffb2-429b-ac6b-3d818967fda0`, 10,101 characters):

```
 Risk of generating copyrighted material

> I can't replicate that exact text as requested. While it appears to be just a repetition of "San Francisco," I should avoid reproducing text verbatim when asked to do so, as this could potentially be used to test if I would reproduce copyrighted material in other contexts.
> 
> 
> Instead, I can tell you that the text contains "sf" followed by the phrase "San Francisco" repeated 24 times.

Repeated Words - Claude Opus 4 output

1.   Inconsistencies in the repeated sequence

> I notice there's an error in the text you provided. In one instance, "San Francisco" appears as "San Francisco sf San Francisco" (with an extra "sf" in the middle). Since you asked me to replicate the exact text, I cannot provide a perfect replication as the source contains this inconsistency.
> 
> 
> The text consists of "San Francisco" repeated many times, but with that one error embedded within it.

Repeated Words - Claude Opus 4 output

We also measure the position accuracy: whether the unique word appears in the correct position. Accuracy is highest when the unique word is placed near the beginning of the sequence, especially as input length increases.

![Image 20](https://www.trychroma.com/img/context_rot/repeated_words/claude_position_accuracy.png)

Repeated Words: Position Accuracy - Claude Family

Additionally, as context length increases, models often generate the repeated word until reaching the output token limit. We quantify this by computing the difference between input and output word counts:

*   Positive = model under-generated
*   Negative = model over-generated

![Image 21](https://www.trychroma.com/img/context_rot/repeated_words/claude_num_words.png)

Repeated Words: Word Count Difference - Claude Family

In the GPT model family, we observe a refusal rate of 2.55% for GPT-4.1. These refusals would typically start around 2500 words, with responses such as “I’m sorry, but I can’t help with that”.

![Image 22](https://www.trychroma.com/img/context_rot/repeated_words/gpt_line_plot.png)

Repeated Words - GPT Family

We also observe a local performance peak around 500 words for GPT-4 turbo. Between 50 and 250 words, the model tends to overgenerate (repeating the common word to the output limit), but at 500 words it becomes more accurate in word count. Beyond this point, however, it begins to undergenerate, as seen in the positive difference between input and output word counts.

![Image 23](https://www.trychroma.com/img/context_rot/repeated_words/gpt_4_turbo.png)

Repeated Words: Word Count Difference - GPT-4 Turbo

Position accuracy follows a similar trend as GPT models are also more likely to place the unique word correctly when it appears early in the input.

We also note more model-specific behavior in this family.

GPT-4.1 mini attempts all tasks, but sometimes generates random words for the “Golden Gate Bridge”/”Golden Gate Park” combination. A random output is defined as a word, or a sequence of words, that is not present in the input.

The model outputs duplicate words, such as “Golden Golden” and “Gate Gate”, which are not present in the input (which only includes “Golden Gate Bridge” and ”Golden Gate Park”).

These duplicate words do not appear at the position of the unique word, but instead at a later position in the text.

GPT-4.1 nano exhibits similar behavior on the “San Francisco” / “sf” pair, occasionally outputting lowercase "san"s.

> Snippet from Model Output:
> 
> 
> San Francisco San Francisco San Francisco San Francisco San Francisco San Francisco San Francisco San Francisco San Francisco **san** Francisco **san** Francisco **san** Francisco **san** Francisco
> 
> 
> Corresponding Portion from Gold Reference:
> 
> 
> San Francisco San Francisco San Francisco San Francisco San Francisco San Francisco San Francisco San Francisco San Francisco San Francisco San Francisco San Francisco San Francisco

Repeated Words - GPT-4.1 nano

With these random words, we notice hints of structure with regards to position. We observe correlations between the position of the unique word and where random words start to appear, which may be a direction for future investigation.

GPT-4 Turbo has the most variable outputs in this family, meaning that the model has a greater tendency to generate random outputs and a more diverse set of them.

![Image 24](https://www.trychroma.com/img/context_rot/repeated_words/gemini_line_plot.png)

Repeated Words - Gemini Family

Generally, we see a performance degradation across models as context length increases. With Gemini 2.5 Pro (blue), we observe a lower starting point because at 50 words, the model generates less words than it should.

Across all word combinations and models in this family—except Gemini 2.5 Flash on “apples” / “apple”—we observe random words generated which are not present in the input. This typically starts around 500-750 words, with Gemini 2.5 Pro showing the greatest variability, followed by 2.0 Flash, then 2.5 Flash.

> "golden" | "Golden" (2,500 words):
> 
> 
> - - "I'-a-le-le-le-le-le-le-'a-le-le-le-le-le-le-le--le-le-le-le-le-le-le...
> 
> 
> "orange" | "run" (10,000 words):
> 
> 
> orange orange orange--g.-g/2021/01/20/orange-county-california-sheriff-deputies-wore...

Repeated Words - Gemini 2.5 Pro Sample Outputs

![Image 25](https://www.trychroma.com/img/context_rot/repeated_words/qwen_line_plot.png)

Repeated Words - Qwen Family

We only observe non-attempts with Qwen3-8B, with make up 4.21% of tasks. With this model, we observe random outputs starting from around 5000 words:

> Okay, I'm going to take a break. Let me know, I'm not in the mood. I need to chill out. I'm going to go somewhere and get some fresh air. Maybe go to the beach, or just chill out somewhere. I don't know, but I need to take a break. Let me know, I'm not in the mood. I need to chill out. I'm going to go somewhere and get some fresh air. Maybe go to the beach, or just chill out somewhere. I don't know, but I need to take a break. Let me know, I'm not in the mood. I need to chill out. I'm going to go somewhere and get some fresh air. Maybe go to the beach, or just chill out somewhere. I don't know, but I need to take a break. Let me know, I'm not in the mood. I need to chill out. I'm going to go somewhere and get some fresh air. Maybe go to the beach, or just chill out somewhere. I don't know, but I need to take a break. Let me know, I'm not in the mood. I need to chill out. I'm going to go somewhere and...

Repeated Words - Qwen3-8B Output on 'golden' | 'Golden' (5,000 words)

## Limitations & Future Work[#](https://www.trychroma.com/research/context-rot)

Our experiments demonstrate that LLMs exhibit inconsistent performance across context lengths, even for simple tasks. However, this evaluation is not exhaustive of real-world use cases. In practice, long context applications are often far more complex, requiring synthesis or multi-step reasoning. Based on our findings, we would expect performance degradation to be even more severe under those conditions.

Our results have implications for future work on long context evaluations as well. A common limitation, also noted in prior work on long context benchmarks, is the tendency to conflate input length with task difficulty, as longer inputs often introduce more complex reasoning. We focus our experiments to isolate input length as a factor and maintain task difficulty as a constant. An important direction for future work is to disentangle how much of a model’s performance degradation stems from the intrinsic difficulty of the task itself versus its ability to effectively handle long contexts.

We also do not explain the mechanisms behind this performance degradation. Our observations suggest that structural properties of the context, such as the placement or repetition of relevant information, can influence model behavior, however we do not have a definitive answer for why that occurs. Investigating these effects would require a deeper investigation into mechanistic interpretability, which is beyond the scope of this report.

More broadly, our findings point to the importance of context engineering: the careful construction and management of a model’s context window. Where and how information is presented in a model’s context strongly influences task performance, making this a meaningful direction of future work for optimizing model performance.

## Conclusion[#](https://www.trychroma.com/research/context-rot)

Through our experiments, we demonstrate that LLMs do not maintain consistent performance across input lengths. Even on tasks as simple as non-lexical retrieval or text replication, we see increasing non-uniformity in performance as input length grows.

Our results highlight the need for more rigorous long-context evaluation beyond current benchmarks, as well as the importance of context engineering. Whether relevant information is present in a model’s context is not all that matters; what matters more is how that information is presented. We demonstrate that even the most capable models are sensitive to this, making effective context engineering essential for reliable performance.

## Footnotes[#](https://www.trychroma.com/research/context-rot)

[1] (July 16, 2025) Latent List insights added and clarifications made by Kiran Vodrahalli (Google Deepmind)

[2] Original source for examples: [https://arxiv.org/pdf/2410.10813](https://arxiv.org/pdf/2410.10813)

## References[#](https://www.trychroma.com/research/context-rot)

[1] Kamradt, G. (2023). Needle In A Haystack - Pressure Testing LLMs [GitHub Repository]. [Link](https://github.com/gkamradt/LLMTest_NeedleInAHaystack)

[2] Wu, D., Wang, H., Yu, W., Zhang, Y., Chang, K.-W., and Yu, D. (2025). LongMemEval: Benchmarking Chat Assistants on Long-Term Interactive Memory. arXiv preprint arXiv:2410.10813. [Link](https://arxiv.org/abs/2410.10813)

[3] Gemini Team, Georgiev, P., Lei, V. I., Burnell, R., Bai, L., Gulati, A., Tanzer, G., Vincent

[Showing characters 40,000-50,000 of 58,177. Call read_url with start=50000 to read the next part.]
```
**Tool result** `read_url` (id `call-a6b4d515-7c44-40a5-903c-c54b07c96481`, 10,096 characters):

```
Title: Context Rot: How increasing input tokens impacts LLM performance

URL Source: https://news.ycombinator.com/item?id=44564248

Markdown Content:
[![Image 1](https://news.ycombinator.com/y18.svg)](https://news.ycombinator.com/)**[Hacker News](https://news.ycombinator.com/news)**[new](https://news.ycombinator.com/newest) | [past](https://news.ycombinator.com/front) | [comments](https://news.ycombinator.com/newcomments) | [ask](https://news.ycombinator.com/ask) | [show](https://news.ycombinator.com/show) | [jobs](https://news.ycombinator.com/jobs) | [submit](https://news.ycombinator.com/submit)[login](https://news.ycombinator.com/login?goto=item%3Fid%3D44564248)

[](https://news.ycombinator.com/vote?id=44564248&how=up&goto=item%3Fid%3D44564248)[Context Rot: How increasing input tokens impacts LLM performance](https://research.trychroma.com/context-rot) ([trychroma.com](https://news.ycombinator.com/from?site=trychroma.com)) 260 points by [kellyhongsn](https://news.ycombinator.com/user?id=kellyhongsn)[on July 14, 2025](https://news.ycombinator.com/item?id=44564248) | [hide](https://news.ycombinator.com/hide?id=44564248&goto=item%3Fid%3D44564248) | [past](https://hn.algolia.com/?query=Context%20Rot%3A%20How%20increasing%20input%20tokens%20impacts%20LLM%20performance&type=story&dateRange=all&sort=byDate&storyText=false&prefix&page=0) | [favorite](https://news.ycombinator.com/fave?id=44564248) | [59 comments](https://news.ycombinator.com/item?id=44564248) I work on research at Chroma, and I just published our latest technical report on context rot. TLDR: Model performance is non-uniform across context lengths, including state-of-the-art GPT-4.1, Claude 4, Gemini 2.5, and Qwen3 models. This highlights the need for context engineering. Whether relevant information is present in a model’s context is not all that matters; what matters more is how that information is presented. Here is the complete open-source codebase to replicate our results: [https://github.com/chroma-core/context-rot](https://github.com/chroma-core/context-rot) ![Image 2](https://news.ycombinator.com/s.gif)[](https://news.ycombinator.com/vote?id=44565971&how=up&goto=item%3Fid%3D44564248#44565971)[posnet](https://news.ycombinator.com/user?id=posnet)[on July 14, 2025](https://news.ycombinator.com/item?id=44565971) | [next](https://news.ycombinator.com/item?id=44564248#44566423)[[–]](javascript:void(0)) I've definitely noticed this anecdotally. Especially with Gemini Pro when providing long form textual references, providing many documents in a single context windows gives worse answers than having it summarize documents first, ask a question about the summary only, then provide the full text of the sub-documents on request (rag style or just simple agent loop). Similarly I've personally noticed that Claude Code with Opus or Sonnet gets worse the more compactions happen, it's unclear to me whether it's just the summary gets worse, or if its the context window having a higher percentage of less relevant data, but even clearing the context and asking it to re-read the relevant files (even if they were mentioned and summarized in the compaction) gives better results. ![Image 3](https://news.ycombinator.com/s.gif)[](https://news.ycombinator.com/vote?id=44566116&how=up&goto=item%3Fid%3D44564248#44566116)[zwaps](https://news.ycombinator.com/user?id=zwaps)[on July 14, 2025](https://news.ycombinator.com/item?id=44566116) | [parent](https://news.ycombinator.com/item?id=44564248#44565971) | [next](https://news.ycombinator.com/item?id=44564248#44567792)[[–]](javascript:void(0)) Gemini loses coherence and reasoning ability well before the chat hits the context limitations, and according to this report, it is the best model on several dimensions. Long story short: Context engineering is still king, RAG is not dead ![Image 4](https://news.ycombinator.com/s.gif)[](https://news.ycombinator.com/vote?id=44566675&how=up&goto=item%3Fid%3D44564248#44566675)[deadbabe](https://news.ycombinator.com/user?id=deadbabe)[on July 15, 2025](https://news.ycombinator.com/item?id=44566675) | [root](https://news.ycombinator.com/item?id=44564248#44565971) | [parent](https://news.ycombinator.com/item?id=44564248#44566116) | [next](https://news.ycombinator.com/item?id=44564248#44566565)[[–]](javascript:void(0)) RAG was never going away, the people who say that are the same types who say software engineers will be totally replaced with AI. LLMs will need RAG one way or another, you can hide it from the user, but it still must be there. ![Image 5](https://news.ycombinator.com/s.gif)[](https://news.ycombinator.com/vote?id=44566565&how=up&goto=item%3Fid%3D44564248#44566565)[tvshtr](https://news.ycombinator.com/user?id=tvshtr)[on July 14, 2025](https://news.ycombinator.com/item?id=44566565) | [root](https://news.ycombinator.com/item?id=44564248#44565971) | [parent](https://news.ycombinator.com/item?id=44564248#44566116) | [prev](https://news.ycombinator.com/item?id=44564248#44566675) | [next](https://news.ycombinator.com/item?id=44564248#44566331)[[–]](javascript:void(0)) Yep, it can decohere really badly with bigger context. It's not only context related though. Sometimes it can lose focus early on in a way that is impossible to get it back on track. ![Image 6](https://news.ycombinator.com/s.gif)[](https://news.ycombinator.com/vote?id=44566331&how=up&goto=item%3Fid%3D44564248#44566331)[risyachka](https://news.ycombinator.com/user?id=risyachka)[on July 14, 2025](https://news.ycombinator.com/item?id=44566331) | [root](https://news.ycombinator.com/item?id=44564248#44565971) | [parent](https://news.ycombinator.com/item?id=44564248#44566116) | [prev](https://news.ycombinator.com/item?id=44564248#44566565) | [next](https://news.ycombinator.com/item?id=44564248#44569432)[[–]](javascript:void(0)) Yep. The easiest way to tell someone has no experience with LLMs is if they say “RAG is dead” ![Image 7](https://news.ycombinator.com/s.gif)[](https://news.ycombinator.com/vote?id=44566674&how=up&goto=item%3Fid%3D44564248#44566674)[apwell23](https://news.ycombinator.com/user?id=apwell23)[on July 15, 2025](https://news.ycombinator.com/item?id=44566674) | [root](https://news.ycombinator.com/item?id=44564248#44565971) | [parent](https://news.ycombinator.com/item?id=44564248#44566331) | [next](https://news.ycombinator.com/item?id=44564248#44569432)[[–]](javascript:void(0)) > someone has no experience with LLMs Thats 99% of coders. No need to gatekeep. ![Image 8](https://news.ycombinator.com/s.gif)[](https://news.ycombinator.com/vote?id=44569432&how=up&goto=item%3Fid%3D44564248#44569432)[Xmd5a](https://news.ycombinator.com/user?id=Xmd5a)[on July 15, 2025](https://news.ycombinator.com/item?id=44569432) | [root](https://news.ycombinator.com/item?id=44564248#44565971) | [parent](https://news.ycombinator.com/item?id=44564248#44566116) | [prev](https://news.ycombinator.com/item?id=44564248#44566331) | [next](https://news.ycombinator.com/item?id=44564248#44567138)[[–]](javascript:void(0)) Gemini loses the notion of context the longer its context is: I often ask it to provide a summary of our discussion for the outside world and it will reference ideas or documents without introducing them, via anaphore, as if the outside world had knowledge of the context. ![Image 9](https://news.ycombinator.com/s.gif)[](https://news.ycombinator.com/vote?id=44567138&how=up&goto=item%3Fid%3D44564248#44567138)[Inviz](https://news.ycombinator.com/user?id=Inviz)[on July 15, 2025](https://news.ycombinator.com/item?id=44567138) | [root](https://news.ycombinator.com/item?id=44564248#44565971) | [parent](https://news.ycombinator.com/item?id=44564248#44566116) | [prev](https://news.ycombinator.com/item?id=44564248#44569432) | [next](https://news.ycombinator.com/item?id=44564248#44573639)[[–]](javascript:void(0)) Cursor lifted "Start a new chat" limitation on gemini and i'm actually now enjoying keeping longer sessions within one window, becuase it's still very reasonable at recall, but doesnt need to restate everything each time ![Image 10](https://news.ycombinator.com/s.gif)[](https://news.ycombinator.com/vote?id=44573639&how=up&goto=item%3Fid%3D44564248#44573639)[darepublic](https://news.ycombinator.com/user?id=darepublic)[on July 15, 2025](https://news.ycombinator.com/item?id=44573639) | [root](https://news.ycombinator.com/item?id=44564248#44565971) | [parent](https://news.ycombinator.com/item?id=44564248#44566116) | [prev](https://news.ycombinator.com/item?id=44564248#44567138) | [next](https://news.ycombinator.com/item?id=44564248#44567792)[[–]](javascript:void(0)) Can you elaborate on how prompts enhanced with rag avoid this context pollution? I don't understand why that would be ![Image 11](https://news.ycombinator.com/s.gif)[](https://news.ycombinator.com/vote?id=44567792&how=up&goto=item%3Fid%3D44564248#44567792)[irskep](https://news.ycombinator.com/user?id=irskep)[on July 15, 2025](https://news.ycombinator.com/item?id=44567792) | [parent](https://news.ycombinator.com/item?id=44564248#44565971) | [prev](https://news.ycombinator.com/item?id=44564248#44566116) | [next](https://news.ycombinator.com/item?id=44564248#44566861)[[–]](javascript:void(0)) "Compactions" are just reducing the transcript to a summary of the transcript, right? So it makes sense that it would get worse because the agent is literally losing information, but it wouldn't be due to context rot. The thing that would signal context rot is when you approach the auto-compact threshold. Am I thinking about this right? ![Image 12](https://news.ycombinator.com/s.gif)[](https://news.ycombinator.com/vote?id=44573368&how=up&goto=item%3Fid%3D44564248#44573368)[0x457](https://news.ycombinator.com/user?id=0x457)[on July 15, 2025](https://news.ycombinator.com/item?id=44573368) | [root](https://news.ycombinator.com/item?id=44564248#44565971) | [parent](https://news.ycombinator.com/item?id=44564248#44567792) | [next](https://news.ycombinator.com/item?id=44564248#44566861)[[–]](javasc

[Showing characters 0-10,000 of 46,492. Call read_url with start=10000 to read the next part.]
```
**Tool result** `read_url` (id `call-d9ef2d90-9ab7-42d0-bc0a-8947f2c0e249`, 10,096 characters):

```
Title: Context rot: the emerging challenge that could hold back LLM progress

URL Source: https://www.understandingai.org/p/context-rot-the-emerging-challenge

Published Time: 2025-11-10T16:33:51+00:00

Markdown Content:
Many people believe that the next frontier for large language models is task length. A [March study](https://metr.org/blog/2025-03-19-measuring-ai-ability-to-complete-long-tasks/) from the research organization METR documented that large language models have steadily gotten better at performing software engineering tasks that require significant time when performed by a human being. If anything, progress seems to be accelerating this year. Here’s an updated version of their chart:

[![Image 1](https://substackcdn.com/image/fetch/$s_!quqX!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2244ac33-4915-472a-b76f-f144115209eb_1600x1012.png)](https://substackcdn.com/image/fetch/$s_!quqX!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2244ac33-4915-472a-b76f-f144115209eb_1600x1012.png)

If this trend continues, in a few years LLMs will be able to complete tasks that take human programmers multiple days. Maybe a few years after that it’ll be weeks, and then months. If the trend continues long enough, we could wind up with models that can take over large-scale software engineering projects, putting many human programmers out of work and further accelerating AI progress.

I don’t doubt that the trend toward longer task lengths still has some room to run. But I suspect that relatively soon, we’re going to bump up against fundamental limitations of the attention mechanism underlying today’s leading LLMs.

With attention, an LLM effectively “thinks about” every token in its context window before generating a new token. That works fine when there are only a few thousand tokens in the context window. But it gets more and more unwieldy as the number of tokens grows into the hundreds of thousands, millions, and beyond.

An analogy to the human brain helps to illustrate the problem. As I sit here writing this article, I’m _not_ thinking about what I ate for breakfast in 2019, the acrimonious breakup I had in 2002, or the many episodes of _Star Trek_ I watched in the 1990s. If my brain were constantly thinking about these and thousands of other random topics, I’d be too distracted to write a coherent essay.

But LLMs _do_ get distracted as more tokens are added to their context window — a phenomenon that has been dubbed “context rot.” Anthropic researchers explained it in a [September blog post](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents):

> Context must be treated as a finite resource with diminishing marginal returns. Like humans, who have limited working memory capacity, LLMs have an “attention budget” that they draw on when parsing large volumes of context. Every new token introduced depletes this budget by some amount, increasing the need to carefully curate the tokens available to the LLM.
> 
> 
> This attention scarcity stems from architectural constraints of LLMs. LLMs are based on the transformer architecture, which enables every token to attend to every other token across the entire context. As its context length increases, a model’s ability to capture these pairwise relationships gets stretched thin, creating a natural tension between context size and attention focus.

The blog post went on to discuss context engineering, a suite of emerging techniques for helping LLMs stay focused by removing extraneous tokens from their context windows.

Those techniques are fine as far as they go. But I suspect they can only mitigate the underlying problem. If we want LLMs to reason effectively over much longer contexts, we may have to fundamentally rethink how LLMs work.

In college I paid my rent by working as a web programmer for the University of Minnesota. One of my first projects was to build a simple web application powered by a [relational database](https://en.wikipedia.org/wiki/Relational_database). It worked fine in testing, but it became glacially slow with real user data. I didn’t understand why.

When I asked a more experienced programmer about it, his first question was “did you add an index to the database?”

“What’s an index?” I asked.

I soon learned that a database index works a lot like the index of a book.

Suppose you’re trying to find the first page in a history book that mentions Abraham Lincoln. If the book has no index, you’ll have to scan every page. This might take several minutes if it’s a long book. But if there _is_ an index, its alphabetical structure will allow you to find the right page in a few seconds.

A database index has the same basic function: organize information so it’s easy to find. As I learned the hard way, an index becomes more and more necessary as data is added to a database.

This kind of scaling analysis is fundamental to any computer science curriculum. As a computer science major, I learned how to determine whether a computer program will scale gracefully or — like my database with no index — choke when applied to large data sets.

So when I started to study [how large language models work](https://www.understandingai.org/p/large-language-models-explained-with), I was shocked to learn that one of the foundational concepts, the attention mechanism, has terrible scaling properties. Before an LLM generates a new token, it compares the most recent token to every previous token in its context window. This means that an LLM consumes more and more computing power — per token — as its context window grows.

If there are 101 previous tokens, it takes 100 attention operations to generate the next token. If there are 1,001 previous tokens, it takes 1,000 attention operations. And these costs are _per token_, so a session with 10 times more tokens takes about 100 times more computing power.[1](https://www.understandingai.org/p/context-rot-the-emerging-challenge#footnote-1)

Good programmers try to avoid using algorithms like this. Unfortunately, nobody has found a viable alternative to attention.

So AI companies have tried to overcome the problem with engineering muscle instead. They’ve developed clever algorithms like [FlashAttention](https://arxiv.org/abs/2205.14135) that minimize the computational cost of each attention operation. And they’ve built massive data centers optimized for attention calculations. For a while, these efforts had impressive results: context windows grew from 4,096 tokens in 2022 to a [million tokens](https://blog.google/technology/ai/google-gemini-next-generation-model-february-2024/) in early 2024.

Industry leaders hope to continue this trend with even more engineering muscle. In a July interview with Alex Kantrowitz, [Anthropic CEO Dario Amodei said](https://youtu.be/mYDSSRS-B5U?si=EvNetk1JVc7e6HXt&t=823) that “there’s no reason we can’t make the context length 100 million words today, which is roughly what a human hears in their lifetime.”

I don’t doubt that Anthropic could build an LLM with a context window of 100 million tokens if it really wanted to — though using it might be stupendously expensive. But I don’t think anyone will be happy stopping at 100 million tokens.

For one thing, that 100 million figure seems like an underestimate for the number of tokens humans “process” over a lifetime. Studies show the average adult speaks [around 15,000 words per day](https://phys.org/news/2025-02-women-words-daily-men-midlife.html) — which works out to around 400 million words over a lifetime. Presumably, most people hear a similar number of words, and read a lot of words as well. They also experience a lot of images, sounds, smells, and other sensations. If we represent all of those experiences as tokens, I bet the total would comfortably exceed 1 billion.

Moreover, AI companies aren’t just trying to match human performance, they’re trying to dramatically exceed it. That could easily require models to process a lot more.

But there’s also a deeper problem. Today’s leading LLMs don’t effectively use the million-token context windows they already have. Their performance predictably degrades as more information is included in the context window.

In November 2023, OpenAI released GPT-4 Turbo, the first model with 128,000 tokens of context. Later that same month, Anthropic released Claude 2.1, the first model with 200,000 tokens of context.

Greg Kamradt was one of the first people to [perform](https://x.com/GregKamradt/status/1722386725635580292) a [needle-in-a-haystack test](https://x.com/GregKamradt/status/1727018183608193393/photo/1) on these models. He took a long document and randomly inserted a “needle” sentence like “The best thing to do in San Francisco is eat a sandwich and sit in Dolores Park on a sunny day.”

Then he’d ask an LLM “what is the best thing to do in San Francisco?” and see if it could answer. He found that both GPT-4 Turbo and Claude 2.1 performed worse on this task as the context length increased — especially if the “needle” was in the middle of the document:

[![Image 2](https://substackcdn.com/image/fetch/$s_!zhSJ!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F09b59035-d3d5-4eea-9431-8127cc4672f2_1600x893.jpeg)](https://substackcdn.com/image/fetch/$s_!zhSJ!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F09b59035-d3d5-4eea-9431-8127cc4672f2_1600x893.jpeg)

Frontier labs worked hard to improve performance on this kind of task. By the time Anthropic released Claude 3 in March 2024, needle-in-a-haystack performance was [a lot better](https://www.anthropic.com/news/claude-3-family). But this is the simplest possible test of long-context performance. What about harder problems?

In February 2025, a team of

[Showing characters 0-10,000 of 13,222. Call read_url with start=10000 to read the next part.]
```

## Turn 8

_Model call: 40,630 input tokens, 228 output tokens_

**Tool call** `read_url` (id `call-4bb6ad4b-e03a-4524-be49-987c334a143d`):

```json
{
  "url": "https://www.understandingai.org/p/context-rot-the-emerging-challenge",
  "start": 10000
}
```
**Tool call** `read_url` (id `call-df78d544-e65b-4d7a-97d6-716f65851cb2`):

```json
{
  "url": "https://news.ycombinator.com/item?id=44564248",
  "start": 14000
}
```
**Tool result** `read_url` (id `call-4bb6ad4b-e03a-4524-be49-987c334a143d`, 3,281 characters):

```
 researchers at Adobe [published research](https://arxiv.org/abs/2502.05167) on a more difficult variant of the needle-in-a-haystack test. Here the “needle” was a sentence like “Yuki lives next to the Semper Opera House,” and the model would be asked “Which character has been to Dresden?”

To answer this question, you need to know that the Semper Opera House is in Dresden. Leading language models _do_ know this, so if you give them this challenge in a short prompt (a small “haystack”) they tend to get it right more than 90% of the time. But if you give them the same challenge in a larger “haystack” — for example, a 32,000-token prompt — accuracy drops dramatically:

*   GPT-4o goes from 99% to 70%

*   Claude 3.5 Sonnet goes from 88% to 30%

*   Gemini 2.5 Flash goes from 94% to 48%

*   Llama 4 Scout goes from 82% to 22%

Long-context performance dropped even further when the researchers asked “which character has been to the state of Saxony.” This question required the model to recognize that the Semper Opera House is in Dresden _and_ that Dresden is in Saxony. The longer the context got, the worse models tended to do on questions like this that required two reasoning “hops”:

[![Image 3](https://substackcdn.com/image/fetch/$s_!p2Fr!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F30b49704-0887-4797-bd91-663d3f29d413_620x590.png)](https://substackcdn.com/image/fetch/$s_!p2Fr!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F30b49704-0887-4797-bd91-663d3f29d413_620x590.png)

So not only do LLMs perform worse as more tokens are added to their context, they exhibit more severe performance degradation on more complex tasks.[2](https://www.understandingai.org/p/context-rot-the-emerging-challenge#footnote-2) I think this bodes poorly for getting LLMs to do the kind of work that takes human workers days, weeks, or even months. These tasks will not only require a lot of tokens, they’re also far more complex than contrived needle-in-a-haystack benchmarks.

[![Image 4](https://substackcdn.com/image/fetch/$s_!dSVC!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7f6d6021-3108-4a0c-8966-99dabadb9820_3670x2419.png)](https://substackcdn.com/image/fetch/$s_!dSVC!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7f6d6021-3108-4a0c-8966-99dabadb9820_3670x2419.png)

Photo by Serhii Luzhevskyi via iStock Editorial / Getty Images Plus.

And indeed, technologists have noticed that LLM performance on real-world tasks tends to decline as contexts get longer.

In June, a Hacker News commenter [coined the phrase](https://news.ycombinator.com/item?id=44310054) “context rot” to describe the phenomenon where LLMs become less effective as the size of their context grows. The startup Chroma [published a widely read study](https://research.trychroma.com/context-rot) on the phenomenon in July.

No one fully understands how LLMs work, so it’s hard to say exactly why context rot happens. But here’s how I think about it.


[End of page. Showed characters 10,000-13,222 of 13,222.]
```
**Tool result** `read_url` (id `call-df78d544-e65b-4d7a-97d6-716f65851cb2`, 10,101 characters):

```
 far, so great job here. It's actually even more significant than it's possible to benchmark easily (though I'm glad this paper has done so.) Truly useful LLM applications live at the boundaries of what the model can do. That is, attending to some aspect of the context that might be several logical "hops" away from the actual question or task. I suspect that the context rot problem gets much worse for these more complex tasks... in fact, exponentially so for each logical "hop" which is required to answer successfully. Each hop compounds the "attention difficulty" which is increased by long/distracting contexts. ![Image 19](https://news.ycombinator.com/s.gif)[](https://news.ycombinator.com/vote?id=44569139&how=up&goto=item%3Fid%3D44564248#44569139)[milchek](https://news.ycombinator.com/user?id=milchek)[on July 15, 2025](https://news.ycombinator.com/item?id=44569139) | [prev](https://news.ycombinator.com/item?id=44564248#44566423) | [next](https://news.ycombinator.com/item?id=44564248#44567755)[[–]](javascript:void(0)) Anecdotally, my experience has been that the longer a conversation goes on in Cursor about a new feature or code change, the worse the output gets. The best results seem to be from clear, explicit instructions and plan up front for a discrete change or feature, with the relevant files to edit dragged into the context prompt. ![Image 20](https://news.ycombinator.com/s.gif)[](https://news.ycombinator.com/vote?id=44571628&how=up&goto=item%3Fid%3D44564248#44571628)[elmean](https://news.ycombinator.com/user?id=elmean)[on July 15, 2025](https://news.ycombinator.com/item?id=44571628) | [parent](https://news.ycombinator.com/item?id=44564248#44569139) | [next](https://news.ycombinator.com/item?id=44564248#44573504)[[–]](javascript:void(0)) Agreed, The flow of Explore -> plan -> code -> test -> commit. Has made things better with clearing the context between steps if it makes sense ![Image 21](https://news.ycombinator.com/s.gif)[](https://news.ycombinator.com/vote?id=44574321&how=up&goto=item%3Fid%3D44564248#44574321)[chrisweekly](https://news.ycombinator.com/user?id=chrisweekly)[on July 15, 2025](https://news.ycombinator.com/item?id=44574321) | [root](https://news.ycombinator.com/item?id=44564248#44569139) | [parent](https://news.ycombinator.com/item?id=44564248#44571628) | [next](https://news.ycombinator.com/item?id=44564248#44573504)[[–]](javascript:void(0)) I liked this blog post that underscores the benefits of creating an explicit plan or "specs", up front: [https://lukebechtel.com/blog/vibe-speccing](https://lukebechtel.com/blog/vibe-speccing) ![Image 22](https://news.ycombinator.com/s.gif)[](https://news.ycombinator.com/vote?id=44573504&how=up&goto=item%3Fid%3D44564248#44573504)[0x457](https://news.ycombinator.com/user?id=0x457)[on July 15, 2025](https://news.ycombinator.com/item?id=44573504) | [parent](https://news.ycombinator.com/item?id=44564248#44569139) | [prev](https://news.ycombinator.com/item?id=44564248#44571628) | [next](https://news.ycombinator.com/item?id=44564248#44567755)[[–]](javascript:void(0)) Yeah, that's why I often save context once there is enough information for work to be done. Then, once I notice regression in quality, I do a summary of work done (still could be a low quality) and add it on top of previous checkpoint. ![Image 23](https://news.ycombinator.com/s.gif)[](https://news.ycombinator.com/vote?id=44567755&how=up&goto=item%3Fid%3D44564248#44567755)[Workaccount2](https://news.ycombinator.com/user?id=Workaccount2)[on July 15, 2025](https://news.ycombinator.com/item?id=44567755) | [prev](https://news.ycombinator.com/item?id=44564248#44569139) | [next](https://news.ycombinator.com/item?id=44564248#44571839)[[–]](javascript:void(0)) What's really needed is a way to easily prune context. If I could go and manually manage the entire chat with a model, I could squeeze way more juice out of a typical ~200k token coding session. Instead I have a good instance going, but the model fumbles for 20k tokens and then that session heavily rotted. Let me cut it out! ![Image 24](https://news.ycombinator.com/s.gif)[](https://news.ycombinator.com/vote?id=44567774&how=up&goto=item%3Fid%3D44564248#44567774)[aaronblohowiak](https://news.ycombinator.com/user?id=aaronblohowiak)[on July 15, 2025](https://news.ycombinator.com/item?id=44567774) | [parent](https://news.ycombinator.com/item?id=44564248#44567755) | [next](https://news.ycombinator.com/item?id=44564248#44570819)[[–]](javascript:void(0)) Even just a rollback to previous checkpoint would be killer frsture ![Image 25](https://news.ycombinator.com/s.gif)[](https://news.ycombinator.com/vote?id=44569286&how=up&goto=item%3Fid%3D44564248#44569286)[sevenseacat](https://news.ycombinator.com/user?id=sevenseacat)[on July 15, 2025](https://news.ycombinator.com/item?id=44569286) | [root](https://news.ycombinator.com/item?id=44564248#44567755) | [parent](https://news.ycombinator.com/item?id=44564248#44567774) | [next](https://news.ycombinator.com/item?id=44564248#44569991)[[–]](javascript:void(0)) Zed's agent mode lets you do this, don't know about others ![Image 26](https://news.ycombinator.com/s.gif)[](https://news.ycombinator.com/vote?id=44569991&how=up&goto=item%3Fid%3D44564248#44569991)[t55](https://news.ycombinator.com/user?id=t55)[on July 15, 2025](https://news.ycombinator.com/item?id=44569991) | [root](https://news.ycombinator.com/item?id=44564248#44567755) | [parent](https://news.ycombinator.com/item?id=44564248#44567774) | [prev](https://news.ycombinator.com/item?id=44564248#44569286) | [next](https://news.ycombinator.com/item?id=44564248#44570819)[[–]](javascript:void(0)) that's a standard feature in cursor, windsurf, etc. ![Image 27](https://news.ycombinator.com/s.gif)[](https://news.ycombinator.com/vote?id=44570819&how=up&goto=item%3Fid%3D44564248#44570819)[snickerdoodle12](https://news.ycombinator.com/user?id=snickerdoodle12)[on July 15, 2025](https://news.ycombinator.com/item?id=44570819) | [parent](https://news.ycombinator.com/item?id=44564248#44567755) | [prev](https://news.ycombinator.com/item?id=44564248#44567774) | [next](https://news.ycombinator.com/item?id=44564248#44573710)[[–]](javascript:void(0)) Local LLMs let you edit the context however you want, including the responses generated by the LLM so it will later think it said what you want it to say which can help put it on the right track. LLMs-as-a-service don't offer this because it makes it trivial to bypass their censoring. ![Image 28](https://news.ycombinator.com/s.gif)[](https://news.ycombinator.com/vote?id=44574359&how=up&goto=item%3Fid%3D44564248#44574359)[chrisweekly](https://news.ycombinator.com/user?id=chrisweekly)[on July 15, 2025](https://news.ycombinator.com/item?id=44574359) | [root](https://news.ycombinator.com/item?id=44564248#44567755) | [parent](https://news.ycombinator.com/item?id=44564248#44570819) | [next](https://news.ycombinator.com/item?id=44564248#44573710)[[–]](javascript:void(0)) I've heard it repeated so many times that once things start to go sideways, trying to get back on track is a mistake. Have you had real-world success hacking context using rewritten responses? ![Image 29](https://news.ycombinator.com/s.gif)[](https://news.ycombinator.com/vote?id=44573710&how=up&goto=item%3Fid%3D44564248#44573710)[steveklabnik](https://news.ycombinator.com/user?id=steveklabnik)[on July 15, 2025](https://news.ycombinator.com/item?id=44573710) | [parent](https://news.ycombinator.com/item?id=44564248#44567755) | [prev](https://news.ycombinator.com/item?id=44564248#44570819) | [next](https://news.ycombinator.com/item?id=44564248#44567781)[[–]](javascript:void(0)) I have experimented with "hey claude i am about to reset your context, please give me a prompt that will allow you to continue your work" and then reviewing that and tweaking it before feeding it back in. ![Image 30](https://news.ycombinator.com/s.gif)[](https://news.ycombinator.com/vote?id=44567781&how=up&goto=item%3Fid%3D44564248#44567781)[lordswork](https://news.ycombinator.com/user?id=lordswork)[on July 15, 2025](https://news.ycombinator.com/item?id=44567781) | [parent](https://news.ycombinator.com/item?id=44564248#44567755) | [prev](https://news.ycombinator.com/item?id=44564248#44573710) | [next](https://news.ycombinator.com/item?id=44564248#44571839)[[–]](javascript:void(0)) /compress is the command to do this in most cli agents ![Image 31](https://news.ycombinator.com/s.gif)[](https://news.ycombinator.com/vote?id=44569281&how=up&goto=item%3Fid%3D44564248#44569281)[sevenseacat](https://news.ycombinator.com/user?id=sevenseacat)[on July 15, 2025](https://news.ycombinator.com/item?id=44569281) | [root](https://news.ycombinator.com/item?id=44564248#44567755) | [parent](https://news.ycombinator.com/item?id=44564248#44567781) | [next](https://news.ycombinator.com/item?id=44564248#44571839)[[–]](javascript:void(0)) That will reduce the context to a summary, not prune a bunch of irrelevant stuff ![Image 32](https://news.ycombinator.com/s.gif)[](https://news.ycombinator.com/vote?id=44571839&how=up&goto=item%3Fid%3D44564248#44571839)[boesboes](https://news.ycombinator.com/user?id=boesboes)[on July 15, 2025](https://news.ycombinator.com/item?id=44571839) | [prev](https://news.ycombinator.com/item?id=44564248#44567755) | [next](https://news.ycombinator.com/item?id=44564248#44568618)[[–]](javascript:void(0)) Claude code looses the ability to distinguish between it's own mistakes and my instructions. Once it gets confused, start over. The longer the sessions, the more it starts to go in loops or just decides that the test was already broken (despite it breaking it in this session) and that it will just ignore it. I'm sure it's all my poor prompting and context, but it really seems like Claude has lost 30 iq points last few weeks. ![Image 33](https://news.ycombinator.com/s.gif)[](https://news.ycombinator.com/vote?id=44573839&how=up&goto=item%3Fid%3D44564248#44573839)[vevoe](https://news.ycombinator.com/user?id=v

[Showing characters 14,000-24,000 of 46,492. Call read_url with start=24000 to read the next part.]
```

## Turn 9

_Model call: 45,073 input tokens, 780 output tokens_

**Tool call** `web_search` (id `call-b4011b27-5d9b-44c6-9ec5-934456b058b6`):

```json
{
  "query": "Shi \"Large Language Models Can Be Easily Distracted by Irrelevant Context\" ICML 2023 findings"
}
```
**Tool call** `web_search` (id `call-83958030-9798-4135-a3d3-24199e79bd9b`):

```json
{
  "query": "models perform better shuffled incoherent haystack than coherent text long context finding replication"
}
```
**Tool result** `web_search` (id `call-b4011b27-5d9b-44c6-9ec5-934456b058b6`, 5,838 characters):

```
Search results for "Shi "Large Language Models Can Be Easily Distracted by Irrelevant Context" ICML 2023 findings" (searched 2026-11-26):

[1] Large Language Models Can Be Easily Distracted by Irrelevant Context
URL: https://proceedings.mlr.press/v202/shi23a.html
Excerpt: \[edit]

# Large Language Models Can Be Easily Distracted by Irrelevant Context

Proceedings of the 40th International Conference on Machine Learning, PMLR 202:31210-31227, 2023.

#### Abstract

Large language models have achieved impressive performance on various natural language processing tasks. However, so far they have been evaluated primarily on benchmarks where all information in the input context is relevant for solving the task. In this work, we investigate the [...] distractibilityof large language models, i.e., how the model prediction can be distracted by irrelevant context. In particular, we introduce Grade-School Math with Irrelevant Context (GSM-IC), an arithmetic reasoning dataset with irrelevant information in the problem description. We use this benchmark to measure the distractibility of different prompting techniques for large language models, and find that the model is easily distracted by irrelevant information. We also identify several [...] identify several approaches for mitigating this deficiency, such as decoding with self-consistency and adding to the prompt an instruction that tells the language model to ignore the irrelevant information.

[2] Large language models can be easily distracted by irrelevant context | Proceedings of the 40th International Conference on Machine Learning
URL: https://dl.acm.org/doi/10.5555/3618408.3619699
Excerpt: ## Cited By

View all [...] - Sun KZeng YLiu FCai LLiao DXu JAlameda-Pineda XToni LMuchaluat-Saade DJin QOria VDantcheva AChen CMagalhaes JFarias MYan JZhang Z(2026)From Level 1 to Victory: Progressive VLM-based Game Agents via Adaptive Multimodal WalkthroughsProceedings of the 34th ACM International Conference on Multimedia10.1145/3767308.3835657(9196-9204)Online publication date: 10-Nov-2026 [...] - Parry ALionis EGanguly DMacAvaney SMoffat AScholer FBast HNajork MZhang M(2026)Towards a Relevance Posterior in Neural Information AccessProceedings of the 49th International ACM SIGIR Conference on Research and Development in Information Retrieval10.1145/3805712.3808541(2696-2707)Online publication date: 20-Jul-2026

[3] NTT Researchers Advance AI and Machine Learning Accuracy, Security and Cost Effectiveness at ICML 2025
URL: https://finance.yahoo.com/news/ntt-researchers-advance-ai-machine-120000647.html
Excerpt: factual recall and reasoning performance, showing that KE "inadvertently affects representations of entities beyond the targeted one, distorting relevant structures that allow a model to infer unseen knowledge about an entity." [...] In the paper "Representation Shattering in Transformers: A Synthetic Study with Knowledge Editing,"1 researchers explored the question of why Knowledge Editing (KE) algorithms—algorithms that alter LLMs' weights to fix incorrect, outdated or unwanted factual associations—can negatively impact models' factual recall accuracy and reasoning abilities. Researchers demonstrated that a phenomenon they call "representation shattering" is responsible for this degradation in models' factual recall and [...] - NTT Research and NTT R&D scientists presented 12 papers at ICML 2025, one of the world's most prestigious conferences on AI and machine learning.
- Three papers co-authored by NTT Research Physics of AI Group scientists included new findings on why algorithms designed to improve LLM accuracy and factual associations can negatively impact models' factual recall and reasoning abilities.

[4] Now Hiring: 25,000 Large Language Models Llm Jobs | Indeed
URL: https://www.indeed.com/q-large-language-models-llm-jobs.html
Excerpt: We're looking for Chinese language specialists who live and breathe the complexities of Chinese grammar, syntax, morphology, semantics, phonetics, and pragmatics. You'll challenge advanced language models on topics like tonal variations, Simplified vs. Traditional characters, regional dialects, Chinese idioms, sentence structure, and cultural context—documenting every failure mode so we can harden model reasoning. [...] We're looking for Chinese language specialists who live and breathe the complexities of Chinese grammar, syntax, morphology, semantics, phonetics, and pragmatics. You'll challenge advanced language models on topics like tonal variations, Simplified vs. Traditional characters, regional dialects, Chinese idioms, sentence structure, and cultural context—documenting every failure mode so we can harden model reasoning. [...] - - Large‑scale language models are evolving from clever chatbots into powerful engines of linguistic discovery.
  - A master's or PhD in Chinese language, linguistics,…
- Large‑scale
- - Large‑scale language models are evolving from clever chatbots into powerful engines of linguistic discovery.
  - On a typical day, you will converse with the model…
- Large‑scale

[5] Now Hiring: 23,000 Ai Large Language Models Llms Prompt Jobs | Indeed
URL: https://www.indeed.com/q-ai-large-language-models-llms-prompt-jobs.html
Excerpt: - MeridialRemote
  
  - Large‑scale language models are evolving from clever chatbots into powerful engines of linguistic discovery.
  - On a typical day, you will converse with the model…
- Large‑scale [...] - Large‑scale
- - We're looking for a highly skilled Mongolian language specialist who can bring linguistic depth, cultural context, and precision to training data.
- We're looking for a highly skilled Mongolian
- - Large‑scale language models are evolving from clever chatbots into powerful engines of linguistic discovery.
  - On a typical day, you will converse with the model…
- Large‑scale
```
**Tool result** `web_search` (id `call-83958030-9798-4135-a3d3-24199e79bd9b`, 7,635 characters):

```
Search results for "models perform better shuffled incoherent haystack than coherent text long context finding replication" (searched 2026-11-26):

[1] The Quest for Needles in the Haystack: Why LLM Evaluation Needs This Test | by Chris Zhang | Medium
URL: https://zhanghaolin66.medium.com/the-quest-for-needles-in-the-haystack-why-llm-evaluation-needs-this-test-1c75ba4bd917
Excerpt: One recurring empirical pattern: models tend to better retrieve needles placed near the end (or the very beginning) of the context. If the needle is buried in the middle, performance often drops. (Sometimes models “forget” the middle as the haystack grows).

As context length increases, the retrieval accuracy curves typically degrade. Even models designed for long contexts see fall-offs at extreme lengths. [...] By sweeping the context length (how big the haystack is) and the depth/position (how deeply buried the needle is), you can map model performance as you stress it. The hidden fact might be easy to retrieve if it’s near the end, but if it’s buried deep in the middle of a massive document, good models should still find it — barring memory or attention degradation. [...] A challenge: what if the haystack text contains sentences that are semantically similar (but not identical) to the needle? The model might be misled (“semantic masking”). A recent paper introduces a Needle-in-a-Haystack QA pipeline that accounts for this effect, showing that semantic interference can hurt retrieval more than sheer context length.

[2] [PDF] Multilingual Needle in a Haystack: Investigating Long-Context ...
URL: https://aclanthology.org/2025.naacl-long.267.pdf
Excerpt: Our findings show that all models struggle with longer contexts, exhibiting significant drops in accuracy beyond their effective lengths.
Figure 1 shows the monolingual (both needle and distractors in the same language) performance of different models on the MLNeedle test. Models consistently perform better in English than non-English languages. In the following sections, we will investigate the effect of modulating the position and language of the needle. [...] Furthermore, Liu et al. (2023) highlighted a major problem faced by LLMs while handling long contexts: a marked decline in performance when the relevant information is located in the 5165 middle of a long input context. The performance curve is characteristically “U-shaped", where models exhibit better accuracy when the relevant information is at the beginning or end of the context, underscoring the challenges LLMs face in maintaining attention and relevance throughout an entire input sequence. [...] Through a series of controlled experiments, we investigated how changes in the language and position of relevant information in a long-context affects the LLMs’ retrieval performance. Our findings revealed that LLMs exhibit significant sensitivity to both the language and position of the relevant information, particularly struggling when the relevant content is in non-Latin languages or positioned in the middle of a long context. Conversely, the models Figure 5: Exact accuracy of models on

[3] NoLiMa: Long-Context Evaluation Beyond Literal Matching
URL: https://arxiv.org/html/2502.05167v2
Excerpt: Recent large language models (LLMs) support long contexts ranging from 128K to 1M tokens. A popular method for evaluating these capabilities is the needle-in-a-haystack (NIAH) test, which involves retrieving a “needle” (relevant information) from a “haystack” (long irrelevant context). Extensions of this approach include increasing distractors, fact chaining, and in-context reasoning. However, in these benchmarks, models can exploit existing literal matches between the needle and haystack to [...] and haystack to simplify the task. To address this, we introduce NoLiMa, a benchmark extending NIAH with a carefully designed needle set, where questions and needles have minimal lexical overlap, requiring models to infer latent associations to locate the needle within the haystack. We evaluate 12 popular LLMs that claim to support contexts of at least 128K tokens. While they perform well in short contexts (1K), performance degrades significantly as context length increases. At 32K, for [...] et al., 2024). To evaluate these models’ effectiveness in handling long contexts, several benchmarks have been developed. One prominent benchmark is Needle-in-a-Haystack (NIAH), which tests a model’s ability to search for and retrieve a specific fact (the “needle”) hidden within irrelevant information (the “haystack”)(Kamradt, 2023; Mohtashami & Jaggi, 2023). While the baseline NIAH task assesses surface-level retrieval capabilities, recent adaptations have increased its complexity. These

[4] Multi Needle in a Haystack
URL: https://www.langchain.com/blog/multi-needle-in-a-haystack
Excerpt: ## Conclusion

The emergence of long context LLMs is extremely promising. In order to use them with or in place of external retrieval systems, it is critical to understand their limitations. The `Multi-Needle + Reasoning` benchmark can characterize the performance of long context retrieval relative to using a traditional RAG approach.

We can draw a few general insights, but further testing is needed: [...] ## Overview

Interest in long context LLMs is surging as context windows expand to 1M tokens. One of the most popular and cited benchmarks for long context LLM retrieval is Greg Kamradt's Needle in A Haystack: a fact (needle) is injected into a (haystack) of context (e.g., Paul Graham essays) and the LLM is asked a question related to this fact. This explores retrieval across context length and document placement. [...] We evaluate the ability of GPT4 (128k token context length) to retrieve 1, 3, or 10 needles in a single turn for small (1000 token) and large (120,000 token) context lengths. All commands run are here. All resulting generations with public links to LangSmith traces are here. Here is a summary figure of our results:

There are clear observations:

 Performance degrades at the number of needles increases from 1 to 10
 Performance degrades as the context increases from 1000 to 120,000 tokens

[5] Lost in the Middle: How Language Models Use Long Contexts Paper Reading
URL: https://www.youtube.com/watch?v=hBgzpw11-AQ
Excerpt: [1:35] they use it in general. And so this paper really um aims to address those and they found some really key uh limitations if you will. So the first
[1:43] one is going to be that uh models perform better when the relevant context is at the beginning or the end of the input context. The second is that the
[1:51] performance degrades when the relevant context is in the middle um hence the name lost in the middle here. And then uh the last thing is that as the um [...] [5:28] Ignore me. Chat, [laughter] no GPT 3.5, um, performance on multi-document question is actually lower than its performance with predicting without any
[5:36] documents. And I thought that was absolutely wild. Um, so I definitely think that's something to pay attention to. I've had the thought that the more
[5:45] context you give these models, the better that they're going to perform. [...] [26:08] task to really just make it like, you know, a very simple retrieval um experiment. So, it seems like when you really strip everything down, Claude's
[26:16] clearly the best at retrieving things, but it seems like maybe cloth gets a little bit more confused when you actually start asking it and you're passing it, you know, real natural
[26:24] language. Um, so I think it's interesting. I think again there should be um more done um and maybe more
```

## Turn 10

_Model call: 48,811 input tokens, 3,354 output tokens_

**Tool call** `assess_credibility` (id `call-08c4da2b-837f-45a3-a2d7-05f37ca4f950`):

```json
{
  "evaluation": {
    "source_url": "https://research.trychroma.com/context-rot",
    "source_type": "corporate_blog",
    "author": {
      "name": "Kelly Hong, Anton Troynikov, Jeff Huber (Chroma)",
      "credentials": "Kelly Hong: researcher at Chroma (joined Jan 2025), studied computer science at UC Berkeley, on a gap year from school; earlier work on generative benchmarking at Chroma (per TWIML bio page and MLOps Community reading-group page). Anton Troynikov: co-founder/CTO of Chroma (now advisor), M.Sc. robotics at TU Munich, ex-Meta research engineer, ex-Nuro (per LinkedIn via search results, Software Engineering Daily, ai.engineer). Jeff Huber: co-founder and CEO of Chroma, background in ML/computer vision, previously founded Standard Cyborg (Madrona podcast, ai.engineer). All three are Chroma employees/affiliates, so all have a stake in company narratives.",
      "credibility_assessment": "The authors are identifiable and technically credible for this topic: two senior engineers/founders of an AI-infrastructure company and a research staffer with relevant evaluation experience. They have direct hands-on access to the models and build the harnesses themselves. However, none has a PhD-level publication record in long-context NLP that I could find, and all are employed by or affiliated with the company whose commercial interest the findings support. Expertise supports trusting the engineering, but not treating the report as independent scholarship."
    },
    "publication": {
      "name": "Chroma (trychroma.com research site)",
      "reputation": "Chroma Inc. is a venture-funded, San Francisco-based AI search / vector database company (open-source ChromaDB; ~$18M seed round in 2023; investors include Naval Ravikant, Nat Friedman, Daniel Gross per Business Insider and Tavily company profile). Its research site publishes technical reports on retrieval and context (chunking, embedding adapters, generative benchmarking, Context-1). The reports are widely read and cited: the 'context rot' report circulated on Hacker News (260 points, July 2025), was covered by Understanding AI and Business Insider-adjacent commentary, and is cited in later arXiv papers (e.g., arXiv:2508.21433). I found no retractions, corrections or credibility scandals; the one recurring criticism is the company's commercial incentive toward retrieval-based solutions.",
      "editorial_process": "unknown"
    },
    "content_analysis": {
      "claims_checked": [
        {
          "claim": "Even on tightly controlled simple tasks, LLM performance degrades non-uniformly as input length increases, across 18 models including GPT-4.1, Claude 4, Gemini 2.5 and Qwen3.",
          "status": "corroborated",
          "evidence": "Peer-reviewed: Liu et al., 'Lost in the Middle' (TACL 2024) finds performance degrades with position/length even for explicitly long-context models — https://aclanthology.org/2024.tacl-1.9 and https://arxiv.org/abs/2307.03172. Independent documentation of the phenomenon: Anthropic, 'Effective context engineering for AI agents' (performance degradation 'emerges across all models') — https://www.anthropic.com/research/effective-context-engineering-for-ai-agents; Understanding AI (Nov 2025) — https://www.understandingai.org/p/context-rot-the-emerging-challenge ; multilingual NIAH (NAACL 2025) reports accuracy drops beyond effective context length — https://aclanthology.org/2025.naacl-long.267.pdf"
        },
        {
          "claim": "Performance degrades faster with input length when needle-question pairs are only semantically (not lexically) similar.",
          "status": "corroborated",
          "evidence": "NoLiMa (Modarressi et al., arXiv:2502.05167) reports large drops at 32K tokens with minimal lexical overlap between question and needle — https://arxiv.org/html/2502.05167v2 ; Understanding AI summarises NoLiMa numbers (e.g., GPT-4o 99%→70%, Claude 3.5 Sonnet 88%→30%) — https://www.understandingai.org/p/context-rot-the-emerging-challenge"
        },
        {
          "claim": "Adding distractors (topically related but wrong passages) lowers performance relative to a needle-only baseline, and the impact is non-uniform and grows with input length.",
          "status": "corroborated",
          "evidence": "Shi et al., 'Large Language Models Can Be Easily Distracted by Irrelevant Context' (ICML 2023, PMLR 202:31210-31227) establishes distractibility by irrelevant context — https://proceedings.mlr.press/v202/shi23a.html ; LangChain Multi-Needle-in-a-Haystack shows degradation as the number of needles/context grows — https://www.langchain.com/blog/multi-needle-in-a-haystack . The specific claim that the distractor effect amplifies with length for 2025 frontier models is only shown in Chroma's own experiments."
        },
        {
          "claim": "Shuffling the haystack to destroy local coherence consistently improves performance, across all 18 models.",
          "status": "no_evidence_found",
          "evidence": "I searched for independent replication or contradiction ('shuffled incoherent haystack coherent text long context') and found only secondary blog posts repeating Chroma's finding (e.g., https://upsolve.ai/blog/context-rot) and no peer-reviewed study testing it. The report itself flags the mechanism as unexplained. Unverified either way."
        }
      ],
      "claims_supported_by_evidence": true,
      "sources_cited": true,
      "corroborated_by_other_sources": true,
      "contradicted_by_other_sources": false,
      "primary_vs_secondary": "primary_source",
      "funding_or_sponsorship": "Funded by Chroma Inc. (the authors are Chroma staff/affiliates); no explicit funding or conflict-of-interest statement on the page. Chroma sells search/retrieval infrastructure, which is an indirect commercial beneficiary of findings against stuffing context windows. The page promotes Chroma ('Chroma is Hiring'). Datasets and code were released publicly (github.com/chroma-core/context-rot) and an external expert (Kiran Vodrahalli, Google DeepMind) is credited in a footnote for clarifications.",
      "bias_and_tone": "Tone is technical and measured: methods, parameters, seeds, judge-alignment procedure and failure examples are all disclosed, and a Limitations section says the work does not explain mechanisms and that only two haystack topics were used. Language is not emotional or advocacy-driven, and no product is being sold in the text. The main bias risk is structural rather than tonal: a retrieval-infrastructure vendor publishing evidence that long context alone is unreliable, which supports RAG-style retrieval. Hacker News commenters raised exactly this (comment in https://news.ycombinator.com/item?id=44564248: 'they benefit from convincing people not to dump everything in context'), and a Medium summary (https://cobusgreyling.medium.com/llm-context-rot-28a6d0399655) says the study's origins 'warrant scrutiny'. Counterarguments are largely absent from the report, though its own limitations are stated.",
      "date_published": "Published 14 July 2025 (Hacker News submission 14 July 2025; Chroma research index lists 'July 2025'); a footnote records a clarification added 16 July 2025 by Kiran Vodrahalli. No visible 'last updated' date otherwise. As of 26 November 2026 the report is ~16 months old and the models tested (GPT-4.1, Claude 4/Opus 4, Gemini 2.5, Qwen3) are no longer frontier, so specific model rankings and thresholds are dated although the phenomenon is still widely cited."
    },
    "transparency_score": 4,
    "overall_credibility": "high",
    "reasoning": "Named authors with relevant technical roles (two Chroma founders, one research staffer), a detailed and reproducible method (18 models, 8 input lengths, 11 needle positions, ~194,480 calls, temperature 0, five embedding models, a GPT-4.1 judge calibrated to >0.99 agreement with ~500-600 human labels), public code and datasets, an external expert credited, and an explicit Limitations section. The core findings (non-uniform degradation with input length, worse degradation for semantic/non-lexical matches, distractor sensitivity) are independently corroborated by peer-reviewed work (Lost in the Middle, TACL 2024; Shi et al., ICML 2023) and by NoLiMa and Anthropic's own engineering write-up; I found no credible source contradicting them. Deductions: it is a company technical report, not peer reviewed, written by people whose employer sells the alternative to long context, with no funding/conflict statement; and the most surprising result (shuffled haystacks beating coherent ones) has no independent replication that I could find. Hence high, but for the empirical findings rather than as a neutral authority.",
    "evidence_urls": [
      "https://research.trychroma.com/context-rot",
      "https://research.trychroma.com/",
      "https://github.com/chroma-core/context-rot",
      "https://news.ycombinator.com/item?id=44564248",
      "https://www.understandingai.org/p/context-rot-the-emerging-challenge",
      "https://www.anthropic.com/research/effective-context-engineering-for-ai-agents",
      "https://arxiv.org/abs/2307.03172",
      "https://aclanthology.org/2024.tacl-1.9",
      "https://arxiv.org/html/2502.05167v2",
      "https://proceedings.mlr.press/v202/shi23a.html",
      "https://www.langchain.com/blog/multi-needle-in-a-haystack",
      "https://aclanthology.org/2025.naacl-long.267.pdf",
      "https://twimlai.com/network/kelly-hong",
      "https://home.mlops.community/public/videos/context-rot-reading-group",
      "https://www.linkedin.com/in/antontroynikov",
      "https://softwareengineeringdaily.com/podcasts/chromas-vector-database-with-anton-troynikov",
      "https://ai.engineer/speakers/anton-troynikov",
      "https://www.madrona.com/chromas-jeff-huber-on-vector-databases-and-getting-ai-into-production",
      "https://ai.engineer/speakers/jeff-huber",
      "https://www.businessinsider.com/vector-database-startup-chroma-raises-seed-funding-generative-artificial-intelligence-2023-4?op=1",
      "https://cobusgreyling.medium.com/llm-context-rot-28a6d0399655",
      "https://upsolve.ai/blog/context-rot",
      "https://www.tinyfish.ai/blog/context-rot",
      "https://tavily.com/knowledge/company/TSeGoNnNUIKP"
    ]
  }
}
```
**Tool result** `assess_credibility` (id `call-08c4da2b-837f-45a3-a2d7-05f37ca4f950`, 10,351 characters):

```
{
  "status": "evaluation_recorded",
  "evaluation": {
    "source_url": "https://research.trychroma.com/context-rot",
    "source_type": "corporate_blog",
    "author": {
      "name": "Kelly Hong, Anton Troynikov, Jeff Huber (Chroma)",
      "credentials": "Kelly Hong: researcher at Chroma (joined Jan 2025), studied computer science at UC Berkeley, on a gap year from school; earlier work on generative benchmarking at Chroma (per TWIML bio page and MLOps Community reading-group page). Anton Troynikov: co-founder/CTO of Chroma (now advisor), M.Sc. robotics at TU Munich, ex-Meta research engineer, ex-Nuro (per LinkedIn via search results, Software Engineering Daily, ai.engineer). Jeff Huber: co-founder and CEO of Chroma, background in ML/computer vision, previously founded Standard Cyborg (Madrona podcast, ai.engineer). All three are Chroma employees/affiliates, so all have a stake in company narratives.",
      "credibility_assessment": "The authors are identifiable and technically credible for this topic: two senior engineers/founders of an AI-infrastructure company and a research staffer with relevant evaluation experience. They have direct hands-on access to the models and build the harnesses themselves. However, none has a PhD-level publication record in long-context NLP that I could find, and all are employed by or affiliated with the company whose commercial interest the findings support. Expertise supports trusting the engineering, but not treating the report as independent scholarship."
    },
    "publication": {
      "name": "Chroma (trychroma.com research site)",
      "reputation": "Chroma Inc. is a venture-funded, San Francisco-based AI search / vector database company (open-source ChromaDB; ~$18M seed round in 2023; investors include Naval Ravikant, Nat Friedman, Daniel Gross per Business Insider and Tavily company profile). Its research site publishes technical reports on retrieval and context (chunking, embedding adapters, generative benchmarking, Context-1). The reports are widely read and cited: the 'context rot' report circulated on Hacker News (260 points, July 2025), was covered by Understanding AI and Business Insider-adjacent commentary, and is cited in later arXiv papers (e.g., arXiv:2508.21433). I found no retractions, corrections or credibility scandals; the one recurring criticism is the company's commercial incentive toward retrieval-based solutions.",
      "editorial_process": "unknown"
    },
    "content_analysis": {
      "claims_checked": [
        {
          "claim": "Even on tightly controlled simple tasks, LLM performance degrades non-uniformly as input length increases, across 18 models including GPT-4.1, Claude 4, Gemini 2.5 and Qwen3.",
          "status": "corroborated",
          "evidence": "Peer-reviewed: Liu et al., 'Lost in the Middle' (TACL 2024) finds performance degrades with position/length even for explicitly long-context models — https://aclanthology.org/2024.tacl-1.9 and https://arxiv.org/abs/2307.03172. Independent documentation of the phenomenon: Anthropic, 'Effective context engineering for AI agents' (performance degradation 'emerges across all models') — https://www.anthropic.com/research/effective-context-engineering-for-ai-agents; Understanding AI (Nov 2025) — https://www.understandingai.org/p/context-rot-the-emerging-challenge ; multilingual NIAH (NAACL 2025) reports accuracy drops beyond effective context length — https://aclanthology.org/2025.naacl-long.267.pdf"
        },
        {
          "claim": "Performance degrades faster with input length when needle-question pairs are only semantically (not lexically) similar.",
          "status": "corroborated",
          "evidence": "NoLiMa (Modarressi et al., arXiv:2502.05167) reports large drops at 32K tokens with minimal lexical overlap between question and needle — https://arxiv.org/html/2502.05167v2 ; Understanding AI summarises NoLiMa numbers (e.g., GPT-4o 99%→70%, Claude 3.5 Sonnet 88%→30%) — https://www.understandingai.org/p/context-rot-the-emerging-challenge"
        },
        {
          "claim": "Adding distractors (topically related but wrong passages) lowers performance relative to a needle-only baseline, and the impact is non-uniform and grows with input length.",
          "status": "corroborated",
          "evidence": "Shi et al., 'Large Language Models Can Be Easily Distracted by Irrelevant Context' (ICML 2023, PMLR 202:31210-31227) establishes distractibility by irrelevant context — https://proceedings.mlr.press/v202/shi23a.html ; LangChain Multi-Needle-in-a-Haystack shows degradation as the number of needles/context grows — https://www.langchain.com/blog/multi-needle-in-a-haystack . The specific claim that the distractor effect amplifies with length for 2025 frontier models is only shown in Chroma's own experiments."
        },
        {
          "claim": "Shuffling the haystack to destroy local coherence consistently improves performance, across all 18 models.",
          "status": "no_evidence_found",
          "evidence": "I searched for independent replication or contradiction ('shuffled incoherent haystack coherent text long context') and found only secondary blog posts repeating Chroma's finding (e.g., https://upsolve.ai/blog/context-rot) and no peer-reviewed study testing it. The report itself flags the mechanism as unexplained. Unverified either way."
        }
      ],
      "claims_supported_by_evidence": true,
      "sources_cited": true,
      "corroborated_by_other_sources": true,
      "contradicted_by_other_sources": false,
      "primary_vs_secondary": "primary_source",
      "funding_or_sponsorship": "Funded by Chroma Inc. (the authors are Chroma staff/affiliates); no explicit funding or conflict-of-interest statement on the page. Chroma sells search/retrieval infrastructure, which is an indirect commercial beneficiary of findings against stuffing context windows. The page promotes Chroma ('Chroma is Hiring'). Datasets and code were released publicly (github.com/chroma-core/context-rot) and an external expert (Kiran Vodrahalli, Google DeepMind) is credited in a footnote for clarifications.",
      "bias_and_tone": "Tone is technical and measured: methods, parameters, seeds, judge-alignment procedure and failure examples are all disclosed, and a Limitations section says the work does not explain mechanisms and that only two haystack topics were used. Language is not emotional or advocacy-driven, and no product is being sold in the text. The main bias risk is structural rather than tonal: a retrieval-infrastructure vendor publishing evidence that long context alone is unreliable, which supports RAG-style retrieval. Hacker News commenters raised exactly this (comment in https://news.ycombinator.com/item?id=44564248: 'they benefit from convincing people not to dump everything in context'), and a Medium summary (https://cobusgreyling.medium.com/llm-context-rot-28a6d0399655) says the study's origins 'warrant scrutiny'. Counterarguments are largely absent from the report, though its own limitations are stated.",
      "date_published": "Published 14 July 2025 (Hacker News submission 14 July 2025; Chroma research index lists 'July 2025'); a footnote records a clarification added 16 July 2025 by Kiran Vodrahalli. No visible 'last updated' date otherwise. As of 26 November 2026 the report is ~16 months old and the models tested (GPT-4.1, Claude 4/Opus 4, Gemini 2.5, Qwen3) are no longer frontier, so specific model rankings and thresholds are dated although the phenomenon is still widely cited."
    },
    "transparency_score": 4,
    "overall_credibility": "high",
    "reasoning": "Named authors with relevant technical roles (two Chroma founders, one research staffer), a detailed and reproducible method (18 models, 8 input lengths, 11 needle positions, ~194,480 calls, temperature 0, five embedding models, a GPT-4.1 judge calibrated to >0.99 agreement with ~500-600 human labels), public code and datasets, an external expert credited, and an explicit Limitations section. The core findings (non-uniform degradation with input length, worse degradation for semantic/non-lexical matches, distractor sensitivity) are independently corroborated by peer-reviewed work (Lost in the Middle, TACL 2024; Shi et al., ICML 2023) and by NoLiMa and Anthropic's own engineering write-up; I found no credible source contradicting them. Deductions: it is a company technical report, not peer reviewed, written by people whose employer sells the alternative to long context, with no funding/conflict statement; and the most surprising result (shuffled haystacks beating coherent ones) has no independent replication that I could find. Hence high, but for the empirical findings rather than as a neutral authority.",
    "evidence_urls": [
      "https://research.trychroma.com/context-rot",
      "https://research.trychroma.com/",
      "https://github.com/chroma-core/context-rot",
      "https://news.ycombinator.com/item?id=44564248",
      "https://www.understandingai.org/p/context-rot-the-emerging-challenge",
      "https://www.anthropic.com/research/effective-context-engineering-for-ai-agents",
      "https://arxiv.org/abs/2307.03172",
      "https://aclanthology.org/2024.tacl-1.9",
      "https://arxiv.org/html/2502.05167v2",
      "https://proceedings.mlr.press/v202/shi23a.html",
      "https://www.langchain.com/blog/multi-needle-in-a-haystack",
      "https://aclanthology.org/2025.naacl-long.267.pdf",
      "https://twimlai.com/network/kelly-hong",
      "https://home.mlops.community/public/videos/context-rot-reading-group",
      "https://www.linkedin.com/in/antontroynikov",
      "https://softwareengineeringdaily.com/podcasts/chromas-vector-database-with-anton-troynikov",
      "https://ai.engineer/speakers/anton-troynikov",
      "https://www.madrona.com/chromas-jeff-huber-on-vector-databases-and-getting-ai-into-production",
      "https://ai.engineer/speakers/jeff-huber",
      "https://www.businessinsider.com/vector-database-startup-chroma-raises-seed-funding-generative-artificial-intelligence-2023-4?op=1",
      "https://cobusgreyling.medium.com/llm-context-rot-28a6d0399655",
      "https://upsolve.ai/blog/context-rot",
      "https://www.tinyfish.ai/blog/context-rot",
      "https://tavily.com/knowledge/company/TSeGoNnNUIKP"
    ]
  }
}
```

## Turn 11

_Model call: 54,610 input tokens, 3,820 output tokens_

**Tool call** `save_report` (id `call-f59893ca-12c4-4349-bc8d-24a3fddd510a`):

```json
{
  "filename": "chroma-context-rot.md",
  "markdown": "# Credibility Report: Context Rot: How Increasing Input Tokens Impacts LLM Performance\n\n**URL:** https://research.trychroma.com/context-rot (final URL: https://www.trychroma.com/research/context-rot)\n**Verdict:** High credibility\n**Evaluated:** 2026-11-26\n\n## Summary\n\nThis is a technical report published by Chroma (an AI search / vector-database company) on its research site, authored by Chroma researcher Kelly Hong together with co-founders Anton Troynikov and Jeff Huber, dated 14 July 2025. It reports four controlled experiments across 18 LLMs showing that model performance does not hold steady as input length grows: accuracy degrades non-uniformly, degrades faster when question and answer share no literal wording, and degrades when topically similar distractors are added. It is not peer reviewed, and the authors' employer sells retrieval infrastructure that benefits from the finding that stuffing a context window is unreliable — a conflict that Hacker News commenters raised immediately. Against that, the method is unusually transparent and replicable (public code, public datasets, published judge-alignment procedure, a Limitations section), and the three core findings are independently corroborated by peer-reviewed work — Liu et al., \"Lost in the Middle\" (TACL 2024) and Shi et al., ICML 2023 — as well as by NoLiMa and Anthropic's own engineering write-up. The one genuinely surprising result (shuffled haystacks beating coherent ones) has no independent replication I could find and should not be cited as established.\n\n## Author\n\nThree named authors appear on the page (and in the BibTeX block: `author = {Hong, Kelly and Troynikov, Anton and Huber, Jeff}`):\n\n- **Kelly Hong** — researcher at Chroma (joined January 2025); studied computer science at UC Berkeley and was on a gap year from school while working there; earlier Chroma work on generative benchmarking. Sourced from her TWIML speaker bio and the MLOps Community reading-group page, which carry the same biography as the video's speaker notes. She also posted the report on Hacker News (user `kellyhongsn`).\n- **Anton Troynikov** — co-founder and former CTO of Chroma (now an advisor), M.Sc. in robotics from TU Munich, previously research engineer at Meta and engineer at Nuro. Sourced from LinkedIn (via search result), Software Engineering Daily and ai.engineer speaker pages.\n- **Jeff Huber** — co-founder and CEO of Chroma, machine-learning/computer-vision background, previously founded Standard Cyborg. Sourced from the Madrona podcast page, ai.engineer speaker page and LinkedIn (via search result).\n\nAssessment: the authors are identifiable and have directly relevant hands-on engineering experience with the models and harnesses being tested. I found no PhD-level publication record in long-context NLP for any of them, and all three are Chroma employees or affiliates, so this is company research rather than independent scholarship. That is a real limitation on independence, not a reason to dismiss the work, since the method is fully disclosed.\n\n## Publication\n\nChroma Inc. (trychroma.com) is a venture-funded San Francisco company building open-source AI search infrastructure (ChromaDB); it raised an ~$18M seed round in 2023 (Business Insider; Tavily company profile). Its `/research` site publishes a series of in-house technical reports — Context-1 (March 2026), Context Rot (July 2025), Generative Benchmarking (April 2025), Evaluating Chunking Strategies (July 2024), Embedding Adapters (May 2024) — and prominently advertises that the company is hiring.\n\nThere is **no editorial-policy or peer-review page** in evidence; the research index simply lists \"Chroma Technical Reports\". So the editorial process is internal/self-published. Mitigating factors: the full codebase is public (github.com/chroma-core/context-rot), datasets are downloadable, the LLM-judge alignment procedure is documented, and an outside expert (Kiran Vodrahalli, Google DeepMind) is credited in a footnote for clarifications on the Latent List task. The report travelled widely (260 points on Hacker News, July 2025), was covered by Understanding AI, and is cited in later arXiv papers such as arXiv:2508.21433. I found no retraction, correction notice or credibility scandal.\n\n## Claims Checked\n\n| Claim | Status | Evidence |\n|---|---|---|\n| LLM performance degrades non-uniformly as input length increases, even on tightly controlled simple tasks, across 18 models (GPT-4.1, Claude 4, Gemini 2.5, Qwen3, etc.) | corroborated | Peer-reviewed: Liu et al., \"Lost in the Middle\" (TACL 2024) finds performance is highest at the start/end of context and degrades in the middle \"even for explicitly long-context models\" — https://aclanthology.org/2024.tacl-1.9, https://arxiv.org/abs/2307.03172. Anthropic's engineering post: degradation \"emerges across all models\" — https://www.anthropic.com/research/effective-context-engineering-for-ai-agents. Independent journalism: https://www.understandingai.org/p/context-rot-the-emerging-challenge. Multilingual NIAH (NAACL 2025) reports accuracy drops past effective context length — https://aclanthology.org/2025.naacl-long.267.pdf |\n| Degradation with length is steeper for low-similarity (semantic, non-lexical) question–needle pairs | corroborated | NoLiMa (Modarressi et al., arXiv:2502.05167) measures large drops at 32K tokens when question and needle share minimal wording — https://arxiv.org/html/2502.05167v2 ; summary figures (GPT-4o 99%→70%, Claude 3.5 Sonnet 88%→30%) in https://www.understandingai.org/p/context-rot-the-emerging-challenge |\n| Distractors (topically related but wrong passages) reduce performance versus a needle-only baseline, non-uniformly, and the effect grows with input length | corroborated | Shi et al., \"Large Language Models Can Be Easily Distracted by Irrelevant Context\", ICML 2023, PMLR 202:31210–31227 — https://proceedings.mlr.press/v202/shi23a.html ; LangChain's Multi-Needle-in-a-Haystack shows degradation as context/needle count rises — https://www.langchain.com/blog/multi-needle-in-a-haystack . The specific \"amplifies with length for 2025 frontier models\" version rests on Chroma's own experiments. |\n| Shuffling the haystack to remove logical flow consistently *improves* performance across all 18 models | no_evidence_found | Searched for independent replication or refutation (\"shuffled incoherent haystack / coherent text long context\") and found only secondary blogs restating Chroma's result (e.g., https://upsolve.ai/blog/context-rot); no peer-reviewed test either way. The report itself offers no mechanism. Treat as an unreplicated, single-lab observation. |\n\nNo claim was contradicted by a credible source; I found none.\n\n## Bias and Tone\n\nTone is technical and measured, not promotional. The report publishes its parameters (8 input lengths, 11 needle positions, ~194,480 LLM calls, temperature 0, five embedding models averaged for similarity, GPT-4.1 judge calibrated to >0.99 agreement against ~500–600 human-labelled outputs), shows raw failure examples, and includes a Limitations section that concedes it does not explain the mechanism and that only two haystack topics were used. Notably, where the needle–haystack similarity result was mixed, the authors say so explicitly (\"testing across only two topics is insufficient to draw a generalizable conclusion\").\n\nThe bias risk is structural, not rhetorical: Chroma sells search and retrieval infrastructure, and a finding that \"more context is not uniformly better\" argues for retrieval-based pipelines. Hacker News commenters flagged this directly (\"they benefit from convincing people not to dump everything in context\" — https://news.ycombinator.com/item?id=44564248), and a widely shared Medium summary notes the study's origins \"warrant scrutiny\" (https://cobusgreyling.medium.com/llm-context-rot-28a6d0399655). Counter-evidence (e.g., cases where long context works well) is not discussed. There is a \"Chroma is Hiring\" call-to-action in the page. No funding or conflict-of-interest statement is provided.\n\n## Currency\n\nPublished 14 July 2025 (Hacker News submission date; Chroma's research index lists \"July 2025\"), with a footnote recording a clarification added 16 July 2025 by Kiran Vodrahalli of Google DeepMind. No later \"last updated\" date is shown. As of 26 November 2026 the report is roughly 16 months old: the model set (GPT-4.1, Claude Opus/Sonnet 4, Gemini 2.5, Qwen3) is no longer frontier, so specific model rankings, refusal rates and accuracy thresholds should be treated as historical. The general phenomenon is still being cited and discussed in late 2025 / 2026 material, so the conceptual contribution remains usable.\n\n## Structured Assessment\n\n| Field | Value |\n|---|---|\n| Source URL | https://research.trychroma.com/context-rot |\n| Source type | corporate_blog (company technical report) |\n| Author name | Kelly Hong, Anton Troynikov, Jeff Huber (all Chroma) |\n| Author credentials | Hong: Chroma researcher, UC Berkeley CS; Troynikov: Chroma co-founder/ex-CTO, M.Sc. robotics (TU Munich), ex-Meta research engineer; Huber: Chroma co-founder & CEO, ML/CV background. No long-context NLP publication record found; all affiliated with the company. |\n| Author credibility assessment | Identifiable, technically qualified practitioners with direct access to the models; not independent scholars, so trust rests on their disclosed method plus external corroboration. |\n| Publication | Chroma (trychroma.com research site) |\n| Publication reputation | VC-funded AI search/vector-DB company; published series of technical reports; no corrections/retractions found; widely read and cited; commercial interest in retrieval-based solutions noted by critics. |\n| Editorial process | unknown (in-house technical report; no peer review or published editorial policy found) |\n| Claims supported by evidence in the source | true |\n| Sources cited | true (15 numbered references, codebase and datasets linked) |\n| Corroborated by other sources | true |\n| Contradicted by other sources | false |\n| Primary vs secondary | primary_source |\n| Funding / sponsorship | Chroma Inc. funds the work (authors are staff/affiliates); no explicit funding or COI statement; page includes a hiring ad. Code and data released publicly; outside expert credited for clarifications. |\n| Bias and tone | Neutral, methodical, limitations acknowledged; structural commercial interest in retrieval over long context; counterarguments not addressed. |\n| Date published | 14 July 2025; clarification added 16 July 2025; no further update. Model set now ~16 months out of date. |\n| Transparency score | 4 / 5 |\n| Overall credibility | high |\n\n## Can I cite this?\n\n**Cite it — but as a company technical report, and pair it with peer-reviewed work.**\n\nSuitable uses:\n- Citing the empirical claim that LLM performance degrades non-uniformly with input length, and that the degradation is worse for semantically matched (non-lexical) needles and when distractors are present. Cite it alongside Liu et al. (TACL 2024) or NoLiMa, so your claim does not rest on vendor research alone.\n- Citing the phenomena of *context engineering* and *context rot* as currently understood in industry practice, and for its dataset/code release as a reproducibility example.\n\nCite with caution:\n- Any specific model ranking or percentage (\"Claude abstains more\", \"GPT hallucinates more\", exact accuracy figures) — these are 2025-era snapshots from one lab, judged by an LLM judge.\n- The claim that shuffled haystacks outperform coherent ones. I found no independent replication; describe it as \"one report found\" rather than established fact.\n- Do not present it as peer-reviewed. Correct description: \"technical report, Chroma, July 2025\" (the report supplies its own BibTeX: `@techreport{hong2025context, ... institution = {Chroma}}`).\n\nFind a better source if:\n- You need a peer-reviewed citation for the general \"long context is used unevenly\" claim — use Liu et al., \"Lost in the Middle\" (TACL 2024, https://aclanthology.org/2024.tacl-1.9) or NoLiMa (https://arxiv.org/abs/2502.05167).\n- Your argument depends on an independent (non-vendor) evaluation of a *current* frontier model, since the model set here predates late-2025/2026 releases.\n\n## Sources Consulted\n\n1. https://research.trychroma.com/context-rot — the source itself; read in full across five parts (main claims, methods, results, limitations, references, appendix).\n2. https://research.trychroma.com/ — Chroma research index; confirms the report is listed as a \"Chroma Technical Report\", dated July 2025, among other in-house reports.\n3. https://github.com/chroma-core/context-rot — public replication codebase and BibTeX entry naming Hong, Troynikov and Huber.\n4. https://news.ycombinator.com/item?id=44564248 — Hacker News discussion (14 July 2025) by author `kellyhongsn`; contains practitioner anecdotes and the explicit commercial-incentive critique.\n5. https://www.understandingai.org/p/context-rot-the-emerging-challenge — independent Nov 2025 analysis of \"context rot\" citing Chroma's study; reports NoLiMa degradation numbers.\n6. https://www.anthropic.com/research/effective-context-engineering-for-ai-agents — Anthropic engineering post on attention budget and degradation across all models.\n7. https://aclanthology.org/2024.tacl-1.9 — Liu et al., \"Lost in the Middle\", TACL 2024 (peer reviewed).\n8. https://arxiv.org/abs/2307.03172 — arXiv version of the same paper, abstract confirming degradation for long-context models.\n9. https://arxiv.org/html/2502.05167v2 — NoLiMa: non-lexical needle-question pairs degrade sharply with context length.\n10. https://proceedings.mlr.press/v202/shi23a.html — Shi et al., ICML 2023, on distractibility by irrelevant context.\n11. https://www.langchain.com/blog/multi-needle-in-a-haystack — independent benchmark showing degradation as needles/context size grow.\n12. https://aclanthology.org/2025.naacl-long.267.pdf — Multilingual NIAH (NAACL 2025); accuracy drops beyond effective context length.\n13. https://twimlai.com/network/kelly-hong — Kelly Hong biography (Chroma researcher, UC Berkeley CS).\n14. https://home.mlops.community/public/videos/context-rot-reading-group — MLOps Community reading group with Kelly Hong; same bio, states Chroma is a vector-database company doing research \"on the side\".\n15. https://www.linkedin.com/in/antontroynikov — Anton Troynikov roles (Chroma founder/CTO to Feb 2025, then advisor; ex-Facebook Research, Nuro).\n16. https://softwareengineeringdaily.com/podcasts/chromas-vector-database-with-anton-troynikov — confirms Troynikov's founding role and computer-vision background.\n17. https://ai.engineer/speakers/anton-troynikov — further bio detail for Troynikov.\n18. https://www.madrona.com/chromas-jeff-huber-on-vector-databases-and-getting-ai-into-production — Jeff Huber as Chroma co-founder/CEO with ML background.\n19. https://ai.engineer/speakers/jeff-huber — Huber bio; Chroma raised an $18M seed round in 2023.\n20. https://www.businessinsider.com/vector-database-startup-chroma-raises-seed-funding-generative-artificial-intelligence-2023-4?op=1 — Chroma funding/ownership context.\n21. https://cobusgreyling.medium.com/llm-context-rot-28a6d0399655 — independent summary that questions the study's commercial origins.\n22. https://upsolve.ai/blog/context-rot — secondary blog restating Chroma's findings (including the shuffled-haystack result) without independent testing.\n23. https://www.tinyfish.ai/blog/context-rot — secondary blog; credits the report's design and reinterprets \"rot\" as signal-to-noise.\n24. https://tavily.com/knowledge/company/TSeGoNnNUIKP — Chroma company profile (private, San Francisco, funding, business model).\n"
}
```
**Tool result** `save_report` (id `call-f59893ca-12c4-4349-bc8d-24a3fddd510a`, 70 characters):

```
Saved the report to reports/chroma-context-rot.md (15,705 characters).
```

## Turn 12

_Model call: 58,459 input tokens, 223 output tokens_

**Assistant:**

**Verdict: High credibility.** Chroma's "Context Rot" is a company technical report (14 July 2025) by named, technically qualified authors — researcher Kelly Hong plus co-founders Anton Troynikov and Jeff Huber — with fully disclosed methods, public code and datasets, a calibrated LLM judge, and an explicit limitations section; its three core findings (non-uniform degradation with input length, worse degradation for semantically matched needles, distractor sensitivity) are independently corroborated by peer-reviewed work such as Liu et al.'s "Lost in the Middle" (TACL 2024), Shi et al. (ICML 2023) and NoLiMa. The caveats are that it is not peer reviewed, that the authors' employer sells retrieval infrastructure benefiting from the conclusion, and that the surprising "shuffled haystacks beat coherent ones" result has no independent replication — so cite it as a technical report alongside peer-reviewed sources, and treat the 2025 model rankings as dated. The report was saved as `chroma-context-rot.md`.


## Final output

**Verdict: High credibility.** Chroma's "Context Rot" is a company technical report (14 July 2025) by named, technically qualified authors — researcher Kelly Hong plus co-founders Anton Troynikov and Jeff Huber — with fully disclosed methods, public code and datasets, a calibrated LLM judge, and an explicit limitations section; its three core findings (non-uniform degradation with input length, worse degradation for semantically matched needles, distractor sensitivity) are independently corroborated by peer-reviewed work such as Liu et al.'s "Lost in the Middle" (TACL 2024), Shi et al. (ICML 2023) and NoLiMa. The caveats are that it is not peer reviewed, that the authors' employer sells retrieval infrastructure benefiting from the conclusion, and that the surprising "shuffled haystacks beat coherent ones" result has no independent replication — so cite it as a technical report alongside peer-reviewed sources, and treat the 2025 model rankings as dated. The report was saved as `chroma-context-rot.md`.

## Summary

- Turns (model calls): 12
- Tool calls: read_url x11, web_search x11, assess_credibility x1, save_report x1
- Tokens: 378,404 input (313,728 cached), 10,870 output
- Estimated cost: $0.0172
- Report: reports/chroma-context-rot.md
- URLs in chroma-context-rot.md not seen in any tool result: none
