# Agent trace: https://www.canada.ca/en/government/system/digital-government/digital-government-innovations/responsible-use-ai/generative-ai/guide-use-generative-ai.html

- Model: `deepseek/deepseek-v4.1-flash-1017`
- Started: 2026-11-26T18:28:35
- Max turns: 25
- Tools: read_url, web_search, assess_credibility, save_report


**User:** Evaluate the credibility of this source: https://www.canada.ca/en/government/system/digital-government/digital-government-innovations/responsible-use-ai/generative-ai/guide-use-generative-ai.html

## Turn 1

_Model call: 4,681 input tokens, 100 output tokens_

**Assistant:**

I'll start by reading the source page.

**Tool call** `read_url` (id `call_fc4cf57452944e71baa21af6`):

```json
{
  "url": "https://www.canada.ca/en/government/system/digital-government/digital-government-innovations/responsible-use-ai/generative-ai/guide-use-generative-ai.html",
  "start": 0
}
```
**Tool result** `read_url` (id `call_fc4cf57452944e71baa21af6`, 10,096 characters):

```
Title: Guide on the use of generative artificial intelligence

URL Source: https://www.canada.ca/en/government/system/digital-government/digital-government-innovations/responsible-use-ai/generative-ai/guide-use-generative-ai.html

Published Time: Wed, 28 Oct 2026 12:12:12 GMT

Markdown Content:
## On this page

*   [Overview](https://www.canada.ca/en/government/system/digital-government/digital-government-innovations/responsible-use-ai/generative-ai/guide-use-generative-ai.html#toc-1)
*   [What is generative AI?](https://www.canada.ca/en/government/system/digital-government/digital-government-innovations/responsible-use-ai/generative-ai/guide-use-generative-ai.html#toc-2)
*   [Challenges and opportunities](https://www.canada.ca/en/government/system/digital-government/digital-government-innovations/responsible-use-ai/generative-ai/guide-use-generative-ai.html#toc-3)
*   [Recommended approach](https://www.canada.ca/en/government/system/digital-government/digital-government-innovations/responsible-use-ai/generative-ai/guide-use-generative-ai.html#toc-4)
*   [Policy considerations and best practices](https://www.canada.ca/en/government/system/digital-government/digital-government-innovations/responsible-use-ai/generative-ai/guide-use-generative-ai.html#toc-5)
*   [Use of this guide](https://www.canada.ca/en/government/system/digital-government/digital-government-innovations/responsible-use-ai/generative-ai/guide-use-generative-ai.html#toc-6)
*   [Additional support](https://www.canada.ca/en/government/system/digital-government/digital-government-innovations/responsible-use-ai/generative-ai/guide-use-generative-ai.html#toc-7)
*   [Frequently asked questions](https://www.canada.ca/en/government/system/digital-government/digital-government-innovations/responsible-use-ai/generative-ai/guide-use-generative-ai.html#toc-8)

## Overview

Generative artificial intelligence (AI) tools offer many potential benefits to Government of Canada (GC) institutions. Federal institutions should explore potential uses of generative AI tools for supporting and improving their operations, but they should not use these tools in all cases. Institutions must be cautious and evaluate the risks before they start using them. They should also limit the use of these tools to instances where they can manage the risks effectively.

This document provides guidance to federal institutions on their use of generative AI tools. This includes instances where federal institutions are deploying these tools. It provides an overview of generative AI, identifies challenges relating to its use, puts forward principles for using it responsibly, and offers policy considerations and best practices.

This guide also seeks to raise awareness and foster coordination among federal institutions. It highlights the importance of engaging key stakeholders before deploying generative AI tools for public use and before using them for purposes such as service delivery.

Stakeholders include:

*   legal counsel
*   privacy and security experts
*   the Office of the Chief Information Officer at the Treasury Board of Canada Secretariat (TBS)
*   bargaining agents
*   advisory groups
*   clients of GC services

The guide complements and supports compliance with many existing federal laws and policies, including those in the areas of privacy, security, intellectual property, and human rights.

This second version of the guide incorporates feedback from internal stakeholders and external experts.

It will be updated regularly to keep pace with regulatory and technological change.

To support public servants considering the use of these tools in their daily work, a [concise summary of this guide](https://www.canada.ca/en/government/system/digital-government/digital-government-innovations/responsible-use-ai/generative-ai-your-daily-work.html) offering do’s and don’ts is also available.

## What is generative AI?

The [_Directive on Automated Decision-Making_](https://www.tbs-sct.canada.ca/pol/doc-eng.aspx?id=32592) defines AI as information technology that performs tasks that would ordinarily require biological brainpower to accomplish, such as making sense of spoken language, learning behaviours or solving problems.

Generative AI is a type of AI that produces content such as text, audio, code, videos and images. [Footnote 1](https://www.canada.ca/en/government/system/digital-government/digital-government-innovations/responsible-use-ai/generative-ai/guide-use-generative-ai.html#fn1) This content is produced based on information the user inputs, called a “prompt,” which is typically a short instructional text.

Examples of generative AI tools:

*   large language models (LLMs) such as ChatGPT, Copilot and LLaMA
*   GitHub Copilot and FauxPilot, which produce code based on text prompts
*   DALL-E, Midjourney and Stable Diffusion, which produce images from text or image prompts

These examples include both proprietary and open-source models. Both types have their own benefits and drawbacks in terms of cost, performance, scalability, security, transparency and user support.

In addition, generative AI models can be fine-tuned, or custom models can be trained and deployed to meet an organization’s needs. [Footnote 2](https://www.canada.ca/en/government/system/digital-government/digital-government-innovations/responsible-use-ai/generative-ai/guide-use-generative-ai.html#fn2)

Many generative AI models have been trained on large volumes of data, including publicly accessible data from the Internet. Based on the training data, these models generate content that is statistically likely in response to a prompt, [Footnote 3](https://www.canada.ca/en/government/system/digital-government/digital-government-innovations/responsible-use-ai/generative-ai/guide-use-generative-ai.html#fn3) for example, by predicting the next word in a sentence. Techniques such as human supervision and reinforcement learning can also be applied to further improve the outputs, [Footnote 3](https://www.canada.ca/en/government/system/digital-government/digital-government-innovations/responsible-use-ai/generative-ai/guide-use-generative-ai.html#fn3) and users can provide feedback or modify their prompt to refine the response. Generative AI can therefore produce content that looks as though a human produced it.

Generative AI can be used to perform or support tasks such as:

*   writing and editing documents and emails
*   generating images for presentations
*   coding tasks, such as debugging and generating templates and common solutions
*   summarizing information
*   brainstorming
*   research, translation and learning
*   providing support to clients (for example, answering questions, troubleshooting)

## Challenges and opportunities

Before federal institutions start using generative AI tools, they must assess and mitigate certain ethical, legal and other risks. For example, these tools can generate inaccurate content; amplify biases; and violate intellectual property, privacy and other laws. Further, some tools may not meet federal privacy and security requirements. When institutions use these tools, they must protect personal information and sensitive data. As well, because these tools generate content that can look as though a human produced it, people might not be able to tell whether they are interacting with a person or a tool. The use of these tools can also affect the skill and judgment of public servants and can have environmental costs. The development and quality assurance practices of some generative AI models have also been associated with socio‑economic harms such as exploitative labour practices. [Footnote 4](https://www.canada.ca/en/government/system/digital-government/digital-government-innovations/responsible-use-ai/generative-ai/guide-use-generative-ai.html#fn4) For example, data‑labelling or annotation requires extensive manual input, and this work is often outsourced to countries where workers are paid very low wages. [Footnote 5](https://www.canada.ca/en/government/system/digital-government/digital-government-innovations/responsible-use-ai/generative-ai/guide-use-generative-ai.html#fn5)

Generative AI tools rely on models that pose various challenges, including limited transparency and explainability. They also rely on training data that is difficult to access and assess. These challenges stem in part from large model sizes, high volumes of training data, and the proprietary nature of many tools. In addition, the outputs of the models are constrained by the prompts users enter and by the training data, which may lack context that is not publicly accessible on the Internet.

Training data could also be outdated. For example, ChatGPT-3.5 is trained on data up to early 2022, so it has a limited ability to provide information on events or developments after that. [Footnote 6](https://www.canada.ca/en/government/system/digital-government/digital-government-innovations/responsible-use-ai/generative-ai/guide-use-generative-ai.html#fn6)[Footnote 7](https://www.canada.ca/en/government/system/digital-government/digital-government-innovations/responsible-use-ai/generative-ai/guide-use-generative-ai.html#fn7) Training data can also be biased and lack a diversity of views, given that the Internet is frequently the data source. These biases can then be reflected in the outputs of the tools.

The performance of these tools can also vary from language to language. Models in English and other languages that are well represented in the training data often perform better than models in languages that are less well represented. [Footnote 8](https://www.canada.ca/en/government/system/digital-government/digital-government-innovations/responsible-use-ai/generative-ai/guide-use-generative-ai.html#fn8) As well, these tools have limitations that reduce their utility for certain purposes; for example, they tend to perform inconsistently on tasks related to emotional or nuanced language. [Footnote 9](https://www.canada.c

[Showing characters 0-10,000 of 68,276. Call read_url with start=10000 to read the next part.]
```

## Turn 2

_Model call: 6,978 input tokens, 269 output tokens_

**Assistant:**

Let me continue reading the page, including the later sections and footnotes.

**Tool call** `read_url` (id `call_551991b1092c4b0abe623792`):

```json
{
  "start": 10000,
  "url": "https://www.canada.ca/en/government/system/digital-government/digital-government-innovations/responsible-use-ai/generative-ai/guide-use-generative-ai.html"
}
```
**Tool call** `read_url` (id `call_7b254621cbac477e85b974de`):

```json
{
  "start": 40000,
  "url": "https://www.canada.ca/en/government/system/digital-government/digital-government-innovations/responsible-use-ai/generative-ai/guide-use-generative-ai.html"
}
```
**Tool result** `read_url` (id `call_551991b1092c4b0abe623792`, 10,101 characters):

```
a/en/government/system/digital-government/digital-government-innovations/responsible-use-ai/generative-ai/guide-use-generative-ai.html#fn9)[Footnote 10](https://www.canada.ca/en/government/system/digital-government/digital-government-innovations/responsible-use-ai/generative-ai/guide-use-generative-ai.html#fn10)

Generative AI could also pose risks to the integrity and security of federal institutions, given its potential misuse by threat actors. Federal institutions should be aware of these risks and consider the best practices recommended by the Canadian Centre for Cyber Security in their guidance [Generative Artificial intelligence (AI) - ITSAP.00.041](https://www.cyber.gc.ca/en/guidance/generative-artificial-intelligence-ai-itsap00041).

Although these tools present challenges and concerns, they also offer potential benefits to public servants and federal institutions. For example, they can enhance productivity through increased efficiency and quality of outputs in analytical and writing tasks in several domains. [Footnote 11](https://www.canada.ca/en/government/system/digital-government/digital-government-innovations/responsible-use-ai/generative-ai/guide-use-generative-ai.html#fn11)[Footnote 12](https://www.canada.ca/en/government/system/digital-government/digital-government-innovations/responsible-use-ai/generative-ai/guide-use-generative-ai.html#fn12) More analysis is needed to determine the most appropriate and beneficial uses of these tools by federal institutions. Experimentation, coupled with performance measurement and analysis, is needed to better understand potential gains and trade-offs and to inform the government’s approach to the use of these tools.

## Recommended approach

In this section
*   [Responsibilities for federal institutions](https://www.canada.ca/en/government/system/digital-government/digital-government-innovations/responsible-use-ai/generative-ai/guide-use-generative-ai.html#toc-4.1)

Federal institutions should explore how they could use generative AI tools to support their operations and improve outcomes for Canadians. Given the challenges and concerns relating to these tools, institutions should assess and mitigate risks and use them only for activities where they can manage the risks effectively. With the growing adoption of these technologies in different sectors and by the public, exploration by federal institutions will help the government understand the risks and opportunities of these tools and keep pace with the evolving digital landscape.

The risks of using these tools depend on what they will be used for and on what mitigation measures are in place.

Examples of **low‑risk**uses:

*   writing an email to invite colleagues to a team‑building event
*   editing a draft document that will go through additional reviews and approvals

Examples of **higher‑risk** uses (such as uses in service delivery):

*   deploying a tool (for example, a chatbot) for use by the public
*   generating a summary of client information

Federal institutions should experiment with low-risk uses before they consider higher‑risk uses. They should always tailor best practices and risk‑mitigation measures to each use.

When deciding whether to use generative AI tools, public servants should refer to the guide to ethical decision-making ([section 6 of _Values Alive: A Discussion Guide to the “Values and Ethics Code for the Public Sector”_](https://www.canada.ca/en/treasury-board-secretariat/services/values-ethics/code/values-alive-discussion-guide.html#Toc11)).

To maintain public trust and ensure the responsible use of generative AI tools by federal institutions, institutions should align with the “FASTER” principles that TBS has developed:

*   **Fair:** ensure that content from these tools does not include or amplify biases and that it complies with human rights, accessibility, and procedural and substantive fairness obligations; engage with affected stakeholders before deployment
*   **Accountable:** take responsibility for the content generated by these tools and the impacts of their use. This includes making sure generated content is accurate, legal, ethical, and compliant with the terms of use; establish monitoring and oversight mechanisms
*   **Secure:** ensure that the infrastructure and tools are appropriate for the security classification of the information and that privacy and personal information are protected; assess and manage cyber security risks and robustness when deploying a system
*   **Transparent:** identify content that has been produced using generative AI; notify users that they are interacting with an AI tool; provide information on institutional policies, appropriate use, training data and the model when deploying these tools; document decisions and be able to provide explanations if tools are used to support decision-making
*   **Educated:** learn about the strengths, limitations and responsible use of the tools; learn how to create effective prompts and to identify potential weaknesses in the outputs
*   **Relevant:** make sure the use of generative AI tools supports user and organizational needs and contributes to better outcomes for clients; consider the environmental impacts when choosing to use a tool; identify appropriate tools for the task; AI tools aren’t the best choice in every situation

For assistance in determining the appropriate use of these tools, public servants should consult relevant stakeholders such as:

*   their institution’s legal services, privacy and security experts
*   the offices of the chief information officer and chief data officer for their institution
*   their institution’s diversity and inclusion specialists

The following can also provide support:

*   the Canadian Centre for Cyber Security
*   Statistics Canada
*   the Office of the Chief Information Officer of Canada (part of TBS)

### Responsibilities for federal institutions

Federal institutions should evaluate generative AI tools for their potential to help employees, not replace them. Institutions are encouraged to responsibly explore uses and to enable employees to optimize their work while ensuring that all uses of these tools are ethical, align with the FASTER principles and comply with policies and laws.

In evaluating these tools and exploring how they could use them, institutions have a number of responsibilities including:

*   ensuring that employees can access and take training on the effective and responsible use of generative AI tools
*   supporting employees in improving their knowledge of topics such as detecting biased and inaccurate content
*   providing access to secure generative AI tools that meet government information, privacy and security requirements
*   enabling access to online generative AI tools, in alignment with the [_Policy on Service and Digital_](https://www.tbs-sct.canada.ca/pol/doc-eng.aspx?id=32603) (requirement 4.4.2.5) and the _Directive on Service and Digital_[Appendix A: Examples of Acceptable Network and Device Use (Non-Exhaustive List)](https://www.tbs-sct.canada.ca/pol/doc-eng.aspx?id=32707#chaAppensix%20A)
*   implementing oversight and performance management processes to monitor the impacts of these tools and to make sure both the tools themselves and their uses comply with applicable laws and policies and align with the FASTER principles, particularly during deployment
*   engaging with employees to understand their needs
*   consulting with stakeholders such as end-users, client representative groups and bargaining agents before high-risk deployments

Institutions should have effective change management practices so that they can help employees improve their current skills and develop new ones.

Managers need to understand what these tools can and can’t be used for and should have realistic expectations of how the tools might help improve employees’ productivity.

Institutions should also evaluate the risks and opportunities associated with using these tools and develop guidance for their institution that aligns with this guide and is tailored to their organization’s context and needs.

## Policy considerations and best practices

In this section
*   [Does the _Directive on Automated Decision-Making_ apply?](https://www.canada.ca/en/government/system/digital-government/digital-government-innovations/responsible-use-ai/generative-ai/guide-use-generative-ai.html#toc-5.1)
*   [Privacy considerations](https://www.canada.ca/en/government/system/digital-government/digital-government-innovations/responsible-use-ai/generative-ai/guide-use-generative-ai.html#toc-5.2)
*   [Documentation requirements](https://www.canada.ca/en/government/system/digital-government/digital-government-innovations/responsible-use-ai/generative-ai/guide-use-generative-ai.html#toc-5.3)
*   [Potential issues and best practices](https://www.canada.ca/en/government/system/digital-government/digital-government-innovations/responsible-use-ai/generative-ai/guide-use-generative-ai.html#toc-5.4)
    1.   [Protection of information](https://www.canada.ca/en/government/system/digital-government/digital-government-innovations/responsible-use-ai/generative-ai/guide-use-generative-ai.html#toc-5.4.a)
    2.   [Bias](https://www.canada.ca/en/government/system/digital-government/digital-government-innovations/responsible-use-ai/generative-ai/guide-use-generative-ai.html#toc-5.4.b)
    3.   [Quality](https://www.canada.ca/en/government/system/digital-government/digital-government-innovations/responsible-use-ai/generative-ai/guide-use-generative-ai.html#toc-5.4.c)
    4.   [Public servant autonomy](https://www.canada.ca/en/government/system/digital-government/digital-government-innovations/responsible-use-ai/generative-ai/guide-use-generative-ai.html#toc-5.4.d)
    5.   [Legal risks](https://www.canada.ca/en/government/system/digital-government/digital-government-innovations/responsible-use-ai/generative-ai/guide-use-generative-ai.html#toc-5.4.e)
    6.   [Distinguishing humans fro

[Showing characters 10,000-20,000 of 68,276. Call read_url with start=20000 to read the next part.]
```
**Tool result** `read_url` (id `call_7b254621cbac477e85b974de`, 10,101 characters):

