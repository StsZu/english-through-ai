# Quiz

## 1. You want a CLI agent to rename files and update imports in a small git branch. Which choice best shows delegation?

**Difficulty:** easy

- ✅ A. Decide which tasks the agent handles and which checks you keep for yourself.  
  *Correct: you divide work between the human and AI.*
- — B. Ask the agent to explain every technical word before touching the files.  
  *Not quite: this improves communication, but it does not divide responsibility.*
- — C. Accept every changed file because the agent is faster than manual editing.  
  *Incorrect: speed alone does not justify giving away all control.*

**Correct answer:** A — Decide which tasks the agent handles and which checks you keep for yourself.

**Explanation:**  
The correct answer is A because delegation is about deciding who should do each part of the work. In a git task, the agent can rename files and update imports, while you can keep final checks and merging. B is mainly about clear communication, not dividing the work. C gives the agent too much control without deciding where human judgment is still needed. A useful extra step is to give the agent a separate branch. That makes delegation safer because you can inspect the diff before any change reaches your main branch.

---

## 2. An AI answer about a MikroTik firewall rule looks confident, but one command seems unusual. What should you do first?

**Difficulty:** easy

- — A. Run the command immediately because confident wording usually means the answer is reliable.  
  *Incorrect: confident language is not evidence that a command is safe.*
- ✅ B. Evaluate the command against documentation and your current router configuration.  
  *Correct: check the output before applying it to a real router.*
- — C. Rewrite the prompt until the AI gives a shorter answer.  
  *Not enough: a shorter answer can still contain a dangerous command.*

**Correct answer:** B — Evaluate the command against documentation and your current router configuration.

**Explanation:**  
The correct answer is B because discernment means checking what AI gives you before using it. Router commands can affect connectivity and security, so a confident tone is not enough. A is wrong because AI can sound certain while making a technical mistake. C may improve readability, but it does not verify the command. One useful nuance is to compare the proposed command with a safe export or backup of your current configuration. You can also test risky changes in a lab router before applying them to equipment you depend on.

---

## 3. Which sentence best uses present perfect to describe the learner's AI experience?

**Difficulty:** easy

- — A. I collaborate with CLI agents yesterday on a Python script.  
  *Incorrect: yesterday normally requires the past simple.*
- — B. I am collaborating with CLI agents since two years.  
  *Incorrect: this form does not fit a continuing experience with since.*
- ✅ C. I have collaborated with CLI agents on several coding projects.  
  *Correct: present perfect describes experience up to now.*

**Correct answer:** C — I have collaborated with CLI agents on several coding projects.

**Explanation:**  
The correct answer is C because present perfect is useful for experience connected to the present. The speaker has done this work before, and that experience matters now. A is wrong because “yesterday” points to a finished past time, so past simple is better. B is wrong because “since two years” is not natural; English normally uses “for two years” for a duration. An extra example is: “I have used AI to build static sites on Vercel.” This tense is especially useful when describing your background in interviews or technical conversations.

---

## 4. A prompt technique worked well six months ago but now gives weaker results. Which conclusion best fits the lesson?

**Difficulty:** medium

- — A. Keep the technique unchanged because old methods are always more stable.  
  *Incorrect: tactical methods can lose value as AI tools change.*
- — B. Stop using AI until one permanent prompting method becomes available.  
  *Incorrect: the lesson argues for lasting skills, not a permanent trick.*
- ✅ C. Use strong grounding in core skills and replace outdated tactics when needed.  
  *Correct: lasting principles should guide changing technical tactics.*

**Correct answer:** C — Use strong grounding in core skills and replace outdated tactics when needed.

**Explanation:**  
The correct answer is C because the lesson separates lasting competencies from short-lived tactics. A grounding in core skills helps you adapt when a prompt pattern becomes outdated. A is wrong because older techniques are not automatically stable or better. B is wrong because no single prompting method is likely to remain perfect while AI tools continue changing. One useful example is coding agents: a special prompt format may change, but checking requirements, testing outputs, and deciding what to delegate remain useful. Those habits survive changes in tools and interfaces.

---

## 5. Your drone-planning assistant suggests a route near controlled airspace. Which response shows the strongest discernment?

**Difficulty:** medium

- ✅ A. Evaluate the route against current aviation rules and remain accountable for the final decision.  
  *Correct: verify the advice and keep responsibility for the outcome.*
- — B. Use the route if the assistant explains its reasoning in enough detail.  
  *Incorrect: a detailed explanation can still be wrong or outdated.*
- — C. Avoid AI for all drone planning because mistakes are possible.  
  *Too extreme: AI can help when its output is checked responsibly.*

**Correct answer:** A — Evaluate the route against current aviation rules and remain accountable for the final decision.

**Explanation:**  
The correct answer is A because discernment requires you to evaluate AI output, especially when safety or rules matter. You also remain accountable for the final choice. B is wrong because a long explanation does not prove that the route follows current aviation rules. C is wrong because the lesson supports thoughtful collaboration, not avoiding AI completely. An important extra point is that drone rules can change by country and airspace type. For certification abroad, checking an official aviation source is stronger evidence than relying only on an assistant’s memory.

---

## 6. You are building a feature for your typing platform. Which workflow best reflects collaboration with AI?

**Difficulty:** medium

