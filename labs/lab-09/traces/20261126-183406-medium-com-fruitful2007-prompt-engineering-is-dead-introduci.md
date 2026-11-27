# Agent trace: https://medium.com/@fruitful2007/prompt-engineering-is-dead-introducing-context-engineering-6280c075a1a9

- Model: `deepseek/deepseek-v4.1-flash-1017`
- Started: 2026-11-26T18:34:06
- Max turns: 25
- Tools: read_url, web_search, assess_credibility, save_report


**User:** Evaluate the credibility of this source: https://medium.com/@fruitful2007/prompt-engineering-is-dead-introducing-context-engineering-6280c075a1a9

## Turn 1

_Model call: 4,702 input tokens, 94 output tokens_

**Assistant:**

I'll start by reading the source page.

**Tool call** `read_url` (id `call-9fa89678-3916-456b-96c1-8bc3bab35dad`):

```json
{
  "url": "https://medium.com/@fruitful2007/prompt-engineering-is-dead-introducing-context-engineering-6280c075a1a9",
  "start": 0
}
```
**Tool result** `read_url` (id `call-9fa89678-3916-456b-96c1-8bc3bab35dad`, 10,096 characters):

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

_Model call: 7,099 input tokens, 93 output tokens_

**Tool call** `read_url` (id `call-b628b5f2-e9d7-4301-b7f9-3a93fd8ea58e`):

```json
{
  "url": "https://medium.com/@fruitful2007/prompt-engineering-is-dead-introducing-context-engineering-6280c075a1a9",
  "start": 10000
}
```
**Tool result** `read_url` (id `call-b628b5f2-e9d7-4301-b7f9-3a93fd8ea58e`, 362 characters):

```
using grammar, all the fancy scientific terms.

Context engineering is just providing and structuring the right information inside the context window of agents using basically prompts.

And the truth is: You probably do this every day with ChatGPT😂  
That’s it for this article.  
Thank you for reading


[End of page. Showed characters 10,000-10,303 of 10,303.]
```

## Turn 3

_Model call: 7,283 input tokens, 261 output tokens_

**Tool call** `web_search` (id `call-27006d6a-d0bb-4fbe-b1e0-27950d948be7`):

```json
{
  "query": "\"Paul Fruitful\" Medium AI writer"
}
```
**Tool call** `web_search` (id `call-85b65bc9-c673-47ad-844e-2ec5ba8fb7e3`):

```json
{
  "query": "Andrej Karpathy \"context engineering\" quote \"filling the context window\""
}
```
**Tool call** `web_search` (id `call-0b4986aa-9827-49d2-8d5a-4eab0541c64b`):

```json
{
  "query": "\"Prompt Engineering is Dead\" \"Context Engineering\" medium fruitful2007"
}
```
**Tool result** `web_search` (id `call-85b65bc9-c673-47ad-844e-2ec5ba8fb7e3`, 6,678 characters):

```
Search results for "Andrej Karpathy "context engineering" quote "filling the context window"" (searched 2026-11-26):

[1] Context engineering vs prompt engineering | HoneyHive
URL: https://www.honeyhive.ai/learn/context-engineering-vs-prompt-engineering
Excerpt: Andrej Karpathy wrote the version LangChain and others quote: people associate prompts with short task descriptions, while in an industrial-strength LLM app, “context engineering is the delicate art and science of filling the context window with just the right information for the next step.” He lists what goes in: task descriptions and explanations, few-shot examples, RAG, related data, tools, state and history, and compacting. [...] Karpathy goes the other way on scope. Karpathy calls context engineering “just one small piece of an emerging thick layer of non-trivial software” that also breaks problems into control flows, dispatches calls to the right model, handles generation-verification UI, and covers guardrails, security, evals, parallelism and prefetching. [...] Karpathy describes both directions: with too little, or the wrong form, the model lacks what it needs, and with too much or irrelevant material, “the LLM costs might go up and performance might come down.”

Everything in a request counts, per the Claude docs: the system prompt, every message, tool results, images, documents and tool definitions.

## The techniques

LangChain sorts context engineering for agents into four strategies.

[2] Karpathy Puts Context at the Core of AI Coding -- Pure AI
URL: https://pureai.com/articles/2025/09/23/karpathy-puts-context-at-the-core-of-ai-coding.aspx
Excerpt: As Karpathy puts it: context engineering is "the delicate art and science of filling the context window with just the right information for the next step." The difference is that prompts instruct what to do now, while context shapes how the model understands the world in which it must act. [...] Karpathy weighed in on the subject on June 25 in a post on X, favoring context engineering. "People associate prompts with short task descriptions you'd give an LLM in your day-to-day use," he wrote. "When in every industrial-strength LLM app, context engineering is the delicate art and science of filling the context window with just the right information for the next step." [...] But prompts are turning out to be only half the story. As applications become more ambitious, models gain larger context windows, and retrieval and memory systems are layered in, a different discipline begins to emerge —the one that Karpathy has now identified as the real key to AI application development: context engineering.

[3] From Prompt Engineering to Context Engineering – Artificial Intelligence for Research Administration
URL: https://ai4ra.uidaho.edu/from-prompt-engineering-to-context-engineering
Excerpt: However, in recent conversations around AI and its development a new term has emerged: context engineering. In mid-2025, the term gained traction rapidly after Shopify CEO Tobi Lütke and former OpenAI researcher Andrej Karpathy both endorsed it publicly.

> Karpathy described it as “the delicate art and science of filling the context window with just the right information for the next step.”
>
> Andrej Karpathy [...] All that information, everything the AI can “see” when it generates a response, is called its context. And the maximum size of the context that a model can handle is called its context window. And it turns out that the quality of that context matters far more than the exact phrasing of any single prompt. As Karpathy put it, the shift is from asking smart questions to building smarter environments for the AI to work in. [...] This is what context engineering is: the practice of designing, curating, and managing the full set of information an AI has access to, not just the instruction you type, but the documents, memory, history, examples, and constraints that surround it. If prompt engineering is asking the right question in a meeting, context engineering is making sure everyone walks in having read the same briefing document first.

### Is This Actually New?

[4] Andrej Karpathy on X: "+1 for "context engineering" over "prompt engineering". People associate prompts with short task des…"
URL: https://x.com/karpathy/status/1937902205765607626
Excerpt: People associate prompts with short task descriptions you'd give an LLM in your day-to-day use. When in every industrial-strength LLM app, context engineering is the delicate art and science of filling the context window with just the right information for the next step. Science because doing this right involves task descriptions and explanations, few shot examples, RAG, related (possibly multimodal) data, tools, state and history, compacting... Too little or of the wrong form and the LLM [...] > Quoting @tobi (tobi lutke):
>
> I really like the term “context engineering” over prompt engineering. 
> 
> It describes the core skill better: the art of providing all the context for the task to be plausibly solvable by the LLM.

## People

- @karpathy (Andrej Karpathy)
- @tobi (tobi lutke) — Shopify CEO by day, Dad in evening, hacker at night, Aspiring comprehensivist. [...] On top of context engineering itself, an LLM app has to:
- break up problems just right into control flows
- pack the context windows just right
- dispatch calls to LLMs of the right kind and capability
- handle generation-verification UIUX flows
- a lot more - guardrails, security, evals, parallelism, prefetching, ...

[5] Context Engineering
URL: https://www.langchain.com/blog/context-engineering-for-agents
Excerpt: As Andrej Karpathy puts it, LLMs are like a new kind of operating system. The LLM is like the CPU and its context window is like the RAM, serving as the model’s working memory. Just like RAM, the LLM context window has limited capacity to handle various sources of context. And just as an operating system curates what fits into a CPU’s RAM, we can think about “context engineering” playing a similar role. Karpathy summarizes this well: [...] > [Context engineering is the] ”…delicate art and science of filling the context window with just the right information for the next step.”

Context types commonly used in LLM applications

What are the types of context that we need to manage when building LLM applications? Context engineering as an umbrella that applies across a few different context types: [...] > The LeadResearcher begins by thinking through the approach and saving its plan to Memory to persist the context, since if the context window exceeds 200,000 tokens it will be truncated and it is important to retain the plan.
```
**Tool result** `web_search` (id `call-0b4986aa-9827-49d2-8d5a-4eab0541c64b`, 7,274 characters):