```
may be inaccurate, incoherent or incomplete

Generative AI technologies can produce content that appears to be well developed, credible and reasonable but that is in fact inaccurate, nonsensical or inconsistent with source data. [Footnote 23](https://www.canada.ca/en/government/system/digital-government/digital-government-innovations/responsible-use-ai/generative-ai/guide-use-generative-ai.html#fn23)[Footnote 6](https://www.canada.ca/en/government/system/digital-government/digital-government-innovations/responsible-use-ai/generative-ai/guide-use-generative-ai.html#fn6) This content is sometimes referred to as a “hallucination.” Also, content generated by AI tools may not provide a holistic view of an issue. Instead, it may focus on prevalent perspectives in the training data. [Footnote 17](https://www.canada.ca/en/government/system/digital-government/digital-government-innovations/responsible-use-ai/generative-ai/guide-use-generative-ai.html#fn17) Content might be out of date, depending on the time period the training data covers and whether the system has live access to recent data. There may also be differences in the quality of the outputs in English and French, depending on the model, task and prompt. The output quality in each language should be evaluated to ensure compliance with official language requirements.

The risks associated with inaccurate content will vary depending on the context and should be assessed. For example, using generative AI tools to learn about a topic may produce incorrect information or non‑existent sources. [Footnote 24](https://www.canada.ca/en/government/system/digital-government/digital-government-innovations/responsible-use-ai/generative-ai/guide-use-generative-ai.html#fn24) If the results were to be used in decision-making, they could lead to unfair treatment of some people or to misguided policy. As well, when considering the use of these tools in public‑facing communications, it is critical that the government not share inaccurate information, which would contribute to misinformation and erode public trust.

##### Best practices for all users of generative AI in federal institutions

*   Clearly indicate that you have used generative AI to develop content.
*   Don’t consider generated content as authoritative. Review it for factual and contextual accuracy by, for example, checking it against information from trusted sources or by having a colleague with expertise review the response.
*   Verify personal information created using generative AI to make sure it is accurate, up to date and complete.
*   Assess the impact of inaccurate outputs. Don’t use generative AI when factual accuracy or data integrity is needed.
*   Strive to understand the quality and source of training data.
*   Consider your ability to identify inaccurate content before you use generative AI. If you can’t confirm the quality of the content, don’t use it.
*   Learn how to create effective prompts and provide feedback to refine outputs to minimize the generation of inaccurate content.
*   Don’t use generative AI tools as search engines unless sources are provided so that you can verify the content.

##### Additional best practices for federal institutions deploying a generative AI tool

*   Test performance and robustness across a variety of uses before deployment. This includes making sure the quality of tools and outputs meets official languages requirements.
*   Assess training data quality when refining models.
*   Use grounding and prompt engineering so the models build responses from only the information you provide and control.
*   Notify users that they are interacting with generative AI.
*   When content is generated by AI, include links to authoritative sources to provide users with additional context and foster transparency.
*   Provide information about the appropriate use of the tools, capabilities and limitations of the system, risk mitigation measures, source of training data and how models were developed.
*   Monitor the performance of generative AI tools on an ongoing basis to understand potential impacts and make sure they are meeting performance targets. Document problems, pause deployment, and update the tool if performance levels are not being achieved.

#### d. Public servant autonomy

##### Issue: overreliance on AI could unduly interfere with judgment, stifle creativity and erode workforce capabilities

Overreliance on generative AI tools could interfere with individual autonomy and judgment. For example, some users may be prone to uncritically accept system recommendations or other outputs, which could be incorrect. [Footnote 25](https://www.canada.ca/en/government/system/digital-government/digital-government-innovations/responsible-use-ai/generative-ai/guide-use-generative-ai.html#fn25)[Footnote 26](https://www.canada.ca/en/government/system/digital-government/digital-government-innovations/responsible-use-ai/generative-ai/guide-use-generative-ai.html#fn26) Overreliance on AI systems can be a sign of automation bias, which is the tendency to favour results generated by automated systems, even in the presence of contrary information from non-automated sources. [Footnote 25](https://www.canada.ca/en/government/system/digital-government/digital-government-innovations/responsible-use-ai/generative-ai/guide-use-generative-ai.html#fn25) As well, confirmation bias could contribute to overreliance [Footnote 25](https://www.canada.ca/en/government/system/digital-government/digital-government-innovations/responsible-use-ai/generative-ai/guide-use-generative-ai.html#fn25) because the outputs of generative AI systems can reinforce a user’s preconceptions, especially when prompts are written in a way that reflects their assumptions and beliefs. [Footnote 27](https://www.canada.ca/en/government/system/digital-government/digital-government-innovations/responsible-use-ai/generative-ai/guide-use-generative-ai.html#fn27) Excessive dependence on AI systems may result in a decline in critical thinking. This could limit diversity in thought, stifle creativity and innovation and lead to partial or incomplete analyses. As such, overreliance on AI may impede employees’ abilities to build and maintain the skills they need to perform tasks that are assigned to generative AI systems, which could potentially erode workforce capabilities.

##### Best practices for all users of generative AI in federal institutions

*   Consider whether you need to use generative AI to meet user and organizational needs.
*   Consider the abilities and limits of generative AI when assigning tasks and reviewing system outputs.
*   Build your AI literacy so that you can critically assess these tools and their outputs.
*   Use generative AI tools as aids, not as substitutes. Do not outsource a skill that you do not understand or possess.
*   Form your own views before seeking ideas or recommendations from AI tools.
*   Use neutral wording when formulating prompts to minimize biased outputs.
*   Always review content generated by AI, even if the system seems to be reliable in providing accurate responses.

#### e. Legal risks

##### Issue: generative AI poses risks to human rights, privacy, intellectual property protection, and procedural fairness

The government’s use of generative AI systems poses risks to the legal rights and obligations of federal institutions and their clients. These risks arise from the data used to train AI models, the way systems process input data, and the quality of system outputs.

The use of copyright-protected materials like articles, books, code, paintings or music by suppliers or federal institutions to train AI models may infringe on intellectual property rights. The use or reproduction of the outputs generated by these models could also infringe on such rights if they contain material that is identical or substantially similar to a copyright-protected work. Further, the ownership of content created by or with the help of generative AI is uncertain. Privacy rights could also be at risk because data used to train generative AI models could include unlawfully collected or used personal information, such as personal information obtained from publicly accessible online sources.

Risks could also arise from the opacity of generative AI models and their potential for producing inaccurate, biased or inconsistent outputs. This opacity makes it difficult to trace and understand how the AI system produces outputs, which can undermine procedural fairness in instances where a federal institution is obliged to provide clients with reasons for administrative decisions, such as decisions to deny benefits. The quality of AI outputs can also impact individuals’ legal rights. For example, biased outputs could lead to discrimination in services, potentially violating human rights.

These risks extend beyond decision-making scenarios. When federal institutions use generative AI tools to help the public find information (for example, chatbots on institutional websites) or to produce public communications, there’s a risk that these tools will generate inappropriate content or misinformation that could contribute to or cause harm for which the government could be liable.

##### Best practices for all users of generative AI in federal institutions

*   Consult your institution’s legal services about the legal risks of deploying generative AI tools or using them in service delivery. The consultation could involve a review of the supplier’s terms of use, copyright policy, privacy policy and other legal documents.
*   Comply with the _Directive on Automated Decision-Making_ when using generative AI in administrative decision-making.
*   Check whether system outputs are identical or substantially similar to copyright-protected material (look at the [Frequently asked questions](https://www.canada.ca/en/government/system/digital-government/digital-government-innovations/responsible-use-ai/generative-ai/guide-use-generative-a

[Showing characters 40,000-50,000 of 68,276. Call read_url with start=50000 to read the next part.]
```

## Turn 3

_Model call: 11,382 input tokens, 122 output tokens_

**Assistant:**

Now let me read the final section, which should contain the footnotes and page footer.

**Tool call** `read_url` (id `call_eec1c1681255422e96e7415b`):

```json
{
  "start": 58000,
  "url": "https://www.canada.ca/en/government/system/digital-government/digital-government-innovations/responsible-use-ai/generative-ai/guide-use-generative-ai.html"
}
```
**Tool result** `read_url` (id `call_eec1c1681255422e96e7415b`, 10,101 characters):

```
osts, social media)?
Use caution.

When you use generative AI to develop content, you are responsible for making sure that:

*   the content is accurate, clear, non‑partisan and unbiased
*   you have the necessary permissions to reproduce, adapt, translate or publish third‑party material
*   the content complies with intellectual property laws
*   you have informed the public of any significant use of generative AI in the production of content
*   the outputs are trusted, given the potential reach and impact of public communications

Can I use generative AI for programming tasks?
Yes, but you must consider the security classification of the code. Also, when it comes to code generation, some generative AI tools may produce content that violates the open‑source licences of the source code they were trained on. To address this issue, use tools to identify potential matches in public code repositories or limit the use of generative AI to tasks like debugging or code explanation.

Can I use generative AI when developing policy?
Yes, but be mindful of the strengths and limitations of generative AI tools, and tailor the tasks you assign to them accordingly. You can use these tools to help with brainstorming during policy development, but use caution and validate the generated content if you will be using it as evidence. Don’t use generative AI tools to recommend, make or interpret policy.

When deciding on policy positions, make your own value judgments, in consultation with the relevant stakeholders and consistent with applicable laws. Be transparent and vigilant about any significant use of generative AI during the policy process, including in research and stakeholder engagement. Make sure the prompts used in such contexts don’t include any information that would pose legal or reputational risks to the government.

Can I use generative AI to automate assessments, recommendations or decisions about clients?
Use caution.

The use of generative AI to make or inform decisions must comply with the _Directive on Automated Decision‑Making_, which seeks to ensure transparency, accountability and fairness in decisions made or informed by automated systems such as those that use generative AI.

If you are considering using generative AI in administrative decision‑making, consult with stakeholders in your institution, including the following, at the planning and design stage:

*   the legal services team
*   the offices of the chief security officer, chief information officer and chief data officer
*   GBA+ experts
*   the privacy team

They will help you make sure you can use generative AI for the identified purpose and will help you identify and mitigate risks.

As well, make sure you:

*   understand how the tool produces its outputs and can find the data it relied on
*   assess outputs for factual accuracy and undue bias toward clients
*   consider potential variation in outputs produced in response to similar prompts, which could lead to inequalities in the treatment of clients
*   consider how you will meet transparency and explainability requirements

How do I check whether system outputs are identical or substantially similar to copyright-protected material?
You can check this by doing an Internet search to compare the output from the generative AI tool with already published material. The risk of copyright issues depends on what you are asking the generative AI system to do, the subject matter, and how you will use the output.

You can lower the risk of a having problem by:

*   using generative AI for tasks that have a lower likelihood of including copyright-protected information, such as editing content that you have drafted yourself as opposed to generating new content
*   using materials where copyright issues are unlikely to be present, for example, a publicly available or paid-for stock image, rather than using generative AI

Your level of diligence in making sure you don’t have a copyright issue also depends on what you are asking the generative AI system to do, the subject matter, and how you will use the output. If the output will be publicly available, you must be extremely vigilant in checking that there are no copyright issues. You may want to consult your institution’s legal services to get advice tailored to your operational requirements.

What do I include when I’m notifying people that I used a generative AI system?
Exactly what you tell people will depend on the context. Consider, for example:

*   who the audience is
*   how the system is being used
*   what format the generated content is (such as text, images, or code)
*   how much of the generative AI content was included in the final product

At a minimum, tell people which system and version you used. In addition, you may want to also include the following:

*   the purpose for using it
*   whether and to what extent you reviewed, validated or modified the output

When you use generative AI in your work, inform your manager.

The following table contains a few scenarios where you might use a generative AI tool and suggestions for information you might provide.

| Scenario | Information you could provide |
| --- | --- |
| Using a generative AI tool to summarize information for your director to prepare them for a meeting | A quick note at the bottom of the email saying: * which generative AI tool you used to help you summarize the information * that you reviewed the content for accuracy |
| Using a generative AI tool in building a presentation | A note on a slide saying which generative AI tool you used and that you used it to organize the slides, generate images, and suggest next steps |
| Deployment of a public‑facing generative AI tool such as a chatbot | A note up front telling clients: * that they aren’t interacting with a human * how to use the tool * what types of responses to expect * a reminder to not input personal or sensitive information In addition to informing clients up front, you should take other transparency measures such as publication of information on: * the tool’s capabilities and limitations * what risk mitigation measures have been taken * the source of training data * what model is being used and how it was developed |
| Using a generative AI tool to summarize articles for a monthly newsletter posted on a collaborative site | * which generative AI tool you used to create the summary * how much of the final summary came from the AI tool * what steps you took to make sure the final content was accurate, up-to-date, complete, valid, unbiased and non‑partisan |
| Using a generative AI tool when writing a research paper | * follow style guides and journal publication requirements to determine whether these tools can be used and the format of such citations |

Do I need to record my use of generative AI tools?
It depends. If your use of these tools is an activity of business value, you must document it. The context in which you are using the tools will inform whether documentation is needed and how long the documentation should be retained.

If you are considering using these tools to make administrative decisions or related assessments, you should comply with the documentation requirements in the _Directive on Automated Decision-Making_.

If you are using these tools for daily tasks such as brainstorming, translation or drafting and editing documents, you may not need to document their use because the information generated will likely be transitory.

Even if the tools produce transitory information, you should still notify your manager of any substantive use.

Your institution may also have guidance on what should be documented. Check with the office of the chief information officer or office of the chief data officer for your institution to find out if there is institution-specific guidance.

Should I use a personal or work email address to register for AI tools?
When using generative AI tools for GC business, you should use an official work email address. Using a work email address:

*   helps ensure transparency and accountability
*   helps ensure that decisions are properly recorded and transferred to corporate repositories, as appropriate

Other recommendations when registering for AI tools:

*   Use a strong, unique password that is different from and not a variant of passwords you use on a corporate device or other service
*   When possible, use two‑factor authentication on third‑party services

How do I write effective prompts?
How you ask a generative AI system to produce content affects the generated outputs.

When writing prompts, be as clear and specific as possible and provide context.

For example, you can:

*   provide background information
*   identify the audience
*   specify the length and tone of the desired output

You can even give the tool a few examples of possible input and the corresponding output you’re seeking, and then ask it to replicate the approach for new inputs. Once you have an output, you can reply with additional prompts to help refine the initial output.

When developing prompts, consider your own views and biases and write prompts that provide holistic and unbiased outputs.

You may also want to ask the system to only generate responses based on certain sources or input that you provide it. For example, you could copy information into the prompt and ask the system to generate an executive summary of it for your senior leader. Or you may want to include the content of an upcoming presentation and ask the system to create engaging introductory speaking points based on the presentation.

There are many other prompting techniques that are not covered here, and best practices may vary depending on the model used.

Experiment with your prompts and language and take training on effective prompt techniques. The Canada School of Public Service offers learning products on AI, including [Using Generative AI in the Government of Canada](https://catalogue.csps-efpc.gc.ca/product?catalog=DDN321&cm_loc

[Showing characters 58,000-68,000 of 68,276. Call read_url with start=68000 to read the next part.]
```

## Turn 4

_Model call: 13,455 input tokens, 169 output tokens_

**Tool call** `read_url` (id `call_a462308152714e6d92cf0a7f`):

```json
{
  "start": 68000,
  "url": "https://www.canada.ca/en/government/system/digital-government/digital-government-innovations/responsible-use-ai/generative-ai/guide-use-generative-ai.html"
}
```
**Tool result** `read_url` (id `call_a462308152714e6d92cf0a7f`, 335 characters):

```
ale=en) and [Working with Artificial Intelligence Series: Writing Inclusive Prompts](https://www.csps-efpc.gc.ca/tools/articles/writing-inclusive-prompts-eng.aspx). Whatever prompt technique you use, follow the FASTER principles and the best practices provided in this guide.


[End of page. Showed characters 68,000-68,276 of 68,276.]
```

## Turn 5

_Model call: 13,717 input tokens, 279 output tokens_

**Tool call** `read_url` (id `call_6e559f22ac0049678acc3832`):

```json
{
  "start": 50000,
  "url": "https://www.canada.ca/en/government/system/digital-government/digital-government-innovations/responsible-use-ai/generative-ai/guide-use-generative-ai.html"
}
```
**Tool call** `web_search` (id `call_90cf8669c12d4cbdb71ccf5d`):

```json
{
  "query": "\"Guide on the use of generative artificial intelligence\" Treasury Board of Canada Secretariat"
}
```
**Tool result** `read_url` (id `call_6e559f22ac0049678acc3832`, 10,101 characters):

```
i.html#toc-8) for more information on how to do this). Give proper attribution, where appropriate, or remove the problematic material to minimize the risk of intellectual property infringement.
*   Consult designated officials on the licensing and administration of Crown copyright if you are planning to include outputs in public communications, in accordance with the [_Procedures for Publishing_](https://www.tbs-sct.canada.ca/pol/doc-eng.aspx?id=27167).
*   Evaluate system outputs for factual inaccuracies, biases or harmful ideas that may conflict with GC values.
*   Keep up to date on legal and policy developments related to AI regulation.

##### Additional best practices for federal institutions deploying a generative AI tool

*   Verify the legality of the method used to obtain data for training AI models and make sure you have permission to use the data for this purpose.
*   Document the data provenance and that you have authorization from the copyright owner.
*   Where feasible, train your model using open‑source data that you have confirmed you may use in this way.
*   Be transparent when you use generative AI. For example, notify users if they are interacting with a system rather than a human. Where relevant, include a disclaimer to minimize liability risks and increase transparency.

#### f. Distinguishing humans from machines

##### Issue: people may not know that they are interacting with an AI system, or they may wrongly assume that AI is being used

Conversational agents or chatbots that use generative AI can produce responses that are so human‑like that it may be difficult to distinguish them from those of a real person. [Footnote 28](https://www.canada.ca/en/government/system/digital-government/digital-government-innovations/responsible-use-ai/generative-ai/guide-use-generative-ai.html#fn28) As a result, clients may think they are interacting with a human. Similarly, clients may think an email they have received was written by a person when it was actually generated by an AI tool. On the other hand, clients might think they are interacting with an AI tool when they are actually dealing with a real person. Transparency about whether a client is interacting with a person or a chatbot is essential to ensure that the client is not misled and to maintain trust in government.

##### Best practices for all users of generative AI in federal institutions

*   Clearly communicate when and how you are using AI in interactions with the public.
*   Inform users when text, audio or visual messages addressed to them are generated by AI.

##### Additional best practices for federal institutions deploying a generative AI tool

*   Offer alternative non-automated means of communicating.
*   Use watermarks to identify content that is generated by AI.
*   Publish information about the system, such as a plain-language description of how it works, why your institution is using it and what steps were taken to ensure the quality of the outputs.

#### g. Environmental impacts

##### Issue: the development and use of generative AI systems can have significant environmental costs

The development and use of generative AI systems can be a significant source of greenhouse gas (GHG) emissions and water usage. These emissions come not only from the compute used to train and operate generative models but also from the production and transportation of servers that support AI programs. In addition, data centres are energy-intensive and consume vast quantities of water for on-site cooling and off-site electricity generation. [Footnote 29](https://www.canada.ca/en/government/system/digital-government/digital-government-innovations/responsible-use-ai/generative-ai/guide-use-generative-ai.html#fn29) Although generative AI has the potential to help combat climate change, its use must be balanced against the need for swift and drastic action to reduce global greenhouse gas emissions and avert irreversible damage to the environment. [Footnote 30](https://www.canada.ca/en/government/system/digital-government/digital-government-innovations/responsible-use-ai/generative-ai/guide-use-generative-ai.html#fn30)

##### Best practices for all users of generative AI in federal institutions

*   Use generative AI tools hosted in net-zero or carbon-neutral data centres.
*   Use generative AI tools only when relevant to program objectives and desired outcomes.
*   Understand that the environmental impact of generative AI comes not only from its use but also from the training of the models and the manufacturing of the hardware components that run data centres, as well as the mining, manufacturing, assembly, transportation, and disposal of them.

##### Additional best practices for federal institutions deploying a generative AI tool

*   Find out whether your AI supplier has set any greenhouse-gas reduction targets. [Footnote 31](https://www.canada.ca/en/government/system/digital-government/digital-government-innovations/responsible-use-ai/generative-ai/guide-use-generative-ai.html#fn31)
*   Conduct an environmental impact assessment as part of the proposal to develop or procure generative AI tools. Make sure any decision to procure these tools is made in accordance with the [_Policy on Green Procurement_](https://www.tbs-sct.canada.ca/pol/doc-eng.aspx?id=32573).
*   Encourage developers to be transparent about sustainability by giving preference to those that clearly communicate the environmental impacts of their AI systems through reports on compliance with GHG Protocols. [Footnote 32](https://www.canada.ca/en/government/system/digital-government/digital-government-innovations/responsible-use-ai/generative-ai/guide-use-generative-ai.html#fn32)
*   Use carbon‑awareness tools to estimate the carbon footprint of systems before training or production. [Footnote 33](https://www.canada.ca/en/government/system/digital-government/digital-government-innovations/responsible-use-ai/generative-ai/guide-use-generative-ai.html#fn33)

## Use of this guide

Federal institutions are encouraged to use this guide as they continue to develop their own guidance on the use of generative AI. This guide and the community will continue to evolve.

## Additional support

### Information and guidance on specific uses of generative AI

*   TBS’s Responsible Data and AI team ([ai-ia@tbs-sct.gc.ca](mailto:ai-ia@tbs-sct.gc.ca))
*   Canadian Centre for Cyber Security’s guidance on [Generative Artificial Intelligence (AI) - ITSAP.00.041](https://www.cyber.gc.ca/en/guidance/generative-artificial-intelligence-ai-itsap00041)
*   TBS’s summary guidance, _[Using Generative AI in Your Daily Work](https://www.canada.ca/en/government/system/digital-government/digital-government-innovations/responsible-use-ai/generative-ai/generative-ai-your-daily-work.html)_.

### Courses and events

The Canada School of Public Service offers different courses and events on AI, including [Using Generative AI in the Government of Canada](https://catalogue.csps-efpc.gc.ca/product?catalog=DDN321&cm_locale=en).

### Additional resources

Federal institutions can also contact the following for additional support:

*   Communications Security Establishment (including the Canadian Centre for Cyber Security)
*   Statistics Canada

## Frequently asked questions

Can I use generative AI to draft emails or briefing notes?
Yes. Depending on the context. If you use a generative AI tool to draft an email or briefing note, you are responsible for making sure that:

*   the data you input into the tool doesn’t include personal, protected, classified or other sensitive information, unless you have confirmed that the tool is appropriate for the security classification of the information
*   generated content is accurate, non-partisan, unbiased, and doesn’t violate intellectual property laws
*   you inform management that you used a generative AI tool in the drafting process

Can I use generative AI to develop content for public communications (for example, web posts, social media)?
Use caution.

When you use generative AI to develop content, you are responsible for making sure that:

*   the content is accurate, clear, non‑partisan and unbiased
*   you have the necessary permissions to reproduce, adapt, translate or publish third‑party material
*   the content complies with intellectual property laws
*   you have informed the public of any significant use of generative AI in the production of content
*   the outputs are trusted, given the potential reach and impact of public communications

Can I use generative AI for programming tasks?
Yes, but you must consider the security classification of the code. Also, when it comes to code generation, some generative AI tools may produce content that violates the open‑source licences of the source code they were trained on. To address this issue, use tools to identify potential matches in public code repositories or limit the use of generative AI to tasks like debugging or code explanation.

Can I use generative AI when developing policy?
Yes, but be mindful of the strengths and limitations of generative AI tools, and tailor the tasks you assign to them accordingly. You can use these tools to help with brainstorming during policy development, but use caution and validate the generated content if you will be using it as evidence. Don’t use generative AI tools to recommend, make or interpret policy.

When deciding on policy positions, make your own value judgments, in consultation with the relevant stakeholders and consistent with applicable laws. Be transparent and vigilant about any significant use of generative AI during the policy process, including in research and stakeholder engagement. Make sure the prompts used in such contexts don’t include any information that would pose legal or reputational risks to the government.

Can I use generative AI to automate assessments, recommendations or decisions about clients?
Use caution.

The use of generative AI to make or inform decision

[Showing characters 50,000-60,000 of 68,276. Call read_url with start=60000 to read the next part.]
```
**Tool result** `web_search` (id `call_90cf8669c12d4cbdb71ccf5d`, 6,875 characters):

