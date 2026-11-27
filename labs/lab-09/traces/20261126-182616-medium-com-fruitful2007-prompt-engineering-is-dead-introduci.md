# Agent trace: https://medium.com/@fruitful2007/prompt-engineering-is-dead-introducing-context-engineering-6280c075a1a9

- Model: `deepseek/deepseek-v4.1-flash-1017`
- Started: 2026-11-26T18:26:16
- Max turns: 25
- Tools: read_url, web_search, assess_credibility, save_report


**User:** Evaluate the credibility of this source: https://medium.com/@fruitful2007/prompt-engineering-is-dead-introducing-context-engineering-6280c075a1a9

## Turn 1

_Model call: 4,162 input tokens, 94 output tokens_

**Assistant:**

I'll start by reading the source page.

**Tool call** `read_url` (id `call_c265a175fd334e04bbfa9561acf29b3c`):

```json
{
  "url": "https://medium.com/@fruitful2007/prompt-engineering-is-dead-introducing-context-engineering-6280c075a1a9",
  "start": 0
}
```
**Tool result** `read_url` (id `call_c265a175fd334e04bbfa9561acf29b3c`, 10,096 characters):

```
Title: PROMPT ENGINEERING IS DEAD INTRODUCING CONTEXT ENGINEERING

URL Source: https://medium.com/@fruitful2007/prompt-engineering-is-dead-introducing-context-engineering-6280c075a1a9

Published Time: 2025-07-21T00:17:53Z

Markdown Content:
## THE NEW HYPE

[![Image 1: Paul Fruitful](https://miro.medium.com/v2/resize:fill:64:64/1*eLpBCQ_I9E1jCEkYs9-eFg.jpeg)](https://medium.com/@fruitful2007?source=post_page---byline--6280c075a1a9------------------------------------------)

7 min read

Jul 21, 2025

Press enter or click to view image in full size

![Image 2](https://miro.medium.com/v2/resize:fit:700/1*CJY4Lw7TBmtpIIECdGosNA.png)

So, over time, we’ve been talking about how the right context is what agents need to work better.   
**Context! Context! Context!**  
Everyone is talking about how agents need context, because the truth is that LLMs, naturally, are next-token predictors and for them to predict accurately, they must be given the right prompts (tokens) prior to their new prediction.

So, if you give them bad context (prompts (tokens)) from the start, their prediction will be off the charts in a bad way😕. It might underperform what you actually intended or overperform (overperform your disappointment 😂)

But the truth is:

### Context is everything to an LLM

Context is the language LLMs speak.  
Because without context, they can’t predict.  
Without understanding and analyzing enough data, they can’t be able to tell what comes next.

So, it is the responsibility of an AI engineer to provide their agents with enough context.

So,

### What’s this context engineering hype?

Prompt engineering was all about crafting the perfect prompts to get outputs and information out of LLMs.  
Context engineering seems different.  
Context engineering is like a superset of prompt engineering.  
This is what context engineering is, as Andrej Karpathy defines it:

> "It’s the art of filling in the context window with the right information so that the LLM knows what’s next."

You see that? It’s about crafting worlds/environments inside the mind of agents (the context window )

So, prompt engineering was about creating a single prompt or creating a prompt flow to get the best information/output out of an LLM.

But context engineering is about shaping the entire context window to fit your needs.  
Utilizing the whole context window to extract efficiency from large language models.  
That’s what context engineering is all about.

Now, you're not just crafting single prompts, no.  
You're building environments on top of the LLM's context window to bring out the best from them.  
To bring out the best outputs from them.

In context engineering, your prompts don’t come out ad hoc. They come out of your context, your environment.  
Context engineering is all about creating worlds inside LLMs for specific tasks.  
That’s what context engineering is all about, being able to create a world, an environment, a system that has everything the model needs to function in a specified task.

The truth is, "Context Engineering" is actually just a fancy word.  
All the things I’m saying right now? Just grammar.  
Context engineering has always been a thing.

It didn’t start today, it didn’t start last week, It’s been here since LLMs came along.

We’re just now standardizing it, making it a thing, a field, a study which is actually interesting.  
I was drowning in a lot of research papers this morning about context engineering, optimization functions, trying to find the right context to give an LLM to get the best output from the optimizer function.

Which were pretty interesting because in theory, they’re sweet.  
But in reality? Do they really matter?  
They do matter but they’re abstracted.

## My honest take on Context Engineering

It’s just a fancy word and it’s coined in a way that makes it look more complex than it actually is, more scientific than it actually is.

Context Engineering is just building worlds, engineering worlds of context inside the mind of an LLM.   
Now you might ask:

### What is the mind of an LLM?

Do LLMs have minds?Oh yes, they do. But it’s not organic like ours, inside the brain it’s statistical and mathematical.   
The context window is the mind of the LLM.

And inside that context window, everything that exists are just tokens in a vector embedding space.

So all those tokens exist there, and the context window, that space just keeps the generated "next" tokens to fill up the empty space inside the window.

Basically, Context Engineering is all about us guiding how information is structured in this vector space

As Andrej Karpathy says:

> “It’s about filling the context windows of LLMs with the right information so they know what’s next.”

And the truth is you’ve actually been doing Context Engineering way before this way before it was a thing.

So maybe you wanted to do a task with ChatGPT.   
First of all, you didn’t know how to explain the task.  
 So you sent the PDF of the book you were trying to read. Then you started asking questions about that book.  
That is actually a form of Context Engineering.

Whereas prompt engineering was about crafting search queries to dig into the context window (and the brain) of the LLM to pull out information...

So,

### How do you even engineer context for agents?

Let’s start with the first step.

Before that, I'd like to make a reference to humans.  
When we were born, we knew nothing about this world.  
We didn’t even know the processes happening around us.  
We didn’t know rain could fall.  
We were just... there, innocent cute babies unconscious of surroundings.  
But gradually, information was distilled into us by our parents, our guardians, the authority figures over us.  
We were being context engineered, our context window (our mind) was being shaped by our environment.  
Now we are fully functional. We understand the world we live in

## Get Paul Fruitful’s stories in your inbox

Join Medium for free to get updates from this writer.

Remember me for faster sign in

The same thing goes for agents.  
When they are birthed, they have foundational knowledge from the training they were given.  
But when you give them tasks, they don’t know the world in which those tasks exist.

That is why it is your responsibility, as an AI engineer performing context engineering...  
...to engineer the world into the model’s mind.

What is the model’s mind?  
Its context window!  
Because that is where it uses to generate and predict the next tokens.  
So, it is your responsibility to craft that environment directly into the model’s mind.

### How do you do that?

You start by explaining the world it operates in

Let’s say you’re building an agent that reads emails, summarizes them, and performs some actions.

So, crafting a world for that email agent means explaining the world it lives in.

That world is your email inbox.

That’s the world the agent lives in.

Now, it’s your responsibility to break down the elements of that world.

Just like we have air, oxygen, chemical elements, the sky, sand...

You explain the elements that exist in that agent’s world.

The elements are:

*   The meta information about the world
*   The entities that exist in the world
*   The tools it can use
*   The constraints that exist in that world

Now, that gives the agent more perspective.  
And it tunes how it generates tokens to match the tasks you threw at it.

Which is pretty interesting.

Now, you might think:

“Okay, that means I can engineer context with just prompts."  
Yes, you can.  
Because at the end of the day, you use prompts to engineer context.  
But prompt engineering is not context engineering.

Prompt engineering is a part of context engineering.

Prompt engineering kind of acts on the system that your context-engineered environment creates.

So, I dive deeper  
The next step, after you create a world inside an agent, is persisted memory.

Without memory, agents are useless.  
Because they always forget.  
They don’t learn in real time.

They will always forget what you put inside them.

And hard-coded memory is also kinda... should I say, flawed?  
Because at the start of everything, you have to come and start explaining it all again.  
That’s why persistent memory exists.  
But there’s a constraint. A global constraint in context engineering: The context window size!

If your agent is working in a large and robust world, it will be hard to give it all the context it needs, without hitting the context window limit.

But there are ways to bypass that, using memory banks, like vector databases and context banks.  
But I hate the term memory banks (personal preference 😅)  
I’d rather call them context banks.

I’m actually building one for myself.  
A system where I’ll be able to share one context dynamically across a group of agents, without even filling their context windows.

So what happens is:  
Whenever an agent needs context on a particular thing, it draws that context directly from my context bank.

And it only draws the adequate context it needs.  
Not redundant context that it doesn’t need.

Just the context it needs for that specified action.

This reduces the risk of overflowing the context window.  
And makes the agent more agile and efficient.

I’ll release it in a few weeks. It’s not as complex as it looks, it’s actually very easy to set up:  
A vector database acting as the bank, a smart search agent and the rest of it. I’ll go into the details later.  
It’ll be open source too. So stay tuned for that.

There’s also a mathematical side to context engineering.  
In fact, there are mathematical foundations for it.  
There’s the assembler function that assembles every component of context (information, tools, constraints) all those elements I defined earlier when creating a context world.

And then there are optimizer functions, all about finding the best context to get the most out of the model’s optimizer.

So, at the end of the day, ignore the word salads, the conf

[Showing characters 0-10,000 of 10,303. Call read_url with start=10000 to read the next part.]
```

## Turn 2

_Model call: 7,072 input tokens, 93 output tokens_

**Tool call** `read_url` (id `call-77eb2a97-41b2-4f1c-8875-ac4e45334390`):

```json
{
  "url": "https://medium.com/@fruitful2007/prompt-engineering-is-dead-introducing-context-engineering-6280c075a1a9",
  "start": 10000
}
```
**Tool result** `read_url` (id `call-77eb2a97-41b2-4f1c-8875-ac4e45334390`, 362 characters):

```
using grammar, all the fancy scientific terms.

Context engineering is just providing and structuring the right information inside the context window of agents using basically prompts.

And the truth is: You probably do this every day with ChatGPT😂  
That’s it for this article.  
Thank you for reading


[End of page. Showed characters 10,000-10,303 of 10,303.]
```

## Turn 3

_Model call: 7,256 input tokens, 254 output tokens_

**Tool call** `web_search` (id `call-48133613-8742-4ac2-a9ab-3e3fc1df18c5`):

```json
{
  "query": "\"Paul Fruitful\" Medium author AI engineer"
}
```
**Tool call** `web_search` (id `call-90055284-c6c9-40c4-8118-b80387a94d39`):

```json
{
  "query": "Karpathy \"context engineering\" quote \"filling the context window\" definition"
}
```
**Tool result** `web_search` (id `call-48133613-8742-4ac2-a9ab-3e3fc1df18c5`, 5,472 characters):

```
Search results for ""Paul Fruitful" Medium author AI engineer" (searched 2026-11-26):

[1] AI Agent Insurance for Agent Owners | Paul Fruitful posted on the topic | LinkedIn
URL: https://www.linkedin.com/posts/paulfruitful_insurance-for-ai-agents-now-this-is-one-activity-7457399028985597952-_EQs
Excerpt: Hong Le Viet, DBA   3mo 

 Report this comment

you can check this github.com/streamentry/AGENTOWNERS

Like Reply  1 Reaction

To view or add a comment, sign in

3,247 followers

 660 Posts
 37 Articles

View Profile   Connect

## More from this author

 

  ### AI Sovereignty: Who Controls The Weights?

  Paul Fruitful   4mo
 

  ### The AI Wild West Era Is Coming To An End

  Paul Fruitful   4mo
 

  ### Agentic Engineering: Goodbye To Building Slop Software

  Paul Fruitful   8mo [...] ## Explore related topics

 Benefits of Agentic AI for Businesses
 AI types in insurance industry
 Engineering insurance in the AI era
 Benefits of front-office AI in insurance
 How to build multiple AI assistants for insurance
 Using synthetic agents in insurance
 AI assistant for insurance policy details
 How to Use Agentic AI in Marketing Strategies
 Algorithmic economy for insurers
 Benefits of AI Agents for Email Ticket Deflection

## Explore content categories [...] View profile for Paul Fruitful 

Paul Fruitful

 Report this post

[2] Paul Iusztin | AI Engineer, Author & Educator
URL: https://www.pauliusztin.ai
Excerpt: # Hi, I'm Paul.

### I help engineers ship AI products.

Bestselling author of the LLM Engineer's Handbook, lead instructor of the Agent Engineering course, and founding AI engineer at a San Francisco start-up. I teach AI engineering end-to-end, from idea to production.

## What People Say

"Working with Paul on the LLM Engineer's Handbook showed me his unique ability to bridge the gap between theoretical AI and modern AI Engineering best practices."

Maxime Labonne [...] Maxime Labonne

"Paul is one of the rare people who truly understands both the technical depth of AI and how to teach it in a way that's engaging and actually clicks."

Louis-Francois Bouchard

"Paul doesn't just talk about AI - he builds it, and when he talks, it's worth listening."

Maria Vechtomova

"If you are serious about building with AI and leave the hype behind, Paul is one of those folks you should follow."

Eduardo Ordax

"If it's decodable, Paul will decode it for you." [...] Pau Labarta Bajo

"In a world where most just talk about AI, Paul actually builds it. A true AI engineer, who shows how to create AI systems that actually work."

Miguel Otero Pedrido

"Decoding AI is an invaluable resource for technical builders to stay up to date in such a rapidly moving space: bookmark it!"

Hugo Bowne-Anderson

"I've learned a lot from Paul. He's my go-to guy when it comes to MLOps."

Shaw Talebi

[3] Fruitful AI CEO, Founder, Key Executive Team, Board of Directors & Employees
URL: https://www.cbinsights.com/company/fruitful-1/people
Excerpt: was founded in 2021 and is based in Munich, Germany. [...] Covision Lab is an innovation hub specializing in Computer Vision and AI within the technology sector. The company focuses on deep learning, image and video analysis, embedded vision, and 3D sensing to develop real-world solutions that bridge academic research and industrial practice. Covision Lab primarily serves sectors that require advanced imaging and sensing technologies, such as industrial manufacturing and digital content creation. It was founded in 2019 and is based in Bolzano, Italy. [...] 36ZERO Vision provides artificial intelligence (AI)-powered visual quality control solutions for manufacturers across various industries. It offers a platform that allows users to train deep learning algorithms for defect and anomaly detection in production lines. Its technology can integrate with different camera systems, supporting quality assurance processes. It serves automotive, electrical, mechanical, textile, and other industries. It was formerly known as FotoNow. It was founded in 2021

[4] Paul Fruitful on Facebook
URL: https://www.facebook.com/frutful.paul/videos/1396039759255562
Excerpt: # Paul Fruitful on Facebook

- Author: Paul Fruitful
- Posted: 2026-07-29T17:16:52+00:00
- Reactions: 0
- Comment count: 0
- Privacy: Public group

[5] He Wrote a Coding Bestseller, Now He Says Don't Code | Paul Iusztin, Founder@Decoding AI
URL: https://www.youtube.com/watch?v=OLt8pZjR-b4
Excerpt: Questions answered:
Who is Paul Iusztin? → Paul Iusztin is a founding AI engineer at a San Francisco startup building vertical AI agents for financial advisors, the author of LLM Engineer's Handbook (~20,000 copies sold), and the creator of Decoding AI — a 40,000-subscriber newsletter on production AI engineering. He works remotely from Portugal and recently launched the Agentic AI Engineering course. [...] ⏱️ Chapters:
0:00 - Why this AI engineer killed RAG, MCP, and agentic loops
1:25 - When does RAG actually make sense
4:30 - Why everyone is using MCP wrong
7:00 - Is vibe coding the future of engineering
9:30 - Why he chose Portugal over San Francisco
12:00 - outro [...] How do I get an AI engineering job without grinding leetcode? → Build a public portfolio. Paul Iusztin spent five years building in public — newsletter, book, LinkedIn posts — and stopped doing traditional interviews entirely. Companies came to him with specific problems, framed as service contracts. Slower than leetcode prep, but it compounds.
```
**Tool result** `web_search` (id `call-90055284-c6c9-40c4-8118-b80387a94d39`, 6,673 characters):

