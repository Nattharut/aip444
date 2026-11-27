# Credibility Report: Lost in the Middle: How Language Models Use Long Contexts

**URL:** https://arxiv.org/abs/2307.03172
**Verdict:** High credibility
**Evaluated:** 2026-11-26

## Summary

This is the arXiv abstract page for "Lost in the Middle: How Language Models Use Long Contexts" (Liu, Lin, Hewitt, Paranjape, Bevilacqua, Petroni and Liang), submitted July 2023 and revised to v3 on 20 November 2023. Although the URL is a preprint server, the page states acceptance in the Transactions of the Association for Computational Linguistics, and I confirmed the peer-reviewed version published as TACL vol. 12 (2024), pp. 157–173, with a named action editor and reviewers. The authors are verifiable academic and industry NLP researchers (Stanford, UC Berkeley, Samaya AI), and the paper is a substantial primary empirical study with detailed methods, released code, and appendices of full result tables. Its central finding — accuracy drops when relevant information sits in the middle of a long context — is not contradicted anywhere I looked and has been corroborated by independent follow-up research. The main caveats are currency (the models tested are from 2023) and that one specific quantitative result was not independently replicated.

## Author

- **Named authors on the page:** Nelson F. Liu, Kevin Lin, John Hewitt, Ashwin Paranjape, Michele Bevilacqua, Fabio Petroni, Percy Liang.
- **Nelson F. Liu** (first author, corresponding): completed a PhD in computer science at Stanford advised by Percy Liang; his Stanford homepage lists this paper as TACL 2024 and links code, poster and abstract. His Google Scholar profile lists him under Stanford and shows this paper among his listed works.
- **Percy Liang**: Stanford CS faculty and a widely known NLP/ML researcher; co-author of foundational work in the area.
- **John Hewitt**: Google Scholar listing describes him as Assistant Professor at Columbia and visiting researcher at Google DeepMind.
- **Kevin Lin** (UC Berkeley) and **Ashwin Paranjape, Michele Bevilacqua, Fabio Petroni** (Samaya AI) round out the team. Affiliations are printed on the paper itself.
- I confirmed these are the same people by matching field (NLP/computational linguistics), co-authors, and the paper title. A search for "Nelson F. Liu" also surfaced an unrelated physician of the same name on LinkedIn, which I excluded.

**Assessment:** Strong, independently verifiable expertise for this topic.

## Publication

- **Host of this URL:** arXiv.org (cs.CL, Computation and Language). arXiv is a moderated preprint server, not a peer-reviewed journal — a bare arXiv posting carries no editorial guarantee.
- **But this specific paper:** the abstract page's Comments field reads "Accepted for publication in Transactions of the Association for Computational Linguistics (TACL), 2023". I confirmed the published version: TACL vol. 12 (2024), pp. 157–173, published 2024-02-19 (`transacl.org/index.php/tacl/article/view/5757`) and indexed as `aclanthology.org/2024.tacl-1.9`.
- **Editorial process:** peer reviewed. The TACL PDF acknowledges "Luke Zettlemoyer, who served as our TACL action editor, and the anonymous reviewers", and lists "Submission batch: 8/2023; Revision batch: 10/2023; Published 2/2024". Licensed CC-BY 4.0.
- **Reputation:** TACL is a well-regarded ACL journal. I found no retraction, correction, expression of concern, or predatory-journal flag for this paper.
- **arXiv's own funding** (Simons Foundation, Simons Foundation International, Schmidt Sciences) appears in the site footer and is unrelated to the paper's content.

## Claims Checked