```
Search results for ""Prompt Engineering is Dead" "Context Engineering" medium fruitful2007" (searched 2026-11-26):

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
That’s what context engineering is all about. [...] “Okay, that means I can engineer context with just prompts."  
Yes, you can.  
Because at the end of the day, you use prompts to engineer context.  
But prompt engineering is not context engineering.

Prompt engineering is a part of context engineering.

Prompt engineering kind of acts on the system that your context-engineered environment creates.

So, I dive deeper  
The next step, after you create a world inside an agent, is persisted memory.

[2] Prompt Engineering Is Dead. Context Engineering Is Next.
URL: https://medium.com/data-science-collective/prompt-engineering-is-dead-context-engineering-is-next-a6c5e1e6012c
Excerpt: Here’s the thing about prompt engineering that nobody talks about: it doesn’t compound. You learn a new trick. It works for one use case. You forget it six months later. There’s no system being built.

Context engineering is different. Every context you design — every system prompt, every knowledge base, every memory structure — is an asset. It gets better over time. You refine it. You add to it. Other people can use it. [...] They set up a retrieval system so the AI can pull from real documents. They wrote a system prompt that gives the AI a clear identity and set of rules. They structured memory so the AI knows what happened in previous conversations. They designed the pipeline so the right information gets injected at the right time.

That is context engineering. And right now, most people have no idea it exists. [...] AI models don’t have memory by default. Every new conversation is a blank slate. Context engineering means designing systems that preserve what matters — previous decisions, user preferences, ongoing project details — and injecting it back into the context window so the AI can build on what came before.

Layer 4 — External State: what’s happening right now?

[3] Prompt Engineering Is Dead. Context Engineering Is What Actually ...
URL: https://hackernoon.com/prompt-engineering-is-dead-context-engineering-is-what-actually-matters-now
Excerpt: Context engineering optimises the whole thing.

The question it asks is not "how should I word this instruction?" It is "what should the model know when it answers?"

These are different questions. They lead to different work. And in production AI systems, the second question is where almost all the real leverage lives.

## The Five Layers of Context What Each One Does [...] Understanding context engineering means understanding what you are assembling. There are five layers, and each has its own design decisions.

### Layer 1: The System Prompt Your Persistent Instructions

This is the layer prompt engineering focused on. It still matters. But context engineers think about it differently.

A prompt engineer asks: "what is the best way to instruct this model?" [...] Prompt engineering assumes the model has everything it needs and just needs good instructions. It is optimising how you ask. It is about the phrasing, the structure, the examples you give, the persona you assign.

Here is where it breaks down.

When the information is not there, no instruction can conjure it.

[4] Prompt Engineering Is Dead. Context Engineering Is Dying. What Comes Next Changes Everything.
URL: https://www.youtube.com/watch?v=QWzLPn164w0
Excerpt: here because naming things matters. Naming is how we create a shared understanding and I think we are short on naming things correctly when it comes to intent and context. Prompt engineering was the first discipline in the age of AI. It was individual, synchronous, and sessionbased. You sit in front of the chat window, you craft an instruction, you iterate the output. It's a personal skill, and the value is personal. This is the era that produced a thousand how to write the perfect prompt blog [...] very expensive way. Intent engineering. Intent engineering is the third discipline and it's the one that almost nobody's building for yet. Context engineering tells the agents what to know. Intent engineering tells agents what to want. It's the practice of encoding organizational purpose into infrastructure, not as pros in a system prompt, but as structured, actionable parameters that shape how agents make decisions autonomously. It's the layer that would have told Clara's AI agent, "Yes, you [...] context engineering. Context engineering is such a good term. I wish I came up with that term because it describes everything we've done at Langchain without knowing the term existed. End quote. That's pretty good. Context engineering is where the action is right now. Building rag pipelines, wiring up MCP servers, structuring organizational knowledge so agents can access it. It's necessary, but it's not sufficient. And I think the industry is about to discover that in a very expensive way.

[5] Prompt Engineering Is Dead, and Context Engineering Is Already Obsolete: Why the Future Is Automated Workflow Architecture with LLMs - Prompting - OpenAI Developer Community
URL: https://community.openai.com/t/prompt-engineering-is-dead-and-context-engineering-is-already-obsolete-why-the-future-is-automated-workflow-architecture-with-llms/1314011
Excerpt: For a time, this was accepted as a necessary cost, especially for teams building prototypes or academic experiments. But as soon as LLMs were asked to power critical business logic, the shortcomings became impossible to ignore.

The Context Engineering Revolution—And Its Limits [...] The landscape of LLM engineering is shifting under our feet. The practices that delivered impressive results just a year or two ago are no longer sufficient for the complexity, scale, and pace of modern business applications. Prompt engineering is a relic. Context engineering, for many, is already showing its limits. [...] The problem is not only “what is being said,” but also what meaning the system assigns to it before and after generation — something the human amygdala does constantly, shaping perception, urgency, and memory. Without that modulatory layer of “importance,” the filter risks becoming another deterministic gate rather than an interpreter of emotional and epistemic integrity.
```
**Tool result** `web_search` (id `call-27006d6a-d0bb-4fbe-b1e0-27950d948be7`, 5,147 characters):

```
Search results for ""Paul Fruitful" Medium AI writer" (searched 2026-11-26):

[1] Medium
URL: https://medium.com/@fruitful2007
Excerpt: Pinned

Paul Fruitful

·

Jun 15

The AI Wild West Era Is Coming To An EndThe AI Wild West Era Is Coming To An End

Oct 19

Jul 2

Feb 4

Jan 19

Nov 9, 2025

Sep 16, 2025

Sep 8, 2025

Jul 21, 2025

Jul 14, 2025

I’m Paul Fruitful, a versatile result-oriented Software Engineer & tech content creator with close to a decade of experience, passionate about the future

Ignacio de Gregorio

Mehmet Ozkaya

Opemipo Disu

Laravel News

[2] Paul Fruitful
URL: https://paulfruiful.com
Excerpt: Over the years, I’ve honed a wide range of skills, including AI, Backend engineering, Machine learning, Cloud computing, Networking, Frontend development, Programming, and Pentesting. I specialize in digitizing manual workflows, automating complex processes, and seamlessly integrating AI into virtually anything. If there’s a better, smarter way to get things done, I’ll find it – and build it. [...] I provide a wide range of services to help turn your ideas into reality.

Pick a service let's get started

Build An AI-powered software, intelligent agents, for seamless AI integrations.

Get robust web, mobile, and desktop applications tailored to your needs.

Get robust APIs and scalable backend systems to power your applications.

Create workflows and automates processes to make life easier and more efficient for yourself. [...] Dive into my technical blog, where I share in-depth articles on software engineering, development practices, and cutting-edge technology topics.

Step-by-step strategies, techniques, and coding challenges to help you prepare for technical interviews.

Learn essential mathematical concepts for machine learning, explained and implemented in Python.

[3] Medium’s NEW Rules for AI-Generated Writing 🚨
URL: https://www.youtube.com/watch?v=px5lmImKXf4
Excerpt: I help writers and authors start writing on Medium, build and audience, and market and monetize their words. 
In this video, I share everything writers need to know about Medium's new AI policy.
I share the email Medium sent to their Medium Partner Program members. I also highlight the most important changes. I talk about the future of AI on Medium and what it means for non-native writers. [...] Medium just announced some huge changes to their Medium partner program that will change the game for writers.
I received an email from Medium in which they talk about their NEW AI policy. what is allowed and what isn’t, who it effects, what writers have to do now and moving forward. [...] false positives and false negatives are common and there's also a peer reviewed paper that showed that AI detectors falsely flect non-native English writing as AI generated and that hit home because it already happened to me that an aditor rejected the story because he thought it was AI generated writing which it wasn't in addition I recently submitted five stories to publication and they rejected me because no human can do this let's see what medium writers have to say about the new AI policy

[4] Medium
URL: https://ai.plainenglish.io/the-ai-prompt-formula-for-writing-medium-articles-people-actually-read-44ed4569561e
Excerpt: The writers who are actually building audiences on Medium in 2026 — the ones with thousands of followers, consistent reads, and articles that get boosted by the Medium curation team — are not writing without AI. They’re writing with AI prompts designed specifically for how Medium works. There’s a difference between using AI to generate content and using AI prompt formulas to craft articles that earn attention. [...] This article gives you that formula. Every prompt, every stage, every structural decision that separates a Medium article people finish from one they abandon in 30 seconds. These are high-volume, battle-tested AI writing prompts built around Medium’s specific reader behavior, algorithm signals, and curation criteria.

By the end, you’ll have a complete repeatable system for writing Medium articles with AI that people actually read, share, and follow you because of. [...] ## Why Medium Is Different From Every Other Platform

Before the prompts, you need to understand why Medium requires its own formula. The AI writing prompts that work for SEO blog posts, LinkedIn articles, or newsletter content will not produce the same results on Medium. The platform has a distinct reader contract that most writers violate without realizing it.

[5] Medium
URL: https://medium.com/data-science-collective/i-run-mediums-largest-ai-ml-publication-here-s-what-i-wish-every-writer-knew-5bcf3b42d22d
Excerpt: Member-only story

Featured

# I Run Medium’s Largest AI/ML Publication. Here’s What I Wish Every Writer Knew.

## 10 lessons and a 90-day playbook from 919K followers.

A few months ago I stopped obsessing over my Medium stats.

The piece I almost didn’t publish, a 9-minute confessional about an NVIDIA dev kit I’d half-given-up on, came in at a 76% read rate. My highest ever. Meanwhile, pieces I’d bet on died.

Something had quietly broken in how I was reading the platform.
```

## Turn 4

_Model call: 11,685 input tokens, 549 output tokens_

**Tool call** `read_url` (id `call-ccd7e184-2eaf-49b6-8923-93cc89066721`):

```json
{
  "url": "https://medium.com/@fruitful2007",
  "start": 0
}
```
**Tool call** `web_search` (id `call-252f48a9-72ea-463d-bc98-6d66d096e57f`):

```json
{
  "query": "\"prompt engineering is dead\" claim overstated still matters experts 2025 2026"
}
```
**Tool result** `read_url` (id `call-ccd7e184-2eaf-49b6-8923-93cc89066721`, 10,096 characters):

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
**Tool result** `web_search` (id `call-252f48a9-72ea-463d-bc98-6d66d096e57f`, 6,528 characters):