```
Search results for "Karpathy "context engineering" quote "filling the context window" definition" (searched 2026-11-26):

[1] Karpathy Puts Context at the Core of AI Coding -- Pure AI
URL: https://pureai.com/articles/2025/09/23/karpathy-puts-context-at-the-core-of-ai-coding.aspx
Excerpt: As Karpathy puts it: context engineering is "the delicate art and science of filling the context window with just the right information for the next step." The difference is that prompts instruct what to do now, while context shapes how the model understands the world in which it must act. [...] Karpathy weighed in on the subject on June 25 in a post on X, favoring context engineering. "People associate prompts with short task descriptions you'd give an LLM in your day-to-day use," he wrote. "When in every industrial-strength LLM app, context engineering is the delicate art and science of filling the context window with just the right information for the next step." [...] But prompts are turning out to be only half the story. As applications become more ambitious, models gain larger context windows, and retrieval and memory systems are layered in, a different discipline begins to emerge —the one that Karpathy has now identified as the real key to AI application development: context engineering.

[2] Context engineering vs prompt engineering | HoneyHive
URL: https://www.honeyhive.ai/learn/context-engineering-vs-prompt-engineering
Excerpt: Andrej Karpathy wrote the version LangChain and others quote: people associate prompts with short task descriptions, while in an industrial-strength LLM app, “context engineering is the delicate art and science of filling the context window with just the right information for the next step.” He lists what goes in: task descriptions and explanations, few-shot examples, RAG, related data, tools, state and history, and compacting. [...] Karpathy goes the other way on scope. Karpathy calls context engineering “just one small piece of an emerging thick layer of non-trivial software” that also breaks problems into control flows, dispatches calls to the right model, handles generation-verification UI, and covers guardrails, security, evals, parallelism and prefetching. [...] Karpathy describes both directions: with too little, or the wrong form, the model lacks what it needs, and with too much or irrelevant material, “the LLM costs might go up and performance might come down.”

Everything in a request counts, per the Claude docs: the system prompt, every message, tool results, images, documents and tool definitions.

## The techniques

LangChain sorts context engineering for agents into four strategies.

[3] From Prompt Engineering to Context Engineering – Artificial Intelligence for Research Administration
URL: https://ai4ra.uidaho.edu/from-prompt-engineering-to-context-engineering
Excerpt: However, in recent conversations around AI and its development a new term has emerged: context engineering. In mid-2025, the term gained traction rapidly after Shopify CEO Tobi Lütke and former OpenAI researcher Andrej Karpathy both endorsed it publicly.

> Karpathy described it as “the delicate art and science of filling the context window with just the right information for the next step.”
>
> Andrej Karpathy [...] All that information, everything the AI can “see” when it generates a response, is called its context. And the maximum size of the context that a model can handle is called its context window. And it turns out that the quality of that context matters far more than the exact phrasing of any single prompt. As Karpathy put it, the shift is from asking smart questions to building smarter environments for the AI to work in.

[4] Context Engineering: Bringing Engineering Discipline to Prompts
URL: https://addyo.substack.com/p/context-engineering-bringing-engineering
Excerpt: > “I really like the term ‘context engineering’ over prompt engineering,” wrote Tobi. “It describes the core skill better: the art of providing all the context for the task to be plausibly solvable by the LLM.” Karpathy emphatically agreed, noting that people associate prompts with short instructions, whereas in every serious LLM application, context engineering is the delicate art and science of filling the context window with just the right information for each step. [...] This realization is why our field is coalescing around “context engineering” as a better descriptor for the craft of getting great results from AI. Context engineering means constructing the entire context window an LLM sees – not just a short instruction, but all the relevant background info, examples, and guidance needed for the task.

The phrase was popularized by developers like Shopify’s CEO Tobi Lütke and AI leader Andrej Karpathy in mid-2025. [...] A useful mental model (suggested by Andrej Karpathy and others) is to think of an LLM like a CPU, and its context window (the text input it sees at once) as the RAM or working memory. As an engineer, your job is akin to an operating system: load that working memory with just the right code and data for the task. In practice, this context can come from many sources: the user’s query, system instructions, retrieved knowledge from databases or documentation, outputs from other tools, and summaries

[5] Context Engineering
URL: https://www.langchain.com/blog/context-engineering-for-agents
Excerpt: As Andrej Karpathy puts it, LLMs are like a new kind of operating system. The LLM is like the CPU and its context window is like the RAM, serving as the model’s working memory. Just like RAM, the LLM context window has limited capacity to handle various sources of context. And just as an operating system curates what fits into a CPU’s RAM, we can think about “context engineering” playing a similar role. Karpathy summarizes this well: [...] > [Context engineering is the] ”…delicate art and science of filling the context window with just the right information for the next step.”

Context types commonly used in LLM applications

What are the types of context that we need to manage when building LLM applications? Context engineering as an umbrella that applies across a few different context types: [...] Share

## TL;DR

Agents need context to perform tasks. Context engineering is the art and science of filling the context window with just the right information at each step of an agent’s trajectory. In this post, we break down some common strategies — write, select, compress, and isolate — for context engineering by reviewing various popular agents and papers. We then explain how LangGraph is designed to support them!

Also, see our video on context engineering here.
```

## Turn 4

_Model call: 10,235 input tokens, 504 output tokens_

**Tool call** `read_url` (id `call-c23fea85-306f-4df6-a78a-f59824b7a98d`):

```json
{
  "url": "https://medium.com/@fruitful2007",
  "start": 0
}
```
**Tool call** `web_search` (id `call-c6cbb527-296a-4be7-8ea5-aafe9ef40621`):

```json
{
  "query": "\"fruitful2007\" OR \"Paul Fruitful\" context engineering prompt engineering article"
}
```
**Tool result** `web_search` (id `call-c6cbb527-296a-4be7-8ea5-aafe9ef40621`, 7,676 characters):

```
Search results for ""fruitful2007" OR "Paul Fruitful" context engineering prompt engineering article" (searched 2026-11-26):

[1] The New Skill in AI is Not Prompting, It's Context Engineering
URL: https://www.philschmid.de/context-engineering
Excerpt: What is context engineering? While "prompt engineering" focuses on crafting the perfect set of instructions in a single text string, context engineering is a far broader. Let's put it simply:

> Context Engineering is the discipline of designing and building dynamic systems that provides the right information and tools, in the right format, at the right time, to give a LLM everything it needs to accomplish a task.

Context Engineering is [...] Then you can generate a response.

> Hey Jim! Tomorrow’s packed on my end, back-to-back all day. Thursday AM free if that works for you? Sent an invite, lmk if it works.

The magic isn't in a smarter model or a more clever algorithm. It’s in about providing the right context for the right task. This is why context engineering will matter. Agent failures aren't only model failures; they are context failures.

## From Prompt to Context Engineering [...] To understand context engineering, we must first expand our definition of "context." It isn't just the single prompt you send to an LLM. Think of it as everything the model sees before it generates a response.

[2] Context engineering vs. prompt engineering | Elasticsearch Labs
URL: https://www.elastic.co/search-labs/blog/context-engineering-vs-prompt-engineering
Excerpt: Key distinction: Prompt engineering takes the context window as given. Context engineering actively curates it.

### Tool orchestration

Prompt engineering can request tool use and describe what tools should do. Context engineering decides which tools to make available, what information to pass them, and how their outputs flow back into context. [...] ### Single-turn vs. multi-turn

Prompt engineering optimizes one interaction. Context engineering thinks in sequences: What did previous turns establish? What tool outputs carry forward? What should persist three steps from now? As tasks move from simple question-answering to multistep agent workflows, context engineering becomes the dominant challenge.

### Context window management

Context engineering manages a finite resource with three failure modes: [...] ### Why it worked

 Prompt engineering: Clear genre specification and concrete examples (Lord of the Rings, Foundation) eliminated ambiguity.
 Context engineering: Focused retrieval bringing only relevant books, maintaining a manageable context window despite the dataset having 103,063 entries.

The agent used the same tools in all three cases, but input quality determined how effectively those tools retrieved relevant context.

## Conclusion

[3] Context Engineering: The Next Frontier Beyond Prompt Engineering | deepset Blog
URL: https://www.deepset.ai/blog/context-engineering-the-next-frontier-beyond-prompt-engineering
Excerpt: Context engineering differs from (and extends) prompt engineering. In brief, prompt engineering focuses on crafting the text of the prompt itself – the instructions or question given directly to the model – whereas context engineering is about designing the entire environment of information that surrounds the prompt.

Some key differences include: [...] approach to steering AI systems, especially as we build more complex agents and enterprise applications. It addresses the question, “What information and environment should we give an AI model so that it can accomplish a task effectively?” rather than just “How do we phrase the prompt?”. In this article we will explain what context engineering is, how it differs from prompt engineering, why it’s crucial, and what techniques and concepts it involves for those building cutting-edge AI [...] In summary, context engineering elevates AI systems from toy demos to reliable products. It recognizes that powerful models still need the right information to solve real business problems. Many failures in AI applications trace back to context failures rather than model failures – if the model wasn’t given the necessary facts or was distracted by irrelevant text, naturally the output will suffer. Context engineering directly tackles this by ensuring the model’s limited attention is focused

[4] Context Engineering Guide | Prompt Engineering Guide<!-- -->
URL: https://www.promptingguide.ai/guides/context-engineering-guide
Excerpt: There are many parts to this prompt that require careful consideration about what exact context we are providing the planning agent to carry out the task effectively. As you can see, it’s not just about designing a simple prompt or instruction; this process requires experimentation and providing important context for the model to perform the task optimally.

Let’s break down the problem into core components that are key to effective context engineering.

### Instructions [...] In other words, what you are trying to achieve in context engineering is optimizing the information you are providing in the context window of the LLM. This also means filtering out noisy information, which is a science on its own, as it requires systematically measuring the performance of the LLM.

Everyone is writing about context engineering, but here we are going to walk you through a concrete example of what context engineering looks like when building AI agents. [...] This is clever context engineering as it makes your application more dynamic, cheaper, and efficient. You see, context engineering is not just about optimizing your prompt; it’s about choosing the right context for the goals you are targeting. You can also get more creative about how you are maintaining that vector store and how you pull those existing subtasks into context. Creative and novel context engineering is the moat!

### States & Historical Context

[5] A comprehensive survey of prompt engineering and context engineering techniques in large language models - Charles Sturt University Research Output
URL: https://researchoutput.csu.edu.au/en/publications/a-comprehensive-survey-of-prompt-engineering-and-context-engineer
Excerpt: a comprehensive systematic literature review of prompt and context engineering techniques, unifying fragmented paradigms into a cohesive analytical framework. We introduce a structured taxonomy spanning the full prompt lifecycle, categorizing foundational approaches—such as zero-shot and few-shot learning—alongside advanced strategies including Chain-of-Thought (CoT), Retrieval-Augmented Generation (RAG), and multi-step reasoning architectures (e.g., Tree-of-Thoughts, Graph-of-Thoughts). [...] a comprehensive systematic literature review of prompt and context engineering techniques, unifying fragmented paradigms into a cohesive analytical framework. We introduce a structured taxonomy spanning the full prompt lifecycle, categorizing foundational approaches—such as zero-shot and few-shot learning—alongside advanced strategies including Chain-of-Thought (CoT), Retrieval-Augmented Generation (RAG), and multi-step reasoning architectures (e.g., Tree-of-Thoughts, Graph-of-Thoughts). [...] a comprehensive systematic literature review of prompt and context engineering techniques, unifying fragmented paradigms into a cohesive analytical framework. We introduce a structured taxonomy spanning the full prompt lifecycle, categorizing foundational approaches—such as zero-shot and few-shot learning—alongside advanced strategies including Chain-of-Thought (CoT), Retrieval-Augmented Generation (RAG), and multi-step reasoning architectures (e.g., Tree-of-Thoughts, Graph-of-Thoughts).
```
**Tool result** `read_url` (id `call-c23fea85-306f-4df6-a78a-f59824b7a98d`, 10,096 characters):

