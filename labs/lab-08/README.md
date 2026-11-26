# Lab 8: img-debug

`img-debug` takes a screenshot of an error (a terminal, an IDE, a browser), shrinks it to a small JPEG, and sends it to a vision model on OpenRouter (`anthropic/claude-haiku-5.5`). The model can call a `lookup_error` tool, which searches the web with Tavily, before it explains the cause and gives a fix with references.

## Install

Python 3.10 or newer.

```bash
cd labs/lab-08
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

`requirements.txt` installs `openai` (the OpenRouter client and the tool schema helper), `tavily-python` (web search), `Pillow` (image resizing), `pydantic` (the tool's argument model) and `python-dotenv`.

## API keys

The script reads two keys from a `.env` file. It looks in the current folder and then in each parent folder, so one `.env` at the repo root works for every lab.

```
OPENROUTER_API_KEY=sk-or-...
TAVILY_API_KEY=tvly-...
```

Get the Tavily key from [app.tavily.com](https://app.tavily.com/). You can sign in with GitHub and no credit card is needed. The free plan has 1,000 searches a month and each `lookup_error` call uses one.

## Usage

```bash
python img-debug.py <screenshot> [optional note for the model]
```

```bash
python img-debug.py traceback.png
python img-debug.py chroma-browse.png "I upgraded to chromadb 1.5.9 and now chroma browse shows this"
python img-debug.py photo.jpg --max-side 1568 --quality 90
```

Options:

- `--max-side N`: longest side after resizing, in pixels (default 1024). Smaller images never get bigger.
- `--quality N`: JPEG quality from 1 to 95 (default 85).

The answer goes to stdout and everything else goes to stderr: image sizes before and after processing, each Tavily query and the URLs it returned, and token use and cost for each model call. `python img-debug.py shot.png > answer.md` saves only the answer.

After the answer is printed, the script compares every URL in it with the URLs Tavily returned during the run and warns about any that did not come from a search.

## Files

- `img-debug.py`: the CLI. It preprocesses the image, then runs the tool-calling loop (at most 5 model calls; the last one cannot search, so the model has to answer).
- `SYSTEM_PROMPT.md`: the debugging assistant's instructions. The script replaces `{{TODAY}}` with today's date so the model knows its training data may be older than the library in the screenshot.
- `screenshots/`: the images used for testing. `horse.jpg` is [Nokota Horses](https://commons.wikimedia.org/wiki/File:Nokota_Horses.jpg) by François Marchal, CC BY-SA 3.0, used as the "no error here" test.