```
Search results for ""Guide on the use of generative artificial intelligence" Treasury Board of Canada Secretariat" (searched 2026-11-26):

[1] Guide on the use of generative artificial intelligence - Canada.ca
URL: https://www.canada.ca/en/government/system/digital-government/digital-government-innovations/responsible-use-ai/generative-ai/guide-use-generative-ai.html
Excerpt: This guide also seeks to raise awareness and foster coordination among federal institutions. It highlights the importance of engaging key stakeholders before deploying generative AI tools for public use and before using them for purposes such as service delivery.

Stakeholders include:

- legal counsel
- privacy and security experts
- the Office of the Chief Information Officer at the Treasury Board of Canada Secretariat (TBS)
- bargaining agents
- advisory groups
- clients of GC services [...] To maintain public trust and ensure the responsible use of generative AI tools by federal institutions, institutions should align with the “FASTER” principles that TBS has developed: [...] - TBS’s Responsible Data and AI team (ai-ia@tbs-sct.gc.ca)
- Canadian Centre for Cyber Security’s guidance on Generative Artificial Intelligence (AI) - ITSAP.00.041
- TBS’s summary guidance, Using Generative AI in Your Daily Work.

### Courses and events

The Canada School of Public Service offers different courses and events on AI, including Using Generative AI in the Government of Canada.

### Additional resources

Federal institutions can also contact the following for additional support:

[2] Guide on the use of generative artificial intelligence | SettlementAtWork
URL: https://settlementatwork.org/en/resources/guide-use-generative-artificial-intelligence
Excerpt: This guide also seeks to raise awareness and foster coordination among federal institutions. It highlights the importance of engaging key stakeholders before deploying generative AI tools for public use and before using them for purposes such as service delivery.

Stakeholders include:

- legal counsel
- privacy and security experts
- the Office of the Chief Information Officer at the Treasury Board of Canada Secretariat (TBS)
- bargaining agents
- advisory groups
- clients of GC services [...] ### Overview

Generative artificial intelligence (AI) tools offer many potential benefits to Government of Canada (GC) institutions. Federal institutions should explore potential uses of generative AI tools for supporting and improving their operations, but they should not use these tools in all cases. Institutions must be cautious and evaluate the risks before they start using them. They should also limit the use of these tools to instances where they can manage the risks effectively. [...] This document provides guidance to federal institutions on their use of generative AI tools. This includes instances where federal institutions are deploying these tools. It provides an overview of generative AI, identifies challenges relating to its use, puts forward principles for using it responsibly, and offers policy considerations and best practices.

[3] Responsible Use of Generative AI - GCwiki
URL: https://wiki.gccollab.ca/index.php?title=Responsible_Use_of_Generative_AI&mobileaction=toggle_view_desktop
Excerpt: Departments are encouraged to responsibly explore potential uses of generative AI tools to support and improve their operations, making sure to identify and manage risks before they do. For example, large language models such as ChatGPT or Copilot could be used to edit or summarize non-sensitive documents or information and brainstorm ideas.

Treasury Board of Canada Secretariat (TBS) has developed guidance to support the responsible use of generative AI in the government: [...] <!--THE END-->

- Working with AI – a series of short articles featuring generative AI use cases such as writing memos, learning a new language and enhancing programming efficiency.

### Enquiries

Please contact the TBS Responsible Data and AI team (ai-ia@tbs-sct.gc.ca) for any questions. [...] ### Resources

- Using Generative AI in the Government of Canada – a virtual course developed by the Canada School of Public Service, Shared Services Canada and TBS that provides an overview of generative AI. It covers topics including exploring potential uses and tools available to public servants, writing effective prompts and ensuring inclusive language.

<!--THE END-->

[4] Government of Canada Guide on the use of Generative AI - Digital Government Hub
URL: https://digitalgovernmenthub.org/examples/government-of-canada-guide-on-the-use-of-generative-ai
Excerpt: This document provides preliminary guidance to federal institutions on their use of generative AI tools. This includes instances where these tools are deployed by federal institutions. It provides an overview of generative AI, identifies challenges and concerns relating to its use, puts forward principles for using it responsibly, and offers policy considerations and best practices. [...] # Government of Canada Guide on the use of Generative AI

Guide for the use of generative artificial intelligence (AI) from the Government of Canada.

Generative artificial intelligence (AI) tools offer many potential benefits to Government of Canada (GC) institutions. Federal institutions should explore potential uses of generative [...] AI tools for supporting and improving their operations. However, because these tools are evolving, they should not be used in all cases. Federal institutions must be cautious and evaluate the risks before they start using them. The use of these tools should be restricted to instances where risks can be effectively managed.

[5] Media Advisory - The President of the Treasury Board will make an announcement on artificial intelligence for the federal public service
URL: https://ca.finance.yahoo.com/news/media-advisory-president-treasury-board-205600418.html
Excerpt: Please confirm your attendance by email at media@tbs-sct.gc.ca by 10:00 am on Tuesday, March 4, 2025. Information on the location of the event will be provided at the time of registration.

Date  
March 4th, 2025

Time (local time)  
2:30 pm – Arrival  
2:45 pm – Event begins

Location  
University of Waterloo  
200 University Avenue West  
Waterloo, Ontario  
N2L 3G1

Stay connected

X: @TBS\_Canada  
Facebook:   
LinkedIn: 

SOURCE Treasury Board of Canada Secretariat

View original content: [...] # Media Advisory - The President of the Treasury Board will make an announcement on artificial intelligence for the federal public service

WATERLOO, ON, March 3, 2025 /CNW/ - The Honourable Ginette Petitpas Taylor, President of the Treasury Board, will make an announcement regarding artificial intelligence in the federal public service.

President Petitpas Taylor will be available to take questions from the media following the announcement.
```

## Turn 6

_Model call: 17,434 input tokens, 454 output tokens_

**Tool call** `read_url` (id `call_8f2679cb920d499a978980bd`):

```json
{
  "start": 0,
  "url": "https://www.canada.ca/en/government/system/digital-government/digital-government-innovations/responsible-use-ai.html"
}
```
**Tool call** `web_search` (id `call_5377859add3544eca612c323`):

```json
{
  "query": "Treasury Board FASTER principles generative AI federal public service guide 2024 2025"
}
```
**Tool call** `web_search` (id `call_348a765841bc46ac81ac0826`):

```json
{
  "query": "ChatGPT GPT-3.5 training data cutoff September 2021 OpenAI"
}
```
**Tool result** `web_search` (id `call_5377859add3544eca612c323`, 6,541 characters):

```
Search results for "Treasury Board FASTER principles generative AI federal public service guide 2024 2025" (searched 2026-11-26):

[1] Consider the Government of Canada’s Guide on the Use of Generative Artificial Intelligence – TESL Ontario Blog
URL: https://blog.teslontario.org/consider-the-government-of-canadas-guide-on-the-use-of-generative-artificial-intelligence
Excerpt: FASTER Principles

Developed by the Treasury Board of Canada, the FASTER principles, are designed to provide an ethical framework when using generative AI tools. This mnemonic is a possible way to introduce good GenAI practices to your staff. These principles appear as they were published in the guide below. [...] Treasury Board of Canada Secretariat. (2024, February 12). Generative AI in your daily work or Concise Guide summary, 

Considering the Government of Canada’s Guide on the Use of Generative Artificial Intelligence before moving forward with GenAI. Tutela Webinar. (June 2025). [...] This is not an extensive list. I am hoping to work with educators, students and administrators this year to refine our understanding of what is ethical, safe and effective for learning when GenAI is used in our centers in the future. I hope to discuss and learn from you this year.

Resources

Treasury Board of Canada Secretariat. (2024, February 12). Guide on the use of generative artificial intelligence.

[2] Guide on the use of generative artificial intelligence - Canada.ca
URL: https://www.canada.ca/en/government/system/digital-government/digital-government-innovations/responsible-use-ai/generative-ai/guide-use-generative-ai.html
Excerpt: To maintain public trust and ensure the responsible use of generative AI tools by federal institutions, institutions should align with the “FASTER” principles that TBS has developed: [...] Federal institutions should evaluate generative AI tools for their potential to help employees, not replace them. Institutions are encouraged to responsibly explore uses and to enable employees to optimize their work while ensuring that all uses of these tools are ethical, align with the FASTER principles and comply with policies and laws.

In evaluating these tools and exploring how they could use them, institutions have a number of responsibilities including: [...] This guide also seeks to raise awareness and foster coordination among federal institutions. It highlights the importance of engaging key stakeholders before deploying generative AI tools for public use and before using them for purposes such as service delivery.

Stakeholders include:

- legal counsel
- privacy and security experts
- the Office of the Chief Information Officer at the Treasury Board of Canada Secretariat (TBS)
- bargaining agents
- advisory groups
- clients of GC services

[3] Statement from the President of the Treasury Board on advancing digital government
URL: https://ca.finance.yahoo.com/news/statement-president-treasury-board-advancing-213100629.html
Excerpt: This includes presenting an artificial intelligence (AI) strategy to better deliver services to Canadians. While AI presents opportunities for innovation and efficiency, it must be balanced with responsible use. This strategy will guide how AI should be used in the federal public service, ensuring it follows clear values, ethics and rules. [...] Today, at the Digital Government Leaders Summit, I shared our What We Heard Report from our consultations on the AI Strategy for the Federal Public Service, which is available online now, reflecting the feedback and recommendations shared by representatives from research institutes, academia, industry, civil society, bargaining agents, Indigenous organizations, and members of the public. I look forward to publishing the full AI strategy this spring."

Associated Links

Stay connected [...] As part of the development of the strategy, the Government of Canada sought input from various groups through engagement and consultation. The feedback shared to date has been instrumental in shaping this plan, focusing on the safe adoption of AI, accessibility and inclusion, and maintaining continuous dialogue and transparency.

[4] Media Advisory - The President of the Treasury Board will make an announcement on artificial intelligence for the federal public service
URL: https://ca.finance.yahoo.com/news/media-advisory-president-treasury-board-205600418.html
Excerpt: # Media Advisory - The President of the Treasury Board will make an announcement on artificial intelligence for the federal public service

WATERLOO, ON, March 3, 2025 /CNW/ - The Honourable Ginette Petitpas Taylor, President of the Treasury Board, will make an announcement regarding artificial intelligence in the federal public service.

President Petitpas Taylor will be available to take questions from the media following the announcement. [...] Please confirm your attendance by email at media@tbs-sct.gc.ca by 10:00 am on Tuesday, March 4, 2025. Information on the location of the event will be provided at the time of registration.

Date  
March 4th, 2025

Time (local time)  
2:30 pm – Arrival  
2:45 pm – Event begins

Location  
University of Waterloo  
200 University Avenue West  
Waterloo, Ontario  
N2L 3G1

Stay connected

X: @TBS\_Canada  
Facebook:   
LinkedIn: 

SOURCE Treasury Board of Canada Secretariat

View original content:

[5] Media Advisory - The President of the Treasury Board will make an announcement on artificial intelligence for the federal public service
URL: https://finance.yahoo.com/news/media-advisory-president-treasury-board-205600912.html
Excerpt: # Media Advisory - The President of the Treasury Board will make an announcement on artificial intelligence for the federal public service

WATERLOO, ON, March 3, 2025 /CNW/ - The Honourable Ginette Petitpas Taylor, President of the Treasury Board, will make an announcement regarding artificial intelligence in the federal public service.

President Petitpas Taylor will be available to take questions from the media following the announcement. [...] Please confirm your attendance by email at media@tbs-sct.gc.ca by 10:00 am on Tuesday, March 4, 2025. Information on the location of the event will be provided at the time of registration.

Date  
March 4th, 2025

Time (local time)  
2:30 pm – Arrival  
2:45 pm – Event begins

Location  
University of Waterloo  
200 University Avenue West  
Waterloo, Ontario  
N2L 3G1

Stay connected

X: @TBS\_Canada  
Facebook:   
LinkedIn: 

SOURCE Treasury Board of Canada Secretariat

View original content:
```
**Tool result** `web_search` (id `call_348a765841bc46ac81ac0826`, 6,757 characters):

```
Search results for "ChatGPT GPT-3.5 training data cutoff September 2021 OpenAI" (searched 2026-11-26):

[1] What is the actual cutoff date for GPT-4? - ChatGPT - OpenAI Developer Community
URL: https://community.openai.com/t/what-is-the-actual-cutoff-date-for-gpt-4/394750
Excerpt: Also ChatGPT-3.5: “I apologize for any confusion in my previous responses. I do not receive updates in real-time. My training data includes information up until September 2021, and I don’t have direct awareness of events or updates that occurred after that date. Any mention of January 2022 in my responses was an error, and I appreciate your patience in seeking clarification.”

Probably September 2021 is the actual accurate date for ChatGPT’s last update on its data. [...] April 2023 is the knowledge cutoff date.

Yes, sorry, that’s for ChatGPT-4 (which is what the original question was about), for ChatGPT-3 the knowledge cut-off date is September 2021, but both models may have an issue in which they are giving responses regarding updates to their data, which suggest they have data after the cut-off date. [...] but the AI telling people it’s more up-to-date than it is, and then suggesting it’s generalising, or even gave the date in error, seems like a pretty fundamental risk.

Yes, this is a risk. The models hallucinate and confabulate, do not trust them.

So my answer to the original question here, though based on ChatGPT-3 (web UI) is:

Probably September 2021 is the actual accurate date for ChatGPT’s last update on its data.

[2] ChatGPT Knowledge Cutoff (October 2026): GPT-6 Is Now the Default - RankScope
URL: https://rankscope.ai/blog/chatgpt-knowledge-cutoff
Excerpt: September 2021 was GPT-3.5 Turbo's cutoff. That date appears in thousands of older articles, which ended up in later models' training data, so models sometimes repeat it about themselves. Check OpenAI's model documentation for the authoritative date.

Which AI model has the most recent knowledge cutoff? [...] | GPT-4 Turbo | December 1, 2023 | Not in ChatGPT |
| GPT-4o | October 1, 2023 | Retired February 13, 2026 (API only) |
| GPT-4o mini | October 1, 2023 | Not in ChatGPT |
| o1 | October 1, 2023 | Not in ChatGPT |
| GPT-3.5 Turbo | September 1, 2021 | Not in ChatGPT | [...] Common confusion: you'll still see "September 2021" given as ChatGPT's cutoff. That is GPT-3.5 Turbo's date. It appears in so many old articles that models sometimes repeat it about themselves. "October 2023" is GPT-4o, which hasn't been in ChatGPT since February 2026. "February 16, 2026" is GPT-5.6, which stopped being the default on October 7.

## All Major LLM Knowledge Cutoffs (October 2026)

[3] New knowledge cutoff date - Community - OpenAI Developer Community
URL: https://community.openai.com/t/new-knowledge-cutoff-date/382962
Excerpt: # New knowledge cutoff date

We’re now up to January 2022.

Interesting that the version didn’t change, still August 3.

Good catch. Thanks for passing it along. Things are moving so quickly these days…

Also just noticed this!

The new knowledge cutoff is only for gpt4, it’s still September 2021 for gpt-3.5-T [...] Would be nice with a specific date in the documentation though :laughing:

:laughing:

Edit: small typo

It is no longer limited to data before September 2021.

That is because Bing webbrowsing is now activated again, not because the training data has been extended.  
I also did ask 3.5 and 4 and would say the link I posted earlier contains a quite definite answer.

Let’s see if I can convince you in another way :wink:

:wink:

Try this prompt and see if you can remember some of these: [...] ([chat share]). “GPT 3.5”, though (even after an upgrade to not giving up prompt secrets), doesn’t do so well with amusing 2022 facts.

FWIW,

There is a discrepancy between GPT-4-8k and GPT-4-32k. Spoiler alert, 32k has 1 more month of knowledge!

GPT-4-8k:  
As an AI, I can’t predict events occurring after my last model’s training cut-off in September 2021. I suggest checking a reliable news source for information about amusing events from January 2022.

[4] Knowledge cutoff date of September 2021 - ChatGPT - OpenAI Developer Community
URL: https://community.openai.com/t/knowledge-cutoff-date-of-september-2021/66215
Excerpt: limited to data up until September 2021. Are there any plans to update the data? Will the model be connected to the internet in the future? It would be cool to use chat to learn the latest technology. For example Laravel 10 (release 14.02.23)&lt;/p&gt; &lt;/div&gt; &lt;/div&gt; &lt;div id="post\_2" class="topic-body crawler-post"&gt; &lt;div class="crawler-post-meta"&gt;&lt;span class="creator"&gt; &lt;a rel="nofollow" href=" &lt;meta itemprop="url" content=" &lt;/span&gt; &lt;link href=" [...] &lt;div class="post"&gt; &lt;p&gt;There is a big difference between avoiding some topics and limiting the knowledge base to an old dataset. Honestly it sounds to me more like they will make you pay for a more recent dataset. I devoloped with gpt 3 a lot of projects. Here list:&lt;/p&gt; &lt;ul&gt; &lt;li&gt;&lt;a href=" rel="nofollow"&gt; &lt;h1&gt;Calculator.Bot&lt;/h1&gt;&lt;/a&gt;&lt;/li&gt; &lt;li&gt;&lt;a href=" rel="nofollow"&gt; &lt;h1&gt;Translate.How&lt;/h1&gt;&lt;/a&gt;&lt;/li&gt; [...] class="topic-body crawler-post"&gt; &lt;div class="crawler-post-meta"&gt;&lt;span class="creator"&gt; &lt;a rel="nofollow" href=" &lt;meta itemprop="url" content=" &lt;/span&gt; &lt;span class="crawler-post-infos"&gt; &lt;time class="post-time"&gt; February 18, 2023, 8:05pm &lt;/time&gt; &lt;meta itemprop="dateModified" content="2023-02-18T20:05:15Z"&gt;&lt;/meta&gt; &lt;span&gt;1&lt;/span&gt; &lt;/span&gt; &lt;/div&gt; &lt;div class="post"&gt; &lt;p&gt;The model is currently limited to data up

[5] ChatGPT Creator OpenAI Debuts New GPT-4 AI System
URL: https://finance.yahoo.com/news/chatgpt-creator-openai-debuts-gpt-174342726.html
Excerpt: GPT-3 was released in 2020, and along with the 3.5 version, was used to create the Dall-E image-generation tool and the chatbot ChatGPT — two products that caught the public imagination and spurred other tech companies to pursue AI more aggressively. Since then, buzz has grown over whether the next model will be more proficient and possibly able to take on additional tasks. [...] GPT-4, which stands for generative pretrained transformer 4, will be available to OpenAI's paid ChatGPT Plus subscribers, and developers can sign up to build applications with it. OpenAI said Tuesday the tool is "40% more likely to produce factual responses than GPT-3.5 on our internal evaluations." The new version can also handle text and image queries — so a user can submit a picture with a related question and ask GPT-4 to describe it or answer questions.
```
**Tool result** `read_url` (id `call_8f2679cb920d499a978980bd`, 10,096 characters):

