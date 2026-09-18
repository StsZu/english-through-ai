# Quiz

## 1. What does it mean when an AI model has a knowledge cutoff date of November 2024?

**Difficulty:** easy

- — A. The model will stop working permanently on November 2024.  
  *Incorrect: cutoff date is a past training boundary, not an expiration date.*
- — B. The model deletes all user accounts created after November 2024.  
  *Incorrect: cutoff refers exclusively to training knowledge limits.*
- ✅ C. The model has no innate training data about world events that occurred after November 2024.  
  *Correct: training datasets only capture history up to the cutoff date.*

**Correct answer:** C — The model has no innate training data about world events that occurred after November 2024.

**Explanation:**  
A knowledge cutoff date represents the point in time after which the AI model has no innate knowledge of world events or newer publications. If a model was trained up to November 2024, it cannot know about software releases or news from 2025 unless it uses external tools like live web search. The A option confuses a historical training boundary with an expiration deadline. The B option is completely unrelated to user account management. Understanding knowledge cutoffs prevents engineers from expecting fresh documentation from offline models without search extensions.

---

## 2. What is an AI hallucination?

**Difficulty:** easy

- ✅ A. An output that sounds confident and plausible but contains factually incorrect information.  
  *Correct: hallucinations appear convincing while being factually wrong.*
- — B. A hardware failure where a server screen turns completely green.  
  *Incorrect: hallucinations are textual factual errors, not monitor glitches.*
- — C. An intentional joke inserted by developers to entertain users.  
  *Incorrect: hallucinations stem from probabilistic next-token generation.*

**Correct answer:** A — An output that sounds confident and plausible but contains factually incorrect information.

**Explanation:**  
An AI hallucination occurs when a language model generates a statement that sounds confident and linguistically plausible, but is actually factually incorrect or fabricated. Because language models predict statistical word sequences rather than querying a verified truth database, they can construct false citations, non-existent software flags, or incorrect historical dates. The B option is an irrelevant hardware malfunction. The C option is wrong because hallucinations are an unintended mathematical byproduct of next-token prediction. Critical discernment is required whenever accuracy is essential.

---

## 3. Why are large language models described as non-deterministic by default?

**Difficulty:** easy

- — A. Because they can only run on computers powered by solar panels.  
  *Incorrect: power source has no effect on software determinism.*
- ✅ B. Because they make probabilistic choices, potentially giving slightly different answers to the same prompt.  
  *Correct: probability distributions create variable response completions.*
- — C. Because they always return identical byte-for-byte outputs under every setting.  
  *Incorrect: that would describe deterministic traditional algorithms.*

**Correct answer:** B — Because they make probabilistic choices, potentially giving slightly different answers to the same prompt.

**Explanation:**  
Language models are non-deterministic by default because word generation involves sampling from probability distributions. Submitting the exact same prompt multiple times can produce slightly different phrasings or structural choices based on the temperature parameter. The A option is an absurd distraction about power supplies. The C option defines deterministic software, such as a traditional compiler or hash function, which always produces identical outputs for identical inputs. When building automated pipelines, developers often set temperature near zero to minimize output variation.

---

## 4. How does the temperature setting influence AI outputs in practice?

**Difficulty:** medium

- — A. Temperature measures the physical Celsius heat of the server CPU.  
  *Incorrect: in AI APIs, temperature is a mathematical sampling hyperparameter.*
- ✅ B. Lower temperature produces more predictable, focused text, while higher temperature increases creative diversity.  
  *Correct: temperature adjusts sampling probabilities from narrow to wide.*
- — C. Higher temperature deletes all adjectives from the generated response.  
  *Incorrect: temperature does not filter specific parts of speech.*

**Correct answer:** B — Lower temperature produces more predictable, focused text, while higher temperature increases creative diversity.

**Explanation:**  
In language model APIs, temperature is a mathematical parameter controlling the randomness of next-token sampling. A low temperature (e.g., 0.1 or 0.2) flattens token probabilities to select the most probable words, making the output focused, deterministic, and ideal for coding or JSON schemas. A high temperature (e.g., 0.8 or 1.0) broadens selection, encouraging creative brainstorming and diverse ideas. The A option confuses the algorithmic parameter with physical hardware heat. The C option is inaccurate because temperature affects probabilistic sampling across all tokens.

---

## 5. What is retrieval-augmented generation (RAG) and what limitation does it solve?

**Difficulty:** medium

- ✅ A. It connects models to external documents and live data sources to ground answers and overcome knowledge cutoffs.  
  *Correct: RAG fetches verified facts before generating final text.*
- — B. It converts text models into image editing software automatically.  
  *Incorrect: RAG is an information retrieval architecture, not an image tool.*
- — C. It completely removes the need for human prompts by predicting thoughts.  
  *Incorrect: RAG still requires structured queries and user prompts.*

**Correct answer:** A — It connects models to external documents and live data sources to ground answers and overcome knowledge cutoffs.

**Explanation:**  
Retrieval-augmented generation (RAG) is an architecture that queries external knowledge bases, internal company documents, or search engines to retrieve relevant text chunks before generating an answer. By injecting real, verified data directly into the model's context window, RAG helps overcome knowledge cutoffs and significantly reduces hallucinations. The C option is an impossible sci-fi claim. The B option mischaracterizes RAG as an image editor. In enterprise environments, RAG allows proprietary documentation and private repositories to be queried accurately without costly model retraining.

---

## 6. Why are extended-thinking models better at multi-step math and complex reasoning?

**Difficulty:** medium

- — A. They bypass all neural processing and search Google for pre-written math homework.  
  *Incorrect: reasoning models generate internal thought tokens autonomously.*
