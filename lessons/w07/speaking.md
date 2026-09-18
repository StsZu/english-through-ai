# Speaking — w07: Project Planning and Delegation

Model answers for reading and review. Personal stories and examples are illustrative, not real events.

## 1. Which multi-step technical project would you like to pursue in this course? Explain why it is substantial yet manageable.

**Answer:**  
I would like to build a small vocabulary trainer for this course as a single HTML page. It is substantial because it involves several types of tasks: planning, collecting words, writing code, designing and testing. But it is manageable because it is one page with no server and a clear goal. I am also really interested in it, because I will use it myself to learn English.

---

## 2. When you break down a complex coding or networking task, how do you look at it through the lens of delegation? Give a concrete example.

**Answer:**  
First, I list all the tasks the project needs. Then, for each task, I ask: which skills does it need, what can the AI do well, and where do I need my own judgment? After that, I decide whether the task is automation, collaboration or human-only work. This turns a big, confusing job into small, clear steps.

**Example:**  
To add a VPN to my home network, I split the work into four parts: choose the VPN type, write the configuration, test it and document it. I discuss the choice with the AI, let it draft the configuration, and do the testing and the final decision myself.

---

## 3. Why is it important to challenge assumptions and ask for clarification during an AI planning session instead of accepting the first plan?

**Answer:**  
The first plan from an AI is often generic and based on assumptions that may not match my situation. If I accept it without questions, I may build the wrong thing or miss important risks. When I challenge the plan and ask for clarification, the AI has to explain its choices and adapt them to my real goals. The conversation also helps me notice things that neither of us saw at the start.

**Example:**  
An AI suggested a database for my small project. When I asked "Why do I need a database?", we agreed that a simple JSON file was enough.

---

## 4. What potential bottlenecks or risks do you anticipate when delegating parts of a live infrastructure project to a CLI agent?

**Answer:**  
The biggest risk is that the agent changes a live system and something breaks for real users. It may not know the whole network, so a small change can cut off access, including my own. Another risk is secrets: passwords or keys can end up in logs or prompts. A bottleneck is review: if the agent works fast but I must check everything, my review becomes the slowest step.

**Example:**  
That is why I let the agent work on a test device or in a separate git branch first. Only after I review and test the change do I apply it to the live router.

---

## 5. How would you create a compelling pitch to explain your AI-assisted project workflow to a manager or client? Use pitch and specify.

**Answer:**  
In my pitch, I would start with the problem and the benefit: the work gets faster, but quality stays under human control. Then I would specify which tasks the AI does, which tasks I do and how I check every result. I would show one short, real example with the time we saved. Finally, I would explain how we keep data safe and who is responsible for the final result.

**Example:**  
"The AI drafts the configuration in ten minutes instead of two hours. I review and test every line, and nothing goes to production without my approval."

---
