# Speaking — w08: A Closer Look at Description

Model answers for reading and review. Personal stories and examples are illustrative, not real events.

## 1. Why is treating an AI like a vending machine an ineffective approach? How do you steer a conversation when an output is unhelpful?

**Answer:**  
A vending machine gives you the same fixed product when you press a button. AI is different: it is an interactive system, and its answer depends on the context and the conversation. If you only type a short command and take whatever comes out, you usually get a generic result. When an output is unhelpful, I steer the conversation: I explain what is wrong, add missing context, give an example or ask for a different approach.

**Example:**  
If an AI writes code that is too complex, I say: "This is too complex for me. Use simple functions and explain each one in one sentence."

---

## 2. Explain the difference between Product Description and Process Description. Give a concrete programming or networking prompt example.

**Answer:**  
Product description is about what you want the AI to create: the output, its format, its audience and its style. Process description is about how the AI should do the work: which steps, methods, data or order to follow. Sometimes the process is just as important as the final product.

**Example:**  
Product description: "Write a script that backs up my MikroTik configuration every night and keeps the last seven files." Process description: "First check which commands my RouterOS version supports, then write the script step by step and test each part before you combine them."

---

## 3. When collaborating on a complex refactor or design, do you prefer the AI to challenge your assumptions or follow your lead? Why?

**Answer:**  
For a complex refactor or design, I prefer the AI to challenge my assumptions. I am not an expert in every area, so my first idea may have hidden problems. If the AI only follows my lead, it may simply help me build the wrong thing faster. But when the decision is already made and I just need the work done, I ask it to follow my lead and keep things short.

**Example:**  
Before a big refactor, I write: "Before you change anything, tell me what is weak in my plan."

---

## 4. How does specifying data sources to draw on create a tremendous difference in code generation accuracy?

**Answer:**  
The AI already knows a lot, but it does not know my specific project, versions or rules. When I tell it which data to draw on, for example my existing code, the official documentation or a specific API version, it stops guessing. The generated code then fits my real project instead of a general example. This is part of process description, and it makes a tremendous difference in accuracy.

**Example:**  
If I say "use the RouterOS 7 documentation", the AI will not give me commands from an older version.

---

## 5. Describe how you would do a bad prompt makeover for an ambiguous terminal command instruction. Use finely tuned and makeover.

**Answer:**  
A bad prompt might be: "Write a command to clean up the disk." It is ambiguous: which system, which folders, and is it safe to delete files? In a makeover, I add product, process and performance description: "On macOS, show me a terminal command that lists the ten largest files in my Downloads folder. Do not delete anything. Explain each part of the command briefly." After this, the AI works like a finely tuned partner, not a guessing machine.

---
