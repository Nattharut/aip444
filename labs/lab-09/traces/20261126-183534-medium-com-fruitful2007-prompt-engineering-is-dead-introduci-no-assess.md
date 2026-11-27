# Agent trace: https://medium.com/@fruitful2007/prompt-engineering-is-dead-introducing-context-engineering-6280c075a1a9

- Model: `deepseek/deepseek-v4.1-flash-1017`
- Started: 2026-11-26T18:35:34
- Max turns: 25
- Tools: read_url, web_search, save_report


**User:** Evaluate the credibility of this source: https://medium.com/@fruitful2007/prompt-engineering-is-dead-introducing-context-engineering-6280c075a1a9

## Turn 1

_Model call: 2,345 input tokens, 94 output tokens_

**Assistant:**

I'll start by reading the source page.

**Tool call** `read_url` (id `chatcmpl-tool-9507addb03c0a7e1`):

```json
{
  "url": "https://medium.com/@fruitful2007/prompt-engineering-is-dead-introducing-context-engineering-6280c075a1a9",
  "start": 0
}
```
**Tool result** `read_url` (id `chatcmpl-tool-9507addb03c0a7e1`, 10,096 characters):

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

_Model call: 4,742 input tokens, 93 output tokens_

**Tool call** `read_url` (id `chatcmpl-tool-809f552c210e4edd`):

```json
{
  "url": "https://medium.com/@fruitful2007/prompt-engineering-is-dead-introducing-context-engineering-6280c075a1a9",
  "start": 10000
}
```
**Tool result** `read_url` (id `chatcmpl-tool-809f552c210e4edd`, 362 characters):

```
using grammar, all the fancy scientific terms.

Context engineering is just providing and structuring the right information inside the context window of agents using basically prompts.

And the truth is: You probably do this every day with ChatGPT😂  
That’s it for this article.  
Thank you for reading


[End of page. Showed characters 10,000-10,303 of 10,303.]
```

## Turn 3

_Model call: 4,926 input tokens, 308 output tokens_

**Tool call** `web_search` (id `chatcmpl-tool-b680a917677c8b81`):

```json
{
  "query": "\"Paul Fruitful\" Medium writer AI engineer"
}
```
**Tool call** `web_search` (id `chatcmpl-tool-97acabf3f6424c12`):

```json
{
  "query": "Andrej Karpathy \"context engineering\" quote \"art of filling\" context window"
}
```
**Tool result** `web_search` (id `chatcmpl-tool-97acabf3f6424c12`, 7,119 characters):

