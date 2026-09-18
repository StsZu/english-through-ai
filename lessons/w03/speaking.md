# Speaking — w03: The 4D Framework

Model answers for reading and review. Personal stories and examples are illustrative, not real events.

## 1. When you collaborate with a CLI agent on a coding task, how do you divide work? Explain your approach to delegation and how you avoid simply offloading tasks.

**Answer:**  
First, I make sure I understand the goal and the problem myself. Then I think about what the agent does well, like writing repetitive code, and what needs my judgment, like design decisions and security. Delegation is not just offloading: I choose each task on purpose and keep the vision of the whole project. I also review the results, so I still understand my own code.

**Example:**  
For a new page, I decide the structure and the data myself. I ask the agent to write the HTML and CSS, and then I read the code and test it before the commit.

---

## 2. Why is a context-rich prompt better than a short command? Give an example where you had to articulate your vision to an AI.

**Answer:**  
A short command leaves the AI guessing about the goal, the audience and the format. A context-rich prompt explains what I want, why I want it, who it is for and what the result should look like. AI can't read my mind, so more relevant context usually gives a better first answer and fewer rounds of fixes.

**Example:**  
Instead of "make a landing page", I wrote: "Make a one-page site for my typing platform for adult beginners. Use a calm style, a big Start button and no external libraries." The first version was already close to what I wanted.

---

## 3. Describe a situation where an AI output did not align with your goal. How did discernment help you decide whether to request refinement or set it aside?

**Answer:**  
Once, I asked an AI to write a small script, and it gave me a working solution that used a library I did not want to install. With discernment, I checked whether the output was accurate, useful and in line with my goal. The idea was good, but it broke my rule "standard library only", so I asked for a refinement without the library. If the whole approach had been wrong, I would set it aside and start again.

---

## 4. How do you practice diligence and maintain transparency when creating software or documentation with AI tools? What helps you stand behind the final result?

**Answer:**  
For me, diligence means I take ownership of everything I publish, even if AI helped to write it. I test the code, check the facts and make sure no private data goes into my prompts. For transparency, I say clearly where AI was involved, for example in the README or in the commit message. What helps me stand behind the result is a simple rule: I never publish something I have not read and understood myself.

**Example:**  
When a CLI agent helps me with a commit, the commit message shows that the agent was a co-author. Anyone who reads the history can see which changes were AI-assisted.

---

## 5. Which of the four Ds (Delegation, Description, Discernment, Diligence) is most critical when using AI for network administration or drone projects? Defend your opinion.

**Answer:**  
In my opinion, discernment is the most critical for network administration and drone projects. In these areas, a small mistake has real consequences: a lost connection, an open port or a drone in the wrong airspace. AI can give a plausible answer that is wrong, and only careful evaluation can catch it. The other Ds are important too, but without discernment, a mistake goes straight from the AI to a real device.

**Example:**  
If an AI puts a firewall rule in the wrong position, the rule may never work. I only notice this because I know that MikroTik processes rules from top to bottom.

---
