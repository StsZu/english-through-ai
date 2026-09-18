# Speaking — w09: Deep Dive 2 — Effective Prompting Techniques

Model answers for reading and review. Personal stories and examples are illustrative, not real events.

## 1. How do you apply prompt engineering in your daily programming or networking tasks? Which of the six techniques do you rely on most?

**Answer:**  
Prompt engineering is simply designing clear instructions for AI. In my daily work, I give context about my project, set constraints like "standard library only", and break big tasks into steps. The technique I rely on most is giving context: what I want, why I want it and who I am. Without context, the agent guesses, and I spend more time fixing its work.

**Example:**  
I start many requests with "I am a beginner in Python, and this is a static site that must work offline." This one sentence changes the level and the style of the answer.

---

## 2. Why is few-shot prompting often more effective than writing long abstract explanations? Describe an example where you showed patterns for the AI to emulate.

**Answer:**  
Few-shot prompting means showing the AI a few examples of the result you want. It is often more effective because some styles and formats are hard to explain in words but easy to show. The AI can follow the pattern directly instead of interpreting a long, abstract description. It works best when the examples cover different cases.

**Example:**  
When I wanted commit messages in my project's style, I gave the AI three examples: "w01: add glossary", "docs: fix paths" and "feat(template): quiz". After that, its messages followed the same pattern.

---

## 3. How does chain-of-thought prompting prevent an AI agent from going astray when solving multi-step technical problems?

**Answer:**  
Chain-of-thought prompting means asking the AI to work through a problem step by step, or listing the steps for it. In multi-step problems, the AI can easily jump to a wrong conclusion or skip a step. When it thinks before it acts, it plans better and its answers are more careful. As a bonus, I can see its reasoning, so I notice early where it is going astray and correct it.

**Example:**  
Before debugging a network problem, I write: "First list the possible causes, then check them one by one, and only then suggest a fix." This stops the AI from changing random settings.

---

## 4. Have you ever used the secret weapon of asking an AI to improve your own prompt? How did this iterative refinement help you hone your instructions?

**Answer:**  
Yes, I have. When I did not know how to ask for something, I described my goal and asked the AI to write a better prompt for me. It added details I had forgotten, like the output format and the level of the reader. Then I tested the new prompt, looked at the result and adjusted it again. This iterative refinement helped me hone my instructions and learn what a good prompt contains.

**Example:**  
I asked: "Help me write a prompt that creates vocabulary cards for a B1 learner." The AI suggested a word limit for the definitions and an example sentence for each word.

---

## 5. Why is it a mistake to overload a single prompt with multiple unrelated tasks? How do timeless communication principles apply to AI collaboration?

**Answer:**  
When one prompt contains many unrelated tasks, the AI may mix them, skip some or do each one badly. It is also harder for me to check the result and give clear feedback. It is better to give one clear task at a time or to split the work into steps. The same timeless principles work with people and with AI: be clear, give relevant context, show examples and say what success looks like.

**Example:**  
Instead of "fix the bug, redesign the page and write the README", I send three separate requests. Each answer is shorter, and I can review it properly.

---