```
Search results for "Andrej Karpathy "context engineering" quote "art of filling" context window" (searched 2026-11-26):

[1] Andrej Karpathy: "Context engineering is the delicate art and science of filling the context window with just the right information for the next step." This repo breaks it down from first… | Paolo Perrone | 21 comments
URL: https://www.linkedin.com/posts/paoloperrone_andrej-karpathy-context-engineering-is-activity-7410862809904992257-Xx3o
Excerpt: Andrej Karpathy: "Context engineering is the delicate art and science of filling the context window with just the right information for the next step." This repo breaks it down from first principles. 𝗪𝗵𝗮𝘁 𝘆𝗼𝘂'𝗹𝗹 𝗹𝗲𝗮𝗿𝗻: → Token budgets — more tokens = more $ and slower → Few-shot learning — examples > explanations → Memory systems — stateful, coherent agents → RAG — ground responses, reduce hallucination → Control flow — break complex tasks into steps → Context pruning — delete ruthlessly → [...] explanations
→ Memory systems — stateful, coherent agents
→ RAG — ground responses, reduce hallucination
→ Control flow — break complex tasks into steps
→ Context pruning — delete ruthlessly
→ Cognitive tools — IBM Zurich boosted GPT-4.1 by 62% with this
𝗤𝘂𝗶𝗰𝗸 𝘀𝘁𝗮𝗿𝘁:
1️⃣ Read `00\_foundations/01\_atoms\_prompting.md` (5 min)
2️⃣ Run `10\_guides\_zero\_to\_hero/01\_min\_prompt.py`
3️⃣ Explore `20\_templates/minimal\_context.yaml`
4️⃣ Study `30\_examples/00\_toy\_chatbot/` [...] ♻️ Repost if you've hit the limits of prompt engineering. | 21 comments on LinkedIn" name="twitter:description"> explanations
→ Memory systems — stateful, coherent agents
→ RAG — ground responses, reduce hallucination
→ Control flow — break complex tasks into steps
→ Context pruning — delete ruthlessly
→ Cognitive tools — IBM Zurich boosted GPT-4.1 by 62% with this
𝗤𝘂𝗶𝗰𝗸 𝘀𝘁𝗮𝗿𝘁:
1️⃣ Read `00\_foundations/01\_atoms\_prompting.md` (5 min)
2️⃣ Run `10\_guides\_zero\_to\_hero/01\_min\_prompt.py`

[2] From Prompt Engineering to Context Engineering – Artificial Intelligence for Research Administration
URL: https://ai4ra.uidaho.edu/from-prompt-engineering-to-context-engineering
Excerpt: However, in recent conversations around AI and its development a new term has emerged: context engineering. In mid-2025, the term gained traction rapidly after Shopify CEO Tobi Lütke and former OpenAI researcher Andrej Karpathy both endorsed it publicly.

> Karpathy described it as “the delicate art and science of filling the context window with just the right information for the next step.”
>
> Andrej Karpathy [...] All that information, everything the AI can “see” when it generates a response, is called its context. And the maximum size of the context that a model can handle is called its context window. And it turns out that the quality of that context matters far more than the exact phrasing of any single prompt. As Karpathy put it, the shift is from asking smart questions to building smarter environments for the AI to work in. [...] This is what context engineering is: the practice of designing, curating, and managing the full set of information an AI has access to, not just the instruction you type, but the documents, memory, history, examples, and constraints that surround it. If prompt engineering is asking the right question in a meeting, context engineering is making sure everyone walks in having read the same briefing document first.

### Is This Actually New?

[3] Andrej Karpathy on X: "+1 for "context engineering" over "prompt engineering". People associate prompts with short task des…"
URL: https://x.com/karpathy/status/1937902205765607626
Excerpt: People associate prompts with short task descriptions you'd give an LLM in your day-to-day use. When in every industrial-strength LLM app, context engineering is the delicate art and science of filling the context window with just the right information for the next step. Science because doing this right involves task descriptions and explanations, few shot examples, RAG, related (possibly multimodal) data, tools, state and history, compacting... Too little or of the wrong form and the LLM [...] > Quoting @tobi (tobi lutke):
>
> I really like the term “context engineering” over prompt engineering. 
> 
> It describes the core skill better: the art of providing all the context for the task to be plausibly solvable by the LLM.

## People

- @karpathy (Andrej Karpathy)
- @tobi (tobi lutke) — Shopify CEO by day, Dad in evening, hacker at night, Aspiring comprehensivist. [...] form and the LLM doesn't have the right context for optimal performance. Too much or too irrelevant and the LLM costs might go up and performance might come down. Doing this well is highly non-trivial. And art because of the guiding intuition around LLM psychology of people spirits.

[4] Context Engineering
URL: https://www.langchain.com/blog/context-engineering-for-agents
Excerpt: As Andrej Karpathy puts it, LLMs are like a new kind of operating system. The LLM is like the CPU and its context window is like the RAM, serving as the model’s working memory. Just like RAM, the LLM context window has limited capacity to handle various sources of context. And just as an operating system curates what fits into a CPU’s RAM, we can think about “context engineering” playing a similar role. Karpathy summarizes this well: [...] > [Context engineering is the] ”…delicate art and science of filling the context window with just the right information for the next step.”

Context types commonly used in LLM applications

What are the types of context that we need to manage when building LLM applications? Context engineering as an umbrella that applies across a few different context types: [...] Share

## TL;DR

Agents need context to perform tasks. Context engineering is the art and science of filling the context window with just the right information at each step of an agent’s trajectory. In this post, we break down some common strategies — write, select, compress, and isolate — for context engineering by reviewing various popular agents and papers. We then explain how LangGraph is designed to support them!

Also, see our video on context engineering here.

[5] Andrej Karpathy Says 'Agentic Engineering' Is the Next Big Thing - Business Insider
URL: https://www.businessinsider.com/agentic-engineering-andrej-karpathy-vibe-coding-2026-2
Excerpt: "Many people have tried to come up with a better name for this to differentiate it from vibe coding, personally, my current favorite is 'agentic engineering,'" he wrote in a recent X post.

Karpathy said he calls it "agentic engineering" not just because agents are writing the code, but because "there is an art & science and expertise to it." [...] The approach is also threatening traditional engineering jobs. In a Business Insider survey of 167 software engineers, 75 engineers said that they were "keeping up," while 30 said they felt ahead of the curve, and 27 felt behind.

"Vibe coding is now mentioned on my Wikipedia as a major memetic 'contribution,' and even its article is longer. lol," Karpathy wrote on X about its meteoric rise.
```
**Tool result** `web_search` (id `chatcmpl-tool-b680a917677c8b81`, 6,136 characters):