- — A. Let AI build and deploy everything without checking the code or user behavior.  
  *Incorrect: collaboration still requires human decisions and evaluation.*
- — B. Write every line yourself and use AI only to correct spelling in comments.  
  *Too limited: AI can support more than simple text correction.*
- ✅ C. Delegate a draft to AI, evaluate the code, and refine it together.  
  *Correct: the human and AI share work while keeping judgment.*

**Correct answer:** C — Delegate a draft to AI, evaluate the code, and refine it together.

**Explanation:**  
The correct answer is C because collaboration means using AI as a partner while keeping human judgment active. You can delegate a first implementation, evaluate the code, test the feature, and then ask for improvements. A is wrong because it removes meaningful human checking. B is wrong because it treats AI like a simple spellchecker, which the lesson specifically moves beyond. One extra example is your typing platform: an agent could generate a scoring function, but you could test whether it rewards speed without encouraging too many typing errors.

---

## 7. A teammate says, “We only need better prompts; deeper AI skills are unnecessary.” Which reply best challenges that view?

**Difficulty:** medium

- — A. Prompt tricks are enough if we collect a very large library of them.  
  *Incorrect: a large library can still become outdated quickly.*
- ✅ B. Prompt tactics can become outdated, so grounding helps us adapt confidently.  
  *Correct: lasting skills support adaptation when tools and tactics change.*
- — C. Prompts are unimportant because AI should always understand vague requests.  
  *Incorrect: clear prompting still matters even within a broader framework.*

**Correct answer:** B — Prompt tactics can become outdated, so grounding helps us adapt confidently.

**Explanation:**  
The correct answer is B because the lesson does not reject prompts; it puts them inside a larger set of lasting skills. Specific tactics can become outdated, while grounding in core competencies helps people adapt confidently. A is wrong because collecting more prompt tricks does not solve the problem of changing tools. C is wrong because clear communication with AI still matters. A useful nuance is that strong users often change both the prompt and the workflow. For example, they may add tests, files, tools, or checkpoints instead of only rewriting one instruction.

---

## 8. A CLI agent produces working code, but you cannot explain why one security change is safe. What is the best next step?

**Difficulty:** medium

- — A. Merge it because passing tests mean the security change is fully understood.  
  *Incorrect: passing tests do not prove every security effect is safe.*
- — B. Remove the tests and ask the agent for a simpler answer.  
  *Incorrect: removing evidence makes evaluation weaker, not stronger.*
- ✅ C. Evaluate the change, document the reason, and stay accountable before merging.  
  *Correct: careful checking and responsibility belong before deployment.*

**Correct answer:** C — Evaluate the change, document the reason, and stay accountable before merging.

**Explanation:**  
The correct answer is C because diligence includes responsible, transparent, and accountable use of AI. If you cannot explain a security change, you should evaluate it before merging and record why it is acceptable. A is wrong because tests cover only what they were designed to test. B is wrong because removing tests reduces useful evidence. One extra practice is to ask the agent to point to the exact changed lines and possible risks. Then you can compare those claims with documentation or a security checklist before approving the pull request.

---

## 9. You want to explain an AI-assisted Raspberry Pi project to your teacher. Which answer is most effective?

**Difficulty:** hard

- ✅ A. State your position, give one concrete project example, and explain how you evaluated the AI output.  
  *Correct: it answers directly and supports the point with evidence.*
- — B. Tell a long story about when you first bought the Raspberry Pi, without answering the question.  
  *Incorrect: the answer drifts away from the requested point.*
- — C. List technical words about AI and Raspberry Pi without saying what you decided.  
  *Incorrect: vocabulary alone does not make a clear, direct answer.*

**Correct answer:** A — State your position, give one concrete project example, and explain how you evaluated the AI output.

**Explanation:**  
The correct answer is A because a strong spoken response answers the exact question and supports it with a concrete example. It also uses the learner’s strength in extended speech without drifting away from the task. B is wrong because a personal story can become unrelated. C is wrong because technical terms do not replace a clear position. One useful speaking technique is a three-part structure: answer, example, conclusion. For instance, say what AI did, explain how you evaluated it, then state whether you would collaborate with AI that way again.

---

## 10. A company wants AI to handle customer messages automatically. Which plan best applies the course framework?

**Difficulty:** hard

- — A. Automate every message immediately because fast replies are the main goal.  
  *Incorrect: speed does not replace judgment, checking, or responsibility.*
- ✅ B. Decide which messages AI handles, check difficult outputs, and define responsibility for mistakes.  
  *Correct: it combines delegation, discernment, and diligence in one workflow.*
- — C. Keep every message manual because responsible AI use means avoiding automation.  
  *Incorrect: responsible use can include automation with suitable human control.*

**Correct answer:** B — Decide which messages AI handles, check difficult outputs, and define responsibility for mistakes.

**Explanation:**  
The correct answer is B because it combines three important competencies. Delegation decides which messages AI should handle. Discernment checks difficult or uncertain outputs. Diligence makes responsibility clear when something goes wrong. A is wrong because fast automation without controls can create poor or unsafe responses. C is wrong because the framework does not say humans must do everything manually. One extra nuance is that companies can use confidence thresholds or message categories. Simple requests may be automated, while legal, financial, or sensitive cases can be sent to a human.

---