```
Search results for ""prompt engineering is dead" claim overstated still matters experts 2025 2026" (searched 2026-11-26):

[1] Is Prompt Engineering Dead? What Replaced It
URL: https://futurefactors.ai/prompt-engineering-dead-what-replaced-it-2026
Excerpt: Absolutely. Good prompting skills still help, but now they’re foundational literacy rather than a specialized expertise. The difference is that you don’t need to learn complex prompt engineering techniques. Clear instructions usually work fine with Claude, GPT-4o, and Gemini in 2026. The effort-to-benefit ratio of prompt optimization has become unfavorable.

What’s the difference between prompt engineering and process engineering? [...] Prompt engineering as a standalone skill is officially dead. IEEE Spectrum said it. The market confirmed it with a 40% drop in job postings. The shift started in late 2024 when models like Claude, GPT-4o, and Gemini became good enough at interpreting natural language that trial-and-error “engineering” became unnecessary. What replaced it: process engineering, AI orchestration, and metacognitive skills. If you want to stay relevant in 2026, focus on building workflows and systems, not perfecting [...] This guide reflects current trends in 2026 and is based on research from IEEE Spectrum, IBM, Lakera, The Neuron, and field observations from working with 50+ teams adopting AI processes. The death of prompt engineering isn’t speculation. It’s documented in job markets, industry publications, and the lived experience of practitioners. What matters now is building on this foundation with systems thinking and process design.

[2] Is Prompt Engineering Still Worth It in 2026? (The Truth)
URL: https://www.youtube.com/watch?v=pi86am09amg
Excerpt: models behave when context is incomplete, misleading, overloaded, or adversarial. So here is the important takeaway for you. Prompt engineering in 2026 is not obsolete, but it is no longer sufficient by itself. The people who grow are the ones who understand prompting inside of this broader context life cycle. So, how do you position yourself based on this reality? If you're aiming for testing, QA or red team roles, be explicit. Talk about prompt based testing, advisoral evaluation, and failure [...] and pipelines. And most importantly, companies stopped experimenting and started shipping Genai systems to real users at scale. Now, once that happened, writing prompts by itself stopped being enough for most teams. Companies didn't just need somebody to find prompts that worked. They needed people who could control the behavior, test the reliability and own the outcomes from these models and that is the key shift. So prompt engineering did not die. It stopped being the whole job. So let's be [...] for LLMdriven systems. Now that is context engineering. And once you start thinking this way, you stop obsessing over the perfect prompt and you start designing systems that actually work in the real world. And this is exactly why prompt engineer as a standalone role might be fading away. The work did not disappear. It's just expanded upward into system thinking in product facing roles like AI engineer or applied AI engineer. Prompting is embedded inside context engineering. You're deciding

[3] The Death of Prompt Engineering Has Been Greatly Exaggerated by Jared Zoneraich
URL: https://imjaredz.com/writing/the-death-of-prompt-engineering-has-been-greatly-exaggerated.html
Excerpt: back

# The Death of Prompt Engineering Has Been Greatly Exaggerated

Jared Zoneraich · February 2025

As AI models become increasingly sophisticated, there's a growing narrative that prompt engineering – the art and science of instructing large language models – will soon become obsolete. As models get better at understanding natural language, will the need for carefully crafted prompts will disappear?

The death of prompt engineering has been greatly exaggerated.

## What is Prompt Engineering [...] Prompt engineering isn't dying. It's evolving into something more sophisticated and accessible. The superficial tricks will fade. The core challenge remains: translating human knowledge and intent into actionable AI instructions.

Stephen Wolfram calls this "computational irreducibility." Advanced AI won't eliminate the human element in defining problems and success metrics. Humanity will be central to the AI revolution. [...] Most people misunderstand prompt engineering. They see it as a collection of tips and tricks – adding "please" and "thank you" or creating elaborate role-playing scenarios to coax better results from AI models. I classify these surface-level and superficial optimizations as prompt folklore. The true essence of prompt engineering lies in communication. We must communicate human knowledge, goals, and constraints into a format that AI systems can meaningfully act upon.

[4] Ai-Agent-Engineering.org on Facebook: "Prompt engineering is dead. Context engineering is what separates the amateurs from the pros in 2026…"
URL: https://www.facebook.com/groups/aiagentengineeringcommunity/posts/1429892538136984
Excerpt: # Ai-Agent-Engineering.org on Facebook: "Prompt engineering is dead. Context engineering is what separates the amateurs from the pros in 2026…"

Prompt engineering is dead. Context engineering is what separates the amateurs from the pros in 2026.

It's not about crafting the perfect prompt anymore. It's about controlling what the model knows, when it knows it, and how much it can see.

The skill shift is real - and it's happening fast. [...] - Author: Ai-Agent-Engineering.org
- Group: AI Agent Engineering
- Posted: 2026-03-16T18:27:41+00:00
- Shared link: 
- Links: 
- Reactions: 0
- Comment count: 1
- Shares: 0
- Privacy: Public group

## Comments

- Ai-Agent-Engineering.org: Read more:

[5] Context engineering: the future of AI | Ghadeer A. posted on the topic | LinkedIn
URL: https://www.linkedin.com/posts/ghadeer-al-ruwaishedi_prompt-engineering-is-dead-context-engineering-activity-7385993284520865793-ZUIv
Excerpt: Prompt engineering is dead. Context engineering is the $500K skill of 2025. Most people still talk about “prompt engineering.” But that’s not how real AI systems think anymore. Prompts die after one interaction. They don’t remember. They don’t reason. You can’t build intelligence on forgetfulness. So we started cramming everything into context docs, chats, rules, and knowledge bases and called it “context-augmented generation.” It worked… until it didn’t. Models got slower. Hallucinations
```

## Turn 5

_Model call: 16,926 input tokens, 417 output tokens_

**Tool call** `read_url` (id `call-ed7647cc-920d-4c1a-9290-0d19b798e204`):

```json
{
  "url": "https://medium.com/@fruitful2007/about",
  "start": 0
}
```
**Tool call** `web_search` (id `call-a16215ab-7b4c-4a99-b58e-e5816b0dec22`):

```json
{
  "query": "context engineering survey arXiv \"assembler\" \"optimizer\" LLM"
}
```
**Tool result** `web_search` (id `call-a16215ab-7b4c-4a99-b58e-e5816b0dec22`, 6,838 characters):

```
Search results for "context engineering survey arXiv "assembler" "optimizer" LLM" (searched 2026-11-26):

[1] [2507.13334] A Survey of Context Engineering for Large Language Models
URL: https://arxiv.org/abs/2507.13334
Excerpt: > Abstract:The performance of Large Language Models (LLMs) is fundamentally determined by the contextual information provided during inference. This survey introduces Context Engineering, a formal discipline that transcends simple prompt design to encompass the systematic optimization of information payloads for LLMs. We present a comprehensive taxonomy decomposing Context Engineering into its foundational components and the sophisticated implementations that integrate them into intelligent [...] into intelligent systems. We first examine the foundational components: context retrieval and generation, context processing and context management. We then explore how these components are architecturally integrated to create sophisticated system implementations: retrieval-augmented generation (RAG), memory systems and tool-integrated reasoning, and multi-agent systems. Through this systematic analysis of over 1400 research papers, our survey not only establishes a technical roadmap for the [...] roadmap for the field but also reveals a critical research gap: a fundamental asymmetry exists between model capabilities. While current models, augmented by advanced context engineering, demonstrate remarkable proficiency in understanding complex contexts, they exhibit pronounced limitations in generating equally sophisticated, long-form outputs. Addressing this gap is a defining priority for future research. Ultimately, this survey provides a unified framework for both researchers and

[2] A Survey of Context Engineering for Large Language Models
URL: https://arxiv.org/html/2507.13334v1
Excerpt: - \ E. Zelikman, Yuhuai Wu, and Noah D. Goodman. Star: Bootstrapping reasoning with reasoning, arXiv preprint arXiv:2203.14465, 2022. URL 
- \ E. Zelikman, Eliana Lorch, Lester Mackey, and A. Kalai. Self-taught optimizer (stop): Recursively self-improving code generation, arXiv preprint arXiv:2310.02304, 2023. URL [...] - \ Sanchit Sinha, Yuguang Yue, Victor Soto, Mayank Kulkarni, Jianhua Lu, and Aidong Zhang. Maml-en-llm: Model agnostic meta-training of llms for improved in-context learning. Knowledge Discovery and Data Mining, 2024.
- \ Colin Sisate, Alistair Goldfinch, Vincent Waterstone, Sebastian Kingsley, and Mariana Blackthorn. Contextually entangled gradient mapping for optimized llm comprehension, arXiv preprint arXiv:2502.00048, 2025. URL [...] - \ M. Ferrag, Norbert Tihanyi, and M. Debbah. From llm reasoning to autonomous ai agents: A comprehensive review, arXiv preprint arXiv:2504.19678, 2025. URL 
- \ M. Ferrag, Norbert Tihanyi, and M. Debbah. Reasoning beyond limits: Advances and open problems for llms, arXiv preprint arXiv:2503.22732, 20252. URL

[3] Medium
URL: https://medium.com/@adnanmasood/a-practitioners-take-on-a-survey-of-context-engineering-for-large-language-models-49ac87d23a1e
Excerpt: Member-only story

# A Practitioner’s Take on ‘A Survey of Context Engineering for Large Language Models’

## Context Engineering as the new performance lever. A practitioner’s tour of a 1,400‑paper synthesis that formalizes how we retrieve, process, and manage information for LLMs — spanning a unified taxonomy (retrieval/generation, processing, management) through full systems (RAG, memory, tool‑use, multi‑agent) — and why the real bottleneck isn’t model size but the context pipeline. [...] > TL;DR — The authors formalize Context Engineering — the discipline of designing, optimizing, and orchestrating what goes into an LLM’s context — and present a unified taxonomy from core components (retrieval/generation, processing, management) to full systems (RAG, memory, tool‑use, multi‑agent). They synthesize 1,400+ papers, highlight a critical “comprehension → generation” gap, and show today’s evaluations expose large performance shortfalls (e.g., GAIA 15% for AI vs 92% human), calling

[4] Agentic Context Engineering: Evolving Contexts for Self-ImprovingLanguage Models
URL: https://arxiv.org/html/2510.04618v1
Excerpt: ACE optimizes LLM contexts for both offline and online adaptation through an agentic context engineering framework. To ensure fairness, we use the same LLM for the Generator, Reflector, and Curator (non-thinking mode of DeepSeek-V3.1 \), preventing knowledge transfer from a stronger Reflector or Curator to a weaker Generator. This isolates the benefit of context construction itself. We adopt a batch size of 1 (constructing a delta context from each sample). We set the maximum number of [...] #### MIPROv2 \.

MIPROv2 is a popular prompt optimizer for LLM applications that works by jointly optimizing system instructions and in-context demonstrations via bayesian optimization. We use the official DSPy implementation \, setting `auto="heavy"` to maximize optimization performance.

#### GEPA \. [...] Context adaptation (or context engineering) refers to methods that improve model behavior by constructing or modifying inputs to an LLM, rather than altering its weights. The current state of the art leverages natural language feedback \[40, 54, 4]. In this paradigm, a language model inspects the current context along with signals such as execution traces, reasoning steps, or validation results, and generates natural language feedback on how the context should be revised. This feedback is then

[5] RAG Is Dead. Long Live Context Engineering for LLM Systems
URL: https://www.callstack.com/blog/rag-is-dead-long-live-context-engineering-for-llm-systems
Excerpt: In my experience working on such systems, these technologies are combined with embedding models and orchestration layers to build scalable RAG pipelines capable of supporting millions or billions of vectors.

## From Retrieval to Context Engineering

Modern LLM system design is gradually shifting from heavy retrieval pipelines toward context engineering—the practice of carefully constructing the information and constraints provided to the model at runtime. [...] Instead of building a full pipeline for document chunking, embedding generation, vector database storage, similarity search, reranking, and prompt assembly, we can design a system that relies on deterministic preprocessing, intelligently structured context injection, a single model API call, and schema enforcement through guardrails. [...] Context engineering includes techniques such as schema enforcement, structured system prompts, metadata injection, tool usage constraints, API-level orchestration, and deterministic preprocessing pipelines that prepare relevant information before it reaches the model.

Here’s a simplified example of what structured context injection looks like in practice:
```
**Tool result** `read_url` (id `call-ed7647cc-920d-4c1a-9290-0d19b798e204`, 5,315 characters):

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