```
Search results for ""Paul Fruitful" Medium writer AI engineer" (searched 2026-11-26):

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

[2] Paul Fruitful on Facebook: "PROMPT ENGINEERING IS DEAD INTRODUCING CONTEXT ENGINEERING THE NEW HYPE So, over time, we’ve been ta…"
URL: https://www.facebook.com/frutful.paul/posts/prompt-engineering-is-dead-introducing-context-engineering-the-new-hype-so-over/1384626395981429
Excerpt: The same thing goes for agents.
When they are birthed, they have foundational knowledge from the training they were given.
But when you give them tasks, they don’t know the world in which those tasks exist.

That is why it is your responsibility, as an AI engineer performing context engineering...
...to engineer the world into the model’s mind. [...] So, it is the responsibility of an AI engineer to provide their agents with enough context.

So,
What’s this context engineering hype?

Prompt engineering was all about crafting the perfect prompts to get outputs and information out of LLMs.
Context engineering seems different.
Context engineering is like a superset of prompt engineering.
This is what context engineering is, as Andrej Karpathy defines it: [...] “Okay, that means I can engineer context with just prompts."
Yes, you can.
Because at the end of the day, you use prompts to engineer context.
But prompt engineering is not context engineering.

Prompt engineering is a part of context engineering.

Prompt engineering kind of acts on the system that your context-engineered environment creates.

So, I dive deeper
The next step, after you create a world inside an agent, is persisted memory.

[3] Paul Fruitful
URL: https://paulfruiful.com
Excerpt: Over the years, I’ve honed a wide range of skills, including AI, Backend engineering, Machine learning, Cloud computing, Networking, Frontend development, Programming, and Pentesting. I specialize in digitizing manual workflows, automating complex processes, and seamlessly integrating AI into virtually anything. If there’s a better, smarter way to get things done, I’ll find it – and build it. [...] I provide a wide range of services to help turn your ideas into reality.

Pick a service let's get started

Build An AI-powered software, intelligent agents, for seamless AI integrations.

Get robust web, mobile, and desktop applications tailored to your needs.

Get robust APIs and scalable backend systems to power your applications.

Create workflows and automates processes to make life easier and more efficient for yourself. [...] Dive into my technical blog, where I share in-depth articles on software engineering, development practices, and cutting-edge technology topics.

Step-by-step strategies, techniques, and coding challenges to help you prepare for technical interviews.

Learn essential mathematical concepts for machine learning, explained and implemented in Python.

[4] Paul Iusztin | AI Engineer, Author & Educator
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

"If it's decodable, Paul will decode it for you." [...] Shaw Talebi

"Working with Paul on the LLM Engineer's Handbook showed me his unique ability to bridge the gap between theoretical AI and modern AI Engineering best practices."

Maxime Labonne

"Paul is one of the rare people who truly understands both the technical depth of AI and how to teach it in a way that's engaging and actually clicks."

Louis-Francois Bouchard

"Paul doesn't just talk about AI - he builds it, and when he talks, it's worth listening."

Maria Vechtomova

[5] He Wrote a Coding Bestseller, Now He Says Don't Code | Paul Iusztin, Founder@Decoding AI
URL: https://www.youtube.com/watch?v=OLt8pZjR-b4
Excerpt: Questions answered:
Who is Paul Iusztin? → Paul Iusztin is a founding AI engineer at a San Francisco startup building vertical AI agents for financial advisors, the author of LLM Engineer's Handbook (~20,000 copies sold), and the creator of Decoding AI — a 40,000-subscriber newsletter on production AI engineering. He works remotely from Portugal and recently launched the Agentic AI Engineering course. [...] ⏱️ Chapters:
0:00 - Why this AI engineer killed RAG, MCP, and agentic loops
1:25 - When does RAG actually make sense
4:30 - Why everyone is using MCP wrong
7:00 - Is vibe coding the future of engineering
9:30 - Why he chose Portugal over San Francisco
12:00 - outro [...] What is the best way to learn AI agent engineering in 2026? → Paul Iusztin's Agentic AI Engineering course covers agent foundations, two capstone projects (deep research agent + writing agent), AI evals, monitoring, and deployment to GCP — built without LangGraph framework dependence so engineers understand what's happening underneath. Prerequisites: Python and basic LLM knowledge. The course assumes you want to build, not theorize.
```

## Turn 4

_Model call: 8,378 input tokens, 378 output tokens_

**Tool call** `read_url` (id `chatcmpl-tool-bee0209f507c872c`):

```json
{
  "url": "https://medium.com/@fruitful2007",
  "start": 0
}
```
**Tool call** `read_url` (id `chatcmpl-tool-a2e4609bc9841d43`):

```json
{
  "url": "https://paulfruiful.com",
  "start": 0
}
```
**Tool result** `read_url` (id `chatcmpl-tool-a2e4609bc9841d43`, 4,856 characters):

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
**Tool result** `read_url` (id `chatcmpl-tool-bee0209f507c872c`, 10,096 characters):

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

_Model call: 13,317 input tokens, 316 output tokens_

**Tool call** `read_url` (id `chatcmpl-tool-a49bb3dd3fe80b0a`):

```json
{
  "url": "https://medium.com/@fruitful2007/about",
  "start": 0
}
```
**Tool call** `web_search` (id `chatcmpl-tool-b0608744e0f114b8`):

```json
{
  "query": "\"prompt engineering is dead\" context engineering debate 2025 experts say still matters"
}
```
**Tool result** `web_search` (id `chatcmpl-tool-b0608744e0f114b8`, 6,477 characters):

