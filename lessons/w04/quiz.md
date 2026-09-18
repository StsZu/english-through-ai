# Quiz

## 1. What is the primary difference between traditional AI systems and generative AI?

**Difficulty:** easy

- — A. Traditional AI only operates on mobile devices, while generative AI requires mainframe computers.  
  *Incorrect: hardware type does not define the functional difference.*
- — B. Generative AI copies fixed pre-written answers from a static database table.  
  *Incorrect: generative models predict new tokens instead of database retrieval.*
- ✅ C. Generative AI creates completely new content, while traditional AI analyzes and categorizes existing data.  
  *Correct: generative AI synthesizes new text, code, and media.*

**Correct answer:** C — Generative AI creates completely new content, while traditional AI analyzes and categorizes existing data.

**Explanation:**  
Generative AI is defined by its ability to create novel content that did not previously exist, rather than merely classifying or filtering existing data. A traditional machine learning model might identify whether an incoming email is spam by examining pattern matches. In contrast, a prominent generative model like Claude can draft a completely new, context-aware reply for you. The A option is incorrect because the distinction is architectural, not based on device format. The B option is wrong because language models generate text dynamically based on learned probabilities rather than retrieving canned static database answers.

---

## 2. Why was the introduction of the transformer architecture in 2017 considered a major game changer?

**Difficulty:** easy

- ✅ A. It allowed AI systems to maintain relationships between words across long passages of text.  
  *Correct: attention mechanisms process context across long sequences effectively.*
- — B. It replaced all neural networks with simple spreadsheet formulas and rules.  
  *Incorrect: transformers are advanced deep neural network architectures.*
- — C. It completely eliminated the need for computational hardware like GPUs and TPUs.  
  *Incorrect: transformers require massive compute clusters to train.*

**Correct answer:** A — It allowed AI systems to maintain relationships between words across long passages of text.

**Explanation:**  
The transformer architecture was a technological breakthrough and a true game changer because it enabled parallel processing of sequences while tracking semantic relationships across long text passages. Before transformers, older recurrent neural networks struggled with memory over long sentences and could not easily scale across large computer clusters. The C option is false because modern transformer training demands thousands of specialized GPUs and TPUs. The B option is absurd because transformers represent complex multi-layer neural networks. This self-attention breakthrough forms the foundation of modern large language models, image generators, and coding assistants.

---

## 3. What occurs during the initial pre-training phase of a large language model?

**Difficulty:** easy

- — A. Human editors manually write answers for every possible user prompt.  
  *Incorrect: pre-training is self-supervised on billions of text documents.*
- — B. The model is connected directly to live router interfaces to execute commands.  
  *Incorrect: initial pre-training only ingests raw text datasets.*
- ✅ C. The model analyzes vast amounts of text and learns to predict what word comes next.  
  *Correct: next-token prediction builds statistical knowledge of language.*

**Correct answer:** C — The model analyzes vast amounts of text and learns to predict what word comes next.

**Explanation:**  
During pre-training, an LLM analyzes a vast collection of text documents and learns by predicting the most probable next word across billions of examples. Through repeated iterations, the system builds a rich internal map of syntax, factual associations, and abstract concepts. The A option is wrong because manual curation at this scale is impossible—pre-training relies on self-supervised learning across web data, books, and code. The B option confuses training with deployment tools. Pre-training gives the model broad knowledge, which is later refined during fine-tuning to follow specific instructions safely and helpfully.

---

## 4. What are scaling laws in modern artificial intelligence research?

**Difficulty:** medium

- ✅ A. Empirical rules showing that model performance improves predictably as compute, data, and parameters increase.  
  *Correct: scaling laws describe predictable quality gains from scale.*
- — B. Hardware limits that cause neural networks to lose all reasoning abilities when expanded.  
  *Incorrect: scaling produces stronger and emergent abilities rather than degradation.*
- — C. Government regulations that limit how many users can access a chatbot daily.  
  *Incorrect: scaling laws are mathematical and empirical research observations.*

