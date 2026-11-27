# Lab 9: Source Credibility Analyzer Agent

`credibility-agent.py` takes a URL and investigates it the way a librarian or fact-checker would: it reads the page, looks up the author and the publication, searches for sources that confirm or contradict the main claims, records a structured assessment, and saves a Markdown credibility report. It is built with the OpenAI Agents SDK, runs `deepseek/deepseek-v4.1-flash-1017` through OpenRouter, reads pages with the Jina Reader and searches with Tavily.

## Install

Python 3.10 or newer.

```bash
cd labs/lab-09
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

`requirements.txt` installs `openai-agents` (the agent loop), `openai` (the OpenRouter client), `tavily-python` (web search), `requests` (the Jina Reader), `pydantic` (tool schemas) and `python-dotenv`.

## API keys

The script reads two keys from a `.env` file in the folder you run it from or any folder above it, so one `.env` at the repo root works for every lab:

```
OPENROUTER_API_KEY=sk-or-...
TAVILY_API_KEY=tvly-...
```

Get the Tavily key at [app.tavily.com](https://app.tavily.com/) (free plan, 1,000 searches a month). The Jina Reader (`https://r.jina.ai/`) needs no key at its free rate limit.

## Usage

```bash
python credibility-agent.py <url>
python credibility-agent.py https://www.cbc.ca/news/health/artificial-intelligence-emergency-rooms-9.7181509
python credibility-agent.py --no-assess <url>      # without the assess_credibility tool
python credibility-agent.py --max-turns 15 <url>    # default is 25
python credibility-agent.py --model qwen/qwen3.6-35b-a3b <url>
```

While it runs, each turn and tool call is printed to the terminal. When it finishes you get:

- the report in `reports/`, with a file name the agent chooses,
- the full trace in `traces/`: every model message, tool call (with arguments) and tool result, one Markdown file per run,
- a summary with the number of turns, tool calls, tokens and estimated cost, plus a check of the saved report. Any URL in the report that never appeared in a tool call or tool result is listed, since that is either a typo or an invented link.

A run costs about $0.01 (between $0.007 and $0.017 in testing).

## Files

- `credibility-agent.py`: SDK setup for OpenRouter, the agent, the run loop and the trace logger (an SDK `RunHooks` class).
- `tools.py`: the four tools. `read_url` reads pages through Jina in 10,000-character parts (the agent passes `start` to read further). A target page's 404 and CAPTCHA or bot-check pages come back as errors, since Jina returns those with HTTP 200. `web_search` uses Tavily. `assess_credibility` is the "think" tool, whose Pydantic schema is the credibility rubric. `save_report` writes to `reports/`, refuses to save before an assessment has been recorded, and gives the file a numbered name (`-2`, `-3`) instead of overwriting a report from an earlier run. When the model sends arguments a tool rejects, the error it gets back names the field and the problem.
- `SYSTEM_PROMPT.md`: the agent's instructions. The parts between `<!-- assess:start -->` and `<!-- assess:end -->` are removed when running with `--no-assess`.

## Test runs

| Category | Source | Verdict | Turns |
|---|---|---|---|
| Government | [canada.ca: Guide on the use of generative AI](https://www.canada.ca/en/government/system/digital-government/digital-government-innovations/responsible-use-ai/generative-ai/guide-use-generative-ai.html) | high | 14 |
| News | [CBC: Paging Dr. AI to the ER?](https://www.cbc.ca/news/health/artificial-intelligence-emergency-rooms-9.7181509) | high | 10, 12 |
| Corporate blog | [Anthropic: Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) | medium | 11 |
| Personal blog | [Medium: Prompt engineering is dead](https://medium.com/@fruitful2007/prompt-engineering-is-dead-introducing-context-engineering-6280c075a1a9) | low | 10, 9 |
| Tricky | [arXiv v1 PDF of a paper MIT disowned and arXiv withdrew](https://arxiv.org/pdf/2412.17866v1) | very low | 7 |
| Research project | [Chroma: Context Rot](https://research.trychroma.com/context-rot) | high | 12 |
| Research project | [Lost in the Middle (arXiv / TACL)](https://arxiv.org/abs/2307.03172) | high | 9 |

`reports/medium-paul-fruitful-context-engineering.md` is the Medium run with `--no-assess`. The CBC report is from the second run; the first run's report, which had one mistyped URL, is still inside its trace.

These runs were made before the last round of fixes (detailed tool errors, the 404 and CAPTCHA checks in `read_url`, numbered report names, a stricter URL check). Two traces show the older behaviour: the first CBC run read a PubMed CAPTCHA page as if it were the article, and the Anthropic trace flags an x.com link that the current check accepts, because the search result had the same URL with `?lang=en`. One run of the arXiv source on the final code worked end to end.