```
Search results for ""prompt engineering is dead" context engineering debate 2025 experts say still matters" (searched 2026-11-26):

[1] Prompt Engineering Is Dead. Context Engineering Is What Actually Matters Now.
URL: https://hackernoon.com/prompt-engineering-is-dead-context-engineering-is-what-actually-matters-now
Excerpt: Andrej Karpathy, the former Director of AI at Tesla, founding member of OpenAI, and one of the most respected voices in the field, coined the term "context engineering" in mid-2025 to name this shift. His point: the leverage in modern AI systems has moved from how you phrase the instruction to what information surrounds it.

In 2026, with models that follow instructions reliably, context is the primary variable.

## What Context Engineering Actually Is [...] Understanding context engineering means understanding what you are assembling. There are five layers, and each has its own design decisions.

### Layer 1: The System Prompt Your Persistent Instructions

This is the layer prompt engineering focused on. It still matters. But context engineers think about it differently.

A prompt engineer asks: "what is the best way to instruct this model?" [...] This table captures the relationship clearly: prompt engineering is still part of the picture. It is one layer inside context engineering, the instruction layer. The mistake is thinking that layer is the whole game.

## When Your Problem Is a Context Problem

Most AI application failures that get described as "the model is not following instructions" or "the model keeps hallucinating" are actually context failures. Here is how to diagnose which layer is broken.

[2] Context Engineering vs Prompt Engineering | DataHub
URL: https://datahub.com/blog/context-engineering-vs-prompt-engineering
Excerpt: No. Prompt engineering remains valuable and is still an essential component of working with LLMs effectively. The shift is one of scope, not replacement. Prompt engineering focuses on how you communicate with a model within a given interaction. Context engineering focuses on the system level, managing the full informational environment the model works within. As AI systems grow more complex, prompt engineering becomes one input into a much larger context engineering workflow rather than the [...] 82% of IT and data leaders say prompt engineering alone is no longer sufficient, and 95% say context engineering is important to power AI agents at scale (DataHub’s State of Context Management Report 2026).

The gap most teams miss: Context engineering is only as good as the context it has access to. Without a context management layer that delivers trusted, governed, up-to-date metadata, context engineering is engineering with unreliable inputs.

[3] Prompt Engineering Is Dead, and Context Engineering Is Already Obsolete: Why the Future Is Automated Workflow Architecture with LLMs - Prompting - OpenAI Developer Community
URL: https://community.openai.com/t/prompt-engineering-is-dead-and-context-engineering-is-already-obsolete-why-the-future-is-automated-workflow-architecture-with-llms/1314011
Excerpt: Context engineering helped, but it created new challenges:

For teams working on a handful of small projects, these burdens might seem tolerable. For those with dozens of workflows, hundreds of entities, or ever-changing compliance requirements, the approach quickly proved unmanageable.

Why Context Engineering Is Already Outdated for Serious Practitioners [...] You are absolutely right: the era of prompt and manual context engineering is coming to an end—at least in scalable systems. The idea of atomic tasks, programmable attention, and automated context generation isn’t just logical—it’s necessary. Especially when dealing with high-stakes domains like law, medicine, or analytics.

However, from a clinical perspective, I must highlight a critical nuance. [...] Having built and operated LLM-driven systems in both the legal and technology industries, my experience is that context engineering is simply not sustainable beyond a certain threshold. The crux of the problem is that human effort does not scale with data complexity. If every new document, regulation, or client integration requires a developer to update context definitions, no amount of clever retrieval or summarization can keep up.

[4] Prompt Engineering Is Dead. Long Live Context Engineering. Or is it?
URL: https://medium.com/@naveenmanwani/prompt-engineering-is-dead-long-live-context-engineering-ae2df63b1353
Excerpt: And understanding why matters enormously for your business — because right now, companies are making million-dollar bets on the wrong assumption.

Some are over-investing in prompt optimization when they should be building better context systems. Others are drowning their AI in data while wondering why it can’t follow basic business rules.

> The difference isn’t academic. It’s the difference between competitive advantage and expensive science experiment.

## The Great Misunderstanding

[5] Prompt engineering is dead. Long live context engineering!
URL: https://martech.org/prompt-engineering-is-dead-long-live-context-engineering
Excerpt: And it’s not just feasible—it’s necessary. Because prompt engineering is dead. The future isn’t defined by who can write better prompts. It’s defined by who can embed better logic.

If you own pipeline, brand, content or customer experience, this shift belongs to you. Not to IT. Not to procurement. Not to legal. It is your strategy that will be scaled—or lost—based on what you build now. [...] That’s why the next era of AI doesn’t start with a better prompt. It starts with better design.

Context is the new code.

## Context is king

AI systems that drive outcomes don’t rely on tricks. They rely on knowledge—specifically, your knowledge, structured and made accessible at scale. The shift we’re living through now is not from analog to digital, or manual to automated. It’s from prompting outputs to engineering context for your AI. [...] You don’t get that with a better prompt. You get that with expert-trained AI.

This requires a change in posture: from experimentation to ownership.

The early phase of GenAI was about tool sprawl and tactical wins. Freelancers used free tools, agencies cobbled together assets and teams pasted prompts into interfaces and called it innovation.

It worked—until it didn’t.

Expert-trained models are not models trained on more data. They’re models trained on the correct data.
```
**Tool result** `read_url` (id `chatcmpl-tool-a49bb3dd3fe80b0a`, 5,315 characters):

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

_Model call: 16,544 input tokens, 537 output tokens_

**Tool call** `web_search` (id `chatcmpl-tool-898c7b3ef56d06cd`):

```json
{
  "query": "\"A Survey of Context Engineering for Large Language Models\" assembler optimizer formalization"
}
```
**Tool call** `read_url` (id `chatcmpl-tool-a16c995e7b1ae974`):

```json
{
  "url": "https://medium.com/about",
  "start": 0
}
```
**Tool result** `read_url` (id `chatcmpl-tool-a16c995e7b1ae974`, 2,119 characters):

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
**Tool result** `web_search` (id `chatcmpl-tool-898c7b3ef56d06cd`, 4,924 characters):