_Model call: 20,388 input tokens, 670 output tokens_

**Tool call** `web_search` (id `call-c072f719-616a-4580-9990-98927293e769`):

```json
{
  "query": "\"context assembler\" \"context optimizers\" context engineering framework"
}
```
**Tool call** `read_url` (id `call-db4018dd-f666-4e23-9bcd-f3b724edc2de`):

```json
{
  "url": "https://paulfruiful.com",
  "start": 0
}
```
**Tool result** `web_search` (id `call-c072f719-616a-4580-9990-98927293e769`, 6,830 characters):

```
Search results for ""context assembler" "context optimizers" context engineering framework" (searched 2026-11-26):

[1] Why Context Assembly Replaces Prompt Engineering | Stop pretending prompt engineering scales. · community · Discussion #188556 · GitHub
URL: https://github.com/orgs/community/discussions/188556
Excerpt: matters most. The assembler selects the N most relevant pieces of context using relevance scoring, not just recency. Our `relevance = importance  (0.95 ^ days_since_stored)` formula ensures recent events don't automatically dominate over important older ones.  3. Working layer (current conversation turns): Progressive compaction applies here. Full text for recent turns, structured summaries for older turns, one-line digests for ancient sessions.  The key insight: context assembly is an [...] | This framing is exactly right. Prompt engineering assumes a static context. Context assembly acknowledges that the context is dynamic — assembled from memory, tools, prior turns, and the current task — and that assembly decisions directly determine cost and quality.  The paradigm shift: instead of "write better prompts," the question becomes "what should be in context for this specific turn?" and "what can be safely excluded without losing quality?"  From production experience building agent [...] building agent systems, context assembly has three layers:  1. Static layer (system instructions, agent personality, tool schemas): This should be as compact as possible. Every byte here pays a tax on every turn. We regularly audit and compress our system instructions — went from 2,400 tokens to 800 tokens with no quality loss by removing examples and verbose explanations.  2. Dynamic layer (relevant memory, retrieved context, user history): This is where smart assembly matters most. The

[2] Optimizing any AI Agent Framework with Context Engineering
URL: https://medium.com/@bijit211987/optimizing-any-ai-agent-framework-with-context-engineering-81ceb09176a0
Excerpt: Build modular microservices for each context layer (identity, task, knowledge, memory).
   Use a Context Orchestrator class to assemble and blend context dynamically.
   Easily integrates with LangChain or custom agent stacks like Flask.

### 2. Context Memory Architectures [...] Context Inheritance: Strip and pass only what’s needed
   Context Transformation: Convert raw outputs to structured inputs
   Validation Gates: Prevent garbage from cascading forward

In LangChain, implement with Runnable Passthrough + middleware functions.

## Measure Context Engineering ROI

Traditional metrics won’t cut it. Use context-aware KPIs:

## Context Efficiency [...] [Initialization State] → [Discovery State] → [Execution State] → [Validation State]

Each state has tailored context strategy:

   _Initialization_: Minimal instructions, open-ended
   _Discovery_: Load FAQs, search tools
   _Execution_: Reduce memory, maximize tool accuracy
   _Validation_: Inject prior interactions, logs

Frameworks like CrewAI or AutoGen? This fits like a glove.  
 LangChain? Build it using Runnable Sequence and custom memory.

## Beyond Token Management

[3] Context Engineering Guide for Developers
URL: https://www.faros.ai/blog/context-engineering-for-developers
Excerpt: The ACE framework addresses this with "incremental delta updates." Instead of regenerating contexts in full, it produces compact updates that are merged into existing context. This prevents what researchers call "context collapse," where iterative rewriting gradually erodes important details.

### 3. Order context by importance

Where information appears in your context window dramatically affects whether the AI uses it correctly. [...] The ACE (Agentic Context Engineering) framework from Stanford demonstrates this division well. Their system uses separate roles: a Generator that produces code, a Reflector that extracts lessons from successes and failures, and a Curator that integrates insights into structured context updates. This modular approach, where different components handle generation, evaluation, and curation, mirrors how human teams actually work. [...] TL;DR: Context engineering is the practice of giving AI coding agents the right information, in the right structure, at the right time. It goes beyond prompt engineering to include codebase context, dependencies, git history, team standards, tools, and documentation. The goal is not to maximize context, but to make it more relevant and usable. Effective context engineering relies on five core strategies: selection, compression, ordering, isolation, and format optimization, helping agents

[4] Context engineering explained: What every AI developer should know
URL: https://www.youtube.com/watch?v=BBPQYtR7oUk
Excerpt: is between context engineering versus prompt engineering. So prompt engineering is how you write and structure instructions examples and constraints. It's still very relevant. And useful, but context engineering is how you assemble everything that the model will see at runtime, like the right tools, the right facts, the right history, and the right format. It's dynamic and happens before every model call. So it's pretty powerful. Think of the model like a brain with a limited short term memory. [...] # Context engineering explained: What every AI developer should know

White-paper on context engineering →  
More info on context engineering →  

Context Engineering: Why writing bigger prompts won't fix your AI, and what to do instead. In this video, Smitha Kolan explains what context engineering is, how it's different from prompt engineering, and gives you a practical step-by-step framework to build smarter, more reliable AI agents. [...] projects. We'll road test it on a tiny but realistic agent, show you where context usually fall apart, and give you a checklist on how to fix them really fast. Context engineering is the craft of deciding exactly what the model should see and what it shouldn't. At each step, it includes your system, message tools, retrieved facts, short term notes. Long term memories. Format rules and also recent history. If prompt engineering is how you word the ask, then context engineering is everything. You

[5] Context Engineering Guide | Prompt Engineering Guide<!-- -->
URL: https://www.promptingguide.ai/guides/context-engineering-guide
Excerpt: In other words, what you are trying to achieve in context engineering is optimizing the information you are providing in the context window of the LLM. This also means filtering out noisy information, which is a science on its own, as it requires systematically measuring the performance of the LLM.

Everyone is writing about context engineering, but here we are going to walk you through a concrete example of what context engineering looks like when building AI agents.
```
**Tool result** `read_url` (id `call-db4018dd-f666-4e23-9bcd-f3b724edc2de`, 4,856 characters):

