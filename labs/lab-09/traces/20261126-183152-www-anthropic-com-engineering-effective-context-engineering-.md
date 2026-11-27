# Agent trace: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents

- Model: `deepseek/deepseek-v4.1-flash-1017`
- Started: 2026-11-26T18:31:52
- Max turns: 25
- Tools: read_url, web_search, assess_credibility, save_report


**User:** Evaluate the credibility of this source: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents

## Turn 1

_Model call: 2,879 input tokens, 82 output tokens_

**Assistant:**

I'll start by reading the source page.

**Tool call** `read_url` (id `call_2ff9d138374c4755ae2cec75`):

```json
{
  "url": "https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents",
  "start": 0
}
```
**Tool result** `read_url` (id `call_2ff9d138374c4755ae2cec75`, 10,096 characters):

```
Title: Effective context engineering for AI agents

URL Source: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents

Final URL: https://www.anthropic.com/research/effective-context-engineering-for-ai-agents

Published Time: 2025-09-29T00:00:00.000Z

Markdown Content:
After a few years of prompt engineering being the focus of attention in applied AI, a new term has come to prominence: **context engineering**. Building with language models is becoming less about finding the right words and phrases for your prompts, and more about answering the broader question of “what configuration of context is most likely to generate our model’s desired behavior?"

**Context** refers to the set of tokens included when sampling from a large-language model (LLM). The **engineering** problem at hand is optimizing the utility of those tokens against the inherent constraints of LLMs in order to consistently achieve a desired outcome. Effectively wrangling LLMs often requires _thinking in context_— in other words: considering the holistic state available to the LLM at any given time and what potential behaviors that state might yield.

In this post, we’ll explore the emerging art of context engineering and offer a refined mental model for building steerable, effective agents.

At Anthropic, we view context engineering as the natural progression of prompt engineering. Prompt engineering refers to methods for writing and organizing LLM instructions for optimal outcomes (see [our docs](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview) for an overview and useful prompt engineering strategies). **Context engineering** refers to the set of strategies for curating and maintaining the optimal set of tokens (information) during LLM inference, including all the other information that may land there outside of the prompts.

In the early days of engineering with LLMs, prompting was the biggest component of AI engineering work, as the majority of use cases outside of everyday chat interactions required prompts optimized for one-shot classification or text generation tasks. As the term implies, the primary focus of prompt engineering is how to write effective prompts, particularly system prompts. However, as we move towards engineering more capable agents that operate over multiple turns of inference and longer time horizons, we need strategies for managing the entire context state (system instructions, tools, [Model Context Protocol](https://modelcontextprotocol.io/docs/getting-started/intro) (MCP), external data, message history, etc).

An agent running in a loop generates more and more data that _could_ be relevant for the next turn of inference, and this information must be cyclically refined. Context engineering is the [art and science](https://x.com/karpathy/status/1937902205765607626?lang=en) of curating what will go into the limited context window from that constantly evolving universe of possible information.

## Why context engineering is important to building capable agents

Despite their speed and ability to manage larger and larger volumes of data, we’ve observed that LLMs, like humans, lose focus or experience confusion at a certain point. Studies on needle-in-a-haystack style benchmarking have uncovered the concept of [context rot](https://research.trychroma.com/context-rot): as the number of tokens in the context window increases, the model’s ability to accurately recall information from that context decreases.

While some models exhibit more gentle degradation than others, this characteristic emerges across all models. Context, therefore, must be treated as a finite resource with diminishing marginal returns. Like humans, who have [limited working memory capacity](https://journals.sagepub.com/doi/abs/10.1177/0963721409359277), LLMs have an “attention budget” that they draw on when parsing large volumes of context. Every new token introduced depletes this budget by some amount, increasing the need to carefully curate the tokens available to the LLM.

This attention scarcity stems from architectural constraints of LLMs. LLMs are based on the [transformer architecture](https://arxiv.org/abs/1706.03762), which enables every token to [attend to every other token](https://huggingface.co/blog/Esmail-AGumaan/attention-is-all-you-need) across the entire context. This results in n² pairwise relationships for n tokens.

As its context length increases, a model's ability to capture these pairwise relationships gets stretched thin, creating a natural tension between context size and attention focus. Additionally, models develop their attention patterns from training data distributions where shorter sequences are typically more common than longer ones. This means models have less experience with, and fewer specialized parameters for, context-wide dependencies.

Techniques like [position encoding interpolation](https://arxiv.org/pdf/2306.15595) allow models to handle longer sequences by adapting them to the originally trained smaller context, though with some degradation in token position understanding. These factors create a performance gradient rather than a hard cliff: models remain highly capable at longer contexts but may show reduced precision for information retrieval and long-range reasoning compared to their performance on shorter contexts.

These realities mean that thoughtful context engineering is essential for building capable agents.

## The anatomy of effective context

Given that LLMs are constrained by a finite attention budget, _good_ context engineering means finding the _smallest_ _possible_ set of high-signal tokens that maximize the likelihood of some desired outcome. Implementing this practice is much easier said than done, but in the following section, we outline what this guiding principle means in practice across the different components of context.

**System prompts** should be extremely clear and use simple, direct language that presents ideas at the _right altitude_ for the agent. The right altitude is the Goldilocks zone between two common failure modes. At one extreme, we see engineers hardcoding complex, brittle logic in their prompts to elicit exact agentic behavior. This approach creates fragility and increases maintenance complexity over time. At the other extreme, engineers sometimes provide vague, high-level guidance that fails to give the LLM concrete signals for desired outputs or falsely assumes shared context. The optimal altitude strikes a balance: specific enough to guide behavior effectively, yet flexible enough to provide the model with strong heuristics to guide behavior.

We recommend organizing prompts into distinct sections (like `<background_information>`, `<instructions>`, `## Tool guidance`, `## Output description`, etc) and using techniques like XML tagging or Markdown headers to delineate these sections, although the exact formatting of prompts is likely becoming less important as models become more capable.

Regardless of how you decide to structure your system prompt, you should be striving for the minimal set of information that fully outlines your expected behavior. (Note that minimal does not necessarily mean short; you still need to give the agent sufficient information up front to ensure it adheres to the desired behavior.) It’s best to start by testing a minimal prompt with the best model available to see how it performs on your task, and then add clear instructions and examples to improve performance based on failure modes found during initial testing.

**Tools** allow agents to operate with their environment and pull in new, additional context as they work. Because tools define the contract between agents and their information/action space, it’s extremely important that tools promote efficiency, both by returning information that is token efficient and by encouraging efficient agent behaviors.