```
Title: Responsible use of artificial intelligence in government

URL Source: https://www.canada.ca/en/government/system/digital-government/digital-government-innovations/responsible-use-ai.html

Markdown Content:
*   [Skip to main content](https://www.canada.ca/en/government/system/digital-government/digital-government-innovations/responsible-use-ai.html#wb-cont)
*   [Skip to "About government"](https://www.canada.ca/en/government/system/digital-government/digital-government-innovations/responsible-use-ai.html#wb-info)
*   [Switch to basic HTML version](https://www.canada.ca/en/government/system/digital-government/digital-government-innovations/responsible-use-ai.html?wbdisable=true)

## Language selection

*   [Français fr](https://www.canada.ca/fr/gouvernement/systeme/gouvernement-numerique/innovations-gouvernementales-numeriques/utilisation-responsable-ai.html)

[![Image 1: Government of Canada](https://www.canada.ca/etc/designs/canada/wet-boew/assets/sig-blk-en.svg) / Gouvernement du Canada](https://www.canada.ca/en.html)

## Search

Search Canada.ca 

Search

* * *

## Menu

Main Menu. Press the SPACEBAR to expand or the escape key to collapse this menu. Use the Up and Down arrow keys to choose a submenu item. Press the Enter or Right arrow key to expand it, or the Left arrow or Escape key to collapse it. Use the Up and Down arrow keys to choose an item on that level and the Enter key to access it.

Main Menu 
*   [Jobs and the workplace](https://www.canada.ca/en/government/system/digital-government/digital-government-innovations/responsible-use-ai.html#)
    *   [Jobs: home](https://www.canada.ca/en/services/jobs.html)

    *   [Job Bank](https://www.jobbank.gc.ca/findajob)
    *   [Government of Canada jobs](https://www.canada.ca/en/services/jobs/opportunities/government.html)
    *   [Youth and student employment](https://www.canada.ca/en/services/jobs/youth.html)
    *   [Jobs in national security and defence](https://www.canada.ca/en/services/defence/jobs.html)
    *   [Moving within Canada to work](https://www.canada.ca/en/employment-social-development/programs/labour-mobility.html)
    *   [Funding for jobs and training](https://www.canada.ca/en/employment-social-development/services/funding/programs.html)
    *   [Training](https://www.canada.ca/en/services/jobs/training.html)
    *   [Hiring and managing employees](https://www.canada.ca/en/services/business/hire.html)
    *   [Starting a business](https://www.canada.ca/en/services/business/start.html)
    *   [Employment Insurance benefits and leave](https://www.canada.ca/en/services/benefits/ei.html)
    *   [Workplace standards](https://www.canada.ca/en/services/jobs/workplace.html)
    *   [Pensions and retirement](https://www.canada.ca/en/services/finance/pensions.html)

    *   [Most requested](https://www.canada.ca/en/government/system/digital-government/digital-government-innovations/responsible-use-ai.html#)
        *   [Work in Canada - work permits](https://www.canada.ca/en/immigration-refugees-citizenship/services/work-canada.html)
        *   [Immigrate as a skilled worker](https://www.canada.ca/en/immigration-refugees-citizenship/services/immigrate-canada/express-entry.html)
        *   [Hire a temporary foreign worker](https://www.canada.ca/en/immigration-refugees-citizenship/services/work-canada/hire-temporary-foreign.html)
        *   [Federal Skilled Worker Program](https://www.canada.ca/en/immigration-refugees-citizenship/services/immigrate-canada/express-entry/who-can-apply/federal-skilled-workers.html)
        *   [View your records of employment](https://www.canada.ca/en/employment-social-development/services/my-account.html)
        *   [Submit a record of employment - employers](https://www.canada.ca/en/employment-social-development/programs/ei/ei-list/ei-roe/access-roe.html)
        *   [Federal Student Work Experience Program (FSWEP)](https://www.canada.ca/en/public-service-commission/jobs/services/recruitment/students/federal-student-work-program.html)
        *   [Apply for a Social Insurance Number (SIN)](https://www.canada.ca/en/employment-social-development/services/sin.html)

*   [Immigration and citizenship](https://www.canada.ca/en/government/system/digital-government/digital-government-innovations/responsible-use-ai.html#)
    *   [Immigration and citizenship: home](https://www.canada.ca/en/services/immigration-citizenship.html)

    *   [IRCC applications](https://www.canada.ca/en/immigration-refugees-citizenship/services/application.html)
    *   [Visit Canada](https://www.canada.ca/en/immigration-refugees-citizenship/services/visit-canada.html)
    *   [Live in Canada permanently](https://www.canada.ca/en/immigration-refugees-citizenship/services/immigrate-canada.html)
    *   [Work in Canada temporarily](https://www.canada.ca/en/immigration-refugees-citizenship/services/work-canada.html)
    *   [Study in Canada](https://www.canada.ca/en/immigration-refugees-citizenship/services/study-canada.html)
    *   [Refugees and asylum](https://www.canada.ca/en/immigration-refugees-citizenship/services/refugees.html)
    *   [International Experience Canada (IEC)](https://ircc.canada.ca/iec/index.asp)
    *   [Passports and other travel documents](https://www.canada.ca/en/immigration-refugees-citizenship/services/canadian-passports.html)
    *   [Citizenship](https://www.canada.ca/en/immigration-refugees-citizenship/services/canadian-citizenship.html)
    *   [Permanent resident (PR) cards and status](https://www.canada.ca/en/immigration-refugees-citizenship/services/permanent-residents.html)
    *   [Settling in Canada as a newcomer](https://www.canada.ca/en/immigration-refugees-citizenship/services/settle-canada.html)
    *   [International adoption](https://www.canada.ca/en/immigration-refugees-citizenship/services/canadians/adopt-child-abroad.html)
    *   [Explore immigration programs](https://ircc.canada.ca/explore-programs/index.asp)
    *   [Immigration fraud and scams](https://www.canada.ca/en/immigration-refugees-citizenship/services/protect-fraud.html)
    *   [Inadmissibility, enforcement and appeals](https://www.canada.ca/en/services/immigration-citizenship/enforcement-violations.html)

    *   [Most requested](https://www.canada.ca/en/government/system/digital-government/digital-government-innovations/responsible-use-ai.html#)
        *   [Sign in to your IRCC account](https://www.canada.ca/en/immigration-refugees-citizenship/services/application/ircc-accounts.html)
        *   [Check your application status](https://www.canada.ca/en/immigration-refugees-citizenship/services/application/check-status.html)
        *   [Current processing times](https://www.canada.ca/en/immigration-refugees-citizenship/services/application/check-processing-times.html)
        *   [Find an application form](https://www.canada.ca/en/immigration-refugees-citizenship/services/application/application-forms-guides.html)
        *   [Portals for representatives and partners](https://www.canada.ca/en/immigration-refugees-citizenship/corporate/partners-service-providers.html)

*   [Travel and tourism](https://www.canada.ca/en/government/system/digital-government/digital-government-innovations/responsible-use-ai.html#)
    *   [Travel and tourism: home](https://travel.gc.ca/)

    *   [Travel advice and advisories](https://travel.gc.ca/travelling/advisories)
    *   [Travel outside Canada](https://travel.gc.ca/travelling)
    *   [Air travel](https://travel.gc.ca/air)
    *   [Canadian passports and travel documents](https://www.canada.ca/en/immigration-refugees-citizenship/services/canadian-passports.html)
    *   [Stay connected](https://travel.gc.ca/stay-connected)
    *   [Assistance outside Canada](https://travel.gc.ca/assistance)
    *   [Visit Canada](https://www.canada.ca/en/immigration-refugees-citizenship/services/visit-canada.html?outside)
    *   [Return or travel to Canada](https://travel.gc.ca/returning)
    *   [Canadian attractions, events and experiences](https://travel.gc.ca/canadian-tourism)

    *   [Most requested](https://www.canada.ca/en/government/system/digital-government/digital-government-innovations/responsible-use-ai.html#)
        *   [Emergency assistance abroad](https://travel.gc.ca/assistance/emergency-assistance)
        *   [Find out if you need a visa to travel to Canada](https://www.canada.ca/en/immigration-refugees-citizenship/services/visit-canada/check-visa-eta.html)
        *   [Apply for an eTA](https://www.canada.ca/en/immigration-refugees-citizenship/services/visit-canada/eta.html)
        *   [Apply for NEXUS](https://www.cbsa-asfc.gc.ca/services/travel-voyage/prog/nexus/menu-eng.html)
        *   [Register as a Canadian abroad](https://travel.gc.ca/travelling/registration)
        *   [Travel insurance](https://travel.gc.ca/travelling/documents/travel-insurance)

*   [Business and industry](https://www.canada.ca/en/government/system/digital-government/digital-government-innovations/responsible-use-ai.html#)
    *   [Business and industry: home](https://www.canada.ca/en/services/business.html)

    *   [Starting a business](https://www.canada.ca/en/services/business/start.html)
    *   [Business taxes](https://www.canada.ca/en/services/business/taxes.html)
    *   [Business financing and support](https://innovation.ised-isde.canada.ca/s/?language=en_CA)
    *   [Federal corporations](https://ised-isde.canada.ca/site/corporations-canada/en)
    *   [Maintaining your business](https://www.canada.ca/en/services/business/maintaingrowimprovebusiness.html)
    *   [Permits, licences and regulations](https://www.canada.ca/en/services/business/permits.html)
    *   [Hiring and managing employees](https://www.canada.ca/en/services/business/hire.html)
    *   [International trade and investment](https://international.canada.ca/en/services/business/trade)
    *   [Intellectual property and copyright](https://www.canada.ca/en/services/business/ip.html)
    *   [Research and business intelligence](htt

[Showing characters 0-10,000 of 44,678. Call read_url with start=10000 to read the next part.]
```

## Turn 7

_Model call: 23,715 input tokens, 641 output tokens_

**Tool call** `read_url` (id `call_52f8f7555f5c478983dffe1f`):

```json
{
  "start": 30000,
  "url": "https://www.canada.ca/en/government/system/digital-government/digital-government-innovations/responsible-use-ai.html"
}
```
**Tool call** `web_search` (id `call_945404ff0ac74ca8bdc619d4`):

```json
{
  "query": "Canada federal public service generative AI guide public servants news coverage \"generative AI\" Treasury Board guidance ChatGPT"
}
```
**Tool result** `read_url` (id `call_52f8f7555f5c478983dffe1f`, 10,101 characters):

```
Canada](https://www.treaty-accord.gc.ca/index.aspx?lang=eng)
        *   [Project Browser](https://w05.international.gc.ca/projectbrowser-banqueprojets/?lang=eng&_ga=2.177755878.2114306412.1738083014-1550541383.1711385614)
        *   [Contact a foreign representative in Canada](https://www.international.gc.ca/protocol-protocole/reps.aspx?lang=eng)
        *   [Canada-United States trade: federal supports](https://www.canada.ca/en/government/united-states-canada.html)

*   [Money and finances](https://www.canada.ca/en/government/system/digital-government/digital-government-innovations/responsible-use-ai.html#)
    *   [Money and finances Finance: home](https://www.canada.ca/en/services/finance.html)

    *   [Managing your money](https://www.canada.ca/en/services/finance/manage.html)
    *   [Consumer affairs](https://www.canada.ca/en/services/finance/consumer-affairs.html)
    *   [Debt and borrowing](https://www.canada.ca/en/services/finance/debt.html)
    *   [Education funding](https://www.canada.ca/en/services/finance/educationfunding.html)
    *   [Pensions and retirement](https://www.canada.ca/en/services/finance/pensions.html)
    *   [Financial tools and calculators](https://www.canada.ca/en/services/finance/tools.html)
    *   [Savings and investments](https://www.canada.ca/en/services/finance/savings.html)
    *   [Taxes](https://www.canada.ca/en/services/taxes.html)
    *   [Financial literacy programs](https://www.canada.ca/en/financial-consumer-agency/services/financial-literacy-programs.html)
    *   [Business financing and support](https://innovation.ised-isde.canada.ca/s/?language=en_CA)
    *   [Protection from frauds and scams](https://www.canada.ca/en/services/finance/fraud.html)
    *   [Financial and money services regulation](https://www.canada.ca/en/services/business/permits/federallyregulatedindustrysectors/financialservicesregulation.html)
    *   [Insolvency](https://www.canada.ca/en/services/finance/bankruptcy.html)

    *   [Most requested](https://www.canada.ca/en/government/system/digital-government/digital-government-innovations/responsible-use-ai.html#)
        *   [Canada's response to U.S. tariffs](https://www.canada.ca/en/department-finance/programs/international-trade-finance-policy/canadas-response-us-tariffs.html)
        *   [Housing](https://www.canada.ca/en/services/finance/manage/housing.html)
        *   [Student loans](https://www.canada.ca/en/services/benefits/education/student-aid.html)
        *   [Credit report and scores](https://www.canada.ca/en/financial-consumer-agency/services/credit-reports-score.html)
        *   [Mortgages](https://www.canada.ca/en/financial-consumer-agency/services/mortgages.html)
        *   [Make a budget](https://itools-ioutils.fcac-acfc.gc.ca/BP-PB/budget-planner)
        *   [Set up or change direct deposit](https://www.canada.ca/en/public-services-procurement/services/payments-to-from-government/direct-deposit.html)
        *   [Find a bankruptcy or insolvency record](https://www.ic.gc.ca/app/scr/bsf-osb/ins/login.html?lang=eng)

*   [Science and innovation](https://www.canada.ca/en/government/system/digital-government/digital-government-innovations/responsible-use-ai.html#)
    *   [Science and innovation: home](https://www.canada.ca/en/services/science.html)

    *   [Research funding and awards](https://www.canada.ca/en/services/science/researchfunding.html)
    *   [R&D and innovation](https://www.canada.ca/en/services/science/innovation.html)
    *   [Science subjects](https://www.canada.ca/en/services/science/sciencesubjects.html)
    *   [Health emergency readiness](https://ised-isde.canada.ca/site/ised/en/programs-and-initiatives/health-emergency-readiness-canada)
    *   [Research institutes and facilities](https://www.canada.ca/en/services/science/institutes.html)
    *   [Open data, statistics and archives](https://www.canada.ca/en/services/science/open-data.html)
    *   [Science education resources](https://www.canada.ca/en/services/science/educationalresources.html)
    *   [Intellectual property and copyright](https://www.canada.ca/en/services/business/ip.html)
    *   [Directory of scientists and research professionals](https://www.canada.ca/en/services/science/scientistsdirectory.html)
    *   [Our environment](https://www.canada.ca/en/services/environment/our-environment.html)
    *   [Federal Open Science Repository of Canada](https://open-science.canada.ca/home?utm_campaign=fosrc-promo-jan-2024&utm_medium=pog&utm_source=ised-e)

    *   [Most requested](https://www.canada.ca/en/government/system/digital-government/digital-government-innovations/responsible-use-ai.html#)
        *   [Grants for technological innovation (IRAP)](https://nrc.canada.ca/en/support-technology-innovation/financial-support-technology-innovation)
        *   [National building codes](https://nrc.canada.ca/en/certifications-evaluations-standards/codes-canada/codes-canada-publications)
        *   [Federal Science Libraries Network](https://science-libraries.canada.ca/eng/home/)
        *   [Check sunrise and sunset times](https://nrc.canada.ca/en/research-development/products-services/software-applications/sun-calculator/)
        *   [Official times across Canada](https://nrc.canada.ca/en/web-clock/)
        *   [Live view of northern lights cam](https://www.asc-csa.gc.ca/eng/astronomy/northern-lights/auroramax-observatory.asp)

*   [Manage life events](https://www.canada.ca/en/government/system/digital-government/digital-government-innovations/responsible-use-ai.html#)
    *   [Manage life events: home](https://www.canada.ca/en/services/life-events.html)

    *   [Welcoming a child](https://www.canada.ca/en/services/life-events/child.html)
    *   [Learn and plan for your retirement](https://www.canada.ca/en/services/life-events/retirement.html)
    *   [What to do when someone dies](https://www.canada.ca/en/services/life-events/death.html)

    *   [Most requested](https://www.canada.ca/en/government/system/digital-government/digital-government-innovations/responsible-use-ai.html#)
        *   [Sign in to a Government of Canada account](https://www.canada.ca/en/government/sign-in-online-account.html)
        *   [CPP payment amounts](https://www.canada.ca/en/services/benefits/publicpensions/cpp/payment-amounts.html)
        *   [Benefits payments dates](https://www.canada.ca/en/services/benefits/calendar.html)
        *   [Canada child benefit](https://www.canada.ca/en/revenue-agency/services/child-family-benefits/canada-child-benefit-overview.html)
        *   [Canadian Retirement Income Calculator](https://www.canada.ca/en/services/benefits/publicpensions/cpp/retirement-income-calculator.html)
        *   [Prepare tax returns for someone who died](https://www.canada.ca/en/revenue-agency/services/tax/individuals/life-events/doing-taxes-someone-died.html)
        *   [Get a birth certificate](https://www.canada.ca/en/services/life-events/child/register-birth.html)
        *   [Apply for a SIN](https://www.canada.ca/en/employment-social-development/services/sin.html)

## You are here:

1.   [Canada.ca](https://www.canada.ca/en.html)
2.   [About government](https://www.canada.ca/en/government/system.html)
3.   [Government in a digital age](https://www.canada.ca/en/government/system/digital-government.html)
4.   [Digital government innovation](https://www.canada.ca/en/government/system/digital-government/digital-government-innovations.html)

# Responsible use of artificial intelligence in government

Artificial intelligence (AI) technologies offer promise for improving how the Government of Canada provides digital services. As we explore the use of AI in government programs and services, we are ensuring it’s governed by clear values, ethics and laws.

## Most requested

*   [_Guide on the Use of Generative Artificial Intelligence_](https://www.canada.ca/en/government/system/digital-government/digital-government-innovations/responsible-use-ai/guide-use-generative-ai.html)
*   [Start an algorithmic impact assessment](https://open.canada.ca/aia-eia-js/?lang=en)
*   [_Directive on Automated Decision-Making_](https://www.tbs-sct.canada.ca/pol/doc-eng.aspx?id=32592)
*   [Guidance on service and digital](https://www.canada.ca/en/government/system/digital-government/guideline-service-digital.html#ToC4_5)
*   [Consultations on the AI Strategy: What we heard report](https://www.canada.ca/en/government/system/digital-government/digital-government-innovations/responsible-use-ai/consultations-ai-strategy-federal-public-service-what-we-heard.html)

## Services and information

### [AI strategy for the federal public service](https://www.canada.ca/en/government/system/digital-government/digital-government-innovations/responsible-use-ai/gc-ai-strategy-overview.html)

How the GC plans to use AI; reports on consultations on the strategy and progress made

### [Guidance on generative AI](https://www.canada.ca/en/government/system/digital-government/digital-government-innovations/responsible-use-ai/generative-ai.html)

How to generate AI content responsibly, disclose AI use, and work with AI agents; policy implementation notices

### [Automated decision-making](https://www.canada.ca/en/government/system/digital-government/digital-government-innovations/responsible-use-ai/automated-decision-making.html)

Using AI in decision-making in the GC; peer reviews of automated decision-making systems; information about algorithmic impact assessments

### [AI ethics and responsibilities](https://www.canada.ca/en/government/system/digital-government/digital-government-innovations/responsible-use-ai/ai-ethics-responsibilities.html)

Principles of responsible AI use, data ethics and de-identification of data

### [Advancing AI](https://www.canada.ca/en/government/system/digital-government/digital-government-innovations/responsible-use-ai/advancing-ai.html)

Progress in the GC; Canada’s AI ecosystem; international engagement

### [Government of Canada Artificial Intellige

[Showing characters 30,000-40,000 of 44,725. Call read_url with start=40000 to read the next part.]
```
**Tool result** `web_search` (id `call_945404ff0ac74ca8bdc619d4`, 6,769 characters):

```
Search results for "Canada federal public service generative AI guide public servants news coverage "generative AI" Treasury Board guidance ChatGPT" (searched 2026-11-26):

[1] Canadian public servants issued guidelines for using generative AI
URL: https://www.globalgovernmentforum.com/canadian-public-servants-issued-guidelines-for-using-generative-ai
Excerpt: The preliminary guidelines define generative AI as an information technology “that would ordinarily require biological brainpower to accomplish, such as making sense of spoken language, learning behaviours, or solving problems”.   
  
They were announced to mark “the initial stages” of the Canadian public service’s “[recognition of] the importance of AI”, according to Anita Anand, president of the Treasury Board of Canada. [...] Designed to complement government’s existing directive to departments on AI, the new rules are expected to undergo updates over time. Their core aim, is to tackle instances where the use of AI constitutes malpractice, resulting in a cybersecurity threat, misinformation, or where generative AI tools like ChatGPT and Google Bard produce discriminatory outcomes. [...] “These guidelines…will make sure that employees are aware of not using private or secret information, making sure that content is factual, making sure that we are transparent about its use, and making sure that we’re complying with laws and policies as well.”

Read more: One in ten Canadian public servants already using AI for work purposes

## Call for government to be clear about ‘no-go zones’ for AI

[2] Guide on the use of generative artificial intelligence - Canada.ca
URL: https://www.canada.ca/en/government/system/digital-government/digital-government-innovations/responsible-use-ai/generative-ai/guide-use-generative-ai.html
Excerpt: This guide also seeks to raise awareness and foster coordination among federal institutions. It highlights the importance of engaging key stakeholders before deploying generative AI tools for public use and before using them for purposes such as service delivery.

Stakeholders include:

- legal counsel
- privacy and security experts
- the Office of the Chief Information Officer at the Treasury Board of Canada Secretariat (TBS)
- bargaining agents
- advisory groups
- clients of GC services [...] Public servants must not input personal information into publicly available online generative AI tools. Doing so would constitute an unlawful disclosure of the information because the supplier might store a copy of the information. Public servants may, however, input personal information into generative AI systems that are controlled or configured by the government when the appropriate privacy and security controls are in place. When using a generative AI tool controlled by the institution, [...] Federal institutions should experiment with low-risk uses before they consider higher‑risk uses. They should always tailor best practices and risk‑mitigation measures to each use.

When deciding whether to use generative AI tools, public servants should refer to the guide to ethical decision-making (section 6 of Values Alive: A Discussion Guide to the “Values and Ethics Code for the Public Sector”).

[3] Canada launches first-ever Artificial Intelligence Strategy for the federal public service
URL: https://finance.yahoo.com/news/canada-launches-first-ever-artificial-200000250.html
Excerpt: - Every 2 years, the government will aim to update the Strategy to ensure it remains relevant and responsive.
- A
  
  Guide on the use of Generative AI is available for public servants to assess the risks associated with generative AI and use it responsibly. [...] Today, the Honourable Ginette Petitpas Taylor, President of the Treasury Board, launched Canada's first AI Strategy for the federal public service at the University of Waterloo, a hub for emerging technology and Canadian talent. Announcing the Strategy at the Waterloo Data and Artificial Intelligence Institute underscores the government's commitment to research and innovation in AI to improve digital service delivery. [...] Quote

"Today's announcement positions Canada as a global leader in the responsible use of AI in the public service. With the first-ever AI Strategy for the public service, we're laying the groundwork to leverage the potential of this technology to deliver the best possible services to Canadians."

\- The Honourable Ginette Petitpas Taylor, President of the Treasury Board

Quick Facts

[4] Beverley Nadiger on Facebook: "are you able to read this OTTAWA — Government employees shouldn’t rely on tools like ChatGPT at the …"
URL: https://www.facebook.com/groups/letstalkalbertaindependence/posts/1400401967224675
Excerpt: Public servants should also use caution in generating content for use in public communication, the guide said, noting it is “critical to ensure that outputs are trusted given the potential reach and impact of public communications.”

Employees can use generative AI for research during policy development, but not to “recommend, make or interpret policy.” [...] The government’s guide says federal institutions should be exploring how they “could use generative AI tools to support their operations and improve outcomes for Canadians,” noting that given the increasing adoption of these technologies, “their use in government will help keep pace with the evolving digital landscape.” [...] That’s a concern recently expressed by a union representing public service employees in a brief to a House of Commons committee studying an AI-regulation bill. The Professional Institute of the Public Service of Canada said it was “informed in discussions with the Treasury Board that there would be layoffs as a result of AI.”

[5] ChatGPT and Generative AI: Guide to the Most Talked-About Technology - Business Insider
URL: https://www.businessinsider.com/generative-ai-chatgpt-guide-to-most-talked-technology-2023-may
Excerpt: ChatGPT brought generative AI into the limelight when it hit 1 million users in five days. But how valid is the buzz around ChatGPT? We unpack what you need to know: How does generative AI work? Who are the key players? Is ChatGPT ready for prime time? And most importantly: How will the technology change the way we do business? [...] What is ChatGPT and how does it fit into the equation? ChatGPT is a conversational AI model built by OpenAI (GPT stands for generative pretrained transformer). Released November 30, 2022, as a proof of concept, it gained 1 million users in five days and blasted into the popular consciousness. Despite the excitement many limitations and challenges remain and OpenAI CEO Sam Altman tweeted a warning about ChatGPT: "it's a mistake to be relying on it for anything important right now."
```