```
Title: Paul Fruitful

URL Source: https://paulfruiful.com/

Markdown Content:
Paul Fruitful🚀

![Image 1](https://paulfruiful.com/)

Turning Your Ideas Into Reality I help individuals and businesses bring their creative ideas to life with expert development and tailored solutions.

![Image 2: Paul Fruitful in action](https://paulfruiful.com/images/image.png)

Over the years, I’ve honed a wide range of skills, including AI, Backend engineering, Machine learning, Cloud computing, Networking, Frontend development, Programming, and Pentesting. I specialize in digitizing manual workflows, automating complex processes, and seamlessly integrating AI into virtually anything. If there’s a better, smarter way to get things done, I’ll find it – and build it.

The Origin Story At 9 years old, I discovered computers – it was love at first click. While other kids were out playing tag, I was learning how to code, dismantling gadgets (sorry, Mom 😂), and figuring out how technology ticks. Fast forward to now, at 17, I’ve spent over half my life immersed in the tech world. It’s been a wild ride of curiosity, building, and exploring what’s possible. 
[Experience](https://docs.google.com/document/d/1SKwfXXKFM6pAZsfavUJISUI1vec6fyjC/edit?usp=sharing&ouid=117179366278903408671&rtpof=true&sd=true)[Projects](https://paulfruiful.com/)

## Sharing, Speaking, and Sparking Ideas

Beyond building, I’m passionate about sharing knowledge. Through my blog, YouTube channel, and newsletter, I connect with fellow tech enthusiasts, offering tips, guides, and resources to empower the community. Whether it’s breaking down complex concepts or providing actionable insights, I’m here to help others grow while having a good laugh along the way.

![Image 3](https://paulfruiful.com/images/work.gif)

### Featured Events

![Image 4: Paul Fruitful](https://paulfruiful.com/images/pfp.jpg)

From inspiring discussions to insightful sessions, I’ve had the privilege of speaking at transformative events across the globe.

## How I Can Help You

I provide a wide range of services to help turn your ideas into reality.

Pick a service let's get started

### AI Engineering

Build An AI-powered software, intelligent agents, for seamless AI integrations.

[Get It Done](https://api.whatsapp.com/send/?phone=2348107279245&text=Hello%20Paul%20Fruitful%20I%20am%20in%20need%20of%20your%20AI%20Engineering%20service&type=phone_number&app_absent=0)

### MVP Development

Get scalable MVPs quickly, and launch your ideas in no time.

[Get It Done](https://api.whatsapp.com/send/?phone=2348107279245&text=Hello%20Paul%20Fruitful%20I%20am%20in%20need%20of%20your%20MVP%20development%20service&type=phone_number&app_absent=0)

### App Development

Get robust web, mobile, and desktop applications tailored to your needs.

[Get It Done](https://api.whatsapp.com/send/?phone=2348107279245&text=Hello%20Paul%20Fruitful%20I%20am%20in%20need%20of%20your%20App%20Development%20service&type=phone_number&app_absent=0)

### SAAS Development

Turn your ideas into software-as-a-service platforms that scale.

[Get It Done](https://api.whatsapp.com/send/?phone=2348107279245&text=Hello%20Paul%20Fruitful%20I%20am%20in%20need%20of%20your%20SAAS%20development%20service&type=phone_number&app_absent=0)

### Backend Engineering

Get robust APIs and scalable backend systems to power your applications.

[Get It Done](https://api.whatsapp.com/send/?phone=2348107279245&text=Hello%20Paul%20Fruitful%20I%20am%20in%20need%20of%20your%20Backend%20Engineering%20service&type=phone_number&app_absent=0)

### Automation

Create workflows and automates processes to make life easier and more efficient for yourself.

[Get It Done](https://api.whatsapp.com/send/?phone=2348107279245&text=Hello%20Paul%20Fruitful%20I%20am%20in%20need%20of%20your%20Automation%20service&type=phone_number&app_absent=0)

Your vision deserves more than just staying in your mind. With a simple call, I’ll show you how your idea can be transformed and be birthed into a thriving reality 🤰

Ready to make your next move? Let’s take your idea from concept to completion together.

[Start With A Call](https://calendly.com/techtasktechnologies/30min)

## My Outlets

![Image 5: Newsletter Cover](https://paulfruiful.com/images/news.webp)

## Becoming a More Than Average Developer

Join my newsletter to learn how to elevate your development career beyond the ordinary. Discover practical tips, unique insights, and expert advice to help you stand out in the software engineering field.

![Image 6: Featured Blog: Load Balancers](https://paulfruiful.com/images/geometric.jpeg)

## Solution Developer

Dive into my technical blog, where I share in-depth articles on software engineering, development practices, and cutting-edge technology topics.

[View Blog →](https://solutiondev.hashnode.dev/load-balancers-the-concept-of-proxies)

```

## Turn 7

_Model call: 23,719 input tokens, 3,509 output tokens_

**Tool call** `assess_credibility` (id `call-a890e2e2-0435-417b-8a0a-d1828e5593c9`):

```json
{
  "evaluation": {
    "source_url": "https://medium.com/@fruitful2007/prompt-engineering-is-dead-introducing-context-engineering-6280c075a1a9",
    "source_type": "personal_blog",
    "author": {
      "name": "Paul Fruitful (Medium handle @fruitful2007)",
      "credentials": "Medium About page describes him only as \"a versatile result-oriented Software Engineer & tech content creator with close to a decade of experience\" (https://medium.com/@fruitful2007/about). No employer, degree, publication record or verifiable professional affiliation is given. His personal site (https://paulfruiful.com) sells freelance AI/backend/app development services and states \"at 17, I've spent over half my life immersed in the tech world\", which sits oddly with the Medium bio's \"close to a decade of experience\" and suggests he is a self-taught teenage developer/consultant rather than a researcher or established practitioner. His Medium profile has 62 followers; posts are general AI/software commentary. I found no academic publications, conference talks or institutional affiliation under his name.",
      "credibility_assessment": "Some relevant background as a working software developer writing about AI agents, but no research credentials, no evidence of peer-reviewed or editor-checked work, and a self-description on his own site that conflicts with the professional framing in his Medium bio. Expertise is asserted, not demonstrated, so the author gives little independent reason to trust the technical claims."
    },
    "publication": {
      "name": "Medium (self-published post on the author's personal profile)",
      "reputation": "Medium is a large open blogging platform where anyone can publish; posts on a personal profile (medium.com/@handle/...) are not vetted by an editorial desk or by peer review. Medium applies platform rules, moderation and curation/\"Boost\" decisions, but no fact-checking of individual posts. This post appears on the author's own profile, not in an edited Medium publication. I searched for the article title and the author's name; the only results were his own profile, his personal site and other unrelated Medium posts with similar titles — no sign of editorial oversight or of the piece being cited as a reference elsewhere.",
      "editorial_process": "self_published"
    },
    "content_analysis": {
      "claims_checked": [
        {
          "claim": "Prompt engineering is dead and is being replaced by context engineering.",
          "status": "contradicted",
          "evidence": "Credible practitioner and industry sources say prompting is still relevant but no longer sufficient on its own, i.e. it is subsumed rather than dead: the Prompt Engineering Guide's Context Engineering Guide (https://www.promptingguide.ai/guides/context-engineering-guide) and a widely cited essay, \"The Death of Prompt Engineering Has Been Greatly Exaggerated\" (https://imjaredz.com/writing/the-death-of-prompt-engineering-has-been-greatly-exaggerated.html). Karpathy's own post frames context engineering as an addition to, not the death of, prompting (https://x.com/karpathy/status/1937902205765607626). The article itself concedes mid-text that \"prompt engineering is a part of context engineering\", which undercuts its own headline."
        },
        {
          "claim": "Context engineering is a superset of prompt engineering: it is about shaping the whole context window rather than a single prompt.",
          "status": "corroborated",
          "evidence": "This is the mainstream framing. Karpathy's June 2025 X post (https://x.com/karpathy/status/1937902205765607626) and LangChain's context engineering write-up (https://www.langchain.com/blog/context-engineering-for-agents) describe context engineering as the umbrella covering system prompts, tools, retrieved data, memory and history. The arXiv survey \"A Survey of Context Engineering for Large Language Models\" (https://arxiv.org/abs/2507.13334) formalizes the same idea, as does https://www.honeyhive.ai/learn/context-engineering-vs-prompt-engineering."
        },
        {
          "claim": "Andrej Karpathy defines context engineering as \"the art of filling in the context window with the right information so that the LLM knows what's next\" (quoted twice, in two slightly different wordings).",
          "status": "contradicted",
          "evidence": "The primary source is Karpathy's X post of 25 June 2025: \"context engineering is the delicate art and science of filling the context window with just the right information for the next step\" (https://x.com/karpathy/status/1937902205765607626). Multiple independent write-ups quote that wording: https://www.honeyhive.ai/learn/context-engineering-vs-prompt-engineering, https://www.langchain.com/blog/context-engineering-for-agents, https://pureai.com/articles/2025/09/23/karpathy-puts-context-at-the-core-of-ai-coding.aspx. The article's quotation marks therefore present a paraphrase as a direct quote, and gives no link to the post."
        },
        {
          "claim": "Context engineering has \"mathematical foundations\" consisting of an assembler function that assembles all context components and optimizer functions that find the best context.",
          "status": "no_evidence_found",
          "evidence": "The article states this without a single citation, formula or link, and hedges immediately (\"ignore the word salads, the confusing grammar, all the fancy scientific terms\"). I searched for a source using this \"assembler / optimizer\" framework (\"context assembler\" \"context optimizers\" context engineering framework) and found only blog posts and a GitHub discussion (https://github.com/orgs/community/discussions/188556, https://medium.com/@bijit211987/optimizing-any-ai-agent-framework-with-context-engineering-81ceb09176a0) — nothing that establishes this as the field's mathematical formalization. The closest serious formal treatment I found, the arXiv survey (https://arxiv.org/abs/2507.13334), uses a different taxonomy (retrieval/generation, processing, management) and I did not find the assembler/optimizer terminology there."
        }
      ],
      "claims_supported_by_evidence": false,
      "sources_cited": false,
      "corroborated_by_other_sources": true,
      "contradicted_by_other_sources": true,
      "primary_vs_secondary": "tertiary_source",
      "funding_or_sponsorship": "Not found. Medium posts carry no funding disclosure; the author's personal site (https://paulfruiful.com) sells AI engineering, MVP, app, SaaS, backend and automation services and solicits clients via WhatsApp and Calendly, and the article ends by promoting a \"context bank\" tool he says he will release as open source — so the piece doubles as self-promotion. No advertiser, sponsor or employer is disclosed.",
      "bias_and_tone": "Informal, hype-adjacent and heavily rhetorical: headline capitalised (\"PROMPT ENGINEERING IS DEAD\"), emoji, jokes, repeated assertions (\"Context! Context! Context!\", \"the truth is\" four times) and an explicit \"My honest take\". It is opinion/commentary rather than reporting; no counterarguments, no limitations and no data are offered, and the anthropomorphic framing (\"the context window is the mind of the LLM\", \"building worlds inside LLMs\") is metaphor presented as explanation. There is a commercial interest: the post advertises the author's services and an unreleased product of his own.",
      "date_published": "Published 21 July 2025 (\"Jul 21, 2025\"; page metadata 2025-07-21T00:17:53Z). No last-updated date shown. As of 26 November 2026 the post is about 16 months old in a fast-moving field; the terminology still matches current usage, but the article contains no dated examples, model references or updates, and the \"prompt engineering is dead\" framing is dated relative to how the industry now describes the relationship."
    },
    "transparency_score": 2,
    "overall_credibility": "low",
    "reasoning": "The author is identifiable (name, photo, Medium About page, personal site) and the post is dated, which is worth something, but nothing else supports it. It is a self-published Medium post on a personal profile: no editorial or peer review, no references, no data, and no link even to the one external authority it leans on. Its central quotation of Andrej Karpathy is misworded — the actual X post says \"the delicate art and science of filling the context window with just the right information for the next step\" (https://x.com/karpathy/status/1937902205765607626) — and the author's \"mathematical foundations / assembler and optimizer functions\" claim is asserted with no citation and could not be matched to any source I found. The headline claim that prompt engineering is \"dead\" is contradicted by credible sources that describe prompting as still necessary but no longer sufficient. Its one solid idea, that context engineering is the broader umbrella containing prompt engineering, is corroborated by Karpathy, LangChain, HoneyHive and an arXiv survey — but the article adds no evidence of its own beyond that, and it doubles as marketing for the author's consulting services and an unreleased tool. Author credentials are asserted (\"close to a decade of experience\") rather than verifiable, and his own site describes him as 17 years old. For an academic report this is a low-credibility source: useful at best as an example of popular discourse on a term, not as support for technical claims.",
    "evidence_urls": [
      "https://medium.com/@fruitful2007/prompt-engineering-is-dead-introducing-context-engineering-6280c075a1a9",
      "https://medium.com/@fruitful2007",
      "https://medium.com/@fruitful2007/about",
      "https://paulfruiful.com",
      "https://x.com/karpathy/status/1937902205765607626",
      "https://www.langchain.com/blog/context-engineering-for-agents",
      "https://www.honeyhive.ai/learn/context-engineering-vs-prompt-engineering",
      "https://arxiv.org/abs/2507.13334",
      "https://pureai.com/articles/2025/09/23/karpathy-puts-context-at-the-core-of-ai-coding.aspx",
      "https://ai4ra.uidaho.edu/from-prompt-engineering-to-context-engineering",
      "https://www.promptingguide.ai/guides/context-engineering-guide",
      "https://imjaredz.com/writing/the-death-of-prompt-engineering-has-been-greatly-exaggerated.html",
      "https://github.com/orgs/community/discussions/188556",
      "https://medium.com/@bijit211987/optimizing-any-ai-agent-framework-with-context-engineering-81ceb09176a0"
    ]
  }
}
```
**Tool result** `assess_credibility` (id `call-a890e2e2-0435-417b-8a0a-d1828e5593c9`, 10,610 characters):