```
Title: Paul Fruitful – Medium

URL Source: https://medium.com/@fruitful2007

Markdown Content:
[Sitemap](https://medium.com/sitemap/sitemap.xml)

[Open in app](https://play.google.com/store/apps/details?id=com.medium.reader&referrer=utm_source%3DmobileNavBar&source=---two_column_layout_nav--------------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fmedium.com%2F%40fruitful2007&source=user_profile_page---two_column_layout_nav-----------------------global_nav---------------------)

[](https://medium.com/?source=---two_column_layout_nav--------------------------------------------)

From

Paul Fruitful

Get app

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---two_column_layout_nav-----------------------new_post_topnav---------------------)

[Search](https://medium.com/search?writer=fruitful2007&source=---two_column_layout_nav--------------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fmedium.com%2F%40fruitful2007&source=user_profile_page---two_column_layout_nav-----------------------global_nav---------------------)

![Image 1: Unknown user](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[](https://medium.com/@fruitful2007)

![Image 2: Paul Fruitful](https://miro.medium.com/v2/resize:fill:96:96/1*eLpBCQ_I9E1jCEkYs9-eFg.jpeg)

Paul Fruitful

he

[62 followers](https://medium.com/@fruitful2007/followers)

[Home](https://medium.com/@fruitful2007)

[Reposts](https://medium.com/@fruitful2007/reposts)

[Activity](https://medium.com/@fruitful2007/activity)

[Lists](https://medium.com/@fruitful2007/lists)

[About](https://medium.com/@fruitful2007/about)

Pinned

[![Image 3: Paul Fruitful](https://miro.medium.com/v2/resize:fill:40:40/1*eLpBCQ_I9E1jCEkYs9-eFg.jpeg)](https://medium.com/@fruitful2007?source=user_profile_page---------0-------------e36eb24f70b7-------------------------)

[Paul Fruitful](https://medium.com/@fruitful2007?source=user_profile_page---------0-------------e36eb24f70b7-------------------------)

·

Jun 15

## [The AI Wild West Era Is Coming To An End ### Intelligence For Me None For Thee](https://medium.com/@fruitful2007/the-ai-wild-west-era-is-coming-to-an-end-2d5b7cb5b68b?source=user_profile_page---------0-------------e36eb24f70b7-------------------------)

[](https://medium.com/@fruitful2007/the-ai-wild-west-era-is-coming-to-an-end-2d5b7cb5b68b?source=user_profile_page---------0-------------e36eb24f70b7-------------------------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F2d5b7cb5b68b&operation=register&redirect=https%3A%2F%2Fmedium.com%2F%40fruitful2007%2Fthe-ai-wild-west-era-is-coming-to-an-end-2d5b7cb5b68b&source=---------0-------------e36eb24f70b7----bookmark_preview---------------------)

![Image 4: The AI Wild West Era Is Coming To An End](https://miro.medium.com/v2/resize:fill:160:106/1*E2KQzU9DQnXG2jRze-o4lQ.png)

![Image 5: The AI Wild West Era Is Coming To An End](https://miro.medium.com/v2/resize:fill:320:214/1*E2KQzU9DQnXG2jRze-o4lQ.png)

[](https://medium.com/@fruitful2007/the-ai-wild-west-era-is-coming-to-an-end-2d5b7cb5b68b?source=user_profile_page---------0-------------e36eb24f70b7-------------------------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F2d5b7cb5b68b&operation=register&redirect=https%3A%2F%2Fmedium.com%2F%40fruitful2007%2Fthe-ai-wild-west-era-is-coming-to-an-end-2d5b7cb5b68b&source=---------0-------------e36eb24f70b7----bookmark_preview---------------------)

[![Image 6: Paul Fruitful](https://miro.medium.com/v2/resize:fill:40:40/1*eLpBCQ_I9E1jCEkYs9-eFg.jpeg)](https://medium.com/@fruitful2007?source=user_profile_page---------1-------------e36eb24f70b7-------------------------)

[Paul Fruitful](https://medium.com/@fruitful2007?source=user_profile_page---------1-------------e36eb24f70b7-------------------------)

·

Oct 19

## [The End of Closed-Source Software? ### Reverse engineering has always been one of the most technically difficult domains to break into in software engineering and cybersecurity…](https://medium.com/@fruitful2007/the-end-of-closed-source-software-a4852bf1c9d3?source=user_profile_page---------1-------------e36eb24f70b7-------------------------)

[1](https://medium.com/@fruitful2007/the-end-of-closed-source-software-a4852bf1c9d3?source=user_profile_page---------1-------------e36eb24f70b7-------------------------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2Fa4852bf1c9d3&operation=register&redirect=https%3A%2F%2Fmedium.com%2F%40fruitful2007%2Fthe-end-of-closed-source-software-a4852bf1c9d3&source=---------1-------------e36eb24f70b7----bookmark_preview---------------------)

![Image 7: The End of Closed-Source Software?](https://miro.medium.com/v2/resize:fill:160:106/1*QpRDFAm11EjZhYBqdzUpYA.png)

![Image 8: The End of Closed-Source Software?](https://miro.medium.com/v2/resize:fill:320:214/1*QpRDFAm11EjZhYBqdzUpYA.png)

[1](https://medium.com/@fruitful2007/the-end-of-closed-source-software-a4852bf1c9d3?source=user_profile_page---------1-------------e36eb24f70b7-------------------------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2Fa4852bf1c9d3&operation=register&redirect=https%3A%2F%2Fmedium.com%2F%40fruitful2007%2Fthe-end-of-closed-source-software-a4852bf1c9d3&source=---------1-------------e36eb24f70b7----bookmark_preview---------------------)

[![Image 9: Paul Fruitful](https://miro.medium.com/v2/resize:fill:40:40/1*eLpBCQ_I9E1jCEkYs9-eFg.jpeg)](https://medium.com/@fruitful2007?source=user_profile_page---------2-------------e36eb24f70b7-------------------------)

[Paul Fruitful](https://medium.com/@fruitful2007?source=user_profile_page---------2-------------e36eb24f70b7-------------------------)

·

Jul 2

## [AI Sovereignty: Who Controls The Weights? ### For the past couple of weeks, I have been getting increasingly vocal about one of the problems that I think the AI industry should begin…](https://medium.com/@fruitful2007/ai-sovereignty-who-controls-the-weights-b6df79be8235?source=user_profile_page---------2-------------e36eb24f70b7-------------------------)

[](https://medium.com/@fruitful2007/ai-sovereignty-who-controls-the-weights-b6df79be8235?source=user_profile_page---------2-------------e36eb24f70b7-------------------------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2Fb6df79be8235&operation=register&redirect=https%3A%2F%2Fmedium.com%2F%40fruitful2007%2Fai-sovereignty-who-controls-the-weights-b6df79be8235&source=---------2-------------e36eb24f70b7----bookmark_preview---------------------)

![Image 10: AI Sovereignty: Who Controls The Weights?](https://miro.medium.com/v2/resize:fill:160:106/g:fp:0.5:0.76/1*9cCBR8wmq08urbWNXCZLHw.png)

![Image 11: AI Sovereignty: Who Controls The Weights?](https://miro.medium.com/v2/resize:fill:320:214/g:fp:0.5:0.76/1*9cCBR8wmq08urbWNXCZLHw.png)

[](https://medium.com/@fruitful2007/ai-sovereignty-who-controls-the-weights-b6df79be8235?source=user_profile_page---------2-------------e36eb24f70b7-------------------------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2Fb6df79be8235&operation=register&redirect=https%3A%2F%2Fmedium.com%2F%40fruitful2007%2Fai-sovereignty-who-controls-the-weights-b6df79be8235&source=---------2-------------e36eb24f70b7----bookmark_preview---------------------)

[![Image 12: Paul Fruitful](https://miro.medium.com/v2/resize:fill:40:40/1*eLpBCQ_I9E1jCEkYs9-eFg.jpeg)](https://medium.com/@fruitful2007?source=user_profile_page---------3-------------e36eb24f70b7-------------------------)

[Paul Fruitful](https://medium.com/@fruitful2007?source=user_profile_page---------3-------------e36eb24f70b7-------------------------)

·

Feb 4

## [Agentic Engineering: Goodbye To Building Slop Software ### Vibecoding: Fun Until It Isn’t](https://medium.com/@fruitful2007/agentic-engineering-goodbye-to-building-slop-software-55dcd7356813?source=user_profile_page---------3-------------e36eb24f70b7-------------------------)

[](https://medium.com/@fruitful2007/agentic-engineering-goodbye-to-building-slop-software-55dcd7356813?source=user_profile_page---------3-------------e36eb24f70b7-------------------------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F55dcd7356813&operation=register&redirect=https%3A%2F%2Fmedium.com%2F%40fruitful2007%2Fagentic-engineering-goodbye-to-building-slop-software-55dcd7356813&source=---------3-------------e36eb24f70b7----bookmark_preview---------------------)

![Image 13: Agentic Engineering: Goodbye To Building Slop Software](https://miro.medium.com/v2/resize:fill:160:106/1*MGjrRV2jbWFnMLeIKc-YXw.png)

![Image 14: Agentic Engineering: Goodbye To Building Slop Software](https://miro.medium.com/v2/resize:fill:320:214/1*MGjrRV2jbWFnMLeIKc-YXw.png)

[](https://medium.com/@fruitful2007/agentic-engineering-goodbye-to-building-slop-software-55dcd7356813?source=user_profile_page---------3-------------e36eb24f70b7-------------------------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F55dcd7356813&operation=register&redirect=https%3A%2F%2Fmedium.com%2F%40fruitful2007%2Fagentic-engineering-goodbye-to-building-slop-software-55dcd7356813&source=---------3-------------e36eb24f70b7----bookmark_preview---------------------)

[![Image 15: Paul Fruitful](https://miro.medium.com/v2/resize:fill:40:40/1*eLpBCQ_I9E1jCEkYs9-eFg.jpeg)](https://medium.com/@fruitful2007?source=user_profile_page---------4-------------e36eb24f70b7-------------------------)

[Paul Fruitful](https://medium.com/@fruitful2007?source=user_profile_page---------4-------------e36eb24f70b7-------------------------)

·

Jan 19

## [Agent Harness: Understanding Claude C

[Showing characters 0-10,000 of 24,720. Call read_url with start=10000 to read the next part.]
```

## Turn 5

_Model call: 15,473 input tokens, 192 output tokens_

**Tool call** `read_url` (id `call-324e7a92-d729-4cf7-921c-8bdaf4878a1e`):

```json
{
  "url": "https://medium.com/@fruitful2007/about",
  "start": 0
}
```
**Tool call** `web_search` (id `call-3d9bfcaf-b986-41bb-afbb-6daad0c33e22`):

```json
{
  "query": "\"prompt engineering is dead\" context engineering experts disagree still relevant 2025"
}
```
**Tool result** `web_search` (id `call-3d9bfcaf-b986-41bb-afbb-6daad0c33e22`, 8,047 characters):