```
Search results for ""A Survey of Context Engineering for Large Language Models" assembler optimizer formalization" (searched 2026-11-26):

[1] A Survey of Context Engineering for Large Language Models
URL: https://arxiv.org/html/2507.13334v1
Excerpt: This formalization reveals deeper mathematical principles. The assembly function is a form of Dynamic Context Orchestration, a pipeline of formatting and concatenation operations, , where each function must be optimized for the LLM’s architectural biases (e.g., attention patterns).

The retrieval of knowledge, , can be framed as an Information-Theoretic Optimality problem. The goal is to select knowledge that maximizes the mutual information with the target answer , given the query : [...] The formalization of Context Engineering highlights its fundamental distinctions from traditional prompt engineering. The following table summarizes the key differences. [...] ##### Automated Assembly Optimization

[2] A Survey of Context Engineering for Large Language Models — The Agent Atlas
URL: https://agent-atlas.blackarcindustrial.com/papers/a-survey-of-context-engineering-for-large-language-models
Excerpt: The survey’s motivating claim: if you formalize context as a structured, optimizable object, every one of these problems becomes a tractable engineering target with measurable components you can evaluate and debug independently.

### What’s New (Core Contribution)

This is a survey, so the novelty is conceptual organization rather than a new algorithm. Four genuine contributions:

1. A formal definition of Context Engineering as an optimization problem. [...] ### Build Your Own (Minimal Recipe)

You don’t “build a survey,” but you can build the context engineering layer it formalizes — a reusable assembler + evaluator that 80% captures the value: [...] A survey has no single algorithm, but the assembly function `A` is the one idea every reader should be able to write. Here is the core context-engineering loop the formalism implies — a budget-aware, mutual-information-flavored assembler:

[3] A Comprehensive Technical Review: Deconstructing the “Survey of Context Engineering for Large Language Models” | by Shubham | Medium
URL: https://shubh7.medium.com/a-comprehensive-technical-review-deconstructing-the-survey-of-context-engineering-for-large-d3c09409c4a5
Excerpt: This formalization is not merely an academic exercise; it provides the theoretical underpinning for the entire field of LLM evaluation and benchmarking. The `Reward` function in the optimization problem is the critical link. In practice, this function is implemented through the evaluation metrics and benchmarks discussed later in this report, such as GAIA, WebArena, and MCP-RADAR. These benchmarks provide the tasks ( [...] From this structured perspective, Context Engineering can be defined as a formal optimization problem. The goal is to find the ideal set of context-generating functions — collectively denoted as F={A,Retrieve,Select,…} — that maximizes the expected quality of the LLM’s output for a given distribution of tasks T. The objective function is expressed as : [...] T) and the scoring mechanisms (the `Reward`) needed to measure the effectiveness of a particular set of context-generating functions (F). This creates a formal, scientific feedback loop: engineers build context-engineered systems (F), evaluate their performance on standardized benchmarks (`Reward`), and use the results to systematically improve the systems (`arg max`). This transforms the goal from the vague "getting a good response" to the precise "optimizing a function to maximize a

[4] A Survey of Context Engineering for Large Language Models - Paper Detail
URL: https://deeplearn.org/arxiv/621918/a-survey-of-context-engineering-for-large-language-models
Excerpt: The performance of Large Language Models (LLMs) is fundamentally determinedby the contextual information provided during inference. This survey introducesContext Engineering, a formal discipline that transcends simple prompt designto encompass the systematic optimization of information payloads for LLMs. Wepresent a comprehensive taxonomy decomposing Context Engineering into itsfoundational components and the sophisticated implementations that integratethem into intelligent systems. We first

[5] [2507.13334] A Survey of Context Engineering for Large Language Models
URL: https://arxiv.org/abs/2507.13334
Excerpt: > Abstract:The performance of Large Language Models (LLMs) is fundamentally determined by the contextual information provided during inference. This survey introduces Context Engineering, a formal discipline that transcends simple prompt design to encompass the systematic optimization of information payloads for LLMs. We present a comprehensive taxonomy decomposing Context Engineering into its foundational components and the sophisticated implementations that integrate them into intelligent
```

## Turn 7

_Model call: 18,549 input tokens, 546 output tokens_

**Tool call** `web_search` (id `chatcmpl-tool-8d567252436b98b6`):

```json
{
  "query": "Anthropic \"effective context engineering for AI agents\" prompt engineering natural progression"
}
```
**Tool result** `web_search` (id `chatcmpl-tool-8d567252436b98b6`, 6,691 characters):