```
{
  "status": "evaluation_recorded",
  "evaluation": {
    "source_url": "https://medium.com/@fruitful2007/prompt-engineering-is-dead-introducing-context-engineering-6280c075a1a9",
    "source_type": "personal_blog",
    "author": {
      "name": "Paul Fruitful (Medium handle @fruitful2007)",
      "credentials": "Medium About page describes him only as \"a versatile result-oriented Software Engineer & tech content creator with close to a decade of experience\" (https://medium.com/@fruitful2007/about). No employer, degree, publication record or verifiable professional affiliation is given. His personal site (https://paulfruiful.com) sells freelance AI/backend/app development services and states \"at 17, I've spent over half my life immersed in the tech world\", which sits oddly with the Medium bio's \"close to a decade of experience\" and suggests he is a self-taught teenage developer/consultant rather than a researcher or established practitioner. His Medium profile has 62 followers; posts are general AI/software commentary. I found no academic publications, conference talks or institutional affiliation under his name.",
      "credibility_assessment": "Some relevant background as a working software developer writing about AI agents, but no research credentials, no evidence of peer-reviewed or editor-checked work, and a self-description on his own site that conflicts with the professional framing in his Medium bio. Expertise is asserted, not demonstrated, so the author gives little independent reason to trust the technical claims."
    },
    "publication": {
      "name": "Medium (self-published post on the author's personal profile)",
      "reputation": "Medium is a large open blogging platform where anyone can publish; posts on a personal profile (medium.com/@handle/...) are not vetted by an editorial desk or by peer review. Medium applies platform rules, moderation and curation/\"Boost\" decisions, but no fact-checking of individual posts. This post appears on the author's own profile, not in an edited Medium publication. I searched for the article title and the author's name; the only results were his own profile, his personal site and other unrelated Medium posts with similar titles — no sign of editorial oversight or of the piece being cited as a reference elsewhere.",
      "editorial_process": "self_published"
    },
    "content_analysis": {
      "claims_checked": [
        {
          "claim": "Prompt engineering is dead and is being replaced by context engineering.",
          "status": "contradicted",
          "evidence": "Credible practitioner and industry sources say prompting is still relevant but no longer sufficient on its own, i.e. it is subsumed rather than dead: the Prompt Engineering Guide's Context Engineering Guide (https://www.promptingguide.ai/guides/context-engineering-guide) and a widely cited essay, \"The Death of Prompt Engineering Has Been Greatly Exaggerated\" (https://imjaredz.com/writing/the-death-of-prompt-engineering-has-been-greatly-exaggerated.html). Karpathy's own post frames context engineering as an addition to, not the death of, prompting (https://x.com/karpathy/status/1937902205765607626). The article itself concedes mid-text that \"prompt engineering is a part of context engineering\", which undercuts its own headline."
        },
        {
          "claim": "Context engineering is a superset of prompt engineering: it is about shaping the whole context window rather than a single prompt.",
          "status": "corroborated",
          "evidence": "This is the mainstream framing. Karpathy's June 2025 X post (https://x.com/karpathy/status/1937902205765607626) and LangChain's context engineering write-up (https://www.langchain.com/blog/context-engineering-for-agents) describe context engineering as the umbrella covering system prompts, tools, retrieved data, memory and history. The arXiv survey \"A Survey of Context Engineering for Large Language Models\" (https://arxiv.org/abs/2507.13334) formalizes the same idea, as does https://www.honeyhive.ai/learn/context-engineering-vs-prompt-engineering."
        },
        {
          "claim": "Andrej Karpathy defines context engineering as \"the art of filling in the context window with the right information so that the LLM knows what's next\" (quoted twice, in two slightly different wordings).",
          "status": "contradicted",
          "evidence": "The primary source is Karpathy's X post of 25 June 2025: \"context engineering is the delicate art and science of filling the context window with just the right information for the next step\" (https://x.com/karpathy/status/1937902205765607626). Multiple independent write-ups quote that wording: https://www.honeyhive.ai/learn/context-engineering-vs-prompt-engineering, https://www.langchain.com/blog/context-engineering-for-agents, https://pureai.com/articles/2025/09/23/karpathy-puts-context-at-the-core-of-ai-coding.aspx. The article's quotation marks therefore present a paraphrase as a direct quote, and gives no link to the post."
        },
        {
          "claim": "Context engineering has \"mathematical foundations\" consisting of an assembler function that assembles all context components and optimizer functions that find the best context.",
          "status": "no_evidence_found",
          "evidence": "The article states this without a single citation, formula or link, and hedges immediately (\"ignore the word salads, the confusing grammar, all the fancy scientific terms\"). I searched for a source using this \"assembler / optimizer\" framework (\"context assembler\" \"context optimizers\" context engineering framework) and found only blog posts and a GitHub discussion (https://github.com/orgs/community/discussions/188556, https://medium.com/@bijit211987/optimizing-any-ai-agent-framework-with-context-engineering-81ceb09176a0) — nothing that establishes this as the field's mathematical formalization. The closest serious formal treatment I found, the arXiv survey (https://arxiv.org/abs/2507.13334), uses a different taxonomy (retrieval/generation, processing, management) and I did not find the assembler/optimizer terminology there."
        }
      ],
      "claims_supported_by_evidence": false,
      "sources_cited": false,
      "corroborated_by_other_sources": true,
      "contradicted_by_other_sources": true,
      "primary_vs_secondary": "tertiary_source",
      "funding_or_sponsorship": "Not found. Medium posts carry no funding disclosure; the author's personal site (https://paulfruiful.com) sells AI engineering, MVP, app, SaaS, backend and automation services and solicits clients via WhatsApp and Calendly, and the article ends by promoting a \"context bank\" tool he says he will release as open source — so the piece doubles as self-promotion. No advertiser, sponsor or employer is disclosed.",
      "bias_and_tone": "Informal, hype-adjacent and heavily rhetorical: headline capitalised (\"PROMPT ENGINEERING IS DEAD\"), emoji, jokes, repeated assertions (\"Context! Context! Context!\", \"the truth is\" four times) and an explicit \"My honest take\". It is opinion/commentary rather than reporting; no counterarguments, no limitations and no data are offered, and the anthropomorphic framing (\"the context window is the mind of the LLM\", \"building worlds inside LLMs\") is metaphor presented as explanation. There is a commercial interest: the post advertises the author's services and an unreleased product of his own.",
      "date_published": "Published 21 July 2025 (\"Jul 21, 2025\"; page metadata 2025-07-21T00:17:53Z). No last-updated date shown. As of 26 November 2026 the post is about 16 months old in a fast-moving field; the terminology still matches current usage, but the article contains no dated examples, model references or updates, and the \"prompt engineering is dead\" framing is dated relative to how the industry now describes the relationship."
    },
    "transparency_score": 2,
    "overall_credibility": "low",
    "reasoning": "The author is identifiable (name, photo, Medium About page, personal site) and the post is dated, which is worth something, but nothing else supports it. It is a self-published Medium post on a personal profile: no editorial or peer review, no references, no data, and no link even to the one external authority it leans on. Its central quotation of Andrej Karpathy is misworded — the actual X post says \"the delicate art and science of filling the context window with just the right information for the next step\" (https://x.com/karpathy/status/1937902205765607626) — and the author's \"mathematical foundations / assembler and optimizer functions\" claim is asserted with no citation and could not be matched to any source I found. The headline claim that prompt engineering is \"dead\" is contradicted by credible sources that describe prompting as still necessary but no longer sufficient. Its one solid idea, that context engineering is the broader umbrella containing prompt engineering, is corroborated by Karpathy, LangChain, HoneyHive and an arXiv survey — but the article adds no evidence of its own beyond that, and it doubles as marketing for the author's consulting services and an unreleased tool. Author credentials are asserted (\"close to a decade of experience\") rather than verifiable, and his own site describes him as 17 years old. For an academic report this is a low-credibility source: useful at best as an example of popular discourse on a term, not as support for technical claims.",
    "evidence_urls": [
      "https://medium.com/@fruitful2007/prompt-engineering-is-dead-introducing-context-engineering-6280c075a1a9",
      "https://medium.com/@fruitful2007",
      "https://medium.com/@fruitful2007/about",
      "https://paulfruiful.com",
      "https://x.com/karpathy/status/1937902205765607626",
      "https://www.langchain.com/blog/context-engineering-for-agents",
      "https://www.honeyhive.ai/learn/context-engineering-vs-prompt-engineering",
      "https://arxiv.org/abs/2507.13334",
      "https://pureai.com/articles/2025/09/23/karpathy-puts-context-at-the-core-of-ai-coding.aspx",
      "https://ai4ra.uidaho.edu/from-prompt-engineering-to-context-engineering",
      "https://www.promptingguide.ai/guides/context-engineering-guide",
      "https://imjaredz.com/writing/the-death-of-prompt-engineering-has-been-greatly-exaggerated.html",
      "https://github.com/orgs/community/discussions/188556",
      "https://medium.com/@bijit211987/optimizing-any-ai-agent-framework-with-context-engineering-81ceb09176a0"
    ]
  }
}
```