```
Search results for ""prompt engineering is dead" context engineering experts disagree still relevant 2025" (searched 2026-11-26):

[1] Context engineering: the future of AI | Ghadeer A. posted on the topic | LinkedIn
URL: https://www.linkedin.com/posts/ghadeer-al-ruwaishedi_prompt-engineering-is-dead-context-engineering-activity-7385993284520865793-ZUIv
Excerpt: Prompt engineering is dead. Context engineering is the $500K skill of 2025. Most people still talk about “prompt engineering.” But that’s not how real AI systems think anymore. Prompts die after one interaction. They don’t remember. They don’t reason. You can’t build intelligence on forgetfulness. So we started cramming everything into context docs, chats, rules, and knowledge bases and called it “context-augmented generation.” It worked… until it didn’t. Models got slower. Hallucinations [...] Hallucinations exploded. Accuracy fell off a cliff. The fix isn’t more context. It’s engineered context. That’s what Paul Iusztin calls Context Engineering 2025’s #1 AI skill. It’s not a chatbot. It’s a living system. Here’s how it works 👇: 1️⃣ Short-term memory — your current chat and actions. Fast. Temporary. Like RAM. 2️⃣ Long-term memory — vector or graph databases. Stores knowledge, preferences, experiences. 3️⃣ Semantic retrieval — RAG and APIs pull what matters. Real-time facts, not [...] Brilliantly put! The shift from prompt engineering to context engineering captures exactly where AI development is heading. Building intelligence isn’t about crafting clever prompts anymore; it’s about structuring memory, retrieval, and context flow so models can truly reason and adapt. The analogy of context as the “RAM” of AI systems is spot on. This mindset bridges the gap between LLM tinkering and real cognitive architecture design the skill that will define next-generation AI engineers.

[2] Prompt Engineering Is Dead. Context Engineering Is Dying. What Comes Next Changes Everything.
URL: https://www.youtube.com/watch?v=QWzLPn164w0
Excerpt: perfect prompt blog post. Most of them are terrible. Context engineering followed prompt engineering. It's the one the industry is currently grappling with. Anthropic published a foundational piece in September of 2025 that defined context engineering is the shift from crafting isolated instructions to crafting the entire information state that an AI system operates within. Chains Harrison Chase put it more bluntly in a Sequoia Capital interview when he described it as everything's context [...] developer laptops to access critical systems like customer PII, financial data or healthcare records. But without sanctioned infrastructure, that is exactly what is happening. The model context protocol which Anthropic introduced late in 2024 and donated to the Linux Foundation in December of 2025 is the most promising attempt at standardization at this point. UCP has seen a ton of adoption. OpenAI, Google, Microsoft, and more than 50 enterprise partners have committed to it. It's become the de [...] requiring judgment. By mid 2025, CEO Sebastian Seycowski told Bloomberg that while cost was a predominant evaluation factor, the result was lower quality. End quote. Clarin began frantically rehiring the human agents it had gutted. Most people tell this story as proof that AI can't handle nuance, and that was a comforting reading in early 2025. A more interesting reading in 2026 is that the AI agent was extraordinarily good at resolving tickets fast and that that was the wrong goal to give the

[3] Prompt Engineering Is Dead. Context Engineering Is Next.
URL: https://medium.com/data-science-collective/prompt-engineering-is-dead-context-engineering-is-next-a6c5e1e6012c
Excerpt: Prompt Engineering — Asking the right question. Phrasing your request clearly. Using techniques like chain-of-thought or few-shot examples inside your message.

Context Engineering — Designing what the AI knows before you even ask. What memory it has. What documents it can see. What role it’s playing. What outputs it’s expected to produce.

Prompting is tactical. Context is architectural.

## Why does this matter right now in 2025? [...] > In 2023, everyone learned to prompt. In 2025, the people building real AI systems are doing something different entirely.

## Breaking it down — the five layers of context

Here’s the clearest way I’ve found to explain what context engineering actually includes. Think of it as five rings around the AI.

Layer 1 — The System Prompt: who is the AI? [...] The companies crushing it with AI right now — they’re not using better prompts than everyone else. They’ve built better contexts. They’ve built systems where the AI walks in every morning with a perfect briefing, a crystal-clear mandate, and exactly the right information to do its job.

That’s the real game. And most people haven’t started playing it yet.

> Prompt Engineering will get you good outputs occasionally. Context Engineering will get you great outputs consistently.

[4] Prompt Engineering Is Dead, and Context Engineering Is Already Obsolete: Why the Future Is Automated Workflow Architecture with LLMs - Prompting - OpenAI Developer Community
URL: https://community.openai.com/t/prompt-engineering-is-dead-and-context-engineering-is-already-obsolete-why-the-future-is-automated-workflow-architecture-with-llms/1314011
Excerpt: Context engineering helped, but it created new challenges:

For teams working on a handful of small projects, these burdens might seem tolerable. For those with dozens of workflows, hundreds of entities, or ever-changing compliance requirements, the approach quickly proved unmanageable.

Why Context Engineering Is Already Outdated for Serious Practitioners [...] The landscape of LLM engineering is shifting under our feet. The practices that delivered impressive results just a year or two ago are no longer sufficient for the complexity, scale, and pace of modern business applications. Prompt engineering is a relic. Context engineering, for many, is already showing its limits. [...] No engineer writes or updates context by hand. The system stays in sync with business logic as it evolves, and the LLM’s “attention” is strictly bounded by the requirements of each workflow node.

The New Skillset: Workflow Architecture and Code-Driven Context

If prompt and context engineering are becoming obsolete, what replaces them? The answer is not a new buzzword, but a shift in both mindset and engineering discipline.

Successful LLM systems are increasingly built by architects who:

[5] Prompt engineering is dead. Long live context engineering!
URL: https://martech.org/prompt-engineering-is-dead-long-live-context-engineering
Excerpt: You don’t get that with a better prompt. You get that with expert-trained AI.

This requires a change in posture: from experimentation to ownership.

The early phase of GenAI was about tool sprawl and tactical wins. Freelancers used free tools, agencies cobbled together assets and teams pasted prompts into interfaces and called it innovation.

It worked—until it didn’t.

Expert-trained models are not models trained on more data. They’re models trained on the correct data. [...] That’s why the next era of AI doesn’t start with a better prompt. It starts with better design.

Context is the new code.

## Context is king

AI systems that drive outcomes don’t rely on tricks. They rely on knowledge—specifically, your knowledge, structured and made accessible at scale. The shift we’re living through now is not from analog to digital, or manual to automated. It’s from prompting outputs to engineering context for your AI. [...] To get there, organizations must build retrieval layers that pull relevant, governed knowledge. They must use systems that embed product data, sales logic and persona nuance. They must train models on proprietary corpora—not just web-scale content. And they must measure success not in speed but in signal: more resonance, less noise.

This isn’t a rejection of language models. It’s a rejection of generic deployment.
```
**Tool result** `read_url` (id `call-324e7a92-d729-4cf7-921c-8bdaf4878a1e`, 5,315 characters):

```
Title: About – Paul Fruitful – Medium

URL Source: https://medium.com/@fruitful2007/about

Markdown Content:
[Sitemap](https://medium.com/sitemap/sitemap.xml)

[Open in app](https://play.google.com/store/apps/details?id=com.medium.reader&referrer=utm_source%3DmobileNavBar&source=---two_column_layout_nav--------------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fmedium.com%2F%40fruitful2007%2Fabout&source=login---two_column_layout_nav-----------------------global_nav---------------------)

[](https://medium.com/?source=---two_column_layout_nav--------------------------------------------)

From

Paul Fruitful

Get app

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---two_column_layout_nav-----------------------new_post_topnav---------------------)

[Search](https://medium.com/search?writer=fruitful2007&source=---two_column_layout_nav--------------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fmedium.com%2F%40fruitful2007%2Fabout&source=login---two_column_layout_nav-----------------------global_nav---------------------)

![Image 1: Unknown user](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[](https://medium.com/@fruitful2007)

![Image 2: Paul Fruitful](https://miro.medium.com/v2/resize:fill:96:96/1*eLpBCQ_I9E1jCEkYs9-eFg.jpeg)

Paul Fruitful

he

[62 followers](https://medium.com/@fruitful2007/followers)

Follow

[Home](https://medium.com/@fruitful2007)

[Reposts](https://medium.com/@fruitful2007/reposts)

[Activity](https://medium.com/@fruitful2007/activity)

[Lists](https://medium.com/@fruitful2007/lists)

[About](https://medium.com/@fruitful2007/about)

#### [62 followers](https://medium.com/@fruitful2007/followers?source=user_about----------------------e36eb24f70b7-------------------------)
·

[10 following](https://medium.com/@fruitful2007/following?source=user_about----------------------e36eb24f70b7-------------------------)

Connect with Paul Fruitful

[](https://twitter.com/Paulfruitful_?source=user_about----------------------e36eb24f70b7-------------------------)

![Image 3: Paul Fruitful](https://miro.medium.com/v2/resize:fill:176:176/1*eLpBCQ_I9E1jCEkYs9-eFg.jpeg)

## Paul Fruitful he

[62 followers](https://medium.com/@fruitful2007/followers?source=user_about---user_sidebar-------------------e36eb24f70b7-------------------------)

I’m Paul Fruitful, a versatile result-oriented Software Engineer & tech content creator with close to a decade of experience, passionate about the future

Follow

Following
*   [![Image 4: Ignacio de Gregorio](https://miro.medium.com/v2/resize:fill:40:40/1*OwdwA_GEONFZdA6lfBqeOQ.png) Ignacio de Gregorio](https://medium.com/@ignacio.de.gregorio.noblejas?source=user_about---blogroll-------------------e36eb24f70b7-------------------------)  
*   [![Image 5: Mehmet Ozkaya](https://miro.medium.com/v2/resize:fill:40:40/1*pgjuS7q21HmvfnpB9LMxVw.png) Mehmet Ozkaya](https://medium.com/@mehmetozkaya?source=user_about---blogroll-------------------e36eb24f70b7-------------------------)  
*   [![Image 6: Opemipo Disu](https://miro.medium.com/v2/resize:fill:40:40/1*yQ-OF6lxTNXLC0mmsTt6xg.jpeg) Opemipo Disu](https://medium.com/@coderoflagos?source=user_about---blogroll-------------------e36eb24f70b7-------------------------)  
*   [![Image 7: Laravel News](https://miro.medium.com/v2/resize:fill:40:40/1*sCMUOOOIXPFZrtkYU8bVtQ.png) Laravel News](https://medium.com/@laravelnews?source=user_about---blogroll-------------------e36eb24f70b7-------------------------)  

[See all (10)](https://medium.com/@fruitful2007/following?source=user_about---blogroll-------------------e36eb24f70b7-------------------------)

[Help](https://help.medium.com/hc/en-us?source=user_about---user_sidebar-------------------e36eb24f70b7-------------------------)

[Status](https://status.medium.com/?source=user_about---user_sidebar-------------------e36eb24f70b7-------------------------)

[About](https://medium.com/about?autoplay=1&source=user_about---user_sidebar-------------------e36eb24f70b7-------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=user_about---user_sidebar-------------------e36eb24f70b7-------------------------)

[Press](https://medium.com/@MediumStaff/medium-press-kit-ebf013f55256?source=user_about---user_sidebar-------------------e36eb24f70b7-------------------------)

[Blog](https://blog.medium.com/?source=user_about---user_sidebar-------------------e36eb24f70b7-------------------------)

[Store](https://medium.com/store)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=user_about---user_sidebar-------------------e36eb24f70b7-------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=user_about---user_sidebar-------------------e36eb24f70b7-------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=user_about---user_sidebar-------------------e36eb24f70b7-------------------------)

[Text to speech](https://speechify.com/medium?source=user_about---user_sidebar-------------------e36eb24f70b7-------------------------)

```

## Turn 6

_Model call: 18,970 input tokens, 476 output tokens_

**Tool call** `web_search` (id `call-3ca87670-0ca2-449d-9142-83b10c937e6f`):

```json
{
  "query": "\"Paul Fruitful\" software engineer LinkedIn \"close to a decade\""
}
```
**Tool call** `web_search` (id `call-7f7d966f-a4b4-4d7a-ae17-533a69243d6e`):

```json
{
  "query": "\"PROMPT ENGINEERING IS DEAD INTRODUCING CONTEXT ENGINEERING\" Fruitful medium"
}
```
**Tool result** `web_search` (id `call-7f7d966f-a4b4-4d7a-ae17-533a69243d6e`, 6,268 characters):