## Turn 8

_Model call: 28,217 input tokens, 700 output tokens_

**Tool call** `read_url` (id `call_12a8ed4c499147db9cf35ea8`):

```json
{
  "start": 0,
  "url": "https://www.canada.ca/en/government/system/digital-government/digital-government-innovations/responsible-use-ai/generative-ai.html"
}
```
**Tool call** `web_search` (id `call_8813904e0dd346469a5a68de`):

```json
{
  "query": "IEA data centres electricity water consumption artificial intelligence report 2024"
}
```
**Tool call** `web_search` (id `call_83c6cd53c286449f97101e13`):

```json
{
  "query": "\"Treasury Board\" generative AI guide criticism unions \"no-go zones\" public servants ChatGPT Ottawa Citizen"
}
```
**Tool result** `web_search` (id `call_8813904e0dd346469a5a68de`, 6,770 characters):

```
Search results for "IEA data centres electricity water consumption artificial intelligence report 2024" (searched 2026-11-26):

[1] Executive summary - Energy and AI - IEA
URL: https://www.iea.org/reports/energy-and-ai/executive-summary
Excerpt: Data centres accounted for around 1.5% of the world’s electricity consumption in 2024, or 415 terawatt-hours (TWh). The United States accounted for the largest share of global data centre electricity consumption in 2024 (45%), followed by China (25%) and Europe (15%). Globally, data centre electricity consumption has grown by around 12% per year since 2017, more than four times faster than the rate of total electricity consumption. AI-focused data centres can draw as much electricity as [...] ### Data centres account for a small share of global electricity consumption today, but their local impacts are far more pronounced

Global investment in data centres has nearly doubled since 2022 and amounted to half a trillion dollars in 2024. This investment boom has led to growing concerns about skyrocketing electricity demand. [...] ### Concerns that AI could accelerate climate change appear overstated, as do expectations that AI alone will address the issue

Emissions from electricity use by data centres grows from 180 million tonnes (Mt) today to 300 Mt in the Base Case by 2035, and up to 500 Mt in the Lift-Off Case. While these emissions remain below 1.5% of the total energy sector emissions in this period, data centres are among the fastest growing sources of emissions.

[2] Energy demand from AI - Energy and AI - IEA
URL: https://www.iea.org/reports/energy-and-ai/energy-demand-from-ai
Excerpt: Data centres – at least at the scale seen today – are relatively new actors in the energy system at the global level. Today, electricity consumption from data centres is estimated to amount to around 415 terawatt hours (TWh), or about 1.5% of global electricity consumption in 2024. It has grown at 12% per year over the last five years. [...] - Servers are computers that process and store data. They can be equipped with central processing units (CPUs) and specialised accelerators such as graphics processing units (GPUs). On average they account for around 60% of electricity demand in modern data centres, although this varies greatly between data centre types.

### Share of electricity consumption by data centre and equipment type, 2024

Open [...] Despite the strong increase, data centre electricity demand growth accounts for less than 10% of global electricity demand growth between 2024 and 2030 in the Base Case. Other key drivers, such as industry output growth and electrification, the deployment of electric vehicles, and the adoption of air conditioning, lead the way. However, while the absolute growth may appear smaller, data centres, unlike electric vehicles, tend to concentrate in specific locations, making their integration into

[3] Energy and AI - Microsoft .NET
URL: https://iea.blob.core.windows.net/assets/de9dea13-b07d-42c5-a398-d1b3ae17d866/EnergyandAI.pdf
Excerpt: 14 International Energy Agency | Energy and AI Data centres accounted for around 1.5% of the world’s electricity consumption in 2024, or 415 terawatt-hours (TWh). The United States accounted for the largest share of global data centre electricity consumption in 2024 (45%), followed by China (25%) and Europe (15%). Globally, data centre electricity consumption has grown by around 12% per year since 2017, more than four times faster than the rate of total electricity consumption. AI-focused data [...] The share of these different components in data centre electricity consumption varies greatly by data centre type, depending on the nature and efficiency of the equipment installed. Figure 2.2 presents the typical breakdown for different data centre types in operation today. Figure 2.2 ⊳ Share of electricity consumption by data centre and equipment type, 2024 IEA. CC BY 4.0. Hyperscale data centres are the most efficient, with the bulk of electricity going to servers and other IT equipment [...] Chapter 2 | Energy for AI 57 2 Figure 2.5 ⊳ Estimated data centre electricity demand due to AI, 2020-2030 IEA. CC BY 4.0. Estimates of the share of AI in total data centre electricity consumption vary widely and are based at best on imperfect proxies Sources: IEA analysis based on data from Deloitte (2024), Gartner (2024), Goldman Sachs (2024), Schneider Electric (2024), SemiAnalysis (2024), and Shehabi, et al., (2024). However, this is an imperfect proxy for total AI electricity consumption.

[4] USA Data Center Electricity Demand Projected to Triple
URL: https://finance.yahoo.com/news/usa-data-center-electricity-demand-161558482.html
Excerpt: "Today, electricity consumption from data centers is estimated to amount to around 415 TWh, or about 1.5 percent of global electricity consumption in 2024. It has grown at 12 percent per year over the last five years," it added.

Take control of your future.  
Search THOUSANDS of Oil & Gas jobs on Rigzone.com  
 Search Now >>

The IEA noted in its report that the rise of AI is accelerating the deployment of high-performance accelerated servers, leading to greater power density in data centers. [...] In data sent to Rigzone, the IEA modelled that U.S. data center electricity consumption stood at 108.41 TWh in 2020, 134.07 TWh in 2022, 154.07 TWh in 2023, and 182.61 TWh in 2024. The IEA projected in its AI report that this demand will rise to well over 200 TWh in 2025, more than 250 TWh in 2026, over 300 TWh in 2027, around 350 TWh in 2028, and a little bit under 400 TWh in 2029. [...] The IEA, which described U.S. data center electricity demand figures as the closest proxy available for the energy consumption of artificial intelligence (AI), modelled that U.S. data center electricity demand came in at 120.65 Terawatt hours (TWh) in 2021, IEA data sent to Rigzone showed. In other data sent to Rigzone, which is available in the IEA's Energy and AI report released earlier this year, the IEA forecasts that this consumption will rise to well over 400 TWh in 2030, in its base

[5] Data centres may not keep up with AI capacity requirements – analysis
URL: https://finance.yahoo.com/news/data-centres-may-not-keep-172404365.html
Excerpt: "The IEA estimates that data centres accounted for around 1.5% of the world's electricity consumption in 2024, or 415TWh. Data centre electricity consumption will more than double to around 945TWh by 2030, representing just under 3% of total global electricity consumption in 2030 (base case scenario)."

"Data centres may not keep up with AI capacity requirements – analysis " was originally created and published by Verdict, a GlobalData owned brand.

Terms  and Privacy Policy

Privacy Dashboard
```
**Tool result** `web_search` (id `call_83c6cd53c286449f97101e13`, 7,513 characters):

```
Search results for ""Treasury Board" generative AI guide criticism unions "no-go zones" public servants ChatGPT Ottawa Citizen" (searched 2026-11-26):

[1] Beverley Nadiger on Facebook: "are you able to read this OTTAWA — Government employees shouldn’t rely on tools like ChatGPT at the …"
URL: https://www.facebook.com/groups/letstalkalbertaindependence/posts/1400401967224675
Excerpt: That’s a concern recently expressed by a union representing public service employees in a brief to a House of Commons committee studying an AI-regulation bill. The Professional Institute of the Public Service of Canada said it was “informed in discussions with the Treasury Board that there would be layoffs as a result of AI.” [...] Public servants should also use caution in generating content for use in public communication, the guide said, noting it is “critical to ensure that outputs are trusted given the potential reach and impact of public communications.”

Employees can use generative AI for research during policy development, but not to “recommend, make or interpret policy.” [...] It also asked for more transparency on use of AI by government for hiring and evaluating public servants. “Employee evaluation with AI can imply some form of worker surveillance. We are asking for complete transparency on how AI is being used as regards to evaluation, monitoring, surveillance and hiring of federal government and agency employees,” the union said.

[2] Federal government issues new rules for public servants using AI | Radio-Canada.ca
URL: https://ici.radio-canada.ca/rci/en/news/2009454/federal-government-issues-new-rules-for-public-servants-using-ai
Excerpt: It only proposes that the government 'be careful' on how they use AI, Carr said. 'Be careful' is a very subjective term. What we're really looking for is that there are strict regulations or guidelines, where there are go and no-go zones.

WATCH: Treasury Board president discusses new rules for AI use

Ottawa's AI guidelines will address privacy, transparency: Anand (new window) [...] 1. Home
2. Politics

# Federal government issues new rules for public servants using AI

Anand says government will monitor to ensure AI tools aren't biased and don't discriminate

The federal government has introduced new guidelines for employees who want to use artificial intelligence tools like ChatGPT on the job to ensure the technology is being used responsibly, says Treasury Board President Anita Anand. [...] The legal obligation continues to remain on all employees regardless of these guidelines, Anand said. The guidelines are on top of those existing obligations.

While the Treasury Board's guidelines for generative AI recommend that federal institutions explore ways to use these tools, it also warns of risks — including cybersecurity threats, bias, violations of privacy and inaccurate information.

[3] Canadian public servants issued guidelines for using generative AI
URL: https://www.globalgovernmentforum.com/canadian-public-servants-issued-guidelines-for-using-generative-ai
Excerpt: Jennifer Carr, president of the Professional Institute of the Public Service of Canada, took issue with the speed with the which the guidelines were introduced, saying her union (which includes government computer experts) had not been properly consulted. She added that the guidelines did not contain sufficiently clear delineations of good and bad practice.

“It only proposes that the government ‘be careful’ on how they use AI. “‘Be careful’ is a very subjective term,” she said. [...] “What we’re really looking for is that there are strict regulations or guidelines, where there are go and no-go zones.”

Carr said finally that public servants and citizens alike would need further reassurance that AI did not put jobs and services at risk by outsourcing decisions to computers. [...] “These guidelines…will make sure that employees are aware of not using private or secret information, making sure that content is factual, making sure that we are transparent about its use, and making sure that we’re complying with laws and policies as well.”

Read more: One in ten Canadian public servants already using AI for work purposes

## Call for government to be clear about ‘no-go zones’ for AI

[4] Federal unions watching AI's usage in the workplace closely | CBC News
URL: https://www.cbc.ca/news/canada/ottawa/federal-unions-watching-ai-s-usage-in-the-workplace-closely-1.6926866
Excerpt: A dozen departments contacted by Radio-Canada indicated that they follow the "directive on automated decision-making" — a document developed by the federal Treasury Board Secretariat, as a guideline for public servants' use of AI.

The federal government website says the directive was made "to ensure that automated decision systems are deployed in a manner that reduces risks to clients, federal institutions and Canadian society." [...] Ottawa

# Federal unions watching AI's usage in the workplace closely

## CRA, National Defence among departments exploring ChatGPT among other technologies

A phone with an orange app on it.

The use of artificial intelligence (AI) technology is now authorized in certain contexts for federal government workers, but some experts and unions are calling for caution in how it's deployed. [...] Camille Awada, president of the Canadian Association of Professional Employees (CAPE), the third-largest union for federal workers, said the union is monitoring the situation.

"CAPE understands that there is no avoiding AI entirely, but we advise the government to see how it can assist federal public servants in doing their jobs more efficiently without the loss of quality and ensuring employment rights are protected through the process of any AI implementation," Awada said.

[5] Guide on the use of generative artificial intelligence - Canada.ca
URL: https://www.canada.ca/en/government/system/digital-government/digital-government-innovations/responsible-use-ai/generative-ai/guide-use-generative-ai.html
Excerpt: This guide also seeks to raise awareness and foster coordination among federal institutions. It highlights the importance of engaging key stakeholders before deploying generative AI tools for public use and before using them for purposes such as service delivery.

Stakeholders include:

- legal counsel
- privacy and security experts
- the Office of the Chief Information Officer at the Treasury Board of Canada Secretariat (TBS)
- bargaining agents
- advisory groups
- clients of GC services [...] Public servants must not input personal information into publicly available online generative AI tools. Doing so would constitute an unlawful disclosure of the information because the supplier might store a copy of the information. Public servants may, however, input personal information into generative AI systems that are controlled or configured by the government when the appropriate privacy and security controls are in place. When using a generative AI tool controlled by the institution, [...] Although these tools present challenges and concerns, they also offer potential benefits to public servants and federal institutions. For example, they can enhance productivity through increased efficiency and quality of outputs in analytical and writing tasks in several domains. Footnote 11Footnote 12 More analysis is needed to determine the most appropriate and beneficial uses of these tools by federal institutions. Experimentation, coupled with performance measurement and analysis, is needed
```
**Tool result** `read_url` (id `call_12a8ed4c499147db9cf35ea8`, 10,096 characters):

```
Title: Generative AI - Canada.ca

URL Source: https://www.canada.ca/en/government/system/digital-government/digital-government-innovations/responsible-use-ai/generative-ai.html

Markdown Content:
*   [Skip to main content](https://www.canada.ca/en/government/system/digital-government/digital-government-innovations/responsible-use-ai/generative-ai.html#wb-cont)
*   [Skip to "About government"](https://www.canada.ca/en/government/system/digital-government/digital-government-innovations/responsible-use-ai/generative-ai.html#wb-info)
*   [Switch to basic HTML version](https://www.canada.ca/en/government/system/digital-government/digital-government-innovations/responsible-use-ai/generative-ai.html?wbdisable=true)

## Language selection

*   [Français fr](https://www.canada.ca/fr/gouvernement/systeme/gouvernement-numerique/innovations-gouvernementales-numeriques/utilisation-responsable-ai/ia-generative.html)

[![Image 1: Government of Canada](https://www.canada.ca/etc/designs/canada/wet-boew/assets/sig-blk-en.svg) / Gouvernement du Canada](https://www.canada.ca/en.html)

## Search

Search Canada.ca 

Search

* * *

## Menu

Main Menu. Press the SPACEBAR to expand or the escape key to collapse this menu. Use the Up and Down arrow keys to choose a submenu item. Press the Enter or Right arrow key to expand it, or the Left arrow or Escape key to collapse it. Use the Up and Down arrow keys to choose an item on that level and the Enter key to access it.

Main Menu 
*   [Jobs and the workplace](https://www.canada.ca/en/government/system/digital-government/digital-government-innovations/responsible-use-ai/generative-ai.html#)
    *   [Jobs: home](https://www.canada.ca/en/services/jobs.html)

    *   [Job Bank](https://www.jobbank.gc.ca/findajob)
    *   [Government of Canada jobs](https://www.canada.ca/en/services/jobs/opportunities/government.html)
    *   [Youth and student employment](https://www.canada.ca/en/services/jobs/youth.html)
    *   [Jobs in national security and defence](https://www.canada.ca/en/services/defence/jobs.html)
    *   [Moving within Canada to work](https://www.canada.ca/en/employment-social-development/programs/labour-mobility.html)
    *   [Funding for jobs and training](https://www.canada.ca/en/employment-social-development/services/funding/programs.html)
    *   [Training](https://www.canada.ca/en/services/jobs/training.html)
    *   [Hiring and managing employees](https://www.canada.ca/en/services/business/hire.html)
    *   [Starting a business](https://www.canada.ca/en/services/business/start.html)
    *   [Employment Insurance benefits and leave](https://www.canada.ca/en/services/benefits/ei.html)
    *   [Workplace standards](https://www.canada.ca/en/services/jobs/workplace.html)
    *   [Pensions and retirement](https://www.canada.ca/en/services/finance/pensions.html)

    *   [Most requested](https://www.canada.ca/en/government/system/digital-government/digital-government-innovations/responsible-use-ai/generative-ai.html#)
        *   [Work in Canada - work permits](https://www.canada.ca/en/immigration-refugees-citizenship/services/work-canada.html)
        *   [Immigrate as a skilled worker](https://www.canada.ca/en/immigration-refugees-citizenship/services/immigrate-canada/express-entry.html)
        *   [Hire a temporary foreign worker](https://www.canada.ca/en/immigration-refugees-citizenship/services/work-canada/hire-temporary-foreign.html)
        *   [Federal Skilled Worker Program](https://www.canada.ca/en/immigration-refugees-citizenship/services/immigrate-canada/express-entry/who-can-apply/federal-skilled-workers.html)
        *   [View your records of employment](https://www.canada.ca/en/employment-social-development/services/my-account.html)
        *   [Submit a record of employment - employers](https://www.canada.ca/en/employment-social-development/programs/ei/ei-list/ei-roe/access-roe.html)
        *   [Federal Student Work Experience Program (FSWEP)](https://www.canada.ca/en/public-service-commission/jobs/services/recruitment/students/federal-student-work-program.html)
        *   [Apply for a Social Insurance Number (SIN)](https://www.canada.ca/en/employment-social-development/services/sin.html)

*   [Immigration and citizenship](https://www.canada.ca/en/government/system/digital-government/digital-government-innovations/responsible-use-ai/generative-ai.html#)
    *   [Immigration and citizenship: home](https://www.canada.ca/en/services/immigration-citizenship.html)

    *   [IRCC applications](https://www.canada.ca/en/immigration-refugees-citizenship/services/application.html)
    *   [Visit Canada](https://www.canada.ca/en/immigration-refugees-citizenship/services/visit-canada.html)
    *   [Live in Canada permanently](https://www.canada.ca/en/immigration-refugees-citizenship/services/immigrate-canada.html)
    *   [Work in Canada temporarily](https://www.canada.ca/en/immigration-refugees-citizenship/services/work-canada.html)
    *   [Study in Canada](https://www.canada.ca/en/immigration-refugees-citizenship/services/study-canada.html)
    *   [Refugees and asylum](https://www.canada.ca/en/immigration-refugees-citizenship/services/refugees.html)
    *   [International Experience Canada (IEC)](https://ircc.canada.ca/iec/index.asp)
    *   [Passports and other travel documents](https://www.canada.ca/en/immigration-refugees-citizenship/services/canadian-passports.html)
    *   [Citizenship](https://www.canada.ca/en/immigration-refugees-citizenship/services/canadian-citizenship.html)
    *   [Permanent resident (PR) cards and status](https://www.canada.ca/en/immigration-refugees-citizenship/services/permanent-residents.html)
    *   [Settling in Canada as a newcomer](https://www.canada.ca/en/immigration-refugees-citizenship/services/settle-canada.html)
    *   [International adoption](https://www.canada.ca/en/immigration-refugees-citizenship/services/canadians/adopt-child-abroad.html)
    *   [Explore immigration programs](https://ircc.canada.ca/explore-programs/index.asp)
    *   [Immigration fraud and scams](https://www.canada.ca/en/immigration-refugees-citizenship/services/protect-fraud.html)
    *   [Inadmissibility, enforcement and appeals](https://www.canada.ca/en/services/immigration-citizenship/enforcement-violations.html)

    *   [Most requested](https://www.canada.ca/en/government/system/digital-government/digital-government-innovations/responsible-use-ai/generative-ai.html#)
        *   [Sign in to your IRCC account](https://www.canada.ca/en/immigration-refugees-citizenship/services/application/ircc-accounts.html)
        *   [Check your application status](https://www.canada.ca/en/immigration-refugees-citizenship/services/application/check-status.html)
        *   [Current processing times](https://www.canada.ca/en/immigration-refugees-citizenship/services/application/check-processing-times.html)
        *   [Find an application form](https://www.canada.ca/en/immigration-refugees-citizenship/services/application/application-forms-guides.html)
        *   [Portals for representatives and partners](https://www.canada.ca/en/immigration-refugees-citizenship/corporate/partners-service-providers.html)

*   [Travel and tourism](https://www.canada.ca/en/government/system/digital-government/digital-government-innovations/responsible-use-ai/generative-ai.html#)
    *   [Travel and tourism: home](https://travel.gc.ca/)

    *   [Travel advice and advisories](https://travel.gc.ca/travelling/advisories)
    *   [Travel outside Canada](https://travel.gc.ca/travelling)
    *   [Air travel](https://travel.gc.ca/air)
    *   [Canadian passports and travel documents](https://www.canada.ca/en/immigration-refugees-citizenship/services/canadian-passports.html)
    *   [Stay connected](https://travel.gc.ca/stay-connected)
    *   [Assistance outside Canada](https://travel.gc.ca/assistance)
    *   [Visit Canada](https://www.canada.ca/en/immigration-refugees-citizenship/services/visit-canada.html?outside)
    *   [Return or travel to Canada](https://travel.gc.ca/returning)
    *   [Canadian attractions, events and experiences](https://travel.gc.ca/canadian-tourism)

    *   [Most requested](https://www.canada.ca/en/government/system/digital-government/digital-government-innovations/responsible-use-ai/generative-ai.html#)
        *   [Emergency assistance abroad](https://travel.gc.ca/assistance/emergency-assistance)
        *   [Find out if you need a visa to travel to Canada](https://www.canada.ca/en/immigration-refugees-citizenship/services/visit-canada/check-visa-eta.html)
        *   [Apply for an eTA](https://www.canada.ca/en/immigration-refugees-citizenship/services/visit-canada/eta.html)
        *   [Apply for NEXUS](https://www.cbsa-asfc.gc.ca/services/travel-voyage/prog/nexus/menu-eng.html)
        *   [Register as a Canadian abroad](https://travel.gc.ca/travelling/registration)
        *   [Travel insurance](https://travel.gc.ca/travelling/documents/travel-insurance)

*   [Business and industry](https://www.canada.ca/en/government/system/digital-government/digital-government-innovations/responsible-use-ai/generative-ai.html#)
    *   [Business and industry: home](https://www.canada.ca/en/services/business.html)

    *   [Starting a business](https://www.canada.ca/en/services/business/start.html)
    *   [Business taxes](https://www.canada.ca/en/services/business/taxes.html)
    *   [Business financing and support](https://innovation.ised-isde.canada.ca/s/?language=en_CA)
    *   [Federal corporations](https://ised-isde.canada.ca/site/corporations-canada/en)
    *   [Maintaining your business](https://www.canada.ca/en/services/business/maintaingrowimprovebusiness.html)
    *   [Permits, licences and regulations](https://www.canada.ca/en/services/business/permits.html)
    *   [Hiring and managing employees](https://www.canada.ca/en/services/business/hire.html)
    *   [International trade and investment](https://international.canada.ca/en/services/business/trade)
    *   [

[Showing characters 0-10,000 of 43,010. Call read_url with start=10000 to read the next part.]
```