## Turn 8

_Model call: 29,614 input tokens, 3,228 output tokens_

**Tool call** `save_report` (id `call-640fd324-2004-401f-b019-7613dad26f6e`):

```json
{
  "filename": "medium-paul-fruitful-prompt-engineering-is-dead.md",
  "markdown": "# Credibility Report: PROMPT ENGINEERING IS DEAD INTRODUCING CONTEXT ENGINEERING\n\n**URL:** https://medium.com/@fruitful2007/prompt-engineering-is-dead-introducing-context-engineering-6280c075a1a9\n**Verdict:** Low credibility\n**Evaluated:** 2026-11-26\n\n## Summary\nThis is a short (7-minute), self-published opinion piece on Medium by Paul Fruitful (@fruitful2007), a software developer and tech content creator, arguing that \"context engineering\" has superseded prompt engineering. It is a personal blog post on the author's own Medium profile, not an edited publication or a peer-reviewed article: it cites no sources, links no studies and presents no data, even for its claim that the field has \"mathematical foundations\" built on assembler and optimizer functions. Its one solid idea — that context engineering is the broader umbrella containing prompt engineering — matches what Andrej Karpathy, LangChain, HoneyHive and an arXiv survey say, but the article's quotation of Karpathy is not the wording Karpathy actually used, and its headline claim that prompt engineering is \"dead\" is contradicted by credible sources describing prompting as still necessary but no longer sufficient. The author's credentials are asserted in his bio rather than verifiable, and his own website (which sells his consulting services) describes him as 17 years old. The piece also doubles as marketing for his services and an unreleased tool, so it is Low credibility for an academic research report.\n\n## Author\n- **Name as written:** Paul Fruitful (Medium handle `@fruitful2007`), \"he\", 62 followers.\n- **Self-description (Medium About page):** \"a versatile result-oriented Software Engineer & tech content creator with close to a decade of experience, passionate about the future\". No employer, degree, publication record, conference talk or institutional affiliation is listed.\n- **Personal site (https://paulfruiful.com):** a freelance services page selling AI engineering, MVP, app, SaaS, backend and automation work, with WhatsApp/Calendly contact links. It states: \"At 9 years old, I discovered computers… Fast forward to now, at 17, I've spent over half my life immersed in the tech world.\" That self-description sits awkwardly with the Medium bio's \"close to a decade of experience\" and suggests a self-taught teenage developer rather than an established practitioner or researcher.\n- **Other work:** posts on AI industry commentary (\"The AI Wild West Era Is Coming To An End\", \"AI Sovereignty: Who Controls The Weights?\", \"Agentic Engineering: Goodbye To Building Slop Software\") — general commentary, no specialist track record on context engineering.\n- **What I checked:** the Medium About page, his profile post list, and a search for his name with \"Medium AI writer\", which returned only his own profile, his personal site and unrelated posts.\n\n## Publication\n- **Name:** Medium — a post on the author's personal profile (`medium.com/@handle/...`), not inside an edited Medium publication.\n- **Editorial process:** self-published. Anyone can post; Medium applies platform rules, moderation and curation/\"Boost\" decisions, but does not fact-check individual posts and does not operate a corrections desk for them.\n- **Reputation:** Medium is a mainstream, widely used blogging platform, but the platform's credibility does not transfer to an individual unchecked post. The article carries no references section, no editor's note and no disclosure of who funds the author.\n- **What I checked:** the article page itself, the author's profile and About page, and searches for the article title and the author's name (no evidence the piece is cited elsewhere or reviewed by anyone).\n\n## Claims Checked\n\n| Claim | Status | Evidence |\n|---|---|---|\n| Prompt engineering is \"dead\" and is being replaced by context engineering. | **Contradicted** | Credible sources describe prompting as still necessary but no longer sufficient, i.e. subsumed rather than dead: the Prompt Engineering Guide's context engineering guide (https://www.promptingguide.ai/guides/context-engineering-guide) and \"The Death of Prompt Engineering Has Been Greatly Exaggerated\" (https://imjaredz.com/writing/the-death-of-prompt-engineering-has-been-greatly-exaggerated.html). Karpathy's own post presents context engineering as an addition to prompting (https://x.com/karpathy/status/1937902205765607626). The article itself later concedes \"prompt engineering is a part of context engineering\", which undercuts its headline. |\n| Context engineering is a superset of prompt engineering: it means shaping the whole context window (instructions, tools, memory, data) rather than one prompt. | **Corroborated** | Karpathy's June 2025 post (https://x.com/karpathy/status/1937902205765607626); LangChain's context engineering write-up (https://www.langchain.com/blog/context-engineering-for-agents); HoneyHive's comparison page (https://www.honeyhive.ai/learn/context-engineering-vs-prompt-engineering); the arXiv survey \"A Survey of Context Engineering for Large Language Models\" (https://arxiv.org/abs/2507.13334). |\n| Andrej Karpathy defines context engineering as \"the art of filling in the context window with the right information so that the LLM knows what's next\" (quoted twice, in two slightly different wordings). | **Contradicted** (misquotation) | The primary source, Karpathy's X post of 25 June 2025, reads: \"context engineering is the delicate art and science of filling the context window with just the right information for the next step\" (https://x.com/karpathy/status/1937902205765607626). Independent write-ups quote that wording: https://www.honeyhive.ai/learn/context-engineering-vs-prompt-engineering, https://www.langchain.com/blog/context-engineering-for-agents, https://pureai.com/articles/2025/09/23/karpathy-puts-context-at-the-core-of-ai-coding.aspx, https://ai4ra.uidaho.edu/from-prompt-engineering-to-context-engineering. The gist is similar, but the words inside quotation marks are not Karpathy's, no link is given, and the two \"quotes\" differ from each other. |\n| Context engineering has \"mathematical foundations\": an assembler function that assembles every context component, and optimizer functions that find the best context. | **No evidence found** | Asserted with no citation, formula or link, and immediately hedged (\"ignore the word salads, the confusing grammar, all the fancy scientific terms\"). A search for this exact framework (\"context assembler\" \"context optimizers\" context engineering framework) returned only blog posts and a GitHub discussion (https://github.com/orgs/community/discussions/188556, https://medium.com/@bijit211987/optimizing-any-ai-agent-framework-with-context-engineering-81ceb09176a0) — nothing establishing it as the field's formalization. The serious survey I found (https://arxiv.org/abs/2507.13334) uses a different taxonomy (retrieval/generation, processing, management). |\n\n## Bias and Tone\n- **Tone:** informal, conversational and hype-adjacent. The headline is capitalised (\"PROMPT ENGINEERING IS DEAD\"), with emoji (\"😕\", \"😂\"), jokes, repetition (\"Context! Context! Context!\", \"the truth is\" used repeatedly) and a section titled \"My honest take\".\n- **Purpose:** commentary and opinion, not reporting or explanation of evidence. No counterarguments, limitations, failure cases or numbers are given; technical-sounding claims (\"vector embedding space\", \"assembler function\", \"optimizer functions\") are asserted rather than demonstrated, and the anthropomorphic framing (\"the context window is the mind of the LLM\", \"building worlds inside LLMs\") is metaphor presented as explanation.\n- **Commercial interest:** the author uses the post to advertise an unreleased \"context bank\" system of his own (\"I'll release it in a few weeks… It'll be open source too. So stay tuned\") and his personal site sells AI/software development services. No sponsor, employer or funding source is disclosed.\n\n## Currency\n- **Published:** 21 July 2025 (shown as \"Jul 21, 2025\"; page metadata `2025-07-21T00:17:53Z`).\n- **Last updated:** not shown.\n- **Currency as of 2026-11-26:** about 16 months old in a fast-moving field. The terminology still matches current usage, but the post has no dated examples, model versions or updates, and its \"prompt engineering is dead\" framing reads as dated relative to how the industry now describes the relationship (prompting embedded within context engineering). Nothing on the page indicates it was revised after publication.\n\n## Structured Assessment\n\n| Field | Assessment |\n|---|---|\n| **Source type** | personal_blog |\n| **Author** | Paul Fruitful (@fruitful2007); self-described software engineer/tech content creator; no verifiable credentials, employer or publication record; personal site describes him as 17 and sells his services. |\n| **Author credibility** | Weak: expertise asserted, not demonstrated; bio claim of \"close to a decade of experience\" conflicts with his own site's \"at 17\". |\n| **Publication** | Medium, self-published post on a personal profile. |\n| **Editorial process** | self_published (no editor review, no peer review, no fact-checking). |\n| **Sources cited** | No. No references, links, data or named documents anywhere in the post. |\n| **Claims supported by evidence in the source** | No. |\n| **Primary vs secondary** | Tertiary — a summary/commentary on a term popularised by others, with no original research. |\n| **Corroborated by other sources** | Yes, for the \"context engineering is the umbrella containing prompt engineering\" idea only. |\n| **Contradicted by other sources** | Yes — the \"prompt engineering is dead\" headline, and the wording of the Karpathy quotation. |\n| **Funding / sponsorship** | Not found. Post promotes the author's own forthcoming tool and his paid services; no disclosure. |\n| **Bias and tone** | Opinionated, hype-driven, self-promotional; no counterarguments or limitations. |\n| **Date published** | 21 July 2025; no update date; ~16 months old as of 26 Nov 2026. |\n| **Transparency score** | 2 / 5 — author identity is clear, but production method and funding are not disclosed and no sources are given. |\n| **Overall credibility** | Low |\n\n## Can I cite this?\n**Find a better source.** Do not cite this post for technical or factual claims about context engineering, and definitely not for the Karpathy definition — quote Karpathy's own post instead (https://x.com/karpathy/status/1937902205765607626), or use LangChain's write-up (https://www.langchain.com/blog/context-engineering-for-agents), the Prompt Engineering Guide (https://www.promptingguide.ai/guides/context-engineering-guide), or the peer-reviewed-style survey on arXiv (https://arxiv.org/abs/2507.13334) for the definitional and technical content.\n\nIf you must use it, cite it **only with care** as an example of popular/practitioner discourse — e.g. \"as a widely circulated Medium explainer puts it…\" — and only for the uncontroversial claim that context engineering is now framed as the broader discipline containing prompt engineering. Do not cite it for the \"prompt engineering is dead\" framing (credible sources disagree), for the claimed \"mathematical foundations\" (unsupported and unverifiable), or for the Karpathy quotation (misquoted). Also be aware that the piece is self-promotional and that the author's stated credentials are unverifiable.\n\n## Sources Consulted\n1. https://medium.com/@fruitful2007/prompt-engineering-is-dead-introducing-context-engineering-6280c075a1a9 — the source itself (full text read; no citations, no author bio beyond byline, no update date).\n2. https://medium.com/@fruitful2007 — author's Medium profile and post list (62 followers; general AI/software commentary).\n3. https://medium.com/@fruitful2007/about — author's About page with the \"close to a decade of experience\" bio.\n4. https://paulfruiful.com — author's personal site: freelance services for sale; states \"at 17, I've spent over half my life immersed in the tech world\".\n5. https://x.com/karpathy/status/1937902205765607626 — Karpathy's 25 June 2025 post, the primary source for the quote the article misattributes.\n6. https://www.langchain.com/blog/context-engineering-for-agents — industry write-up confirming context engineering as the umbrella term and quoting Karpathy correctly.\n7. https://www.honeyhive.ai/learn/context-engineering-vs-prompt-engineering — comparison page quoting Karpathy's actual wording and explaining scope.\n8. https://arxiv.org/abs/2507.13334 — \"A Survey of Context Engineering for Large Language Models\": formal treatment; different taxonomy from the article's \"assembler/optimizer\" claim.\n9. https://pureai.com/articles/2025/09/23/karpathy-puts-context-at-the-core-of-ai-coding.aspx — news write-up quoting Karpathy's actual wording.\n10. https://ai4ra.uidaho.edu/from-prompt-engineering-to-context-engineering — university-hosted explainer on the term's mid-2025 rise and Karpathy's wording.\n11. https://www.promptingguide.ai/guides/context-engineering-guide — Prompt Engineering Guide: prompting still relevant; context engineering is about optimizing what is in the window.\n12. https://imjaredz.com/writing/the-death-of-prompt-engineering-has-been-greatly-exaggerated.html — counterargument that prompt engineering is evolving rather than dying.\n13. https://github.com/orgs/community/discussions/188556 — practitioner discussion of context assembly; no formal \"assembler/optimizer\" framework.\n14. https://medium.com/@bijit211987/optimizing-any-ai-agent-framework-with-context-engineering-81ceb09176a0 — another blog post on context assembly; not a scholarly source for the \"mathematical foundations\" claim.\n"
}
```
**Tool result** `save_report` (id `call-640fd324-2004-401f-b019-7613dad26f6e`, 99 characters):