```
Search results for ""PROMPT ENGINEERING IS DEAD INTRODUCING CONTEXT ENGINEERING" Fruitful medium" (searched 2026-11-26):

[1] PROMPT ENGINEERING IS DEAD INTRODUCING CONTEXT ENGINEERING
URL: https://medium.com/@fruitful2007/prompt-engineering-is-dead-introducing-context-engineering-6280c075a1a9
Excerpt: Prompt engineering was all about crafting the perfect prompts to get outputs and information out of LLMs.  
Context engineering seems different.  
Context engineering is like a superset of prompt engineering.  
This is what context engineering is, as Andrej Karpathy defines it:

> "It’s the art of filling in the context window with the right information so that the LLM knows what’s next."

You see that? It’s about crafting worlds/environments inside the mind of agents (the context window ) [...] So, prompt engineering was about creating a single prompt or creating a prompt flow to get the best information/output out of an LLM.

But context engineering is about shaping the entire context window to fit your needs.  
Utilizing the whole context window to extract efficiency from large language models.  
That’s what context engineering is all about. [...] In context engineering, your prompts don’t come out ad hoc. They come out of your context, your environment.  
Context engineering is all about creating worlds inside LLMs for specific tasks.  
That’s what context engineering is all about, being able to create a world, an environment, a system that has everything the model needs to function in a specified task.

[2] Context Engineering Guide | Prompt Engineering Guide<!-- -->
URL: https://www.promptingguide.ai/guides/context-engineering-guide
Excerpt: A few years ago, many, even top AI researchers, claimed that prompt engineering would be dead by now.

Obviously, they were very wrong, and in fact, prompt engineering is now even more important than ever. It is so important that it is now being rebranded as context engineering.

Yes, another fancy term to describe the important process of tuning the instructions and relevant context that an LLM needs to perform its tasks effectively.

[3] Context Engineering vs Prompt Engineering | DataHub
URL: https://datahub.com/blog/context-engineering-vs-prompt-engineering
Excerpt: No. Prompt engineering remains valuable and is still an essential component of working with LLMs effectively. The shift is one of scope, not replacement. Prompt engineering focuses on how you communicate with a model within a given interaction. Context engineering focuses on the system level, managing the full informational environment the model works within. As AI systems grow more complex, prompt engineering becomes one input into a much larger context engineering workflow rather than the [...] Most organizations understand this conceptually. Fewer understand what it actually requires. According to our 2026 State of Context Management Report, 82% of IT and data leaders agree that prompt engineering alone is no longer sufficient to power AI at scale. The shift is real, and the investment is following: 95% of data teams plan to invest in context engineering training during 2026. [...] 82% of IT and data leaders say prompt engineering alone is no longer sufficient, and 95% say context engineering is important to power AI agents at scale (DataHub’s State of Context Management Report 2026).

The gap most teams miss: Context engineering is only as good as the context it has access to. Without a context management layer that delivers trusted, governed, up-to-date metadata, context engineering is engineering with unreliable inputs.

[4] Prompt Engineering Is Dead, and Context Engineering Is Already Obsolete: Why the Future Is Automated Workflow Architecture with LLMs - Prompting - OpenAI Developer Community
URL: https://community.openai.com/t/prompt-engineering-is-dead-and-context-engineering-is-already-obsolete-why-the-future-is-automated-workflow-architecture-with-llms/1314011
Excerpt: The landscape of LLM engineering is shifting under our feet. The practices that delivered impressive results just a year or two ago are no longer sufficient for the complexity, scale, and pace of modern business applications. Prompt engineering is a relic. Context engineering, for many, is already showing its limits. [...] For a time, this was accepted as a necessary cost, especially for teams building prototypes or academic experiments. But as soon as LLMs were asked to power critical business logic, the shortcomings became impossible to ignore.

The Context Engineering Revolution—And Its Limits [...] The problem is not only “what is being said,” but also what meaning the system assigns to it before and after generation — something the human amygdala does constantly, shaping perception, urgency, and memory. Without that modulatory layer of “importance,” the filter risks becoming another deterministic gate rather than an interpreter of emotional and epistemic integrity.

[5] Vishal Rajput on Facebook: "> **Prompt Engineering** is Dead, it's time for **Context Engineering**. Do you remember a year or s…"
URL: https://www.facebook.com/groups/DeepNetGroup/posts/2616188292107370
Excerpt: Table Of Contents
 Context Is Everything, Not Prompting
 Natural Language → Tool Calls
 Own Your Prompts
 Own Your Context Window
 Tools Are Structured Outputs
 Unify Execution State and Business State
 Launch, Pause, Resume: Lifecycle Management via Simple APIs
 Own Your Control Flow
 Compact Errors into Context Window
 Next Gen Agents: Modular, Accessible & Stateless Agents [...] But now things have changed and have taken the approach of traditional software engineering with the power of LLMs. So, let's look at the ultimate guide on how to build real agentic workflows that actually scale and don’t break in production. [...] # Vishal Rajput on Facebook: "> Prompt Engineering is Dead, it's time for Context Engineering. Do you remember a year or s…"

> 

Prompt Engineering is Dead, it's time for Context Engineering.

Do you remember a year or so ago, when companies were offering up to 300K USD for prompt engineering? We don’t see these posts or the company anymore. Prompt engineering was kind of hacky from the start. It was the fancy way to make everyone believe that they were engineers.
```
**Tool result** `web_search` (id `call-3ca87670-0ca2-449d-9142-83b10c937e6f`, 6,048 characters):

```
Search results for ""Paul Fruitful" software engineer LinkedIn "close to a decade"" (searched 2026-11-26):

[1] Paul Fruitful - AI Evangelist-Engineer || Making Efficient Agentic Workflows ...
URL: https://ng.linkedin.com/in/paulfruitful
Excerpt: Headline: AI Evangelist-Engineer || Making Efficient Agentic Workflows With Almost Zero Running Cost|| 18 Y.O
Current role: Builder
Seniority: Specialist, Trades
Location: Lagos State, Nigeria
Experience: 6 years 2 months
LinkedIn:  · 3,249 followers [...] Description: I’m Paul Fruitful, a versatile and results-driven Software Engineer with a passion for full-stack development, cybersecurity, AI, and technical leadership. With more than half of my lifetime dedicated to software engineering, I’ve gained extensive experience across various industries. My roles have spanned backend and frontend development, digital forensics, and AI engineering. Over the years, I’ve contributed to open-source projects, developed AI-powered tools like Roadmapr and [...] ## Experience
- Builder at Odibua (Jun 2026 to present)
- Senior Software Engineer at Roadmapr (Aug 2024 to present)
- Coding Instructor at Vision Incubation Hub (Apr 2023 to present)
- Software Engineer at Whiz Navigators (Jun 2020 to present)
- Back End Developer at Syticks (Mar 2024 to Jan 2025)
- Software Engineering Fellow at Headstarter AI (Jul 2024 to Sep 2024)

[2] How AI is changing the software industry | Paul Fruitful posted on the topic | LinkedIn
URL: https://www.linkedin.com/posts/paulfruitful_the-rise-of-personal-software-ps-just-activity-7315631112217624577-VLLY
Excerpt: 💻 I’ve officially opened up space for freelance web development and AI integration work. Over the last few years, I’ve focused heavily on combining modern web technology with practical AI solutions — helping brands turn static websites into smart, automated systems that actually convert. We’re past the point where AI is optional. Businesses that integrate it now are already seeing: Higher lead-to-client conversion rates Faster response times More efficient operations And measurable [...] And measurable improvements in customer engagement Most of my recent work focuses on helping small to mid-sized teams: ✅ Build high-performance websites using Next.js, React, and Tailwind ✅ Integrate AI assistants that handle inbound questions, capture leads, and sync directly into CRMs ✅ Automate manual workflows while maintaining security and compliance Whether it’s a website refresh, AI-powered lead funnel, or a complete digital transformation strategy, I’m interested in collaborating with [...] isn’t coming — it’s already here. The teams that move early will define the next decade. 🚀

[3] Free OpenAI Inference on Local Machine | Paul Fruitful posted on the topic | LinkedIn
URL: https://www.linkedin.com/posts/paulfruitful_yesterday-i-developed-an-open-source-product-activity-7474057480839389184-JbLp
Excerpt: + No alternative text description for this image

    4   2 Comments

  Like   Comment

  To view or add a comment, sign in

3,248 followers

 660 Posts
 37 Articles

View Profile   Connect

## More from this author

 

  ### AI Sovereignty: Who Controls The Weights?

  Paul Fruitful   3mo
 

  ### The AI Wild West Era Is Coming To An End

  Paul Fruitful   4mo
 

  ### Agentic Engineering: Goodbye To Building Slop Software

  Paul Fruitful   8mo

## Explore related topics [...] Yesterday, I developed an open source product that will revolutionize AI inference by saving millions of dollars worth of tokens without being rate-limited and it runs 100% on your local machine without consuming your GPU or CPU. I developed a product that will allow for completely free AI inference from OpenAI on your local machine and using absolutely no model provider, their API or any local model, just your browser and voila, you get free inference of OpenAI models, with others following [...] researchers behind SWEBench, but this benchmark tests something much closer to real software engineering. Instead of asking models to patch existing repositories or solve isolated GitHub issues, it tasks them with building complete software systems from scratch The models were asked to create things like: - FFMPEG - SQLite - PHP interpreters - CLI tools None of the models were able to successfully complete the tasks, this exposed one of the biggest limitations of current LLMs. They are good at

[4] https://www.linkedin.com/in/adam-laughlin-31363920a
URL: https://www.linkedin.com/in/adam-laughlin-31363920a
Excerpt: # Adam Laughlin

Headline: Founding Engineer @ Fruitful
Current role: Engineer
Seniority: Specialist, Engineering and Technical
Location: Greenwich, New Jersey, United States
Experience: 11 years 6 months
LinkedIn:  · 106 followers

## Experience
- Engineer at Fruitful (Feb 2023 to present)
- Lead Software Engineer at Storyblocks (Jan 2016 to Feb 2023)
- Software Engineer at Dash (Oct 2014 to Dec 2015)

[5] Senior Software Engineer at LinkedIn | Indeed.com
URL: https://www.indeed.com/cmp/Linkedin/job-titles/Senior-Software-Engineer
Excerpt: # Senior Software Engineer at LinkedIn

## Reviews

### Senior Software Engineer in Sunnyvale, CA

on November 14, 2023

### Senior Software Engineer in Sunnyvale, CA

on September 13, 2023

### Sr. Software Engineer, Datawarehouse Solutions in Carpinteria, CA

on September 30, 2017

## What would you say about your employer?

Help fellow job seekers by sharing your unique experience.

## Salaries

Salary estimated from 58 past and present job postings on Indeed.

Last updated: November 15, 2026 [...] Average salary

$194,923

- Select pay period
- per yearMost common pay period for Senior Software Engineer at this company
- per monthConverted from most common pay period
- per weekConverted from most common pay period
- per dayConverted from most common pay period
- per hourConverted from most common pay period

## Jobs

We were not able to detect your location. You can browse through all 16 jobs LinkedIn has to offer

slide1 of 1

There are 16 jobs at LinkedIn
```

## Turn 7

_Model call: 22,180 input tokens, 693 output tokens_

**Tool call** `web_search` (id `call-9d0ef4ad-fddd-4672-89ab-8046b6c93a3a`):

```json
{
  "query": "\"context engineering\" paper \"context assembler\" optimizer function mathematical formulation LLM"
}
```
**Tool call** `read_url` (id `call-7a91d212-13e5-4299-a1b4-6a1478574e12`):

```json
{
  "url": "https://medium.com/about",
  "start": 0
}
```
**Tool result** `web_search` (id `call-9d0ef4ad-fddd-4672-89ab-8046b6c93a3a`, 7,146 characters):

```
Search results for ""context engineering" paper "context assembler" optimizer function mathematical formulation LLM" (searched 2026-11-26):

[1] Context-Engineering/00_COURSE/00_mathematical_foundations/01_context_formalization.md at main · jasontang-ai/Context-Engineering · GitHub
URL: https://github.com/davidkimai/context-engineering/blob/main/00_COURSE/00_mathematical_foundations/01_context_formalization.md
Excerpt: Context Game Theory: Extension of game-theoretic frameworks to multi-agent context assembly scenarios where different agents contribute components and assembly strategies, requiring mathematical frameworks for negotiating optimal collective context formalization strategies.

Mathematical Formalization:

- Context assembly function: `C = A(c₁, c₂, c₃, c₄, c₅, c₆)`
- Component analysis and quality metrics
- Multi-objective optimization framework

Three Paradigm Integration: [...] Information-Theoretic Context Bounds: Research into fundamental limits of context compression and assembly efficiency, establishing mathematical bounds on how much information can be effectively integrated within token constraints while maintaining quality.

Context Assembly Convergence: Investigation of mathematical conditions under which iterative context optimization approaches converge to optimal solutions, and development of convergence guarantees for adaptive assembly algorithms. [...] Next Module: 02\_optimization\_theory.md - Where we'll learn to systematically find the optimal assembly functions and component configurations using mathematical optimization techniques.

- Component templates for each context type (c₁-c₆)
- Assembly strategy templates (linear, weighted, hierarchical)
- Quality standard definitions and validation templates
- Domain-specific template libraries

<!--THE END-->

[2] Beyond LLM Wrappers: Context Engineering and the Three-Engine Architecture for Reliable Financial AI
URL: https://arxiv.org/html/2610.39230v1
Excerpt: This paper presented a three-engine architecture for reliable financial AI. A financial knowledge graph provides persistent context, relationship reasoning, provenance, and temporal state. A deterministic optimization engine computes constrained decisions such as payment schedules and cash allocation. A multi-agent LLM layer interprets queries, assembles tasks, explains outputs, and validates generated claims against structured ground truth. The engines are coordinated through context [...] Mathematical optimization has a long history in finance and operations research. Portfolio optimization, cash-flow planning, payment scheduling, credit allocation, and supply-chain finance all use deterministic optimization methods \[Markowitz, 1952; Konno & Yamazaki, 1991; Baccarin, 2009; Wuttke et al., 2016]. This paper does not propose a new solver or optimization algorithm. Instead, it shows how optimization can function as one engine in an AI system. LLMs formulate and explain; solvers [...] and a context window budget, the context engineering layer produces a context package and execution plan that maximize decision-relevant information subject to accuracy, completeness, recency, access-control, and budget constraints. This characterization captures the multi-dimensional nature of the problem. A rigorous optimization formulation would require defining relevance functions and feasibility constraints that vary by tenant, query type, and data state—an open research problem we discuss

[3] Medium
URL: https://medium.com/@adnanmasood/a-practitioners-take-on-a-survey-of-context-engineering-for-large-language-models-49ac87d23a1e
Excerpt: > TL;DR — The authors formalize Context Engineering — the discipline of designing, optimizing, and orchestrating what goes into an LLM’s context — and present a unified taxonomy from core components (retrieval/generation, processing, management) to full systems (RAG, memory, tool‑use, multi‑agent). They synthesize 1,400+ papers, highlight a critical “comprehension → generation” gap, and show today’s evaluations expose large performance shortfalls (e.g., GAIA 15% for AI vs 92% human), calling [...] Member-only story

# A Practitioner’s Take on ‘A Survey of Context Engineering for Large Language Models’

## Context Engineering as the new performance lever. A practitioner’s tour of a 1,400‑paper synthesis that formalizes how we retrieve, process, and manage information for LLMs — spanning a unified taxonomy (retrieval/generation, processing, management) through full systems (RAG, memory, tool‑use, multi‑agent) — and why the real bottleneck isn’t model size but the context pipeline.

[4] Context Engineering: Bringing Engineering Discipline to Prompts
URL: https://addyo.substack.com/p/context-engineering-bringing-engineering
Excerpt: The impact of these techniques is huge. When you see an impressive LLM demo solving a complex task (say, debugging code or planning a multi-step process), you can bet it wasn’t just a single clever prompt behind the scenes. There was a pipeline of context assembly enabling it.

For instance, an AI pair programmer might implement a workflow like: [...] A useful mental model (suggested by Andrej Karpathy and others) is to think of an LLM like a CPU, and its context window (the text input it sees at once) as the RAM or working memory. As an engineer, your job is akin to an operating system: load that working memory with just the right code and data for the task. In practice, this context can come from many sources: the user’s query, system instructions, retrieved knowledge from databases or documentation, outputs from other tools, and summaries [...] In other words, real-world LLM apps don’t succeed by luck or one-shot prompts – they succeed by carefully assembling context around the model’s queries.

[5] Context Engineering
URL: https://www.langchain.com/blog/context-engineering-for-agents
Excerpt: As Andrej Karpathy puts it, LLMs are like a new kind of operating system. The LLM is like the CPU and its context window is like the RAM, serving as the model’s working memory. Just like RAM, the LLM context window has limited capacity to handle various sources of context. And just as an operating system curates what fits into a CPU’s RAM, we can think about “context engineering” playing a similar role. Karpathy summarizes this well: [...] Context Trimming

Whereas summarization typically uses an LLM to distill the most relevant pieces of context, trimming can often filter or, as Drew Breunig points out, “prune” context. This can use hard-coded heuristics like removing older messages from a list. Drew also mentions Provence, a trained context pruner for Question-Answering.

## Isolating Context

Isolating context involves splitting it up to help an agent perform a task.

Multi-agent [...] > [Context engineering is the] ”…delicate art and science of filling the context window with just the right information for the next step.”

Context types commonly used in LLM applications

What are the types of context that we need to manage when building LLM applications? Context engineering as an umbrella that applies across a few different context types:
```
**Tool result** `read_url` (id `call-7a91d212-13e5-4299-a1b4-6a1478574e12`, 2,119 characters):