**Correct answer:** A — Empirical rules showing that model performance improves predictably as compute, data, and parameters increase.

**Explanation:**  
Scaling laws are empirical scientific observations showing that as models grow in parameter count, training dataset size, and compute budget, their loss decreases and performance improves in mathematically predictable curves. Researchers at Anthropic and other labs discovered that scaling is not merely incremental—it also unlocks emergent capabilities such as step-by-step reasoning that were never explicitly coded. The C option confuses scientific scaling laws with public policy regulations. The B option contradicts reality, as increased scale consistently produces more capable and nuanced models. Understanding scaling laws helps engineers plan compute investments.

---

## 5. How does fine-tuning differ from pre-training in the model development pipeline?

**Difficulty:** medium

- ✅ A. Fine-tuning uses instruction datasets and reinforcement learning to make the base model helpful, honest, and harmless.  
  *Correct: fine-tuning aligns the raw base model for conversational collaboration.*
- — B. Fine-tuning erases all vocabulary knowledge learned during the pre-training phase.  
  *Incorrect: fine-tuning builds directly on top of pre-trained knowledge.*
- — C. Fine-tuning is a hardware maintenance process that cleans dust from TPU cooling fans.  
  *Incorrect: fine-tuning is an algorithmic model training process.*

**Correct answer:** A — Fine-tuning uses instruction datasets and reinforcement learning to make the base model helpful, honest, and harmless.

**Explanation:**  
Fine-tuning takes a raw pre-trained base model and shapes its behavior using high-quality instruction examples and reinforcement learning with human feedback (RLHF). This process teaches the assistant how to converse constructively, format responses clearly, decline harmful requests, and follow complex system prompts. The B option is incorrect because fine-tuning preserves the general language comprehension gained during pre-training. The C option is a joke about physical server maintenance. Without fine-tuning, a base model would simply continue your prompt text without realizing it is supposed to answer your question.

---

## 6. What is an AI model's 'context window' and why does it matter during real work?

**Difficulty:** medium

- — A. It is a physical glass screen installed on server racks in data centers.  
  *Incorrect: context window is a software token limit, not physical glass.*
- — B. It is a database table where all previous chat sessions from last year are stored permanently.  
  *Incorrect: context window is active memory for the current session only.*
- ✅ C. It is the working memory limit containing current prompts, files, and conversation history.  
  *Correct: models only process tokens inside their active context window.*

**Correct answer:** C — It is the working memory limit containing current prompts, files, and conversation history.

**Explanation:**  
The context window represents the maximum amount of text (measured in tokens) an LLM can actively hold in working memory during a conversation. It contains the system prompt, conversation history, user attachments, and generated replies. If a project exceeds this window, older context falls out of scope unless retrieved via external tools. The A option is an amusing literal confusion with physical windows. The B option confuses active context with persistent storage. In CLI agent workflows, monitoring token usage in the context window ensures that code snippets and error logs fit within available memory.

---

## 7. How does in-context learning allow a developer to teach an AI a custom formatting style?

**Difficulty:** medium

- — A. By deleting all punctuation marks from the user query before execution.  
  *Incorrect: punctuation removal does not teach task structures.*
- ✅ B. By providing two or three example inputs and outputs directly in the prompt without retraining the model.  
  *Correct: few-shot prompt examples guide output format dynamically.*
- — C. By renting GPU clusters to re-train the foundational model weights from scratch.  
  *Incorrect: in-context learning requires zero model retraining.*

**Correct answer:** B — By providing two or three example inputs and outputs directly in the prompt without retraining the model.

**Explanation:**  
In-context learning is the emergent ability of language models to recognize patterns and follow instructions directly from examples supplied within the prompt itself (often called few-shot prompting). You do not need to retrain the neural network or modify its internal weights under the hood. The C option describes expensive full pre-training, which is unnecessary for formatting tasks. The A option is irrelevant. For example, if you want an AI to convert router logs into a specific JSON schema, showing two sample transformations in your prompt enables the model to format subsequent inputs accurately.

