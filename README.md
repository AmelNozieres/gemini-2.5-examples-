# Gemini 2.5 Examples

💡 Real-world code examples showcasing the power of Gemini 2.5 — from structured outputs to vision, tool calling, and wide context reasoning.

Built for developers, AI builders, and indie hackers looking to go from idea to product — fast.

## 🔍 What's Inside

| File                        | Feature                    | Description                                                  |
|-----------------------------|-----------------------------|--------------------------------------------------------------|
| `01_json_output.py`        | JSON Output                 | Prompt Gemini to return clean structured JSON.               |
| `02_tool_calling.py`       | Tool Calling                | Let Gemini call real Python functions natively.              |
| `03_vision_parsing.py`     | Vision Reasoning            | Parse data from an invoice image using Gemini's vision model.|
| `04_long_context_summary.py`| Wide Context Window (1M tokens) | Summarize and analyze long feedback input from a .txt file.   |
| `user_feedback_dump.txt`   | Sample Input File           | Sample feedback file used for the long context demo.         |

## 🛠 Requirements

```bash
pip install google-generativeai Pillow
```

## 🔐 Setup

Set your Gemini API key using an environment variable or directly in code.

```bash
export GEMINI_API_KEY=your-api-key  # on Mac/Linux
set GEMINI_API_KEY=your-api-key     # on Windows
```

## 🚀 Quick Start

```bash
python 01_json_output.py
python 02_tool_calling.py
python 03_vision_parsing.py
python 04_long_context_summary.py
```

## 📥 New to Gemini?

Check out the full breakdown and live article:  
👉 [Read the Substack article here](https://decryptai.substack.com/p/gemini-25-is-quietly-insane)

---

## 🙌 Stay in the Loop

I'm building a full Gemini Dev Kit for beginners: annotated code, walkthroughs, and real-world use cases.  
👉 [Join the waitlist here]((https://amaln.gumroad.com/l/edgekit-dev-kit))

---

© 2025 – Built by Amal | For indie builders who move fast 🚀

## License

This project is licensed under the MIT License.

> ✳️ You may not resell or redistribute this repository or its contents as-is.