```
Title: About Medium

URL Source: https://medium.com/about

Markdown Content:
## Everyone has a story to tell

Medium is a home for human stories and ideas. Here, anyone can share knowledge and wisdom with the world—without having to build a mailing list or a following first. The internet is noisy and chaotic; Medium is quiet yet full of insight. It’s simple, beautiful, collaborative, and helps you find the right readers for whatever you have to say.

> Ultimately, our goal is to deepen our collective understanding of the world through the power of writing.

We believe that what you read and write matters. Words can divide or empower us, inspire or discourage us. In a world where the most sensational and surface-level stories often win, we’re building a system that rewards depth, nuance, and time well spent. A space for thoughtful conversation more than drive-by takes, and substance over packaging.

Over 100 million people connect and share their wisdom on Medium every month. They’re software developers, amateur novelists, product designers, CEOs, and anyone burning with a story they need to get out into the world. They write about what they’re working on, what’s keeping them up at night, what they’ve lived through, and what they’ve learned that the rest of us might want to know too.

Instead of selling ads or selling your data, we’re supported by a growing community of over a million[Medium members](https://medium.com/membership)who believe in our mission. If you’re new here,[start reading](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2F&source=--------------------------landing_about---------------------). Dive deeper into whatever matters to you. Find a post that helps you learn something new, or reconsider something familiar—and then[write your story](https://medium.com/new-story).

[Start reading→](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2F&source=--------------------------landing_about---------------------)

[Start writing→](https://medium.com/new-story)[Become a member→](https://medium.com/membership)

```

## Turn 8

_Model call: 24,842 input tokens, 3,198 output tokens_

**Tool call** `assess_credibility` (id `call-509e8da6-49cb-4c93-9edd-65297743d261`):

```json
{
  "evaluation": {
    "source_url": "https://medium.com/@fruitful2007/prompt-engineering-is-dead-introducing-context-engineering-6280c075a1a9",
    "source_type": "personal_blog",
    "author": {
      "name": "Paul Fruitful (Medium handle @fruitful2007)",
      "credentials": "Medium About page bio: \"I'm Paul Fruitful, a versatile result-oriented Software Engineer & tech content creator with close to a decade of experience, passionate about the future\" (no employer, degree, publication record or topic-specific credentials). Medium profile shows 62 followers and posts mainly opinion pieces on AI (e.g. 'The AI Wild West Era Is Coming To An End', 'AI Sovereignty: Who Controls The Weights?'). A LinkedIn profile at ng.linkedin.com/in/paulfruitful headlines 'AI Evangelist-Engineer || Making Efficient Agentic Workflows With Almost Zero Running Cost || 18 Y.O', location Lagos State, Nigeria, ~6 years 2 months listed experience (Roadmapr, Vision Incubation Hub, Whiz Navigators, Syticks, Headstarter AI fellowship) and ~3,249 followers. I found no research publications, no academic affiliation and no evidence of recognised expertise in LLM systems. The LinkedIn '18 Y.O' / '6 years 2 months' claims also sit awkwardly with the Medium bio's 'close to a decade of experience'.",
      "credibility_assessment": "The author is identifiable but has no verifiable expertise in LLM engineering or research: a self-described software engineer/content creator with a thin, partly inconsistent public bio and a small following. Nothing in his background supports treating his definitions or generalisations about the field as authoritative, and he cites no sources of his own. His practical experience with AI agents is relevant context but not a substitute for sourcing."
    },
    "publication": {
      "name": "Medium (personal profile of @fruitful2007)",
      "reputation": "Medium is a large open blogging platform (Medium's About page: 'anyone can share knowledge and wisdom with the world'; funded by reader memberships rather than ads). Posts on personal profiles are self-published: there is no fact-checking, editor, peer review or correction process. This article is not part of a Medium editorial publication, so it carries only the platform's baseline content rules. The author's account has ~62 followers, so there is no editorial brand behind the piece.",
      "editorial_process": "self_published"
    },
    "content_analysis": {
      "claims_checked": [
        {
          "claim": "Prompt engineering is dead and is being replaced by context engineering.",
          "status": "contradicted",
          "evidence": "The Prompt Engineering Guide's Context Engineering Guide states that predictions of prompt engineering's death were 'very wrong' and that prompt engineering is 'now even more important than ever' (https://www.promptingguide.ai/guides/context-engineering-guide). DataHub's comparison answers 'No. Prompt engineering remains valuable... The shift is one of scope, not replacement' (https://datahub.com/blog/context-engineering-vs-prompt-engineering). Karpathy himself framed context engineering as a better name for the craft, not the death of prompting (https://pureai.com/articles/2025/09/23/karpathy-puts-context-at-the-core-of-ai-coding.aspx). The article's own body later concedes prompt engineering is 'a part of context engineering', so the headline overstates its case."
        },
        {
          "claim": "Andrej Karpathy defines context engineering as \"the art of filling in the context window with the right information so that the LLM knows what's next.\"",
          "status": "contradicted",
          "evidence": "Karpathy's actual June 2025 wording, as reported by multiple independent outlets, is: 'the delicate art and science of filling the context window with just the right information for the next step' (https://pureai.com/articles/2025/09/23/karpathy-puts-context-at-the-core-of-ai-coding.aspx, https://www.langchain.com/blog/context-engineering-for-agents, https://ai4ra.uidaho.edu/from-prompt-engineering-to-context-engineering). The article presents a loose paraphrase in quotation marks, gives no link to the original post, and then repeats a second, slightly different version of the 'quote' later in the same piece."
        },
        {
          "claim": "Context engineering is a superset of prompt engineering, i.e. prompt engineering is one component of it.",
          "status": "corroborated",
          "evidence": "LangChain's agent context-engineering post treats context engineering as the umbrella covering instructions, knowledge, tools, memory and state (https://www.langchain.com/blog/context-engineering-for-agents); Phil Schmid describes prompt engineering as a narrower single-string practice versus the broader discipline (https://www.philschmid.de/context-engineering); deepset and Elastic make the same scope distinction (https://www.deepset.ai/blog/context-engineering-the-next-frontier-beyond-prompt-engineering, https://www.elastic.co/search-labs/blog/context-engineering-vs-prompt-engineering)."
        },
        {
          "claim": "Because the context window is a hard constraint, agents need persistent memory and retrieval (vector databases / 'context banks') that supply only the context a task needs.",
          "status": "corroborated",
          "evidence": "LangChain's write/select/compress/isolate strategies describe exactly this: storing memory outside the window and retrieving only relevant context (https://www.langchain.com/blog/context-engineering-for-agents); Elasticsearch Labs discusses context-window management failure modes (https://www.elastic.co/search-labs/blog/context-engineering-vs-prompt-engineering); the Prompt Engineering Guide makes the same point about filtering noise (https://www.promptingguide.ai/guides/context-engineering-guide)."
        },
        {
          "claim": "Context engineering has 'mathematical foundations', including an 'assembler function' and 'optimizer functions' for finding the best context.",
          "status": "no_evidence_found",
          "evidence": "The article cites no paper or source for this. A search for 'context engineering' plus 'context assembler'/'optimizer function' returned only community material such as a GitHub course repo using a 'context assembly function' notation (https://github.com/davidkimai/context-engineering/blob/main/00_COURSE/00_mathematical_foundations/01_context_formalization.md) and an arXiv paper on a financial-AI architecture that calls a rigorous optimisation formulation an 'open research problem' (https://arxiv.org/html/2610.39230v1). No authoritative source found establishing these formalisms as the article implies."
        }
      ],
      "claims_supported_by_evidence": false,
      "sources_cited": false,
      "corroborated_by_other_sources": true,
      "contradicted_by_other_sources": true,
      "primary_vs_secondary": "tertiary_source",
      "funding_or_sponsorship": "No funding, sponsor or advertiser disclosed. Medium itself is funded by reader memberships rather than ads (https://medium.com/about). The article does contain a self-promotional pitch: the author says he is building a 'context bank' product, will 'release it in a few weeks' and that 'it'll be open source too. So stay tuned for that', which gives him an interest in driving attention to his own project.",
      "bias_and_tone": "Opinionated and informal: the author frames the piece as 'THE NEW HYPE' and 'My honest take', uses emojis and jokes ('overperform your disappointment 😂'), and repeatedly asserts that context engineering 'is just a fancy word' while also promoting his own forthcoming tool. The headline is clickbait ('PROMPT ENGINEERING IS DEAD') and is stronger than the body, which concedes prompt engineering is a subset of context engineering. There are no citations, no data, no links to the research papers he says he was reading, no counterarguments or limitations, and no explanation of method. It is primarily a personal opinion/explainer with a promotional hook rather than reporting or analysis grounded in evidence.",
      "date_published": "Published 21 July 2025 (page metadata: 2025-07-21T00:17:53Z; byline 'Jul 21, 2025'). No last-updated date shown. As of 26 November 2026 the piece is roughly 16 months old; the concept is still current, but the field moves quickly and the article describes no specific models, benchmarks or 2026 developments, so it is dated as a technical reference."
    },
    "transparency_score": 2,
    "overall_credibility": "low",
    "reasoning": "The author is named and identifiable, which is a plus, but he is a self-described software engineer/content creator with no verifiable expertise in LLM research, a thin and partly inconsistent public bio (Medium: 'close to a decade of experience'; LinkedIn: '18 Y.O', ~6 years listed), and a small following. The post is self-published on a personal Medium profile, so there is no editor, peer review or correction mechanism. It cites no sources at all despite referring to research papers, and the one attributed authority — Andrej Karpathy — is misquoted (his actual phrasing is 'the delicate art and science of filling the context window with just the right information for the next step'), with no link to the original. The headline claim ('prompt engineering is dead') is contradicted by credible sources that describe a shift in scope rather than a replacement, and the body itself concedes the point. On the positive side, the core conceptual claims (context engineering as an umbrella over prompt engineering; context-window limits requiring persistent memory/retrieval) are corroborated by LangChain, Phil Schmid, deepset, Elastic and the Prompt Engineering Guide, so the article is not substantively wrong on its main ideas. Because the ideas are right but the sourcing, expertise, editorial oversight and accuracy of quotation are weak, plus a self-promotional agenda, the source is Low credibility for an academic report — usable only as an example of practitioner commentary, not as evidence for facts.",
    "evidence_urls": [
      "https://medium.com/@fruitful2007/prompt-engineering-is-dead-introducing-context-engineering-6280c075a1a9",
      "https://medium.com/@fruitful2007",
      "https://medium.com/@fruitful2007/about",
      "https://medium.com/about",
      "https://ng.linkedin.com/in/paulfruitful",
      "https://www.linkedin.com/posts/paulfruitful_insurance-for-ai-agents-now-this-is-one-activity-7457399028985597952-_EQs",
      "https://pureai.com/articles/2025/09/23/karpathy-puts-context-at-the-core-of-ai-coding.aspx",
      "https://www.langchain.com/blog/context-engineering-for-agents",
      "https://www.honeyhive.ai/learn/context-engineering-vs-prompt-engineering",
      "https://ai4ra.uidaho.edu/from-prompt-engineering-to-context-engineering",
      "https://addyo.substack.com/p/context-engineering-bringing-engineering",
      "https://www.philschmid.de/context-engineering",
      "https://www.elastic.co/search-labs/blog/context-engineering-vs-prompt-engineering",
      "https://www.deepset.ai/blog/context-engineering-the-next-frontier-beyond-prompt-engineering",
      "https://www.promptingguide.ai/guides/context-engineering-guide",
      "https://datahub.com/blog/context-engineering-vs-prompt-engineering",
      "https://github.com/davidkimai/context-engineering/blob/main/00_COURSE/00_mathematical_foundations/01_context_formalization.md",
      "https://arxiv.org/html/2610.39230v1"
    ]
  }
}
```
**Tool result** `assess_credibility` (id `call-509e8da6-49cb-4c93-9edd-65297743d261`, 11,602 characters):