- ✅ B. They break down problems into sequential reasoning steps and verify sub-conclusions before producing a final answer.  
  *Correct: chain-of-thought processing improves logical consistency.*
- — C. They only answer questions that contain fewer than five words.  
  *Incorrect: extended thinking handles long, complex problem statements.*

**Correct answer:** B — They break down problems into sequential reasoning steps and verify sub-conclusions before producing a final answer.

**Explanation:**  
Extended-thinking and reasoning models are trained to generate invisible or visible intermediate chains of thought before delivering the final response. By breaking down complex logic, coding refactors, or mathematical proofs into sequential steps, the model can catch errors, test alternative paths, and avoid premature conclusions. The A option is false because extended-thinking models reason mathematically through weights rather than simple web copy-pasting. The C option is inaccurate. This capability represents a significant breakthrough for algorithmic debugging, networking configurations, and system design.

---

## 7. An executive wants an AI to summarize a 500-page financial report in one prompt. What constraint might she encounter?

**Difficulty:** medium

- ✅ A. The context window capacity may be exceeded, causing parts of the report to be dropped or ignored.  
  *Correct: models have token memory limits for single interactions.*
- — B. The model will permanently convert all dollar figures into ancient Greek coins.  
  *Incorrect: models maintain currency formats correctly.*
- — C. Financial numbers automatically trigger an irreversible shutdown of the model.  
  *Incorrect: models process financial text safely within token limits.*

**Correct answer:** A — The context window capacity may be exceeded, causing parts of the report to be dropped or ignored.

**Explanation:**  
While modern models can condense long documents into clear executive summaries, extremely large files (like a 500-page report) can challenge context window limits or dilute attention across thousands of tokens. If the document exceeds the active context capacity, older or middle sections may be truncated. The C and B options are absurd exaggerations. A practical solution is to chunk the document into chapter summaries, process them sequentially, and then synthesize a final overview. This workflow ensures that important financial details are not lost.

---

## 8. What is the most effective approach to combining human and AI capabilities in technical workflows?

**Difficulty:** medium

- — A. Refuse to use AI tools for any task to avoid learning new software workflows.  
  *Incorrect: rejecting tools forfeits major productivity and learning benefits.*
- — B. Delegate 100% of all decision-making to AI without human review or code testing.  
  *Incorrect: unmonitored delegation introduces severe operational risks.*
- ✅ C. Leverage AI for rapid drafting, scale, and pattern analysis while reserving judgment and ethical oversight for humans.  
  *Correct: complementary strengths maximize efficiency and reliability.*

**Correct answer:** C — Leverage AI for rapid drafting, scale, and pattern analysis while reserving judgment and ethical oversight for humans.

**Explanation:**  
The most effective technical workflows leverage the complementary strengths of humans and artificial intelligence. AI excels at rapid text condensation, code scaffolding, parsing large datasets, and pattern recognition. Humans supply domain expertise, critical discernment, nuanced creativity, and final ethical responsibility. The B option is dangerous because AI cannot replace human accountability. The A option prevents professional growth. Staying abreast of tool capabilities allows engineers to design robust human-in-the-loop systems where automation speeds up work without compromising safety. In software engineering, for example, an agent can draft unit tests while senior developers inspect system architecture and edge cases.

---

## 9. A CLI coding assistant invents a non-existent parameter for a MikroTik router command. What caused this error?

**Difficulty:** hard

- — A. The router's network cable was physically unplugged during the terminal prompt.  
  *Incorrect: network physical state does not generate invented syntax.*
- — B. The AI model deliberately chose to destroy the user's networking hardware.  
  *Incorrect: models have no consciousness or malicious intent.*
- ✅ C. A plausible hallucination caused by probabilistic next-token generation without exact syntax verification.  
  *Correct: the model generated a plausible-sounding command that does not exist.*

**Correct answer:** C — A plausible hallucination caused by probabilistic next-token generation without exact syntax verification.

**Explanation:**  
This error is a classic technical hallucination. The language model combined patterns from general networking documentation and generated a plausible-sounding parameter that looks legitimate but is not supported by RouterOS. Because the model predicts tokens probabilistically rather than testing the command against live hardware, it cannot detect the syntax error internally. The A option is an unrelated physical cabling issue. The B option falsely anthropomorphizes the model. Practicing discernment by testing scripts in a lab environment prevents live configuration outages.

---

## 10. Why will human discernment remain necessary for the foreseeable future despite advances in AI tools?

**Difficulty:** hard

- ✅ A. Because statistical generation can still produce subtle inaccuracies, bias, or misaligned recommendations that require human oversight.  
  *Correct: human judgment remains essential for validating truth and safety.*
- — B. Because all AI development will permanently stop next month by international law.  
  *Incorrect: AI technology continues to accelerate rapidly.*
- — C. Because language models will lose their ability to process English vocabulary after updates.  
  *Incorrect: future models expand linguistic and reasoning capabilities.*

**Correct answer:** A — Because statistical generation can still produce subtle inaccuracies, bias, or misaligned recommendations that require human oversight.

**Explanation:**  
Human discernment will remain indispensable for the foreseeable future because language models generate outputs statistically. Even with breakthroughs like retrieval-augmented generation and extended thinking, models can still misinterpret ambiguous requirements, produce subtle hallucinations, or reflect training data biases. The B option is factually untrue. The C option is nonsensical because model capabilities are expanding. Fluent professionals leverage AI for productivity while actively verifying that outputs align with technical standards, business objectives, and ethical norms. Ultimately, responsibility for production code, security policies, and published documentation rests with human engineers, making active review an irreplaceable skill.

---