```
Search results for "Anthropic "effective context engineering for AI agents" prompt engineering natural progression" (searched 2026-11-26):

[1] Effective context engineering for AI agents \ Anthropic
URL: https://www.anthropic.com/research/effective-context-engineering-for-ai-agents
Excerpt: At Anthropic, we view context engineering as the natural progression of prompt engineering. Prompt engineering refers to methods for writing and organizing LLM instructions for optimal outcomes (see our docs for an overview and useful prompt engineering strategies). Context engineering refers to the set of strategies for curating and maintaining the optimal set of tokens (information) during LLM inference, including all the other information that may land there outside of the prompts. [...] Letting agents navigate and retrieve data autonomously also enables progressive disclosure—in other words, allows agents to incrementally discover relevant context through exploration. Each interaction yields context that informs the next decision: file sizes suggest complexity; naming conventions hint at purpose; timestamps can be a proxy for relevance. Agents can assemble understanding layer by layer, maintaining only what's necessary in working memory and leveraging note-taking strategies [...] An agent running in a loop generates more and more data that could be relevant for the next turn of inference, and this information must be cyclically refined. Context engineering is the art and science of curating what will go into the limited context window from that constantly evolving universe of possible information.

## Why context engineering is important to building capable agents

[2] Raymond de Lacaze on Facebook: "Effective context engineering for AI agents (Anthropic Blog, September 2025) "Context is a critical …"
URL: https://www.facebook.com/groups/3670562573177653/posts/4332375363663034
Excerpt: At Anthropic, we view context engineering as the natural progression of prompt engineering. Prompt engineering refers to methods for writing and organizing LLM instructions for optimal outcomes (see our docs for an overview and useful prompt engineering strategies). Context engineering refers to the set of strategies for curating and maintaining the optimal set of tokens (information) during LLM inference, including all the other information that may land there outside of the prompts. [...] After a few years of prompt engineering being the focus of attention in applied AI, a new term has come to prominence: context engineering. Building with language models is becoming less about finding the right words and phrases for your prompts, and more about answering the broader question of “what configuration of context is most likely to generate our model’s desired behavior?" [...] An agent running in a loop generates more and more data that could be relevant for the next turn of inference, and this information must be cyclically refined. Context engineering is the art and science of curating what will go into the limited context window from that constantly evolving universe of possible information."

[3] Effective Context Engineering for AI Agents: Anthropic's Guide, Read and Highlighted
URL: https://www.youtube.com/watch?v=grs8yPUJ8j0
Excerpt: #ContextEngineering #Anthropic #AIAgents #AIEngineering

### Transcript
[0:00] Prompt engineering is giving way to context engineering. We read Anthropic's guide together and highlight the ideas that matter: why context engineering is the natural progression of prompting, the phenomenon of context rot, the model's finite attention budget, the principle of finding the smallest set of high-signal tokens, and long-horizon techniques like note-taking and sub-agents. [...] Prompt engineering is giving way to context engineering. We read Anthropic's guide together and highlight the ideas that matter: why context engineering is the natural progression of prompting, the phenomenon of context rot, the model's finite attention budget, the principle of finding the smallest set of high-signal tokens, and long-horizon techniques like note-taking and sub-agents.

Enroll in the full course: [...] Topics covered in this video:
Beyond prompt engineering
Context rot and the attention budget
The smallest set of high-signal tokens
Notes, compaction, and sub-agents

Instructor: Standarity

This video provides a comprehensive overview of the key concepts, frameworks, and implementation steps covered in the full Udemy course. Whether you're preparing for certification or looking to implement best practices in your organization, this preview will give you a solid foundation.

[4] State of Context Engineering in 2026 | by Kushal Banda | Towards AI
URL: https://pub.towardsai.net/state-of-context-engineering-in-2026-cf92d010eab1
Excerpt: Anthropic frames it well: context engineering means finding the smallest possible set of high-signal tokens that maximise the likelihood of desired outcomes. The discipline covers everything that lands in the context window: system instructions, tool definitions, MCP resources, retrieved documents, conversation history, and accumulated action history. [...] # State of Context Engineering in 2026

Context Engineering has gone from a niche concern to the core discipline of AI Engineering in under a year. In mid-2025, two posts laid much of the groundwork. Manus shared lessons from rebuilding their agent framework four times (July 2025). Anthropic followed with their guide on effective context engineering for agents (September 2025). That was eight months ago. The patterns they described have since matured and were adopted across platforms. [...] Agent Skills are the standard implementation. A skill is a markdown file with YAML frontmatter. The platform reads only the name and description at startup (~80 tokens median per skill). When the model determines a skill is relevant, the full instruction body loads (275 to 8,000 tokens). Supporting scripts and reference materials load only during execution. The format was released by Anthropic in December 2025 and adopted by OpenAI, Google, GitHub, and Cursor within weeks.

[5] Medium
URL: https://medium.com/data-science-collective/context-is-the-new-prompt-why-context-engineering-is-shaping-the-future-of-ai-46eb062ed270
Excerpt: Sitemap

Open in app

Sign in

Write

Search

Sign in

## Data Science Collective

·

Data Science Collective

Advice, insights, and ideas from the Medium data science community

Member-only story

Context Engineering

Large Language Models

AI Agent

Prompt Engineering

Generative Ai Tools

# Context Is the New Prompt: Why Anthropic’s Context Engineering Could Play a Transformative Role
```

## Turn 8

_Model call: 20,443 input tokens, 3,754 output tokens_

**Tool call** `save_report` (id `chatcmpl-tool-b225e494303f8e5f`):