## Turn 9

_Model call: 34,616 input tokens, 490 output tokens_

**Tool call** `read_url` (id `call_07e38b2171a149449b7bf35c`):

```json
{
  "start": 0,
  "url": "https://wiki.gccollab.ca/index.php?title=Responsible_Use_of_Generative_AI"
}
```
**Tool call** `web_search` (id `call_e56d5916475b4f60b890a99b`):

```json
{
  "query": "\"guide on the use of generative artificial intelligence\" canada.ca \"date modified\" 2026 OR 2025 updated version"
}
```
**Tool result** `web_search` (id `call_e56d5916475b4f60b890a99b`, 6,749 characters):

```
Search results for ""guide on the use of generative artificial intelligence" canada.ca "date modified" 2026 OR 2025 updated version" (searched 2026-11-26):

[1] Guide on the use of generative artificial intelligence - Canada.ca
URL: https://www.canada.ca/en/government/system/digital-government/digital-government-innovations/responsible-use-ai/generative-ai/guide-use-generative-ai.html
Excerpt: ##### Best practices for all users of generative AI in federal institutions

- Clearly communicate when and how you are using AI in interactions with the public.
- Inform users when text, audio or visual messages addressed to them are generated by AI.

##### Additional best practices for federal institutions deploying a generative AI tool [...] - Assess the impact of inaccurate outputs. Don’t use generative AI when factual accuracy or data integrity is needed.
- Strive to understand the quality and source of training data.
- Consider your ability to identify inaccurate content before you use generative AI. If you can’t confirm the quality of the content, don’t use it.
- Learn how to create effective prompts and provide feedback to refine outputs to minimize the generation of inaccurate content. [...] - Use generative AI tools hosted in net-zero or carbon-neutral data centres.
- Use generative AI tools only when relevant to program objectives and desired outcomes.
- Understand that the environmental impact of generative AI comes not only from its use but also from the training of the models and the manufacturing of the hardware components that run data centres, as well as the mining, manufacturing, assembly, transportation, and disposal of them.

[2] Responsible use of artificial intelligence in government - Canada.ca
URL: https://www.canada.ca/en/government/system/digital-government/digital-government-innovations/responsible-use-ai.html
Excerpt: ### Guidance on generative AI

How to generate AI content responsibly, disclose AI use, and work with AI agents; policy implementation notices

### Automated decision-making

Using AI in decision-making in the GC; peer reviews of automated decision-making systems; information about algorithmic impact assessments

### AI ethics and responsibilities

Principles of responsible AI use, data ethics and de-identification of data

### Advancing AI [...] # Responsible use of artificial intelligence in government

Artificial intelligence (AI) technologies offer promise for improving how the Government of Canada provides digital services. As we explore the use of AI in government programs and services, we are ensuring it’s governed by clear values, ethics and laws.

## Services and information

### AI strategy for the federal public service

How the GC plans to use AI; reports on consultations on the strategy and progress made [...] ### Advancing AI

Progress in the GC; Canada’s AI ecosystem; international engagement

### Government of Canada Artificial Intelligence Security Risk Management Framework

Guidance on managing security risks introduced or amplified by AI capabilities within information systems

## Innovation spotlight

### G7 public sector commitments

Commitments to accelerate public sector AI adoption from Canada’s 2025 G7 presidency

### Government of Canada AI Register

[3] Canada launches first-ever Artificial Intelligence Strategy for the federal public service
URL: https://finance.yahoo.com/news/canada-launches-first-ever-artificial-200000250.html
Excerpt: - Every 2 years, the government will aim to update the Strategy to ensure it remains relevant and responsive.
- A
  
  Guide on the use of Generative AI is available for public servants to assess the risks associated with generative AI and use it responsibly. [...] Accordingly, the Strategy will advance 4 key priority areas: establishing an AI Centre of Expertise to support and to help coordinate government-wide AI efforts; ensuring AI systems are secure and used responsibly; providing training and talent development pathways; and building trust through openness and transparency in how AI is used. [...] Through this Strategy, the government will be able to implement AI more efficiently by removing barriers to AI adoption that exist in departmental processes and legacy systems. It will promote more effective collaboration between government departments to identify successful AI-driven initiatives and implement them more widely. As well, the Strategy strengthens transparency and accountability for the responsible use of AI, ensuring the development of AI solutions that are ethical, inclusive,

[4] Guide to Artificial Intelligence ETFs
URL: https://finance.yahoo.com/news/guide-artificial-intelligence-etfs-154800573.html
Excerpt: Das noted that the $600 billion total addressable market comprises three major segments:

Chips and Systems ($300 Billion): The foundation of AI, hardware like GPUs and specialized AI chips will play a crucial role in powering AI applications across various industries.

Generative AI Software ($150 Billion): Software that generates content, such as ChatGPT, is gaining traction and transforming creative processes, content generation, and data analysis. [...] It is constructed on top of OpenAI's GPT-3 family of large language models and has been modified further using both supervised and reinforcement learning techniques. OpenAI has now been working on a more powerful version of the ChatGPT system called GPT-4, which is set to be released in 2023.

### How Hot Is Artificial Intelligence as an Investing Area?

[5] Top Artificial Intelligence Companies in Generative AI in Europe (Nov, 2026) - Tracxn
URL: https://tracxn.com/d/artificial-intelligence/ai-startups-in-generative-ai-in-europe/__ptjtgnVe6dbvtJD53hHI7EkBIqTDVREDOm5m0t2zk8A/companies
Excerpt: ## 1. Mistral AI

Provider of customizable, open-source artificial intelligence models and solutions for various applications. It is a company specializing in open-source large language models and generative AI, providing cutting-edge language models for various applications.

### Key facts about Mistral AI [...] Developer of conversational voice artificial intelligence agents for customer service. These software tools automate interactions by processing spoken language to handle inquiries, manage appointments, and resolve service requests. The technology integrates with existing enterprise systems to facilitate automated communication across voice, chat, and messaging channels. Engineering teams utilize provided development kits to build, deploy, and manage these automated agents within their own [...] within their own technical environments. The system tracks interaction metrics and provides analytical insights to monitor performance and manage automated workflows.
```
**Tool result** `read_url` (id `call_07e38b2171a149449b7bf35c`, 394 characters):

```
Title: https://wiki.gccollab.ca/extensions/SkinTweaksGCwiki/resources/images/sig-alt-en.svg

URL Source: https://wiki.gccollab.ca/index.php?title=Responsible_Use_of_Generative_AI

Final URL: https://wiki.gccollab.ca/extensions/SkinTweaksGCwiki/resources/images/sig-alt-en.svg

Published Time: Wed, 21 Oct 2026 19:59:15 GMT

Markdown Content:
A 213x20 small image, likely a logo, icon or avatar

```

## Turn 10

_Model call: 36,532 input tokens, 774 output tokens_

**Tool call** `web_search` (id `call_a5f8560c115a40389269c785`):

```json
{
  "query": "\"Government of Canada\" September 2023 guidelines generative AI public service Anita Anand announcement \"guide\""
}
```
**Tool call** `web_search` (id `call_ead5ea29927441c59def4843`):

```json
{
  "query": "Treasury Board of Canada Secretariat mandate role central agency policy \"Policy on Service and Digital\" about"
}
```
**Tool result** `web_search` (id `call_ead5ea29927441c59def4843`, 7,684 characters):

```
Search results for "Treasury Board of Canada Secretariat mandate role central agency policy "Policy on Service and Digital" about" (searched 2026-11-26):

[1] Let's Chat with Treasury Board of Canada Secretariat: Modernizing the Policy on Service and Digital - Insights | Public Sector Network
URL: https://publicsectornetwork.com/insight/lets-chat-with-treasury-board-of-canada-secretariat-modernizing-the-policy-on-service-and-digital
Excerpt: The Treasury Board of Canada Secretariat is leading the reset of the Policy on Service and Digital (PSD)—a modernization of the rules that guide how government designs, delivers, and oversees digital services. This reset is about reducing administrative burden, strengthening accountability, and ensuring digital government delivers real impact for Canadians. [...] The Government of Canada is undergoing a significant shift in how it designs, delivers, and evaluates digital services. At the center of this transformation is the Treasury Board of Canada Secretariat (TBS), which has launched the Enterprise Health Approach and is now leading the reset of the Policy on Service and Digital. We spoke with TBS about how these initiatives are modernizing oversight, fostering cross-departmental collaboration, and enabling a culture of continuous improvement. This [...] Clarify roles and cultivate trustDepartments are responsible for delivery; central agencies like TBS provide calibrated oversight, aligned to risk and maturity. This partnership approach builds resilience and trust.

[2] Policy on Service and Digital- Canada.ca
URL: https://www.tbs-sct.canada.ca/pol/doc-eng.aspx?id=32603
Excerpt: ## Note to reader

The Office of the Chief Information Officer (OCIO) at Treasury Board of Canada Secretariat (TBS) is modernizing the Policy on Service and Digital (PSD). Minor amendments were published and work is ongoing. This reset is a whole-of-government shift in how services are designed and delivered and better aligned to outcomes. Learn more

The Policy on Service and Digital and the Directive on Service and Digital took effect on . They replace the: [...] + 4.1.8Providing support for innovation and experimentation in service, information, data, IT and cyber security;

  IT and information standards

  + 4.1.9Informing the Treasury Board of Canada Secretariat of activities related to this policy that involve the development of national or international IT, information or data standards;

  Client-centric service design and delivery [...] 2.3The Treasury Board has delegated to the President of the Treasury Board the authority to issue, amend, and rescind directives related to this policy.
 2.4The Treasury Board has delegated to the Chief Information Officer (CIO) of Canada the authority to issue, amend and rescind standards, mandatory procedures and other appendices related to this policy.

[3] National Security and Intelligence Committee of Parliamentarians Special Report on the Government of Canada’s Framework and Activities to Defend its Systems and Networks from Cyber Attack: Part III: Key Cyber Defence Players, Authorities and Activities (1/3)
URL: https://nsicop-cpsnr.ca/reports/rp-2022-02-14/05-en-part-3-1.html?wbdisable=true
Excerpt: 108\. The Policy on Service and Digital includes a number of delegated authorities from the Treasury Board to specific officials:

- The President of the Treasury Board has the authority to issue, amend and rescind directives related to the policy.
- The CIO of Canada has the authority to issue, amend and rescind standards, mandatory procedures and other appendices related to the policy, and to enhance the government's framework to defend its networks from cyber attack. [...] 109\. The Policy on Service and Digital further defines the roles and responsibilities of key senior officials for the governance and administration of cyber security and cyber defence. The Secretary of the Treasury Board is responsible for establishing and chairing the Deputy Minister Committee on Enterprise Priority and Planning, a senior-level body that provides advice and recommendations on a number of information technology issues, including cyber security. Footnote 159 The CIO of Canada [...] 96\. Treasury Board exercises a broad mandate across government. Under the FAA, it is responsible for departmental accountability and financial management in the administration of government and for regulatory oversight of government programs and services; it is also the primary employer for the Government of Canada. The FAA sets out the requirements for a number of key officials and enables the Treasury Board, through the Treasury Board of Canada Secretariat (TBS), to issue policies,

[4] Digital Standards for Government of Canada Services | Treasury Board of Canada Secretariat | Secrétariat du Conseil du Trésor du Canada posted on the topic | LinkedIn
URL: https://www.linkedin.com/posts/tbs-sct_digitalstandards-digital-governmentofcanada-activity-7433214343036547072-GVhO
Excerpt: will take place in 2026 to refine and improve it. For more, explore the Register on the Open Government Portal: [...] Report this post

The #DigitalStandards help teams design and deliver #digital services that truly meet the needs of Canadians. Whether your work focuses on: ✔️Policy ✔️Service delivery ✔️Communications ✔️Information technology ✔️Program design The Standards provide practical guidance to ensure #GovernmentOfCanada services are user-centred, accessible, and aligned with how people actually engage online. Learn more: 

    38

Like   Comment 

##### Transcript [...] How are you investing in your professional growth in 2026? Strong digital leadership starts with strong digital skills. Today, TBS released new leadership-specific behavioural indicators for the #GCDigital Competencies Guidance. The new guidance helps leaders understand how to enable, model, and scale digital practices across their teams and organizations. Whether you're advancing work in data, artificial intelligence, cybersecurity, or cyber vigilance, these resources can help you build the

[5] Investigation into the Treasury Board of Canada Secretariat’s implementation of the Direction on Prescribed Presence in the Workplace - Office of the Privacy Commissioner of Canada
URL: https://www.priv.gc.ca/en/opc-actions-and-decisions/investigations/investigations-into-federal-institutions/2025-26/pa_20260318_tbs?wbdisable=true
Excerpt: 1. As a central agency and the administrative arm of the Treasury Board (TB), TBS provides oversight and leadership to help federal departments and agencies fulfill government priorities and achieve results for Canadians. One of TBS’s core responsibilities is to develop policies and to set the strategic direction for people and workplace management in the public service, which includes developing, updating and overseeing the implementation of the Direction.Footnote 20 TBS also employs [...] obligations within its specific operating environment and to support managers in their role. Additionally, in its policy role, TBS has developed guidance to support government institutions during the implementation of the updated hybrid work model.Footnote 51 [...] 4. TBS subsequently updated the Direction in May 2024 to establish a consistent approach to hybrid work and to ensure fairness across the public service. The updated mandate, which currently remains in effect, requires the core public administration with hybrid work arrangements to work on-site at least 3 days per week.Footnote 12 It also launched the transition to on-site presence for Information Technology (IT) employees who had previously been exempted from the Direction.Footnote 13
```
**Tool result** `web_search` (id `call_a5f8560c115a40389269c785`, 5,509 characters):

```
Search results for ""Government of Canada" September 2023 guidelines generative AI public service Anita Anand announcement "guide"" (searched 2026-11-26):

[1] Canada launches first-ever Artificial Intelligence Strategy for the federal public service
URL: https://finance.yahoo.com/news/canada-launches-first-ever-artificial-200000250.html
Excerpt: - Every 2 years, the government will aim to update the Strategy to ensure it remains relevant and responsive.
- A
  
  Guide on the use of Generative AI is available for public servants to assess the risks associated with generative AI and use it responsibly. [...] Quote

"Today's announcement positions Canada as a global leader in the responsible use of AI in the public service. With the first-ever AI Strategy for the public service, we're laying the groundwork to leverage the potential of this technology to deliver the best possible services to Canadians."

\- The Honourable Ginette Petitpas Taylor, President of the Treasury Board

Quick Facts [...] Through this Strategy, the government will be able to implement AI more efficiently by removing barriers to AI adoption that exist in departmental processes and legacy systems. It will promote more effective collaboration between government departments to identify successful AI-driven initiatives and implement them more widely. As well, the Strategy strengthens transparency and accountability for the responsible use of AI, ensuring the development of AI solutions that are ethical, inclusive,

[2] Progress on AI in government - Canada.ca
URL: https://www.canada.ca/en/government/system/digital-government/digital-government-innovations/responsible-use-ai/advancing-ai/progress.html
Excerpt: - Complements the Guide on the Use of Generative AI, offering concise best practices and do’s and don’ts for the use of generative AI tools by public servants in their daily work

### Public Consultation on Government of Canada’s artificial intelligence strategy for the federal public service ( – ) [...] ### Release of the Guide on the use of generative artificial intelligence ( )

- Provides guidance to federal institutions in their use of generative AI
- Includes an overview of generative AI, identifies limitations and concerns about its use, puts forward “FASTER” principles for its responsible use, and includes policy considerations and best practices

### Updates to the Directive on Automated Decision-Making ( ) [...] - Complements existing Government of Canada instruments and guidance by addressing the specific opportunities, risks and controls associated with agentic AI systems, which require additional governance considerations beyond the material covered in the Guide on the Use of Generative Artificial Intelligence, while remaining fully aligned with its principles.

[3] Minister of Public Services and Procurement, Anita Anand to Make an Announcement at the CN Tower as It Reopens Its Doors to Guests
URL: https://finance.yahoo.com/news/minister-public-services-procurement-anita-180400025.html
Excerpt: Science Centre. www.clc.ca [...] Where:

CN Tower main entrance

290 Bremner Blvd., Toronto

About Canada Lands Company [...] Starting July 23, timed tickets for the CN Tower's observation levels and EdgeWalk can be booked at  The 360 Restaurant will reopen on July 29.

What:

Announcement from the Minister of Public Services and Procurement as the CN Tower reopens to guests

When:

Friday July 23

9:00 a.m.

Who:

The Honourable Anita Anand, Minster of Public Services and Procurement

John Campbell, Canada Lands Company Board of Directors

Peter George, Chief Operating Officer, CN Tower

Where:

[4] Media advisory - Government of Canada to make an important announcement about the Cap-aux-Meules Port
URL: https://finance.yahoo.com/news/media-advisory-government-canada-important-201500629.html
Excerpt: MAGDALEN ISLANDS, QC, Feb. 26, 2025 /CNW/ - The Minister of Fisheries, Oceans and the Canadian Coast Guard, the Honourable Diane Lebouthillier and the Minister of Public Services and Procurement and Quebec Lieutenant, the Honourable Jean-Yves Duclos will make an announcement about the Cap-aux-Meules Port, Magdalen Islands.

They will make this announcement on behalf of the Minister of Transport and Internal Trade, the Honourable Anita Anand.

[5] Anita Anand, Minister of Public Services and Procurement and Canada Lands Company Announce a $21 million Investment to the CN Tower
URL: https://finance.yahoo.com/news/anita-anand-minister-public-services-134000434.html
Excerpt: Quotes:

"Toronto's vibrant tourism industry was hit hard by COVID-19. Canada Lands' investment of $21 million will provide visitors with a new experience to explore and discover at one of our country's most beloved attractions, and give Toronto the boost it deserves."

The Honourable Anita Anand, Minister of Public Services and Procurement [...] Today's announcement accompanies the CN Tower's reopening. After a suspension of operations of more than nine months, the CN Tower is delighted to welcome back guests to its observations level and EdgeWalk. The 360 Restaurant will reopen for dining on July 29.

Quotes: [...] John Tory, Mayor of Toronto

"As its proud owner and manager, Canada Lands Company continuously innovates and invests in the CN Tower to offer enriching, world-class experiences. Today's announcement is anchored to our commitment to accessibility. It marks another exciting chapter in the CN Tower's history as a national icon and celebration destination."
```