In [Writing tools for AI agents – with AI agents](https://www.anthropic.com/engineering/writing-tools-for-agents), we discussed building tools that are well understood by LLMs and have minimal overlap in functionality. Similar to the functions of a well-designed codebase, tools should be self-contained, robust to error, and extremely clear with respect to their intended use. Input parameters should similarly be descriptive, unambiguous, and play to the inherent strengths of the model.

One of the most common failure modes we see is bloated tool sets that cover too much functionality or lead to ambiguous decision points about which tool to use. If a human engineer can’t definitively say which tool should be used in a given situation, an AI agent can’t be expected to do better. As we’ll discuss later, curating a minimal viable set of tools for the agent can also lead to more reliable maintenance and pruning of context over long interactions.

Providing examples, otherwise known as few-shot prompting, is a well known best practice that we continue to strongly advise. However, teams will often stuff a laundry list of edge cases into a prompt in an attempt to articulate every possible rule the LLM should follow for a particular task. We do not recommend this. Instead, we recommend working to curate a set of diverse, canonical examples that effectively portray the expected behavior of the agent. For an LLM, examples are the “pictures” worth a thousand words.

Our overall guidance across the different components of context (system prompts**,**tools**,**examples**,**message history, etc) is to be thoughtful and keep your context informative, yet tight. Now let's dive into dynamically retrieving context at runtime.

## Context retrieval and agentic search

In [Building effective AI agents](https://www.anthropic.com/research/building-effective-agents), we highlighted the differences between LLM-based workflows and agents. Since we wrote that post, we’ve gravitated towards a [simple definition](https://simonwillison.net/2025/Sep/18/agents/

[Showing characters 0-10,000 of 21,665. Call read_url with start=10000 to read the next part.]
```

## Turn 2

_Model call: 4,937 input tokens, 79 output tokens_

**Tool call** `read_url` (id `call_2a9fee98c83e4d1e9326c8cb`):

```json
{
  "url": "https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents",
  "start": 10000
}
```
**Tool result** `read_url` (id `call_2a9fee98c83e4d1e9326c8cb`, 10,101 characters):

```
) for agents: LLMs autonomously using tools in a loop.

Working alongside our customers, we’ve seen the field converging on this simple paradigm. As the underlying models become more capable, the level of autonomy of agents can scale: smarter models allow agents to independently navigate nuanced problem spaces and recover from errors.

We’re now seeing a shift in how engineers think about designing context for agents. Today, many AI-native applications employ some form of embedding-based pre-inference time retrieval to surface important context for the agent to reason over. As the field transitions to more agentic approaches, we increasingly see teams augmenting these retrieval systems with “just in time” context strategies.

Rather than pre-processing all relevant data up front, agents built with the “just in time” approach maintain lightweight identifiers (file paths, stored queries, web links, etc.) and use these references to dynamically load data into context at runtime using tools. Anthropic’s agentic coding solution [Claude Code](https://www.anthropic.com/claude-code) uses this approach to perform complex data analysis over large databases. The model can write targeted queries, store results, and leverage Bash commands like head and tail to analyze large volumes of data without ever loading the full data objects into context. This approach mirrors human cognition: we generally don’t memorize entire corpuses of information, but rather introduce external organization and indexing systems like file systems, inboxes, and bookmarks to retrieve relevant information on demand.

Beyond storage efficiency, the metadata of these references provides a mechanism to efficiently refine behavior, whether explicitly provided or intuitive. To an agent operating in a file system, the presence of a file named `test_utils.py` in a `tests` folder implies a different purpose than a file with the same name located in `src/core_logic/` Folder hierarchies, naming conventions, and timestamps all provide important signals that help both humans and agents understand how and when to utilize information.

Letting agents navigate and retrieve data autonomously also enables progressive disclosure—in other words, allows agents to incrementally discover relevant context through exploration. Each interaction yields context that informs the next decision: file sizes suggest complexity; naming conventions hint at purpose; timestamps can be a proxy for relevance. Agents can assemble understanding layer by layer, maintaining only what's necessary in working memory and leveraging note-taking strategies for additional persistence. This self-managed context window keeps the agent focused on relevant subsets rather than drowning in exhaustive but potentially irrelevant information.

Of course, there's a trade-off: runtime exploration is slower than retrieving pre-computed data. Not only that, but opinionated and thoughtful engineering is required to ensure that an LLM has the right tools and heuristics for effectively navigating its information landscape. Without proper guidance, an agent can waste context by misusing tools, chasing dead-ends, or failing to identify key information.

In certain settings, the most effective agents might employ a hybrid strategy, retrieving some data up front for speed, and pursuing further autonomous exploration at its discretion. The decision boundary for the ‘right’ level of autonomy depends on the task. Claude Code is an agent that employs this hybrid model: [CLAUDE.md](http://claude.md/) files are naively dropped into context up front, while primitives like glob and grep allow it to navigate its environment and retrieve files just-in-time, effectively bypassing the issues of stale indexing and complex syntax trees.

The hybrid strategy might be better suited for contexts with less dynamic content, such as legal or finance work. As model capabilities improve, agentic design will trend towards letting intelligent models act intelligently, with progressively less human curation. Given the rapid pace of progress in the field, "do the simplest thing that works" will likely remain our best advice for teams building agents on top of Claude.

### Context engineering for long-horizon tasks

Long-horizon tasks require agents to maintain coherence, context, and goal-directed behavior over sequences of actions where the token count exceeds the LLM’s context window. For tasks that span tens of minutes to multiple hours of continuous work, like large codebase migrations or comprehensive research projects, agents require specialized techniques to work around the context window size limitation.

Waiting for larger context windows might seem like an obvious tactic. But it's likely that for the foreseeable future, context windows of all sizes will be subject to context pollution and information relevance concerns—at least for situations where the strongest agent performance is desired. To enable agents to work effectively across extended time horizons, we've developed a few techniques that address these context pollution constraints directly: compaction, structured note-taking, and multi-agent architectures.

#### Compaction

Compaction is the practice of taking a conversation nearing the context window limit, summarizing its contents, and reinitiating a new context window with the summary. Compaction typically serves as the first lever in context engineering to drive better long-term coherence. At its core, compaction distills the contents of a context window in a high-fidelity manner, enabling the agent to continue with minimal performance degradation.

In Claude Code, for example, we implement this by passing the message history to the model to summarize and compress the most critical details. The model preserves architectural decisions, unresolved bugs, and implementation details while discarding redundant tool outputs or messages. The agent can then continue with this compressed context plus the five most recently accessed files. Users get continuity without worrying about context window limitations.

The art of compaction lies in the selection of what to keep versus what to discard, as overly aggressive compaction can result in the loss of subtle but critical context whose importance only becomes apparent later. For engineers implementing compaction systems, we recommend carefully tuning your prompt on complex agent traces. Start by maximizing recall to ensure your compaction prompt captures every relevant piece of information from the trace, then iterate to improve precision by eliminating superfluous content.

An example of low-hanging superfluous content is clearing tool calls and results – once a tool has been called deep in the message history, why would the agent need to see the raw result again? One of the safest lightest touch forms of compaction is tool result clearing, most recently launched as a [feature on the Claude Developer Platform](https://www.anthropic.com/news/context-management).

#### Structured note-taking

Structured note-taking, or agentic memory, is a technique where the agent regularly writes notes persisted to memory outside of the context window. These notes get pulled back into the context window at later times.

This strategy provides persistent memory with minimal overhead. Like Claude Code creating a to-do list, or your custom agent maintaining a NOTES.md file, this simple pattern allows the agent to track progress across complex tasks, maintaining critical context and dependencies that would otherwise be lost across dozens of tool calls.

[Claude playing Pokémon](https://www.twitch.tv/claudeplayspokemon) demonstrates how memory transforms agent capabilities in non-coding domains. The agent maintains precise tallies across thousands of game steps—tracking objectives like "for the last 1,234 steps I've been training my Pokémon in Route 1, Pikachu has gained 8 levels toward the target of 10." Without any prompting about memory structure, it develops maps of explored regions, remembers which key achievements it has unlocked, and maintains strategic notes of combat strategies that help it learn which attacks work best against different opponents.

After context resets, the agent reads its own notes and continues multi-hour training sequences or dungeon explorations. This coherence across summarization steps enables long-horizon strategies that would be impossible when keeping all the information in the LLM’s context window alone.

As part of our [Sonnet 4.5 launch](https://www.anthropic.com/effective-context-engineering-for-ai-agents), we released [a memory tool](http://anthropic.com/news/context-management) in public beta on the Claude Developer Platform that makes it easier to store and consult information outside the context window through a file-based system. This allows agents to build up knowledge bases over time, maintain project state across sessions, and reference previous work without keeping everything in context.

#### Sub-agent architectures

Sub-agent architectures provide another way around context limitations. Rather than one agent attempting to maintain state across an entire project, specialized sub-agents can handle focused tasks with clean context windows. The main agent coordinates with a high-level plan while subagents perform deep technical work or use tools to find relevant information. Each subagent might explore extensively, using tens of thousands of tokens or more, but returns only a condensed, distilled summary of its work (often 1,000-2,000 tokens).

This approach achieves a clear separation of concerns—the detailed search context remains isolated within sub-agents, while the lead agent focuses on synthesizing and analyzing the results. This pattern, discussed in [How we built our multi-agent research system](https://www.anthropic.com/engineering/multi-agent-research-system), showed a substantial improvement over single-agent systems on complex research tasks.

T

[Showing characters 10,000-20,000 of 21,665. Call read_url with start=20000 to read the next part.]
```

## Turn 3

_Model call: 6,881 input tokens, 75 output tokens_

**Tool call** `read_url` (id `call_dd23ec9e9b654603885f522f`):

```json
{
  "url": "https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents",
  "start": 20000
}
```
**Tool result** `read_url` (id `call_dd23ec9e9b654603885f522f`, 1,724 characters):

```
he choice between these approaches depends on task characteristics. For example:

*   Compaction maintains conversational flow for tasks requiring extensive back-and-forth;
*   Note-taking excels for iterative development with clear milestones;
*   Multi-agent architectures handle complex research and analysis where parallel exploration pays dividends.

Even as models continue to improve, the challenge of maintaining coherence across extended interactions will remain central to building more effective agents.

## Conclusion

Context engineering represents a fundamental shift in how we build with LLMs. As models become more capable, the challenge isn't just crafting the perfect prompt—it's thoughtfully curating what information enters the model's limited attention budget at each step. Whether you're implementing compaction for long-horizon tasks, designing token-efficient tools, or enabling agents to explore their environment just-in-time, the guiding principle remains the same: find the smallest set of high-signal tokens that maximize the likelihood of your desired outcome.

The techniques we've outlined will continue evolving as models improve. We're already seeing that smarter models require less prescriptive engineering, allowing agents to operate with more autonomy. But even as capabilities scale, treating context as a precious, finite resource will remain central to building reliable, effective agents.

Get started with context engineering in the Claude Developer Platform today, and access helpful tips and best practices via our [memory and context management](https://platform.claude.com/cookbook/tool-use-memory-cookbook) cookbook.


[End of page. Showed characters 20,000-21,665 of 21,665.]
```

## Turn 4

_Model call: 7,279 input tokens, 266 output tokens_

**Tool call** `web_search` (id `call_9ff407c1025346dcb3fb3486`):

```json
{
  "query": "\"Effective context engineering for AI agents\" Anthropic author"
}
```
**Tool call** `web_search` (id `call_256daa1f206e445daee91189`):

```json
{
  "query": "Chroma research \"context rot\" study increasing input tokens performance degradation"
}
```
**Tool result** `web_search` (id `call_9ff407c1025346dcb3fb3486`, 7,274 characters):

```
Search results for ""Effective context engineering for AI agents" Anthropic author" (searched 2026-11-26):

[1] Anthropic on Effective Context Engineering for AI Agents | Sunil Thakur posted on the topic | LinkedIn
URL: https://www.linkedin.com/posts/thakursunil_effective-context-engineering-for-ai-agents-activity-7383674531825197057-xjGP
Excerpt: longer contexts can lead to diminished precision and weaker long-range reasoning. Designing Effective Context Effective context engineering involves inserting the right information into the model’s limited attention window. Here are essential components to consider: System Prompts System prompts should be: Clear, specific, and minimal to define desired behavior. Avoiding complex logic that can become brittle and vague instructions that are too... [...] 🚀 Context Engineering: The Next Frontier in AI Agent Design Anthropic’s new piece on Effective Context Engineering for AI Agents draws a clear line between what worked in early prompt engineering—and what’s required to build truly scalable, reliable agentic systems. 👉  ⚙️ Why It Matters Every AI system lives or dies by its context window—the finite memory that defines what an agent “knows” at any moment. Managing that context effectively determines whether your agents stay aligned, coherent, [...] As AI agents evolve beyond simple tasks to handle complex, multi-turn workflows, \\context engineering\\ is critical in how agents are built to operate. While prompt engineering taught us to craft better instructions, context engineering focuses on the bigger question: \What configuration of context is most likely to generate our model’s desired behavior?\ Key insights from Anthropic’s latest research: 🎯 \\Context is finite and precious\\ – More tokens ≠ better performance. “Context rot”

[2] Effective context engineering for AI agents \ Anthropic
URL: https://www.anthropic.com/research/effective-context-engineering-for-ai-agents
Excerpt: Given that LLMs are constrained by a finite attention budget, good context engineering means finding the smallest possible set of high-signal tokens that maximize the likelihood of some desired outcome. Implementing this practice is much easier said than done, but in the following section, we outline what this guiding principle means in practice across the different components of context. [...] #### Compaction

Compaction is the practice of taking a conversation nearing the context window limit, summarizing its contents, and reinitiating a new context window with the summary. Compaction typically serves as the first lever in context engineering to drive better long-term coherence. At its core, compaction distills the contents of a context window in a high-fidelity manner, enabling the agent to continue with minimal performance degradation. [...] An agent running in a loop generates more and more data that could be relevant for the next turn of inference, and this information must be cyclically refined. Context engineering is the art and science of curating what will go into the limited context window from that constantly evolving universe of possible information.

## Why context engineering is important to building capable agents

[3] State of Context Engineering in 2026 | by Kushal Banda | Towards AI
URL: https://pub.towardsai.net/state-of-context-engineering-in-2026-cf92d010eab1
Excerpt: Anthropic frames it well: context engineering means finding the smallest possible set of high-signal tokens that maximise the likelihood of desired outcomes. The discipline covers everything that lands in the context window: system instructions, tool definitions, MCP resources, retrieved documents, conversation history, and accumulated action history. [...] # State of Context Engineering in 2026

Context Engineering has gone from a niche concern to the core discipline of AI Engineering in under a year. In mid-2025, two posts laid much of the groundwork. Manus shared lessons from rebuilding their agent framework four times (July 2025). Anthropic followed with their guide on effective context engineering for agents (September 2025). That was eight months ago. The patterns they described have since matured and were adopted across platforms. [...] Agent Skills are the standard implementation. A skill is a markdown file with YAML frontmatter. The platform reads only the name and description at startup (~80 tokens median per skill). When the model determines a skill is relevant, the full instruction body loads (275 to 8,000 tokens). Supporting scripts and reference materials load only during execution. The format was released by Anthropic in December 2025 and adopted by OpenAI, Google, GitHub, and Cursor within weeks.

[4] Context Engineering for RAG Agents: Enterprise Guide 2026
URL: https://atlan.com/know/context-engineering/context-engineering-for-rag-agents
Excerpt: Anthropic describes context engineering as the work of curating and maintaining the information that enters an agent’s context during inference, including tools, external data, message history, and MCP. Gartner’s July 2025 summary uses the same direction of travel: leaders need context-aware architectures and dynamic data, not prompt tweaks alone.

For RAG builders, the message is simple. Do not throw RAG away. Upgrade what surrounds it.

A context-engineered RAG agent adds: [...] ## Key takeaways

 Context engineering turns RAG from a retrieval pipeline into a governed agent system
 The biggest RAG failures start upstream, in stale definitions, weak lineage, and missing policies
 A context layer gives RAG governed definitions, policies, lineage, relationships, and freshness signals
 Reliable RAG needs context bootstrapping, testing, deployment, and observability before more tuning

## What is context engineering for RAG agents? [...] Is your data estate AI-agent ready?

Assess Your Readiness

## What value does context engineering add to RAG agents?

RAG answers a runtime question: what should this agent fetch right now? Context engineering answers the underlying system question: which knowledge is safe, current, relevant, and sufficiently governed to become agent context?

[5] Writing effective tools for AI agents \ Anthropic
URL: https://www.anthropic.com/research/writing-tools-for-agents
Excerpt: ### Returning meaningful context from your tools

In the same vein, tool implementations should take care to return only high signal information back to agents. They should prioritize contextual relevance over flexibility, and eschew low-level technical identifiers (for example: `uuid`, `256px_image_url`, `mime_type`). Fields like `name`, `image_url`, and `file_type` are much more likely to directly inform agents’ downstream actions and responses. [...] We suggest implementing some combination of pagination, range selection, filtering, and/or truncation with sensible default parameter values for any tool responses that could use up lots of context. For Claude Code, we restrict tool responses to 25,000 tokens by default. We expect the effective context length of agents to grow over time, but the need for context-efficient tools to remain. [...] Optimizing the quality of context is important. But so is optimizing the quantity of context returned back to agents in tool responses.
```
**Tool result** `web_search` (id `call_256daa1f206e445daee91189`, 6,877 characters):

```
Search results for "Chroma research "context rot" study increasing input tokens performance degradation" (searched 2026-11-26):

[1] ChromaDB: Context Rot: Evaluating LLM Performance Degradation with Increasing Input Tokens - ZenML LLMOps Database
URL: https://www.zenml.io/llmops-database/context-rot-evaluating-llm-performance-degradation-with-increasing-input-tokens
Excerpt: ChromaDB's technical report examines how large language models (LLMs) experience performance degradation as input context length increases, challenging the assumption that models process context uniformly. Through evaluation of 18 state-of-the-art models including GPT-4.1, Claude 4, Gemini 2.5, and Qwen3 across controlled experiments, the research reveals that model reliability decreases significantly with longer inputs, even on simple tasks like retrieval and text replication. The study [...] The repeated words experiment revealed fundamental limitations in models’ ability to maintain consistency even on trivial tasks as output length scales with input length. Since these models are autoregressive, each generated token becomes part of the input for subsequent tokens, creating a compounding effect. The experiment showed that models struggled to maintain accuracy in simple text replication tasks as length increased, with different model families exhibiting distinct failure patterns. [...] The study evaluated 18 leading models including GPT-4.1, Claude 4 (Opus and Sonnet variants), Gemini 2.5 Pro and Flash, and Qwen3 models across multiple dimensions. The research methodology was deliberately designed to isolate input length as the primary variable while keeping task complexity constant, addressing a common limitation in existing benchmarks where longer inputs often correlate with increased task difficulty.

[2] Context Rot: How Increasing Input Tokens Impacts LLM Performance | Chroma
URL: https://www.trychroma.com/research/context-rot
Excerpt: Across all experiments, model performance consistently degrades with increasing input length.
 Lower similarity needle-question pairs increases the rate of performance degradation.
 Distractors have non-uniform impact on model performance with regards to how distracting they are relative to each other. We see this impact more prominently as input length increases, and observe distinctions in how various models respond to them. [...] Our experiments demonstrate that LLMs exhibit inconsistent performance across context lengths, even for simple tasks. However, this evaluation is not exhaustive of real-world use cases. In practice, long context applications are often far more complex, requiring synthesis or multi-step reasoning. Based on our findings, we would expect performance degradation to be even more severe under those conditions. [...] We verify that the models are highly capable of succeeding on the focused inputs, then observe consistent performance degradation with the full inputs. This performance drop suggests that adding irrelevant context, and thereby adding an additional step of retrieval, significantly impacts a model’s ability to maintain reliable performance.

## Experiment#

Given a chat history between a user and assistant, the model’s task is to answer a question relating to part of that chat history.

[3] LLM Context Rot
URL: https://cobusgreyling.substack.com/p/llm-context-rot
Excerpt: # Cobus Greyling on AI, Agents, Loop & Harness Engineering...

# LLM Context Rot

### The Chroma “Context Rot” study reveals that simply increasing input length & maximising token windows doesn’t deliver linearly improving accuracy.

Cobus Greyling

#### Instead, LLM performance degrades unevenly & often unpredictably as contexts grow, underscoring the limitations of relying on sheer scale over thoughtful context engineering. [...] Thanks for reading Cobus Greyling on LLMs, NLU, NLP, chatbots & voicebots! Subscribe for free to receive new posts and support my work.

# In Short

Chroma’s recent study evaluated 18 leading large language models (LLMs), including cutting-edge ones like GPT-4.1, Claude 4, Gemini 2.5 & Qwen3.

The research highlights that models don’t process context uniformly, leading to increasingly unreliable performance as input lengths expand — a phenomenon dubbed context rot.

[4] Context Rot: Why LLMs Degrade as Context Grows (+ Fixes)
URL: https://upsolve.ai/blog/context-rot
Excerpt: Context rot is the measurable decline in LLM output quality as input context grows longer, even when the task stays exactly the same, and even when the model is nowhere near its context window limit. Chroma's 2025 technical report tested 18 frontier models and found that every single one degraded as input length increased. [...] ## Frequently Asked Questions

### What is context rot in LLMs?

Context rot is the decline in an LLM's output quality as input context grows longer, even on tasks of constant difficulty. The term comes from Chroma's 2025 research showing all 18 tested frontier models degrade non-uniformly with input length.

### Is context rot the same as "lost in the middle"? [...] Most long-context benchmarks accidentally conflate input length with task difficulty (longer inputs usually mean harder problems). Chroma's methodology held task complexity constant and varied only input length, which lets you attribute the performance drop to length alone.

Four experiments stand out.

### Needle in a Haystack, Made Realistic

[5] Context Rot — Intermediate Paper (Free) | THE D*AI*LY BRIEF
URL: https://www.beri.net/learning/chroma-context-rot-report
Excerpt: ModelsRAGML

# Context Rot: How Increasing Input Tokens Impacts LLM Performance

by Chroma

IntermediatePaperFree~40 min read, plus a reproducible codebase

Eighteen frontier models, and every one degrades as the context grows — even on a task a child could do.

Start LearningAdded Jul 12, 2026 · Updated Aug 22, 2026

## Overview [...] A July 2025 technical report from Chroma testing 18 frontier models on how performance changes purely as input length grows. It extends Needle in a Haystack with semantic matching and distractors, runs LongMemEval focused-versus-full prompts, and adds a trivially simple repeated-words task. The finding that matters for RAG: what is in the context matters less than how much surrounds it.

### Is Context Rot: How Increasing Input Tokens Impacts LLM Performance free? [...] from 25 to 10,000 words. The findings: performance declines with input length across every model tested; lower needle-question similarity degrades faster; distractors compound, with Claude models tending to abstain and GPT models tending to hallucinate; and, counterintuitively, a shuffled incoherent haystack outperformed a logically coherent one on all 18 models. Thinking modes narrowed but did not close the focused-versus-full gap. The report ships with an MIT-licensed repository at
```

## Turn 5

_Model call: 10,443 input tokens, 211 output tokens_

**Tool call** `web_search` (id `call_97e581caba9c4dfab418d24b`):

```json
{
  "query": "Anthropic engineering blog authors \"Applied AI\" team posts byline context engineering September 2025"
}
```
**Tool call** `read_url` (id `call_3fba98c31edf45d2a4eda8b3`):

```json
{
  "url": "https://www.anthropic.com/about",
  "start": 0
}
```
**Tool result** `web_search` (id `call_97e581caba9c4dfab418d24b`, 6,996 characters):

```
Search results for "Anthropic engineering blog authors "Applied AI" team posts byline context engineering September 2025" (searched 2026-11-26):

[1] Context Engineering Explained: The Anthropic Guide That’s Changing How Developers Work with AI | Towards AI
URL: https://towardsai.com/p/machine-learning/context-engineering-explained-the-anthropic-guide-thats-changing-how-developers-work-with-ai
Excerpt: Latest   Machine Learning

# Context Engineering Explained: The Anthropic Guide That’s Changing How Developers Work with AI

R Amogh

 33 likes 

November 29, 2025

Last Updated on December 2, 2025 by Editorial Team

#### Author(s): R Amogh

Originally published on Towards AI.

## In September 2025, Anthropic’s Applied AI team published a blog post that racked up nearly 500,000 views in a week. The title? “Effective Context Engineering for AI Agents.” [...] The article explores the concept of context engineering, which enhances AI interactions and improves the effectiveness of prompt engineering. It discusses the challenges of information overload, the “context rot” problem, and offers practical techniques recommended by Anthropic, such as compaction, structured note-taking, and utilizing multi-agent architectures to better manage and organize context during AI interactions. The article highlights the importance of avoiding contradictions and [...] The post signaled something bigger than a new technique. It marked the moment the industry acknowledged that prompt engineering — the skill everyone spent 2023–2024 mastering — was no longer enough.

The original Anthropic guide is excellent but technical. This is the plain-English version — everything you need to understand context engineering, why it matters, and how to start using it today.

[2] State of Context Engineering in 2026 | by Kushal Banda | Towards AI
URL: https://pub.towardsai.net/state-of-context-engineering-in-2026-cf92d010eab1
Excerpt: # State of Context Engineering in 2026

Context Engineering has gone from a niche concern to the core discipline of AI Engineering in under a year. In mid-2025, two posts laid much of the groundwork. Manus shared lessons from rebuilding their agent framework four times (July 2025). Anthropic followed with their guide on effective context engineering for agents (September 2025). That was eight months ago. The patterns they described have since matured and were adopted across platforms. [...] Anthropic frames it well: context engineering means finding the smallest possible set of high-signal tokens that maximise the likelihood of desired outcomes. The discipline covers everything that lands in the context window: system instructions, tool definitions, MCP resources, retrieved documents, conversation history, and accumulated action history. [...] Agent Skills are the standard implementation. A skill is a markdown file with YAML frontmatter. The platform reads only the name and description at startup (~80 tokens median per skill). When the model determines a skill is relevant, the full instruction body loads (275 to 8,000 tokens). Supporting scripts and reference materials load only during execution. The format was released by Anthropic in December 2025 and adopted by OpenAI, Google, GitHub, and Cursor within weeks.

[3] Anthropic on X: "New on the Anthropic Engineering Blog: Most developers have heard of prompt engineering. But to get …"
URL: https://x.com/AnthropicAI/status/1973098580060631341?lang=en
Excerpt: - Author: @AnthropicAI (Anthropic)
- Posted: 2025-09-30T18:52:14+00:00
- Views: 510726
- Likes: 3112
- Reposts: 479
- Replies: 119
- Quotes: 105
- Bookmarks: 2386
- Links: 
- Card: Effective context engineering for AI agents — www.anthropic.com — In this post, we explore strategies for effectively curating and managing their context.

## People [...] # Anthropic on X: "New on the Anthropic Engineering Blog: Most developers have heard of prompt engineering. But to get …"

New on the Anthropic Engineering Blog: Most developers have heard of prompt engineering. But to get the most out of AI agents, you need context engineering.

We explain how it works:

[4] Effective context engineering for AI agents \ Anthropic
URL: https://www.anthropic.com/research/effective-context-engineering-for-ai-agents
Excerpt: After a few years of prompt engineering being the focus of attention in applied AI, a new term has come to prominence: context engineering. Building with language models is becoming less about finding the right words and phrases for your prompts, and more about answering the broader question of “what configuration of context is most likely to generate our model’s desired behavior?" [...] In this post, we’ll explore the emerging art of context engineering and offer a refined mental model for building steerable, effective agents.

## Context engineering vs. prompt engineering [...] An agent running in a loop generates more and more data that could be relevant for the next turn of inference, and this information must be cyclically refined. Context engineering is the art and science of curating what will go into the limited context window from that constantly evolving universe of possible information.

## Why context engineering is important to building capable agents

[5] Anthropic's Applied AI Engineers: The Forward-Deployed Function Behind Claude's Enterprise Strategy | Blog | Perspective AI
URL: https://getperspective.ai/blog/anthropic-applied-ai-engineers-forward-deployed-claude-enterprise
Excerpt: Anthropic calls its forward-deployed engineering function "Applied AI Engineer" — same job as a Palantir or OpenAI FDE, different label that reflects Anthropic's safety-first, research-led culture. The role sits at the center of Anthropic's enterprise push for Claude, and a reported $1.5 billion joint venture announced in 2025 underwrites the customer-deployment muscle that Applied AI Engineers bring into regulated industries: financial services, healthcare, legal, and government. Day-to-day, [...] Anthropic built the Applied AI Engineer function because frontier models do not sell themselves into regulated enterprises — they require human technical translation. A widely reported $1.5 billion joint venture in 2025, structured around scaled customer deployments, gave the company the runway to staff up customer-embedded engineering aggressively. Reuters covered the Anthropic enterprise revenue trajectory and Bloomberg tracked the regulated-industry buyer wave — both make the case for [...] An Applied AI Engineer and a Forward Deployed Engineer perform the same function — customer-embedded technical work that ships AI into enterprise production — but Anthropic chose the "Applied" label to signal that customer-facing engineering is part of the same research-to-deployment continuum as model research, not a separate sales function. Palantir, OpenAI, and most of the AI vendor market use FDE; Anthropic, Cohere, and others prefer Applied or Solutions titles. Functionally the titles are
```
**Tool result** `read_url` (id `call_3fba98c31edf45d2a4eda8b3`, 462 characters):

```
Title: Not Found

URL Source: https://www.anthropic.com/about

Warning: This page contains shadow DOM that are currently hidden, consider enabling shadow DOM processing.

Markdown Content:
### Our mission

Anthropic is a Public Benefit Corporation. Our mission is the responsible development and maintenance of advanced AI for the long-term benefit of humanity.

### Log in

*   [Claude.ai](https://claude.ai/)
*   [Claude console](https://platform.claude.com/)

```

## Turn 6

_Model call: 12,240 input tokens, 402 output tokens_

**Tool call** `web_search` (id `call_627c324c46124dfaa191299d`):

```json
{
  "query": "Anthropic \"how we built our multi-agent research system\" 90.2% improvement over single agent"
}
```
**Tool call** `web_search` (id `call_608b01fe606c4bc29c087f78`):

```json
{
  "query": "Anthropic company funding Amazon Google investors public benefit corporation Reuters 2025"
}
```
**Tool result** `web_search` (id `call_627c324c46124dfaa191299d`, 7,380 characters):

```
Search results for "Anthropic "how we built our multi-agent research system" 90.2% improvement over single agent" (searched 2026-11-26):

[1] Anthropic: How we built our multi-agent research system
URL: https://simonwillison.net/2025/Jun/14/multi-agent-research-system
Excerpt: > Our internal evaluations show that multi-agent research systems excel especially for breadth-first queries that involve pursuing multiple independent directions simultaneously. We found that a multi-agent system with Claude Opus 4 as the lead agent and Claude Sonnet 4 subagents outperformed single-agent Claude Opus 4 by 90.2% on our internal research eval. For example, when asked to identify all the board members of the companies in the Information Technology S&P 500, the multi-agent system [...] > For speed, we introduced two kinds of parallelization: (1) the lead agent spins up 3-5 subagents in parallel rather than serially; (2) the subagents use 3+ tools in parallel. These changes cut research time by up to 90% for complex queries, allowing Research to do more work in minutes instead of hours while covering more information than other systems. [...] multi-agent system found the correct answers by decomposing this into tasks for subagents, while the single agent system failed to find the answer with slow, sequential searches.

[2] How we built our multi-agent research system \ Anthropic
URL: https://www.anthropic.com/research/multi-agent-research-system
Excerpt: Our internal evaluations show that multi-agent research systems excel especially for breadth-first queries that involve pursuing multiple independent directions simultaneously. We found that a multi-agent system with Claude Opus 4 as the lead agent and Claude Sonnet 4 subagents outperformed single-agent Claude Opus 4 by 90.2% on our internal research eval. For example, when asked to identify all the board members of the companies in the Information Technology S&P 500, the multi-agent system [...] 8. Parallel tool calling transforms speed and performance. Complex research tasks naturally involve exploring many sources. Our early agents executed sequential searches, which was painfully slow. For speed, we introduced two kinds of parallelization: (1) the lead agent spins up 3-5 subagents in parallel rather than serially; (2) the subagents use 3+ tools in parallel. These changes cut research time by up to 90% for complex queries, allowing Research to do more work in minutes instead of hours [...] Multi-agent systems have key differences from single-agent systems, including a rapid growth in coordination complexity. Early agents made errors like spawning 50 subagents for simple queries, scouring the web endlessly for nonexistent sources, and distracting each other with excessive updates. Since each agent is steered by a prompt, prompt engineering was our primary lever for improving these behaviors. Below are some principles we learned for prompting agents:

[3] Anthropic's Multi-Agent Research Architecture Explained
URL: https://theaiengineer.substack.com/p/how-anthropic-built-multi-agent-deep
Excerpt: Anthropic shipped a different answer in April 2025: a Research feature1 that spawns parallel subagents, each with its own context window, each chasing one independent thread. On their internal eval, this setup beat single-agent Claude Opus 4 by 90.2%. The cost: roughly 15x the tokens of a normal chat2.

This issue is about what the architecture is, when the 15x cost is worth paying, and the production decisions that separate 'neat demo' from 'shipped to millions.'

## TL;DR [...] - Performance: 90.2% improvement over single-agent Claude Opus 4 on Anthropic’s internal research eval. 90% reduction in research time on complex queries.
- Cost: ~15x the tokens of a chat interaction. Token usage alone explains 80% of performance variance.
- Lesson: Architecture follows task structure. Multi-agent only wins when the task decomposes into independent parallel threads [...] The result. Up to 90% reduction in research time on complex queries that previously ran serially. Wall-clock per wave drops from the sum of subagent times to the max of subagent times.

My take. Parallel subagents work because each one gets its own context window. Total tokens spent on the query goes up, even though no single context window gets bigger. Anthropic found that token spend alone, more than any other variable, predicts how good the final answer is.

[4] Medium
URL: https://medium.com/@reliabledataengineering/how-anthropic-built-an-ai-that-outperforms-itself-by-90-142d27e7d06a
Excerpt: # How Anthropic Built An AI That Outperforms Itself By 90%

When AI agents collaborate, they become exponentially more capable

## The Breakthrough That Changes Everything

Anthropic just published the engineering deep-dive on Claude’s Research feature, and buried in the details is a finding that rewrites the playbook for AI systems:

A multi-agent system with Claude Opus 4 orchestrating Claude Sonnet 4 subagents outperformed single-agent Claude Opus 4 by 90.2%. [...] Try Claude Research:  
Claude.ai

Explore Open-Source Prompts:  
Anthropic Cookbook — Agent Prompts

Learn About Extended Thinking:  
Extended Thinking Documentation

Understand MCP:  
Model Context Protocol

90.2% better performance isn’t incremental. It’s architectural.

The question isn't whether multi-agent systems matter. The question is: are you building them yet?

Building multi-agent systems? What challenges are you facing? Drop your questions below. 👇 [...] The same principle applies to AI agents.

Individual agents face limits. Even generally-intelligent agents operating alone hit capacity constraints.

Groups of agents accomplish far more. Multi-agent systems scale performance not through better models, but through better organization.

## The 90.2% Performance Gain Explained:

It’s not magic. It’s architecture:

[5] This month in genAI: xAI raises $5B, Microsoft announces multi-agent system, Anthropic partners with Palantir and AWS - CB Insights Research
URL: https://www.cbinsights.com/research/this-month-in-genai-november-2024
Excerpt: ### Apps

 Strategy Terminal

  Powerful AI-driven discovery, research and insight tools
 Browser Analyst

  Personal AI-powered insights on any web page
 Mobile app

  Instant insights, in the moment

### Agents

 Team of agents

  Put our agents to work and turn insights into action

### Features

 ChatCBI™

  Unique insight and data, plus the creativity of generative AI
 10M+ companies

  Data and insight on 10M+ companies
 1,500+ markets [...] CB Insights

# This month in genAI: xAI raises $5B, Microsoft announces multi-agent system, Anthropic partners with Palantir and AWS

We highlight notable generative AI deals, partnerships, and big tech activity in November 2024.

 December 6, 2024
 Already a CB Insights customer? Sign in.

 December 6, 2024
 Already a CB Insights customer? Sign in. [...] Data and insight on 1,500+ markets
 Personal briefing

  Like a team of researchers working 24/7 — just for you
 Predictive data science

  National science-backed data science on private companies
 Personalized research library

  Concise, precise visual research that drives decisions

### Integrations

 API & data feeds

  Double-verified, continually refreshed
 Snowflake

  Market intelligence accessible to AI and agents in real time
 Microsoft 365 Copilot
```
**Tool result** `web_search` (id `call_608b01fe606c4bc29c087f78`, 7,312 characters):

```
Search results for "Anthropic company funding Amazon Google investors public benefit corporation Reuters 2025" (searched 2026-11-26):

[1] Anthropic Valuation: Funding History and Growth Trajectory | Bybit Wiki
URL: https://www.bybit.com/en/wiki/article/anthropic-valuation-61b-funding-growth
Excerpt: Anthropic has raised approximately $14.7 billion in total funding across all rounds as of early 2025, including Amazon's multi-tranche commitment of up to $4 billion, Google's reported investment of $300 million to $500 million in initial tranches with follow-on commitments, and multiple rounds from venture capital and corporate investors. All figures are reported estimates from Bloomberg, TechCrunch, the Wall Street Journal, and Reuters. The complete round-by-round breakdown is in the funding [...] | Company | Most Recent Post-Money Valuation | Total Funding Raised (Approx.) | Key Investors | Primary Product |
 ---  --- 
| OpenAI | ~$157 billion (Oct 2024, Bloomberg/Reuters) | ~$19 billion | Microsoft (~$13B committed), others | ChatGPT / GPT-4o |
| Anthropic | ~$61 billion (early 2025, Bloomberg/WSJ) | ~$14.7 billion | Amazon (up to $4B), Google, General Catalyst | Claude |
| xAI | ~$50 billion (2024, Reuters) | ~$12 billion | Private investors | Grok | [...] | Series D Extension | Spring 2024 | ~$2.75 billion | ~$18 billion | Amazon (second tranche), Google | Additional disbursements; valuation recalibrated by reporting |
| Series E | Early 2025 | ~$3.5 billion | ~$61 billion | General Catalyst, others | Major valuation step-up; ARR growth and Claude 3.5/3.7 traction cited |

[2] Google To Invest $2B In Anthropic As AI Funding Wars Heat Up
URL: https://news.crunchbase.com/ai/google-anthropic-openai-funding-wars
Excerpt: Earlier this month, The Information reported the new round could value the company at between $20 billion and $30 billion.

The news comes just a month after Anthropic — a ChatGPT rival with its AI assistant Claude — inked a deal with Amazon for the e-commerce and cloud titan to invest up to $4 billion in the AI startup. In that deal, the immediate investment was reported as $1.25 billion, with either party having the right to trigger another $2.75 billion in funding, Reuters reported. [...] ## Big money

Of course, both deals still lag behind the massive $10 billion investment from Microsoft into OpenAI back in January.

However, Anthropic has been doing its best to catch up. In February, it was reported that Google had invested between $300 million and $400 million in the startup. In May, the company raised a $450 million Series C led by Spark Capital. In August, Anthropic raised a $100 million round from SK Telecom.

The Amazon deal followed late last month. [...] It will be hard for any startup to catch OpenAI when it comes to funding dollars, but it seems Anthropic is willing to give it a go.

Previous investor Google has agreed to invest up to $2 billion in the OpenAI competitor, per a Wall Street Journal report late Friday. The deal includes $500 million upfront plus an additional $1.5 billion more over time, according to the report. No valuation was reported.

[3] Anthropic - Wikipedia
URL: https://en.wikipedia.org/wiki/Anthropic
Excerpt: In October 2023, Google invested $500 million in Anthropic and committed to an additional $1.5 billion over time. In March 2025, Google agreed to invest another $1 billion in Anthropic. Anthropic raised $3.5 billion in a Series E funding round in March 2025, achieving a post-money valuation of $61.5 billion, led by Lightspeed Venture Partners with participation by several major investors. In September 2025, Anthropic completed a Series F funding round, raising $13 billion at a post-money [...] 126. ↑ Hu, Krystal (October 27, 2023). "Google agrees to invest up to $2 billion in OpenAI rival Anthropic". Reuters. Archived from the original on November 2, 2023. Retrieved October 30, 2023.
127. ↑ Field, Hayden (January 22, 2025). "Google agrees to new $1 billion investment in Anthropic". CNBC. Archived from the original on October 23, 2025. Retrieved September 24, 2025. [...] 124. ↑ "Amazon and Anthropic deepen their shared commitment to advancing generative AI". Amazon. March 27, 2024. Archived from the original on September 17, 2025. Retrieved September 24, 2025.
125. ↑ Bajwa, Arsheeya; Hu, Krystal; Hu, Krystal (November 22, 2024). "Amazon doubles down on AI startup Anthropic with another $4 bln". Reuters. Archived from the original on July 23, 2025. Retrieved September 24, 2025.

[4] Anthropic clinches $380 billion valuation after $30 billion funding round By Reuters
URL: https://www.investing.com/news/economy-news/anthropic-valued-at-380-billion-in-latest-funding-round-4503855
Excerpt: Anthropic, backed by Google and Amazon, had raised $13 billion in a Series F round that valued the company at $183 billion, the company said in early September.

Meanwhile, OpenAI could be valued at about $830 billion as part of talks with SoftBank Group to invest as much as an additional $30 billion in the ChatGPT maker, Reuters reported in January.

REVENUE SURGES [...] "The companies building AI have a responsibility to help ensure the technology serves the public good, not just their own interests," Anthropic had said separately earlier on Thursday.

Earlier this week, Reuters reported that Blackstone, the world’s largest alternative asset manager, was increasing its stake in Anthropic to about $1 billion. [...] Anthropic’s recently launched series of plugins for its Cowork agent had sparked a brutal selloff in global software stocks as investors debated the disruptive potential to the sector from sophisticated AI models.

The funding round, announced on Thursday, was co-led by investors including D. E. Shaw Ventures, ICONIQ and MGX. It also included a portion of previously announced investments from Microsoft and Nvidia.

[5] Anthropic IPO: Valuation, Timeline and Investment Options
URL: https://smartasset.com/investing/anthropic-ipo
Excerpt: | Menlo-Led Financing Discussion | Late 2023 / Early 2024 | $18.4 billion pre-money | Reuters reported that Anthropic was discussing a $750 million financing led by Menlo Ventures. This was not Anthropic’s formal Series E or Series F round. 5 |
| Amazon Expansion | November 2024 | Not publicly disclosed | Amazon invested an additional $4 billion, bringing its total investment in Anthropic to $8 billion, while remaining a minority investor. 6 | [...] Amazon: Amazon is Anthropic’s largest strategic capital provider and Anthropic’s primary cloud provider and training partner. Amazon invested $8 billion by November 2024 and later agreed to invest $5 billion immediately, with up to another $20 billion possible. 15  However, Amazon did not disclose its exact equity percentage, so it is better to avoid ranking Amazon as Anthropic’s second-largest shareholder unless a source explicitly supports that claim. [...] Anthropic is structured as a public benefit corporation. This legal designation allows a company to pursue goals beyond shareholder profit, but does not prevent Anthropic from going public. However, it could shape how public-market investors evaluate the company’s governance, mission and long-term trade-offs between growth, safety and profitability.

## Anthropic’s Valuation and Funding History
```

## Turn 7

_Model call: 15,975 input tokens, 538 output tokens_

**Tool call** `web_search` (id `call_d2f8aefdfe6149519b53b611`):

```json
{
  "query": "\"context engineering\" critique hype criticism \"context rot\" exaggeration long context still useful"
}
```
**Tool call** `read_url` (id `call_1b124f87a3fb4ad1b506cacb`):

```json
{
  "url": "https://www.anthropic.com/engineering",
  "start": 0
}
```
**Tool result** `read_url` (id `call_1b124f87a3fb4ad1b506cacb`, 10,096 characters):

```
Title: Engineering

URL Source: https://www.anthropic.com/engineering

Markdown Content:
[Skip to main content](https://www.anthropic.com/engineering#main-content)

[News](https://www.anthropic.com/news)Research Policy Commitments

[](https://www.anthropic.com/)

Company

Try Claude

[](https://www.anthropic.com/search)

# The Engineering team builds the infrastructure that makes Claude reliable and trustworthy. We translate our research into production systems, and share what we learn about building, evaluating, and deploying AI agents at scale.

*   [![Image 1: Illustration of two offset half circles with a grid pattern, one green and one pink, facing each other across a gap on a light blue background.](https://assets.claude.com/8d3836735b8659a7c39c9c9b5b795d579195bde1.jpg?w=3840&q=75&fm=webp&fit=max)](https://www.anthropic.com/research/components-of-agent-memory)
*   [![Image 2: Redesigning source control at Anthropic](https://assets.claude.com/cfb6c0671a1e04252d55fc3c6776daad399e8356.jpg?w=3840&q=75&fm=webp&fit=max)](https://www.anthropic.com/research/redesigning-source-control)
*   [![Image 3: Harness design for long-running application development](https://assets.claude.com/06e96ccf5aecdd14d34f8c7c14d24c48147c20f4.jpg?w=3840&q=75&fm=webp&fit=max)](https://www.anthropic.com/research/harness-design-long-running-apps)
*   [![Image 4: Designing AI-resistant technical evaluations](https://assets.claude.com/d89131632520ea85953121daa687b257a261208b.jpg?w=3840&q=75&fm=webp&fit=max)](https://www.anthropic.com/research/AI-resistant-technical-evaluations)

[Engineering](https://www.anthropic.com/engineering)

Nov 6, 2026## [The components of agent memory](https://www.anthropic.com/research/components-of-agent-memory)
For Claude to learn from experience, it has to decide what’s worth remembering before it knows what’s next. Here’s how “dreaming” helps it organize memory and correct mistakes.

[Engineering](https://www.anthropic.com/engineering)

Oct 13, 2026## [Redesigning source control at Anthropic](https://www.anthropic.com/research/redesigning-source-control)
As our merges per day grew more than tenfold, source control became our biggest development bottleneck. Here, we share how we migrated to an in-house version control system in five months.

[Read more](https://www.anthropic.com/research/redesigning-source-control)

[Engineering](https://www.anthropic.com/engineering)

Mar 24, 2026## [Harness design for long-running application development](https://www.anthropic.com/research/harness-design-long-running-apps)
Harness design is key to performance at the frontier of agentic coding. Here's how we pushed Claude further in frontend design and long-running autonomous software engineering.

[Read more](https://www.anthropic.com/research/harness-design-long-running-apps)

[Engineering](https://www.anthropic.com/engineering)

Jan 21, 2026## [Designing AI-resistant technical evaluations](https://www.anthropic.com/research/AI-resistant-technical-evaluations)
What we learned from three iterations of a performance engineering take-home that Claude keeps beating.

[Read more](https://www.anthropic.com/research/AI-resistant-technical-evaluations)

01

/

04

30

ARTICLES

Most recent Grid view

Nov 25, 2026![Image 5](https://assets.claude.com/3005501db46139ddf6cbf5954744cb4c18cef482.jpg?w=1080&q=75&fm=webp&fit=max)

### [Migrating our Messages API to Rust](https://www.anthropic.com/research/migrating-api-to-rust)

Nov 13, 2026![Image 6: Illustration of a tilted red gridded square and an upright blue gridded square overlapping imperfectly to form a dark green square, on a light green background.](https://assets.claude.com/abd5df81fa75d3f4a2b489a120e93f7af2f7456f.jpg?w=1080&q=75&fm=webp&fit=max)

### [Building strong safety evaluations](https://www.anthropic.com/research/building-strong-safety-evaluations)

Nov 6, 2026![Image 7: Illustration of two offset half circles with a grid pattern, one green and one pink, facing each other across a gap on a light blue background.](https://assets.claude.com/8d3836735b8659a7c39c9c9b5b795d579195bde1.jpg?w=1080&q=75&fm=webp&fit=max)

### [The components of agent memory](https://www.anthropic.com/research/components-of-agent-memory)

Oct 13, 2026![Image 8](https://assets.claude.com/17cafd9f2d8061a4771416ea5ebc6dde3e71e398.jpg?w=1080&q=75&fm=webp&fit=max)

### [Redesigning source control at Anthropic](https://www.anthropic.com/research/redesigning-source-control)

May 25, 2026![Image 9](https://assets.claude.com/0949ccd8b43ad8728f89c71ad006d01a6d2f2eb7.jpg?w=1080&q=75&fm=webp&fit=max)

### [How we contain Claude across products](https://www.anthropic.com/research/how-we-contain-claude)

Apr 23, 2026![Image 10](https://assets.claude.com/59e4dad5ac806215ac1faac3331f86160674864f.jpg?w=1080&q=75&fm=webp&fit=max)

### [An update on recent Claude Code quality reports](https://www.anthropic.com/research/april-23-postmortem)

Apr 8, 2026![Image 11](https://assets.claude.com/bc042c54afc1c90f628bb3a7e65df06e108fa7db.jpg?w=1080&q=75&fm=webp&fit=max)

### [Scaling Managed Agents: Decoupling the brain from the hands](https://www.anthropic.com/research/managed-agents)

Mar 25, 2026![Image 12](https://assets.claude.com/9df3374050aca30df3c9807c1a2aa06a3268cedc.jpg?w=1080&q=75&fm=webp&fit=max)

### [How we built Claude Code auto mode: a safer way to skip permissions](https://www.anthropic.com/research/claude-code-auto-mode)

Mar 24, 2026![Image 13](https://assets.claude.com/73495421fe8ab222bf855648fcff78749ac27cc7.jpg?w=1080&q=75&fm=webp&fit=max)

### [Harness design for long-running application development](https://www.anthropic.com/research/harness-design-long-running-apps)

Mar 6, 2026![Image 14](https://assets.claude.com/8a8a0c19bc294c64ab0b4e985e5df7c3cd85ce5b.jpg?w=1080&q=75&fm=webp&fit=max)

### [Eval awareness in Claude Opus 4.6’s BrowseComp performance](https://www.anthropic.com/research/eval-awareness-browsecomp)

Feb 5, 2026![Image 15](https://assets.claude.com/57b3f52a50fad2bece75f47e7f1c4f8f963a0f49.jpg?w=1080&q=75&fm=webp&fit=max)

### [Building a C compiler with a team of parallel Claudes](https://www.anthropic.com/research/building-c-compiler)

Feb 5, 2026![Image 16](https://assets.claude.com/40a2d4c805fba4cf460cecfbf6c2d8560c639ccd.jpg?w=1080&q=75&fm=webp&fit=max)

### [Quantifying infrastructure noise in agentic coding evals](https://www.anthropic.com/research/infrastructure-noise)

Jan 21, 2026![Image 17](https://assets.claude.com/9761056407a6aedc229983a2667a83ce5e6c2344.jpg?w=1080&q=75&fm=webp&fit=max)

### [Designing AI-resistant technical evaluations](https://www.anthropic.com/research/AI-resistant-technical-evaluations)

Jan 9, 2026![Image 18](https://assets.claude.com/dda2a21f9030a761c6057c106f195ae377014bdb.jpg?w=1080&q=75&fm=webp&fit=max)

### [Demystifying evals for AI agents](https://www.anthropic.com/research/demystifying-evals-for-ai-agents)

Nov 26, 2025![Image 19](https://assets.claude.com/b2a3cd3b5897a178c985d7886d43cf53d39b0813.jpg?w=1080&q=75&fm=webp&fit=max)

### [Effective harnesses for long-running agents](https://www.anthropic.com/research/effective-harnesses-for-long-running-agents)

Nov 24, 2025![Image 20](https://assets.claude.com/e95d3a9f390e2d93238de38fe118b00d2606e417.jpg?w=1080&q=75&fm=webp&fit=max)

### [Introducing advanced tool use on the Claude Developer Platform](https://www.anthropic.com/research/advanced-tool-use)

Nov 4, 2025![Image 21](https://assets.claude.com/05de8f969ae169db0885c1fb9481d8393537d4cf.jpg?w=1080&q=75&fm=webp&fit=max)

### [Code execution with MCP: Building more efficient agents](https://www.anthropic.com/research/code-execution-with-mcp)

Oct 20, 2025![Image 22](https://assets.claude.com/e7a92fbfadc1e610460ef4985929ca0b44853243.jpg?w=1080&q=75&fm=webp&fit=max)

### [Beyond permission prompts: making Claude Code more secure and autonomous](https://www.anthropic.com/research/claude-code-sandboxing)

Oct 16, 2025![Image 23](https://assets.claude.com/a9fa52bd85fa83a411ed54d78d9c1e9420387626.jpg?w=1080&q=75&fm=webp&fit=max)

### [Equipping agents for the real world with Agent Skills](https://www.anthropic.com/research/equipping-agents-for-the-real-world-with-agent-skills)

Sep 29, 2025![Image 24](https://assets.claude.com/ce8e124a876012db3eb360ff1cfc2046528396be.jpg?w=1080&q=75&fm=webp&fit=max)

### [Effective context engineering for AI agents](https://www.anthropic.com/research/effective-context-engineering-for-ai-agents)

Sep 17, 2025![Image 25](https://assets.claude.com/f306bba15f86c2ced382060b23274e0756db8f5d.jpg?w=1080&q=75&fm=webp&fit=max)

### [A postmortem of three recent issues](https://www.anthropic.com/research/a-postmortem-of-three-recent-issues)

Sep 11, 2025![Image 26](https://assets.claude.com/487c971eb7245643e58d7b8f92b550d2f6b534e1.png?w=1920&q=75&fm=webp&fit=max)

### [Writing effective tools for agents — with agents](https://www.anthropic.com/research/writing-tools-for-agents)

Jun 26, 2025![Image 27](https://assets.claude.com/4a3ca3038520d9aae9e3ca2e826aacae1c1dae18.png?w=1920&q=75&fm=webp&fit=max)

### [Desktop Extensions: One-click MCP server installation for Claude Desktop](https://www.anthropic.com/research/desktop-extensions)

Jun 18, 2025![Image 28](https://assets.claude.com/71fcd5480d9df8597e4ef51431dae586a74c60ac.jpg?w=1080&q=75&fm=webp&fit=max)

### [Confidential Inference via Trusted Virtual Machines](https://www.anthropic.com/research/confidential-inference-trusted-vms)

See more

## Explore work from other teams

### [Alignment](https://www.anthropic.com/research/team/alignment)
50 posts

Works to understand the risks of AI models and develops ways to ensure future ones remain helpful, honest, and harmless.

### [Economics](https://www.anthropic.com/research/team/economics)
28 posts

Studies and monitors the impact of AI systems on individuals, firms, and economies.

### [Frontier Red Team](https://www.anthropic.com/research/team/frontier-red-team)
38 posts

Stress-tests AI systems to understand the full exten

[Showing characters 0-10,000 of 12,542. Call read_url with start=10000 to read the next part.]
```
**Tool result** `web_search` (id `call_d2f8aefdfe6149519b53b611`, 7,204 characters):

```
Search results for ""context engineering" critique hype criticism "context rot" exaggeration long context still useful" (searched 2026-11-26):

[1] Context Rot In LLMs: Why Long Context Fails & How To Fix It
URL: https://vertexfrontier.com/context-rot-long-context-llm-performance
Excerpt: Anthropic’s engineering guidance on context engineering makes a similar operational point: context should be treated as a finite resource with diminishing returns. Its “attention budget” language is a useful engineering model, not a standardized scalar that can be read from an API.

## Why the Context Window Number Misleads [...] Measure your own effective window. The useful number is the longest input at which your model still meets your quality floor on your real tasks.

  Context Engineering Approach 

The practical fix is context engineering. Select, compress, externalize, isolate, and verify context instead of filling the window by default.

## What Is Context Rot? [...] Prompt engineering asks how to phrase instructions. Context engineering asks what the model should see now: instructions, tool descriptions, retrieved evidence, memory, user history, state, and observations.

Context engineering practical fix

Context engineering practical fix

Anthropic describes context engineering as curating the smallest useful set of tokens for the desired behavior. A practical taxonomy is:

### Write

[2] Context Engineering: What It Is and 4 Ways It Fails | Glasp
URL: https://glasp.co/articles/context-engineering
Excerpt: Bigger context windows made this worse: Liu et al. (2024) showed information in the middle of long contexts gets ignored. Chroma's 2025 "Context Rot" study found all 18 frontier models degrade well before the window fills. Databricks put the onset near 32,000 tokens.
 Context pollution has four named forms: Drew Breunig's taxonomy (poisoning, distraction, confusion, clash) is the practical diagnostic. Each one has a different fix, and adding more context makes three of them worse. [...] The phrase is retiring. The techniques under the phrase still work. Chain-of-thought, few-shot examples, and clear output formats are all still useful. What's dead is the idea that good phrasing alone gets you great output. In 2026, phrasing is a minor lever. Context assembly is the major one. When people say "prompt engineering is dead," this is what they mean.

### Is context engineering dead or just a buzzword? [...] The honest read as of mid-2026: the phrase is past its hype peak, and the standalone "context engineer" title is emergent rather than standard. Adobe posts roles carrying that exact name, but at most companies the work sits inside existing AI, data, or platform engineering jobs. The practice underneath it is more established than ever. Expect the label to fade into the background the way "responsive design" did, absorbed into the default definition of competent work.

[3] Context Rot: When Long Context Fails
URL: https://www.youtube.com/watch?v=3s_N60u0jEY
Excerpt: Kelly Hong from Chroma presents the "Context Rot" technical report, demonstrating that Large Language Models' performance is not uniform across input lengths. She reveals through several experiments that performance degrades significantly as input tokens increase, especially when tasks involve semantic ambiguity or distracting information, highlighting the critical need for thoughtful context engineering over simply expanding context windows.

See annotated post version of this video: [...] in your context, if you have distractors. So you need to think about like how you engineer the context before you give it into your model. And I think context engineering it's is highly dependent on use case. So there's no like general like context engineering solution but I'll just walk through one example that I've seen being used in practice just to give a sense but it's really dependent on your applications. Yeah, definitely think about specifically. But for this use case, say you have a [...] like using elements they talk about like context engineering you want to give it like the most relevant information the ways in which you do that is not only about retrieval there is so many different methods like the sub Asian approach I talked about. So I think like people are coming to the consensus that like context engineering is important. So I think maybe like the terms are changing a bit to shift away from like solely vector retrieval. What would be your advice to people who have AI

[4] Context rot: the emerging challenge that could hold back LLM progress
URL: https://www.understandingai.org/p/context-rot-the-emerging-challenge
Excerpt: And indeed, technologists have noticed that LLM performance on real-world tasks tends to decline as contexts get longer.

In June, a Hacker News commenter coined the phrase “context rot” to describe the phenomenon where LLMs become less effective as the size of their context grows. The startup Chroma published a widely read study on the phenomenon in July.

No one fully understands how LLMs work, so it’s hard to say exactly why context rot happens. But here’s how I think about it. [...] The blog post went on to discuss context engineering, a suite of emerging techniques for helping LLMs stay focused by removing extraneous tokens from their context windows.

Those techniques are fine as far as they go. But I suspect they can only mitigate the underlying problem. If we want LLMs to reason effectively over much longer contexts, we may have to fundamentally rethink how LLMs work.

## Structure matters

[5] Context Engineering Is Knowing When to Start Over
URL: https://every.to/also-true-for-humans/why-i-start-a-new-thread-in-claude-every-time
Excerpt: Turning memory off doesn’t entirely solve the problem. Even within a single thread, context can accumulate in ways that make the model’s responses worse—a problem known as context rot. It might keep following instructions you’ve moved on from, build on an earlier mistake, or overlook a crucial detail buried in the conversation.

That’s why I start a fresh thread for every task. If the task changes, I open a new chat—even if it’s for the same project I was working on five minutes ago. [...] you need to give it the context it needs. In this case, I used voice mode to explain what I’d learned from running an agency. Those details helped the model write a more useful post that reflected my experience. If you’re leaving a long thread that has valuable context but is starting to degrade from context rot, ask the model to save a handoff file—a document summarizing the key facts, decisions, and next steps. Upload it to a fresh thread so the model has what it needs to keep going. [...] In my forthcoming book, Context Engineering with DSPy, I explore the seven ways in which context goes wrong and what to do about it. The book is written for engineers building AI products, but I’ve adapted the examples that follow—inspired by Drew Breunig’s “How Long Contexts Fail”—for anyone who uses AI chat. They’ll help you recognize when a conversation has gone off track and restart without losing useful work.

## 1. Context distraction: Old patterns constrain new answers
```

## Turn 8

_Model call: 21,297 input tokens, 966 output tokens_

**Tool call** `read_url` (id `call_c61a63141ca046abbcb42861`):

```json
{
  "url": "https://www.anthropic.com/news/context-management",
  "start": 0
}
```
**Tool call** `web_search` (id `call_8ad61d7ea4ce47328ff904ff`):

```json
{
  "query": "Cognition \"Don't Build Multi-Agents\" context engineering single agent argue against subagents"
}
```
**Tool result** `read_url` (id `call_c61a63141ca046abbcb42861`, 4,980 characters):

```
Title: Managing context on the Claude Developer Platform

URL Source: https://www.anthropic.com/news/context-management

Final URL: https://claude.com/resources/articles/context-management

Published Time: 2025-09-29

Markdown Content:
Today, we’re introducing new capabilities for managing your agents’ context on the Claude Developer Platform: context editing and the memory tool.

With our latest model, [Claude Sonnet 4.5](https://www.anthropic.com/news/claude-sonnet-4-5), these capabilities enable developers to build AI agents capable of handling long-running tasks at higher performance and without hitting context limits or losing critical information.

## Context windows have limits, but real work doesn’t

As production agents handle more complex tasks and generate more tool results, they often exhaust their effective context windows—leaving developers stuck choosing between cutting agent transcripts or degrading performance. Context management solves this in two ways, helping developers ensure only relevant data stays in context and valuable insights get preserved across sessions.

**Context editing** automatically clears stale tool calls and results from within the context window when approaching token limits. As your agent executes tasks and accumulates tool results, context editing removes stale content while preserving the conversation flow, effectively extending how long agents can run without manual intervention. This also increases the effective model performance as Claude focuses only on relevant context.

![Image 1](https://assets.claude.com/614d9e48dd7fdba4d52f7ab3f12129793f337d01.png)
**The memory tool** enables Claude to store and consult information outside the context window through a file-based system. Claude can create, read, update, and delete files in a dedicated memory directory stored in your infrastructure that persists across conversations. This allows agents to build up knowledge bases over time, maintain project state across sessions, and reference previous learnings without having to keep everything in context.

[Video 3](https://www.youtube.com/watch?v=BER3EhUIyz0)

The memory tool operates entirely client-side through tool calls. Developers manage the storage backend, giving them complete control over where the data is stored and how it’s persisted.

Claude Sonnet 4.5 enhances both capabilities with built-in context awareness—tracking available tokens throughout conversations to manage context more effectively.

Together, these updates create a system that improves agent performance:

*   Enable longer conversations by automatically removing stale tool results from context
*   Boost accuracy by saving critical information to memory—and bring that learning across successive agentic sessions

## Building long-running agents

Claude Sonnet 4.5 is the best model in the world for building agents. These features unlock new possibilities for long-running agents—processing entire codebases, analyzing hundreds of documents, or maintaining extensive tool interaction histories. Context management builds on this foundation, ensuring agents can leverage this expanded capacity efficiently while still handling workflows that extend beyond any fixed limit. Use cases include:

*   **Coding:** Context editing clears old file reads and test results while memory preserves debugging insights and architectural decisions, enabling agents to work on large codebases without losing progress.
*   **Research:**Memory stores key findings while context editing removes old search results, building knowledge bases that improve performance over time.
*   **Data processing:**Agents store intermediate results in memory while context editing clears raw data, handling workflows that would otherwise exceed token limits.

## Performance improvements with context management

On an internal evaluation set for agentic search, we tested how context management improves agent performance on complex, multi-step tasks. The results demonstrate significant gains: combining the memory tool with context editing improved performance by 39% over baseline. Context editing alone delivered a 29% improvement.

In a 100-turn web search evaluation, context editing enabled agents to complete workflows that would otherwise fail due to context exhaustion—while reducing token consumption by 84%.

## Getting started

These capabilities are available today in public beta on the Claude Developer Platform, natively and in Amazon Bedrock and Google Cloud’s Vertex AI. Explore the documentation for [context editing](https://docs.claude.com/en/docs/build-with-claude/context-editing) and the [memory tool](https://docs.claude.com/en/docs/agents-and-tools/tool-use/memory-tool), or visit our [cookbook](https://platform.claude.com/cookbook/tool-use-memory-cookbook) to learn more.

_Anthropic is not affiliated with, endorsed by, or sponsored by CATAN GmbH or CATAN Studio. The CATAN trademark and game are the property of CATAN GmbH._

```
**Tool result** `web_search` (id `call_8ad61d7ea4ce47328ff904ff`, 7,263 characters):

```
Search results for "Cognition "Don't Build Multi-Agents" context engineering single agent argue against subagents" (searched 2026-11-26):

[1] Why Cognition does not use multi-agent systems - Jason Liu
URL: https://jxnl.co/writing/2025/09/11/why-cognition-does-not-use-multi-agent-systems
Excerpt: I hosted a session with Walden Yan, co-founder and CPO of Cognition, to explore why multi-agent systems might not be the optimal approach for coding contexts. We discussed the theory of context engineering, the challenges of context passing between agents, and how single agents with proper context management can often outperform multi-agent setups.

▶️ Learn Why Devin Chose Single Agents

## Why are multi-agent systems problematic for coding tasks?¶ [...] > "If you're abiding by like kind of principles of good context, engineering your system as a whole, even if it has like subparts and tasks. It kind of should feel to the user like a single agent, because the user has to feel like they're they're talking with one continuous decision maker, one continuous like consciousness." [...] To minimize the "telephone game" problem, we need to ensure sub-agents have at least the same context as the main agent. This means:

 Sub-agents should see everything the main agent saw
 Sub-agents should have access to the full history of actions taken by the main agent
 The final agent should see everything from all previous agents

[2] Organizing Single-Agent vs Multi-Agent
URL: https://zenn.dev/r_kaga/articles/ea7119d22d4d3c?locale=en
Excerpt: ## Cognition's Argument

Cognition's key point is the importance of context engineering for building reliable agents.  
 They describe the current state of agent development as "still in the stage of playing with vanilla HTML and CSS" and advocate for principles to build robust agent systems.

They believe that multi-agent architectures tend to violate two principles they propose (complete sharing of context, synchronization of implicit decisions), posing a high risk of compounding errors. [...] When thinking about this, I recalled an article published by Cognition AI (the developer of Devin) on June 12, 2025.  
 In an article titled "Don't Build Multi-Agents," they discuss how the lack of context sharing between sub-agents can undermine system reliability.

This is a slightly older article, but All Hands published an article titled "Don't Sleep on Single-Agent Systems."

[3] Don’t Build Multi-Agents | Cognition
URL: https://cognition.com/blog/dont-build-multi-agents
Excerpt: do anything beyond answering a well-defined question. And if they were to run multiple parallel subagents, they might give conflicting responses, resulting in the reliability issues we saw with our earlier examples of agents. The benefit of having a subagent in this case is that all the subagent’s investigative work does not need to remain in the history of the main agent, allowing for longer traces before running out of context. The designers of Claude Code took a purposefully simple approach. [...] This may seem contrived, but most real-world tasks have many layers of nuance that all have the potential to be miscommunicated. You might think that a simple solution would be to just copy over the original task as context to the subagents as well. That way, they don’t misunderstand their subtask. But remember that in a real production system, the conversation is most likely multi-turn, the agent probably had to make some tool calls to decide how to break down the task, and any number of [...] This is what us humans do when we disagree (in an ideal world). If Engineer A’s code causes a merge conflict with Engineer B, the correct protocol is to talk out the differences and reach a consensus. However, agents today are not quite able to engage in this style of long-context proactive discourse with much more reliability than you would get with a single agent. Humans are quite efficient at communicating our most important knowledge to one another, but this efficiency takes nontrivial

[4] Don’t Build Multi-Agents | Cognition
URL: https://cognition.ai/blog/dont-build-multi-agents
Excerpt: do anything beyond answering a well-defined question. And if they were to run multiple parallel subagents, they might give conflicting responses, resulting in the reliability issues we saw with our earlier examples of agents. The benefit of having a subagent in this case is that all the subagent’s investigative work does not need to remain in the history of the main agent, allowing for longer traces before running out of context. The designers of Claude Code took a purposefully simple approach. [...] This may seem contrived, but most real-world tasks have many layers of nuance that all have the potential to be miscommunicated. You might think that a simple solution would be to just copy over the original task as context to the subagents as well. That way, they don’t misunderstand their subtask. But remember that in a real production system, the conversation is most likely multi-turn, the agent probably had to make some tool calls to decide how to break down the task, and any number of [...] This is what us humans do when we disagree (in an ideal world). If Engineer A’s code causes a merge conflict with Engineer B, the correct protocol is to talk out the differences and reach a consensus. However, agents today are not quite able to engage in this style of long-context proactive discourse with much more reliability than you would get with a single agent. Humans are quite efficient at communicating our most important knowledge to one another, but this efficiency takes nontrivial

[5] Context Engineering for Building Better Agents
URL: https://www.youtube.com/watch?v=Oj35c8MkPLE&vl=en
Excerpt: do not build multi- aents is from cognition labs who are the creator of devon. I'll highly recommend to read both of these articles but in this video I want to give you a very quick summary of what these articles say about building agentic systems. Okay. So today if you're building a aentic system for a complex task the proposed approach is that you divide it into subtasks where each of the subtask is carried out by a separate small sub agent and then you somehow combine them. So you have an [...] the lead agent and cloud solid 4 sub aents outperformed single agent cloud opus 4 by 90% on their internal research evolves which is kind of crazy. So you can almost get double the performance using this multi- aent system compared to a single monolithic agents that cognition was proposing. Now they make the case of why multi-agent systems can potentially work specifically for search applications and one of the idea is that since you're using multiple different agents each of the sub aent can [...] So you have an orchestrator and then an aggregator and in between you have multiple agents working together. But this article from cognition lab says that it might not be the most optimal approach. So in general here is what a usual approach looks like. You have the orchestrator which receives a task from the user. Then it's going to break it down into sub aents. It will assign a task to each of the sub aents. Sub aents perform those tasks and then the aggregator will combine the results. Now
```

## Turn 9

_Model call: 24,767 input tokens, 3,125 output tokens_

**Tool call** `assess_credibility` (id `call_563b67fb821344e8b69cae15`):

```json
{
  "evaluation": {
    "source_url": "https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents",
    "source_type": "corporate_blog",
    "author": {
      "name": "Unknown (no individual byline)",
      "credentials": "No named author on the page or in its metadata. The post is published under Anthropic's Engineering blog; a third-party summary (Towards AI) attributes it to Anthropic's 'Applied AI team', but the page itself names no people, roles or bios.",
      "credibility_assessment": "Institutional credibility only. Anthropic is a leading frontier AI lab, so the post reflects real practitioner expertise, but an uncritiqued, unnamed corporate author is harder to hold accountable than a signed, biographied piece."
    },
    "publication": {
      "name": "Anthropic (Engineering blog; URL redirects to anthropic.com/research/...)",
      "reputation": "Anthropic is one of the major AI labs and the maker of Claude. Its engineering blog is widely read and cited in the AI practitioner community. It is a commercial vendor blog, not a peer-reviewed outlet, and posts go through no disclosed external review.",
      "editorial_process": "unknown"
    },
    "content_analysis": {
      "claims_checked": [
        {
          "claim": "As the number of tokens in the context window increases, a model's ability to accurately recall information from that context decreases ('context rot'), so context should be treated as a finite resource with diminishing returns.",
          "status": "corroborated",
          "evidence": "The article links to Chroma's 'Context Rot' technical report, which tested 18 frontier models including GPT-4.1, Claude 4, Gemini 2.5 and Qwen3 and found performance degrades as input length grows even on simple retrieval tasks. Independent commentary (understandingai.org) and the earlier 'Lost in the Middle' literature report the same phenomenon. Note: degradation is non-uniform/non-monotonic, which the article acknowledges by saying some models degrade more gently than others."
        },
        {
          "claim": "Techniques such as compaction, structured note-taking (agentic memory) and sub-agent architectures let agents work past the context window on long-horizon tasks.",
          "status": "corroborated",
          "evidence": "Anthropic's own product announcement (anthropic.com/news/context-management, same date 2025-09-29) documents context editing and a memory tool and reports 39% improvement (memory + context editing), 29% (context editing alone) and 84% lower token consumption on a 100-turn search eval. These are internal, unpublished evals; no independent replication was found. The techniques themselves are widely adopted in the field."
        },
        {
          "claim": "Multi-agent architectures 'showed a substantial improvement over single-agent systems on complex research tasks.'",
          "status": "contradicted",
          "evidence": "Anthropic's linked post (anthropic.com/research/multi-agent-research-system) reports a 90.2% gain on its own internal research eval, i.e. a self-reported, single-company benchmark. Independent coverage (theaiengineer.substack.com) notes the same architecture costs roughly 15x the tokens of a chat interaction, and Cognition's 'Don't Build Multi-Agents' (cognition.com/blog/dont-build-multi-agents) argues sub-agents that do not share full context can compound errors and be less reliable than a single agent, especially for coding. So 'contested', not settled fact."
        },
        {
          "claim": "Good context engineering means finding the smallest set of high-signal tokens; system prompts should sit at the 'right altitude'; tool sets should be minimal and non-overlapping; few-shot examples should be canonical rather than exhaustive edge cases.",
          "status": "no_evidence_found",
          "evidence": "This is practitioner guidance rather than an empirical claim. It is widely echoed by other practitioners (e.g. Manus, Simon Willison, and the 2026 'state of context engineering' write-ups), but I found no controlled study testing these specific recommendations."
        }
      ],
      "claims_supported_by_evidence": true,
      "sources_cited": true,
      "corroborated_by_other_sources": true,
      "contradicted_by_other_sources": true,
      "primary_vs_secondary": "secondary_source",
      "funding_or_sponsorship": "Corporate content: Anthropic is a commercial AI company (backed by Amazon, Google and others) that sells the Claude models and Claude Developer Platform discussed throughout the piece. The article ends with a call to action to start using the Claude Developer Platform. No separate funding or sponsorship disclosure, which is normal for a company blog but means the content is inherently promotional in part.",
      "bias_and_tone": "Neutral, technical and largely hedged ('we've observed', 'likely', 'we recommend'), with explicit trade-offs acknowledged (runtime retrieval is slower; aggressive compaction can lose later-critical detail; larger context windows may never fully solve the problem). No sensationalism. Bias is commercial rather than political: the framing favours Anthropic's own product roadmap, and the multi-agent result is presented as a success without mentioning its token cost or the contrary view from Cognition.",
      "date_published": "2025-09-29 (confirmed in page metadata and on the Engineering index page) "
    },
    "transparency_score": 3,
    "overall_credibility": "medium",
    "reasoning": "Strengths: a detailed, technically sophisticated account from a leading frontier lab; the key empirical claim (context rot) rests on a public, reproducible external study (Chroma) and standard primary literature (transformer paper, 'Lost in the Middle'-type work), and the engineering recommendations are concrete and traceable to Anthropic's docs. Weaknesses: no named author or bios anywhere on the page or in metadata (third-party attribution to the 'Applied AI team' only); no peer review or disclosed editorial process; the strongest performance numbers (39%/29%/84% and 90.2% multi-agent gain) come from unpublished internal evals of the company's own products, so they are marketing-adjacent evidence; the piece is commercially motivated (it ends by promoting the Claude Developer Platform) and does not engage the contrary view of multi-agent architectures (Cognition). Minor editorial sloppiness: the 'Sonnet 4.5 launch' link points back to the article itself. Overall, a reliable source for Anthropic's own framing and engineering practice, but not an independent or peer-reviewed source for empirical claims about model performance, hence Medium rather than High.",
    "evidence_urls": [
      "https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents",
      "https://www.anthropic.com/research/effective-context-engineering-for-ai-agents",
      "https://www.anthropic.com/engineering",
      "https://www.anthropic.com/about",
      "https://www.anthropic.com/news/context-management",
      "https://www.anthropic.com/research/multi-agent-research-system",
      "https://simonwillison.net/2025/Jun/14/multi-agent-research-system",
      "https://cognition.com/blog/dont-build-multi-agents",
      "https://www.trychroma.com/research/context-rot",
      "https://www.understandingai.org/p/context-rot-the-emerging-challenge",
      "https://towardsai.com/p/machine-learning/context-engineering-explained-the-anthropic-guide-thats-changing-how-developers-work-with-ai",
      "https://theaiengineer.substack.com/p/how-anthropic-built-multi-agent-deep",
      "https://x.com/AnthropicAI/status/1973098580060631341",
      "https://en.wikipedia.org/wiki/Anthropic"
    ]
  }
}
```
**Tool result** `assess_credibility` (id `call_563b67fb821344e8b69cae15`, 7,790 characters):

```
{
  "status": "evaluation_recorded",
  "evaluation": {
    "source_url": "https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents",
    "source_type": "corporate_blog",
    "author": {
      "name": "Unknown (no individual byline)",
      "credentials": "No named author on the page or in its metadata. The post is published under Anthropic's Engineering blog; a third-party summary (Towards AI) attributes it to Anthropic's 'Applied AI team', but the page itself names no people, roles or bios.",
      "credibility_assessment": "Institutional credibility only. Anthropic is a leading frontier AI lab, so the post reflects real practitioner expertise, but an uncritiqued, unnamed corporate author is harder to hold accountable than a signed, biographied piece."
    },
    "publication": {
      "name": "Anthropic (Engineering blog; URL redirects to anthropic.com/research/...)",
      "reputation": "Anthropic is one of the major AI labs and the maker of Claude. Its engineering blog is widely read and cited in the AI practitioner community. It is a commercial vendor blog, not a peer-reviewed outlet, and posts go through no disclosed external review.",
      "editorial_process": "unknown"
    },
    "content_analysis": {
      "claims_checked": [
        {
          "claim": "As the number of tokens in the context window increases, a model's ability to accurately recall information from that context decreases ('context rot'), so context should be treated as a finite resource with diminishing returns.",
          "status": "corroborated",
          "evidence": "The article links to Chroma's 'Context Rot' technical report, which tested 18 frontier models including GPT-4.1, Claude 4, Gemini 2.5 and Qwen3 and found performance degrades as input length grows even on simple retrieval tasks. Independent commentary (understandingai.org) and the earlier 'Lost in the Middle' literature report the same phenomenon. Note: degradation is non-uniform/non-monotonic, which the article acknowledges by saying some models degrade more gently than others."
        },
        {
          "claim": "Techniques such as compaction, structured note-taking (agentic memory) and sub-agent architectures let agents work past the context window on long-horizon tasks.",
          "status": "corroborated",
          "evidence": "Anthropic's own product announcement (anthropic.com/news/context-management, same date 2025-09-29) documents context editing and a memory tool and reports 39% improvement (memory + context editing), 29% (context editing alone) and 84% lower token consumption on a 100-turn search eval. These are internal, unpublished evals; no independent replication was found. The techniques themselves are widely adopted in the field."
        },
        {
          "claim": "Multi-agent architectures 'showed a substantial improvement over single-agent systems on complex research tasks.'",
          "status": "contradicted",
          "evidence": "Anthropic's linked post (anthropic.com/research/multi-agent-research-system) reports a 90.2% gain on its own internal research eval, i.e. a self-reported, single-company benchmark. Independent coverage (theaiengineer.substack.com) notes the same architecture costs roughly 15x the tokens of a chat interaction, and Cognition's 'Don't Build Multi-Agents' (cognition.com/blog/dont-build-multi-agents) argues sub-agents that do not share full context can compound errors and be less reliable than a single agent, especially for coding. So 'contested', not settled fact."
        },
        {
          "claim": "Good context engineering means finding the smallest set of high-signal tokens; system prompts should sit at the 'right altitude'; tool sets should be minimal and non-overlapping; few-shot examples should be canonical rather than exhaustive edge cases.",
          "status": "no_evidence_found",
          "evidence": "This is practitioner guidance rather than an empirical claim. It is widely echoed by other practitioners (e.g. Manus, Simon Willison, and the 2026 'state of context engineering' write-ups), but I found no controlled study testing these specific recommendations."
        }
      ],
      "claims_supported_by_evidence": true,
      "sources_cited": true,
      "corroborated_by_other_sources": true,
      "contradicted_by_other_sources": true,
      "primary_vs_secondary": "secondary_source",
      "funding_or_sponsorship": "Corporate content: Anthropic is a commercial AI company (backed by Amazon, Google and others) that sells the Claude models and Claude Developer Platform discussed throughout the piece. The article ends with a call to action to start using the Claude Developer Platform. No separate funding or sponsorship disclosure, which is normal for a company blog but means the content is inherently promotional in part.",
      "bias_and_tone": "Neutral, technical and largely hedged ('we've observed', 'likely', 'we recommend'), with explicit trade-offs acknowledged (runtime retrieval is slower; aggressive compaction can lose later-critical detail; larger context windows may never fully solve the problem). No sensationalism. Bias is commercial rather than political: the framing favours Anthropic's own product roadmap, and the multi-agent result is presented as a success without mentioning its token cost or the contrary view from Cognition.",
      "date_published": "2025-09-29 (confirmed in page metadata and on the Engineering index page) "
    },
    "transparency_score": 3,
    "overall_credibility": "medium",
    "reasoning": "Strengths: a detailed, technically sophisticated account from a leading frontier lab; the key empirical claim (context rot) rests on a public, reproducible external study (Chroma) and standard primary literature (transformer paper, 'Lost in the Middle'-type work), and the engineering recommendations are concrete and traceable to Anthropic's docs. Weaknesses: no named author or bios anywhere on the page or in metadata (third-party attribution to the 'Applied AI team' only); no peer review or disclosed editorial process; the strongest performance numbers (39%/29%/84% and 90.2% multi-agent gain) come from unpublished internal evals of the company's own products, so they are marketing-adjacent evidence; the piece is commercially motivated (it ends by promoting the Claude Developer Platform) and does not engage the contrary view of multi-agent architectures (Cognition). Minor editorial sloppiness: the 'Sonnet 4.5 launch' link points back to the article itself. Overall, a reliable source for Anthropic's own framing and engineering practice, but not an independent or peer-reviewed source for empirical claims about model performance, hence Medium rather than High.",
    "evidence_urls": [
      "https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents",
      "https://www.anthropic.com/research/effective-context-engineering-for-ai-agents",
      "https://www.anthropic.com/engineering",
      "https://www.anthropic.com/about",
      "https://www.anthropic.com/news/context-management",
      "https://www.anthropic.com/research/multi-agent-research-system",
      "https://simonwillison.net/2025/Jun/14/multi-agent-research-system",
      "https://cognition.com/blog/dont-build-multi-agents",
      "https://www.trychroma.com/research/context-rot",
      "https://www.understandingai.org/p/context-rot-the-emerging-challenge",
      "https://towardsai.com/p/machine-learning/context-engineering-explained-the-anthropic-guide-thats-changing-how-developers-work-with-ai",
      "https://theaiengineer.substack.com/p/how-anthropic-built-multi-agent-deep",
      "https://x.com/AnthropicAI/status/1973098580060631341",
      "https://en.wikipedia.org/wiki/Anthropic"
    ]
  }
}
```

## Turn 10

_Model call: 29,548 input tokens, 3,694 output tokens_

**Tool call** `save_report` (id `call_f91e6f24a7e84b118615f038`):

```json
{
  "filename": "anthropic-context-engineering-ai-agents.md",
  "markdown": "# Credibility Report: Effective context engineering for AI agents\n\n**URL:** https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents (redirects to https://www.anthropic.com/research/effective-context-engineering-for-ai-agents)\n**Verdict:** Medium credibility\n**Evaluated:** 2026-11-26\n\n## Summary\nThis is an engineering blog post published by Anthropic, the AI company behind Claude, on 29 September 2025. It argues that \"prompt engineering\" is being superseded by \"context engineering\" — curating the smallest set of high-signal tokens in an LLM's context window — and sets out concrete practices (system-prompt \"altitude\", minimal tool sets, just-in-time retrieval, compaction, structured note-taking, sub-agent architectures). The writing is technical, well hedged and hyperlinked, and its central empirical claim (so-called \"context rot\") is backed by an external, reproducible study from Chroma that I could verify independently. The main problems are structural rather than factual: there is **no named author anywhere on the page**, the outlet is a commercial vendor with an obvious interest in the recommendations, and the headline performance numbers (39%, 29%, 84%, 90.2%) come from Anthropic's own unpublished internal evaluations, with the multi-agent claim actively contested elsewhere in the industry (Cognition's \"Don't Build Multi-Agents\"). Overall: a credible, authoritative-*for-Anthropic* source that a student can cite carefully, but not a peer-reviewed or independent source for empirical claims about model performance.\n\n## Author\n- **No individual author is named.** There is no byline, no author box, no `Author:` metadata and no bios on the page, and the full text (21,665 characters, read to the end) contains no attribution beyond \"At Anthropic, we view…\" and \"we've observed…\".\n- A third-party explainer (Towards AI, November 2025) says the piece was published by \"Anthropic's Applied AI team\", which is consistent with how the company's engineering posts are usually produced — but this is not stated on the source itself, so I record the author as **Unknown**.\n- What can be attributed with confidence is institutional expertise: Anthropic builds the models the article is about, and the engineering blog has a substantive track record (multi-agent systems, tool design, MCP, evals).\n- Consequence: the argument has to be assessed on its references and logic rather than on a named expert's accountability. That is a real, if modest, credibility cost.\n\n## Publication\n- **Anthropic Engineering** (`anthropic.com/engineering`, with posts now served under `anthropic.com/research/`). Anthropic describes the team as building \"the infrastructure that makes Claude reliable and trustworthy\" and sharing \"what we learn about building, evaluating, and deploying AI agents at scale.\"\n- Anthropic is a public benefit corporation and one of the leading frontier AI labs; it is funded by large strategic investors including Amazon and Google (confirmed via Wikipedia's summary of Reuters/CNBC reporting). It sells Claude models, the Claude Developer Platform and Claude Code — the exact products the article recommends.\n- **Editorial process: not disclosed.** There is no masthead, editorial policy, peer-review statement or corrections log for the engineering blog that I could find, and `anthropic.com/about` returns only a one-paragraph mission statement. Posts are not peer reviewed.\n- Reputation: the engineering blog is heavily read and quoted in the AI practitioner community (Anthropic's own X post promoting this piece displayed ~510,000 views; a 2026 \"state of context engineering\" write-up treats it as one of two foundational mid-2025 posts). Wide citation by practitioners is evidence of influence, not of accuracy.\n\n## Claims Checked\n\n| Claim | Status | Evidence |\n|---|---|---|\n| \"Context rot\": as the number of tokens in the context window increases, a model's ability to accurately recall information from that context decreases, so context is a finite resource with diminishing returns. | **Corroborated** | The article links to Chroma's *Context Rot* technical report (https://www.trychroma.com/research/context-rot), which tested 18 frontier models (GPT-4.1, Claude 4, Gemini 2.5, Qwen3) and found performance degrades as input length grows even on simple retrieval/replication tasks — see also the ZenML summary and independent commentary at Understanding AI (https://www.understandingai.org/p/context-rot-the-emerging-challenge), which independently describes the Chroma study as \"widely read\". Caveat: degradation is non-uniform/non-monotonic (a shuffled haystack beat a coherent one in Chroma's tests); the article's phrasing is a fair simplification and it does say some models degrade more gently. |\n| Compaction, tool-result clearing, structured note-taking and sub-agent architectures let agents keep working beyond the context window on long-horizon tasks. | **Corroborated (only by Anthropic's own product data)** | Anthropic's product announcement dated the same day (https://www.anthropic.com/news/context-management) documents context editing and a memory tool and reports +39% (memory + context editing) and +29% (context editing alone) on an internal agentic-search eval and 84% lower token consumption on a 100-turn web-search eval. These are **unpublished internal evals**; I found no independent replication. The techniques themselves are widely adopted by other labs and practitioners. |\n| Multi-agent architectures \"showed a substantial improvement over single-agent systems on complex research tasks.\" | **Contested / not independently verified** | The article's own link (https://www.anthropic.com/research/multi-agent-research-system, echoed by Simon Willison's notes) gives the figure: a 90.2% gain for Opus 4 + Sonnet 4 sub-agents over single-agent Opus 4 on **Anthropic's internal research eval** — a self-reported benchmark. Independent analysis (https://theaiengineer.substack.com/p/how-anthropic-built-multi-agent-deep) notes the same architecture costs roughly 15× the tokens of a chat turn, a cost the article does not mention. Cognition's \"Don't Build Multi-Agents\" (https://cognition.com/blog/dont-build-multi-agents) argues that sub-agents without full shared context compound errors and can be less reliable than a single agent, particularly for coding. The article's own hedging (\"the decision boundary… depends on the task\") is fair, but the claim should be treated as one company's internal result, not a settled finding. |\n| Practitioner guidance: aim for the smallest set of high-signal tokens; keep system prompts at the \"right altitude\"; keep tool sets minimal and non-overlapping; use canonical few-shot examples rather than exhaustive edge cases. | **No evidence found** (not empirically tested) | This is normative engineering advice, not a testable factual claim. It is echoed by many other practitioners (Cognition, Manus, Simon Willison, and 2026 practitioner round-ups), which shows consensus — not controlled evidence. |\n\nOther details worth flagging:\n- The article says the memory tool shipped \"as part of our Sonnet 4.5 launch\" but the hyperlink points back to this same article — a broken self-link and a small sign of limited editorial checking.\n- The product claims in the article (Claude Code compaction behaviour, the Pokémon-playing agent, the memory tool in public beta) are verifiable against Anthropic's own docs/news (https://www.anthropic.com/news/context-management) but are self-reported product descriptions.\n\n## Bias and Tone\n- **Tone:** calm, technical and mostly hedged (\"we've observed\", \"likely\", \"we recommend\", \"for the foreseeable future\"). No hype adjectives, no outrage, no clickbait. It explicitly acknowledges limitations: runtime retrieval is slower than pre-computed retrieval; agents can waste context chasing dead ends; aggressive compaction can discard detail whose importance only appears later; larger context windows alone probably will not solve the problem.\n- **Commercial interest:** substantial and undisclosed as an interest. Anthropic sells the models, Claude Code and Developer Platform APIs the piece is effectively a guide to, and the article closes with a call to action: \"Get started with context engineering in the Claude Developer Platform today.\" That does not make the advice wrong, but the piece is partly a developer-marketing asset.\n- **Omissions:** the multi-agent result is presented as a win with no mention of its token cost and no reference to the significant public counter-argument from Cognition; no competing or failed approaches are discussed.\n- **No political or ideological agenda** beyond ordinary vendor positioning; no donation or advocacy interest.\n\n## Currency\n- Published **29 September 2025** (confirmed both in the page's `Published Time` metadata and on the Engineering index page). No \"last updated\" date is shown.\n- As of 2026-11-26 the post is about **14 months old**. In a field that moves this fast that is middle-aged: the conceptual framing and the techniques remain standard and are still cited in 2026 practitioner literature, but specific product details (Claude Sonnet 4.5, the memory tool \"in public beta\", the latest model generation at the time) are dated, and Anthropic's own later posts (e.g. *Equipping agents for the real world with Agent Skills*, Oct 2025; *The components of agent memory*, Nov 2026) extend or revise parts of this picture.\n- Fine to cite as a landmark statement of the concept; do not cite it for \"current capabilities\" or current product behaviour.\n\n## Structured Assessment\n\n| Field | Value |\n|---|---|\n| **Source URL** | https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents |\n| **Source type** | Corporate blog (vendor engineering blog) |\n| **Author** | Unknown — no byline, no bios, no author metadata; third-party attribution to Anthropic's \"Applied AI team\" only |\n| **Author credibility** | Institutional only (frontier AI lab), no named accountable individual |\n| **Publication** | Anthropic Engineering (anthropic.com) |\n| **Publication reputation** | Major AI lab's engineering blog, heavily read and cited by practitioners; not peer reviewed; no public editorial policy or corrections process found |\n| **Date published** | 2025-09-29 |\n| **Last updated** | Not shown |\n| **Claims supported by evidence** | Yes — external links to Chroma's study, the transformer paper, an arXiv position-interpolation paper, Karpathy, Simon Willison, plus Anthropic docs |\n| **Sources cited** | Yes |\n| **Corroborated by other sources** | Yes (context rot; context-management techniques) |\n| **Contradicted by other sources** | Yes (multi-agent superiority is contested, e.g. Cognition) |\n| **Primary vs secondary** | Secondary for the science; primary for \"what Anthropic does and recommends\" |\n| **Funding / sponsorship** | Commercial vendor content; Anthropic is backed by Amazon and Google and sells the products recommended; no separate disclosure |\n| **Bias and tone** | Neutral, technical, hedged; acknowledges trade-offs; commercially self-interested; silent on costs and on contrary views |\n| **Transparency score** | 3 / 5 (sources and production context are clear; **author is not identified**; funding/interest not disclosed) |\n| **Overall credibility** | **Medium** |\n\n## Can I cite this?\n**Cite it — with care, and for the right things.**\n\n- **Good uses.** As an authoritative primary statement of *what Anthropic recommends* and of how a leading lab builds agentic systems: `(Anthropic, 2025)`. Also good for framing/definitions (\"context engineering\", \"context rot\", the \"smallest set of high-signal tokens\" principle) and for named techniques (compaction, structured note-taking, sub-agent isolation, just-in-time retrieval).\n- **Cite in the knowledge that** it is a vendor blog, the author is unnamed, and it has not been peer reviewed — say so in a footnote if your assignment requires source evaluation.\n- **Do not use it as your only evidence** for empirical numbers. The 90.2% multi-agent gain and the 39%/29%/84% context-management figures are unpublished internal evals of Anthropic's own products. For those, cite the primary or independent work instead: Chroma's *Context Rot* report for the degradation effect, and for multi-agent trade-offs pair the Anthropic result with Cognition's \"Don't Build Multi-Agents\" so you show both sides.\n- **Find a better source** if your claim is about model capability, benchmark performance or the state of the art generally — use peer-reviewed papers (e.g. arXiv transformer paper; \"Lost in the Middle\") or independent evaluations, and use a 2026-dated source for current tooling, since this piece predates several product changes.\n- **Where it stands among alternatives:** stronger than a generic SEO blog or Medium repost (real engineering depth, traceable references, verifiable product docs); weaker than peer-reviewed literature or an independent technical evaluation body (no named authors, no review, commercial interest).\n\n## Sources Consulted\n1. https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents — the source itself, read in full (all 21,665 characters); no author byline, Publication date 2025-09-29, external links to Chroma, arXiv, Hugging Face, Karpathy, Simon Willison, Anthropic docs.\n2. https://www.anthropic.com/research/effective-context-engineering-for-ai-agents — the URL the engineering link now redirects to; same content.\n3. https://www.anthropic.com/engineering — Engineering index page: confirms the 29 Sept 2025 date, the team's self-description and the blog's wider catalogue (30 articles, latest Nov 2026).\n4. https://www.anthropic.com/about — one-paragraph mission statement (\"Anthropic is a Public Benefit Corporation\"); no editorial policy, masthead or author information.\n5. https://www.anthropic.com/news/context-management — Anthropic product announcement dated 2025-09-29: context editing + memory tool, with 39%/29% internal-eval improvements and 84% token reduction. Confirms the techniques exist; also confirms the numbers are internal.\n6. https://www.anthropic.com/research/multi-agent-research-system — Anthropic's multi-agent post: the 90.2% gain is on \"our internal research eval\".\n7. https://simonwillison.net/2025/Jun/14/multi-agent-research-system — independent practitioner's quotation of the same 90.2% internal-eval figure and the 90% time reduction; useful cross-check of what was claimed.\n8. https://www.trychroma.com/research/context-rot — Chroma's primary technical report: 18 models, performance consistently degrades with input length; supports the \"context rot\" claim.\n9. https://www.zenml.io/llmops-database/context-rot-evaluating-llm-performance-degradation-with-increasing-input-tokens — third-party summary of the Chroma report (models tested, experimental design).\n10. https://www.understandingai.org/p/context-rot-the-emerging-challenge — independent commentary confirming the phenomenon and noting that current mitigation techniques \"can only mitigate\" the underlying problem.\n11. https://cognition.com/blog/dont-build-multi-agents — Cognition's counter-argument to multi-agent architectures (context sharing, error compounding); used as contradicting evidence for the sub-agent claim.\n12. https://theaiengineer.substack.com/p/how-anthropic-built-multi-agent-deep — independent analysis of Anthropic's multi-agent numbers, including the ~15× token cost not mentioned in the source.\n13. https://towardsai.com/p/machine-learning/context-engineering-explained-the-anthropic-guide-thats-changing-how-developers-work-with-ai — third-party explainer that attributes the post to \"Anthropic's Applied AI team\" (the only author-type attribution found).\n14. https://x.com/AnthropicAI/status/1973098580060631341 — Anthropic's own promotional post for the article (posted 2025-09-30, ~510k views); shows reach, not accuracy.\n15. https://en.wikipedia.org/wiki/Anthropic — background on Anthropic's structure (public benefit corporation) and its Google/Amazon funding, cited to Reuters/CNBC.\n16. https://www.bybit.com/en/wiki/article/anthropic-valuation-61b-funding-growth and https://news.crunchbase.com/ai/google-anthropic-openai-funding-wars — search results supporting the corporate-investment background (used only for context on commercial interest).\n"
}
```
**Tool result** `save_report` (id `call_f91e6f24a7e84b118615f038`, 91 characters):

```
Saved the report to reports/anthropic-context-engineering-ai-agents.md (16,351 characters).
```

## Turn 11

_Model call: 33,276 input tokens, 176 output tokens_

**Assistant:**

**Verdict: Medium credibility.** Anthropic's "Effective context engineering for AI agents" (published 29 Sept 2025) is a technically serious, well-hedged engineering post whose central empirical claim — "context rot" — is backed by an external, reproducible Chroma study I could verify, but it has no named author anywhere on the page, is commercial vendor content that ends by promoting the Claude Developer Platform, and its headline performance figures (39%/29%/84%, and the 90.2% multi-agent gain) come from Anthropic's own unpublished internal evals, with the multi-agent recommendation actively contested by Cognition. Cite it as a primary statement of what Anthropic recommends, and pair it with independent or peer-reviewed sources for the numbers. The report was saved as `anthropic-context-engineering-ai-agents.md`.


## Final output

**Verdict: Medium credibility.** Anthropic's "Effective context engineering for AI agents" (published 29 Sept 2025) is a technically serious, well-hedged engineering post whose central empirical claim — "context rot" — is backed by an external, reproducible Chroma study I could verify, but it has no named author anywhere on the page, is commercial vendor content that ends by promoting the Claude Developer Platform, and its headline performance figures (39%/29%/84%, and the 90.2% multi-agent gain) come from Anthropic's own unpublished internal evals, with the multi-agent recommendation actively contested by Cognition. Cite it as a primary statement of what Anthropic recommends, and pair it with independent or peer-reviewed sources for the numbers. The report was saved as `anthropic-context-engineering-ai-agents.md`.

## Summary

- Turns (model calls): 11
- Tool calls: web_search x7, read_url x6, assess_credibility x1, save_report x1
- Tokens: 169,522 input (134,912 cached), 9,614 output
- Estimated cost: $0.0114
- Report: reports/anthropic-context-engineering-ai-agents.md
- URLs in anthropic-context-engineering-ai-agents.md not seen in any tool result: https://x.com/AnthropicAI/status/1973098580060631341