```json
{
  "filename": "medium-paul-fruitful-context-engineering.md",
  "markdown": "# Credibility Report: PROMPT ENGINEERING IS DEAD INTRODUCING CONTEXT ENGINEERING\n\n**URL:** https://medium.com/@fruitful2007/prompt-engineering-is-dead-introducing-context-engineering-6280c075a1a9\n**Verdict:** Low credibility\n**Evaluated:** 2026-11-26\n\n## Summary\nThis is a self-published opinion/explainer post on Medium by \"Paul Fruitful,\" a personal account with 62 followers and no editorial oversight, posted on 21 July 2025. The post argues that \"context engineering\" (shaping the whole context window) is a superset of prompt engineering, that it is \"just a fancy word\" for something practitioners already do, and that it has \"mathematical foundations\" in assembler and optimizer functions. The general framing is broadly consistent with what authoritative sources (Anthropic, LangChain, an arXiv survey) say, but the post supplies **no citations at all**: it quotes Andrej Karpathy in quotation marks using wording that does not match Karpathy's actual post, and it presents the \"assembler/optimizer\" idea without naming the paper it evidently comes from. It also mixes opinion, hype and promotion of the author's own forthcoming side project, and its technical description of how a context window works is loose. It is a readable blog take, not a reliable source for facts or definitions.\n\n## Author\n- Byline: **Paul Fruitful** (Medium handle `@fruitful2007`), posted 21 Jul 2025, \"7 min read\".\n- Medium About page bio: \"I'm Paul Fruitful, a versatile result-oriented Software Engineer & tech content creator with close to a decade of experience, passionate about the future.\" The profile shows **62 followers, 10 following**, and no employer, institution, publication or credential.\n- His personal site (https://paulfruiful.com) is a **freelance services landing page** selling AI engineering, MVP/app/SaaS development, backend and automation work, plus a newsletter. It states: \"At 9 years old, I discovered computers… Fast forward to now, at 17, I've spent over half my life immersed in the tech world.\" That self-description (a teenage self-taught developer) sits awkwardly with the Medium bio's \"close to a decade of experience\" in a professional sense, and neither claim is independently verifiable.\n- He writes frequently on AI topics on Medium (e.g., \"Agentic Engineering: Goodbye To Building Slop Software\", \"AI Sovereignty: Who Controls The Weights?\"), so he is consistent on topic, but there is **no evidence of research output, industry affiliation, or recognised expertise** in LLM systems. Searches for his name surfaced his own properties (Medium, personal site, a Facebook repost of the same article) and unrelated people (e.g., AI engineer Paul Iusztin) — no third-party profile, interviews or citations of his work.\n\n## Publication\n- **Medium** is an open self-publishing platform. Its own About page says \"anyone can share knowledge and wisdom with the world\" (https://medium.com/about). Individual posts are **not editorially reviewed, fact-checked or peer reviewed**; there is no editorial policy or corrections process behind this article beyond Medium's general content rules.\n- The host is therefore a platform, not a publisher with standards that vouch for this piece. Credibility has to rest entirely on the author and on whether the claims check out.\n- No funding or conflict-of-interest disclosure on the page (Medium's revenue model is memberships; the page also contains a newsletter sign-up prompt).\n\n## Claims Checked\n\n| Claim | Status | Evidence |\n|---|---|---|\n| Karpathy defines context engineering as: *\"It's the art of filling in the context window with the right information so that the LLM knows what's next\"* (presented in quotation marks) | **Partly corroborated / misquoted** | Karpathy did publicly endorse the term, but his actual wording is: \"context engineering is the delicate art and science of filling the context window with just the right information for the next step\" — https://x.com/karpathy/status/1937902205765607626 (also quoted by https://www.anthropic.com/research/effective-context-engineering-for-ai-agents and https://www.langchain.com/blog/context-engineering-for-agents). The article gives *two different* versions of the \"quote\" in the same post, both in quotation marks, and neither matches the original. It also links to nothing. |\n| Context engineering is a superset of prompt engineering; prompt engineering is a part of it | **Corroborated** | Anthropic: \"we view context engineering as the natural progression of prompt engineering… Context engineering refers to the set of strategies for curating and maintaining the optimal set of tokens (information) during LLM inference\" — https://www.anthropic.com/research/effective-context-engineering-for-ai-agents. LangChain uses context engineering as the umbrella over prompt-level concerns — https://www.langchain.com/blog/context-engineering-for-agents. arXiv survey: \"a formal discipline that transcends simple prompt design\" — https://arxiv.org/abs/2507.13334 |\n| Context engineering has \"mathematical foundations\" — an \"assembler function\" and \"optimizer functions\" for finding the best context | **Corroborated in substance, but uncited** | The framing matches *A Survey of Context Engineering for Large Language Models* (arXiv, 18 July 2025), which formalises context as an optimisation problem with assembly/retrieval/selection functions — https://arxiv.org/html/2507.13334v1. The article names no paper, author or link, so a reader cannot trace the claim. |\n| Headline: \"PROMPT ENGINEERING IS DEAD\" (i.e., prompt engineering is obsolete) | **Contradicted (overstated)** | Anthropic frames context engineering as a *progression* in which prompt engineering remains a component, not a replacement — https://www.anthropic.com/research/effective-context-engineering-for-ai-agents. DataHub's explainer answers the same question \"No. Prompt engineering remains valuable and is still an essential component\" — https://datahub.com/blog/context-engineering-vs-prompt-engineering. The article's own body also contradicts its headline (\"Prompt engineering is a part of context engineering\"), so the title is clickbait framing. |\n| Technical description: the context window \"just keeps the generated 'next' tokens to fill up the empty space inside the window\", and tokens in it \"exist in a vector embedding space\" | **Not supported / imprecise** | Anthropic and LangChain describe the context window as the set of tokens available at inference — system prompt, tool definitions, retrieved documents, history, tool results — not as generated tokens filling empty space, and prompt tokens are not literally stored as a persistent \"vector embedding space\". No source states the article's version; treat it as an inaccurate simplification rather than a citable technical statement. |\n| Claim that he is building a \"context bank\" to share context across agents, to be released open source \"in a few weeks\" | **Not checked / unverifiable** | No public release, repo or follow-up found in searches. It functions as a teaser/promotion inside the article. |\n\n## Bias and Tone\n- **Tone:** informal, jokey, heavily first-person, with emoji (\"overperform your disappointment 😂\", \"personal preference 😅\"), rhetorical questions and short one-line paragraphs. It reads like a social-media post, not a technical explainer.\n- **Framing:** explicitly hype-aware (\"THE NEW HYPE\", \"It's just a fancy word\"), which is a reasonable angle, but the piece repeatedly asserts things without evidence and slides between opinion and fact without signalling which is which (\"the truth is…\", \"the truth is…\").\n- **Commercial interest:** the author plugs his own upcoming \"context bank\" tool (\"I'll release it in a few weeks… It'll be open source too. So stay tuned\"), and his personal site sells AI engineering services; the article also carries a newsletter sign-up. Mild self-promotion, not concealed, but it is a promotional surface rather than a neutral explainer.\n- **Balance:** no counterarguments, no limitations of context engineering, no engagement with the \"prompt engineering is dead\" backlash, no names of researchers or systems, no links.\n- **Transparency:** no sources, no funding note, no corrections policy, no stated expertise on the topic.\n\n## Currency\n- **Published:** 21 July 2025 (Medium timestamp `2025-07-21T00:17:53Z`). No \"last updated\" date shown.\n- As of 2026-11-26 the piece is roughly **16 months old**, in a field that moved quickly after it: Anthropic's guide on context engineering for agents (Sept 2025), agent \"skills\"/progressive-disclosure patterns (Dec 2025), and a much larger body of formal and practical work on context management. The article's concepts are not wrong for their date, but a student writing in late 2026 should not rely on a July 2025 hot take for the current state of the field.\n\n## Can I cite this?\n**Find a better source — or cite it only as an example of the discourse, with care.**\n\n- **Don't cite it for facts or definitions.** The Karpathy quotation is not accurate, nothing is referenced, and the technical explanation of the context window is loose. If you want the definition of context engineering, cite the primary sources directly: Karpathy's post (https://x.com/karpathy/status/1937902205765607626), Anthropic's guide (https://www.anthropic.com/research/effective-context-engineering-for-ai-agents), LangChain's post (https://www.langchain.com/blog/context-engineering-for-agents), and the survey (https://arxiv.org/abs/2507.13334).\n- **Acceptable use:** if your report is *about* the \"prompt engineering is dead\" hype cycle or how practitioners talk about context engineering, you can cite this as one illustrative example of a self-published practitioner blog post — label it as such (\"a Medium blog post by a freelance developer\"), note the date, and do not present its claims as established findings.\n- **If you must cite a specific claim from it**, cite the underlying source instead (Karpathy, Anthropic, the arXiv survey) and check the wording against the original yourself — never copy the article's quoted text.\n- Not suitable for a literature review, a definition, or any statement of fact about how LLMs process context.\n\n## Sources Consulted\n1. https://medium.com/@fruitful2007/prompt-engineering-is-dead-introducing-context-engineering-6280c075a1a9 — the source itself (read in full, both parts); byline, date, content, no citations, self-promotion.\n2. https://medium.com/@fruitful2007 — author's Medium profile; 62 followers, post list, no credentials.\n3. https://medium.com/@fruitful2007/about — author bio (\"close to a decade of experience\"), no institutional affiliation.\n4. https://paulfruiful.com — author's personal site; freelance AI/dev services, states he is 17, newsletter.\n5. https://medium.com/about — Medium describes itself as a place where \"anyone can share knowledge\"; confirms self-publishing with no editorial review.\n6. https://x.com/karpathy/status/1937902205765607626 — Karpathy's actual post defining context engineering (verbatim wording differs from the article's \"quote\").\n7. https://www.anthropic.com/research/effective-context-engineering-for-ai-agents — authoritative framing: context engineering as the \"natural progression\" of prompt engineering; description of the context window.\n8. https://www.langchain.com/blog/context-engineering-for-agents — context engineering as umbrella over prompt-level work; repeats Karpathy's actual wording.\n9. https://arxiv.org/abs/2507.13334 and https://arxiv.org/html/2507.13334v1 — survey formalising context engineering (assembly/retrieval/selection functions), the likely origin of the article's \"assembler/optimizer\" claim.\n10. https://datahub.com/blog/context-engineering-vs-prompt-engineering — vendor explainer answering \"No\" to \"is prompt engineering dead\"; contradicts the headline framing.\n11. https://ai4ra.uidaho.edu/from-prompt-engineering-to-context-engineering — university-hosted explainer confirming the term's mid-2025 uptake via Lütke and Karpathy, with the accurate Karpathy quotation.\n12. https://hackernoon.com/prompt-engineering-is-dead-context-engineering-is-what-actually-matters-now — another self-published post on the same theme; used only to show the framing is a common blog trope, not as evidence.\n"
}
```
**Tool result** `save_report` (id `chatcmpl-tool-b225e494303f8e5f`, 92 characters):

