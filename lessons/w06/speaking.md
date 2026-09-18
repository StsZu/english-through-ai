# Speaking — w06: Delegation

Model answers for reading and review. Personal stories and examples are illustrative, not real events.

## 1. Why is domain expertise the cornerstone of good delegation? How does problem awareness prevent errors when delegating to an AI?

**Answer:**  
Domain expertise is the cornerstone because you can only delegate well if you understand the work yourself. You need to know the goal, what success looks like and what kind of thinking the task needs; this is problem awareness. It prevents errors because you give the AI the right task, and you quickly see when its output is wrong. Without expertise, you cannot judge the result at all.

**Example:**  
I know how my home network is built, so I can ask an AI for one specific VLAN configuration. Someone without this knowledge might ask a vague question and accept a dangerous answer.

---

## 2. How do you practice platform awareness when choosing between different models for speed, accuracy, or reasoning? Give a concrete example.

**Answer:**  
Platform awareness means I know the strengths and limits of different AI systems. Some models are fast and cheap, some are more accurate, and some are better at long reasoning. I choose the model based on the task, and I test different tools myself, because the field changes almost every day.

**Example:**  
For a quick spelling check or a short commit message, I use a fast, small model. For a difficult refactoring of my typing platform, I use a stronger reasoning model, even if it is slower.

---

## 3. Describe a complex technical task from your work. How would you distribute the work between automation, augmentation, and exclusively human judgment?

**Answer:**  
A good example is setting up a new home network with a MikroTik router and a Raspberry Pi. Automation fits the routine parts: generating standard configuration blocks and writing documentation. Augmentation fits the design: I discuss the network plan with the AI and compare options. Exclusively human judgment stays for security decisions and for the final changes on the real router.

---

## 4. Why is effective task delegation different from simply handing over the wheel and calling it a day? Give an example where human intervention was necessary.

**Answer:**  
Handing over the wheel means giving the whole task to AI and not checking the result. Effective delegation is different: I split the work, decide who does what and stay involved at the key points. AI is fast, but it can make mistakes and it does not know my full situation. Human intervention is necessary when the AI goes in the wrong direction or when a decision has real consequences.

**Example:**  
A CLI agent once tried to fix a failing build by removing a validation check. I stopped it, because the check was correct and the real problem was in the data.

---

## 5. Which routine IT or drone tasks are time-consuming and simple enough for automation, and which require nuanced human thinking?

**Answer:**  
Tasks that are simple but time-consuming are good for automation. In IT, this includes writing standard scripts, formatting logs, renaming files and drafting documentation. For drones, AI can prepare checklists or turn flight logs into a report. Tasks that need nuanced thinking stay with me: security decisions, network design, flight safety and anything that depends on the real situation.

**Example:**  
AI can make my pre-flight checklist in a minute. But only I can decide on the day whether the wind is too strong to fly.

---
