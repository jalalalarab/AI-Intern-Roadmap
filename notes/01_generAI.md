\# Generative AI



\## Definition

AI systems that create new content (text, images, code, audio, video) rather than just classifying or predicting a fixed label. Trained on huge amounts of existing data to learn patterns, then generate new outputs that follow those patterns.



\## Where it's used

\- Text generation: chatbots, writing assistants, code generation (e.g. Claude, ChatGPT, GitHub Copilot)

\- Image generation: Midjourney, DALL-E, Stable Diffusion

\- Code: autocomplete, full function generation, debugging help

\- Audio/video: voice synthesis, video generation tools



\## Example

Asking an LLM "write a Python function to reverse a string" — it generates working code it wasn't explicitly programmed with, by predicting the most likely next tokens based on patterns learned from training data.



\## Key terms

\- \*\*Prompt\*\* — the input/instruction you give the model

\- \*\*Token\*\* — a chunk of text (roughly a word or part of a word) the model processes one at a time

\- \*\*Hallucination\*\* — when a model confidently generates false or made-up information

\- \*\*Fine-tuning\*\* — further training a pre-trained model on specific data to specialize it

\- \*\*Temperature\*\* — a setting controlling how random/creative vs. predictable the output is



\## Risks

\- \*\*Hallucination\*\* — generating plausible-sounding but false information (dates, facts, citations that don't exist)

\- \*\*Bias\*\* — models can reproduce biases present in their training data

\- \*\*Overreliance\*\* — treating generated output as automatically correct without verification

\- \*\*Misuse\*\* — generating misinformation, spam, or deceptive content at scale



\## Prompting basics

\- Be specific and give context — vague prompts get vague answers

\- Provide examples of desired output format when possible (few-shot prompting)

\- Break complex tasks into smaller steps

\- Iterate — refine the prompt based on what the output gets wrong



\## Connection to internship

Directly relevant to LLM-related parts of the roadmap (Day 3): prompting, agents, and tool-calling all build on these fundamentals. Also relevant to Project 3 (AI Prompt/Tools API), which logs prompts/responses.