| Claim | Status | Evidence |
|---|---|---|
| Model accuracy on multi-document QA is U-shaped: highest when the answer document is first or last, significantly lower in the middle (GPT-3.5-Turbo 75.8% at position 1 vs 53.8% at position 10 of 20 documents). | corroborated | Primary data in the paper (Fig. 1, Fig. 5, Table 6 in appendix G.2 — https://cs.stanford.edu/~nfliu/papers/lost-in-the-middle.arxiv2023.pdf). Independently corroborated by follow-up work, e.g. Hsieh et al., "Found in the Middle" (ACL Findings 2024) on U-shaped attention/position bias, summarized at https://tacnode.io/glossary/lost-in-the-middle and https://davidwsilva.substack.com/p/lost-in-the-middle-the-context-crisis; NVIDIA's RULER (2024) is cited for the same "readable length ≠ usable length" gap at https://teapot123.github.io/files/CSE_5610_Fall25/Lecture_12_Long_Context.pdf |
| Extended-context variants (GPT-3.5-Turbo-16K, Claude-1.3-100K, LongChat-13B-16K) do no better than standard counterparts when the input fits in both windows — a bigger window does not make a model position-robust. | corroborated | Paper's Figures 5 and 8 and Tables 5–6. Direction consistent with independent reporting on RULER and long-context benchmarks at https://teapot123.github.io/files/CSE_5610_Fall25/Lecture_12_Long_Context.pdf ("Extended Context ≠ Robust Use") and https://vanleke.com/blog/2026-08-23-why-long-context-llms-get-lost-in-the-middle.html |
| In open-domain retriever-reader QA, accuracy saturates long before recall: 50 vs 20 retrieved documents gains only ~1.5% (GPT-3.5-Turbo) and ~1% (Claude-1.3). | no_evidence_found | Reported only in the paper's own Section 5. I searched for independent replication of these figures and found none; the general diminishing-returns point is widely discussed in RAG literature, but I did not locate a source reproducing these numbers. Not contradicted — simply unverified. |
| The effect is not an artefact of relevance-ordered documents or of instruction tuning: random distractors, randomised distractor order, and base (non-instruction-tuned) models still show a U-shaped curve; only the smallest Llama-2 7B is recency-biased only. | corroborated | Paper Section 4.3 and appendices B/C (Figures 13–14, 16). Echoed in secondary summaries at https://www.alphaxiv.org/abs/2307.03172 and https://teapot123.github.io/files/CSE_5610_Fall25/Lecture_12_Long_Context.pdf ("Instruction Tuning is Not the Fix") |
| Findings are model-specific and should not be treated as a fixed property of all LLMs. | corroborated | Paper's own hedging and model-specific results; the same caveat is stated explicitly by commentators at https://vanleke.com/blog/2026-08-23-why-long-context-llms-get-lost-in-the-middle.html |

No source I found contradicts the paper's main claims. No fact-check, correction or retraction exists for it.

## Bias and Tone

- **Tone:** neutral, technical, academic. Claims are measured and hedged ("preliminary investigations into the role of…", "we hypothesise that…").
- **Informing vs. persuading:** informing. Nothing is for sale on the page; no product, donation pitch or advocacy campaign is attached to the paper.
- **Limitations acknowledged:** unusually good. The paper includes a section on ambiguity in the NaturalQuestions distractor documents, experiments with random distractors, randomised document ordering, ablations on GPT-4 and Llama-2, and openly reports cases where models or techniques performed perfectly (Claude-1.3 on key-value retrieval; query-aware contextualization nearly solving the key-value task).
- **Possible interest:** three co-authors are affiliated with Samaya AI (which builds retrieval/QA tooling over documents), and the first-page footnote reads "*Work partially completed as an intern at Samaya AI". That is a mild commercial interest in findings about retrieval-augmented generation limits, but it is disclosed, and the paper argues against easy fixes rather than promoting a product.

## Currency

- **Submitted:** 6 July 2023 (v1); **last revised:** 20 November 2023 (v3, the version on this page); **journal publication:** 19 February 2024.
- **As of 2026-11-26** the paper is roughly three years old. The phenomenon it documents is still the standard reference for positional bias, so citing it for the concept is appropriate. However, the models evaluated — GPT-3.5-Turbo-0613, GPT-4 (8K), Claude-1.3 / 100K, Llama-2, MPT-30B-Instruct, LongChat-13B-16K, Flan-T5-XXL, Flan-UL2 — are several generations out of date. Its specific percentages should be described as results for 2023 models, not as a description of current systems.
- Note: the "Published Time: Mon, 24 Aug 2026" string returned when scraping the arXiv page is a page-render artifact, not the publication date.

## Structured Assessment

| Field | Value |
|---|---|
| **Source URL** | https://arxiv.org/abs/2307.03172 |
| **Source type** | peer_reviewed_journal (arXiv-hosted; peer-reviewed TACL 2024 article) |
| **Author name** | Nelson F. Liu, Kevin Lin, John Hewitt, Ashwin Paranjape, Michele Bevilacqua, Fabio Petroni, Percy Liang |
| **Author credentials** | Liu: Stanford CS PhD (advisor Percy Liang), verified via cs.stanford.edu/~nfliu and Google Scholar; Liang: Stanford CS faculty; Hewitt: Columbia asst. prof. / Google DeepMind; Lin: UC Berkeley; Paranjape, Bevilacqua, Petroni: Samaya AI |
| **Author credibility** | Very strong — verifiable affiliations printed on the paper and confirmed independently; established NLP researchers |
| **Publication name** | arXiv (cs.CL); published in Transactions of the Association for Computational Linguistics, vol. 12, 2024 |
| **Publication reputation** | arXiv = moderated preprint server, no peer review by itself; but this article is confirmed published in TACL (pp. 157–173, ACL Anthology 2024.tacl-1.9); no retraction/correction found |
| **Editorial process** | peer_reviewed |
| **Claims checked** | 5 (3 corroborated, 1 no_evidence_found, 0 contradicted; 1 general caveat corroborated) |
| **Claims supported by evidence in the source** | Yes — datasets, prompt formats, per-position accuracy tables, token-count tables, released code |
| **Sources cited** | Yes — extensive academic references; methods and data are documented |
| **Corroborated by other sources** | Yes — Hsieh et al. "Found in the Middle" (ACL Findings 2024), RULER (2024) discussion, wide secondary coverage |
| **Contradicted by other sources** | No |
| **Primary vs. secondary** | primary_source (original experiments) |
| **Funding / sponsorship** | No explicit grant statement found in parts read; disclosed footnote "*Work partially completed as an intern at Samaya AI"; three co-authors at Samaya AI; arXiv's own funders listed in site footer, unrelated to content |
| **Bias and tone** | Neutral, technical, hedged; limitations and counter-checks reported; no commercial or political advocacy; minor disclosed industry affiliation |
| **Date published** | v1 2023-07-06; v3 2023-11-20; TACL publication 2024-02-19 — concept current, model-specific numbers dated (2023 models) |
| **Transparency score** | 4 / 5 (authors, methods and affiliations clear; explicit funding statement not found) |
| **Overall credibility** | **high** |

## Can I cite this?

**Yes — cite it as is**, and cite it as the peer-reviewed journal article rather than as a preprint:

> Liu, N. F., Lin, K., Hewitt, J., Paranjape, A., Bevilacqua, M., Petroni, F., & Liang, P. (2024). Lost in the middle: How language models use long contexts. *Transactions of the Association for Computational Linguistics, 12*, 157–173.

Practical notes for your report:

1. **Cite the TACL version, not the arXiv ID.** Use https://aclanthology.org/2024.tacl-1.9 (or the DOI for the TACL article) if your style guide allows; you can mention the arXiv preprint as the accessible version. Ask your instructor if a preprint URL alone is acceptable — some courses require the version of record.
2. **Attribute the numbers to the models tested.** Write "in 2023-era models such as GPT-3.5-Turbo and Claude-1.3, Liu et al. found…" rather than presenting 75.8% vs 53.8% as a fact about LLMs today.
3. **Use it for what it is good for:** the definition of positional / "lost in the middle" bias, the U-shaped accuracy curve, the point that larger context windows ≠ better context use, and the proposed evaluation protocol (performance should vary little with the position of the evidence).
4. **Do not lean on the Section 5 retrieval-saturation percentages** (~1.5% / ~1% gains from 20→50 documents) as independently established — I found no replication of those specific figures.
5. **Pair it with newer work** for currency: e.g. NVIDIA's RULER benchmark (2024) and Hsieh et al.'s "Found in the Middle" (ACL Findings 2024) show the phenomenon's continuation and remediation. Both are discussed in the background readings I consulted, but verify the originals before citing them.

## Sources Consulted

1. https://arxiv.org/abs/2307.03172 — the source under evaluation: abstract, authors, submission history (v1 2023-07-06, v3 2023-11-20), TACL acceptance note, DOI.
2. https://arxiv.org/html/2307.03172v3 — attempted full-text read; the page served only an embedded SVG figure ("Line chart for accuracy of retrieved documents…"), so it gave no usable text.
3. https://cs.stanford.edu/~nfliu/papers/lost-in-the-middle.arxiv2023.pdf — the paper's full text from the first author's site: abstract, affiliations footnote (Samaya AI internship), Sections 1–4, appendices A–G with per-position accuracy tables, references. Read in four segments.
4. https://cs.stanford.edu/~nfliu — Nelson Liu's homepage: Stanford CS PhD advised by Percy Liang; lists this paper as TACL 2024 with code/poster links.
5. https://scholar.google.com/citations?user=ghGDz7MAAAAJ&hl=en — Google Scholar profile confirming Liu at Stanford and co-author affiliations (Hewitt at Columbia, Petroni at EMBL Rome, Bevilacqua at Google DeepMind).
6. https://transacl.org/index.php/tacl/article/view/5757 — TACL journal record: "Vol. 12 (2024)", "TACL approved", published 2024-02-19, full author list.
7. https://aclanthology.org/2024.tacl-1.9 — ACL Anthology record of the peer-reviewed version.
8. https://aclanthology.org/2024.tacl-1.9.pdf — TACL PDF: page range 157–173, "Action Editor: Luke Zettlemoyer… Published 2/2024", CC-BY 4.0, acknowledgments thanking the action editor and anonymous reviewers.
9. https://huggingface.co/papers/2307.03172 — Hugging Face paper page restating the abstract (secondary, no independent verification).
10. https://www.alphaxiv.org/abs/2307.03172 — secondary summary of the paper's results, including the 75.8% / 53.8% / 56.1% figures.
11. https://teapot123.github.io/files/CSE_5610_Fall25/Lecture_12_Long_Context.pdf — university lecture slides discussing the paper alongside RULER (2024); used only as background on how the finding is taught, not as independent verification.
12. https://tacnode.io/glossary/lost-in-the-middle — glossary entry describing the paper and Hsieh et al.'s "Found in the Middle" (ACL Findings 2024).
13. https://davidwsilva.substack.com/p/lost-in-the-middle-the-context-crisis — Substack post referencing Hsieh et al. (MIT / Google Cloud AI) on U-shaped attention bias.
14. https://vanleke.com/blog/2026-08-23-why-long-context-llms-get-lost-in-the-middle.html — blog post summarizing follow-up literature and explicitly cautioning that "lost in the middle" is not a universal constant for newer models.