## Turn 11

_Model call: 39,951 input tokens, 181 output tokens_

**Tool call** `read_url` (id `call_e3877a1f0bdc4dbc851c7696`):

```json
{
  "start": 10000,
  "url": "https://www.canada.ca/en/government/system/digital-government/digital-government-innovations/responsible-use-ai/advancing-ai/progress.html"
}
```
**Tool result** `read_url` (id `call_e3877a1f0bdc4dbc851c7696`, 1,337 characters):

```
th the Office of the Privacy Commissioner of Canada ( September 18, 2018 )

### Justice AI taskforce session ( June 12, 2018 )

*   Justice AI taskforce created to provide input and direction on legal issues
*   25 representatives including from human rights, IP, commercial, IRCC, ESDC, and TBS

### AI Day ( May 28, 2018 )

*   120 participants from industry, academia, and government

### AI policy working group kick-off ( February 16, 2018 )

*   Hosted by GAC to develop departmental policies on AI

### Policy Horizons Directive Design Session ( February 13, 2018 )

*   Interdepartmental workshop to talk about the development of the Directive
*   Participants included TBS, IRCC, ISED, and ESDC

### Kick-off session with Departments ( January 22, 2018 )

*   Organized workshop with over 100 participants
*   Participants included TBS, IRCC, DFO, AAFC, CBSA, Funding Councils, GAC, ESDC, NRC, PCH, HC, NRCAN, Canada Council for the Arts, CRA, ISED, Policy Horizons, and SSC

### Drafting of the Directive (October, 2017 – March, 2019)

*   TBS binding policy focused on the automation of decisions

### Drafting of the AI whitepaper (October, 2016 – October, 2017)

*   Developed in the open with several academic, civil society, and government subject matter experts


[End of page. Showed characters 10,000-11,278 of 11,278.]
```

## Turn 12

_Model call: 40,500 input tokens, 3,707 output tokens_

**Assistant:**

I have enough evidence. Let me record the structured assessment.

**Tool call** `assess_credibility` (id `call_b7362b01d0d74cf48bf55d16`):

```json
{
  "evaluation": {
    "author": {
      "credentials": "No individual byline appears on the page. The page sits in the Treasury Board of Canada Secretariat's digital-government / responsible-use-of-AI section of Canada.ca and names 'TBS's Responsible Data and AI team (ai-ia@tbs-sct.gc.ca)' as the point of contact for information and guidance, and the Office of the Chief Information Officer of Canada (part of TBS) as a support body. No named author, no individual credentials, no author bio.",
      "credibility_assessment": "Institutional authorship by the Government of Canada's central policy agency (TBS) is appropriate for a document that sets out federal guidance: the organisation, not an individual expert, is the accountable source. The lack of a named author means there is no individual expertise to verify and no personal accountability, which slightly reduces transparency but not the authority of the content, which is official government policy guidance backed by in-text citations to statutes, policies and external literature.",
      "name": "No named author; published by the Treasury Board of Canada Secretariat (Government of Canada). The page lists TBS's Responsible Data and AI team as the contact."
    },
    "content_analysis": {
      "bias_and_tone": "Tone is neutral, instructional and bureaucratic, typical of government policy guidance. The document informs rather than persuades: it sets out the FASTER principles, a low-risk/high-risk framing, best practices, and FAQ answers. It explicitly acknowledges limitations and risks of generative AI (inaccuracy/hallucination, bias, privacy and IP risk, automation bias, erosion of skills, exploitative data-labelling labour, environmental costs) and repeatedly cautions against over-reliance and against treating outputs as authoritative. No products or services are sold; the page links only to government tools and courses (Canada School of Public Service, Canadian Centre for Cyber Security). The Government of Canada has an institutional interest in promoting its own framework, and the page functions as policy advocacy in that limited sense, but it does not misrepresent evidence and presents countervailing considerations. External critics (PIPSC president Jennifer Carr, quoted by Radio-Canada/Global Government Forum) argue the guidance is too vague and lacks clear 'no-go zones' - a critique of adequacy rather than of accuracy.",
      "claims_checked": [
        {
          "claim": "The document is official Government of Canada (Treasury Board of Canada Secretariat) guidance for federal institutions on the responsible use of generative AI, organised around 'FASTER' principles.",
          "evidence": "Corroborated by other Government of Canada pages and independent coverage: TBS's own 'Progress on AI in government' page describes the release of the Guide and the FASTER principles (https://www.canada.ca/en/government/system/digital-government/digital-government-innovations/responsible-use-ai/advancing-ai/progress.html); a TBS news release on the federal AI strategy refers to the Guide being available to public servants (https://finance.yahoo.com/news/canada-launches-first-ever-artificial-200000250.html); Global Government Forum reports the guidelines being issued to public servants (https://www.globalgovernmentforum.com/canadian-public-servants-issued-guidelines-for-using-generative-ai); Radio-Canada reports the new rules for public servants using AI (https://ici.radio-canada.ca/rci/en/news/2009454/federal-government-issues-new-rules-for-public-servants-using-ai).",
          "status": "corroborated"
        },
        {
          "claim": "The 'FASTER' principles (Fair, Accountable, Secure, Transparent, Educated, Relevant) were developed by TBS as the framework institutions must align with.",
          "evidence": "The Guide's own text lists the six FASTER principles. Government and secondary sources repeat the same attribution: GCwiki 'Responsible Use of Generative AI' page (https://wiki.gccollab.ca/index.php?title=Responsible_Use_of_Generative_AI) and the TBS 'Progress on AI in government' page both describe the Guide as putting forward FASTER principles (https://www.canada.ca/en/government/system/digital-government/digital-government-innovations/responsible-use-ai/advancing-ai/progress.html); a TESL Ontario blog post reproduces them as 'Developed by the Treasury Board of Canada' (https://blog.teslontario.org/consider-the-government-of-canadas-guide-on-the-use-of-generative-artificial-intelligence).",
          "status": "corroborated"
        },
        {
          "claim": "Training data can be outdated: ChatGPT-3.5 was trained on data up to early 2022, limiting its ability to answer about later events.",
          "evidence": "Substantially corroborated, with a small discrepancy on the date: OpenAI community/developer documentation and model references put the GPT-3.5 Turbo/GPT-3 knowledge cutoff at September 2021 (https://community.openai.com/t/what-is-the-actual-cutoff-date-for-gpt-4/394750; https://community.openai.com/t/new-knowledge-cutoff-date/382962; https://rankscope.ai/blog/chatgpt-knowledge-cutoff). The Guide's 'early 2022' is a few months later than the commonly documented September 2021 date, but the substantive point (fixed, stale training cutoff) is correct and widely documented.",
          "status": "corroborated"
        },
        {
          "claim": "Generative AI development and use can be a significant source of greenhouse gas emissions and water consumption because data centres are energy-intensive.",
          "evidence": "Corroborated by the International Energy Agency's 'Energy and AI' report: data centres used about 415 TWh, roughly 1.5% of global electricity, in 2024, growing ~12% a year since 2017, with data-centre emissions projected to rise from about 180 Mt to 300 Mt by 2035 and data centres described as energy- and water-intensive (https://www.iea.org/reports/energy-and-ai/executive-summary; https://www.iea.org/reports/energy-and-ai/energy-demand-from-ai). Note the IEA also says concerns that AI could accelerate climate change appear overstated, i.e. the Guide's framing is broadly consistent but the magnitude is contested.",
          "status": "corroborated"
        }
      ],
      "claims_supported_by_evidence": true,
      "contradicted_by_other_sources": false,
      "corroborated_by_other_sources": true,
      "date_published": "No visible 'Date modified' footer was captured by my reader, but the page's machine-readable metadata gives Published/Modified Time: Wed, 28 Oct 2026. The guide describes itself as the 'second version' and says it 'will be updated regularly'. On 2026-11-26 the information is current: it was updated about one month ago.",
      "funding_or_sponsorship": "Publicly funded Government of Canada publication (Treasury Board of Canada Secretariat). No advertising, sponsorship or commercial products; the only promotional links are to Government of Canada services (Canada School of Public Service courses, Canadian Centre for Cyber Security guidance). Nothing on the page suggests outside funding.",
      "primary_vs_secondary": "primary_source",
      "sources_cited": true
    },
    "evidence_urls": [
      "https://www.canada.ca/en/government/system/digital-government/digital-government-innovations/responsible-use-ai/generative-ai/guide-use-generative-ai.html",
      "https://www.canada.ca/en/government/system/digital-government/digital-government-innovations/responsible-use-ai.html",
      "https://www.canada.ca/en/government/system/digital-government/digital-government-innovations/responsible-use-ai/advancing-ai/progress.html",
      "https://www.tbs-sct.canada.ca/pol/doc-eng.aspx?id=32603",
      "https://www.globalgovernmentforum.com/canadian-public-servants-issued-guidelines-for-using-generative-ai",
      "https://ici.radio-canada.ca/rci/en/news/2009454/federal-government-issues-new-rules-for-public-servants-using-ai",
      "https://www.cbc.ca/news/canada/ottawa/federal-unions-watching-ai-s-usage-in-the-workplace-closely-1.6926866",
      "https://finance.yahoo.com/news/canada-launches-first-ever-artificial-200000250.html",
      "https://wiki.gccollab.ca/index.php?title=Responsible_Use_of_Generative_AI",
      "https://blog.teslontario.org/consider-the-government-of-canadas-guide-on-the-use-of-generative-artificial-intelligence",
      "https://community.openai.com/t/what-is-the-actual-cutoff-date-for-gpt-4/394750",
      "https://community.openai.com/t/new-knowledge-cutoff-date/382962",
      "https://rankscope.ai/blog/chatgpt-knowledge-cutoff",
      "https://www.iea.org/reports/energy-and-ai/executive-summary",
      "https://www.iea.org/reports/energy-and-ai/energy-demand-from-ai",
      "https://settlementatwork.org/en/resources/guide-use-generative-artificial-intelligence",
      "https://digitalgovernmenthub.org/examples/government-of-canada-guide-on-the-use-of-generative-ai"
    ],
    "overall_credibility": "high",
    "publication": {
      "editorial_process": "editor_reviewed",
      "name": "Government of Canada / Canada.ca (Treasury Board of Canada Secretariat)",
      "reputation": "Canada.ca is the official website of the Government of Canada; this page sits in TBS's digital-government / responsible-use-of-AI section. TBS is the central agency that issues federal policies and directives (the Guide itself cites the Policy on Service and Digital, its Directive, and the Directive on Automated Decision-Making, all hosted at tbs-sct.canada.ca), so it is the authoritative publisher for federal AI policy guidance. The Guide states it 'incorporates feedback from internal stakeholders and external experts' and cites the government's Procedures for Publishing, indicating formal review and publishing controls rather than self-publication. Independent coverage (Global Government Forum, Radio-Canada, CBC) confirms the guidelines were officially released and publicly discussed by the Treasury Board president; union representatives criticised their vagueness but did not dispute the facts. Minor caveat: I searched for the page's footer 'Date modified' and the footnote/reference text, which my reader did not render, so I could not inspect the reference list line by line."
    },
    "reasoning": "This is an official Government of Canada policy document published by the Treasury Board of Canada Secretariat on canada.ca, the government's primary web domain, and it is about as authoritative as a source can be for what Canadian federal guidance on generative AI says. It is transparent about its purpose, its limits (it calls itself a guide that 'complements and supports compliance with' existing laws, and says it will be updated), and its risks section is unusually candid, covering bias, accuracy, privacy, IP, labour exploitation and environmental costs. It carries 33 numbered in-text footnote references plus direct links to statutes, policies and cyber-security guidance, and it names the responsible TBS team and an email contact. Its main descriptive claims (that it is TBS guidance built on FASTER principles; that LLM training data goes stale; that generative AI has real environmental costs) are corroborated by other Government of Canada pages, independent trade/industry reporting and the IEA. I found no credible contradiction, only criticism from public-service unions that the guidance is too vague - a critique of policy adequacy, not of factual accuracy. Reasons not to give it full marks: no named individual author, and the printed 'Date modified' did not render in my reader (metadata shows 28 Oct 2026), and the footnote text itself was not retrievable. Also, this is a primary source about government policy, so it should not be used as an independent scientific authority on AI's technical or environmental impacts - for those, cite the underlying studies.",
    "source_type": "government_agency",
    "source_url": "https://www.canada.ca/en/government/system/digital-government/digital-government-innovations/responsible-use-ai/generative-ai/guide-use-generative-ai.html",
    "transparency_score": 4
  }
}
```
**Tool result** `assess_credibility` (id `call_b7362b01d0d74cf48bf55d16`, 12,186 characters):

```
{
  "status": "evaluation_recorded",
  "evaluation": {
    "source_url": "https://www.canada.ca/en/government/system/digital-government/digital-government-innovations/responsible-use-ai/generative-ai/guide-use-generative-ai.html",
    "source_type": "government_agency",
    "author": {
      "name": "No named author; published by the Treasury Board of Canada Secretariat (Government of Canada). The page lists TBS's Responsible Data and AI team as the contact.",
      "credentials": "No individual byline appears on the page. The page sits in the Treasury Board of Canada Secretariat's digital-government / responsible-use-of-AI section of Canada.ca and names 'TBS's Responsible Data and AI team (ai-ia@tbs-sct.gc.ca)' as the point of contact for information and guidance, and the Office of the Chief Information Officer of Canada (part of TBS) as a support body. No named author, no individual credentials, no author bio.",
      "credibility_assessment": "Institutional authorship by the Government of Canada's central policy agency (TBS) is appropriate for a document that sets out federal guidance: the organisation, not an individual expert, is the accountable source. The lack of a named author means there is no individual expertise to verify and no personal accountability, which slightly reduces transparency but not the authority of the content, which is official government policy guidance backed by in-text citations to statutes, policies and external literature."
    },
    "publication": {
      "name": "Government of Canada / Canada.ca (Treasury Board of Canada Secretariat)",
      "reputation": "Canada.ca is the official website of the Government of Canada; this page sits in TBS's digital-government / responsible-use-of-AI section. TBS is the central agency that issues federal policies and directives (the Guide itself cites the Policy on Service and Digital, its Directive, and the Directive on Automated Decision-Making, all hosted at tbs-sct.canada.ca), so it is the authoritative publisher for federal AI policy guidance. The Guide states it 'incorporates feedback from internal stakeholders and external experts' and cites the government's Procedures for Publishing, indicating formal review and publishing controls rather than self-publication. Independent coverage (Global Government Forum, Radio-Canada, CBC) confirms the guidelines were officially released and publicly discussed by the Treasury Board president; union representatives criticised their vagueness but did not dispute the facts. Minor caveat: I searched for the page's footer 'Date modified' and the footnote/reference text, which my reader did not render, so I could not inspect the reference list line by line.",
      "editorial_process": "editor_reviewed"
    },
    "content_analysis": {
      "claims_checked": [
        {
          "claim": "The document is official Government of Canada (Treasury Board of Canada Secretariat) guidance for federal institutions on the responsible use of generative AI, organised around 'FASTER' principles.",
          "status": "corroborated",
          "evidence": "Corroborated by other Government of Canada pages and independent coverage: TBS's own 'Progress on AI in government' page describes the release of the Guide and the FASTER principles (https://www.canada.ca/en/government/system/digital-government/digital-government-innovations/responsible-use-ai/advancing-ai/progress.html); a TBS news release on the federal AI strategy refers to the Guide being available to public servants (https://finance.yahoo.com/news/canada-launches-first-ever-artificial-200000250.html); Global Government Forum reports the guidelines being issued to public servants (https://www.globalgovernmentforum.com/canadian-public-servants-issued-guidelines-for-using-generative-ai); Radio-Canada reports the new rules for public servants using AI (https://ici.radio-canada.ca/rci/en/news/2009454/federal-government-issues-new-rules-for-public-servants-using-ai)."
        },
        {
          "claim": "The 'FASTER' principles (Fair, Accountable, Secure, Transparent, Educated, Relevant) were developed by TBS as the framework institutions must align with.",
          "status": "corroborated",
          "evidence": "The Guide's own text lists the six FASTER principles. Government and secondary sources repeat the same attribution: GCwiki 'Responsible Use of Generative AI' page (https://wiki.gccollab.ca/index.php?title=Responsible_Use_of_Generative_AI) and the TBS 'Progress on AI in government' page both describe the Guide as putting forward FASTER principles (https://www.canada.ca/en/government/system/digital-government/digital-government-innovations/responsible-use-ai/advancing-ai/progress.html); a TESL Ontario blog post reproduces them as 'Developed by the Treasury Board of Canada' (https://blog.teslontario.org/consider-the-government-of-canadas-guide-on-the-use-of-generative-artificial-intelligence)."
        },
        {
          "claim": "Training data can be outdated: ChatGPT-3.5 was trained on data up to early 2022, limiting its ability to answer about later events.",
          "status": "corroborated",
          "evidence": "Substantially corroborated, with a small discrepancy on the date: OpenAI community/developer documentation and model references put the GPT-3.5 Turbo/GPT-3 knowledge cutoff at September 2021 (https://community.openai.com/t/what-is-the-actual-cutoff-date-for-gpt-4/394750; https://community.openai.com/t/new-knowledge-cutoff-date/382962; https://rankscope.ai/blog/chatgpt-knowledge-cutoff). The Guide's 'early 2022' is a few months later than the commonly documented September 2021 date, but the substantive point (fixed, stale training cutoff) is correct and widely documented."
        },
        {
          "claim": "Generative AI development and use can be a significant source of greenhouse gas emissions and water consumption because data centres are energy-intensive.",
          "status": "corroborated",
          "evidence": "Corroborated by the International Energy Agency's 'Energy and AI' report: data centres used about 415 TWh, roughly 1.5% of global electricity, in 2024, growing ~12% a year since 2017, with data-centre emissions projected to rise from about 180 Mt to 300 Mt by 2035 and data centres described as energy- and water-intensive (https://www.iea.org/reports/energy-and-ai/executive-summary; https://www.iea.org/reports/energy-and-ai/energy-demand-from-ai). Note the IEA also says concerns that AI could accelerate climate change appear overstated, i.e. the Guide's framing is broadly consistent but the magnitude is contested."
        }
      ],
      "claims_supported_by_evidence": true,
      "sources_cited": true,
      "corroborated_by_other_sources": true,
      "contradicted_by_other_sources": false,
      "primary_vs_secondary": "primary_source",
      "funding_or_sponsorship": "Publicly funded Government of Canada publication (Treasury Board of Canada Secretariat). No advertising, sponsorship or commercial products; the only promotional links are to Government of Canada services (Canada School of Public Service courses, Canadian Centre for Cyber Security guidance). Nothing on the page suggests outside funding.",
      "bias_and_tone": "Tone is neutral, instructional and bureaucratic, typical of government policy guidance. The document informs rather than persuades: it sets out the FASTER principles, a low-risk/high-risk framing, best practices, and FAQ answers. It explicitly acknowledges limitations and risks of generative AI (inaccuracy/hallucination, bias, privacy and IP risk, automation bias, erosion of skills, exploitative data-labelling labour, environmental costs) and repeatedly cautions against over-reliance and against treating outputs as authoritative. No products or services are sold; the page links only to government tools and courses (Canada School of Public Service, Canadian Centre for Cyber Security). The Government of Canada has an institutional interest in promoting its own framework, and the page functions as policy advocacy in that limited sense, but it does not misrepresent evidence and presents countervailing considerations. External critics (PIPSC president Jennifer Carr, quoted by Radio-Canada/Global Government Forum) argue the guidance is too vague and lacks clear 'no-go zones' - a critique of adequacy rather than of accuracy.",
      "date_published": "No visible 'Date modified' footer was captured by my reader, but the page's machine-readable metadata gives Published/Modified Time: Wed, 28 Oct 2026. The guide describes itself as the 'second version' and says it 'will be updated regularly'. On 2026-11-26 the information is current: it was updated about one month ago."
    },
    "transparency_score": 4,
    "overall_credibility": "high",
    "reasoning": "This is an official Government of Canada policy document published by the Treasury Board of Canada Secretariat on canada.ca, the government's primary web domain, and it is about as authoritative as a source can be for what Canadian federal guidance on generative AI says. It is transparent about its purpose, its limits (it calls itself a guide that 'complements and supports compliance with' existing laws, and says it will be updated), and its risks section is unusually candid, covering bias, accuracy, privacy, IP, labour exploitation and environmental costs. It carries 33 numbered in-text footnote references plus direct links to statutes, policies and cyber-security guidance, and it names the responsible TBS team and an email contact. Its main descriptive claims (that it is TBS guidance built on FASTER principles; that LLM training data goes stale; that generative AI has real environmental costs) are corroborated by other Government of Canada pages, independent trade/industry reporting and the IEA. I found no credible contradiction, only criticism from public-service unions that the guidance is too vague - a critique of policy adequacy, not of factual accuracy. Reasons not to give it full marks: no named individual author, and the printed 'Date modified' did not render in my reader (metadata shows 28 Oct 2026), and the footnote text itself was not retrievable. Also, this is a primary source about government policy, so it should not be used as an independent scientific authority on AI's technical or environmental impacts - for those, cite the underlying studies.",
    "evidence_urls": [
      "https://www.canada.ca/en/government/system/digital-government/digital-government-innovations/responsible-use-ai/generative-ai/guide-use-generative-ai.html",
      "https://www.canada.ca/en/government/system/digital-government/digital-government-innovations/responsible-use-ai.html",
      "https://www.canada.ca/en/government/system/digital-government/digital-government-innovations/responsible-use-ai/advancing-ai/progress.html",
      "https://www.tbs-sct.canada.ca/pol/doc-eng.aspx?id=32603",
      "https://www.globalgovernmentforum.com/canadian-public-servants-issued-guidelines-for-using-generative-ai",
      "https://ici.radio-canada.ca/rci/en/news/2009454/federal-government-issues-new-rules-for-public-servants-using-ai",
      "https://www.cbc.ca/news/canada/ottawa/federal-unions-watching-ai-s-usage-in-the-workplace-closely-1.6926866",
      "https://finance.yahoo.com/news/canada-launches-first-ever-artificial-200000250.html",
      "https://wiki.gccollab.ca/index.php?title=Responsible_Use_of_Generative_AI",
      "https://blog.teslontario.org/consider-the-government-of-canadas-guide-on-the-use-of-generative-artificial-intelligence",
      "https://community.openai.com/t/what-is-the-actual-cutoff-date-for-gpt-4/394750",
      "https://community.openai.com/t/new-knowledge-cutoff-date/382962",
      "https://rankscope.ai/blog/chatgpt-knowledge-cutoff",
      "https://www.iea.org/reports/energy-and-ai/executive-summary",
      "https://www.iea.org/reports/energy-and-ai/energy-demand-from-ai",
      "https://settlementatwork.org/en/resources/guide-use-generative-artificial-intelligence",
      "https://digitalgovernmenthub.org/examples/government-of-canada-guide-on-the-use-of-generative-ai"
    ]
  }
}
```