```
Saved the report to reports/medium-paul-fruitful-prompt-engineering-is-dead.md (13,625 characters).
```

## Turn 9

_Model call: 32,879 input tokens, 199 output tokens_

**Assistant:**

**Verdict: Low credibility.** The source is a self-published opinion post on the author's personal Medium profile (Paul Fruitful, @fruitful2007) with no citations, no data and no editorial oversight; its one defensible idea — that context engineering is the broader umbrella containing prompt engineering — matches Karpathy, LangChain, HoneyHive and an arXiv survey, but its headline "prompt engineering is dead" is contradicted by credible sources, its direct quotation of Karpathy does not match his actual X post, and its claim about "mathematical foundations" (assembler/optimizer functions) could not be traced to any source. The author's credentials are asserted rather than verifiable, and his own services site describes him as 17 and sells his consulting work, so the piece is also self-promotional. The report has been saved as `reports/medium-paul-fruitful-prompt-engineering-is-dead.md`.


## Final output

**Verdict: Low credibility.** The source is a self-published opinion post on the author's personal Medium profile (Paul Fruitful, @fruitful2007) with no citations, no data and no editorial oversight; its one defensible idea — that context engineering is the broader umbrella containing prompt engineering — matches Karpathy, LangChain, HoneyHive and an arXiv survey, but its headline "prompt engineering is dead" is contradicted by credible sources, its direct quotation of Karpathy does not match his actual X post, and its claim about "mathematical foundations" (assembler/optimizer functions) could not be traced to any source. The author's credentials are asserted rather than verifiable, and his own services site describes him as 17 and sells his consulting work, so the piece is also self-promotional. The report has been saved as `reports/medium-paul-fruitful-prompt-engineering-is-dead.md`.

## Summary

- Turns (model calls): 9
- Tool calls: web_search x6, read_url x5, assess_credibility x1, save_report x1
- Tokens: 154,295 input (125,696 cached), 9,020 output
- Estimated cost: $0.0101
- Report: reports/medium-paul-fruitful-prompt-engineering-is-dead.md
- URLs in medium-paul-fruitful-prompt-engineering-is-dead.md not seen in any tool result: none