```
{
  "status": "evaluation_recorded",
  "evaluation": {
    "source_url": "https://medium.com/@fruitful2007/prompt-engineering-is-dead-introducing-context-engineering-6280c075a1a9",
    "source_type": "personal_blog",
    "author": {
      "name": "Paul Fruitful (Medium handle @fruitful2007)",
      "credentials": "Medium About page bio: \"I'm Paul Fruitful, a versatile result-oriented Software Engineer & tech content creator with close to a decade of experience, passionate about the future\" (no employer, degree, publication record or topic-specific credentials). Medium profile shows 62 followers and posts mainly opinion pieces on AI (e.g. 'The AI Wild West Era Is Coming To An End', 'AI Sovereignty: Who Controls The Weights?'). A LinkedIn profile at ng.linkedin.com/in/paulfruitful headlines 'AI Evangelist-Engineer || Making Efficient Agentic Workflows With Almost Zero Running Cost || 18 Y.O', location Lagos State, Nigeria, ~6 years 2 months listed experience (Roadmapr, Vision Incubation Hub, Whiz Navigators, Syticks, Headstarter AI fellowship) and ~3,249 followers. I found no research publications, no academic affiliation and no evidence of recognised expertise in LLM systems. The LinkedIn '18 Y.O' / '6 years 2 months' claims also sit awkwardly with the Medium bio's 'close to a decade of experience'.",
      "credibility_assessment": "The author is identifiable but has no verifiable expertise in LLM engineering or research: a self-described software engineer/content creator with a thin, partly inconsistent public bio and a small following. Nothing in his background supports treating his definitions or generalisations about the field as authoritative, and he cites no sources of his own. His practical experience with AI agents is relevant context but not a substitute for sourcing."
    },
    "publication": {
      "name": "Medium (personal profile of @fruitful2007)",
      "reputation": "Medium is a large open blogging platform (Medium's About page: 'anyone can share knowledge and wisdom with the world'; funded by reader memberships rather than ads). Posts on personal profiles are self-published: there is no fact-checking, editor, peer review or correction process. This article is not part of a Medium editorial publication, so it carries only the platform's baseline content rules. The author's account has ~62 followers, so there is no editorial brand behind the piece.",
      "editorial_process": "self_published"
    },
    "content_analysis": {
      "claims_checked": [
        {
          "claim": "Prompt engineering is dead and is being replaced by context engineering.",
          "status": "contradicted",
          "evidence": "The Prompt Engineering Guide's Context Engineering Guide states that predictions of prompt engineering's death were 'very wrong' and that prompt engineering is 'now even more important than ever' (https://www.promptingguide.ai/guides/context-engineering-guide). DataHub's comparison answers 'No. Prompt engineering remains valuable... The shift is one of scope, not replacement' (https://datahub.com/blog/context-engineering-vs-prompt-engineering). Karpathy himself framed context engineering as a better name for the craft, not the death of prompting (https://pureai.com/articles/2025/09/23/karpathy-puts-context-at-the-core-of-ai-coding.aspx). The article's own body later concedes prompt engineering is 'a part of context engineering', so the headline overstates its case."
        },
        {
          "claim": "Andrej Karpathy defines context engineering as \"the art of filling in the context window with the right information so that the LLM knows what's next.\"",
          "status": "contradicted",
          "evidence": "Karpathy's actual June 2025 wording, as reported by multiple independent outlets, is: 'the delicate art and science of filling the context window with just the right information for the next step' (https://pureai.com/articles/2025/09/23/karpathy-puts-context-at-the-core-of-ai-coding.aspx, https://www.langchain.com/blog/context-engineering-for-agents, https://ai4ra.uidaho.edu/from-prompt-engineering-to-context-engineering). The article presents a loose paraphrase in quotation marks, gives no link to the original post, and then repeats a second, slightly different version of the 'quote' later in the same piece."
        },
        {
          "claim": "Context engineering is a superset of prompt engineering, i.e. prompt engineering is one component of it.",
          "status": "corroborated",
          "evidence": "LangChain's agent context-engineering post treats context engineering as the umbrella covering instructions, knowledge, tools, memory and state (https://www.langchain.com/blog/context-engineering-for-agents); Phil Schmid describes prompt engineering as a narrower single-string practice versus the broader discipline (https://www.philschmid.de/context-engineering); deepset and Elastic make the same scope distinction (https://www.deepset.ai/blog/context-engineering-the-next-frontier-beyond-prompt-engineering, https://www.elastic.co/search-labs/blog/context-engineering-vs-prompt-engineering)."
        },
        {
          "claim": "Because the context window is a hard constraint, agents need persistent memory and retrieval (vector databases / 'context banks') that supply only the context a task needs.",
          "status": "corroborated",
          "evidence": "LangChain's write/select/compress/isolate strategies describe exactly this: storing memory outside the window and retrieving only relevant context (https://www.langchain.com/blog/context-engineering-for-agents); Elasticsearch Labs discusses context-window management failure modes (https://www.elastic.co/search-labs/blog/context-engineering-vs-prompt-engineering); the Prompt Engineering Guide makes the same point about filtering noise (https://www.promptingguide.ai/guides/context-engineering-guide)."
        },
        {
          "claim": "Context engineering has 'mathematical foundations', including an 'assembler function' and 'optimizer functions' for finding the best context.",
          "status": "no_evidence_found",
          "evidence": "The article cites no paper or source for this. A search for 'context engineering' plus 'context assembler'/'optimizer function' returned only community material such as a GitHub course repo using a 'context assembly function' notation (https://github.com/davidkimai/context-engineering/blob/main/00_COURSE/00_mathematical_foundations/01_context_formalization.md) and an arXiv paper on a financial-AI architecture that calls a rigorous optimisation formulation an 'open research problem' (https://arxiv.org/html/2610.39230v1). No authoritative source found establishing these formalisms as the article implies."
        }
      ],
      "claims_supported_by_evidence": false,
      "sources_cited": false,
      "corroborated_by_other_sources": true,
      "contradicted_by_other_sources": true,
      "primary_vs_secondary": "tertiary_source",
      "funding_or_sponsorship": "No funding, sponsor or advertiser disclosed. Medium itself is funded by reader memberships rather than ads (https://medium.com/about). The article does contain a self-promotional pitch: the author says he is building a 'context bank' product, will 'release it in a few weeks' and that 'it'll be open source too. So stay tuned for that', which gives him an interest in driving attention to his own project.",
      "bias_and_tone": "Opinionated and informal: the author frames the piece as 'THE NEW HYPE' and 'My honest take', uses emojis and jokes ('overperform your disappointment 😂'), and repeatedly asserts that context engineering 'is just a fancy word' while also promoting his own forthcoming tool. The headline is clickbait ('PROMPT ENGINEERING IS DEAD') and is stronger than the body, which concedes prompt engineering is a subset of context engineering. There are no citations, no data, no links to the research papers he says he was reading, no counterarguments or limitations, and no explanation of method. It is primarily a personal opinion/explainer with a promotional hook rather than reporting or analysis grounded in evidence.",
      "date_published": "Published 21 July 2025 (page metadata: 2025-07-21T00:17:53Z; byline 'Jul 21, 2025'). No last-updated date shown. As of 26 November 2026 the piece is roughly 16 months old; the concept is still current, but the field moves quickly and the article describes no specific models, benchmarks or 2026 developments, so it is dated as a technical reference."
    },
    "transparency_score": 2,
    "overall_credibility": "low",
    "reasoning": "The author is named and identifiable, which is a plus, but he is a self-described software engineer/content creator with no verifiable expertise in LLM research, a thin and partly inconsistent public bio (Medium: 'close to a decade of experience'; LinkedIn: '18 Y.O', ~6 years listed), and a small following. The post is self-published on a personal Medium profile, so there is no editor, peer review or correction mechanism. It cites no sources at all despite referring to research papers, and the one attributed authority — Andrej Karpathy — is misquoted (his actual phrasing is 'the delicate art and science of filling the context window with just the right information for the next step'), with no link to the original. The headline claim ('prompt engineering is dead') is contradicted by credible sources that describe a shift in scope rather than a replacement, and the body itself concedes the point. On the positive side, the core conceptual claims (context engineering as an umbrella over prompt engineering; context-window limits requiring persistent memory/retrieval) are corroborated by LangChain, Phil Schmid, deepset, Elastic and the Prompt Engineering Guide, so the article is not substantively wrong on its main ideas. Because the ideas are right but the sourcing, expertise, editorial oversight and accuracy of quotation are weak, plus a self-promotional agenda, the source is Low credibility for an academic report — usable only as an example of practitioner commentary, not as evidence for facts.",
    "evidence_urls": [
      "https://medium.com/@fruitful2007/prompt-engineering-is-dead-introducing-context-engineering-6280c075a1a9",
      "https://medium.com/@fruitful2007",
      "https://medium.com/@fruitful2007/about",
      "https://medium.com/about",
      "https://ng.linkedin.com/in/paulfruitful",
      "https://www.linkedin.com/posts/paulfruitful_insurance-for-ai-agents-now-this-is-one-activity-7457399028985597952-_EQs",
      "https://pureai.com/articles/2025/09/23/karpathy-puts-context-at-the-core-of-ai-coding.aspx",
      "https://www.langchain.com/blog/context-engineering-for-agents",
      "https://www.honeyhive.ai/learn/context-engineering-vs-prompt-engineering",
      "https://ai4ra.uidaho.edu/from-prompt-engineering-to-context-engineering",
      "https://addyo.substack.com/p/context-engineering-bringing-engineering",
      "https://www.philschmid.de/context-engineering",
      "https://www.elastic.co/search-labs/blog/context-engineering-vs-prompt-engineering",
      "https://www.deepset.ai/blog/context-engineering-the-next-frontier-beyond-prompt-engineering",
      "https://www.promptingguide.ai/guides/context-engineering-guide",
      "https://datahub.com/blog/context-engineering-vs-prompt-engineering",
      "https://github.com/davidkimai/context-engineering/blob/main/00_COURSE/00_mathematical_foundations/01_context_formalization.md",
      "https://arxiv.org/html/2610.39230v1"
    ]
  }
}
```

## Turn 9

_Model call: 30,612 input tokens, 3,351 output tokens_

**Tool call** `save_report` (id `call-45cff68a-8cfb-48f1-80cf-9b02fe19d943`):