---

## 8. Why can unexpected 'emergent capabilities' appear when language models scale up in size?

**Difficulty:** medium

- ✅ A. Because complex multi-layered representations allow the network to combine patterns into novel reasoning steps.  
  *Correct: emergent abilities arise organically from scale and depth.*
- — B. Because software engineers secretly write hidden if-else statements inside the weights.  
  *Incorrect: neural network weights are mathematical matrices, not hardcoded code.*
- — C. Because the model connects directly to quantum satellites during nighttime hours.  
  *Incorrect: emergent behaviors stem from classical matrix multiplication at scale.*

**Correct answer:** A — Because complex multi-layered representations allow the network to combine patterns into novel reasoning steps.

**Explanation:**  
Emergent capabilities arise because deep neural networks trained on vast datasets learn generalized abstract representations across diverse domains. As parameter count and compute increase according to scaling laws, the model learns to compose simple linguistic associations into sophisticated reasoning chains, solving multi-step logic problems without explicit coding. The B option is false because neural models contain billions of floating-point numbers rather than manual rule trees. The C option is science fiction. Emergence is one of the most fascinating phenomena in machine learning, demonstrating that scale creates qualitative functional jumps.

---

## 9. A developer runs a CLI agent on a large codebase, and the agent suddenly forgets early instructions. What happened under the hood?

**Difficulty:** hard

- — A. The agent switched automatically from reinforcement learning to binary machine code execution.  
  *Incorrect: execution mode does not alter context retention dynamics.*
- ✅ B. The session history and code diffs exceeded the active context window limit, causing older tokens to be dropped.  
  *Correct: exceeding context capacity forces truncation of earlier context.*
- — C. The transformer architecture suffered permanent hardware damage and forgot its pre-training weights.  
  *Incorrect: model weights remain unchanged; only ephemeral conversation memory overflowed.*

**Correct answer:** B — The session history and code diffs exceeded the active context window limit, causing older tokens to be dropped.

**Explanation:**  
When an agent loses track of early instructions, the conversation transcript and code files have exceeded the model's active context window. Language models have a strict upper boundary on how many tokens they can ingest in a single forward pass; once history overflows, older messages are truncated or summarized. The C option is incorrect because the pre-trained weights in data centers remain completely intact. The A option is nonsense. To prevent this issue in large coding sessions, experienced engineers break large refactors into smaller commits and periodically clear non-essential terminal outputs.

---

## 10. Why is reinforcement learning with human feedback (RLHF) critical before deploying AI assistants to the public?

**Difficulty:** hard

- — A. Because fine-tuning is only permitted by law on desktop computers without internet access.  
  *Incorrect: model training occurs on cloud supercomputing clusters.*
- ✅ B. Because raw pre-trained models predict likely text without considering truthfulness, safety boundaries, or helpfulness.  
  *Correct: RLHF aligns statistical word prediction with human ethical standards.*
- — C. Because reinforcement learning reduces the power consumption of server hardware to zero watts.  
  *Incorrect: reinforcement learning is an alignment method, not an electrical power tool.*

**Correct answer:** B — Because raw pre-trained models predict likely text without considering truthfulness, safety boundaries, or helpfulness.

**Explanation:**  
Reinforcement learning is essential because a raw pre-trained model is simply a statistical next-word prediction engine. Left unaligned, it might autocomplete dangerous instructions, reproduce internet toxicity, or generate misleading claims. Through fine-tuning and reinforcement learning, human feedback guides the reward model to favor helpful, honest, and harmless responses while penalizing harmful outputs. The C option is physically impossible. The A option is factually inaccurate. This alignment breakthrough transforms raw language models into reliable, professional collaborators suitable for production environments. In practice, techniques like Constitutional AI allow models to critique their own drafts against written safety rules during reinforcement training.

---
