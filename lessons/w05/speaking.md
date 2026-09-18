# Speaking — w05: Deep Dive 1 (Part 2) — Capabilities & Limitations

Model answers for reading and review. Personal stories and examples are illustrative, not real events.

## 1. When using AI for coding or writing, how do you verify outputs when a model generates a plausible hallucination? Explain using plausible and hallucination.

**Answer:**  
A hallucination is when the AI confidently says something that sounds plausible but is wrong. It is dangerous because the text looks correct and professional. To verify it, I test the code, check the official documentation and ask the AI where the information comes from. For important facts, I never trust a single AI answer.

**Example:**  
An AI once gave me a Python function that does not exist in the standard library. The code looked plausible, but it failed as soon as I ran it, and the documentation showed the correct function.

---

## 2. Why is temperature an important setting when you need exact configurations versus creative brainstorming? Explain using temperature and non-deterministic.

**Answer:**  
LLMs are non-deterministic: if you ask the same question twice, you may get different answers. Temperature is a setting that controls this randomness. For exact configurations, I want a low temperature, because I need a predictable and correct answer every time. For brainstorming, a higher temperature is useful, because it gives more varied and creative ideas.

**Example:**  
For a router command, variety is a risk, so a low temperature is better. For name ideas for my typing platform, I want many different options, so a higher temperature helps.

---

## 3. How does a knowledge cutoff limit what an AI can answer about recent tools or APIs? How does retrieval-augmented generation help overcome this?

**Answer:**  
A knowledge cutoff is the date after which the model has no training data. So it may not know a new tool, a new API version or recent changes, and it may give outdated advice. Retrieval-augmented generation helps: it connects the model to external sources, like documentation or a database, and adds fresh information to its context. Then the model answers from current documents, not only from its old training.

**Example:**  
If a library changed its API last month, the model may suggest the old syntax. If I paste the new documentation, or the agent searches the web, it can use the correct version.

---

## 4. Describe a project where you leverage complementary human and AI strengths. What tasks do you condense and what critical judgment do you keep?

**Answer:**  
In this English course, I leverage the complementary strengths of humans and AI. The AI is fast: it can condense a long lesson transcript into a short summary, suggest vocabulary and draft quiz questions. I keep the critical judgment: I decide which words are useful for me, check that the facts match the source and make sure the questions really teach something. The AI gives speed and scale, and I give judgment and purpose.

---

## 5. How do you stay abreast of rapid AI changes in your technical field? Why will some limitations remain for the foreseeable future?

**Answer:**  
I stay abreast of AI changes by using the tools every day, reading release notes and trying new models on my own tasks. Hands-on experiments teach me more than long articles. Some limitations will remain for the foreseeable future, because models generate text from statistical patterns, not from real understanding of the world. They can still hallucinate, their context is limited, and they can't use data they don't have access to.

**Example:**  
When a new model comes out, I give it the same small task I gave the old one, for example a bash script. Comparing the results shows me what has really improved.

---