```json
{
  "filename": "medium-prompt-engineering-is-dead-context-engineering.md",
  "markdown": "# Credibility Report: PROMPT ENGINEERING IS DEAD INTRODUCING CONTEXT ENGINEERING\n\n**URL:** https://medium.com/@fruitful2007/prompt-engineering-is-dead-introducing-context-engineering-6280c075a1a9\n**Verdict:** Low credibility\n**Evaluated:** 2026-11-26\n\n## Summary\nThis is a self-published personal opinion/explainer on a Medium profile, written by Paul Fruitful (@fruitful2007), who describes himself as a software engineer and tech content creator. It argues that \"prompt engineering is dead\" and that \"context engineering\" — filling an LLM's context window with the right information — is the real skill, and it adds that context engineering is \"just a fancy word\" for something practitioners already do. The article cites no sources whatsoever, even though it refers to research papers, and its one quoted authority (Andrej Karpathy) is presented in a paraphrase that does not match Karpathy's actual wording. Medium personal profiles are not edited, fact-checked or peer reviewed, and the author's bio offers no verifiable expertise in LLM engineering or research. The main ideas are broadly consistent with mainstream practitioner sources (LangChain, Phil Schmid, deepset, Elastic), so the piece is not substantively wrong — but the clickbait headline is contradicted by credible sources, and the article carries a self-promotional pitch for the author's own forthcoming tool.\n\n## Author\n- **Name as written:** Paul Fruitful (Medium handle `@fruitful2007`; byline photo and \"Get Paul Fruitful's stories in your inbox\").\n- **Medium bio (About page):** \"I'm Paul Fruitful, a versatile result-oriented Software Engineer & tech content creator with close to a decade of experience, passionate about the future.\" No employer, degree, research record or topic-specific credentials.\n- **Medium footprint:** 62 followers; posts are opinion/commentary pieces (\"The AI Wild West Era Is Coming To An End\", \"AI Sovereignty: Who Controls The Weights?\", \"Agentic Engineering: Goodbye To Building Slop Software\").\n- **LinkedIn (ng.linkedin.com/in/paulfruitful):** headline \"AI Evangelist-Engineer || Making Efficient Agentic Workflows With Almost Zero Running Cost || 18 Y.O\"; Lagos State, Nigeria; ~6 years 2 months listed experience (Roadmapr, Vision Incubation Hub, Whiz Navigators, Syticks, Headstarter AI fellowship); ~3,249 followers.\n- **Inconsistency worth noting:** the LinkedIn \"18 Y.O\" and ~6 years listed experience do not fit comfortably with the Medium bio's \"close to a decade of experience.\"\n- **Not found:** any research publications, academic affiliation, conference talks, or independent recognition as an authority on LLM/agent systems.\n\n## Publication\n- **Platform:** Medium, a large open blogging site. Medium's own About page describes it as a place where \"anyone can share knowledge and wisdom with the world\"; it is funded by reader memberships rather than advertising.\n- **Editorial process:** none. This article sits on a personal profile, not inside a Medium editorial publication, so there is no editor, fact-check, peer review, or visible corrections policy. There is no corrections notice or update log on the page.\n- **Reputation:** Medium as a platform is legitimate and widely used, but a personal-profile post carries only the author's own credibility. With ~62 followers there is no editorial brand behind this piece.\n\n## Claims Checked\n\n| Claim | Status | Evidence |\n|---|---|---|\n| \"Prompt engineering is dead\"; context engineering replaces it | **Contradicted** | The Prompt Engineering Guide states that predictions of prompt engineering's death were \"very wrong\" and that it is \"now even more important than ever\" (https://www.promptingguide.ai/guides/context-engineering-guide). DataHub answers the replacement question \"No. Prompt engineering remains valuable… The shift is one of scope, not replacement\" (https://datahub.com/blog/context-engineering-vs-prompt-engineering). Reporting on Karpathy's June 2025 post frames context engineering as a better *name* for the craft, not the death of prompting (https://pureai.com/articles/2025/09/23/karpathy-puts-context-at-the-core-of-ai-coding.aspx). The article's own body later concedes prompt engineering is \"a part of context engineering\". |\n| Karpathy defines context engineering as \"the art of filling in the context window with the right information so that the LLM knows what's next\" | **Contradicted** (misquotation) | Karpathy's actual wording, reported independently, is \"the delicate art and science of filling the context window with just the right information for the next step\" (https://pureai.com/articles/2025/09/23/karpathy-puts-context-at-the-core-of-ai-coding.aspx; https://www.langchain.com/blog/context-engineering-for-agents; https://ai4ra.uidaho.edu/from-prompt-engineering-to-context-engineering). The article puts a loose paraphrase in quotation marks, gives no link to the original post, and later repeats a second, slightly different version of the same \"quote\". |\n| Context engineering is a superset of prompt engineering; prompt engineering is one part of it | **Corroborated** | LangChain treats context engineering as the umbrella over instructions, knowledge, tools, memory and state (https://www.langchain.com/blog/context-engineering-for-agents); Phil Schmid draws the same scope distinction (https://www.philschmid.de/context-engineering); deepset (https://www.deepset.ai/blog/context-engineering-the-next-frontier-beyond-prompt-engineering) and Elastic (https://www.elastic.co/search-labs/blog/context-engineering-vs-prompt-engineering) agree. |\n| Because the context window is a hard limit, agents need persistent memory and retrieval (\"context banks\"/vector databases) that supply only the context a task needs | **Corroborated** | LangChain's write / select / compress / isolate strategies describe storing memory outside the window and retrieving only relevant context (https://www.langchain.com/blog/context-engineering-for-agents); Elasticsearch Labs discusses context-window failure modes (https://www.elastic.co/search-labs/blog/context-engineering-vs-prompt-engineering); the Prompt Engineering Guide makes the same point about filtering noise (https://www.promptingguide.ai/guides/context-engineering-guide). |\n| Context engineering has \"mathematical foundations\", including an \"assembler function\" and \"optimizer functions\" | **No evidence found** | The article cites nothing for this. Searching for these terms surfaced only community material — a GitHub course repo using a \"context assembly function\" notation (https://github.com/davidkimai/context-engineering/blob/main/00_COURSE/00_mathematical_foundations/01_context_formalization.md) and an arXiv paper that calls a rigorous optimisation formulation an \"open research problem\" (https://arxiv.org/html/2610.39230v1). No authoritative source establishes the formalisms as the article implies. |\n\n## Bias and Tone\n- **Framing:** The piece is labelled \"THE NEW HYPE\" and \"My honest take\"; it is an opinion column, not reporting or analysis.\n- **Language:** Informal and emotionally flavoured — emojis, jokes (\"overperform your disappointment 😂\"), rhetorical questions, repetition. It asserts that context engineering \"is just a fancy word\" and \"just grammar\" while also presenting it as a discipline with mathematical foundations — an internal tension.\n- **Headline vs body:** The headline (\"PROMPT ENGINEERING IS DEAD\") is much stronger than the body, which concedes prompt engineering is a subset of context engineering. This is clickbait framing.\n- **Missing:** no counterarguments, no limitations, no data, no methodology, no links to the \"research papers\" the author says he was reading.\n- **Interest:** The article promotes the author's own in-development \"context bank\" product (\"I'm actually building one for myself… I'll release it in a few weeks… It'll be open source too. So stay tuned\"), which gives him a stake in driving attention to his work. No funding, sponsorship or advertising is disclosed.\n\n## Currency\n- **Published:** 21 July 2025 (page metadata `2025-07-21T00:17:53Z`; byline \"Jul 21, 2025\"). **No last-updated date is shown.**\n- **Assessment:** About 16 months old as of 26 November 2026. The concept remains current, but the field moves quickly and the article names no models, benchmarks, tools or 2026 developments, so it is dated for any technical detail. The Karpathy quote dates from June 2025.\n\n## Structured Assessment\n\n| Field | Value |\n|---|---|\n| Source URL | https://medium.com/@fruitful2007/prompt-engineering-is-dead-introducing-context-engineering-6280c075a1a9 |\n| Source type | Personal blog (Medium personal profile) |\n| Author | Paul Fruitful (@fruitful2007) — self-described software engineer / tech content creator; no verifiable LLM research credentials; bio partly inconsistent with his LinkedIn (see Author) |\n| Author credibility | Low: identifiable but no demonstrated expertise; no publications or affiliations found |\n| Publication | Medium (personal profile, not an editorial publication) |\n| Editorial process | Self-published |\n| Publication reputation | Legitimate open platform; no editorial gatekeeping on personal posts; ~62 followers on this account |\n| Claims supported by evidence in the source | No |\n| Sources cited | No |\n| Primary / secondary / tertiary | Tertiary (summarises/opines on concepts popularised elsewhere) |\n| Corroborated by other sources | Yes (core concepts: context engineering as umbrella; memory/retrieval for context limits) |\n| Contradicted by other sources | Yes (\"prompt engineering is dead\"; the Karpathy quotation) |\n| Funding / sponsorship | Not found. Medium is membership-funded; the article promotes the author's own forthcoming tool |\n| Bias and tone | Opinionated, informal, clickbait headline, no counterarguments, self-promotional |\n| Date published | 21 July 2025; no update date; ~16 months old as of evaluation |\n| Transparency score | 2 / 5 (author identified, but no sources, no method, no funding/sponsorship statement) |\n| **Overall credibility** | **Low** |\n\n## Can I cite this?\n**Find a better source.** Do not cite this for facts, definitions, or the claim that prompt engineering is dead.\n\n- If you need the *definition* of context engineering, cite the primary or near-primary material instead: Karpathy's June 2025 post as reported/quoted by a reliable outlet (https://pureai.com/articles/2025/09/23/karpathy-puts-context-at-the-core-of-ai-coding.aspx), LangChain's context-engineering post (https://www.langchain.com/blog/context-engineering-for-agents), Anthropic's engineering writing, or Phil Schmid (https://www.philschmid.de/context-engineering).\n- If you want to show that *practitioners debate the term* — e.g. that some argue \"context engineering\" is a rebrand of existing prompt practice — you may cite this **with care, as an example of practitioner opinion**, clearly labelled as a self-published Medium blog post and dated 21 July 2025. Do not use it as evidence that the field has reached that conclusion, and do not repeat its Karpathy quotation (it is not accurate).\n- Avoid quoting the headline claim. Credible sources describe a shift in scope, not the death of prompt engineering.\n- If your instructor requires peer-reviewed or editorially reviewed sources, this does not qualify.\n\n## Sources Consulted\n1. https://medium.com/@fruitful2007/prompt-engineering-is-dead-introducing-context-engineering-6280c075a1a9 — the source itself (read in full, 10,303 characters): opinion essay, no citations, two paraphrased Karpathy \"quotes\", promo for author's own tool.\n2. https://medium.com/@fruitful2007 — author's Medium profile: 62 followers, list of AI opinion posts, no credentials.\n3. https://medium.com/@fruitful2007/about — author bio: \"versatile result-oriented Software Engineer & tech content creator with close to a decade of experience\".\n4. https://medium.com/about — Medium's own description of the platform and its membership funding model.\n5. https://ng.linkedin.com/in/paulfruitful — author's LinkedIn: \"18 Y.O\", Lagos State, ~6 years 2 months experience, no research credentials.\n6. https://www.linkedin.com/posts/paulfruitful_insurance-for-ai-agents-now-this-is-one-activity-7457399028985597952-_EQs — author's LinkedIn activity (3,247 followers, 660 posts, 37 articles), confirming he is an active AI commentary poster.\n7. https://pureai.com/articles/2025/09/23/karpathy-puts-context-at-the-core-of-ai-coding.aspx — Karpathy's actual June 25, 2025 wording of the context-engineering definition; shows the article's quote is a paraphrase.\n8. https://www.langchain.com/blog/context-engineering-for-agents — corroborates the umbrella definition and the memory/retrieval strategies; also quotes Karpathy correctly.\n9. https://www.honeyhive.ai/learn/context-engineering-vs-prompt-engineering — independent comparison of the two terms; same Karpathy wording.\n10. https://ai4ra.uidaho.edu/from-prompt-engineering-to-context-engineering — university-hosted explainer; confirms the quote and the mid-2025 origin of the term.\n11. https://addyo.substack.com/p/context-engineering-bringing-engineering — practitioner explainer on Tobi Lütke and Karpathy popularising the term.\n12. https://www.philschmid.de/context-engineering — corroborates context engineering as broader than prompt engineering.\n13. https://www.elastic.co/search-labs/blog/context-engineering-vs-prompt-engineering — corroborates scope distinction and context-window management.\n14. https://www.deepset.ai/blog/context-engineering-the-next-frontier-beyond-prompt-engineering — corroborates the scope distinction.\n15. https://www.promptingguide.ai/guides/context-engineering-guide — directly contradicts \"prompt engineering is dead\"; supports filtering relevant context.\n16. https://datahub.com/blog/context-engineering-vs-prompt-engineering — directly contradicts replacement framing: \"shift is one of scope, not replacement\".\n17. https://github.com/davidkimai/context-engineering/blob/main/00_COURSE/00_mathematical_foundations/01_context_formalization.md — community course repo using a \"context assembly function\"; not an authoritative source for the article's math claim.\n18. https://arxiv.org/html/2610.39230v1 — arXiv paper calling a rigorous context optimisation formulation an \"open research problem\"; relevant to the unverified \"mathematical foundations\" claim.\n"
}
```
**Tool result** `save_report` (id `call-45cff68a-8cfb-48f1-80cf-9b02fe19d943`, 105 characters):

```
Saved the report to reports/medium-prompt-engineering-is-dead-context-engineering.md (14,347 characters).
```

## Turn 10

_Model call: 33,999 input tokens, 231 output tokens_

**Assistant:**

The report is saved as `medium-prompt-engineering-is-dead-context-engineering.md`.

**Verdict: Low credibility.** The source is a self-published opinion piece on a personal Medium profile (no editor, fact-check or peer review) by Paul Fruitful, a self-described software engineer/content creator whose public bios are thin and mutually inconsistent, and who cites no sources at all despite referring to research papers. Its headline claim that "prompt engineering is dead" is contradicted by credible sources that describe a shift in scope rather than a replacement, and its attributed Andrej Karpathy quote is an inaccurate paraphrase of his actual wording — plus the article ends with a promo for the author's own forthcoming tool. To its credit, the core conceptual claims (context engineering as an umbrella over prompt engineering; context-window limits requiring persistent memory and retrieval) are corroborated by LangChain, Phil Schmid, deepset, Elastic and the Prompt Engineering Guide, so the ideas aren't wrong — but for an academic report you should cite those sources instead, and use this piece at most as an explicitly labelled example of practitioner opinion.


## Final output

The report is saved as `medium-prompt-engineering-is-dead-context-engineering.md`.

**Verdict: Low credibility.** The source is a self-published opinion piece on a personal Medium profile (no editor, fact-check or peer review) by Paul Fruitful, a self-described software engineer/content creator whose public bios are thin and mutually inconsistent, and who cites no sources at all despite referring to research papers. Its headline claim that "prompt engineering is dead" is contradicted by credible sources that describe a shift in scope rather than a replacement, and its attributed Andrej Karpathy quote is an inaccurate paraphrase of his actual wording — plus the article ends with a promo for the author's own forthcoming tool. To its credit, the core conceptual claims (context engineering as an umbrella over prompt engineering; context-window limits requiring persistent memory and retrieval) are corroborated by LangChain, Phil Schmid, deepset, Elastic and the Prompt Engineering Guide, so the ideas aren't wrong — but for an academic report you should cite those sources instead, and use this piece at most as an explicitly labelled example of practitioner opinion.

## Summary

- Turns (model calls): 10
- Tool calls: web_search x7, read_url x5, assess_credibility x1, save_report x1
- Tokens: 174,801 input (144,768 cached), 9,086 output
- Estimated cost: $0.0104
- Report: reports/medium-prompt-engineering-is-dead-context-engineering.md
