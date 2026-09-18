# Speaking — w04: Deep Dive 1 — What is Generative AI? (Part 1)

Model answers for reading and review. Personal stories and examples are illustrative, not real events.

## 1. In your own words, explain how Generative AI differs from traditional classification AI. Give one concrete example from your programming or networking experience using prominent and breakthrough.

**Answer:**  
Traditional AI analyzes existing data and puts it into categories, for example "spam" or "not spam". Generative AI creates new content that did not exist before, such as text, code or images. Large language models are a prominent type of generative AI. This was a real breakthrough, because AI moved from sorting information to producing it.

**Example:**  
A classification model could look at router logs and label traffic as normal or suspicious. A generative model can read the same logs and write a new firewall script or explain the problem in plain words.

---

## 2. Describe how the transformer architecture became a game changer in 2017. How does attention under the hood help AI maintain context across long code files?

**Answer:**  
The transformer architecture appeared in 2017 and was a game changer for AI. It processes long sequences of text and keeps the relationships between words, even when they are far apart. Under the hood, the attention mechanism lets the model look at all parts of the input and decide which parts matter most at each moment. In a long code file, this helps the model connect a function call with the place where the function is defined.

**Example:**  
If I define a variable at the top of a 500-line file, the model can still use it correctly at the bottom. Attention helps it keep that connection.

---

## 3. What is the difference between pre-training and fine-tuning? Why is reinforcement learning necessary to make models helpful and safe?

**Answer:**  
In pre-training, the model reads huge amounts of text and learns to predict what comes next, so it learns language and general knowledge. In fine-tuning, the model gets extra training to follow instructions and give helpful answers. Reinforcement learning uses rewards and penalties, often based on human feedback, to shape the model's behaviour. It is necessary because a model that only predicts text can also produce harmful or unhelpful answers; this step makes it more helpful, honest and harmless.

---

## 4. Have you ever experienced context window limits when working with a CLI agent or chat model? How did you adapt your workflow to manage memory effectively?

**Answer:**  
Yes, I have. In a long session with a CLI agent, it started to forget the rules I had given at the beginning. This happens because the context window is the model's working memory, and old information can fall out of it. Now I keep important rules in a project file that the agent reads every time, and I start a new session for each new task. I also give short summaries instead of pasting whole files.

**Example:**  
In this course project, the rules live in a CLAUDE.md file. So the agent always knows, for example, that it must not touch the legacy folder.

---

## 5. Do you think emergent capabilities from scaling laws will eventually make prompt engineering obsolete? Defend your position using in-context learning and vast.

**Answer:**  
I think they will make some prompt tricks obsolete, but not clear communication. As models train on vast amounts of data, they get better at understanding what we mean. However, in-context learning means the model adapts to the instructions and examples in my prompt, so the quality of my input still matters. The model cannot know my goal, my audience or my project unless I tell it.

**Example:**  
A newer model may not need "think step by step" anymore. But it still needs to know that my site must work offline without external libraries.

---