## Turn 13

_Model call: 46,854 input tokens, 3,989 output tokens_

**Assistant:**

Now I'll write the report.

**Tool call** `save_report` (id `call_928b6379d496498e80b50e62`):

```json
{
  "filename": "canada-ca-generative-ai-guide.md",
  "markdown": "# Credibility Report: Guide on the use of generative artificial intelligence\n\n**URL:** https://www.canada.ca/en/government/system/digital-government/digital-government-innovations/responsible-use-ai/generative-ai/guide-use-generative-ai.html\n**Verdict:** High credibility\n**Evaluated:** 2026-11-26\n\n## Summary\n\nThis is the Government of Canada's official guide for federal institutions on using generative AI, published on Canada.ca by the Treasury Board of Canada Secretariat (TBS). It explains what generative AI is, sets out the TBS \"FASTER\" principles (Fair, Accountable, Secure, Transparent, Educated, Relevant), and gives policy considerations, best practices and FAQ answers for public servants and for institutions deploying tools to the public. Its main claims are corroborated by other Government of Canada pages, independent news coverage of the guidelines' release, and external technical/scientific sources (OpenAI developer documentation on model training cut-offs; the IEA on data-centre energy use). The tone is neutral and it candidly lists risks to privacy, human rights, intellectual property, workers and the environment, so there is no evident bias beyond a natural institutional interest in promoting its own framework. The main shortcomings are that no individual author is named, the page's \"Date modified\" footer did not render for me (metadata shows 28 October 2026), and as a policy document it is not an independent scientific authority on AI's technical impacts — cite the underlying studies for those.\n\n## Author\n\n**No named author.** There is no byline, author box or \"Author:\" metadata field on the page. What the page does provide:\n\n- The document sits in TBS's digital-government / responsible-use-of-AI section of Canada.ca.\n- The \"Additional support\" section names **\"TBS's Responsible Data and AI team\"** with the contact email `ai-ia@tbs-sct.gc.ca`, and lists the Office of the Chief Information Officer of Canada (part of TBS) as a support body.\n- The Guide says it \"incorporates feedback from internal stakeholders and external experts,\" and that this is the \"second version.\"\n\nI checked: the byline area, the page metadata, the bottom-of-page material I could retrieve, and the parent pages (`responsible-use-ai.html`, `generative-ai.html`) for an author or team attribution. No individual's name, title or credentials appear anywhere. For a government policy instrument this is normal — the institution is the accountable author — but it means there is no individual expertise to verify and no named person to hold responsible for errors.\n\n## Publication\n\n**Government of Canada / Canada.ca, under the Treasury Board of Canada Secretariat.** Canada.ca is the official federal web domain, and TBS is the central agency that issues federal policy instruments. The Guide itself links to, and claims to support compliance with, instruments hosted on the TBS site: the *Policy on Service and Digital*, the *Directive on Service and Digital*, and the *Directive on Automated Decision-Making*. It also directs readers to TBS's *Procedures for Publishing*, which indicates the page goes through the government's formal publishing and review controls rather than being self-published.\n\nIndependent evidence of track record and process:\n\n- TBS's own \"Progress on AI in government\" page records the release of the Guide and describes it as putting forward the FASTER principles and policy considerations.\n- A TBS news release on the first federal AI strategy for the public service links the Guide as a resource for public servants.\n- Mainstream and trade outlets covered the guidelines when they were issued: Global Government Forum, Radio-Canada (RCI), and CBC all report on the federal guidance for public servants using generative AI.\n- Public-service union representatives (PIPSC president Jennifer Carr) publicly criticised the guidance as too vague and lacking clear \"go/ no-go zones\" — a critique of policy adequacy, not a factual correction.\n\nI did not find any retraction, correction or misinformation finding about this page. Note that I could not render the printed footer (\"Date modified\") or the text of the 33 numbered footnotes with my reader; the in-text footnote markers and links do exist.\n\n## Claims Checked\n\n| Claim | Status | Evidence |\n|---|---|---|\n| The document is official Government of Canada (TBS) guidance for federal institutions on generative AI, organised around \"FASTER\" principles. | corroborated | TBS \"Progress on AI in government\" page describes the Guide's release and FASTER principles (https://www.canada.ca/en/government/system/digital-government/digital-government-innovations/responsible-use-ai/advancing-ai/progress.html); TBS news release on the federal AI strategy points public servants to the Guide (https://finance.yahoo.com/news/canada-launches-first-ever-artificial-200000250.html); Global Government Forum (https://www.globalgovernmentforum.com/canadian-public-servants-issued-guidelines-for-using-generative-ai) and Radio-Canada (https://ici.radio-canada.ca/rci/en/news/2009454/federal-government-issues-new-rules-for-public-servants-using-ai) report the guidelines being issued. |\n| The FASTER principles (Fair, Accountable, Secure, Transparent, Educated, Relevant) were developed by TBS as the framework institutions should align with. | corroborated | GCwiki \"Responsible Use of Generative AI\" page lists TBS guidance built on these principles (https://wiki.gccollab.ca/index.php?title=Responsible_Use_of_Generative_AI); TBS progress page describes the Guide as putting forward FASTER (https://www.canada.ca/en/government/system/digital-government/digital-government-innovations/responsible-use-ai/advancing-ai/progress.html); TESL Ontario blog reproduces them as \"Developed by the Treasury Board of Canada\" (https://blog.teslontario.org/consider-the-government-of-canadas-guide-on-the-use-of-generative-artificial-intelligence). |\n| Training data can be outdated — the Guide says \"ChatGPT-3.5 is trained on data up to early 2022.\" | corroborated (minor date imprecision) | OpenAI developer-community documentation and model references put the GPT-3.5 / GPT-3.5 Turbo knowledge cutoff at September 2021, not early 2022 (https://community.openai.com/t/what-is-the-actual-cutoff-date-for-gpt-4/394750; https://community.openai.com/t/new-knowledge-cutoff-date/382962; https://rankscope.ai/blog/chatgpt-knowledge-cutoff). The substance — a fixed, stale training cutoff — is correct; the specific date is a few months off and is now itself dated, since GPT-3.5-era models have since been retired. |\n| Generative AI development and use can cause significant greenhouse-gas emissions and water consumption because data centres are energy-intensive. | corroborated | IEA, *Energy and AI*: data centres used ~415 TWh, about 1.5% of global electricity in 2024, growing ~12%/yr since 2017; data-centre emissions projected to rise from ~180 Mt to ~300 Mt by 2035 (https://www.iea.org/reports/energy-and-ai/executive-summary; https://www.iea.org/reports/energy-and-ai/energy-demand-from-ai). The IEA also judges fears that AI alone will accelerate climate change \"overstated,\" so the Guide's framing is sound but the magnitude is debated — verify specific figures against the underlying report. |\n\nClaims I did **not** check individually: the Guide's statements about Canadian privacy law and IP law, the exploitation of data-labelling workers (it cites footnotes 4 and 5), and the language-performance gaps across languages (footnote 8).\n\n## Bias and Tone\n\n- **Language:** neutral, formal, instructional — the register of government policy, not marketing or advocacy journalism.\n- **Purpose:** to inform public servants and institutions and to set expectations, not to sell anything. No advertising; the only promotional links are to Government of Canada services (Canada School of Public Service courses, Canadian Centre for Cyber Security guidance).\n- **Balance:** unusually candid. It devotes separate sections to inaccuracy/hallucination, bias, quality, public-servant autonomy and automation bias, legal risks, distinguishing humans from machines, and environmental impacts. It warns readers repeatedly *not* to treat outputs as authoritative and *not* to use these tools where factual accuracy is required.\n- **Interests:** the Government of Canada has an institutional interest in promoting its own framework, and the document is by nature a statement of government policy — that is \"advocacy\" only in the sense that every policy instrument is. No commercial interest, no donation mechanism.\n- **Missing:** it does not engage directly with critics who say the guidance is too vague; that debate appears in outside coverage (Global Government Forum, Radio-Canada), not on the page.\n\n## Currency\n\n- The page's machine-readable metadata gives a published/modified timestamp of **Wednesday, 28 October 2026** — about one month before this evaluation, so it is current.\n- The printed footer \"Date modified\" did not render in my reader, so I am relying on the metadata timestamp.\n- The Guide describes itself as the **second version** and says it \"will be updated regularly to keep pace with regulatory and technological change.\"\n- One sign of age in the content: it still uses \"ChatGPT-3.5 is trained on data up to early 2022\" as its example of stale training data, and discusses tools like GitHub Copilot/FauxPilot and DALL-E/Midjourney/Stable Diffusion as the examples. The framework is current, but individual examples may date quickly — check for a newer revision if you need the very latest tool landscape.\n\n## Structured Assessment\n\n| Field | Assessment |\n|---|---|\n| **Source URL** | https://www.canada.ca/en/government/system/digital-government/digital-government-innovations/responsible-use-ai/generative-ai/guide-use-generative-ai.html |\n| **Source type** | Government agency (Treasury Board of Canada Secretariat, on Canada.ca) |\n| **Primary vs secondary** | Primary source — an official government statement of policy and guidance |\n| **Author** | No named author; institutional author is TBS. Contact listed: TBS Responsible Data and AI team (`ai-ia@tbs-sct.gc.ca`). No credentials or bio found on page, parent pages or metadata. |\n| **Author credibility** | Appropriate institutional authority for a policy instrument; weak individual accountability (no named expert) |\n| **Publication** | Government of Canada / Canada.ca (TBS) |\n| **Publication reputation** | Official federal domain; TBS is the central agency issuing federal digital/AI policy. Guide's release confirmed by TBS's own progress page, a TBS news release, and coverage by Global Government Forum, Radio-Canada and CBC. No retractions or corrections found. |\n| **Editorial process** | Editor-reviewed (formal government publishing controls; the Guide cites the GC *Procedures for Publishing* and says it incorporates internal and external expert feedback) |\n| **Sources cited** | Yes — 33 numbered in-text footnotes plus direct links to the *Directive on Automated Decision-Making*, TBS policies, and Canadian Centre for Cyber Security guidance (footnote text not renderable with my reader) |\n| **Claims supported by evidence in the source** | Yes |\n| **Corroborated by other sources** | Yes |\n| **Contradicted by other sources** | No (only criticism that the guidance is too vague — a policy critique, not a factual contradiction) |\n| **Funding / sponsorship** | Publicly funded Government of Canada publication; no commercial sponsorship, ads or products |\n| **Bias and tone** | Neutral, instructional; acknowledges risks and limitations; institutional interest in its own framework |\n| **Date published / updated** | Metadata: 28 October 2026 (printed \"Date modified\" not rendered); described as \"second version,\" updated regularly |\n| **Transparency score** | 4/5 — clear on publisher, purpose and process and on funding (public), but no named author and the reference list text was not inspectable |\n| **Overall credibility** | **High** |\n\n## Can I cite this?\n\n**Yes — cite it as is**, with a couple of sensible precautions.\n\n- **Best use:** any claim about *what the Government of Canada's guidance says*, federal AI policy, the FASTER principles, or the Canadian government's position on risks and best practices for generative AI. This is the authoritative primary document; there is no better source for that.\n- **Cite with care:** for general factual claims about generative AI (bias, hallucination, language-performance gaps, environmental impacts, labour practices). The Guide is summarising other people's research, and its footnote text did not render for me. Cite the underlying study or dataset (e.g., the IEA *Energy and AI* report for energy/water figures) alongside or instead of the Guide for a stronger paper.\n- **Note the vintage of examples:** if you quote the \"ChatGPT-3.5 trained on data up to early 2022\" line, flag that this was already imprecise (OpenAI's documented GPT-3.5 cutoff was September 2021) and that both the model and the example are now dated.\n- **Do not use it** as evidence that Canadian AI guidance *works*, is *sufficient*, or is uncontested — that is an evaluative question, and unions and experts have publicly argued the guidance is too vague. Pair it with independent analysis/criticism (Global Government Forum, Radio-Canada) if your paper makes an argument about policy effectiveness.\n- **Citation form:** Government of Canada, Treasury Board of Canada Secretariat. *Guide on the use of generative artificial intelligence.* Canada.ca, modified 28 October 2026. URL. (No individual author to cite; treat it as a corporate author.)\n\n## Sources Consulted\n\n1. https://www.canada.ca/en/government/system/digital-government/digital-government-innovations/responsible-use-ai/generative-ai/guide-use-generative-ai.html — the source itself (read in full across five segments: overview, key risks, FASTER principles, best practices, FAQ). No byline; 33 numbered footnotes; footnote text and footer did not render; metadata timestamp 28 Oct 2026.\n2. https://www.canada.ca/en/government/system/digital-government/digital-government-innovations/responsible-use-ai.html — TBS \"Responsible use of artificial intelligence in government\" hub; lists the Guide under \"Most requested\" and alongside related AI policy instruments.\n3. https://www.canada.ca/en/government/system/digital-government/digital-government-innovations/responsible-use-ai/generative-ai.html — \"Generative AI\" section index page confirming the Guide's place in current TBS guidance.\n4. https://www.canada.ca/en/government/system/digital-government/digital-government-innovations/responsible-use-ai/advancing-ai/progress.html — TBS progress timeline confirming release of the Guide and its FASTER principles (dates were stripped from the rendered text).\n5. https://www.tbs-sct.canada.ca/pol/doc-eng.aspx?id=32603 — *Policy on Service and Digital*, the TBS instrument the Guide says it supports compliance with; confirms TBS's policy-issuing role.\n6. https://www.globalgovernmentforum.com/canadian-public-servants-issued-guidelines-for-using-generative-ai — independent trade coverage of the guidelines' release, including union criticism about vague \"no-go zones.\"\n7. https://ici.radio-canada.ca/rci/en/news/2009454/federal-government-issues-new-rules-for-public-servants-using-ai — Radio-Canada English report on the new rules, quoting Treasury Board president Anita Anand and PIPSC's Jennifer Carr.\n8. https://www.cbc.ca/news/canada/ottawa/federal-unions-watching-ai-s-usage-in-the-workplace-closely-1.6926866 — CBC report on federal unions monitoring AI use; corroborates the policy context.\n9. https://finance.yahoo.com/news/canada-launches-first-ever-artificial-200000250.html — TBS news release (via Yahoo Finance) on the federal AI strategy, which cites the Guide as available to public servants.\n10. https://wiki.gccollab.ca/index.php?title=Responsible_Use_of_Generative_AI — GCwiki page listing TBS guidance on responsible generative AI use (read attempt redirected to an image; used the search-result excerpt only).\n11. https://blog.teslontario.org/consider-the-government-of-canadas-guide-on-the-use-of-generative-artificial-intelligence — third-party summary attributing the FASTER principles to the Treasury Board and citing the Guide.\n12. https://community.openai.com/t/what-is-the-actual-cutoff-date-for-gpt-4/394750 — OpenAI developer-community discussion documenting ChatGPT/GPT-3.5 training data up to September 2021.\n13. https://community.openai.com/t/new-knowledge-cutoff-date/382962 — further developer-community confirmation that GPT-3.5's cutoff stayed at September 2021.\n14. https://rankscope.ai/blog/chatgpt-knowledge-cutoff — model-cutoff reference table listing GPT-3.5 Turbo at September 1, 2021.\n15. https://www.iea.org/reports/energy-and-ai/executive-summary — IEA data-centre electricity (415 TWh, ~1.5% of global use in 2024), growth and emissions trajectory; also notes some climate fears are overstated.\n16. https://www.iea.org/reports/energy-and-ai/energy-demand-from-ai — IEA chapter on AI-driven data-centre electricity demand.\n17. https://settlementatwork.org/en/resources/guide-use-generative-artificial-intelligence — third-party reposting of the Guide's text; shows the content is widely redistributed (not used as independent corroboration).\n18. https://digitalgovernmenthub.org/examples/government-of-canada-guide-on-the-use-of-generative-ai — directory listing describing an earlier \"preliminary guidance\" version of the Guide, consistent with the page now being a \"second version.\"\n"
}
```
**Tool result** `save_report` (id `call_928b6379d496498e80b50e62`, 81 characters):

```
Saved the report to reports/canada-ca-generative-ai-guide.md (17,586 characters).
```

## Turn 14

_Model call: 50,878 input tokens, 284 output tokens_

**Assistant:**

**Verdict: High credibility** — the report was saved as `canada-ca-generative-ai-guide.md`. The page is the Treasury Board of Canada Secretariat's official guide on generative AI, published on the Government of Canada's primary domain; it is editor-reviewed, publicly funded, neutral in tone, and cites 33 numbered footnotes plus the federal policy instruments it supports. Its four main claims (that it is TBS guidance built on the FASTER principles, that TBS developed those principles, that LLM training data goes stale, and that generative AI carries real energy/water costs) were all corroborated by other Government of Canada pages, independent news coverage of the guidelines' release, OpenAI developer documentation and the IEA — though the guide's "ChatGPT-3.5 trained on data up to early 2022" line is slightly off (September 2021) and is itself now dated, and union critics argue the guidance is too vague, which is a policy critique rather than a factual contradiction. The only dents are the absence of a named individual author and the fact that the printed "Date modified" footer and footnote text didn't render in my reader (metadata shows 28 October 2026, so it is current). Cite it confidently as a primary source for Canadian federal AI policy, but go to the underlying studies for technical or environmental figures.


## Final output

**Verdict: High credibility** — the report was saved as `canada-ca-generative-ai-guide.md`. The page is the Treasury Board of Canada Secretariat's official guide on generative AI, published on the Government of Canada's primary domain; it is editor-reviewed, publicly funded, neutral in tone, and cites 33 numbered footnotes plus the federal policy instruments it supports. Its four main claims (that it is TBS guidance built on the FASTER principles, that TBS developed those principles, that LLM training data goes stale, and that generative AI carries real energy/water costs) were all corroborated by other Government of Canada pages, independent news coverage of the guidelines' release, OpenAI developer documentation and the IEA — though the guide's "ChatGPT-3.5 trained on data up to early 2022" line is slightly off (September 2021) and is itself now dated, and union critics argue the guidance is too vague, which is a policy critique rather than a factual contradiction. The only dents are the absence of a named individual author and the fact that the printed "Date modified" footer and footnote text didn't render in my reader (metadata shows 28 October 2026, so it is current). Cite it confidently as a primary source for Canadian federal AI policy, but go to the underlying studies for technical or environmental figures.

## Summary

- Turns (model calls): 14
- Tool calls: read_url x11, web_search x9, assess_credibility x1, save_report x1
- Tokens: 368,910 input (312,320 cached), 12,159 output
- Estimated cost: $0.0167
- Report: reports/canada-ca-generative-ai-guide.md
- URLs in canada-ca-generative-ai-guide.md not seen in any tool result: none