```
Saved the report to reports/medium-paul-fruitful-context-engineering.md (12,269 characters).
```

## Turn 9

_Model call: 24,231 input tokens, 215 output tokens_

**Assistant:**

**Verdict: Low credibility.** The source is a self-published opinion post on Medium (a platform where "anyone can share knowledge," with no editorial review) by Paul Fruitful, a freelance developer with 62 followers and no verifiable expertise on LLM systems, who also uses the piece to tease his own upcoming side project. Its central idea — context engineering as a superset of prompt engineering — does line up with Anthropic, LangChain and an arXiv survey, but the post cites nothing, presents a paraphrased Andrej Karpathy remark in quotation marks as if verbatim (in two different versions), and describes the context window in a technically loose way; its "PROMPT ENGINEERING IS DEAD" headline is contradicted even by its own body text. Use it only as an example of practitioner hype discourse, and cite Karpathy's actual post, Anthropic's guide or the arXiv survey for the substance. The report was saved as `reports/medium-paul-fruitful-context-engineering.md`.


## Final output

**Verdict: Low credibility.** The source is a self-published opinion post on Medium (a platform where "anyone can share knowledge," with no editorial review) by Paul Fruitful, a freelance developer with 62 followers and no verifiable expertise on LLM systems, who also uses the piece to tease his own upcoming side project. Its central idea — context engineering as a superset of prompt engineering — does line up with Anthropic, LangChain and an arXiv survey, but the post cites nothing, presents a paraphrased Andrej Karpathy remark in quotation marks as if verbatim (in two different versions), and describes the context window in a technically loose way; its "PROMPT ENGINEERING IS DEAD" headline is contradicted even by its own body text. Use it only as an example of practitioner hype discourse, and cite Karpathy's actual post, Anthropic's guide or the arXiv survey for the substance. The report was saved as `reports/medium-paul-fruitful-context-engineering.md`.

## Summary

- Turns (model calls): 9
- Tool calls: read_url x6, web_search x5, save_report x1
- Tokens: 113,475 input (89,088 cached), 6,241 output
- Estimated cost: $0.0077
- Report: reports/medium-paul-fruitful-context-engineering.md
- URLs in medium-paul-fruitful-context-engineering.md not seen in any tool result: none
