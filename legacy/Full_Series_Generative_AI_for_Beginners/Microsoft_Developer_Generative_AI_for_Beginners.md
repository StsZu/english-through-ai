Эпизод 1: Introduction to Generative AI and LLMs [Pt 1]

0:09

9 секунд

hi everyone and welcome to the first lesson of the generative AI for beginners course uh this course is based

0:16

16 секунд

on an open source curriculum with the same name available on gab that you can find at a link on the screen I'm carot

0:24

24 секунды

Castello I'm A Cloud Advocate at Microsoft focused on artificial intelligence Technologies and in this video video I'm going to introduce you

0:31

31 секунда

to generative Ai and large language models large language models represent

0:38

38 секунд

the Pinnacle of AI technology pushing the boundaries of what was once foring possible they've conquered numerous

0:45

45 секунд

challenges that older language models struggled with achieving human L performance in various

0:52

52 секунды

tasks they have sever capabilities and applications but for the sake of this course we'll explore how larg large

1:00

1 минута

language models are revolutionizing education through a fictional startup that we'll be referring to as our

1:08

1 минута 8 секунд

startup our startup works in the education domain with the Ambi with the ambitious mission of improving

1:15

1 минута 15 секунд

accessibility in learning on a global scale ensuring Equitable access to education and providing personalized

1:22

1 минута 22 секунды

learning experiences to every learner according to their needs in this course we'll de into to how our startup

1:31

1 минута 31 секунда

harnesses the power of generative AI to unlock new possibilities in education we also examine how they

1:39

1 минута 39 секунд

address the enevitable challenges tied to the social impact of this technology and its technological limitations but

1:47

1 минута 47 секунд

let's start by defining some basic concept we'll be using throughout the course despite the uh relatively recent

1:56

1 минута 56 секунд

hype surrounding generative AI we can say that in the last couple of years we have really uh heard of generative AI

2:04

2 минуты 4 секунды

everywhere and every time um but this technology has been decades in the making with its Origins racing back to

2:11

2 минуты 11 секунд

the 1950s 1960s uh the early AI Pro types consisted of type pretend chatbots

2:19

2 минуты 19 секунд

relying on knowledge bases maintained by experts uh this chatbots generated responses based on keywords found in

2:28

2 минуты 28 секунд

user input but it's soon became clear that this approach had scalability limitations a significant Turning Point

2:36

2 минуты 36 секунд

arrived in the 1990s when a statistical approach was applied to text analysis and this gave birth to machine learning

2:45

2 минуты 45 секунд

algorithms uh which could learn patterns from data without explicit programming and these algorithms allowed machines to

2:54

2 минуты 54 секунды

simulate human language understanding ping the way for the eye we know today in more recent times advancements in

3:02

3 минуты 2 секунды

Hardware technology allowed for development of advanced masch learning algorithms particularly neural networks

3:11

3 минуты 11 секунд

these Innovations significantly improved natural language processing enabling machines to understand the context of words in

3:19

3 минуты 19 секунд

sentences this breakthrough technology powered the birth of virual assistance in the early 21st century this viral

3:27

3 минуты 27 секунд

assistance excelled at interpreting human language identifying needs and taking actions to fulfill them such as

3:35

3 минуты 35 секунд

answering queries with predefined scripts or connecting to third party services and so we arrived at generative

3:44

3 минуты 44 секунды

AI a subset of deep learning after Decades of AI research a new model

3:50

3 минуты 50 секунд

architecture known as the Transformer um emerged and Transformers could handle longer text sequences as input and were

4:00

4 минуты

based on the attention mechanism enabling them to focus on the most relevant information regardless of its

4:07

4 минуты 7 секунд

order in the input text today M generative AI models often referred to as large language models are

4:16

4 минуты 16 секунд

built upon the Transformer architecture and that's uh what the T in gbt uh actually

4:25

4 минуты 25 секунд

means um these models trained on vast amounts of data from sources like like books articles and websites possess a

4:33

4 минуты 33 секунды

unique adaptability they can tackle a wide range of tasks and generate chromatically correct text with a hint

4:39

4 минуты 39 секунд

of creativity but let's dive deeper into the mechanism of large language models and shed light on the inner workings of

4:48

4 минуты 48 секунд

models like o the openi gbts one of the key concept to grasp is

4:56

4 минуты 56 секунд

tokenization large language models receive text as input and produce text as output if we want to really simplify

5:04

5 минут 4 секунды

the mechanism however these models work much more efficiently with numbers rather than with row text sequences and

5:14

5 минут 14 секунд

that's where the tokenizer comes into play text prompts are chunked into tokens uh helping the model in

5:22

5 минут 22 секунды

predicting the next token for completion models also have a maximum a

5:29

5 минут 29 секунд

Max maximum length of token window and model pricing is also typically computed by the number of tokens used in output

5:38

5 минут 38 секунд

and inputs so um tokenization is really an important Concept in large language

5:45

5 минут 45 секунд

models and generative I domain now a token is essentially a

5:51

5 минут 51 секунда

chunk of text which can vary in length uh and typically consist of a sequence of characters and the tokenizer primary

6:00

6 минут

job is to really is to really break down the input text into an array of those tokens um which are then further mapped

6:10

6 минут 10 секунд

to token indices these token indices are essentially integer and coding of the original text chunks making it easier

6:18

6 минут 18 секунд

for the model to process and understand now let's move to predicting

6:26

6 минут 26 секунд

the output tokens um given an input sequence of n tokens with the maximum n varing from

6:35

6 минут 35 секунд

one model to another according to the maximum um content window length or for

6:42

6 минут 42 секунды

for one model uh the model is designed to predict a single token as its

6:48

6 минут 48 секунд

output but here's where it gets interesting the predicted token is then incorporated into the input of the next

6:57

6 минут 57 секунд

iteration creating an expans window pattern and this pattern allows the model to provide more coh coherent and

7:05

7 минут 5 секунд

contextually relevant responses often extending to one or multiple

7:12

7 минут 12 секунд

sentences now let's delve into the selection process the model chooses the output token based on its probability of

7:21

7 минут 21 секунда

occurring after the current text sequence this probability distribution is calculating using the model's training data

7:30

7 минут 30 секунд

however here's the twist the model doesn't always choose the token with the highest probability from the distribution to simulate the process of

7:39

7 минут 39 секунд

creative thinking a degree of Randomness is introduced into the selection process this means that the model doesn't

7:46

7 минут 46 секунд

produce the exact same output for the same input every time that's the element that allows generative AI to generate

7:55

7 минут 55 секунд

Tex that feels you know creative and engaging now we said that the main capability of a large language model is

8:02

8 минут 2 секунды

generating a text from scratch starting from a textual input written in natural language but what kind of textual input

8:11

8 минут 11 секунд

and output first of all let me say that input of a large language model is known as prompt while the output is known as

8:20

8 минут 20 секунд

completion um term that refers to the model mechanism of generating the next token to complete the current input

8:29

8 минут 29 секунд

let's do some examples of prompts and completion by using the open AI CH gbt playground um always in our educational

8:37

8 минут 37 секунд

scenario now a prompt may include an instruction specifying the type of output we expect from the model in the

8:44

8 минут 44 секунды

example we are seeing we are asking to write an assignment for a high for high school students including four

8:51

8 минут 51 секунда

open-ended questions um about Lou 14 and his court and you can see that the

8:58

8 минут 58 секунд

output is exact what I'm asking for um so the mother was able to generate an assignment with the

9:05

9 минут 5 секунд

questions now another kind of prompt might be uh a question asked in the form of a conversation with an agent in this

9:14

9 минут 14 секунд

example we are asking about Luis 14th um in a question so we asked who is Luis 14

9:21

9 минут 21 секунда

and why he is an important historical character and we've got an answer another type of trump might be a

9:29

9 минут 29 секунд

of text to complete so an incipit of a text to complete and you can see now that we um used a an insit of a text to

9:39

9 минут 39 секунд

complete as prompt and we've got a whole paragraph to um um complete the the

9:47

9 минут 47 секунд

current input so this is basically an implicit ask for writing assistance now

9:54

9 минут 54 секунды

the examples I just did are quite simple and don't want to be you know an examp itive demonstration of large language

10:01

10 минут 1 секунда

models capabilities they just want to show you the potential of using generative in particular but not limited

10:09

10 минут 9 секунд

in a context such as the educational context we have used today as example that's all for now uh in the

10:16

10 минут 16 секунд

following lesson we are going to explore different types of generative AI models and we're going to cover also how to

10:23

10 минут 23 секунды

test uh to iterate and to improve the performance and compare also different mod us to find the most suitable one for

10:31

10 минут 31 секунда

a specific use case thank you hey folks welcome back to dtive AI

Эпизод 2: Exploring and comparing different LLMs [Pt 2]

10:43

10 минут 43 секунды

for beginners here at Microsoft learn I am Pabo Lopez Cloud advocate inet in artificial intelligence and with here

10:50

10 минут 50 секунд

with carlot say hi carlot hi hi everyone I'm carot cucho I'm A Cloud Advocate focused on artificial intelligence

10:59

10 минут 59 секунд

that's incredible so today let's talk about a little bit on the basics you're starting you started on the in introduction now let's go deeper let's

11:07

11 минут 7 секунд

see how can we explore and compare different llms of course now that we have aurei are llms but if you want to

11:15

11 минут 15 секунд

take a look at that we can talk a lot later but we're going to talk a little bit about the comparisons on language models so going from here you're going

11:23

11 минут 23 секунды

to see a little bit of foundation models language models and later carot you show a little bit on Azure AI so what you going to learn today you may

11:32

11 минут 32 секунды

have heard of foundation models so let's understand Foundation models verus llms and language models how to classify a language model because they have a lot

11:40

11 минут 40 секунд

of classifications for them and then carlot you show a little bit of azure

11:47

11 минут 47 секунд

AI let's go with Foundation models versus llms but you understand this let's start with Foundation models

11:56

11 минут 56 секунд

themselves why because you may have seen a lot of a little bit of heard about Foundation models Z LS Etc you may have

12:05

12 минут 5 секунд

been confused on how those work let's think about it a little bit the foundation models they do the following

12:12

12 минут 12 секунд

so usually it's the base is a the the basis of you're deploying something new so what does you mean about it Pablo

12:21

12 минут 21 секунда

okay let's think about like this imagine that I have a foundation model that I want you to do multiple tasks so here I

12:28

12 минут 28 секунд

have a teaching one so you can put like a multimodel data source to train it so

12:35

12 минут 35 секунд

it can have teaching materials videos interaction and the subject M matters and then we have like CTIC so we can have multiple assist students Educators

12:44

12 минут 44 секунды

facilitate learning teaching and there's a subject matter so you can see that we have a lot of input here we have a bunch of things we are training with and they

12:52

12 минут 52 секунды

we can have a lot of tests and goals but you see that it does a lot of things right but it may not do them perfectly

13:02

13 минут 2 секунды

we may need to you know guide them in how to do X or Y so as this Educators how to assess them right because you

13:09

13 минут 9 секунд

don't have like instructions to you know understand how is helping it then it's Foundation why because it's the basis of

13:16

13 минут 16 секунд

our constructing new Solutions so that's why you're call the foundation models and let's bring this graph as well so

13:24

13 минут 24 секунды

let's think about this and Foundation models were brought by Stanford researchers researchers so that's why you're using like that so the foundation

13:33

13 минут 33 секунды

models here are very simple they have some prerequisites need to be pre-trained generalized adaptable large

13:40

13 минут 40 секунд

and self-supervised so you may see right here that Foundation models can cover a lot of things and you might may note as

13:48

13 минут 48 секунд

well if you know a little bit about llms that they fulfill all those five so yes llms are foundational models because

13:57

13 минут 57 секунд

they fulfill all those five however not all Foundation models are llms because they can they don't use

14:06

14 минут 6 секунд

language sometimes as I said they use a multim model we to no learn so they have a multi model weight to as how to answer

14:13

14 минут 13 секунд

how to interpret they don't use tokenizer sometimes so that's the difference so yes Foundation models are

14:20

14 минут 20 секунд

very important because our llms are Foundation models but not all Foundation models are llms

14:29

14 минут 29 секунд

that's incredible but now that we understood those we're going to start talk a little bit of our language models

14:36

14 минут 36 секунд

themselves right so then it brings a classic right open source verus

14:43

14 минут 43 секунды

proprietary so let's think about open source a little so when you have open source nowadays we had like a big

14:51

14 минут 51 секунда

expansion right a lot of companies are doing open source language models which are incredible but let's think about a

14:58

14 минут 58 секунд

little bit so what are those means right so open source usually they are open sourcing some of the parts that they use

15:06

15 минут 6 секунд

to you know or train the llm so imagine that you have like the code that I use to train some provides the weights if

15:13

15 минут 13 секунд

you don't know the weights are basically the the fine tuning of the the language model so it can like go inside and try

15:20

15 минут 20 секунд

to investigate or even some provide like the full model that you can just download and go and you know start having fun with and you can tweak and Dr

15:29

15 минут 29 секунд

everything so these are incredible but here's the thing a lot of them are provided by you know research groups or

15:37

15 минут 37 секунд

NOS so those usually what they have they don't can have a lot of know resources should be supported and to be updated

15:46

15 минут 46 секунд

with new features or you know new updates on security on especially if you think about promp injection Etc so you

15:53

15 минут 53 секунды

may see here that yes open source is incredible but they can have some faults here and there or maybe their license

16:01

16 минут 1 секунда

aren't permissive enough that what we want to do so open source opens a lot of small issues here and there that you

16:08

16 минут 8 секунд

need to think about if you want to solve proprietary usually they are much easier they are already provided a lot of those

16:16

16 минут 16 секунд

of course they're provided by apis if you go to cloud services but what is good about proprietary is that you know

16:24

16 минут 24 секунды

you're going to get you know a lot of things done correctly so you're going to have like like updates constantly the models of course it limits you the they

16:32

16 минут 32 секунды

opportunity to fine tune the model but usually it means that you're going to have a lot of things that you can already use it's a already made solution

16:41

16 минут 41 секунда

that you can go and grab and go okay so you learn a little bit of the open source models and about the proprietary

16:49

16 минут 49 секунд

if you ask open source you have a bunch of them right you have Falcon we have a llama we have old Lama as well so we

16:58

16 минут 58 секунд

have a bun and our proprietary can ask about you know jbt so why I'm saying this because you notice that I didn't talk about eddings

17:07

17 минут 7 секунд

right so what are the embedding one so let's pick an openi add so let's talk about here about their categorizations

17:15

17 минут 15 секунд

you're noticing that they have like very strict categorizations here so let's go to a language model that converts

17:22

17 минут 22 секунды

everything to embeding so we have a string we have a prompt you need somebody to communicate imagine that

17:29

17 минут 29 секунд

that you know I have a format that you know I can communicate with different models right so getting is to convert to

17:36

17 минут 36 секунд

in beddings are great because then I can easily imagine that I can use it for systems like rock that I

17:45

17 минут 45 секунд

can store alling beddings and I again search and I got my information back so Bings are very important for systems

17:53

17 минут 53 секунды

today on generative Ai and it's not only that they are used to communicate mul multiple types of language systems

18:01

18 минут 1 секунда

language models so it's just very simple back string convert to edding that everyone can understand then we have

18:10

18 минут 10 секунд

language models to my generation that everyone knows Dolly everyone already play and you have as well on web co-pilot so I have a prompt here so you

18:19

18 минут 19 секунд

have like in quotes and then you're going to put in your generative AI neon Network and then boom you're gonna have an image so here you have a painting of

18:26

18 минут 26 секунд

a flying dog and here have a no this incredible image then the classics who didn't already use sex generation right

18:35

18 минут 35 секунд

everyone here already had some fun with it so you go to atic co-pilot web as well jbt you can go as if you even go to

18:45

18 минут 45 секунд

hugging face right you can access on hugging face a lot of the other mobs that have Falcon orama we have mol and

18:52

18 минут 52 секунды

those are incredible so basically put a prompt and then you have prompt engineer that you're going to see later in this course and then the gener AI starts to

19:00

19 минут

write it and then it generates a text and it can be text it can be code we have of course some that are optimized for code but you can see here that is

19:09

19 минут 9 секунд

how it works so we have usually those are the three um more defined ones well of course if you want to break it down you can do like specialize you can do a

19:18

19 минут 18 секунд

lot of you know extra things here and there remember you can always you know interact of this those language models and you what you need for you know your

19:27

19 минут 27 секунд

business your hobby or anything you want to great let's talk about service versus model remember what I talked before that

19:35

19 минут 35 секунд

you can easily access some of the incredible models in the cloud exactly why I say that because those are earn

19:43

19 минут 43 секунды

the service what it means those are already you know start the cloud you cannot change the yourself without you

19:51

19 минут 51 секунда

know going more inside and try to just mind tuning but basically those are story and they are easy usually API call

19:59

19 минут 59 секунд

you just you know send it send your prompt and then you can an answer you need to deal with scalability the

20:05

20 минут 5 секунд

scalability the cloud are us of you your security is defined on how is your security on the cloud as well so

20:13

20 минут 13 секунд

everything is tight a niche and not only that you can actually integrate all your services so that's the good part about

20:21

20 минут 21 секунда

having the service right you don't it's easier to manipulate and do sometimes um if you want to change a little bit but

20:28

20 минут 28 секунд

of course we on fine tun in a bunch of services but that's important you to know but after this you can have like

20:36

20 минут 36 секунд

easy way to interact with this the model is a little bit harder because you need to download the model you need to set up imagine that you have a server right so

20:44

20 минут 44 секунды

you need to take care of the server take care about scalability imagine that you have multiple clients coming in so the

20:52

20 минут 52 секунды

model is for you to interact directly it makes easy interacting directly it goes It goes much more easy it you're trying to understand how this is working and

21:01

21 минута 1 секунда

the pipeline but imagine that you need to interact with your cloud service I need to tr something it makes much harder without the ecosystem but you

21:10

21 минута 10 секунд

have more full control but you need to deal with infrastructure costs Etc so now I'm very interested and carlot can

21:19

21 минута 19 секунд

tell me how Azure AI Studio you know how it works I actually don't know of course uh thanks Pablo um yeah I'm I'm happy to

21:27

21 минута 27 секунд

walk you through you know how to use Foundation models in asure and specifically in a studio and the first question I want to cover here is why

21:37

21 минута 37 секунд

eror right uh so in the ever evolving landscape of foundation models uh selecting the right candidate for your specific scenario is just the beginning

21:46

21 минута 46 секунд

of the journey so once you have identified your top choices it's time to put them to test uh on your use case uh

21:53

21 минута 53 секунды

so a studio is your One-Stop platform for developing test testing and managing the entire life cycle of your AI

22:02

22 минуты 2 секунды

applications in fact this platform integrates Microsoft data Technologies for optimized storage and search in

22:09

22 минуты 9 секунд

databases a wide range of pro proprietary and open source large language models um that Pablo just

22:16

22 минуты 16 секунд

presented uh for example from the open family but also from Partners like meta a hugging phas or

22:23

22 минуты 23 секунды

mistra uh tools that enable ensuring responsible and secure development of AI applications but also prompt engineering

22:30

22 минуты 30 секунд

and evaluation facilities as well as monitoring assets for Genera applications now recalling our

22:38

22 минуты 38 секунд

educational startup scenario let's imagine that uh after extensive research our startup has explored the current large

22:46

22 минуты 46 секунд

language models landscape and have pinpointed some strong contenders for the unique scenario uh now the real fun

22:53

22 минуты 53 секунды

begins because testing these models involves an iterative process using experiments and prees uh measures to

23:01

23 минуты 1 секунда

ensure they meet the mark and and where they can you know um where where they can test these

23:07

23 минуты 7 секунд

models they can do that using uh the model catalog in a studio um hrii Studio

23:14

23 минуты 14 секунд

provides a seamless experience with you know a user friendly interface so here's what you can do in the model catalog you

23:22

23 минуты 22 секунды

can easily find the foundation model of your interest by using different filters such as you can search for um the model

23:30

23 минуты 30 секунд

provider that can be Azure open can be meta can be hugging phase and so on and so forth you can search for inference or

23:39

23 минуты 39 секунд

fine-tuning task for example you can uh search for Q&A or summarization task or object detection for computer vision

23:47

23 минуты 47 секунд

kind of scenarios um and also you can filter by license for example and you can even look for a specific model of

23:54

23 минуты 54 секунды

course by searching its name in the in the search box um now once you you know

24:01

24 минуты 1 секунда

um once you select a model before you proceed with the deployment of the model itself it's always a good idea to get to

24:08

24 минуты 8 секунд

know your model a bit um so the model card in the model catalog provides a comprehensive view um complete with

24:17

24 минуты 17 секунд

detailed description of use cases and training data of the model you selected and for some models you can also find

24:25

24 минуты 25 секунд

some code samples providing uh with providing us with a sense of how inputs and outputs look like for real time

24:33

24 минуты 33 секунды

inference um also sometimes a bit of fine-tuning is necessary and s studio empowers you to improve your modest

24:41

24 минуты 41 секунда

performance with custom Training data for a selected subset of models in the model catalog um like Lama 2 uh 70b that

24:51

24 минуты 51 секунда

you see here in this slide uh once your model is you know primed and ready it's time to deploy it whether it's the

24:59

24 минуты 59 секунд

original pre-train model or your final final tuned version H Studio has has you

25:06

25 минут 6 секунд

covered in terms of deployments for a few models like lamb 2 here um or the

25:13

25 минут 13 секунд

ones of the meta collection in general you have a couple of options you can go with the standard deployment approach

25:20

25 минут 20 секунд

which is real time and point uh so you deploy your model in your Asia subscription and you manage the infrastructure used for inference um or

25:31

25 минут 31 секунда

you can use the recent pay as you go type of deployment that has been introduced um and this means that you

25:38

25 минут 38 секунд

can consume for in this case Lama 2 uh model as a rest API without caring about you know the underlying infrastructure

25:47

25 минут 47 секунд

uh with an experience similar to using aure OPI Service uh apis um so just

25:54

25 минут 54 секунды

consuming uh it as uh through a rest API and and this is what we call model as a

26:01

26 минут 1 секунда

service now another interesting feature of H studio is the model benmark um here you can basically compare different

26:09

26 минут 9 секунд

models in the catalog using filters to determine the specific subset against some predefined performance metrics such

26:17

26 минут 17 секунд

as accuracy fluency coherence uh and so on and so forth and there are several test data set you can choose

26:26

26 минут 26 секунд

um to use for for the comparison uh when it comes to deploying

26:33

26 минут 33 секунды

large language models into production uh businesses have a word of options each with its own set of complexities of

26:41

26 минут 41 секунда

course cost but also quality levels um let's dive into these approaches and see which one suits you know different

26:49

26 минут 49 секунд

requirements the first approach is leveraging prompt engineering with context uh now pre-trained large language models excel in hand handling

26:58

26 минут 58 секунд

General language task and you can simply feed them a short prompt like a question or an incomplete sentence um and they

27:06

27 минут 6 секунд

work like a charm right um and we call this zero short learning but here's the catch the more context you provide the

27:14

27 минут 14 секунд

better the large language model understands your request and when you include detail uh detailed examples and

27:21

27 минут 21 секунда

and request uh this approach is called One Shot learning if you're using a single example or few shot learning if you're using multiple

27:30

27 минут 30 секунд

examples in the case of a conversation you can even use the prompt to describe the personality of the assistant for example the style and the tone of the

27:39

27 минут 39 секунд

responses or pass the conversation history into the prompt uh this approach is cost effective and and a great

27:47

27 минут 47 секунд

starting point then approach two uh is uh using retrieval augmented generation which is

27:54

27 минут 54 секунды

a pattern um I would say um a specific technique prompt engineering technique

28:01

28 минут 1 секунда

um in fact large language models have their limitations and because they only know what they were trained on and can't

28:08

28 минут 8 секунд

access post trainining information or private company data for example and to bridge this Gap uh we use this pattern

28:17

28 минут 17 секунд

retrial augmented generation that adds external data in the form of documents CHS to your prompt effectively expanding

28:24

28 минут 24 секунды

its knowledge so we are passing data through the prompt but before doing that we are going to use some um some search

28:32

28 минут 32 секунды

pipeline to look for the data to add to our um context um in HRI platform this

28:40

28 минут 40 секунд

is powered by Vector database tools like HRI search uh rag is available approach when you know you lack the data the time

28:48

28 минут 48 секунд

or the resources to find tune your large language model but you want to boost its performance and minimize the risk of

28:55

28 минут 55 секунд

incorrect information or harmful content the third approach I would like to cover

29:01

29 минут 1 секунда

here is fine-tuning uh fine-tuning is a process that customize an llm for a specific task so it generates a new

29:10

29 минут 10 секунд

model with updated weights and biases making it it ideal if you have you know strict lency requirements so you cannot

29:17

29 минут 17 секунд

really have a huge context in the prompt or you possess high quality data and ground prooof labels and you can maintain them over time uh so fine

29:27

29 минут 27 секунд

tuning with the respect to rag requires additional competition competitional resources to adjust the weights um of

29:34

29 минут 34 секунды

the model now I want to say that uh these techniques I have uh presented here so prompt engineering retrieval

29:42

29 минут 42 секунды

augmented generation and fine-tuning are not um mutually exclusive they are complementary so there are cases in

29:49

29 минут 49 секунд

which you are going to use for example promp uring and fine-tuning other cases in which you are going to use the three of them

29:58

29 минут 58 секунд

the last approach I want to um to cover is uh training your own large language model now TR training an llm from

30:06

30 минут 6 секунд

scratch is a huge undertaking demanding vast amounts of data of high quality data skilled professionals and serious

30:14

30 минут 14 секунд

computational power you'd consider this option only if you have a very domain specific use case and also an abundance

30:22

30 минут 22 секунды

of domain Centric data um in the word of large language deployment there's no one-size Feit all solution so the right

30:29

30 минут 29 секунд

approach depends on your unique requirements resources and goals also the techniques we explored um as I said

30:38

30 минут 38 секунд

are not always mutually exclusive so there are cases in which you need to evaluate uh if you need to combine um a

30:46

30 минут 46 секунд

few of them um also any choice we take in terms of training and deployment we should be conscious and transparent

30:54

30 минут 54 секунды

about uh the technology limitations and use responsible practices and tools in the next episode you'll discover what

31:02

31 минута 2 секунды

this mean but for now I would like to wrap up and Pablo hey I want to bring you back just to say goodbye

31:10

31 минута 10 секунд

everyone folks it was a pleasure to talk more about generative AI carlot is incredible as well to learn more and I'm

31:18

31 минута 18 секунд

really excited to you know talk more of you folks I gonna come back soon as well for more lessons on J for beginers thank

31:25

31 минута 25 секунд

you so much and learn learn more with Microsoft learn awesome thanks

Эпизод 3: Using Generative AI Responsibly [Pt 3]

31:38

31 минута 38 секунд

everyone hi I'm Corey ster Pace part of the AI Cloud advocacy team here at Microsoft and I have the pleasure of

31:45

31 минута 45 секунд

delivering lesson number three using generative AI responsibly uh to you today and you know gener using

31:54

31 минута 54 секунды

generative AI responsibility is important whether you have one us user or 1,000 users or a million users it should be really at the Cornerstone of

32:02

32 минуты 2 секунды

everything you build with generative AI applications so let's dive deep into this concept and actually look at how we can apply it when we're building

32:10

32 минуты 10 секунд

applications for users so as an introduction of this lesson we're going to look at why we

32:17

32 минуты 17 секунд

should really prioritize responsible AI I mean we put this this lesson up early in this course but we want to make sure

32:24

32 минуты 24 секунды

that everything we do is wrapped around responsible AI then we're going to look at the core principles of responsible Ai and how

32:32

32 минуты 32 секунды

they relate to generative AI in particular and then lastly we're going to put these principles into practice it's great to have some principles but

32:40

32 минуты 40 секунд

like how do they actually apply to building generative AI applications is important to talk about our goals for this lesson are we're going to see the

32:48

32 минуты 48 секунд

importance of responsible AI when building generative AI applications we're going to learn how to apply those core principles of responsible Ai and

32:57

32 минуты 57 секунд

then lastly we're going to leave with some tools and strategies that you can use today to put these principles into

33:04

33 минуты 4 секунды

practice so why should you prioritize responsible AI here at Microsoft and in this course

33:11

33 минуты 11 секунд

we want to focus on taking a human Centric approach to application development and what that really boils down to is the user's best interest

33:20

33 минуты 20 секунд

equals the best results for your application and generative AI we realize create can create tons of value for your

33:28

33 минуты 28 секунд

users but that value can be lost in an instant in in terms of when responsible AI is also not maintained so we need to

33:37

33 минуты 37 секунд

make sure that impact requires monitoring and that intent is not enough we don't think people go into all the time saying they're going to build an

33:45

33 минуты 45 секунд

irresponsible generative AI application but we do think that if you're monitoring it and making sure even if you don't expect these things things to

33:53

33 минуты 53 секунды

come about is that you have the right necessar systems in place to deliver a responsible experience so let's look at

34:01

34 минуты 1 секунда

the potential harms that we might have with working with generative ey applications the first one is ungrounded outputs or errors these are most

34:09

34 минуты 9 секунд

commonly known things like hallucinations or Fabrications and they can be sometimes funny in terms of nonsensical responses or they could be

34:17

34 минуты 17 секунд

harmful like factual errors that might be used in other systems or even contradictions in responses whether it's stating a claim in one sentence and then

34:26

34 минуты 26 секунд

contradicting in the other or just even presenting completely irrelevant information to the user the next one it's not so funny and it's

34:34

34 минуты 34 секунды

harmful content uh large language models can produce uh in instructions in whether it's encouraging things like

34:41

34 минуты 41 секунда

self harm hateful or demeaning content or providing instructions maybe for either finding illegal content or even

34:50

34 минуты 50 секунд

acts of illegal content so we need to make our make sure we're keep an eye on that as well and then lastly is the lack of

34:58

34 минуты 58 секунд

fairness I tell my kids all the time life isn't fair but generative AI system should definitely be and fairness really

35:06

35 минут 6 секунд

equals free being free from bias and discrimination so this is making sure that the output is not producing anything that has exclusionary

35:14

35 минут 14 секунд

worldviews or has any bias towards any particular groups this is particularly important especially when we're talking

35:21

35 минут 21 секунда

about generating images or text and this aligns well with Microsoft's own responsible AI practice es whether

35:28

35 минут 28 секунд

that's being fairness reliability and safety privacy and security inclusion transparency and accountability so how

35:36

35 минут 36 секунд

to actually use generative AI responsibly now that we understand the potential harms that could come about the first thing is to measure these

35:44

35 минут 44 секунды

potential harms and we've we've encouraged taking like a similar idea to software testing but also making sure that you doing things like prompt

35:53

35 минут 53 секунды

testing and this what this means is you're actually aiming for a diversity of prompts that you uh that might be

36:00

36 минут

potentially used from your user and these aren't the ideal prompts these aren't things that always like you expect the happy path for your users but

36:09

36 минут 9 секунд

making sure uh that anything that might come about when you're deploying your applications to users or them using your

36:16

36 минут 16 секунд

application that you incorp that in your prompt testing I we would like to say you should start manual so you get you

36:24

36 минут 24 секунды

know sending a prompt to the large language model and receiving and evaluating that response but you can also scale this to to automation as well

36:33

36 минут 33 секунды

by batching these prompts and then also seeing the results there the starting manual gives you a high touch and very

36:41

36 минут 41 секунда

clear understanding of how your the large language models responding to your use case and there's four layers of

36:49

36 минут 49 секунд

mitigation that we're going to discover today as well one is on the model level building a safety system using correct

36:55

36 минут 55 секунд

meta prompts and then lastly on the user experience side so let's look how this actually plays out in practice first is

37:04

37 минут 4 секунды

the model side I like to say really easily right model right use case well Mo large language models can do many

37:11

37 минут 11 секунд

things but some of them are e more specialized than others and you know using the most powerful model is not always better better where you can maybe

37:20

37 минут 20 секунд

use things like a specialized model that maybe is more attained to your use case or even knowing the sort of parameters things like model temperature and how

37:29

37 минут 29 секунд

that affects responses and even the option of fine-tuning or have using a fine-tune model that maybe even more gear to your use case or what your users

37:37

37 минут 37 секунд

will be using your application for are all great ways to mitigate on the model side also in safety system things like

37:45

37 минут 45 секунд

content filtering so making sure that the responses from the model go through grows through their filter and does not present any harmful content uh also

37:54

37 минут 54 секунды

using things like responsible Ai and building out SCH scoring and metrics on responses and then lastly mod monitoring the model and its responses are all

38:03

38 минут 3 секунды

great ways to build a good pillar of Safety Systems next is meta prompt and this is really how we sort of Define the

38:12

38 минут 12 секунд

behavior or rules for the model in terms of how it engages with users we can ground the model on cont context or even using trusted data by using techniques

38:21

38 минут 21 секунда

like retrieval augmented generation which is actually covered in this course as well and then lastly most importantly is on the user experience side building

38:30

38 минут 30 секунд

transparency to users in terms of that there are engaging a generative AI application or a model is very important as well as even putting things like

38:39

38 минут 39 секунд

constraints or inputs uh from the user side to that you limit and mitigate the harms that they could bring about with their prompts and then even doing some

38:47

38 минут 47 секунд

input or output validation on the responses are also great ways to deliver a great user experience and a responsible

38:56

38 минут 56 секунд

one and now let's say putting this responsible AI into practice we've looked at the concepts we looked at mitigating harms but how do we actually

39:03

39 минут 3 секунды

get started well within Microsoft we have things like the Azure AI content safety these are API API endpoints and tools

39:12

39 минут 12 секунд

that allow for this information to uh information in your responses to be presented in a way uh that gets scanned

39:21

39 минут 21 секунда

before being delivered to your users whether that's analyzing the text building things like prompt Shields to scan attacks before for any user input

39:30

39 минут 30 секунд

ATT attacks as well as ground groundedness detection making sure the model is grounded in the source materials that have been provided by

39:38

39 минут 38 секунд

users we also have the responsible AI dashboard which allows us to keep score essentially on how the model is being

39:46

39 минут 46 секунд

responded and being interacted with with our users and gives you a good understanding and Overlook of how the model performs over time which is very

39:54

39 минут 54 секунды

important in terms of not only when we deliver the this generative AI application production the first time but the sixth time the 10th time or the

40:02

40 минут 2 секунды

100 time and then lastly we can do great things with monitoring via promp flow prom flow is an open source tool U we

40:11

40 минут 11 секунд

can also use it to find out and understand the type of responses that are being delivered to users and we have

40:19

40 минут 19 секунд

metrics around this whether it's coherence the type of responses if it's coherent if it's fluent the groundedness as I I mentioned earlier is it relevant

40:28

40 минут 28 секунд

to the actual prompt and how similar is it to other prompts that we have seen before these are all great things to give you an oversight and put those

40:36

40 минут 36 секунд

responsible AI practices uh principles into practice and that covers this

40:43

40 минут 43 секунды

responsible AI lesson you can check out more information in the full course at aka.ms genners

Эпизод 4: Understanding Prompt Engineering Fundamentals [Pt 4]

40:59

40 минут 59 секунд

hi welcome to Lesson Four of generative AI for beginners my name is Nan Nan I'm a senior Cloud Advocate on the AI advocacy team and I'm excited to talk to

41:07

41 минута 7 секунд

you about prompt engineering fundamentals So today we're going to first start off with a quick recap if you've been following the series you

41:15

41 минута 15 секунд

know most of the terms we'll just look at them really briefly then we'll talk about the three providers that you can use if you want to get started trying

41:23

41 минута 23 секунды

this out on your own but most of this is going to focus on prompt engineering you're going to learn what it is you're going to learn why it matters you're going to learn how to do prompt

41:31

41 минута 31 секунда

engineering and then we leave you with a sense of intuition for how you can build your own mindset for prompt Engineering in practice so let's get started a quick

41:40

41 минута 40 секунд

recap if you've been following this course these terms are probably familiar to you what is a prompt so we're talking generative AI large language models a

41:49

41 минута 49 секунд

prompt is just the natural language input the text input that the user provides and you can almost think of it as the way it programs the model to do

41:58

41 минута 58 секунд

what it wants or the user programs the model to do what they want so the response is then what the model does to kind of support the user request by

42:06

42 минуты 6 секунд

generating content fabrication you might have also heard of it by the term Hallucination is when sometimes the

42:14

42 минуты 14 секунд

model generates a response that may not be rooted in fact and we'll talk about that a base llm or large language model is really this foundational model that's

42:22

42 минуты 22 секунды

Stained on massive amounts of data think of it as a general purpose model that knows everything but sometimes you want specialized models things that know how

42:30

42 минуты 30 секунд

to do a task very well and that's what you look at for instruction tuned llms things that are good at summarization or

42:37

42 минуты 37 секунд

translation or code generation so what is prompt engineering prompt engineering is really this process where you iterate on the prompt

42:46

42 минуты 46 секунд

that the text input that you give to the model study the response and keep going till the response looks like what you want it to be to understand that you

42:55

42 минуты 55 секунд

need to understand how it works so let's take a look at how the model Works chat completion is this very basic thing

43:02

43 минуты 2 секунды

where you go to the model that's you and the pink prompt you give it your text input and it gives you content done

43:10

43 минуты 10 секунд

right but wait what's prompt engineering it turns out that there are a lot of little things you can tweak that will

43:18

43 минуты 18 секунд

help the model tune the response that it provides you so for instance you could have prompt templates that the user's input is put into that provide

43:27

43 минуты 27 секунд

additional context you can look at the conversation history you can do things like retrieval augmented generation and grounded in data there are system

43:35

43 минуты 35 секунд

context there are model parameters so with prompt engineering we're really looking at how do we kind of like adjust all these variables so that you get the

43:44

43 минуты 44 секунды

best response you can for the prompt but before we get started and dive into the details let's talk about your choices now if you've been

43:52

43 минуты 52 секунды

following the course there's a getting started folder that will tell you how to set yourself up with one of these providers you can go with open AI or

44:00

44 минуты

hugging face or you can set up on Azure Ai and use both models in there with Azure open AI or Azure AI

44:09

44 минуты 9 секунд

studio today for the most part we're going to use open AI because that's something that's really accessible to you but you can check out the repo for

44:16

44 минуты 16 секунд

notebooks to use the others once you picked your model again you have two choices for trying out exercises on your own you can go with a

44:25

44 минуты 25 секунд

no code option where you don't need to know any code at all you just go to the sandbox that they provide or you can use the notebooks that we've given you that

44:33

44 минуты 33 секунды

are set up with your credentials and then you can do interactively programming exercises to learn prompt engineering today we're going to pick the no code

44:41

44 минуты 41 секунда

option so now let's dive in are you ready the first thing we need to understand is why prompt engineering what's the motivation number one

44:50

44 минуты 50 секунд

motivation is models are stochastic what that means is if you ask the model if you go to it and give it a text input there's no guarantee it's going to give

44:58

44 минуты 58 секунд

you the same response every time there's no guarantee that the response is going to be correct there's no guarantee that the response is what you thought it would be let's take a look at what that

45:07

45 минут 7 секунд

means so what we're going to do is we're going to try out some of these exercises first I have some of these provider set

45:15

45 минут 15 секунд

up so here is hugging face we're actually going to use hugging chat which is their open- Source chat implementation which has a model built

45:22

45 минут 22 секунды

in and right now we're using Microsoft 53 I also have it set up with uh open AI their play playground and on the other

45:30

45 минут 30 секунд

hand I have Azure open AI as well so we're going to start by giving all of them the exact same prompt let's see

45:37

45 минут 37 секунд

what happens so I'm going to go in here and ask let's start with hugging face and say hey tell me about the element

45:44

45 минут 44 секунды

gallium and you'll see that it's giving you a proper response tells you it's a chemical element but look at what it's giving you it's like a multi- paragraph

45:52

45 минут 52 секунды

response right so you go to this provider this model you get this response what happens if I tried an open

46:00

46 минут

AI here I'm using gp35 turbo and you'll see that it's given me a response and shorter and it seems different and it

46:08

46 минут 8 секунд

keeps going wow okay but they were not identical correct let's try this with Azure open

46:15

46 минут 15 секунд

Ai and by now you know where we're going so I'm going to say tell me about the element gallium and remember that Azure

46:24

46 минут 24 секунды

open AI is using open under the covers you'd assume that it would look similar to the other one but it's not exactly

46:31

46 минут 31 секунда

and this is what we mean by stochastic that the same request going to different providers different models is going to generate different responses but wait

46:40

46 минут 40 секунд

you might tell yourself H okay providers are different but if I stick to the one provider and just do everything with them that's not an issue right okay

46:49

46 минут 49 секунд

let's try it out and see so I'm going to say tell me about the element Gallum and first let's look at the

46:56

46 минут 56 секунд

response with GPD 35 turbo and you can see that it's giving me a response which has three to four paragraphs now I'm going to cancel this

47:05

47 минут 5 секунд

response switch this to use gp4 turbo same provider right should look

47:12

47 минут 12 секунд

similar um not exactly right you can see that the text is different it's doing something different you can see that it's actually giving you stuff in

47:21

47 минут 21 секунда

markdown I didn't say what I should do but you can see the response is different same provider but wait it gets

47:28

47 минут 28 секунд

better let's try something different we're going to go back to gp35 Turbo but now I'm going to basically say tell me about the element gallium and let's just

47:36

47 минут 36 секунд

keep it short so you can see the difference in one sentence right now the reason I want to do this I want to show you something really

47:43

47 минут 43 секунды

interesting this sounds nice I've already engineed my prompt to give it a shorter response but if I submit this again you think it should give me the

47:52

47 минут 52 секунды

same response same model same request I haven't changed anything but look it's different this is stochastic this means that if I

48:00

48 минут

were to try to use the responses from this model for my actual application I have no guarantee I'm going to get the same thing multiple times but want to

48:07

48 минут 7 секунд

see something fun it gets worse see this thing called temperature if I change this and say hey get more creative the M

48:15

48 минут 15 секунд

the bigger I make it now when I tell her the same thing it gives me something completely different

48:23

48 минут 23 секунды

it tells me everyday Electronics to Medical Imaging I don't even know if it's true but it tells me something different so you can see that by changing the parameters changing the

48:32

48 минут 32 секунды

model changing the text we can actually get different responses and that is challenge number one all right let's look at what else we

48:40

48 минут 40 секунд

can do we've tried all these oh yes system Persona I forgot that one that's a fun one so here by default the system Persona says you're a helpful assistant

48:49

48 минут 49 секунд

so let's say tell me about Gallum and we already seen this but now we'll make it fun we'll tell the system your persona

48:58

48 минут 58 секунд

is you are a cheerful or you're a creative assistant that

49:05

49 минут 5 секунд

only speaks in limeric all right let's see what

49:14

49 минут 14 секунд

happens it gives you liic so now you see how you can change the quality of the response by trying to tune all these

49:21

49 минут 21 секунда

parameters that's your first kind of like step into understanding the power of prompt engineering but it also exposed to you the challenge

49:29

49 минут 29 секунд

of stochastic responses there's no determinism you don't know what's happening but there's a second challenge

49:36

49 минут 36 секунд

remember we talked about fabrication models can fabricate responses and because of how they work you may not even know that what they're saying is

49:44

49 минут 44 секунды

not grounded in truth because remember a model doesn't really understand doesn't know the meaning of what you're asking it it's just predicting tokens it's

49:52

49 минут 52 секунды

predicting the next word based on its Global Knowledge so it look realistic but may not be true let's try it out and

49:59

49 минут 59 секунд

see so what we're going to do is we're going to look at two different models in open AI we're going to look at GPD 35 turbo its cut off date was September

50:08

50 минут 8 секунд

2021 so it only knows about things prior to that date gp4 turbo has a September 2023 cut off date but it's also one of

50:16

50 минут 16 секунд

the more newer models so it kind of has already been given a little extra sauce to make sure you know it doesn't fabricate as much so we're going to go

50:25

50 минут 25 секунд

to these models and ask them who won the 2025 Oscar for best picture and yes 2025 has not happened yet so let's try it out

50:33

50 минут 33 секунды

and see what happens so we're going to go in here and we're going to first start by saying and let's start with GPD 35

50:42

50 минут 42 секунды

turbo and I'm just going to copy this in there oh and let's set reset this because I want this to go back to being

50:49

50 минут 49 секунд

just the default assisted so now I'm saying who won this and it's GPD 35 turbo and it doesn't tell you that it

50:58

50 минут 58 секунд

doesn't know it's not fabric it just says I can't tell you real time information which itself is weird because you know 2025 is not real time

51:05

51 минута 5 секунд

but hey that's okay let's see what happens when I go to gp4 Turbo which is a newer model I give it the same thing

51:12

51 минута 12 секунд

but what this is doing is telling you hey I don't have information because you're giving me a date that doesn't exist so this is actually a little bit

51:20

51 минута 20 секунд

smarter but now let's go back and try something interesting remember that GPD 35 Turbo told me that you know hey I

51:28

51 минута 28 секунд

can't tell you because it's real time information let's try changing it just slightly right we're going to change

51:35

51 минута 35 секунд

we're asking the same question but we're going to change it slightly and instead of saying who won it say tell me the premise for the movie

51:44

51 минута 44 секунды

that won the Oscar we're saying it won tell me what it was let's see what happens do you see what's happening it

51:52

51 минута 52 секунды

made up a movie and it even told me what it did this is fabrication there's no way this movie exists because 2025

51:59

51 минута 59 секунд

hasn't happened yet but it did it this is fabrication now let's see what happens if we ask gp45 turbo which is

52:07

52 минуты 7 секунд

the newer model right or gp4 Turbo this one is smarter it's going to come and say I can't deal with 2025 it

52:16

52 минуты 16 секунд

hasn't happened yet right so this is a fair and just kind of like you know make sure we are not doing the wrong thing we

52:23

52 минуты 23 секунды

can try to have it tell us about the 2015 B Oscar which you know did happen and sure enough it gives you the right

52:31

52 минуты 31 секунда

response both of them will do so here I can go ahead and through this with GPD 35 turbo and this will get it right as

52:38

52 минуты 38 секунд

well so what did we learn we've learned that the prompt engineering model has an issue with stochastic responses and with

52:47

52 минуты 47 секунд

fabrication and prompt engineering is what we need to do to improve the quality of that response so now let's

52:55

52 минуты 55 секунд

dive into how we can do that so over here we're going to look at the first and more the the kind of like

53:03

53 минуты 3 секунды

the high level principle which is start by giving your model clear instructions we're going to go through a bunch of uh

53:11

53 минуты 11 секунд

demos here back toback first we'll start out the basic prompt just let it complete it then we'll iterate on it with conversation then we'll instruct it

53:19

53 минуты 19 секунд

we'll kind of make it clearer by giving it Specific Instructions it should do refine it for specificities of the fast

53:26

53 минуты 26 секунд

the format the length then we'll try doing something called primary content to see if we can stop the fabrication or ground it in real data look at cues and

53:35

53 минуты 35 секунд

finally look at something interesting called um fusar prompting or providing examples let's get

53:43

53 минуты 43 секунды

started so here I'm going to go back to the Azure open AI I'm sorry the open AI model we'll stick with gp35 turbo

53:52

53 минуты 52 секунды

everything reset back to uh like the default assistant message we start start with our basic prompt so I'm just going to go in and I want to just show you

53:59

53 минуты 59 секунд

what prompt completion looks like so what I'm going to say is I'm literally and this is how you know that it really doesn't understand context I'm just

54:08

54 минуты 8 секунд

giving it O say can you see let's see what it does it comes back to you with by the dawn's early light it's literally just completing it so this is a basic

54:16

54 минуты 16 секунд

prompt that does completion right no context I didn't give it a task it just predicted the next things and lo and behold anything starts with that is

54:24

54 минуты 24 секунды

likely to be the national anthem now let's try a complex prompt so what I'm going to do is I'm going to change

54:31

54 минуты 31 секунда

this now and say okay let let's go back to our gallium and I want to say hey what is

54:39

54 минуты 39 секунд

gallium and it comes back to me and tells me hey this is this element in the periodic table but now I can get into a

54:47

54 минуты 47 секунд

conversation right so I can actually say and this is where it gets interesting I can say what follows it I didn't give

54:56

54 минуты 56 секунд

the name I just said what follows it and it automatically connects the context to what I asked before so this is one of the first techniques in prompt

55:03

55 минут 3 секунды

engineering that we can refine the response by getting into a conversation where we interactively trying to get it to improve on the response from

55:12

55 минут 12 секунд

before but wait now we want to talk about using instruction we were just looking at basic prompts and how you can do complex multi conversation I mean

55:20

55 минут 20 секунд

multi-term conversations now let's get serious so I let's assume that I a middle school teacher and I have to do a

55:28

55 минут 28 секунд

lesson plan for my kids on the Civil War so I go over here and I say hey I need to kind of have something I can put on a

55:36

55 минут 36 секунд

slide that helps them understand the Civil War so I go over there and I say hey write me a short essay on the Civil

55:44

55 минут 44 секунды

War and you can see it's writing me this really long essay and this is great I don't know how much of it is true but that's a lot I

55:53

55 минут 53 секунды

don't know I mean like I couldn't read this in class so I'm like you know I actually need to get more specific so first thing for prompt engineering when

56:01

56 минут 1 секунда

you want a better response is you try to make it more specific so what we're going to go in here and we're going to basically let me get rid of this

56:12

56 минут 12 секунд

one and I'm also going to change the maximum length to something smaller so we're not being overwhelmed and what we're going to do is we say write a

56:20

56 минут 20 секунд

short essay on the Civil War but I'm going to give you more instructions provide key dates for the event tell me the

56:28

56 минут 28 секунд

significance identify key figures and their contributions because this is what I want to teach my students right and if

56:36

56 минут 36 секунд

you try this now you can see that it is actually beginning to answer according to the things that I asked right so it's telling me the events it's telling me

56:44

56 минут 44 секунды

the issues and uh and by the way if I continue this on key figures and that's because i' set this minimum length to

56:52

56 минут 52 секунды

192 so the First Response came back with that many um characters and then I had to hit it again for it to continue on

56:59

56 минут 59 секунд

right but you can see it's answered my questions but this is still a little too much right I want to kind of make it a

57:06

57 минут 6 секунд

little bit better because this is not my students are not going to read all this stuff so what can I do let's try to

57:13

57 минут 13 секунд

improve it by now defining the length and format so I'm going to take the same thing and we're going to try to improve the prompt and this is literally what

57:21

57 минут 21 секунда

prompt engineering is you keep iterating now I'm saying provide a list of dates Etc but now give it to me in markdown and two paragraphs that's all I want two

57:30

57 минут 30 секунд

paragraphs and give it to me in markdown notice how it's formatting it for me markdown it's giving me two sections it's giving me a bulleted list with the

57:38

57 минут 38 секунд

dates I cannot copy this into a web page or into a slide and it's clear concise and better much better

57:46

57 минут 46 секунд

right but now let's talk about remember we said fabrication how can I potentially try to reduce the amount of fabrication this

57:54

57 минут 54 секунды

could have so to try this out first I'm going to uh take a question from the Civil War and I'm going to say

58:02

58 минут 2 секунды

okay let's ask this question who fired on S Fort Sumpter and it gives me this

58:09

58 минут 9 секунд

information and I don't know if this is right or wrong but more importantly let's say I asked my students to read a

58:17

58 минут 17 секунд

particular paragraph and come back to me with a relevant response I can't check if this is what's in there now we're going to talk about this thing called

58:26

58 минут 26 секунд

primary content where now you can actually provide an instruction where you give it the grounding context so I

58:33

58 минут 33 секунды

can actually put down and this paragraph is actually from Wikipedia so I can put down this the the the content the

58:41

58 минут 41 секунда

primary content that is relevant to this particular question and then I asked the question I'm like okay who fired on

58:48

58 минут 48 секунд

sport Suter and if you look into this the answer is actually in this right so Confederate troops fired on forth Suter

58:56

58 минут 56 секунд

and if I hit an enter it tells me exactly what's in there and the interesting thing is if I hit enter

59:03

59 минут 3 секунды

again and again you'll notice that the response remains consistent it's no longer as stochastic as it used to be because now I've literally given it the

59:13

59 минут 13 секунд

context the primary content on which that question should be asked much better right what else can we do well let's say

59:22

59 минут 22 секунды

for example uh this particular teacher not only wants to get the answer answer but wants to get the answer to be

59:28

59 минут 28 секунд

phrased in a certain way this is where you can use something called cues so what happens with cues is if you ask a

59:36

59 минут 36 секунд

question or you tell it to give it an instruction you can kind of it's like a cold start you can nudge it in the direction you want it to go so let's try

59:45

59 минут 45 секунд

this out I'm going to start with a simple instruction tell me about five popular fruits and it comes back to me with a

59:53

59 минут 53 секунды

whole bunch of information right and I'm like that's not what I wanted I wanted it to tell me something and I want it to

1:00:01

1 час 1 секунда

be in alphabetical order so what I'm going to do is I'm going to do this and say okay tell me about this and then I'm

1:00:08

1 час 8 секунд

going to hit this and I'm going to cue it up I'm going to queue up the response when I say tell me about five popular fruits and then say the five popular

1:00:15

1 час 15 секунд

fruits in Reverse alphabetical order are and if I did this right it gives me the same fruits and they're in Reverse

1:00:22

1 час 22 секунды

alphabetical order I I kind of seeded it I nudged it in the direction I wanted it to go but wait it gets better I'm

1:00:30

1 час 30 секунд

looking at this going hm it's this is not what I want I want my I want those kids to remember it so I want to kind of

1:00:39

1 час 39 секунд

give it some examples of how I want this to how how I want the response to be done right and so we can do this and

1:00:47

1 час 47 секунд

this is called first we're going to talk about zero shot prompting and few short prompting so here I'm basically going to start with zero short prompting where I'm saying I don't I haven't told you

1:00:56

1 час 56 секунд

anything I'm just giving you an example and I'm going to see what it does and you'll see that it continues on and tries to describe this fruit so he

1:01:04

1 час 1 минута 4 секунды

didn't learn it he's just like continuing on and I get a decent response but it's not what I wanted what

1:01:12

1 час 1 минута 12 секунд

if I went in and instead said hey what I really want is for you to talk about fruit but I want you to make it into this kind of like this hey these are

1:01:21

1 час 1 минута 21 секунда

maybe um middle no Elementary uh school kids so so I'm Like A is for apple of fruit that's sweet now let's see what

1:01:29

1 час 1 минута 29 секунд

happens when I hit an enter here do you see it Not only was able to look at the pattern and see hey there

1:01:37

1 час 1 минута 37 секунд

are two at a time but it figured out that they were alphabetical I didn't tell it it figured it out that they're alphabetical and this is the most

1:01:46

1 час 1 минута 46 секунд

interesting it figured out that they rhymed sweet and treat red and spread indeed in fre you see that so this is

1:01:53

1 час 1 минута 53 секунды

where you can effectively tell it examples of what you want to see and it tries to learn from them not learn from

1:02:00

1 час 2 минуты

them sees the pattern if you will and tries to use that pattern to give you a better response so all of these are techniques you can use for prompt

1:02:08

1 час 2 минуты 8 секунд

engineering and with that let's kind of get back to our slides and wrap up what we were talking about we talked about clear instructions you want to try this

1:02:17

1 час 2 минуты 17 секунд

out go try out the assignment that's in the lesson and you can do that with a code first approach by putting in your credentials once you've got that what

1:02:26

1 час 2 минуты 26 секунд

can you do next as you notice the best way for prompt engineering you have to iterate iterate iterate so you can do things like change the Persona change

1:02:35

1 час 2 минуты 35 секунд

the parameters add examples understand limitations and when you're done when you've got it to the point where it

1:02:41

1 час 2 минуты 41 секунда

looks good create a template so that next time you don't need to go through the excise again you know exactly the prompt that you need to ask put it in

1:02:50

1 час 2 минуты 50 секунд

there and share it with all the other teachers so they can use it too and this is exactly what we do when we think about prompt template Library so I encourage you to go look at this site as

1:02:58

1 час 2 минуты 58 секунд

an example of how you would build a prompt template library for your application this is prompts for edu but you might be telling yourself well I'm

1:03:05

1 час 3 минуты 5 секунд

not education I want to know what how to write prompts for something else for retail for gaming I don't know this is where I encourage you to go look at the

1:03:14

1 час 3 минуты 14 секунд

provider sites openai has a prompt examples collection so you can go look at what a good prompt looks like how to set system context parameters Etc

1:03:23

1 час 3 минуты 23 секунды

hugging chat will let you pick any model and then literally give it an example that you can see how it works on it and Azure AI has a prompt catalog so you've

1:03:32

1 час 3 минуты 32 секунды

got a good place to start from and with that we come to the end of Lesson Four so to recap if you are interested in

1:03:41

1 час 3 минуты 41 секунда

what we were doing today we learned Core Concepts we understood the challenges of uh generative AI today in terms of prompt usage we figured out what are the

1:03:50

1 час 3 минуты 50 секунд

different techniques for prompt engineering and we looked at ways in which you can go and build your intuition by using templates and examples from other

1:03:58

1 час 3 минуты 58 секунд

providers we can't wait to see what generative a applications you build see you in the next

Эпизод 5: Creating Advanced Prompts [Pt 5]

1:04:11

1 час 4 минуты 11 секунд

lesson hey folks my name is Chris noring I work as a senior Cloud Advocate at Microsoft in today's lesson lesson five

1:04:19

1 час 4 минуты 19 секунд

we'll talk about how to create Advanced proms uh you can definitely check out this link here at the bottom AK Ms gen

1:04:27

1 час 4 минуты 27 секунд

AI beginners where you will be able to find all the different lessons that will skill you up from beginner to

1:04:33

1 час 4 минуты 33 секунды

expert now as we move in let's check out this lesson right uh you can see that this is part of a GitHub repo there's a

1:04:42

1 час 4 минуты 42 секунды

ton of different lessons here so we definitely recommend that you check out all of these lessons to make sure that you scale up properly the goals of this

1:04:50

1 час 4 минуты 50 секунд

lesson is to learn how to apply prompt engineering techniques that improve the outcome of your prompts and hopefully by

1:04:58

1 час 4 минуты 58 секунд

now you saw the previous video where we introduced the concepts of prompts and prompt engineering and this takes it to

1:05:05

1 час 5 минут 5 секунд

a different level where we explain that there is actually a method and an engineering principle behind getting a better result because that that's really

1:05:13

1 час 5 минут 13 секунд

what we're trying to achieve so for example if we look at a very basic prompt you see that it says how to

1:05:21

1 час 5 минут 21 секунда

generate 10 questions on geography that's all well and fine but there are some includes in here that makes this a good prompt because we are providing

1:05:29

1 час 5 минут 29 секунд

context by saying geography we're also limiting the output by saying no more than 10 questions not 20 questions not

1:05:37

1 час 5 минут 37 секунд

30 questions not 50 questions but 10 and this is an important principle when it comes to be better at prompting which is

1:05:45

1 час 5 минут 45 секунд

what you're about to do uh one also one other thing when it comes to a topic when you go into a

1:05:52

1 час 5 минут 52 секунды

topic just imagine that it could be a very big topic so the more you can drill down into specifics the better so for example if you're interested in Paris

1:06:01

1 час 6 минут 1 секунда

and London you should say that instead of UK or France or what have you so always think about providing just the

1:06:08

1 час 6 минут 8 секунд

right level of context to ensure that that output is what you need and the format is also something that we can

1:06:15

1 час 6 минут 15 секунд

work on so far you saw how we said 10 questions but you can also decide how you want that output to come to you like

1:06:23

1 час 6 минут 23 секунды

for example with a title a description or maybe some other keywords so these are just some good grounding some basic tips on how to be a

1:06:32

1 час 6 минут 32 секунды

better prompter but there are also some various techniques that we're here to learn today and this is something that you can take with and run and it doesn't

1:06:41

1 час 6 минут 41 секунда

really matter whether you're using Asher open AI or chap GPT or some other AI systems these are techniques and

1:06:48

1 час 6 минут 48 секунд

Technologies approaches that you can use anywhere so what you've seen so far is a principle here called zero shot prompt

1:06:56

1 час 6 минут 56 секунд

this is your most basic form of prompting where you construct a prompt you're sending that to your AI assistant

1:07:03

1 час 7 минут 3 секунды

and you hope for the best now one other principles that you could be using also is something called Chain of Thought and

1:07:11

1 час 7 минут 11 секунд

what we want to say about this principle is that imagine this imagine that you are a student and you are a teacher right so the student would guide you

1:07:19

1 час 7 минут 19 секунд

through Problem by saying Chris to actually solve this problem you need to take a few steps first you need to do a

1:07:26

1 час 7 минут 26 секунд

then B and then C and then you try to mimic what the teacher does and little by little you're able to take on more and advanced problems and kind of

1:07:35

1 час 7 минут 35 секунд

conquer those that's the idea of Chain of Thought but now imagine instead of a student and a teacher it's you who are

1:07:42

1 час 7 минут 42 секунды

the teacher and the student is really the llm or your AI assistant so you are guiding it step by step on how to

1:07:49

1 час 7 минут 49 секунд

actually present the solution to a problem we'll quickly show a example of that one there's also something called generated

1:07:58

1 час 7 минут 58 секунд

knowledge and the idea is to improve the response of a prompt and you can provide a generated facts or add additional

1:08:07

1 час 8 минут 7 секунд

knowledge that then the AI assistant can utilize to present you with a bad response and if it didn't have those

1:08:14

1 час 8 минут 14 секунд

facts and then there's a principle called least to most it's very similar to Chain of Thought but this is about breaking down the problem into series of

1:08:22

1 час 8 минут 22 секунды

steps and we see how this could be really useful in for example data science where it's often known which steps that's going to happen in what

1:08:30

1 час 8 минут 30 секунд

order for example fetching data cleaning data and doing some other projections maybe and then you end up training maybe

1:08:37

1 час 8 минут 37 секунд

a machine learning model and there's also a couple of techniques here that I I thought it to mention at the very end of things which is selfrefined and

1:08:46

1 час 8 минут 46 секунд

myotic prompting now the idea with selfrefined is that you are actually critiquing the llm your AI system and

1:08:53

1 час 8 минут 53 секунды

said are you sure about these facts and what you're saying to it is not only that you're questioning the very output

1:09:00

1 час 9 минут

but you're also saying how can you improve this response just to give it a few different iteration of saying are you're really sure about this response

1:09:09

1 час 9 минут 9 секунд

how about you try and go for another round myotic prompting is interesting because what you want just like with self- refine is that you want to make

1:09:17

1 час 9 минут 17 секунд

sure that the outcome is correct so what you do is that you break down the answer who which might consist of let's say

1:09:24

1 час 9 минут 24 секунды

five or six different parts and for each and every part you are trying to ass certain whether that response from the AI assistant is actually correct by

1:09:33

1 час 9 минут 33 секунды

getting it to countermand Itself by giving you a different response so definitely look at selfrefined and

1:09:40

1 час 9 минут 40 секунд

myotic prompting if you're interested in validating your response and also something so why are we doing this in

1:09:48

1 час 9 минут 48 секунд

the first place why do we need techniques to actually ensure that the output of our AI system is correct well the truth is it doesn't know everything

1:09:57

1 час 9 минут 57 секунд

right and just like us humans we make up responses when we don't have it especially if we're kids right but it's the same thing with an AI if it doesn't

1:10:05

1 час 10 минут 5 секунд

have the correct answer it's trying to give you its best guess what it should be and this is a way for you to tell the llm are you really sure about this

1:10:14

1 час 10 минут 14 секунд

response you didn't make it up this is also known as hallucinating when it comes to llms but uh yeah now that I

1:10:21

1 час 10 минут 21 секунда

described these various principles let's look at Chain of Thought cuz I find that this one is super interesting so imagine now that you have this simple problem

1:10:30

1 час 10 минут 30 секунд

where you say Alice has five apples she throws away three apples she gives two apples to Bob and Bob's give one back

1:10:38

1 час 10 минут 38 секунд

how many apples does Alice have now it answers us with five and this is problematic right because five is

1:10:46

1 час 10 минут 46 секунд

incorrect if you actually do the math for this you see that you should calculate it as 5 - 3 - 2 + 1 which is 1

1:10:54

1 час 10 минут 54 секунды

and it's answering us with five so how can we actually come up with a better response well and this is where the

1:11:02

1 час 11 минут 2 секунды

whole Chain of Thought comes in and this is really the teacher and the student idea so the idea what you're doing is to show the llm you show your AI assistant

1:11:11

1 час 11 минут 11 секунд

here's a similar problem here's how I break it down and then hopefully you end up with a more accurate response so what

1:11:19

1 час 11 минут 19 секунд

you can do is give it a similar example where you say that Lisa has seven apples she throws away one Apple she gives four

1:11:27

1 час 11 минут 27 секунд

apples to Bart and Bart gives one back and then you show the calculation being

1:11:32

1 час 11 минут 32 секунды

7 - 1 is 6 6 - 4 is 2 2 + 1 = 3 now this is super interesting right because now

1:11:40

1 час 11 минут 40 секунд

you've shown a similar examples but you've also show the calculation and then you add the original question being

1:11:47

1 час 11 минут 47 секунд

Alice has five apples she throws away three apples gives two apples to Bob Bob gives one back and so on and so forth

1:11:54

1 час 11 минут 54 секунды

and lo and behold now the llm will actually answer you with a correct response which is

1:12:00

1 час 12 минут

one so just to rehash what we did here we provided it with a similar examples we provided it with a calculation for

1:12:10

1 час 12 минут 10 секунд

how to uh calculate this very similar uh answer and then we readded our original question and all of this is called Chain

1:12:19

1 час 12 минут 19 секунд

of Thought because we teach it how to do things in a chain so we we're showing the entire calculation the the entire

1:12:26

1 час 12 минут 26 секунд

Chain of Thought from start to finish and our llm our AI uh assistant is now

1:12:33

1 час 12 минут 33 секунды

able to answer us better now looking at generated knowledge this principle is also super interesting because this

1:12:41

1 час 12 минут 41 секунда

allows you to provide information uh to your question as you need it so what we're looking at here is a template we

1:12:49

1 час 12 минут 49 секунд

see that this is a template because it's using these curly brackets where with company and company name and products and products list this is information

1:12:57

1 час 12 минут 57 секунд

that doesn't exist yet and for this question to be able to be posed towards the AI system we need to fetch this information from somewhere and once we

1:13:06

1 час 13 минут 6 секунд

fetch this information once we include it into our prompt then we will be able to get a better response from the llm

1:13:14

1 час 13 минут 14 секунд

and this is often times used in in a principle called rag or retrieval augmented generation the idea is that

1:13:21

1 час 13 минут 21 секунда

you fetch existing data that you own as part of your company you insert that as part of your template then you ask the

1:13:28

1 час 13 минут 28 секунд

question to the AI assistant and then you arrive at hopefully a better response than if you had just tried to

1:13:34

1 час 13 минут 34 секунды

ask the llm the question right away so imagine now if if we go just to show an

1:13:41

1 час 13 минут 41 секунда

example of this if we just ask it please suggest an insurance like this so we go to our

1:13:50

1 час 13 минут 50 секунд

playground that we can have and you definitely have the same kind of playground so what we can do here inside of this playground is we can paste this

1:13:57

1 час 13 минут 57 секунд

and this is not fetching any business data it's only fetching the actual question so at this point we're saying please suggest an insurance giving the

1:14:06

1 час 14 минут 6 секунд

following budget and requirements my budget is $1,000 and it should be about car and home or even better let's remove

1:14:13

1 час 14 минут 13 секунд

this part and then what we want to do is to scroll down all the way to the bottom see if we can do

1:14:21

1 час 14 минут 21 секунда

that so now we can come to a point where we hit generate button but now we're going to get a response where we just

1:14:28

1 час 14 минут 28 секунд

hope that the llm is actually trained on insurance products and we get a very generic response so we're not really happy about this response because it

1:14:36

1 час 14 минут 36 секунд

says well for $1,000 there's multiple insurances but this is not really what you want right because most likely you own an insurance

1:14:45

1 час 14 минут 45 секунд

company and you want that insurance products to actually be something that you tell the user about so if the user come to your site they ask about the

1:14:54

1 час 14 минут 54 секунды

best insurance you actually need to fill stuff out so instead of just asking this question provide that extra context and now we

1:15:03

1 час 15 минут 3 секунды

pretend that this extra context has been fetched from somewhere before the users's request is actually coming through and this is what we call a rag

1:15:11

1 час 15 минут 11 секунд

so imagine now that we fetch this information thanks to doing some web API call with Acme Insurance we're showing

1:15:18

1 час 15 минут 18 секунд

it all the different insurances and now we still ask the same question we have a budget of,

1:15:25

1 час 15 минут 25 секунд

and at this point we want to go back and we want to hit generate and this time we're hoping for a better answer because

1:15:32

1 час 15 минут 32 секунды

we provided it with more context so now we can see because we added this generated data we ask our question of

1:15:42

1 час 15 минут 42 секунды

$1,000 now it's saying to us here's a much better response you should be using the cheap insurance of $500 US that's

1:15:50

1 час 15 минут 50 секунд

within your budget or you can use the other one for $600 and so on all of this is based on this improved context but of

1:15:58

1 час 15 минут 58 секунд

course the devil's in the detail here right how do we actually fetch this data this is where rag Solutions come in and you need to build the system around it

1:16:07

1 час 16 минут 7 секунд

but the good news here is that we have many samples on Asher how to do this for python for JavaScript for java.net and

1:16:14

1 час 16 минут 14 секунд

so on so don't worry we got your back even here yes we went through this example and you can see how much better

1:16:21

1 час 16 минут 21 секунда

the prompt was when you were able to in run time provide that extra context while asking this question and just to

1:16:29

1 час 16 минут 29 секунд

show you also about least to most that this is a principle of how you're able to present it with a breakdown of a

1:16:37

1 час 16 минут 37 секунд

problem so as I said before let's for example use this within data science and we can actually start with a prompt in

1:16:44

1 час 16 минут 44 секунды

which we say well how would I do data science in five steps or how would I make this chocolate cake in five steps

1:16:52

1 час 16 минут 52 секунды

by having this initial prompt we are actually able to use the llm and we get some kind of recipe for how to solve our

1:17:00

1 час 17 минут

problem so here we're saying collect data clean data analyze data plot data and present data that's excellent right

1:17:08

1 час 17 минут 8 секунд

because once we have that breakdown uh we can actually use each of these steps and go back here and

1:17:17

1 час 17 минут 17 секунд

say how would I do collect data in data science so now we're utilizing the fact

1:17:25

1 час 17 минут 25 секунд

that we've already asked that initial prompts how we do data science in five steps now we're using the information and knowing what one of these steps are

1:17:33

1 час 17 минут 33 секунды

called and we can just make that information important with a quote and now we hit generate and now it's able to

1:17:41

1 час 17 минут 41 секунда

give us a better answer about how to do data science because we mention a specific step and if we want to be even better

1:17:49

1 час 17 минут 49 секунд

with this response show me python code and and this is just utilizing all of those great principles when it comes to

1:17:58

1 час 17 минут 58 секунд

prompting in general that we if we add more context on how to do something we are more likely to get the response we need and and by me adding show me python

1:18:07

1 час 18 минут 7 секунд

code and collect data in combination you see that I now get some kind of answer that makes sense so now it says how to

1:18:15

1 час 18 минут 15 секунд

read data from a CSP file and it's showing me how to do Header information on the data it's showing me how to select various features from that data

1:18:24

1 час 18 минут 24 секунды

set and so on so you can see context matters and the more specific you are and and I think you all saw this when I didn't say show

1:18:32

1 час 18 минут 32 секунды

me python code it just gave me some text it didn't really show me what I needed which was the python

1:18:39

1 час 18 минут 39 секунд

code and uh yeah as I mentioned before self- refine this is a very important process when it comes to critiquing your

1:18:46

1 час 18 минут 46 секунд

your results to say are you sure about this outcome and and here you can see an example of this technology where we're

1:18:54

1 час 18 минут 54 секунды

saying um we first start off with a prompt where we say create the python web API with routes products and customer that's

1:19:02

1 час 19 минут 2 секунды

a great start right but what you want to do as part of the self- refine is to say suggest three improvements of the above

1:19:09

1 час 19 минут 9 секунд

code so here we're saying we're not really happy with your first attempt but we want to iterate on the results and now we can say three improvements or

1:19:17

1 час 19 минут 17 секунд

five improvements or just any improvements and we arrive at a better response so we can keep self-critique an

1:19:25

1 час 19 минут 25 секунд

and number of times until we're happy with the end results and myotic prompting is also an interesting one is

1:19:32

1 час 19 минут 32 секунды

that we can ask the llm to answer a question and for each part of the answer we can ask it to explain the answer just to make sure that what we're getting

1:19:41

1 час 19 минут 41 секунда

back seems consistent if we notice any kind of signs of inconsistency that's probably uh something that we can

1:19:48

1 час 19 минут 48 секунд

discard because then the llm is just making stuff up and we can see here for example of how can create a crisis plan

1:19:55

1 час 19 минут 55 секунд

to mitigate a pandemic in five steps great we get five steps back and for each step can you explain

1:20:02

1 час 20 минут 2 секунды

more in detail how I can deal with each of these but if we come to a point now where it starts to explain one of these

1:20:10

1 час 20 минут 10 секунд

steps and it doesn't seem like what it's explaining back makes a lot of sense as I said before is probably something that

1:20:17

1 час 20 минут 17 секунд

we can discard hopefully you'll be able to feel like you're skilled up in your prompting you've leveled up you now feel like you have different options Chain of

1:20:26

1 час 20 минут 26 секунд

Thought was a fantastic pattern to use if you wanted to lead it in in its reasoning if you feel like it's doing wrong for some reason it really helps to

1:20:34

1 час 20 минут 34 секунды

provide that example to break it down in steps and even showing it the calculation and uh critiquing the result you saw how you could improve that

1:20:42

1 час 20 минут 42 секунды

source code step by step by just asking for do that Improvement or do this Improvement and so on so with these patterns you can see how we can improve

1:20:51

1 час 20 минут 51 секунда

the quality of the output of the out because that's really what we want at the end of the day we want something that's more correct or more to our

1:21:00

1 час 21 минута

liking so huge thank you everyone for watching this

Эпизод 6: Building Text Generation Applications [Pt 6]

1:21:09

1 час 21 минута 9 секунд

video okay hey folks welcome to another video in this series about generative AI my name is Chris noring I'm a senior

1:21:16

1 час 21 минута 16 секунд

Cloud Advocate at Microsoft and in this very exciting lesson you'll learn how to build your own text generation app this

1:21:24

1 час 21 минута 24 секунды

is that's super cool as usual you can go to this bottom link here at the slide akam Ms gen AI beginners that will show

1:21:32

1 час 21 минута 32 секунды

you the entire series of everything you want to know but this lesson is very Hands-On so without further Ado let's go

1:21:40

1 час 21 минута 40 секунд

into Visual Studio code your code editor where you can see how we can craft our own code and build our own AI augmented

1:21:49

1 час 21 минута 49 секунд

app so let's uh start off here where we used to be right we have a open text window there are a couple of things I want you to know about building apps

1:21:57

1 час 21 минута 57 секунд

like this one of them is how to import Asher open AI we're going to need this to instantiate a client but before that

1:22:06

1 час 22 минуты 6 секунд

we need libraries called open AI andv open AI this is the library that

1:22:13

1 час 22 минуты 13 секунд

helps you make it easy to make those calls towards your Asher open AI or open AI resource and get that response back

1:22:22

1 час 22 минуты 22 секунды

from your AI assistant the other bit here is going to help us during development time and it's called

1:22:29

1 час 22 минуты 29 секунд

envv has U the role of loading secrets and other environment variables from an environment file uh the idea is that you

1:22:38

1 час 22 минуты 38 секунд

have some kind of key value setup where you say these are my keys and these are the values that go with it in general

1:22:46

1 час 22 минуты 46 секунд

and this is a very uh strong recommendation don't put anything that's secret within your code separate secrets

1:22:54

1 час 22 минуты 54 секунды

from your code typically by having them as environment variables or you know elsewhere somewhere that's not the code

1:23:01

1 час 23 минуты 1 секунда

because what happens if you check this in someone will be able to use and authenticate and use your resources you don't want that to

1:23:09

1 час 23 минуты 9 секунд

happen so what we're looking at here is how EnV helps us by taking the values within the EnV file load those in as

1:23:18

1 час 23 минуты 18 секунд

environment variables which makes it simple then for us to refer to them as we instantiate our client so here we're

1:23:26

1 час 23 минуты 26 секунд

building our client by calling Asher open AI there are three things it needs to work one of them is an endpoint this

1:23:33

1 час 23 минуты 33 секунды

is something that you can find within Asher portal with your deployed Cloud resource next piece of information that

1:23:40

1 час 23 минуты 40 секунд

it needs is the API key and this is your unique secret that says that you are you

1:23:46

1 час 23 минуты 46 секунд

and then we need to uh specify the right API version this one tends to change over time so definitely check back back

1:23:54

1 час 23 минуты 54 секунды

to our official Microsoft docs uh to make sure that you're using the right version using the right version will

1:24:01

1 час 24 минуты 1 секунда

ensure that you have access to the right features on Asher open AI now deployment is also one of these

1:24:09

1 час 24 минуты 9 секунд

things that's important because you can deploy more than one model on the same Cloud resource so imagine that you want to for example deploy Da Vinci or maybe

1:24:18

1 час 24 минуты 18 секунд

chat gbt 3 and a half turbo you need different models for different things especially if you try to embed code that's a model of its own you try to do

1:24:27

1 час 24 минуты 27 секунд

chat conversation that's another model and so on and so forth so you need to read up a little bit on what kind of deployment that you need but you can

1:24:34

1 час 24 минуты 34 секунды

think of deployment as a what type of model am I using now on line 18 here this is the

1:24:42

1 час 24 минуты 42 секунды

interesting part right this is what you feed into your AI uh application this is the prompt this is the instruction that

1:24:50

1 час 24 минуты 50 секунд

you want some kind of answer to so in this very simple case we're saying complete the following and we're saying

1:24:57

1 час 24 минуты 57 секунд

once upon a time there was a something something this is a fantastic example of how you can build your own story so if you got kids at home or maybe a niece

1:25:06

1 час 25 минут 6 секунд

and a nephew and you want to tell them a great story why not use that AI assistant to be able to do so and here

1:25:13

1 час 25 минут 13 секунд

we establish something called messages and this is how we can establish some kind of Prior conversation so this could

1:25:20

1 час 25 минут 20 секунд

either be you starting out your conversation or this can be a whole list of messages between you as a user or the system so let me just show you quickly

1:25:29

1 час 25 минут 29 секунд

what I mean in case you wanted to establish a really long conversation that's been happening for a while at this point you would just add this and

1:25:37

1 час 25 минут 37 секунд

say that the to the system for example that you are you are a

1:25:46

1 час 25 минут 46 секунд

curator at the Museum so if you change uh like this this would mean that your

1:25:55

1 час 25 минут 55 секунд

AI system suddenly changes behavior that it needs to consider this piece of information before it responds so this could be super interesting if you want

1:26:03

1 час 26 минут 3 секунды

to build an app for example that works for museums or you can either say it's a curator at the Museum or you could even

1:26:10

1 час 26 минут 10 секунд

say that it's a Lincoln and it would actually tell you a story like it was a lincol so lots of different options when

1:26:18

1 час 26 минут 18 секунд

it comes to messages how to customize uh either by saying that there's previous history of messages that happens and you

1:26:26

1 час 26 минут 26 секунд

take you continue your AI application with a conversation that you already had or you use this as an opportunity to

1:26:33

1 час 26 минут 33 секунды

kind of tweak that AI assistant of yours to make sure that you get very interesting responses for now we'll keep this very simple all we want to see at

1:26:42

1 час 26 минут 42 секунды

this point is a simple prompt and a simple message to make sure that that is actioned upon now to make the actual

1:26:49

1 час 26 минут 49 секунд

completion to get that response back from your AI application we are calling in completions create and you see here

1:26:56

1 час 26 минут 56 секунд

how we set the variables model and messages and after that we are trying to print the response coming back as

1:27:03

1 час 27 минут 3 секунды

message. content so without further Ado let's actually try to call this piece of code and make sure that we match the

1:27:12

1 час 27 минут 12 секунд

name here A O

1:27:15

1 час 27 минут 15 секунд

[Music]

1:27:17

1 час 27 минут 17 секунд

AI see nope not that one for now so this is the very simplest form of this so give this a couple of seconds because it

1:27:26

1 час 27 минут 26 секунд

needs to establish that connection with your resource in the cloud and then it sends the prompt and then you hopefully get that response so assume that this

1:27:34

1 час 27 минут 34 секунды

will take a couple of seconds the first time you run this but uh hopefully you'll see how it executes all these lines of code up until line 24 where it

1:27:43

1 час 27 минут 43 секунды

should output things now looking at this if you remember once more what we wrote to it

1:27:51

1 час 27 минут 51 секунда

said complete the following once upon a time there was a something so at this point it would already tell us here's a fairy

1:27:58

1 час 27 минут 58 секунд

tale and you can see here if you scroll up that we got a very long response back where it says so if you read this all

1:28:05

1 час 28 минут 5 секунд

the way through you see that you have a fantastic fairy tale where it says once upon a time there was a beautiful princess named Aurora who lived in a

1:28:14

1 час 28 минут 14 секунд

magnificent castle at the edge of a vast Kingdom now if you want to tweak this fairy tale a little bit once upon a time

1:28:22

1 час 28 минут 22 секунды

there was a uh girl who lived on a spaceship you

1:28:29

1 час 28 минут 29 секунд

will get a very different story but this is the beautiful part right you can take this prompt and tweak it to whatever you want it to do so now when we ask the

1:28:37

1 час 28 минут 37 секунд

very same question again run this app we have tweaked The Prompt with a different instruction so hopefully this time around we get more of a science fiction

1:28:46

1 час 28 минут 46 секунд

type setting now if you scroll back we have our unique story so if you are a parent

1:28:53

1 час 28 минут 53 секунды

if you are an uncle or Aunt you will be able to be that favorite relative who always tells nit new stories so at this

1:29:02

1 час 29 минут 2 секунды

point we have a girl here called Nova that lives on a spaceship since she was born and Nova is fascinated by stars and the possibility of discovering new

1:29:10

1 час 29 минут 10 секунд

planets I'm already hooked I want to hear more about this story and I hope you want too now this is nice right I mean we have a fairy tale story that's

1:29:20

1 час 29 минут 20 секунд

already something that's very useful but if you want to have an everyday kind of application you might want to look at an app like this instead so in a

1:29:29

1 час 29 минут 29 секунд

interactive app you probably have a way to collect information and how we collect information in Python is by using an input construct and at this

1:29:37

1 час 29 минут 37 секунд

point we want to tell the user what we're after so we're saying I want you to name the number of recipes for example five could be one two five and

1:29:46

1 час 29 минут 46 секунд

so on we also want to ask the user for what ingrediences do you have in your fridge or your cupboard so at this point

1:29:54

1 час 29 минут 54 секунды

point we're saying we think you have something like chicken or potatoes or carrots whatever have you in your fridge and then of course we want to make sure

1:30:02

1 час 30 минут 2 секунды

that we are inclusive so we add some kind of filter that if you are allergic to peanut we don't want to show you some

1:30:10

1 час 30 минут 10 секунд

kind of peanut recipe because that would be bad for your health and then after we've inputed all of these ingredientses now we construct The Prompt that has

1:30:19

1 час 30 минут 19 секунд

these templates uh here with the curly brackets so number of recip piece would be interpolated here the ingredients is

1:30:27

1 час 30 минут 27 секунд

in your cupboard would end up here and the filter would make sure that we don't have for example any recipes containing

1:30:34

1 час 30 минут 34 секунды

peanuts and then ultimately we'll do just like the fairy tale application and uh set messages and then we end up

1:30:43

1 час 30 минут 43 секунды

printing the response so there's quite a few different bits here so what we want to do at this point is to clear things up a little bit and see if we can

1:30:51

1 час 30 минут 51 секунда

actually run this app as is so a o i this and this so now that we run this we

1:30:59

1 час 30 минут 59 секунд

expect to be prompted so number of recipes two list of ingredients is well if you know Chris you know that he

1:31:06

1 час 31 минута 6 секунд

always have chocolate at home and he probably has I don't know caviar maybe not the best ingrediences for creating

1:31:13

1 час 31 минута 13 секунд

something but hey it is what it is and filter I'm not allergic to peanut but let's just humor me and say that I am so

1:31:22

1 час 31 минута 22 секунды

at this point we just want wanted to produce a recipe based on this user-driven input so now it's not only producing recipes that I can use but

1:31:31

1 час 31 минута 31 секунда

also shopping this but let me show you the two different recipes that we did get and the first recipe is chocolate

1:31:38

1 час 31 минута 38 секунд

caviar tart now I have to admit to myself I've never tried chocolate and caviar together so I'm not sure it's a winner but this one tells us about

1:31:47

1 час 31 минута 47 секунд

allpurpose flour butter sugar okay heavy cream chocolate chip and caveat

1:31:54

1 час 31 минута 54 секунды

H I'm a bit uh you know I'm I'm not sure but hey let's give it a try the other recipe here is chocolate caviar truffles

1:32:02

1 час 32 минуты 2 секунды

I don't know if that works maybe it does heavy cream caviar cocoa powder but at this point you might be thinking that's way more ingrediences that I might have

1:32:10

1 час 32 минуты 10 секунд

in my cupboard or fridge I mean you know and for that reason there's a shopping list H I'm not sure this app works as it

1:32:18

1 час 32 минуты 18 секунд

should but I think you get the idea here so that if you want this app to actually respect ingredients you have at home you can always tweak The Prompt and

1:32:27

1 час 32 минуты 27 секунд

say so here below here you see that producer shopping list and please don't so I thought I was

1:32:34

1 час 32 минуты 34 секунды

being very courteous here when I say please don't you can actually use very strong language here and say

1:32:43

1 час 32 минуты 43 секунды

and all ingredients is must exist so at this point you can

1:32:50

1 час 32 минуты 50 секунд

be very firm with it and this is part of the prompt engineer ing if you saw those earlier lessons is if that first prompt don't work you can always tweak it and

1:32:59

1 час 32 минуты 59 секунд

hope for a better result um this is how you could be solving those kind of problems but I think you get the idea of how we can build a really rich

1:33:08

1 час 33 минуты 8 секунд

application with various types of input um and you can keep on prompting as you saw because we have one prompt here for

1:33:15

1 час 33 минуты 15 секунд

listing the recipe and another prompt for producing a shopping list so all of these prompts can work in tandem to

1:33:21

1 час 33 минуты 21 секунда

produce a greater outcome and you saw how we took all those simple ideas from that first app of telling a fairy tale

1:33:29

1 час 33 минуты 29 секунд

story to create a more advanced app including user prompts and hopefully now you feel like you have an app that

1:33:36

1 час 33 минуты 36 секунд

actually produces something of Great Value to you but just to see if we actually improve things by changing the

1:33:43

1 час 33 минуты 43 секунды

prompt a little bit let's see if we can run it again hopefully with a better result number of recipes one and let's

1:33:52

1 час 33 минуты 52 секунды

say I got chocolate and ice cream that seems more

1:33:58

1 час 33 минуты 58 секунд

fair right and filter is still peanut let's hope it produces something that makes more sense this time so this time

1:34:07

1 час 34 минуты 7 секунд

around it's giving us what okay chocolate ice cream sunde that sounds pretty good there's definitely no

1:34:15

1 час 34 минуты 15 секунд

caviar in there there's ice cream chocolate sauce whip cream tablespoon of chocolate chips Marino Cherry sounds

1:34:23

1 час 34 минуты 23 секунды

good to me yeah and we seem to have a bug with a shopping list but just given the fact that you have a template to work off of

1:34:31

1 час 34 минуты 31 секунда

already should make it easier for you to get started but let's just rehash all our winnings today everything that we

1:34:38

1 час 34 минуты 38 секунд

learned today you saw two how we built two different apps you saw the simpler app with the fairy tale you saw a more H

1:34:46

1 час 34 минуты 46 секунд

fit for purpose kind of application in which we were able to use a food recipe we use that for chocolate or caviar so

1:34:54

1 час 34 минуты 54 секунды

we have everything from dessert to you know main meal let's just rehash the things that really mattered for you to understand how you can build your own

1:35:02

1 час 35 минут 2 секунды

first application using AI augmented within your application so what was important to know is that keep your

1:35:10

1 час 35 минут 10 секунд

secrets out of your code uh make sure that those Secrets can be read for example from an environment file and make sure that you use a library like NV

1:35:18

1 час 35 минут 18 секунд

to do all that heavy lifting to populate your environment variables so then when you instan up the client that's made

1:35:26

1 час 35 минут 26 секунд

really easy once you had that client up and ready now is the fun part in which you create the prompt the instruction

1:35:34

1 час 35 минут 34 секунды

the input towards your AI app and you can give it those messages so it's either a a new conversation or an

1:35:42

1 час 35 минут 42 секунды

existing conversation and as I showed you in the beginning of the video you can tweak those messages to have the AI assistant be anyone from a Lincoln to

1:35:51

1 час 35 минут 51 секунда

Gordon Ramsey so here you can can see on line 21 also how we created our first completion we sent that towards the AI

1:35:59

1 час 35 минут 59 секунд

we got a message back and thanks to here on line 24 we're able to print that we also saw in the other example how we

1:36:07

1 час 36 минут 7 секунд

could take this and make it really Advanced by adding inputs and multiple prompts to create that really great

1:36:15

1 час 36 минут 15 секунд

experience uh that interactive experience so hopefully now you all feel very excited about building your own AI

1:36:22

1 час 36 минут 22 секунды

apps whether whether that app is a space captain or or a Lincoln or maybe your favorite Chef so good luck with that and

1:36:30

1 час 36 минут 30 секунд

hopefully I'll catch you in another video in this series thanks so

Эпизод 7: Building Chat Applications [Pt 7]

1:36:41

1 час 36 минут 41 секунда

much hello and welcome to generative AI for beginners today we'll be covering chat applications I'm Jasmine Greenway

1:36:50

1 час 36 минут 50 секунд

and let's get into it first we will cover the differences between chat Bots and generative AI chat

1:36:58

1 час 36 минут 58 секунд

applications then we'll talk about building and integrating chat applications then we'll focus on options for the user experience and how to

1:37:06

1 час 37 минут 6 секунд

enhance it then we'll talk about performance and capturing metrics around the applications and then we'll talk

1:37:15

1 час 37 минут 15 секунд

about leveraging AI responsibly and then we'll wrap up with a set of demos so

1:37:24

1 час 37 минут 24 секунды

let's start with the difference between a chat bot and the chat application both facilitate some sort of communication chat Bots often follow a

1:37:33

1 час 37 минут 33 секунды

set of predescribed scripts and rules and in contrast Advanced chat applications especially those powered by

1:37:41

1 час 37 минут 41 секунда

generative AI can generate new and contextually relevant responses in real time a great example of this is when you

1:37:50

1 час 37 минут 50 секунд

ask a chat bot something along lines that's something outside of its domain it may say something like I don't know

1:37:59

1 час 37 минут 59 секунд

ask another question where a generative AI application would ask for more context or provide a best

1:38:06

1 час 38 минут 6 секунд

guess when it comes to building chat applications it's not always about making them smarter but also making them

1:38:13

1 час 38 минут 13 секунд

performance and a great experience for the user so let's talk through some options for building a chat application

1:38:24

1 час 38 минут 24 секунды

first is the usage of apis and sdks when you're building application one of the first things you're going to want to do

1:38:31

1 час 38 минут 31 секунда

is assess what's already out there and save yourself a little bit of time and apis and sdks are really great

1:38:38

1 час 38 минут 38 секунд

first step to leverage functionalities that you don't have to build from scratch and it also reduces some overhead and speeds up your development

1:38:46

1 час 38 минут 46 секунд

process so you can focus on the parts of your application that are the most important to you next is enhancing the user

1:38:53

1 час 38 минут 53 секунды

experience and this can be quite important because general ux principles apply but there's also going to be some

1:39:00

1 час 39 минут

additional considerations that become important due to the nature of this application so adding features that

1:39:08

1 час 39 минут 8 секунд

allow users to ask for clarifications should your chat application generate an ambiguous answer also maintaining context

1:39:17

1 час 39 минут 17 секунд

retaining the context so that a user can build prompts based on past information as well as things like personalization

1:39:25

1 час 39 минут 25 секунд

to be able to allow the user to tailor the responses that are the best fit for them and you know going deeper into this

1:39:33

1 час 39 минут 33 секунды

idea of personalization um you want to tailor the user experience so that the user can receive specific answers that

1:39:41

1 час 39 минут 41 секунда

the user that make the user feel good and really just more understood and last but not least

1:39:49

1 час 39 минут 49 секунд

accessibility accessibility across visual auditory motor or cognitive impairments provides an experience that

1:39:57

1 час 39 минут 57 секунд

allows your application to be used by everyone some things you might want to consider our resizable text screen reader compatibility text to speech and

1:40:06

1 час 40 минут 6 секунд

speech text functionalities visual cues for audio notifications voice commands and simplified voice

1:40:14

1 час 40 минут 14 секунд

options now let's move on to another way to apply customization through a process

1:40:21

1 час 40 минут 21 секунда

called fine tuning fine-tuning is often considered when a pre-trained model falls short in a specialized domain or a

1:40:29

1 час 40 минут 29 секунд

specific task so things like company jargon or maybe context around a particular medical condition that a phys

1:40:38

1 час 40 минут 38 секунд

a physician is trying to diagnosed can fall under this category and are usually great candidates for fine-tuning now the process of fine

1:40:46

1 час 40 минут 46 секунд

tuning requires a data set and a existing pre-train model an llm and what normally happens is that that model is

1:40:54

1 час 40 минут 54 секунды

trained with a data set to apply that specific domain knowledge so let's look an example of this with Azure openai one

1:41:04

1 час 41 минута 4 секунды

of the first steps in applying fine tuning in Azure open AI is selecting a base model and this model is what you

1:41:11

1 час 41 минута 11 секунд

will train with your training data and that next step is selecting that particular training data now this is

1:41:20

1 час 41 минута 20 секунд

probably going to be your longest step you might have to clean the data you might have to format in a particular way and you know you can also refer to the docs and how to do that um but this will

1:41:29

1 час 41 минута 29 секунд

probably take a little bit of time to massage the data into into a way that is that is consumable for the model to be

1:41:37

1 час 41 минута 37 секунд

used to and also to be used effectively next you have the choice to apply hyperparameters so one of these hyper

1:41:47

1 час 41 минута 47 секунд

parameters might be things like an Epoch which defines the number of times that the learning algorithm will work through

1:41:53

1 час 41 минута 53 секунды

the entire training data set and finally after selecting your data and your hyperparameters you can now start

1:42:01

1 час 42 минуты 1 секунда

training that model with a data set and as soon as it's done you're ready to go and use this new finetune model another

1:42:09

1 час 42 минуты 9 секунд

option is retrieval augmented generation or rag it's architecture pattern that augments the capabilities of a llm like

1:42:18

1 час 42 минуты 18 секунд

for example chat GPT by adding an in informational retrieval system provides grounding data and adding this system

1:42:27

1 час 42 минуты 27 секунд

gives you control over grounding data used by an llm when it forms a response now here what we're looking at

1:42:35

1 час 42 минуты 35 секунд

here is like a diagram of of this particular architecture using Azure services so in here we have Azure AI

1:42:43

1 час 42 минуты 43 секунды

search and Azure open Ai and this architecture diagram isn't like every

1:42:51

1 час 42 минуты 51 секунда

every rag architecture but it's it really provides a really great highlevel summary of the pattern and basically how it works is that you would start with a

1:43:00

1 час 43 минуты

user question or requests also known as a prompt you would send that to something like Android AI search to find relevant

1:43:07

1 час 43 минуты 7 секунд

information and then you would send the top ranked search results to an llm and finally you would use natural language

1:43:16

1 час 43 минуты 16 секунд

and reasoning capabilities of the llm to generate a response to that prod so let's start applying these steps

1:43:26

1 час 43 минуты 26 секунд

onto the architecture diagram that we're looking at right now and and math them to the services so the web app on the

1:43:33

1 час 43 минуты 33 секунды

left here provides the user experience so the user will essentially ask their questions are prompts there in that

1:43:41

1 час 43 минуты 41 секунда

particular app now the code in the app server orchestr strator coordinates the handoffs handoffs of the user experience

1:43:50

1 час 43 минуты 50 секунд

between the informational retrieval and the llm so essentially Azure AI search

1:43:59

1 час 43 минуты 59 секунд

and that large language model that might be an Azure open AI so inputs pass through here to get search results

1:44:05

1 час 44 минуты 5 секунд

through a query but also go to the llm to set the context and intent so that query in Azure a open AI search or Azure

1:44:15

1 час 44 минуты 15 секунд

AI search can really handle the keyword or term or vector queries now the llm

1:44:23

1 час 44 минуты 23 секунды

receives the original prompt plus the results from Azure AI search the llm will analyze them and essentially

1:44:30

1 час 44 минуты 30 секунд

formulated response that goes back to the user now AA search provides inputs to The llm Prompt but doesn't actually

1:44:39

1 час 44 минуты 39 секунд

train the model and this is really where it deviates from fine-tuning so in rag architecture there's no extra training

1:44:46

1 час 44 минуты 46 секунд

the llm is pre-trained using public data and generates gen responses that are augmented by bu information from the

1:44:54

1 час 44 минуты 54 секунды

Retriever and you can learn more about this pattern in chapter 15 of the curriculum now we'll move on to

1:45:03

1 час 45 минут 3 секунды

considerations for a high quality Aid driven chat experience we'll look at performance rhetorics and how to use AI

1:45:11

1 час 45 минут 11 секунд

responsibly in these sections so numbers matter and it's essential to keep track of metrics like response time and user

1:45:18

1 час 45 минут 18 секунд

sat satisfaction to make sure their application is performing at its best so considerations for performance metrics

1:45:25

1 час 45 минут 25 секунд

fall across time accuracy user perception error rate and anomaly detection and time is usually one of our

1:45:33

1 час 45 минут 33 секунды

most valuable resources and one of the things you really want to consider is how long does it take for user to get the answer that they're looking for how

1:45:42

1 час 45 минут 42 секунды

long does it take for your application to run successfully measurements like uptime and response time fall under this

1:45:49

1 час 45 минут 49 секунд

category another in consideration is accuracy and metrics like precision and recall that also create what is known F1 score

1:45:57

1 час 45 минут 57 секунд

can be helpful here moving on to user perception this can really come from a number of different sources for example

1:46:05

1 час 46 минут 5 секунд

surveys user interviews or user studies and the important thing here is what will you do with the feedback and how

1:46:13

1 час 46 минут 13 секунд

will you apply it and integrate it into your chat application another consideration is error rate or how often the model makes

1:46:21

1 час 46 минут 21 секунда

mistakes in understanding or its output and finally anomaly detection or identifying unusual

1:46:29

1 час 46 минут 29 секунд

patterns that don't conform to expected behavior and one of the things you might want to consider here and really every

1:46:36

1 час 46 минут 36 секунд

and really all these metrics is how will you respond to these another component for a highquality chat application is

1:46:44

1 час 46 минут 44 секунды

using AI responsibly and Microsoft has an approach to responsible AI that is split into six principles that should

1:46:51

1 час 46 минут 51 секунда

guide AI development use it's important to build trust and inclusivity amongst your user prese prevent harm protect

1:47:00

1 час 47 минут

their data as well as provide Improvement and corrective measures in case of mistakes let let's take a look

1:47:07

1 час 47 минут 7 секунд

at some demos the first Dem I'm going to show you is a basic usage of the Azure

1:47:14

1 час 47 минут 14 секунд

open AI end points in in the Azure open AI service so we're in AET intera

1:47:23

1 час 47 минут 23 секунды

notebook and what we're going to be doing is bringing in three libraries here Azure Azure open AI SDK as well as

1:47:32

1 час 47 минут 32 секунды

system environment for some configuration steps so I've already brought in my endpoint in my key and I'm

1:47:40

1 час 47 минут 40 секунд

just going to go ahead and click these cells and go ahead and click on this sub

1:47:47

1 час 47 минут 47 секунд

before I do I just want to kind of walk you through what's happening here we're them we're telling uh the we're sending

1:47:55

1 час 47 минут 55 секунд

in a a system prompt that says that you're a software engineer that ended your day and and the user or the input

1:48:04

1 час 48 минут 4 секунды

that's going that's going to take in is what tasks need to be doing so essentially this chat this application is a software engineer finishing their

1:48:13

1 час 48 минут 13 секунд

day and they need a task list of what to do at the end of their day now in Azure open AI you deploy you deploy your your

1:48:22

1 час 48 минут 22 секунды

llm and you give them a label and so that's what's happening here on this line here where we're called uh get chat

1:48:29

1 час 48 минут 29 секунд

completions and so we are accessing the chat completions model and this is

1:48:35

1 час 48 минут 35 секунд

essentially chat uh GPT 35 turbo and we're we're accessing it to to complete

1:48:42

1 час 48 минут 42 секунды

our our message here and our input and respond to our input and there we go so

1:48:50

1 час 48 минут 50 секунд

here are our steps that we need to do to Wine down for the day now that was a really basic example but now I'm going to show you a little bit more of an

1:48:58

1 час 48 минут 58 секунд

involved example um of a doet application that is has a basic chat app

1:49:05

1 час 49 минут 5 секунд

here so let's go ahead and ask the chat app what is the

1:49:12

1 час 49 минут 12 секунд

highest point of NYC and we immediately got a question answer or response back saying the

1:49:20

1 час 49 минут 20 секунд

highest point is in and Staten Island reaching an elevation of 410 ft or 125 m

1:49:27

1 час 49 минут 27 секунд

above sea level and as we can see on the left here kind of how similar how you

1:49:33

1 час 49 минут 33 секунды

would see this in uh in chat gbt it actually summarize we actually use asro

1:49:40

1 час 49 минут 40 секунд

openingi to summarize the conversation that we're having on the left side here in our chat history if you're interested

1:49:48

1 час 49 минут 48 секунд

in learning more about building chat applications with generative AI or even learning other topics visit our

1:49:55

1 час 49 минут 55 секунд

curricula listed here in the curricula you'll find more in-depth information about this topic and many others including interactive notebooks for you

1:50:04

1 час 50 минут 4 секунды

to try out for yourself like the one you saw here happy

Эпизод 8: Building Search Apps Vector Databases [Pt 8]

1:50:14

1 час 50 минут 14 секунд

learning okay welcome to the session for generative generative AI for beginners uh my name is Dave Glover I'm A Cloud Advocate I'm based in Sydney Australia

1:50:23

1 час 50 минут 23 секунды

and uh this is for lesson six building search applications all righty so what we're going to cover in the session we're

1:50:30

1 час 50 минут 30 секунд

going to look at what semantic search is you might a term you might have heard banded around we're going to talk about vectors and embeddings again a term that

1:50:38

1 час 50 минут 38 секунд

you might have heard but just kind of what the difference is between them we're going to talk about Vector stores and we're going to coup of

1:50:44

1 час 50 минут 44 секунды

demos so the goal of this session so ultimately at the end of the session you're going to have a better idea how vectors play a crucial role enabling

1:50:53

1 час 50 минут 53 секунды

effective semantic search so hopefully that's what you're going to pick up out of the session now when I first uh

1:51:00

1 час 51 минута

started talking and learning about generative AI um one of the terms that was banded around a lot was semantic search and I must admit at the time I

1:51:09

1 час 51 минута 9 секунд

didn't really know what semantic search was but a bit of digging around and I kind of got the general idea of how this works and hopefully this will help you

1:51:16

1 час 51 минута 16 секунд

as well so semantic search is really kind of intent based search or boiling down to what are the Core Concepts

1:51:24

1 час 51 минута 24 секунды

you're thinking about you want to look for so take an example if you talk about my dream watch now if you did a keyword

1:51:32

1 час 51 минута 32 секунды

search you would end up with results which were about dreams and which are about watches which is probably what you

1:51:40

1 час 51 минута 40 секунд

weren't what not what you were looking to find now if you were doing semantic search what they would do is it would

1:51:47

1 час 51 минута 47 секунд

boil down to the concept probably of my ideal watch which is what you're really thinking about and then you would find things about

1:51:55

1 час 51 минута 55 секунд

ideal watches and you'd probably expand on that search term so the key thing about semantic search is around intent or around the concept that you're

1:52:03

1 час 52 минуты 3 секунды

looking for as opposed to keyword search which would find dreams and watches now semantic search is kind of like a really

1:52:11

1 час 52 минуты 11 секунд

pivotal point or pivotal concept when it comes to building large language model applications and you'll often find these

1:52:19

1 час 52 минуты 19 секунд

applications take a big dependency on what we call semantic Sur and embeddings okay so you've heard about

1:52:27

1 час 52 минуты 27 секунд

the term vectors no doubt you're learning about those in University of school and um you might have heard the word embeddings you might be thinking

1:52:35

1 час 52 минуты 35 секунд

well what's the difference because often they're used almost um semantically or so almost hand

1:52:43

1 час 52 минуты 43 секунды

inand um so vectors and embeddings what are they so an embedding is a special

1:52:50

1 час 52 минуты 50 секунд

type of vector that is generated by a large language model that has semantic meaning so ultimately what it's going to

1:52:58

1 час 52 минуты 58 секунд

generate when you go and send a piece of text off to an embedding engine it's going to return back a vector and that

1:53:07

1 час 53 минуты 7 секунд

Vector will have a representation of what the semantic meaning was of that bit of tax you sent into that um

1:53:14

1 час 53 минуты 14 секунд

embeddings engine now there are lots of different embedding models now the ones you've probably heard of would be like the open AI embeddings model so there's

1:53:22

1 час 53 минуты 22 секунды

text embedding 3- small which is a new model that's just come out uh -3- large is again a new one you might have heard

1:53:31

1 час 53 минуты 31 секунда

of text embedding adaah -002 which has been a very popular one now these are by no means the only embeddings models if

1:53:40

1 час 53 минуты 40 секунд

you go after hugging face um you'll find a whole um series of embedding models and you'll find rankings of performance

1:53:47

1 час 53 минуты 47 секунд

and how well these things do but to give an example and in fact for the for this for the example I'm going to be showing you in the example in this lesson plan

1:53:56

1 час 53 минуты 56 секунд

it's using text and Benny a002 and it will return back a vector

1:54:03

1 час 54 минуты 3 секунды

which is 1 by 1536 dimensioned Vector so that's what you're going to get back and obviously that's pretty difficult to kind of visualize and you can't really

1:54:11

1 час 54 минуты 11 секунд

imagine what that is um but anyway that's the size of the vector you get back now the other concept that you that you'll often hear banded about when it

1:54:20

1 час 54 минуты 20 секунд

comes to vectors and embeddings is around this concept called nearest neighbor search and what that's doing is that

1:54:29

1 час 54 минуты 29 секунд

you've taking you've got a a collection of these these vectors which have been created using these embedding models and

1:54:36

1 час 54 минуты 36 секунд

what you want to be to do is you want to say okay well I've got this collection of of embedding models now I want to go and find I've got another piece of text

1:54:45

1 час 54 минуты 45 секунд

I want this is my search term my dream watch for example and I want to go and find in that collection which of the vectors are closest

1:54:53

1 час 54 минуты 53 секунды

to this concept of my dream watch and this is the concept you hear called nearest neighbor and you'll also

1:55:01

1 час 55 минут 1 секунда

he hear the concept of cosine similarities and cosine similarities is a Formula that you can use across a

1:55:09

1 час 55 минут 9 секунд

collection of vectors to go and find a vector which matches closest to the vectors in this collection and basically calculates how close one vector is to

1:55:18

1 час 55 минут 18 секунд

others in multi-dimensional space in this case 1 by 15 36 Dimension vector and basically what you get back is you

1:55:26

1 час 55 минут 26 секунд

get a ranking of relatedness of vectors or semantic meaning against your vector that you're looking for now to kind of

1:55:34

1 час 55 минут 34 секунды

visualize this if you think about we've got most of us we can we can happy with two-dimensional vectors and threedimensional vectors you think about

1:55:42

1 час 55 минут 42 секунды

um we've got on the left hand side here we got two dimensional vectors and we can see here okay well I've got this this was this blue dot here was um the

1:55:51

1 час 55 минут 51 секунда

vector for search where you could very easy see well okay these other vectors around here these points that represent

1:55:58

1 час 55 минут 58 секунд

these vectors you can see they're close but you can see this black dot over here and this blue dot over here they're not so close so you can see that if you were

1:56:07

1 час 56 минут 7 секунд

to do a cosine similarity these these this these other dot these dots here would be um closest the same thing here

1:56:15

1 час 56 минут 15 секунд

in threedimensional space now I'm using an application called octava um which is quite a nice application just

1:56:22

1 час 56 минут 22 секунды

visualizing things and you can see I've got um 10 vectors here and we'll go and run

1:56:31

1 час 56 минут 31 секунда

this and just to help visualize this so we just move this around you can start seeing well I've got these vectors in three dimensional space and we can most

1:56:39

1 час 56 минут 39 секунд

of us we can see x y and Zed and we can visualize that pretty straightforward and again if I said okay well this red dot here this was the Red Dot which

1:56:48

1 час 56 минут 48 секунд

represents my search question my the Vector that I want to search for you could see around here that okay well you

1:56:55

1 час 56 минут 55 секунд

can see that these dots here are most likely related to the the Red Dot on the center so kind of you can again visualize this so we can visualize

1:57:04

1 час 57 минут 4 секунды

two-dimensional space we can visualize threedimensional space but clearly we can't really visualize too much more than that we certainly can't visualize a

1:57:12

1 час 57 минут 12 секунд

1 by 1536 uh based Vector so hopefully kind of gives you a bit of an idea and you can just kind of extrapolate that

1:57:19

1 час 57 минут 19 секунд

concept of saying okay well I can understand two- dimensional threedimensional there's a formula that can help me go and work out what it would look like

1:57:28

1 час 57 минут 28 секунд

what would be the nearest neighbor using coine similarity now what you find is with again this concept of vectors and

1:57:36

1 час 57 минут 36 секунд

embeddings if you were have go create a an embedding for boots shoes and socks

1:57:42

1 час 57 минут 42 секунды

they will create vectors which are in multi-dimensional space related they'll be sitting in the same multi-dimensional

1:57:50

1 час 57 минут 50 секунд

space and over here the concept of a camera well that's not the same concept as shoes socks and and Boots so it's

1:57:58

1 час 57 минут 58 секунд

going to be in a different dimensional space so again when I when I said I want I want to go and buy some shoes for example might be a query um you would

1:58:07

1 час 58 минут 7 секунд

create a an embedding for that and then you would go and search across these vectors and You' find okay these shoe socks and um boots would be the closest

1:58:16

1 час 58 минут 16 секунд

um Vector in multi-dimensional space hopefully that was clear what's going on okay so the next thing I want to talk about is we've got we've got these

1:58:25

1 час 58 минут 25 секунд

vectors that we've created from embeddings and we want to store them somewhere so you again you'll hear about

1:58:32

1 час 58 минут 32 секунды

Vector stores and these are just um uh effectively like an index or like a database but they're optimized for

1:58:39

1 час 58 минут 39 секунд

storing vectors so you hear um products like Azure AI search is a a vector

1:58:47

1 час 58 минут 47 секунд

engine redus postgress Pine gon and there are a lot of others out there they're about maybe maybe 20 or so Vector stores out there in the

1:58:55

1 час 58 минут 55 секунд

marketplace today um but again the popular ones are things like red as Azure AI search now the demo that I'm going to

1:59:03

1 час 59 минут 3 секунды

show you and a great way of prototyping some of these things is actually to do this just in memory and a super easy way to do this was just with a pandas data

1:59:12

1 час 59 минут 12 секунд

frame and this is what the demo that I'm going to be showing you and the demo that you'll find in the repo is rather than having to worry about backend data

1:59:20

1 час 59 минут 20 секунд

Stores um for prototyping and just playing around with ideas a pandas data frame is a super easy way to get up and run into this but clearly wouldn't do

1:59:29

1 час 59 минут 29 секунд

the view pushing this application into production you wouldn't run this application from a panda's data frame you would use some sort of backend uh

1:59:37

1 час 59 минут 37 секунд

data service like Ed our search okay so we got a bit of a demo and I just want to show you a bit of how this works and how this how this how

1:59:46

1 час 59 минут 46 секунд

this data set was built so the the example that you're going to find in the repo for this uh

1:59:53

1 час 59 минут 53 секунды

for this for this talk is actually taking the transcripts from a whole lot of YouTube videos it's actually um

2:00:00

2 часа

content from the um AI search the Microsoft AI search uh Channel which is on YouTube and what we did is we took

2:00:08

2 часа 8 секунд

around about 300 transcripts from various from various talks and we embedded those we created

2:00:15

2 часа 15 секунд

embeddings for them and we put them into in this case into a panda data frame and we can use that for searching now I just want to talk a bit about the

2:00:23

2 часа 23 секунды

concept about what you do around this so say you've got this transcript now whenever you got large data sets it could be a transcript it

2:00:31

2 часа 31 секунда

could be a PDF document it could be data from a Word document or whatever that with this bit of text is coming from um what you typically do is you break that

2:00:39

2 часа 39 секунд

down or you do this concept called chunking so you take this video transcript in this case and what you do is you chunk it down and and the chunks

2:00:48

2 часа 48 секунд

are kind of the way you think about this is what Fidelity do you want for the search do I want about to search in five minute increments in that video

2:00:57

2 часа 57 секунд

transcript or three minute increments for example and that would determine how big the chunking size is now the other

2:01:06

2 часа 1 минута 6 секунд

concept you do with chunking and you again you'll find various libraries which help you with chunking is you also tend to do an

2:01:13

2 часа 1 минута 13 секунд

overlap um and the idea behind this is often it's it doesn't make sense just to cut off a chunk at an arbitrary sentence

2:01:21

2 часа 1 минута 21 секунда

or things like that you might will say well I want a sentence or two from the next chunk and that kind of gives you

2:01:28

2 часа 1 минута 28 секунд

context gives you kind of better context and you can see in this chunk these chunks here I've got a bit of you can see this red text here is actually the

2:01:36

2 часа 1 минута 36 секунд

beginning of the next chunk and again you'll find that there's a second chunk down here the red text is the beginning

2:01:43

2 часа 1 минута 43 секунды

of the next chunk and again that's done to provide better search semantic search so then what you go do is you're

2:01:52

2 часа 1 минута 52 секунды

going to send each of these chunks off to an embedding in this case we're going to send it off to text embedding 002 that's the model we're using and that's

2:02:00

2 часа 2 минуты

going to return back a vector remember returns back a 1 by 1536 Dimension vector and then what you do is you put

2:02:09

2 часа 2 минуты 9 секунд

that into a store now in this demo what the store is actually just going to be a Json a Json file and we're going to load that up into Panda's data frame so now I

2:02:18

2 часа 2 минуты 18 секунд

want to go and search Okay in this case here I want to go and look I want to learn about our studio and notebooks so

2:02:25

2 часа 2 минуты 25 секунд

you remember my data set was um the AI show and it's going to have lots of to lots of content around Azure and

2:02:34

2 часа 2 минуты 34 секунды

notebooks and Jupiter notebooks and cognitive services and things like that our studio but I want to find particular round our studio notebooks so the way

2:02:42

2 часа 2 минуты 42 секунды

you do that that's my query and then what I would do is I would generate an embedding for that

2:02:49

2 часа 2 минуты 49 секунд

query so again I'd send that bit of text off to the the um in this case text embedding Ada model and I get back my 15

2:02:58

2 часа 2 минуты 58 секунд

1X 1536 dimensioned vector and then what I would do is I would do a nearest neighbor or cosine

2:03:06

2 часа 3 минуты 6 секунд

similarities uh against my store now backend Data Systems like redis and AI

2:03:14

2 часа 3 минуты 14 секунд

search they have the capability to go and look at vast amounts of vector data and then find the nearest neighbor that's kind of what they're optimized

2:03:22

2 часа 3 минуты 22 секунды

for we're going to be using a pandas data frame and we're going to be using cosine similarities and that we're going and do that we're going and find um the

2:03:30

2 часа 3 минуты 30 секунд

closest vectors which match that data and I get back the results and you you typically get back a ranking to say okay

2:03:37

2 часа 3 минуты 37 секунд

well we think this is 094 95% closest um ranking and again you'd see various

2:03:44

2 часа 3 минуты 44 секунды

rankings of the um chunks of text that most closely match the by semantic

2:03:52

2 часа 3 минуты 52 секунды

meaning the result set and the data set okay so hopefully that was fairly clear so what I'm going to do is pop across to

2:03:59

2 часа 3 минуты 59 секунд

visual studio code and in the repo for this lesson you'll find there's this Jupiter notebook and what this Jupiter notebook's going to do it's going to

2:04:08

2 часа 4 минуты 8 секунд

load up various things but the most important thing about well the couple things that's going on here we're going to be calling um the open AI text

2:04:16

2 часа 4 минуты 16 секунд

embedding a model to go and generate a an embedding for my qu question which we're then going to use against the um

2:04:25

2 часа 4 минуты 25 секунд

the set sets of embeddings for the um the transcripts okay so the first thing we

2:04:32

2 часа 4 минуты 32 секунды

here we're going to put up the endpoint we got to the API key API version this is just information that's needed for Azure open Ai and then I'm going to say

2:04:40

2 часа 4 минуты 40 секунд

the model is text embedding now it's super important that the that the when you're going to embed your question

2:04:48

2 часа 4 минуты 48 секунд

you're using the same model that you used to to create the vectors um for the transcripts so those

2:04:55

2 часа 4 минуты 55 секунд

models are got to match and then this is the the data set that I'm going to load up into memory now I'm going to skip through some of this reasonably quickly

2:05:04

2 часа 5 минут 4 секунды

um you can get look at this in your own time but here goes the function for the

2:05:10

2 часа 5 минут 10 секунд

cosine similarity and there's a numpy um um formulas in here for working out our

2:05:17

2 часа 5 минут 17 секунд

nearest neighbor so we're going to come through here and ultimately what this is going to do we're going to load up the data set and then we're going to sit in

2:05:25

2 часа 5 минут 25 секунд

the loop and we're going to ask for a query and this is so we're going to run this so you run this stupid notebook and that's loaded and it's

2:05:34

2 часа 5 минут 34 секунды

going to be I'm interested in talks about uh R studio and

2:05:41

2 часа 5 минут 41 секунда

notebooks okay so that's going to be my query so that's that's a question so remember what's going to happen this is going to be sent to the embedding

2:05:49

2 часа 5 минут 49 секунд

engine and what it's going to do it's created an embedding for that and it's going to go and check all of the embeddings that I've created for the

2:05:57

2 часа 5 минут 57 секунд

transcripts and it's going to bring back the videos that are most similar and a nice one that I've tested out already is

2:06:06

2 часа 6 минут 6 секунд

in this one here so the second one here data science with machine learning in this video Rafal is going to talk about

2:06:13

2 часа 6 минут 13 секунд

data science and machine learning and you'll see the similari is 084 and if I go and click on this link what you're going to notice it's going

2:06:22

2 часа 6 минут 22 секунды

to start talking about it's going to take us straight to that transcript and to the place in the

2:06:33

2 часа 6 минут 33 секунды

video you see what happened there is it I'll just go back we'll link on we'll click on that

2:06:44

2 часа 6 минут 44 секунды

link so you see the beauty of this is taking that complete transcript we chunked it up into I think 3 minute uh

2:06:52

2 часа 6 минут 52 секунды

chunks I did my query I converted that into embedding then I looked across my pandas data frame I looked at all of the

2:06:59

2 часа 6 минут 59 секунд

embeddings or the vectors I've got sitting in there I found the closest and then and inside that data set I also had the time that said okay they're going to

2:07:08

2 часа 7 минут 8 секунд

start talking about our studio and notebooks at this particular time in this um YouTube video so that's kind of

2:07:17

2 часа 7 минут 17 секунд

how this works so hopefully that makes sense and gives you a bit of an idea of how the application

2:07:24

2 часа 7 минут 24 секунды

works okay so with that we've got a couple of resources so we've got the Search application I've just shown you so you'll find that that link in here so

2:07:32

2 часа 7 минут 32 секунды

you'll find that and there's also a really good um set of uh Microsoft learned content and a particular one

2:07:41

2 часа 7 минут 41 секунда

they're about understanding embeddings and Azure open AI search or service and then have a read through that again you're going to learn more but hopefully

2:07:49

2 часа 7 минут 49 секунд

that's giving you enough to get you going and learning about how to go and build search applications using um

2:07:56

2 часа 7 минут 56 секунд

embeddings vectors and cosine similarity and using nearest neighbor to go and find the relevant content in your data

2:08:03

2 часа 8 минут 3 секунды

sets Okay thank you very much hey everyone welcome back to

Эпизод 9: Building Image Generation Applications [Pt 9]

2:08:15

2 часа 8 минут 15 секунд

generative aifa beginners I said I would be back I am Pabo Lopez Cloud advocate in AI in a little bit of thought net and

2:08:23

2 часа 8 минут 23 секунды

we have Chris nari I I believe you folks know him by this point say hi Chris hey folks super excited to be back

2:08:32

2 часа 8 минут 32 секунды

my name is Chris noring as Pablo was saying you might have seen me in a couple of videos already hopefully I'm a senior Advocate at Microsoft and just

2:08:39

2 часа 8 минут 39 секунд

like Pablo we do awesome things with AI and many other exciting Technologies back to you

2:08:46

2 часа 8 минут 46 секунд

Pablo thank you so much Chris and you know what that's why is really excited of J because I know you folks are alreadying a lot of text right so you

2:08:55

2 часа 8 минут 55 секунд

folks saw me on lesson two talking about how you learn on on llm Foundation models the very bases on ASI but now you

2:09:04

2 часа 9 минут 4 секунды

folks are more advanced here I just saw a little bit of you know chat applications text applications let's go to images now so what we going to cover

2:09:13

2 часа 9 минут 13 секунд

today we're gonna show um image generation and how to use and build an image generation app you see just to

2:09:21

2 часа 9 минут 21 секунда

things here but I have to a little bit do some explaining because image generation it's a little bit more complicated than you know what what do

2:09:29

2 часа 9 минут 29 секунд

we usually Sol a little bit on text right so let's build an image generation app we're gonna prompt engineer for

2:09:37

2 часа 9 минут 37 секунд

image generation and work Dolly and me Journey but not only those two I going to talk that a bit

2:09:45

2 часа 9 минут 45 секунд

later so let's start with a single question how right because if you folks

2:09:52

2 часа 9 минут 52 секунды

saw on the last episodes you folks may know that um I can type and then it can

2:09:59

2 часа 9 минут 59 секунд

you know try to tokenize right try to generate next token next token next token to finish but images do not work

2:10:07

2 часа 10 минут 7 секунд

like that J they they have pixels they have rdb values right so it sounds a little bit confusing on how those can

2:10:15

2 часа 10 минут 15 секунд

work when it sounds like magic right so how to generate images of AI

2:10:22

2 часа 10 минут 22 секунды

anyway so I'm going to start talking about one thing remember what I said about Foundation models they are

2:10:30

2 часа 10 минут 30 секунд

training a multi mold way so they have like not only tax they have tax images videos um music they have a lot of

2:10:39

2 часа 10 минут 39 секунд

things to train them so one of cool thing that happened is that they try to do a open the ey has clip so what is

2:10:47

2 часа 10 минут 47 секунд

clip clip is basically you get images and then they going to charch your closet it so here I have one of the test

2:10:53

2 часа 10 минут 53 секунды

they did with clip so it's food 101 which is a small data set for testing so you can see here have a very fancy

2:11:01

2 часа 11 минут 1 секунда

guacamole by the way look how fancy it is and you can see that it can rank perfectly on that of course not always

2:11:10

2 часа 11 минут 10 секунд

is going to know be exact remember JS of AI has a lot of Statistics in cabul stochastics get things a little bit

2:11:18

2 часа 11 минут 18 секунд

wrong but you can see that was major advance so what a good thing about clip is that it is a generative that can

2:11:25

2 часа 11 минут 25 секунд

describe images very well so it can get images and think I believe this is that

2:11:32

2 часа 11 минут 32 секунды

and this is how it it is blah blah blah blah blah so you can see it's very can be very descriptive as well okay Pablo

2:11:41

2 часа 11 минут 41 секунда

great now the Jour I can describe images cool and how you saying this is great

2:11:48

2 часа 11 минут 48 секунд

because imagine the following remember when I talk about embeddings yeah baby

2:11:54

2 часа 11 минут 54 секунды

embeddings so what can it do it can pick this text and generate embeddings right

2:12:02

2 часа 12 минут 2 секунды

and then I know if I can do text I can describe it how can I do the reverse so

2:12:10

2 часа 12 минут 10 секунд

imagine that clip instead of you know trying to describe something and generate something with like eddings and then I have like a near network with you

2:12:18

2 часа 12 минут 18 секунд

know tension diffusion you know all the all the amazing things that we have ji it could actually you know go back into

2:12:26

2 часа 12 минут 26 секунд

the reverse process so that's what it does so clip gives you know a Vibe basically I like to say a little bit gen Z right so it picks the vibe of the

2:12:35

2 часа 12 минут 35 секунд

image say this I believe should be the vibe then when you type you're going to have something that you want to describe right for imagine that I want to

2:12:43

2 часа 12 минут 43 секунды

describe a dog in the Eiffel Tower so it will have like Eiffel Tower you have dog

2:12:50

2 часа 12 минут 50 секунд

have some you know it will have something that you can think about something that can imagine so what it it does is basically pick that turn it

2:12:58

2 часа 12 минут 58 секунд

edings and then clip can judge right clip can judge between you know the images that you have and the image that

2:13:05

2 часа 13 минут 5 секунд

they generate so that's how they trained this model here this attention model to create images by your text because we

2:13:14

2 часа 13 минут 14 секунд

had clip so we could just always compare that's amazing so then they created this so it's two Parts basically clip which

2:13:22

2 часа 13 минут 22 секунды

communicates and can judge and can say things and have like this diffusion model right here that can generate images by a text so that's how they

2:13:31

2 часа 13 минут 31 секунда

created those amazing AI models that you know today with images but okay we have now so many

2:13:40

2 часа 13 минут 40 секунд

right I just pick four here Dolly which is from the open AI family TBT family you folks already know and love web

2:13:49

2 часа 13 минут 49 секунд

copilot that we had a lot of you know D do uses so if you want to test do the

2:13:56

2 часа 13 минут 56 секунд

best way and the quickest way is to go to web co-pilot on bank or Edge we have me Journey which uses the

2:14:05

2 часа 14 минут 5 секунд

interface of you know Discord servers it is you know it can have some seven limits and you can have L meta AI which

2:14:13

2 часа 14 минут 13 секунд

is not available right now for most countries but then we have meta AI meta

2:14:19

2 часа 14 минут 19 секунд

AI is basically The Meta version of D of course they they do a lot of things they can talk Etc so they have inside of it a

2:14:27

2 часа 14 минут 27 секунд

generator model that can generate images so and these are just four we have so

2:14:34

2 часа 14 минут 34 секунды

many to describe from but these as know are the most used of course you can use stable diffusion you can use your own

2:14:43

2 часа 14 минут 43 секунды

computer to do that as we talk on service versus model as well it's the same things you can think about on here

2:14:50

2 часа 14 минут 50 секунд

so there you go now you know like to generate images anyway right so you may think I don't have many uses for that

2:14:59

2 часа 14 минут 59 секунд

Pablo why should I know care about those and here's the thing about it it is a

2:15:06

2 часа 15 минут 6 секунд

fast way to prototype anything imagine that you're doing an app and the design team is not ready you can actually do a

2:15:14

2 часа 15 минут 14 секунд

small small logo just to test and then try already with a specifications to do it create things faster so you can

2:15:23

2 часа 15 минут 23 секунды

prototype and then on the resign team is ready you just change and done you already have your feature ready or if

2:15:30

2 часа 15 минут 30 секунд

you are you know a company you're just you you don't have budget to contract them so we can actually try to generate

2:15:36

2 часа 15 минут 36 секунд

a lot of with AI you know just do tweaks here and there trying to understand a little bit more to help your ux to to

2:15:44

2 часа 15 минут 44 секунды

blow up so these are some amazing things that we have regenerative AI it empowers people that don't have you know

2:15:52

2 часа 15 минут 52 секунды

sometimes the knowledge to create great things and then try them to improve on those to make excellent Concepts or you

2:15:59

2 часа 15 минут 59 секунд

can try to prototype fast to deliver things on time and not only that you can

2:16:06

2 часа 16 минут 6 секунд

use them to scale as well so we have three amazing things that you can do with images with generative

2:16:14

2 часа 16 минут 14 секунд

AI so I'm going to bring Chris Chris man what do you have for me today

2:16:21

2 часа 16 минут 21 секунда

right so try to so what we're trying to achieve today is to make sure that you understand when you're supposed to use image generation right because it sounds

2:16:29

2 часа 16 минут 29 секунд

super cool even with text generation you send something to an AI you get some interesting response back indic case with text versus text that's fun but

2:16:37

2 часа 16 минут 37 секунд

even more fun is if you can take that text prompt that prompting knowledge send that into the AI and out comes an image right and you've already shown

2:16:46

2 часа 16 минут 46 секунд

Pablo how we can get some really uh exciting images with space or landscape or what have you all of that sounds

2:16:53

2 часа 16 минут 53 секунды

super nice and neat but what if we had a customer scenario because I can imagine that many of you are watching this and

2:17:00

2 часа 17 минут

maybe you are senior developers or some kind of Enterprise developers or maybe you're thinking about a startup and it's like how would I use image generation in

2:17:09

2 часа 17 минут 9 секунд

a business scenario so that's what we're trying to do here today so what we're going to do is me and Pablo we're going to play the role of a customer that's

2:17:17

2 часа 17 минут 17 секунд

going to be me and Pablo is going to be the developer who's going to interview the customer namely me and see what I want and just for the sake of scenario

2:17:26

2 часа 17 минут 26 секунд

I'm going to play a property manager in London right so I'm going to be that customer I want Pablo's help as an

2:17:34

2 часа 17 минут 34 секунды

engineer to use image generation to improve my business so Pablo I'm going to let you take it away from this point

2:17:41

2 часа 17 минут 41 секунда

so you can start interviewing me so I get what I need um Chris um hello what do you need

2:17:49

2 часа 17 минут 49 секунд

today hey Pablo it's uh good to meet you today it's going to be exciting to see if we can work on a project together so you can help improve my business but

2:17:58

2 часа 17 минут 58 секунд

today I'm going to be a property manager I'm based in London so I'm going to need help with all my properties to make sure that we can sell them or or sublet them

2:18:07

2 часа 18 минут 7 секунд

to whoever you know my customers might be but one of the problems I struggle with right is to make sure that I can visualize things to people because

2:18:16

2 часа 18 минут 16 секунд

sometimes I have a photo sometimes I I have not and I'm not even sure what the photos make sense in the evening light or the Morning Light so I I think I want

2:18:25

2 часа 18 минут 25 секунд

some kind of AI service with image generation that can really help me you know think like is this what I want is this not what I want so maybe you can

2:18:33

2 часа 18 минут 33 секунды

help me based on the context of this being London what do you think absolutely Chris so we can actually generate some images to at

2:18:42

2 часа 18 минут 42 секунды

least prototype what you seeing in Your Vision that's a very good part of ji ji can do a lot of those things to help you

2:18:50

2 часа 18 минут 50 секунд

so what what kind of properties are you thinking about yeah so I I usually have a lot of

2:18:57

2 часа 18 минут 57 секунд

properties by water so would make total sense maybe to say hey let's go for London properties buy water I mean of

2:19:05

2 часа 19 минут 5 секунд

course I'm going to have some high-rise buildings and some smaller buildings but I'm just curious to see what at this point what this tool can can do for me

2:19:12

2 часа 19 минут 12 секунд

so maybe you can show me based on that info absolutely so we can do a very basic prompt right here which is

2:19:19

2 часа 19 минут 19 секунд

properties in London by water or comma River here so it can actually start to generate something and that's a thing I

2:19:27

2 часа 19 минут 27 секунд

going show you on Azure AI so you can see that we are have have settings but first I want to show you that it's

2:19:34

2 часа 19 минут 34 секунды

generate one image by prompt on a AI I want to uh request more you're going to

2:19:41

2 часа 19 минут 41 секунда

see later how to do that but you can see right you have some options so you can copy prompt generate you images at the

2:19:48

2 часа 19 минут 48 секунд

same prompt download show code or delete right here it show that succeeded which is great because now it's going to to

2:19:57

2 часа 19 минут 57 секунд

hand her our image here and while that shows there we go um this is the image that is generated but I want to show you

2:20:05

2 часа 20 минут 5 секунд

as well folks some things on settings because yes we are not just limited imagine that you think oh this is too Vivid this

2:20:13

2 часа 20 минут 13 секунд

is so dream likee how can I know be more realistic you can change on prompt sure

2:20:21

2 часа 20 минут 21 секунда

but you can change here on our style image so it can be like natural I want the quality of image and HD and let's be

2:20:29

2 часа 20 минут 29 секунд

with the classic the square one okay Chris I generated some images here uh an image what you think about

2:20:37

2 часа 20 минут 37 секунд

this why don't want to change something so looks pretty good right I mean it's by the water kind of resembles

2:20:45

2 часа 20 минут 45 секунд

the building I I do sublet or sell uh what I'm bit curious about if you can show this In a Different Light maybe because this looks like evening and I

2:20:53

2 часа 20 минут 53 секунды

probably want to show it in the morning light I think like it's it's always nice to have both right because people want to see that nice Lighting in the dark

2:21:00

2 часа 21 минута

but if if I can have some reference image with Morning Light I think that'd be great by the Morning Light so you see

2:21:09

2 часа 21 минута 9 секунд

how I'm doing here right so basically I'm trying to describe what Chris is feeling so and may be asking okay but comparing to what I wrote on an agent

2:21:18

2 часа 21 минута 18 секунд

Pablo what is difference so on images usually you have to be more direct you you need to imagine being a director right so you have to imagine where

2:21:27

2 часа 21 минута 27 секунд

you're putting things or trying to understand the lighting the composition you need to understand if you're going to use lenses what kind of lenses are

2:21:35

2 часа 21 минута 35 секунд

you using yes that's important as well so you have so many things you may think about on you try to write a prompt but

2:21:41

2 часа 21 минута 41 секунда

it's different a lot different than you try to write forr instes on text because text you're an AIG agent you do this

2:21:50

2 часа 21 минута 50 секунд

that this is how you do it no here be more like a director imagine that you have a camera and you can try to put things here and there you can change

2:21:57

2 часа 21 минута 57 секунд

lighting so have a lot more flexibility here it doesn't need to you know instruct what it needs to do like you're

2:22:05

2 часа 22 минуты 5 секунд

gonna do this that try to be more you know take some elaborators on here as well so there you go I added here by the

2:22:12

2 часа 22 минуты 12 секунд

morning light and see what I generates and while it generates I can show you as well some things I can copy this prompt

2:22:20

2 часа 22 минуты 20 секунд

and I can can generate New Image so you can see right here that I'm generating another image with the same prompt and

2:22:28

2 часа 22 минуты 28 секунд

let's go for easily download but I want to show you more things very very very soon I'm going to show you the code and

2:22:36

2 часа 22 минуты 36 секунд

there you go it's already generated both of the images there you go this is uh properties in London by the water comma

2:22:44

2 часа 22 минуты 44 секунды

river by the Morning Light um what do you think about those two images Chris

2:22:51

2 часа 22 минуты 51 секунда

yeah I especially like the middle one it actually looks like one of the properties that we are selling right now so what I am curious about also because

2:23:00

2 часа 23 минуты

you know we need to be able to feature this at various web pages you know mobile apps and so on so are you able to show this in different resolutions like

2:23:07

2 часа 23 минуты 7 секунд

could I have like a mini map or or no um the word I'm looking for is thumbnail like could you make a thumbnail out of this and maybe a you know a screen

2:23:16

2 часа 23 минуты 16 секунд

resolution that's quite big so I'm kind of wondering about the flexibility here absolutely and I'm going to tell you one

2:23:24

2 часа 23 минуты 24 секунды

thing before that you notice that I already changed some of the settings here remember I already change it from Vivid natural and HD and I show you what

2:23:33

2 часа 23 минуты 33 секунды

the same prompt does with different properties so this is a vivid and standard look how different it looks with HD and natural you can see that

2:23:42

2 часа 23 минуты 42 секунды

it's trying to be more a photo than trying to fit on the properties so we need to make sure that you're fitting on the properties any you can see right

2:23:51

2 часа 23 минуты 51 секунда

here this looks much more natural right doesn't look like a painting or something like that of course a water maybe but you can adjust on the prompt

2:23:59

2 часа 23 минуты 59 секунд

as always so Chris is asking can I generate different sizes and for sure let's go to a bigger size let's imagine

2:24:07

2 часа 24 минуты 7 секунд

that we need to a better for web page so let's generate on a big size and then let's generate you know in a tiny tiny

2:24:16

2 часа 24 минуты 16 секунд

bit like two six 256 for two5 like very small so yeah you can actually right now I'm

2:24:24

2 часа 24 минуты 24 секунды

trying to generate where am I just end oh okay I love when this

2:24:31

2 часа 24 минуты 31 секунда

happens there we go okay let's go to got that

2:24:41

2 часа 24 минуты 41 секунда

basically okay so you can see right here that now I'm generating my banner so the banner is generated and my ask Pablo I

2:24:49

2 часа 24 минуты 49 секунд

didn't like this angle right it isn't doesn't look what I'm thinking that this should be don't worry you can try or to generate new image with the same prompt

2:24:58

2 часа 24 минуты 58 секунд

or you can try to do a little bit I gonna show you not gonna PA I didn't like the image what

2:25:06

2 часа 25 минут 6 секунд

can I do let's pick this one I don't like this sky so what can we do here we can try to mask or try try to regenerate

2:25:13

2 часа 25 минут 13 секунд

images pick the best ones and then try to see what you have remember J AI is a little bit you know stochastic how generate images so some sometimes not

2:25:21

2 часа 25 минут 21 секунда

generate great things but look at that that looks funny yep for sure yeah I really like

2:25:29

2 часа 25 минут 29 секунд

that image so I was also thinking like a lot of the objects we sell are like apartments right so wondering if you can be flexible to do like tow houses

2:25:38

2 часа 25 минут 38 секунд

because we have those too oh excellent so then folks what you need to do is that properties in London

2:25:45

2 часа 25 минут 45 секунд

right you can describe here inside of it so let's go with properties in London properties

2:25:55

2 часа 25 минут 55 секунд

with town houses there you

2:26:02

2 часа 26 минут 2 секунды

go so you may ask Pablo this is not the most you know sometimes corre to describe and yes but remember

2:26:09

2 часа 26 минут 9 секунд

technically it can just put more and more and more sometimes need take care of how we put the order of the words but

2:26:18

2 часа 26 минут 18 секунд

connectivity in sometimes even when you try to write the most no grammatic correct doesn't you know allow zali to

2:26:28

2 часа 26 минут 28 секунд

optimize by The Prompt remember you're trying here to optimize to not you know in know way right so properties left

2:26:35

2 часа 26 минут 35 секунд

town houses sounds strange but sometimes it's the best way because I understand that you can mix other properties with

2:26:43

2 часа 26 минут 43 секунды

town houses right we're trying to detach here the meaning of both yeah classic generative AI you need to learn some

2:26:51

2 часа 26 минут 51 секунда

Small Tricks here and let's talk about a little of the prompt you can see here that it's talk properties of tow houses

2:26:58

2 часа 26 минут 58 секунд

and you may ask that's doesn't seem that correct grammatically or stylistically and that's true but you may think one

2:27:07

2 часа 27 минут 7 секунд

thing is that sometimes you need to prioritize the way that work for the not to make the most sense but try to make

2:27:13

2 часа 27 минут 13 секунд

like waights into the prompt imagine that you're not putting like a prompt like a

2:27:20

2 часа 27 минут 20 секунд

very defined sentence it's more like trying to delate to understand okay what is the weights you should put here and

2:27:27

2 часа 27 минут 27 секунд

go here so we have properties of course it tries to put houses there and that's the thing sometimes they'll hallucinate

2:27:35

2 часа 27 минут 35 секунд

but if it try to hallucinate okay let's get rid of properties and then just do town houses and that's the thing you need need to tweak a little bit here and

2:27:43

2 часа 27 минут 43 секунды

there to try to get the best image but I I'll be very honest this one it's stunning right so thank you for this one

2:27:51

2 часа 27 минут 51 секунда

Pablo I think we're going to close down on our customer scenario here but I think it's pretty clear that you know you're able to deliver different kinds of light different kind of buildings

2:27:59

2 часа 27 минут 59 секунд

maybe different angles and exactly what you showed right I mean you just need to adjust the prompt and you can even change the size of the image for

2:28:07

2 часа 28 минут 7 секунд

thumbnails for larger image oh that looks pretty good so yeah let's uh let's take it home Pablo let's see if we can

2:28:14

2 часа 28 минут 14 секунд

summarize this video all right absolutely but before I summarize I may ask how can I implement this in our my

2:28:22

2 часа 28 минут 22 секунды

applications so if you have some doubts take a look in our guide here building generative AI application on lesson nine

2:28:30

2 часа 28 минут 30 секунд

or take a look here we have some documentation so here have my here's python but as always you can select

2:28:38

2 часа 28 минут 38 секунд

multiple things then you're going to have your client your API version your endpoint and your API key remember that

2:28:45

2 часа 28 минут 45 секунд

you need to generate with prompt right there and then you're going to have n n is not number of images generated as you folks see I'm generating one for one but

2:28:54

2 часа 28 минут 54 секунды

you remember if you generate for if you generate for dolly or M you have multiple so I can just put n equals

2:29:03

2 часа 29 минут 3 секунды

another desire and then you can analyze image by image by this image URL more things then how to generate Pablo I love

2:29:12

2 часа 29 минут 12 секунд

that I want this exact thing you can click code and then you can to send how to write this prompt and then they JS and loads but

2:29:21

2 часа 29 минут 21 секунда

let's recap what we learned today you understood how Dolly and mean Journey works you understood how many

2:29:30

2 часа 29 минут 30 секунд

opportunities that we have and you understand how apply those you got here me and Chris talk a little bit how should you prompt engineering and how to

2:29:38

2 часа 29 минут 38 секунд

put that in your codes folks that was a great lesson thank you so much for being with us on gen for beginners and Chris

2:29:46

2 часа 29 минут 46 секунд

last words all right so thank you so much Pablo and all of you out there I hope this was an interesting lesson on how to work with images and especially

2:29:55

2 часа 29 минут 55 секунд

how you can generate those exactly what Pablo said little bit of prompt engineering little bit of tweaking and you can see vastly different results so

2:30:02

2 часа 30 минут 2 секунды

you saw how flexible that was you saw how easy also it bu to use some python code whatever kind of code to integrate

2:30:09

2 часа 30 минут 9 секунд

that into your app so definitely use the studio to get that help but there are also some great tips on Microsoft learn

2:30:16

2 часа 30 минут 16 секунд

and Microsoft docs pages and also some sample repo out there and definitely our own curriculum generative AI for

2:30:24

2 часа 30 минут 24 секунды

beginners so thank you for watching thank you folks see you next

Эпизод 10: Building Low Code AI Applications [Pt 10]

2:30:35

2 часа 30 минут 35 секунд

class welcome everybody to the generative AI for beginners course my name is SoMo and I'm A Cloud Advocate at

2:30:43

2 часа 30 минут 43 секунды

Microsoft so today I just want to showcase lesson 10 building no code AI application

2:30:50

2 часа 30 минут 50 секунд

using generative AI which you probably didn't think it was possible so this is also part of the generative AI for beginners course and for this lesson

2:30:59

2 часа 30 минут 59 секунд

we're going to be covering a few things so we're going to cover how you can use generative AI in Power Platform and then

2:31:07

2 часа 31 минута 7 секунд

we're going to switch over to look at the AI capabilities with AI Builder and generative AI so it's not going to be

2:31:14

2 часа 31 минута 14 секунд

just only purely based on generative AI we're going to look at some models that come with AI Builder and also gen AI within the Power Platform so the

2:31:23

2 часа 31 минута 23 секунды

generative Ai and the Power Platform is actually about enhancing local development and application with generative AI which is a key Focus area

2:31:33

2 часа 31 минута 33 секунды

for the Power Platform the goal is to enable everyone to build AI enabled and powered apps sites dashboards and

2:31:41

2 часа 31 минута 41 секунда

automate processes with AI without requiring any data science expertise whereas in the past you needed to have a

2:31:49

2 часа 31 минута 49 секунд

technical background or become a data scientist to actually work with AI and like I mentioned we can Empower every

2:31:56

2 часа 31 минута 56 секунд

person with AI because AI is no longer a niche capabilities for pro developers and data Sciences which we can provide

2:32:06

2 часа 32 минуты 6 секунд

through aour AI is an imperative and expected offering in our day-to-day productivity so you can think about

2:32:14

2 часа 32 минуты 14 секунд

PowerPoint designer for an example in which in this case when you are working on those slide presentations you may have some suggestions for how your

2:32:23

2 часа 32 минуты 23 секунды

design would look like for a specific uh slide on your deck and also you can also have teams transcriptions so you record

2:32:31

2 часа 32 минуты 31 секунда

a teams meeting and then you can be able to pull a transcript from that specific teams meeting and hear what other people

2:32:39

2 часа 32 минуты 39 секунд

were saying if you couldn't make it out on the audio and of course the new Co pilot capabilities in Microsoft

2:32:46

2 часа 32 минуты 46 секунд

365 but before we actually had like technical workers that worked with AI through Pro Cod development around using

2:32:55

2 часа 32 минуты 55 секунд

Microsoft aure and some of the connective cognitive services within Microsoft Azure but now the making experience in the Power Platform as part

2:33:04

2 часа 33 минуты 4 секунды

of the Microsoft cloud offering takes the same principle of bringing AI capabilities to Aid every makers in our

2:33:12

2 часа 33 минуты 12 секунд

platform being able to build solutions that are AI powered and also AI enabled so that they can be able to build those

2:33:20

2 часа 33 минуты 20 секунд

Solutions either you are sitting in an HR department or a marketing department you can use low code no code tools such

2:33:27

2 часа 33 минуты 27 секунд

as the Power Platform so that you can be able to ship your solutions to your everyday end users that are in a sense

2:33:35

2 часа 33 минуты 35 секунд

using Microsoft teams Microsoft 365 and also SharePoint but low cold no code tools

2:33:42

2 часа 33 минуты 42 секунды

like the Power Platform are not necessarily familiar with a lot of people and you might be asking yourself what is a Microsoft platform well this

2:33:51

2 часа 33 минуты 51 секунда

is where no code low code and code first is welcome so this is where you can be able to build Solutions without needing

2:33:59

2 часа 33 минуты 59 секунд

to have any knowledge of how to write a program or how to write code but again even if you know how to do that you can

2:34:07

2 часа 34 минуты 7 секунд

be able to build bring those experiences into the Power Platform and build solutions that already enhance with some

2:34:15

2 часа 34 минуты 15 секунд

of the skills that you already have and also the new capabilities that you can have the Power Platform is actually made up of five products where you have power

2:34:23

2 часа 34 минуты 23 секунды

apps for mobile development mobile app development power automate for process automation powerbi for business

2:34:30

2 часа 34 минуты 30 секунд

analytics co-pilot Studio which is my personal favorite where you can build you can build your own co-pilot power

2:34:37

2 часа 34 минуты 37 секунд

Pages lastly where you can build externally facing websites and all of these have a generative AI capability

2:34:46

2 часа 34 минуты 46 секунд

enabled for them and this is co-pilot where you have the Power Platform Co pilot that enables you to build even

2:34:54

2 часа 34 минуты 54 секунды

faster Solutions using each or every single one of this products within the Microsoft Power Platform but how does

2:35:02

2 часа 35 минут 2 секунды

this actually fit into the Microsoft cloud in the past because of the fully integrated Microsoft cloud and our

2:35:10

2 часа 35 минут 10 секунд

investment in AEL or in up open AI we're able to apply generative AI which is

2:35:16

2 часа 35 минут 16 секунд

large language models into the fabric of each and every single one of our products so you can think about for an example Microsoft 365 now we have a

2:35:25

2 часа 35 минут 25 секунд

Microsoft 365 co-pilot that enables and enhances productivity there's also co-pilot in developer tools in the form

2:35:34

2 часа 35 минут 34 секунды

of GitHub co-pilot and you will have either your IDE or you're using your code editor like Visual Studio code to

2:35:41

2 часа 35 минут 41 секунда

actually write code even much more faster using GitHub co-pilot even the Power Platform has its own co-pilot that

2:35:49

2 часа 35 минут 49 секунд

I like I actually mentioned earlier on so co-pilots is about making AI a

2:35:56

2 часа 35 минут 56 секунд

companion to help you do your job better and faster you can think of the error of co-pilots rather as having AI as a real

2:36:05

2 часа 36 минут 5 секунд

time collaborator that generates content Sparks creativity and completes

2:36:12

2 часа 36 минут 12 секунд

work but then how do you then take advantage or positive advantage of genv within the Power Platform how do you use

2:36:20

2 часа 36 минут 20 секунд

co- pilot to enhance your productivity when Building Solutions let's take this example for for for a moment to actually

2:36:28

2 часа 36 минут 28 секунд

look at how you can be able to build an automation much more quicker than you would have in the past so we just

2:36:36

2 часа 36 минут 36 секунд

describe our Automation and say on a daily basis we want to collect all the performed inspections from power apps and we have a condition here that says

2:36:44

2 часа 36 минут 44 секунды

all those that have PA composed an email summary and attach an invoice from sap in the past we needed to add the steps

2:36:52

2 часа 36 минут 52 секунды

manually but with the help of generative AI in the form of co-pilot in power automate we have a power timate flow already built as a draft then we can be

2:37:01

2 часа 37 минут 1 секунда

able to see some of the actions that are already added so we retrieve an invoice from sap add generative AI capability by generating an email body which we'll get

2:37:10

2 часа 37 минут 10 секунд

to later and also we need to make sure that we enforce responsible AI where we review that email message that was

2:37:18

2 часа 37 минут 18 секунд

generated by by AI then after we've approved that we send an email to that specific party but then in a sense where

2:37:28

2 часа 37 минут 28 секунд

you actually want to update this draft using generative AI instead of using the manual process as we would have done in

2:37:35

2 часа 37 минут 35 секунд

the past we can still use or take positive advantage of the chat enabled co-pilot within the designer or the

2:37:43

2 часа 37 минут 43 секунды

design studio within power automate so let's say we have another condition now into our power automate flow that we

2:37:51

2 часа 37 минут 51 секунда

actually want to cater to so we look at if the car has been inspected we want the bot to check if the car has been

2:37:58

2 часа 37 минут 58 секунд

inspected and is off brand then after that it needs to send an alert to A team's Channel after that specific

2:38:06

2 часа 38 минут 6 секунд

inspection has failed so what then J AI does it actually adds those actions in that very specific place so that you can

2:38:15

2 часа 38 минут 15 секунд

be able to put in all of those details that you actually need and then you can even see even with this capability you can also add in some of the other

2:38:23

2 часа 38 минут 23 секунды

conditions where it checks for if the inspection has failed and if it has it posts that specific teams message onto

2:38:31

2 часа 38 минут 31 секунда

that specific teams meet teams channel that you are specifying within your power aut to make flow but then again

2:38:40

2 часа 38 минут 40 секунд

does is that it is it really that much that you can be able to use generative AI like that within the Power Platform

2:38:47

2 часа 38 минут 47 секунд

no let's actually look at how you can use other AI capabilities within the Power Platform by looking at the AI

2:38:54

2 часа 38 минут 54 секунды

models and gen AI with AI Builder firstly let's look at AI Builder it actually enables you to infuse AI to

2:39:03

2 часа 39 минут 3 секунды

turn data into actions without writing any code so you have a few different capabilities in this case where you can look at documents where you can process

2:39:12

2 часа 39 минут 12 секунд

some of those documents either you want to process a form reip processing or you want to do some language detection text

2:39:20

2 часа 39 минут 20 секунд

translation and also category classification and so forth you can also take it a step further and work with images where you want to detect some

2:39:28

2 часа 39 минут 28 секунд

objects within a specific image so you can use the object detection model within AI Builder or you can use the

2:39:36

2 часа 39 минут 36 секунд

text recognition OCR then it doesn't end there with AI Builder you can also make decisions by

2:39:43

2 часа 39 минут 43 секунды

using the prediction model that AI builda is actually enabling you to use it doesn't doesn't end there but the

2:39:50

2 часа 39 минут 50 секунд

biggest question is okay this course is about generative Ai and we're just only talking about AI models that have

2:39:58

2 часа 39 минут 58 секунд

already been there even before generative AI came into play and this is where we actually look at how AI build

2:40:05

2 часа 40 минут 5 секунд

and datae ground secure and integrate business data with AI through this data

2:40:12

2 часа 40 минут 12 секунд

verse has your knowledge you have all of your information stored into a data verse table and then you want to actually be able to access that and

2:40:21

2 часа 40 минут 21 секунда

utilize that that knowledge into some of your Solutions using prompts and that is done through AI Builder and within AI

2:40:30

2 часа 40 минут 30 секунд

Builder we have something called The Prompt Builder that enables you to either use or create your own custom

2:40:38

2 часа 40 минут 38 секунд

prompts that you can be able to put into some of the solutions that you have so you'll have a pre-u prompt library that has templates to leverage models and

2:40:46

2 часа 40 минут 46 секунд

prompts without any training require then if you don't want to use a pre-u prompt uh prompt Library you can also

2:40:55

2 часа 40 минут 55 секунд

use or create your own custom prompts by using the prompt engineering interface within either power apps or power

2:41:02

2 часа 41 минута 2 секунды

automate so you can build your GPT proms that trigger instructions on GPT model hosted in aure open AI service in this

2:41:11

2 часа 41 минута 11 секунд

case you don't manage the models in the Azure open service you just consume and build your own custom prompts using the prompt engineering inter interace then

2:41:20

2 часа 41 минута 20 секунд

last but not least you can also add your data into some of your prompts so you can cater for your data in some of your prompts where you add Dynamic inputs for

2:41:29

2 часа 41 минута 29 секунд

an example data from Auto an automated workflow and also Enterprise data to ground your prompts let's look at some

2:41:37

2 часа 41 минута 37 секунд

of the scenarios that are available with the prompt Builder you have summarization which is the most famous one where you can have some text

2:41:45

2 часа 41 минута 45 секунд

summarization either from an email you have text classif ification you have content generation and email reply you

2:41:53

2 часа 41 минута 53 секунды

want to be able to reply to an email or have help from generative AI to help you reply to an email instead of having to

2:42:01

2 часа 42 минуты 1 секунда

sit there and think about how you can be able to draft this email reply capability for an example can be able to help you to have a draft already working

2:42:10

2 часа 42 минуты 10 секунд

and you can just edit edit it and then you can send it through to your customer and then some of the other ones that are available are sentiment analysis you can

2:42:19

2 часа 42 минуты 19 секунд

have some promts that check for sentiment within a specific text or within a specific input that you're getting either from your user or from

2:42:27

2 часа 42 минуты 27 секунд

your solution and translation and Co code generation but how does this really work

2:42:34

2 часа 42 минуты 34 секунды

we're going to look at a high level workflow at first you have end users they consume your content and provide

2:42:42

2 часа 42 минуты 42 секунды

possible input through some of the apps that you built so it could be a power app which is an Enterprise app a power autom flow that's running in the

2:42:50

2 часа 42 минуты 50 секунд

background taking the input from the user or a Microsoft 365 co-pilot either be it it's coming from a Word document

2:42:58

2 часа 42 минуты 58 секунд

or it's coming in from an email then you have you as part of this generative act uh for beginners course where you are a

2:43:07

2 часа 43 минуты 7 секунд

maker where you create custom proms optimized for a business scenario and you can utilize some of the proms within

2:43:14

2 часа 43 минуты 14 секунд

power apps power automate and co-pilot Studio to enhance the solutions that you buil and all of these solutions that you

2:43:22

2 часа 43 минуты 22 секунды

are building that are being used by your end users are powered by AI Builder where you have that prompt creation experience and some of the system

2:43:30

2 часа 43 минуты 30 секунд

guidelines and even retrieval augmented generation which is also called rag again makes you it makes use of AI

2:43:39

2 часа 43 минуты 39 секунд

Builder and data R and all of this is powered by the gbt 3.5 turbo hosted by

2:43:47

2 часа 43 минуты 47 секунд

the Azure openi service it's not managed by you it's already built in onto AI Builder so that you can then be able to

2:43:54

2 часа 43 минуты 54 секунды

use it to build some of the solutions that you actually have that you're going to ship out to your users you don't have to worry about managing the gbt 3.5

2:44:04

2 часа 44 минуты 4 секунды

turbo model on your own you just need to worry about building a solution that makes the experience for your users

2:44:12

2 часа 44 минуты 12 секунд

better right with all of this prompt talk that we're talking about we have to actually think about how to build an

2:44:21

2 часа 44 минуты 21 секунда

effective prod because at the end of the day whenever we are using generative AI we need to be able to get the most basic

2:44:28

2 часа 44 минуты 28 секунд

or the Most Wanted solution or we want the most basic uh response that we are getting from the generative AI model for

2:44:37

2 часа 44 минуты 37 секунд

an example so here comes in prompt engineering where you have to build an effective prompt to get the best response so for example when you are

2:44:46

2 часа 44 минуты 46 секунд

building an effective prompt you need to think about a few things the the task which is an instruction telling the GPT model that task to be performed then

2:44:54

2 часа 44 минуты 54 секунды

consider the context as you provide within your prompt that describes the data that will be acted on along with any input variables the the next step

2:45:03

2 часа 45 минут 3 секунды

into your prompt is the expectation convey to GPT the goals and expectations on the response then last

2:45:11

2 часа 45 минут 11 секунд

but not least the output help the generative AI model or help GPT format the output the way you wanted so that

2:45:19

2 часа 45 минут 19 секунд

you don't end up saying that this is not what you're looking for how do you then be able to use this or take advantage of

2:45:26

2 часа 45 минут 26 секунд

this within the Power Platform like I mentioned earlier on you have the prompt library and GPT templates so you can use

2:45:34

2 часа 45 минут 34 секунды

preconfigured prompts to help you get started with common scenarios like responding to a customer complaint classifying text or extracting

2:45:43

2 часа 45 минут 43 секунды

information from a text or summarizing text that is coming either from an email or from an application that you actually

2:45:50

2 часа 45 минут 50 секунд

buil using power apps if you want to use some of the preconfigured proms you can actually use the pre-configure templates

2:45:57

2 часа 45 минут 57 секунд

to get you started so that you can be able to in integrate those proms in an endtoend workflow and also sometimes

2:46:04

2 часа 46 минут 4 секунды

into an endtoend solution that you can be able to use power apps to build and then enhance it using an endtoend

2:46:12

2 часа 46 минут 12 секунд

workflow now the next step for you is to actually try it out yourself so go through the lesson complete the entire

2:46:19

2 часа 46 минут 19 секунд

lesson 10 to actually build a local AI application and you'll be able to build a power app by describing you want to

2:46:28

2 часа 46 минут 28 секунд

build an app to track and manage student assignments and then there are some other extra steps so that you can be able to build a power automate Flow by

2:46:35

2 часа 46 минут 35 секунд

describing what you actually want from it and also check out the other lessons within this specific generative AI for

2:46:42

2 часа 46 минут 42 секунды

beginers course will actually give you some of the knowledge on how you can be able to use generative AI with different

2:46:49

2 часа 46 минут 49 секунд

tools and different levels of

Эпизод 11: Integrating External Applications with Function Calling [Pt 11]

2:46:58

2 часа 46 минут 58 секунд

expertise hi my name is Cory stered pace and I'm part of the AI Cloud ay team here at Microsoft and I have the honor

2:47:06

2 часа 47 минут 6 секунд

of delivering to you lesson number 11 uh called function calling and working with external applications of our generative

2:47:14

2 часа 47 минут 14 секунд

AI for beginners course in the introduction of this course and what we'll cover today is really one explaining what function

2:47:22

2 часа 47 минут 22 секунды

calling is and also understanding when we should be reusing that in our applications how to use function callink specifically with with using the Azure

2:47:31

2 часа 47 минут 31 секунда

openai service and lastly how to integrate a function call into your applications the learning goals for

2:47:39

2 часа 47 минут 39 секунд

today after you complete this lesson you should have a better understanding of the purpose of function calling how to actually set up a function call and then

2:47:47

2 часа 47 минут 47 секунд

lastly and most importantly how to design an effective function call so that you have successful function call within your

2:47:55

2 часа 47 минут 55 секунд

application first we're going to explain a bit of a scenario or what we're actually building here in this course as well as in this specific

2:48:03

2 часа 48 минут 3 секунды

lesson in this case we're going to look at uh when a user would come in and let's say they want to maybe request uh

2:48:11

2 часа 48 минут 11 секунд

that they want to get some courses to learn about mic different various different Microsoft products in the case the user would make a request directly

2:48:19

2 часа 48 минут 19 секунд

to our large language model let's say in this case uh GPT 3.5 turbo and in the case that we will want the large

2:48:27

2 часа 48 минут 27 секунд

language model to be able to call a function uh in this case get courses that would actually make an API call to

2:48:34

2 часа 48 минут 34 секунды

the Microsoft learn catalog API to get courses that would be relevant for the user and then lastly in the flow I'll

2:48:41

2 часа 48 минут 41 секунда

present those options to the user so that's what we're going to be building towards in today's lesson but before we even do that we

2:48:49

2 часа 48 минут 49 секунд

need to answer the question of why function calling in the first place why is it important and why would you want to use

2:48:56

2 часа 48 минут 56 секунд

it well one of the increasing importance of building applications with large language models is in fact that U you

2:49:04

2 часа 49 минут 4 секунды

know what many have start with chat applications whether working directly with the model or making requests directly to the model we're seeing more

2:49:11

2 часа 49 минут 11 секунд

and more that applications need to have a precise formatting in terms of responses from the model when they want

2:49:19

2 часа 49 минут 19 секунд

to actually integrate this into other flows or parts of the application and that be the application itself uh and this is what you know function calling

2:49:27

2 часа 49 минут 27 секунд

really addresses so if we look at this two descriptions here we have two descriptions of students Emily Johnson and Michael Lee we have very similar

2:49:36

2 часа 49 минут 36 секунд

descriptions in terms of what their GPA is your skills um and you know extracurriculars in terms of what they've been doing and where they want

2:49:43

2 часа 49 минут 43 секунды

to go in their lives essentially now we're going to take two of the same proms uh in this case we're going to say we want to extract all the

2:49:52

2 часа 49 минут 52 секунды

information that's important so their name their major the school the grades and the clubs that they've been involved in so these are the same prompts and

2:50:00

2 часа 50 минут

we've requested the model to actually send this into a Json object because maybe we want to use that format later on uh maybe just restore that

2:50:07

2 часа 50 минут 7 секунд

information into a database or maybe make us some sort of API request with that information what happens is if we even

2:50:15

2 часа 50 минут 15 секунд

run these two prompts what you will see is we might actually get different formatting in the responses that could cause errors in our application unless

2:50:23

2 часа 50 минут 23 секунды

we check them and maybe add any additional features so in this case we have the name which is about the same the major which is computer science the

2:50:31

2 часа 50 минут 31 секунда

same school which is in also in the same format but then if you notice here at grades in one we have a 3.7 and in the

2:50:39

2 часа 50 минут 39 секунд

other with Michael Le we have a 3o GPA 3.8 GPA so are both strings but they obviously contain different information

2:50:47

2 часа 50 минут 47 секунд

that could cause issues in our application later on so when we want we're talking about function calling it is really to address these concerns in a

2:50:55

2 часа 50 минут 55 секунд

way so that we can make sure that the formats that we receive are in a good weight that we can actually call a function later on in our application and

2:51:02

2 часа 51 минута 2 секунды

that function runs successfully so what are the actually the use cases for function calling well like I said earlier the one is if we want to call

2:51:11

2 часа 51 минута 11 секунд

any external tools whether that be tools that our application is using or even what our users are using uh and we want to make sure that the format that these

2:51:19

2 часа 51 минута 19 секунд

tools expect or the ones that we deliver we also might want to even create API calls or database queries so in the case

2:51:26

2 часа 51 минута 26 секунд

of our uh use case that we're building towards we also we will be making API call and we want to make sure that we have the right parameters to make that

2:51:34

2 часа 51 минута 34 секунды

call successful whether that be the required param parameters or even optional ones and then lastly if you just want to work with some sort of

2:51:41

2 часа 51 минута 41 секунда

structured data working with function calling is another good way to do that whether we want to use that structure data to display to the user in a

2:51:48

2 часа 51 минута 48 секунд

different format um that maybe not not coming directly from the large language model so now that we kind of understand the use case let's actually get started

2:51:57

2 часа 51 минута 57 секунд

on creating our first function call so the first thing we'll do is actually create a message and in this case it's a very standard format in terms of U the

2:52:05

2 часа 52 минуты 5 секунд

messages that we would develop with using a GPT 3.5 and in this case we have a user that comes in the content we're

2:52:12

2 часа 52 минуты 12 секунд

sending and they just want to find a good course for beginner student to learn Azure so that's the message that we're initially setting then we also need to sort of

2:52:21

2 часа 52 минуты 21 секунда

Define the functions uh first thing we do is Define the name of that function we give it a general description that is also very helpful for the large language

2:52:29

2 часа 52 минуты 29 секунд

model to identify if that function is relevant and then lastly is the parameters in this case we are going to assign an object and make it have three

2:52:38

2 часа 52 минуты 38 секунд

different properties one is the role which also has a description so this is all the role of the learner of the product and this is has a description of

2:52:46

2 часа 52 минуты 46 секунд

what the product's actually being covered here whether it's Azure powerbi or any sort of maybe Microsoft tools that are in the Microsoft learn catalog

2:52:54

2 часа 52 минуты 54 секунды

and then lastly is the level this is the skill level of the or level experience of the learn so this gives a lot of information to the large language model

2:53:01

2 часа 53 минуты 1 секунда

to understand that these are the criteria or the necessary parameters that's needed for this function to operate and then lastly we even have a

2:53:09

2 часа 53 минуты 9 секунд

required field that we can set here so at Le at the very least large language model needs to be able to determine that there's a role that's been sent to the

2:53:18

2 часа 53 минуты 18 секунд

or determined or sent by the user in their chat message in order for this to function to

2:53:25

2 часа 53 минуты 25 секунд

operate then we actually going to make the function call so in this case we're going to choose the model that we've deployed uh all the messages that we've

2:53:33

2 часа 53 минуты 33 секунды

completed in the cases of the user message of the system message we're also going to include the functions that we have done so this is the function equl

2:53:40

2 часа 53 минуты 40 секунд

functions and then lastly we have this function called Auto and auto means that the the large language model has the ability to decide whether or not uh the

2:53:49

2 часа 53 минуты 49 секунд

function is uh appropriate for this particular instance or this chat message then next we'll actually see

2:53:58

2 часа 53 минуты 58 секунд

what the function call that the the model has determined in this case if you remember our earlier message the student had determined that they were a beginner

2:54:06

2 часа 54 минуты 6 секунд

and they were looking to learn Azure so just kind of looking at what the model has interpreted here is that the role is

2:54:13

2 часа 54 минуты 13 секунд

student uh the product that is relevant for this user is azure and then lastly it's a beginner now we're actually going to

2:54:21

2 часа 54 минуты 21 секунда

integrate this into our application by importing requests because we want to make an API request and also the parameters which is the role product and

2:54:29

2 часа 54 минуты 29 секунд

level that this API requires in order to get some information and then lastly we're going to take that URL all those

2:54:38

2 часа 54 минуты 38 секунд

parameters and pend it to the URL to get the results then we're going to integrate that into our application by doing the

2:54:45

2 часа 54 минуты 45 секунд

function to call and the available functions which the function name that we will have and then we're going to also load that into Json uh so that we

2:54:53

2 часа 54 минуты 53 секунды

will handle the responses within the arguments that we get from the function then most importantly after we get those responses we want to make sure

2:55:02

2 часа 55 минут 2 секунды

that the model is have an ability to include that me into their messages so we want to then append those message that message uh and give that into the

2:55:10

2 часа 55 минут 10 секунд

model so that when it it goes into make the last week the output that this was what the model will receive so this is kind of ending the

2:55:20

2 часа 55 минут 20 секунд

flow is that now the assistant has the role of and the content where they say they find some good courses for beginner

2:55:27

2 часа 55 минут 27 секунд

students is presenting the URLs uh that has been retrieved from the function that was calling the API from Microsoft

2:55:34

2 часа 55 минут 34 секунды

learn catalog and then it also even encourages the user to click on those links if they want to have access to the course so that was a bit of brief about

2:55:42

2 часа 55 минут 42 секунды

how function calling Works to get the complete uh code example please check out the GitHub repo at the aka.ms Gen

2:55:51

2 часа 55 минут 51 секунда

beginners that you see here as well as the full course uh where we explain not only how to use function calling but all things also things like AI agents which

2:55:59

2 часа 55 минут 59 секунд

are very much relevant in this case thank you and good

Эпизод 12: Designing UX for AI Applications [Pt 12]

2:56:09

2 часа 56 минут 9 секунд

luck hi everyone this is Beth tumba and I'll be taking you through Lesson 12 of

2:56:16

2 часа 56 минут 16 секунд

the generative AI for beginnner curriculum in this lesson we'll be covering designing your user experience

2:56:24

2 часа 56 минут 24 секунды

for your AI applications our Focus will be first understanding what exactly user

2:56:31

2 часа 56 минут 31 секунда

experience is and then the user in US experience will be diving into what are their needs and how do we now build the

2:56:41

2 часа 56 минут 41 секунда

different components of ux around the user and lastly we'll dive into the specifics of how do you build your user

2:56:48

2 часа 56 минут 48 секунд

us experience for generative AI applications so let's dive in what is user experience user experience is the

2:56:56

2 часа 56 минут 56 секунд

entire Journey a user text when they're interacting your application it's from when a user comes in gets onboarded to

2:57:05

2 часа 57 минут 5 секунд

your application and performs a few tasks and then the offboarding of the user that entire process is experience

2:57:13

2 часа 57 минут 13 секунд

how does the user navigate around your product the main thing I've mentioned is the user so we should also have in mind

2:57:21

2 часа 57 минут 21 секунда

who this user is and what exactly their needs are in our scenario we'll be

2:57:28

2 часа 57 минут 28 секунд

creating a fixes educational chatboard and our users are two main users one is the students as a student might come

2:57:36

2 часа 57 минут 36 секунд

into the application and have it you help you as a tutor to write as and Report or come in and have the

2:57:45

2 часа 57 минут 45 секунд

application generate summar for you and other teacher you may come into the application and have it generate quizzes

2:57:52

2 часа 57 минут 52 секунды

for you or you may have pre-recorded videos and audios that you want to make accessible so how can the application

2:58:00

2 часа 58 минут

generate a transcript for you in the entire ux experience we have different

2:58:07

2 часа 58 минут 7 секунд

components that make up how your user interacts the product how do you make sure their experience is okay the first

2:58:14

2 часа 58 минут 14 секунд

thing is the usability of the product this means does the application function as it was intended to function does it

2:58:23

2 часа 58 минут 23 секунды

perform its intended purpose so for example if a if a teacher is coming in to generate quizzes does the quizzes are

2:58:31

2 часа 58 минут 31 секунда

the quizzes generated using the application the other thing is accessibility this means the application should be accessible to all regardless

2:58:40

2 часа 58 минут 40 секунд

of the different abilities and disabilities and it should also be accessible regardless of the language a

2:58:47

2 часа 58 минут 47 секунд

person uses that is if your application is meant to go Global and reach different users and

2:58:54

2 часа 58 минут 54 секунды

for us application is primarily Target to all teachers and students so we should be able to ensure it is accessible for all other thing is

2:59:03

2 часа 59 минут 3 секунды

reliability we've been able to see that usability is around does the application perform the function it intend it was

2:59:11

2 часа 59 минут 11 секунд

intended to perform reliability comes in when it consistently performs well performs a different function fun well

2:59:19

2 часа 59 минут 19 секунд

without any errors and then of course once your application checks all the boxes it should also be pleasant users

2:59:26

2 часа 59 минут 26 секунд

should be able to have fun using it it should be enjoyable and appealing to the different users that's about creating

2:59:35

2 часа 59 минут 35 секунд

your application but what about creating your specifically your AI applications the first thing you should be able to do

2:59:42

2 часа 59 минут 42 секунды

is ensure you're designing for trust and transparency so the question are you user might ask is does the response I'm

2:59:50

2 часа 59 минут 50 секунд

getting correspond to the question that I asked users need to be able to trust the application will deliver expected

2:59:59

2 часа 59 минут 59 секунд

results and they should do this consistently and accurately especially an application that is bound to impart

3:00:08

3 часа 8 секунд

knowledge to the Next Generation building trust is critical as it ensures that the user is confident with the

3:00:15

3 часа 15 секунд

application that it will get the work done and deliver the results transparency comes in when you're able to also share with the users this is the

3:00:24

3 часа 24 секунды

data we collected and this is how we able to use your data the key things around trust is ensuring the application

3:00:32

3 часа 32 секунды

gets the work done it is reliable it gets the work done over and over again and the results are able to match what

3:00:40

3 часа 40 секунд

the user means the two risks when it comes to trust that is over trust and mistrust over trust is when I user is

3:00:48

3 часа 48 секунд

very overconfident in the AI capabilities and they trust it too much to the extent they they do not even

3:00:56

3 часа 56 секунд

verify they just summarize and then go ahead and give the quiz to the students and stuff like that that is an issue because generative AI is

3:01:05

3 часа 1 минута 5 секунд

not 100% perfect all the time you a user should be able to come in and authenticate that what was produced

3:01:14

3 часа 1 минута 14 секунд

by the AI is actually true other thing is mistrust a user can come from the background of this is AI I don't trust

3:01:23

3 часа 1 минута 23 секунды

what AI does so those two are very opposite sides of the poll and we want the user to come back and Trust the

3:01:31

3 часа 1 минута 31 секунда

application so how do you calibrate trust there are two main ways you can calibrate TR the first thing is explainability

3:01:40

3 часа 1 минута 40 секунд

explainability is how does the application work does the user understand what the application work does the user understand what they're

3:01:48

3 часа 1 минута 48 секунд

doing in the application the first thing is of course in the onboarding when I come into your application am I able to

3:01:55

3 часа 1 минута 55 секунд

know this is what the tutor does so for example for application it's welcome on board to your AI tutor and it doesn't

3:02:04

3 часа 2 минуты 4 секунды

really give you an idea of okay this is an AI tutor but what can it do what does it do if you TR it a little bit

3:02:12

3 часа 2 минуты 12 секунд

different it tells you get personalized a tutoring for any subject it now gives you a clearer idea of what exactly the

3:02:21

3 часа 2 минуты 21 секунда

application does the other thing is ensuring your explanations as a and simple ensuring anyone regardless of

3:02:30

3 часа 2 минуты 30 секунд

their background can be able to understand what exactly the application does so for example in this example we

3:02:38

3 часа 2 минуты 38 секунд

have a chatboard saying hey Bethany I use a neural network process information and generate

3:02:46

3 часа 2 минуты 46 секунд

responses I might have the question what exactly is a NE Network right you might even not know even if you're Inta you

3:02:54

3 часа 2 минуты 54 секунды

might not even know what exactly a neural network is but if you phrase it differently hey be I am a computer

3:03:01

3 часа 3 минуты 1 секунда

program that can answer your questions and help you learn new things but I'm not a real person that's a different phrasing of the sentence and it's more

3:03:10

3 часа 3 минуты 10 секунд

clearer regardless of what the background the person is coming from the other bit around explainability is how are you you able to interact with the

3:03:19

3 часа 3 минуты 19 секунд

users depending on the access they have for example if it's an AI tutor and a much student coming into the application

3:03:27

3 часа 3 минуты 27 секунд

I willn't expect it to give me responses and give me answers if I ask it a question immediately it should be able

3:03:35

3 часа 3 минуты 35 секунд

to help me answer the questions that I have for example in this student is has a mathematical problem and comes in and

3:03:42

3 часа 3 минуты 42 секунды

ask hey can you give me the answer to this and the a is like yeah this is the answer that's not right what you should

3:03:50

3 часа 3 минуты 50 секунд

have your application do is instead tutor the student so for example student comes in can you give me the answer to

3:03:57

3 часа 3 минуты 57 секунд

this and the response from the AI is hey there's a cool tool that you can use to solve the equation which is a quadratic

3:04:05

3 часа 4 минуты 5 секунд

formula and this is how it goes so on and so forth it's now acting more a teure versus acting as an answering

3:04:13

3 часа 4 минуты 13 секунд

machine the other thing around trust the second thing is control users should be able to have a station level of control

3:04:22

3 часа 4 минуты 22 секунды

over their AI application this means you should be able to control how exactly

3:04:28

3 часа 4 минуты 28 секунд

the application responses responses to your questions for example the co-pilot

3:04:34

3 часа 4 минуты 34 секунды

extension on Microsoft age has a very good tool when it comes to compose

3:04:41

3 часа 4 минуты 41 секунда

whereby I can write a question give me py pan phone a generative a chat board

3:04:48

3 часа 4 минуты 48 секунд

and I can be able to use controls to say yeah I want it to be funny I want you to give me ideas of it and medium length

3:04:57

3 часа 4 минуты 57 секунд

and even when it gives me a response because yeah what do you call an a that makes art a Picasso which is very

3:05:04

3 часа 5 минут 4 секунды

interesting it will also tell me give me room to be able to go in and edit okay

3:05:11

3 часа 5 минут 11 секунд

can you send me more or you can even add in your own suggestions like are not funny can you make them funny or

3:05:20

3 часа 5 минут 20 секунд

something of that sort this gives a user control over what responses you're getting from your AI

3:05:27

3 часа 5 минут 27 секунд

application now we've talked about trust but then the other bit is you've been able to trust that this application

3:05:34

3 часа 5 минут 34 секунды

delivers exactly what it should be delivering but then how do you give feedback when an error occurs how does

3:05:42

3 часа 5 минут 42 секунды

the user collaborate with the AI application to ensure the feedback is given and you're also ensuring you're

3:05:50

3 часа 5 минут 50 секунд

able to improve your user experience so you should be able to design for collaboration and feedback the first thing is creating a feedback

3:05:58

3 часа 5 минут 58 секунд

loop a feedback loop allows users to suggest different improvements and suggestions they might have for the AI

3:06:06

3 часа 6 минут 6 секунд

output for example you can have a thumbs up and a thumbs down for the feedback loop so if the response is good thumbs

3:06:14

3 часа 6 минут 14 секунд

up if it's bad thumbs down and you can be able to go ahead and even add more features like if a user says thumbs down

3:06:23

3 часа 6 минут 23 секунды

can ask okay can you give feedback why is it bad and so on and so forth these features allow a user to come back and

3:06:31

3 часа 6 минут 31 секунда

collaborate and give feedback on the application the other bit is error handling error handling is in case the

3:06:38

3 часа 6 минут 38 секунд

application does not do as expected how do you handle errors so for example a student comes in and asks what is the

3:06:46

3 часа 6 минут 46 секунд

meaning of life as an AI application that's been trained on just different subjects you might be cautious to say

3:06:55

3 часа 6 минут 55 секунд

this is the meaning of life so instead the application should come back and say hey sorry I've only been trained with data on history and maap I cannot be

3:07:04

3 часа 7 минут 4 секунды

able to respond to the question you asked this helps handle any errors that come up so you should be able to figure

3:07:12

3 часа 7 минут 12 секунд

out the entire scope of your application how do the students interact with the applications how do the teachers interact with the application and how

3:07:20

3 часа 7 минут 20 секунд

can you be able to handle in case an error happens yeah and of course as a good teacher I will also leave you with an

3:07:28

3 часа 7 минут 28 секунд

assignment if you have built if you have already built an AI application the the objective will be how can you be able to improve the user

3:07:37

3 часа 7 минут 37 секунд

experience of that application for example you can say how do you make it

3:07:43

3 часа 7 минут 43 секунды

more pleasant how do you word your error messages how does the user explore the application do you give room for users

3:07:52

3 часа 7 минут 52 секунды

to to have control in the application so you can go back look over the different items I've mentioned create a checklist

3:08:00

3 часа 8 минут

and see ases your application check all the boxes and yeah that will be your assignment for

3:08:07

3 часа 8 минут 7 секунд

today thank so much and in conclusion designing the user experience of the AI application does not only require it to

3:08:15

3 часа 8 минут 15 секунд

be functional accessible reliable and pleasant but you should also be able to think about how are you building trust

3:08:22

3 часа 8 минут 22 секунды

with the users and also how do you fer collaboration and feedback to ensure your application is continually

3:08:29

3 часа 8 минут 29 секунд

improving and the users have a positive experience thank you so much and

Эпизод 13: Securing Your Generative AI Applications [Pt 13]

3:08:41

3 часа 8 минут 41 секунда

goodbye hi I'm Corey sted Place part of the AI Cloud a team here at Microsoft

3:08:49

3 часа 8 минут 49 секунд

and I have the absolute pleasure of delivering lesson number 13 yes lucky number 13 to you covering securing your

3:08:57

3 часа 8 минут 57 секунд

generative AI applications and if you have the right security strategy luck you don't need luck on your side you

3:09:05

3 часа 9 минут 5 секунд

have a good plan in place and that's what we're going to discuss today so just to do a bit of introduction this lesson is going to

3:09:12

3 часа 9 минут 12 секунд

cover security within context of AI systems what are the common risks and threat that you need to look at when you're building generative AI

3:09:21

3 часа 9 минут 21 секунда

applications and just methods and considerations for securing these systems or these applications that you're de

3:09:28

3 часа 9 минут 28 секунд

developing so the learning goals so we're going to examine the threats and risk that you have against your AI

3:09:35

3 часа 9 минут 35 секунд

systems and applications we're also going to look at methods and practices that you can put in place to secure against those risk and lastly how you

3:09:43

3 часа 9 минут 43 секунды

can actually Implement and security testing to prevent any of these unexpected results and like I said so you can continue to have users trust and

3:09:52

3 часа 9 минут 52 секунды

have a working environment for your generative AI application so let's start with security and generative AI these two topics and

3:10:02

3 часа 10 минут 2 секунды

how do they relate to each other well the impact of generative AI cannot be said even more uh this this

3:10:10

3 часа 10 минут 10 секунд

diagram is a really good understanding of the market size of generative AI in terms of the applications uh that are

3:10:18

3 часа 10 минут 18 секунд

being built and you can already see when that we have more if we have more generative AI applications we should have more secure generative AI

3:10:27

3 часа 10 минут 27 секунд

applications and taking from this uh oasf list and OAS is a Authority in terms of cyber security there's actually

3:10:35

3 часа 10 минут 35 секунд

they have defined 10 uh significant threats or security challenges for large language model applications well we

3:10:43

3 часа 10 минут 43 секунды

won't go through all of these in this lesson uh you can check out the link below uh within the GitHub repo of this course so you can see all the details of

3:10:51

3 часа 10 минут 51 секунда

these threats but there's some that we will be covering things like prompt injection over Reliance on a Model as

3:10:58

3 часа 10 минут 58 секунд

well as U you know training dat data poisoning and even model denial of service we things that we also will

3:11:05

3 часа 11 минут 5 секунд

cover throughout this course and in particular in this lesson as well so now that we understand all of

3:11:13

3 часа 11 минут 13 секунд

the challenges that we have as application developers building with generative Ai and large language models let's look at specifically in details

3:11:21

3 часа 11 минут 21 секунда

these threats and risks that we have and lastly how can we circumvent them or mitigate them through direct correct

3:11:29

3 часа 11 минут 29 секунд

security practices so we'll look at the first one it's called prompt injection and you can kind of think this is uh using the idea

3:11:38

3 часа 11 минут 38 секунд

of prompts so prompt engineering but not for the intended behaviors of your application so you can actually we've

3:11:45

3 часа 11 минут 45 секунд

seen threats and attacks out there where they've used prompts to either extract sensitive information so this could be sensitive information that your

3:11:54

3 часа 11 минут 54 секунды

generative AI application integrates with or perform unwanted task so e throughout this course we will talk

3:12:01

3 часа 12 минут 1 секунда

about things like building a meta prompt or a system prompt and we've seen even attacks on those sorts of methods where

3:12:09

3 часа 12 минут 9 секунд

uh users can come in and almost trick the llm into doing things that it's not necessarily designed to do uh this can lead into things like responding with

3:12:18

3 часа 12 минут 18 секунд

bias or misinformation or even sending hateful content to our users uh largely because all of the security measures or safety measures that we put in place or

3:12:26

3 часа 12 минут 26 секунд

removed through these PR prompt injections and then lastly uh even exploiting the vulnerabilities of the AI models themselves large language models

3:12:35

3 часа 12 минут 35 секунд

still is a rather new technology and if we find vulnerabilities in the models themselves uh you can use uh attackers

3:12:43

3 часа 12 минут 43 секунды

can use prompts to find out and get unwanted unwanted consequences for your users next one we're talking about a

3:12:52

3 часа 12 минут 52 секунды

supply chain brone abilities and this is not supply chain in terms of shipping and things like that but I like to think of this as kind of like the

3:12:59

3 часа 12 минут 59 секунд

infrastructure that runs around your whole generative AI applications so there's things a lot of vulnerabilities perhaps in when you're using outdated

3:13:07

3 часа 13 минут 7 секунд

software there's many new tools out there in terms of being able to deliver generative AI applications and manage them well it's important as application

3:13:16

3 часа 13 минут 16 секунд

Developers uh to make sure that we're not using anything outdated that could have security vulnerabilities as well as uh insecure plugins and toolings we're

3:13:24

3 часа 13 минут 24 секунды

finding out more and more that when we hook these uh generative AI applications into other software systems to get

3:13:31

3 часа 13 минут 31 секунда

information and data it actually performs really well in terms of the user experience but we want to make sure that we're using the right plugins and toolings uh that does not create any

3:13:40

3 часа 13 минут 40 секунд

vulnerabilties in that as well and then lastly it's the idea of over Reliance when we over trust the lm's uh responses

3:13:49

3 часа 13 минут 49 секунд

and we put those responses in situations where they're prone either to uh having errors or inaccuracies because as we

3:13:58

3 часа 13 минут 58 секунд

have probably discussed it in other lessons as well large language models they are prone to either hallucinate or fabricate information at times and this

3:14:07

3 часа 14 минут 7 секунд

can lead to unworn consequences uh if we just take them as face value and we just leave them lead them to the negative consequences that they

3:14:15

3 часа 14 минут 15 секунд

present so now that we've looked at those challenges like how can we overcome them or build Out Security tests and systems uh to protect against

3:14:24

3 часа 14 минут 24 секунды

these CH these attacks so with the idea of prompt injection we really want to mitigate this whether that's invalidating the

3:14:33

3 часа 14 минут 33 секунды

input of the user so we're making sure that this isn't any um disruptive prompts or content filtering where we are making sure that the content that is

3:14:40

3 часа 14 минут 40 секунд

being sent to the users goes through a filter or even sanitizing response and request uh in the cases so that we're

3:14:48

3 часа 14 минут 48 секунд

making sure that this information is what we are expecting to send to the model and then largely it's about monitoring making sure that we're

3:14:55

3 часа 14 минут 55 секунд

logging users inputs as well as the responses uh and if we see any typical attacks even adding those users or that

3:15:03

3 часа 15 минут 3 секунды

information to certain watch list so we can make sure in the future to mitigate those harms next is supply chain ver abilities

3:15:12

3 часа 15 минут 12 секунд

so we always want to ensure that we're using the latest secure version and don't to say latest version because sometimes the latest version

3:15:19

3 часа 15 минут 19 секунд

unfortunately is not always the most secure but using the latest secure version or latest one deployed we also want to verify the plugins that we're

3:15:27

3 часа 15 минут 27 секунд

using or even build our own plugins if necessary and then verifying the model for correctness and completeness is an important step and then lastly through

3:15:35

3 часа 15 минут 35 секунд

the testing of what we call adversarial testing which is through AI red teaming where we actually challenging in creating scenarios where we might see

3:15:43

3 часа 15 минут 43 секунды

vulnerabilities in our applications and then finding out where we can improve upon and on the over Reliance standpoint

3:15:51

3 часа 15 минут 51 секунда

again this is all about over trusting the output of the model the first step is user education giving them the understandings of the limitations of the

3:15:58

3 часа 15 минут 58 секунд

model or where errors could occur is very important also verifying the output and monitoring them with various

3:16:06

3 часа 16 минут 6 секунд

monitoring tools that are available and then lastly testing and evaluation presenting not only a relevant prompts that you think of but also a very

3:16:14

3 часа 16 минут 14 секунд

diverse set of prompts uh towards the use case that you're building so you can see the types of outputs and responses that you get from the model is very

3:16:22

3 часа 16 минут 22 секунды

important in terms of how the user experiences driven after you've launched this into production so that wraps up this lesson

3:16:30

3 часа 16 минут 30 секунд

in terms of build building security applications or securing your generative AI applications you can get more information here in full the full course

3:16:38

3 часа 16 минут 38 секунд

at aka.ms gen gen AI beginners and keep building and keep building secure thank

3:16:46

3 часа 16 минут 46 секунд

you hey folks welcome back to Jour of AI for

Эпизод 14: The Generative AI Application Lifecycle [Pt 14]

3:16:56

3 часа 16 минут 56 секунд

beginners I am Pablo Lopez Global Cloud advocate in net and artificial intelligence here at Microsoft you folks

3:17:03

3 часа 17 минут 3 секунды

saw me twice already right so it's a pleasure to teach you folks again about J of AI and this time let's pick a a

3:17:11

3 часа 17 минут 11 секунд

more complex topic than the last times first so now I believe your folks a lot about J of AI your folks know how to

3:17:19

3 часа 17 минут 19 секунд

generate text your folks know how to use images your folks how to know a little bit of a little bit of fine tuni prompt

3:17:27

3 часа 17 минут 27 секунд

design you know a lot and even use AI functions yeah so now that we are coming

3:17:34

3 часа 17 минут 34 секунды

to the end part of the series I want to tell you a little bit about LM mops

3:17:42

3 часа 17 минут 42 секунды

right because here's the thing we talk about a lot of know theoretical right you talked about and how can use the

3:17:51

3 часа 17 минут 51 секунда

sports of all of your gen AI systems into new systems but you know that's not

3:17:58

3 часа 17 минут 58 секунд

always the case you need to develop systems you need to make them scale you need take care of a lot of Stu so now

3:18:07

3 часа 18 минут 7 секунд

you know how to use you know operations how real operations work with llms and

3:18:14

3 часа 18 минут 14 секунд

language systems what we cover today we're going to cover llm Ops llm life

3:18:21

3 часа 18 минут 21 секунда

cycle Azure AI tooling and evaluation and what we're going to learn we're going to understand the paradigm shift

3:18:28

3 часа 18 минут 28 секунд

that happened between mlops and LM Ops the llm life cycle toing metrification

3:18:34

3 часа 18 минут 34 секунды

and evaluation let's start very simple let far before llms right before LMS

3:18:43

3 часа 18 минут 43 секунды

became more mainstream so we had a lot of melops right which is machine learn operations so we had to a lot of machine

3:18:52

3 часа 18 минут 52 секунды

learn operations to take all models in great shape so we had a lot of you know very technical people dealing with

3:19:00

3 часа 19 минут

constantly you have you have your data scientist you have to have people that knew a lot of the machine learn self to understand how these operations are

3:19:09

3 часа 19 минут 9 секунд

going so we have to have a lot of technical people as was not that accessible and if you didn't if work a

3:19:16

3 часа 19 минут 16 секунд

very technical person you have a lot of difficulties to understand how to maintain a you know a tool chain complete for you know machine learn

3:19:24

3 часа 19 минут 24 секунды

operations but then we had llms and the cool part about llm is that they simplified a lot of tasks that were

3:19:31

3 часа 19 минут 31 секунда

really hard for machine learning operations especially now with trt engineering a little bit of you know the rock Pon so we have a bunch of new

3:19:41

3 часа 19 минут 41 секунда

things that now you can learn that you can apply to your llmo so if you know a little bit about uh retried augmented

3:19:49

3 часа 19 минут 49 секунд

generation we're going to see on the next lessons so let's talk about this paradigm shift so let's start with the

3:19:57

3 часа 19 минут 57 секунд

traditional ml so we have a lot of ml Engineers data scientists and what they show was about the model the data the

3:20:04

3 часа 20 минут 4 секунды

environments and we had only one metric accuracy and a lot of those machine learn models you have to build from

3:20:11

3 часа 20 минут 11 секунд

scratch now we have llm Ops and the good part about llm Ops is that now not just reserved for those ml engineers and data

3:20:20

3 часа 20 минут 20 секунд

scientists we have as well our app developers so now everyone can join and trying to do a better AI solution for

3:20:28

3 часа 20 минут 28 секунд

everyone and the assets change of course you should have model data Etc but now it's easier to manipulate so have your

3:20:36

3 часа 20 минут 36 секунд

llms your agents your plugins your prompts your chains and your apis remember when I said we said a lot about Azure AI so that's the thing I want to

3:20:45

3 часа 20 минут 45 секунд

show you is to demonst rate how much now we can change more easily to have access to those AI Solutions into your

3:20:54

3 часа 20 минут 54 секунды

applications and not only that for metrics now I have a lot more metrics and you may ask why it's because of AI

3:21:01

3 часа 21 минута 1 секунда

effects now of the power of those big language models we need to much more about how it's being used so we have

3:21:10

3 часа 21 минута 10 секунд

what quality with this the same as accuracy right but have to a little bit about the similarity depending on your

3:21:17

3 часа 21 минута 17 секунд

we have our biases right so it need to take care of the harm that it can take so the bias and toxicity of the responses it has to be honest it has to

3:21:26

3 часа 21 минута 26 секунд

be a some ground level to get correct information so I need a Cress and I need

3:21:33

3 часа 21 минута 33 секунды

to take care of the cost and the latency the cost being the to token for request and the latency be the response time and

3:21:41

3 часа 21 минута 41 секунда

response seconds or PS so here I have as well on the B the base of the EML models

3:21:48

3 часа 21 минута 48 секунд

you can see it's prebuilt it's sign tuned to serve as API it's a model as a service that's why the a a here so you

3:21:56

3 часа 21 минута 56 секунд

see here that now we're changing a lot of paradigms now even app developers can participate into a AI enabled platform

3:22:05

3 часа 22 минуты 5 секунд

and it's not only this right because right now the life cycle is changing a lot because you must remember that

3:22:14

3 часа 22 минуты 14 секунд

before this now we need you understand if you are an app developer how to make an LM cycle in the real world so what is

3:22:23

3 часа 22 минуты 23 секунды

going on here we have here the classics the base of all our AI driven needs which is the business need remember all

3:22:32

3 часа 22 минуты 32 секунды

solutions need a business reason to exist so we always need to get a business needed to apply your AI

3:22:39

3 часа 22 минуты 39 секунд

solution so after this we're going to apply this into the IDE exploring so I need to do hypothesis

3:22:47

3 часа 22 минуты 47 секунд

trying to find new models and llms or even slms depending on the scope of your solution then you're going to try prompt

3:22:54

3 часа 22 минуты 54 секунды

engineering our way to get good accuracy after this we need to build an Argent our Solutions so then we going to do now

3:23:03

3 часа 23 минуты 3 секунды

a more advanced prompt engineering or fine tuning or even both you can going to use evaluation to see if our

3:23:10

3 часа 23 минуты 10 секунд

Solutions are scaling giving right answers and understanding how it's performing under the test

3:23:17

3 часа 23 минуты 17 секунд

to handle exceptions and have especially retrieval augmented generation which is a P that is trying to get answers from

3:23:26

3 часа 23 минуты 26 секунд

documents that you insert if you have any doubts about it check our gent AI playlist that you're going to have an episode of retrieval AED generation so

3:23:36

3 часа 23 минуты 36 секунд

after this imagine that all steps go through with building your Solution that's great now I need to operationalize so basically now you're

3:23:44

3 часа 23 минуты 44 секунды

going to apply the basics of all operations so I need to take care of the quota and cost manager of your AI

3:23:51

3 часа 23 минуты 51 секунда

Solutions and llms need to take care of the monitor the safe roll out the content filtering and the deployment of

3:23:58

3 часа 23 минуты 58 секунд

this app or UI so everything will be need to be operationalized to take care of everything that you need for your

3:24:06

3 часа 24 минуты 6 секунд

solution so you see that you have three steps and these steps can go forwards and backwards basically you're going to

3:24:14

3 часа 24 минуты 14 секунд

advance projects prepare apps for development but if you want a new version you can like revert to new ideations of

3:24:21

3 часа 24 минуты 21 секунда

Explorations or even get back from feedback from the operations and building again into your new solution

3:24:28

3 часа 24 минуты 28 секунд

here you can see a more complex infographic of everything here we have so we have here like to identify the business user case to connect the data

3:24:37

3 часа 24 минуты 37 секунд

build your prompt flow if you have doubts what is promp flow I going to show very soon develop prompt flow based

3:24:44

3 часа 24 минуты 44 секунды

on the prompt St to see if it's joing correct and that the data that you have can work perfectly with the flows that

3:24:52

3 часа 24 минуты 52 секунды

you have then you're going to do testing it's a lot of test in the second part so you have to run tests evaluate if the

3:24:59

3 часа 24 минуты 59 секунд

promp goes and it can modify or not after this you if everything goes well

3:25:06

3 часа 25 минут 6 секунд

you can at least go forward if not you can go backwards as always like you can go and the end point if not try to

3:25:15

3 часа 25 минут 15 секунд

modify a flow get you better results so after it got great results it can always

3:25:22

3 часа 25 минут 22 секунды

deployer endpoint add monitoring and integrated your application but I want some more

3:25:29

3 часа 25 минут 29 секунд

examples do Microsoft has some examples on having a whole flow for sure let's take a look on it so here we have a

3:25:37

3 часа 25 минут 37 секунд

perfect sample we already have cont chat cont chat has a lot of the features that you're looking for so here you have an l

3:25:46

3 часа 25 минут 46 секунд

M which is easy deployed with Azure scli and has a lot of llm use cases so here

3:25:53

3 часа 25 минут 53 секунды

you have a lot of the learn objectives so if you want to understand rag you have to take a look here to build run

3:26:00

3 часа 26 минут

evaluate and deploy your rag based llm app so now we need to understand how you're goingon to evaluate right because

3:26:08

3 часа 26 минут 8 секунд

I talk a lot about testing and testing with llms is usually a harder test than you usually know so let's take a look on

3:26:16

3 часа 26 минут 16 секунд

how we evaluate internally so on Kota chat we have this folder called eval take a look here then it can have a lot

3:26:25

3 часа 26 минут 25 секунд

of IPython notebooks to see how it works so here it is a non-python notebook talking about how to evaluate ground

3:26:33

3 часа 26 минут 33 секунды

this so here you have a question a customer ID and an output the customer

3:26:40

3 часа 26 минут 40 секунд

ID here it refers to a a specific client so then you're going to use PF client which is from pront flow pront flow is

3:26:48

3 часа 26 минут 48 секунд

our tool application to make flows easier what is a flow you may ask a flow

3:26:55

3 часа 26 минут 55 секунд

and promt flow means that we know which process it goes from question to answer

3:27:02

3 часа 27 минут 2 секунды

in which points of the code touches so what is retrieving what is getting from the database um which points of the code

3:27:10

3 часа 27 минут 10 секунд

it is executing to get the correct answer so here we have front flow here apply into Cod so here goes the flow and

3:27:19

3 часа 27 минут 19 секунд

then goes to the input then I get an output and the good part is that promp flow has a test so it can get the

3:27:27

3 часа 27 минут 27 секунд

question the context and the answer and then it get to zero to five into the gring five being five the best and zero

3:27:35

3 часа 27 минут 35 секунд

the worst then not only can try to evaluate on on just ground this it can evaluate a lot of things it can evaluate

3:27:44

3 часа 27 минут 44 секунды

the question between all those point that I tou it is harmful it is grounded it is correct remember always not always

3:27:53

3 часа 27 минут 53 секунды

being grounded be correct and if the answer makes sense because yes it can answer correctly imagine that I say the

3:28:01

3 часа 28 минут 1 секунда

guarantee is 60 days however imagine that 60 days is not guaranteed okay it

3:28:09

3 часа 28 минут 9 секунд

got the information correctly but then wrote it wrong so sometimes need take care on how it answers not only you need

3:28:16

3 часа 28 минут 16 секунд

to pass the information but you has to complement it and you need to take care if it's getting correct and you can do a

3:28:23

3 часа 28 минут 23 секунды

bat run to do a bunch of questions to try to if everything is run correctly so these are the some of the parts you can

3:28:31

3 часа 28 минут 31 секунда

do but we have a lot more please take a look on cont chat on Azure samples and

3:28:38

3 часа 28 минут 38 секунд

if you want more versions We have more versions here on GitHub so thank you so much for joining

3:28:47

3 часа 28 минут 47 секунд

us in this new episode of generative AI for beginners if you want to know more you can always access our resources on

3:28:55

3 часа 28 минут 55 секунд

Microsoft's learn and not only that we have talks just we had like this on Microsoft ignite and Microsoft build

3:29:02

3 часа 29 минут 2 секунды

take a look on how we Implement rug Solutions into this operations new world thank you so much and I hope to see you

3:29:09

3 часа 29 минут 9 секунд

soon hi everyone welcome to the generative AI

Эпизод 15: Retrieval Augmented Generation (RAG) and Vector Databases [Pt 15]

3:29:20

3 часа 29 минут 20 секунд

for beginners curriculum I am bethan chumba and I'll be taking you through lesson 15 that is retrieval argumented

3:29:28

3 часа 29 минут 28 секунд

generation and Vector data builds let get started in this lesson we'll cover why

3:29:36

3 часа 29 минут 36 секунд

exactly you need R why you even need to care about it talk about the components of R and we'll show you how you can be

3:29:45

3 часа 29 минут 45 секунд

able to build a full rag application before we conclude the session in our scenario we'll be

3:29:53

3 часа 29 минут 53 секунды

using aopi as our LM then we'll be using data from the AI for beginners

3:30:00

3 часа 30 минут

curriculum the lesson around neural networks and we'll have a search and a

3:30:06

3 часа 30 минут 6 секунд

cosmos DB for our database and search index currently our llms have a couple of limitations for example the

3:30:15

3 часа 30 минут 15 секунд

limitation around knowledge around current events if you go in and ask is que elizabe the second alive the a model

3:30:23

3 часа 30 минут 23 секунды

will tell you as from my last update on October 2021 yes she was but I do not have fing

3:30:31

3 часа 30 минут 31 секунда

data the other thing is around your own personal data so you it was trained using publicly available data so if I

3:30:39

3 часа 30 минут 39 секунд

want to ask what is the price of kaks from a specific store it will tell me I'm sorry I an model I cannot tell you

3:30:47

3 часа 30 минут 47 секунд

the real time priv of specific St the other limitation is around the context provided as well as

3:30:54

3 часа 30 минут 54 секунды

data that responses generated might not be rooted in fact with this limitations in mind we have the solution of using

3:31:04

3 часа 31 минута 4 секунды

retrieval agumented generation this is whereby you add supporting information to an prompt to give it more context and

3:31:12

3 часа 31 минута 12 секунд

knowledge so that when you go to the llm it can give you respons based on the data provided how it works

3:31:20

3 часа 31 минута 20 секунд

is a rug application acts whereby a user asks a question and the application queries data from a knowledge base

3:31:29

3 часа 31 минута 29 секунд

adding the data as well as your query through the prompts that you query to the model then once you get the results

3:31:37

3 часа 31 минута 37 секунд

from the model it's both a combination of your data as well as the user promt a user asked so regardless where whether

3:31:46

3 часа 31 минута 46 секунд

person is asking questions around prices of items in your store or prices of

3:31:53

3 часа 31 минута 53 секунды

personal data for example if you have your own data on Microsoft Word and you want responses retrieval argumented

3:32:00

3 часа 32 минуты

generation can com in and help you argument your responses with personal data and generate more better and ssten

3:32:09

3 часа 32 минуты 9 секунд

responses the components of a rag include one a knowledge bit whereby the data is stor and can be able to retrieve

3:32:17

3 часа 32 минуты 17 секунд

the data a user query when once a user asks a question and then the retrieval system when now you build an entire

3:32:25

3 часа 32 минуты 25 секунд

system that can be able to go INRI relevant information argument it to the prompt provided and generate a response

3:32:34

3 часа 32 минуты 34 секунды

based on the data retried in this scenario you have heard about the knowledge P but then how do you store

3:32:41

3 часа 32 минуты 41 секунда

your knowledge base you use a vector dat base a vector dat base is is unique in that it can be able to store embedded

3:32:49

3 часа 32 минуты 49 секунд

vect not just storing documents as they are but it also has numerical representations of

3:32:58

3 часа 32 минуты 58 секунд

your document to be able to now interact with large language model once you've been able to have all

3:33:05

3 часа 33 минуты 5 секунд

these things in place we can go ahead and create our dark application the first thing of course is ensuring we have our knowledge based ready so we can

3:33:14

3 часа 33 минуты 14 секунд

create our AA Cosmos be able to to our data once you have your database the next thing is you have

3:33:22

3 часа 33 минуты 22 секунды

your data your data made be long paragraphs for example if you have a book and you might want to split it into

3:33:29

3 часа 33 минуты 29 секунд

short passages to be able to have the llm easily retrieve the data as well as reducing the cost in terms of the tokens

3:33:38

3 часа 33 минуты 38 секунд

passed to your llms so the next the next thing you do once you have your data is to break it down the ch for is rual next

3:33:48

3 часа 33 минуты 48 секунд

thing is now embeddings embeddings are encoded data format that you can be able

3:33:55

3 часа 33 минуты 55 секунд

to use as input to your data to your application so the next thing once you have your chance is to convert the

3:34:03

3 часа 34 минуты 3 секунды

chunks to embedding converting the chunks to embedding enables you to of course also have high retrievable speed

3:34:11

3 часа 34 минуты 11 секунд

as well as being able to easily find the similarities between different Tong in our scenario we'll be using the T

3:34:19

3 часа 34 минуты 19 секунд

embedding .002 the second model to be able to embed our data you can use other Vector

3:34:27

3 часа 34 минуты 27 секунд

embeddings such as word to work be able to do your embedding so you can go on around what are the different embedding

3:34:35

3 часа 34 минуты 35 секунд

tools I can be able to use and how do I make how do I ensure it's the right one for my application once you have your

3:34:42

3 часа 34 минуты 42 секунды

embeddings you now want to be able to get which are similar to The Prompt provided as we said what you're doing is

3:34:50

3 часа 34 минуты 50 секунд

argumenting your prompt with your data so you want to find the data that is most related to the text that you

3:34:58

3 часа 34 минуты 58 секунд

provided so once you have your text you will go back to your data and be able

3:35:05

3 часа 35 минут 5 секунд

to have similarity assign to your data to your vectors ensuring that you can be

3:35:12

3 часа 35 минут 12 секунд

able to find words that are closely related in document we can do this of course by creating also a sear index

3:35:20

3 часа 35 минут 20 секунд

once been able to create you been able to figure out how similar your words are you can go ahead and create a seex to be

3:35:29

3 часа 35 минут 29 секунд

able to now go in and retrieve Chun that similar and now you can be able to go in

3:35:36

3 часа 35 минут 36 секунд

and embed your prompt with related CH but then the question might be okay you have probably your data spread across

3:35:45

3 часа 35 минут 45 секунд

different chance probably you might have one that's very closely related another that's not closely related so you would

3:35:53

3 часа 35 минут 53 секунды

want to come in again and ensure you are able to rank them in order of relevance to be able to now get such results that

3:36:01

3 часа 36 минут 1 секунда

are most relevant to be able to be chunked together to be able to be retrieved together with your prompt this

3:36:08

3 часа 36 минут 8 секунд

ensures that the most reliable data the most the data that you most closely related to your prompt is now run on

3:36:17

3 часа 36 минут 17 секунд

top you can also do this as well with your code by creating a rerun card be able to now rank the chance okay these

3:36:25

3 часа 36 минут 25 секунд

are the chance close Che the question and so on and so forth once you've been able to go in and create your ranker

3:36:33

3 часа 36 минут 33 секунды

you've been able to create your search index you want to bring everything together into an application and get a

3:36:40

3 часа 36 минут 40 секунд

response so for example in our code the first thing is the user input so user might ask based on the data what is a

3:36:48

3 часа 36 минут 48 секунд

perception and then we have our chatboard created you quer f the embeddings that have been created you

3:36:55

3 часа 36 минут 55 секунд

create an embedding of first what is a perception once you've been able to create your embeddings you go in and

3:37:01

3 часа 37 минут 1 секунда

find which in your database which data is closely related to the embedding of the question once that's done you can be

3:37:10

3 часа 37 минут 10 секунд

able to upend that to the user input and now the question that's going into to the llm is both your question the users

3:37:19

3 часа 37 минут 19 секунд

and as well as the data that you've been able to retrieve this is just a API call to be able to now come in use open a to

3:37:27

3 часа 37 минут 27 секунд

be able to generate responses based on your question and from the response you can see it gives you a response of

3:37:35

3 часа 37 минут 35 секунд

perceptron is the type of artificial intelligence neural network model and so on and so forth you can be able to also add other features to your application

3:37:43

3 часа 37 минут 43 секунды

such as for example you also retrieve the document or the exact Channel whereby I can be able to find the

3:37:52

3 часа 37 минут 52 секунды

question that has been asked as well as the content that we've been able to add on top to now get an clear picture of

3:38:00

3 часа 38 минут

what exactly what point of your data exactly did you get the response from and that's it you've been able to build your R

3:38:08

3 часа 38 минут 8 секунд

application but then the question might be okay You' built it but how do you ensure that your application is actually working

3:38:16

3 часа 38 минут 16 секунд

in the same way that you intend to work we have three different evaluation metrics that you should look into one is

3:38:23

3 часа 38 минут 23 секунды

groundedness to be able to evaluate did the response come from the documents you supplied or was it just random responses

3:38:31

3 часа 38 минут 31 секунда

so she'll be able to go back in and check what responsibil you get and how do they match with the data you provided

3:38:39

3 часа 38 минут 39 секунд

the are things relevance in terms of we were able to rank our data in terms of the most relevant based on the

3:38:47

3 часа 38 минут 47 секунд

similarity of the vectors but then you also want to ensure that that what is the most relevant that the most relevant

3:38:54

3 часа 38 минут 54 секунды

data we will use then the last thing is coherence coherence is around how fluent or how Clos natural language did the tax

3:39:03

3 часа 39 минут 3 секунды

retrieve some and that's it of course I will leave you as an assignment and I want you to continue learning about rag

3:39:12

3 часа 39 минут 12 секунд

continue building on top of what you've learned so I'll leave you with two tasks first of all the first task is can you

3:39:19

3 часа 39 минут 19 секунд

be able to build a front end for the application and be able to have users actually interact with your rag

3:39:27

3 часа 39 минут 27 секунд

application the next thing is are you able to utilize a framework to recreate your application make it more simpler or

3:39:34

3 часа 39 минут 34 секунды

even use other tools like as you've seen I've been able to create the search index from from scratch I was able to

3:39:42

3 часа 39 минут 42 секунды

create a such index but then we have other application such as a a suchar that can be able to do all this without

3:39:50

3 часа 39 минут 50 секунд

you being able to create from scratch so you can also explore all those other options and with that thank you so much

3:39:57

3 часа 39 минут 57 секунд

for joining in and have a good day

3:40:07

3 часа 40 минут 7 секунд

bye hi I'm Corey seared pace and I'm part of the AI Cloud aacy team here at Microsoft and I have the pleasure of

3:40:15

3 часа 40 минут 15 секунд

presenting to you lesson number 16 of our generative AI for beginners course covering working with open source models

3:40:22

3 часа 40 минут 22 секунды

in this lesson we're going to cover what exactly are open- Source models some of the benefits of why you would want to

3:40:29

3 часа 40 минут 29 секунд

use open source models and also understanding where we can find the different open soured models that are available to build our

3:40:36

3 часа 40 минут 36 секунд

applications we also have some learning goals here we want to understand the difference between these open source models when helping us determine which

3:40:44

3 часа 40 минут 44 секунды

ones to use how to actually use these in an application and where to find more detail about these open source models that are available so what are exactly

3:40:53

3 часа 40 минут 53 секунды

open source models the standard definition that we sort of taking from open- Source software would put this

3:41:00

3 часа 41 минута

category of that all this information when we were talking about large language models whether it's the training data being publicly available

3:41:09

3 часа 41 минута 9 секунд

the full model weights that were you for training the evaluation code that was also used to evaluate the training as well as fine-tuning the model the

3:41:17

3 часа 41 минута 17 секунд

training metrics that we determine during that process and then last but most importantly is also an open source license in terms of being able to use

3:41:27

3 часа 41 минута 27 секунд

this uh as a developer uh freely without any sort of restrictions this is the sort of criteria that uh an open source software

3:41:36

3 часа 41 минута 36 секунд

would have if you translate that over to open source models if we look at the available models that are out there now

3:41:43

3 часа 41 минута 43 секунды

there's actually only a few models that sort of fit all of these criterias perfectly one series of models that are

3:41:50

3 часа 41 минута 50 секунд

is worth looking at is uh the olmo models from Allen AI olmo Oro is short

3:41:59

3 часа 41 минута 59 секунд

for actually open language models H and these models are like I mentioned a series of models the most latest one is

3:42:07

3 часа 42 минуты 7 секунд

7 billion parameter open llm uh which is compar comparable to or even out performs in some metrics with llama 2 uh

3:42:15

3 часа 42 минуты 15 секунд

which is a 13 billion uh parameter model uh you would also see available the data set that was used to train on which is

3:42:22

3 часа 42 минуты 22 секунды

the domal data set uh a data set that has three trillion tokens uh and it contains a lot of information in terms

3:42:29

3 часа 42 минуты 29 секунд

of both code content whether that be web content and books whether that be publicly available books or even public

3:42:36

3 часа 42 минуты 36 секунд

uh Publications as well if you are interested you can see the evaluation and fine-tuning code that was involved

3:42:43

3 часа 42 минуты 43 секунды

in this process but I mentioned this is a you know a prime example of where a model can fit all that criteria for a

3:42:53

3 часа 42 минуты 53 секунды

probably be calling open source models where the community has sort of focused on lately is this world of open models

3:43:00

3 часа 43 минуты

where they might fit some of the criteria but maybe not all of their criteria that if we were to translate directly into what open source software

3:43:07

3 часа 43 минуты 7 секунд

is and this is where you primarily see a lot of either the model hosting or model providers out there whe that's some C

3:43:15

3 часа 43 минуты 15 секунд

coher meta or even a a hugging face which actually hosts these models uh when we're talking about working with

3:43:22

3 часа 43 минуты 22 секунды

open model open models that are there so throughout this the rest of this course we're going to call this open models uh but this is interchangeable in terms of

3:43:30

3 часа 43 минуты 30 секунд

Open Source models if that's what you prefer so what are actually the benefits of using these open models well first they're highly customizable like I

3:43:39

3 часа 43 минуты 39 секунд

mentioned some of these models have open weights which that leads developers to be able to either fine-tune or alter their behavior which is very important

3:43:48

3 часа 43 минуты 48 секунд

when we're talking about creating these models for a specialized task whether that's speaking different languages speaking different programming languages

3:43:56

3 часа 43 минуты 56 секунд

or maybe performing uh different rule sets in terms of the way that these models operate and they're only being a

3:44:04

3 часа 44 минуты 4 секунды

available because of their open sourness also in the cost perspective essentially these models on a whole or

3:44:12

3 часа 44 минуты 12 секунд

averagely is more or cheaper than the proprietary models that are typically controlled by one organization whether that's be a cost per token when

3:44:20

3 часа 44 минуты 20 секунд

utilizing these models uh which is also contribute to both both the model size which has some flexibility in terms of being where being able to host it

3:44:29

3 часа 44 минуты 29 секунд

whether that's hosting it in a cloud or even working it locally on your machine and like I mentioned earlier

3:44:36

3 часа 44 минуты 36 секунд

it's the flexibility that Lots Prides these open source models with a lot of benefits we are seeing a lot now where

3:44:44

3 часа 44 минуты 44 секунды

applications are determining and working with a multimodel architecture meaning that maybe a certain model performs well

3:44:52

3 часа 44 минуты 52 секунды

on a specific task or is even specialized under that specific task and maybe that incorporates with either multiple open source models or an open

3:45:00

3 часа 45 минут

source model and let's say a proprietary model and with working with these open siiz models are essential because as mentioned uh because of the cost and

3:45:08

3 часа 45 минут 8 секунд

performance that they deliver uh is far uh adds a lot of benefits in terms of building application when we're talking

3:45:15

3 часа 45 минут 15 секунд

about scaling later on also flexibility is really getting the understanding of the task and their specialization how

3:45:22

3 часа 45 минут 22 секунды

they actually perform uh with your task whether it's summarization text generation code generation is another

3:45:30

3 часа 45 минут 30 секунд

really important part of working with these open source models and once you've understand that uh you can get great benefits of working with these models

3:45:37

3 часа 45 минут 37 секунд

for sure and then lastly it's Community uh we're going to talk about a bit more about hugging face later on uh but there's things like the hugging face Hub

3:45:46

3 часа 45 минут 46 секунд

uh where you actually get a lot of different diversity in terms of fine- tune models like as mentioned you can get a fine tune model that speaks uh

3:45:54

3 часа 45 минут 54 секунды

even a language that um specific languages are specialized in that and it's really this concept or this idea of innovation in numbers if everyone's sort

3:46:02

3 часа 46 минут 2 секунды

of contributing uh we have a lot more freedom in terms of innovating as well as the abilities to create new tasks new

3:46:11

3 часа 46 минут 11 секунд

specializations that might be overlooked by working with just proprietary model models so exploring different open

3:46:18

3 часа 46 минут 18 секунд

models is another very important question to answer because as mentioned there's many of them out there one way you can look at this work with this is

3:46:27

3 часа 46 минут 27 секунд

using the Azure AI Studio we actually have a model catalog built in with this that as I say here currently has 1,600

3:46:35

3 часа 46 минут 35 секунд

plus models I put the plus here because models are continuing to be added almost every week uh with the collection also includes the Microsoft research models

3:46:44

3 часа 46 минут 44 секунды

that are out there specifically the ones around even sar's small language models where we talk about cost and performance as another really good key the hugging

3:46:52

3 часа 46 минут 52 секунды

face models that are out there available mrw models which we'll talk a little bit more in details coher and meta are also

3:46:59

3 часа 46 минут 59 секунд

uh models that are available or parts of collections in this model catalog of the Azure studio so do check it out and you'll definitely get find the model

3:47:08

3 часа 47 минут 8 секунд

step or most appropriate for your application there speaking of those models that are available we're going to look at a a little bit more in depth

3:47:15

3 часа 47 минут 15 секунд

about a few that are available here uh first one we'll look at is llama 3 and llama 3 comes in uh essentially three

3:47:23

3 часа 47 минут 23 секунды

different model sizes or model flavors if you will uh first is the Llama 38b so 8 billion parameters you also have

3:47:31

3 часа 47 минут 31 секунда

available the Llama 370b uh which is 70 billion parameters as well as the instruct that uses it for chat

3:47:38

3 часа 47 минут 38 секунд

completions uh you will see this if you want to compare this to a proprietary model model it's comparable to a GP T4

3:47:45

3 часа 47 минут 45 секунд

and also performs zp4 on some task so again as an application Builder it's really important to understand those

3:47:52

3 часа 47 минут 52 секунды

tasks that it does outperform so and then you can Implement that within your application to get the best benefits and performance when using this model and

3:48:01

3 часа 48 минут 1 секунда

one of the strong suits is that llama 3 also operates or delivers fast image generation so if you were working with a

3:48:09

3 часа 48 минут 9 секунд

application that requires that llama 3 is worth uh working with or experimenting with within your application as well

3:48:16

3 часа 48 минут 16 секунд

well the next provider that we have is mrol mrol has three currently models open source models that are available in

3:48:23

3 часа 48 минут 23 секунды

the model catalog which is a 7B an 8X 7B and an NX uh the most recent one 8X

3:48:30

3 часа 48 минут 30 секунд

22b uh what's unique about the 8X 22b is that this has actually native function calling built-in which is the first Mr

3:48:38

3 часа 48 минут 38 секунд

model that has that available an open source license and that allows you to get essentially uh F allow the model to

3:48:46

3 часа 48 минут 46 секунд

call function with your application based on the user's inputs uh and actually then get those responses back and send that to the user so this

3:48:54

3 часа 48 минут 54 секунды

designs a very much a userfriendly experience that thought of just doing a chat application and expecting the response from the model what makes this

3:49:02

3 часа 49 минут 2 секунды

unique and why the cost for this is uh could be less than working with proprietary models it's Unique architecture which is this mixture of

3:49:11

3 часа 49 минут 11 секунд

expert architecture that allows uh essentially um a expert two expert neural networks

3:49:18

3 часа 49 минут 18 секунд

to be chosen at a time and perform the the given task uh at inference point and allows that model to run in a more

3:49:25

3 часа 49 минут 25 секунд

lightweight fashion compared to larger models that are available it also has things like Json and safe mode which controls has the gift developers a bit

3:49:34

3 часа 49 минут 34 секунды

more control on the responses that the model outputs and then lastly we look at the

3:49:41

3 часа 49 минут 41 секунда

hugging face models so in the world of hugging face there's currently 600,000 models available uh we won't talk about

3:49:48

3 часа 49 минут 48 секунд

all of them here obviously uh but one of the things I like to think about when working with hugging phase is this idea of maybe working with AI applications uh

3:49:57

3 часа 49 минут 57 секунд

sort of like Legos well there's so many models that are out there that do either General tasks in their multimodal models but also very excelling and very

3:50:05

3 часа 50 минут 5 секунд

specific task and if you make sure that you use these models in your application for those specific task um that you'll

3:50:13

3 часа 50 минут 13 секунд

get a lot better performance and a cost weight analysis there uh when you're using let's say a model that's really good at translating specific language

3:50:22

3 часа 50 минут 22 секунды

and then another model that's also really good at transcribing that specific language rather than using a relying on one model to do that as well

3:50:30

3 часа 50 минут 30 секунд

uh and like I mentioned earlier there's really a strong Community around Huggy face uh that gives you a lot of information about working with these

3:50:36

3 часа 50 минут 36 секунд

models whe whether it's the discussion the model cards that are available that gives you understanding of what these models are special at specialize that

3:50:44

3 часа 50 минут 44 секунды

how they perform and last mentioned a really strong Community around fine tuning as well from a um performance perspective so if you're looking for a

3:50:53

3 часа 50 минут 53 секунды

model to be fine tuned you most likely find it in Huggy face being available so that covers a brief and

3:51:00

3 часа 51 минута

working with open source models or open open models uh check out the full information of about this lesson um from

3:51:09

3 часа 51 минута 9 секунд

on the GitHub repo which is aka.ms genyen beginners as well as other lessons covering topics including like

3:51:18

3 часа 51 минута 18 секунд

the full application life cycle when working with generative AI applications which is an important part when we're talking about working with open source

3:51:26

3 часа 51 минута 26 секунд

models as they fit within that application life cycle thank you and good

Эпизод 16: AI Agents [Pt 17]

3:51:35

3 часа 51 минута 35 секунд

luck hi I'm Cory ster pce a cloud advocate here at Microsoft part of our AI Cloud advocacy team and I have the

3:51:43

3 часа 51 минута 43 секунды

pleasure of delivering to you lesson number 17 of our generative AI for beginners course covering AI

3:51:50

3 часа 51 минута 50 секунд

agents in this lesson we're going to cover a few things first we're going to answer the question of what exactly are

3:51:57

3 часа 51 минута 57 секунд

AI agents what are AI agent Frameworks how do they sort of work and what are the difference between them and when

3:52:04

3 часа 52 минуты 4 секунды

should you actually use an AI agent uh when building generative AI applications the learning goals of this

3:52:11

3 часа 52 минуты 11 секунд

this lesson is going to be explaining how AI agents work understanding the difference between some of the popular Frameworks out there and then how to

3:52:20

3 часа 52 минуты 20 секунд

design properly working with AI agents so what exactly are AI

3:52:27

3 часа 52 минуты 27 секунд

agents this is a very open definition of what AI agents are uh it means a lot to different people when they're sort of

3:52:34

3 часа 52 минуты 34 секунды

building with applications but to standardize this or to keep it really General we're going to understand that to for an AI AG to be defined you need

3:52:43

3 часа 52 минуты 43 секунды

to have one a large language model two some sort of state and then lastly tools so with a large language model

3:52:51

3 часа 52 минуты 51 секунда

essentially what I like to say it's sort of this Choose Your Own Adventure game with the large language model is trying to reason or decide on which tools to

3:52:59

3 часа 52 минуты 59 секунд

actually use um when you're working or interacting with users and then we have this idea of state which is really this

3:53:08

3 часа 53 минуты 8 секунд

the sort of the context of the conversation interaction with users or even another large language model and in terms of the past what it's been

3:53:16

3 часа 53 минуты 16 секунд

received and the present of what it's sort of planning to do next then it's also maintaining those particular results uh so that the user is getting

3:53:25

3 часа 53 минуты 25 секунд

the task they want to have completed or that information that they need and then when we talk about tools that could be any sort of external system whether it's

3:53:34

3 часа 53 минуты 34 секунды

a database uh an API uh even another large language model or maybe even just some code whether that's python function

3:53:42

3 часа 53 минуты 42 секунды

things like that that are used being utilized by the large language model or being interpreted by responses that the large language model should in the next

3:53:51

3 часа 53 минуты 51 секунда

process execute the function so now that we have a very general definition let's actually look

3:53:58

3 часа 53 минуты 58 секунд

at how different AI agent framework sort of implement this idea of large language model State and

3:54:06

3 часа 54 минуты 6 секунд

tools so in the case of Lang Chan who also has uh available features we have the large language model which can be

3:54:14

3 часа 54 минуты 14 секунд

defined very simply as whatever sort of model that's available or what you to be using in this case we're going to use

3:54:21

3 часа 54 минуты 21 секунда

GPT 3.5 turbo then from a state management perspective uh we can define a specific agent whether that's uh you

3:54:30

3 часа 54 минуты 30 секунд

know we have a this agent we're going to say we're going to use this to create open AI functions and what's nice is also we want to define the large

3:54:38

3 часа 54 минуты 38 секунд

language model which is again is going to be GPT 3.5 turbo uh the tools and the case of Lang chain there's actually a a

3:54:46

3 часа 54 минуты 46 секунд

whole catalog of tools that are available in this case we're going to use something like called Tavi which is basically a search based tool and then

3:54:53

3 часа 54 минуты 53 секунды

the prompt so what the actual user is being requested there so in the case of the large language model again it's gp3

3:55:01

3 часа 55 минут 1 секунда

3.5 we have this defined we're going to manage the state by well what is actually going to be uh being discussed

3:55:09

3 часа 55 минут 9 секунд

or with between the agent and the user and then lastly again the tool tools how do we uh determine which tools to use

3:55:17

3 часа 55 минут 17 секунд

and what information that they actually need in terms of whether it's a search whether it's uh API request or database

3:55:24

3 часа 55 минут 24 секунды

and that's a very standard way that langen uses agents if we were to get more advanced in terms of complexity we also have

3:55:33

3 часа 55 минут 33 секунды

other agent Frameworks that are available uh things like autogen which in fact we can use uh where there's

3:55:40

3 часа 55 минут 40 секунд

actually we can even give in this case multiple use mult large language models or even large language models that have

3:55:47

3 часа 55 минут 47 секунд

a very distinct or different system message and a system message is basically way to sort of Define the rules of where the large large large

3:55:56

3 часа 55 минут 56 секунд

language model operate so in the case here maybe we want to indicate or simulate a discussion between a technical team and we give one uh agent

3:56:05

3 часа 56 минут 5 секунд

or the large language model the uh name of coder and a configuration where the system Mees acting as a developer within

3:56:12

3 часа 56 минут 12 секунд

the team and in another case we're going to have a large language model operate as a product manager and we also give that a clear and distinct system message

3:56:21

3 часа 56 минут 21 секунда

that may be different uh than the coder and then we want to manage the state here and we actually do this with an on

3:56:29

3 часа 56 минут 29 секунд

gen what we call a user proxy which essentially is one that's going to be interacting with the user uh taking in

3:56:36

3 часа 56 минут 36 секунд

sort of the request as also operating and making sure that uh whatever the user wants whether it's executing a

3:56:43

3 часа 56 минут 43 секунды

function that executes the correct function and then lastly in the case of autogen we can Define tools and in this

3:56:50

3 часа 56 минут 50 секунд

case we're going to use these tools to be uh functions within our code so we have a one in this case doing exchange rate and looking at the symbol and then

3:56:59

3 часа 56 минут 59 секунд

doing the proper exchange rate there so when a user in this case when it says how much is a certain amount in USD in

3:57:06

3 часа 57 минут 6 секунд

Euros uh the large language model then responds back by executing uh that particular function uh and getting that

3:57:14

3 часа 57 минут 14 секунд

result out and the last framework that we'll look at is Task Weaver in this case a task weer task Weaver is very

3:57:22

3 часа 57 минут 22 секунды

much focused on being a code first agent framework and what they mean by that is first we can Define in config the large

3:57:29

3 часа 57 минут 29 секунд

language model that's available which is the model in this case again we're going to use GPT 3.5 turbo then the state is

3:57:37

3 часа 57 минут 37 секунд

essentially managed between what we call a planner where we have in this case uh the task weer the is going to uh take in

3:57:46

3 часа 57 минут 46 секунд

the request so in the case we're going to 10 generate 10 random numbers and then the uh code interpreter will

3:57:53

3 часа 57 минут 53 секунды

initiate a plan uh where how to actually execute that and in this case we're actually going to say that it's going to

3:58:01

3 часа 58 минут 1 секунда

execute the handle the request that's the first step and then report back the result pretty standard in a way that this function this request would happen

3:58:09

3 часа 58 минут 9 секунд

because random Genera random numbers is pretty straightforward in terms of code but but then we also have other tools that are available uh we can call that

3:58:17

3 часа 58 минут 17 секунд

we actually call them in the world of task weer plugins uh in this case this uh plugin is an anomaly detection plugin

3:58:24

3 часа 58 минут 24 секунды

in in the case that we have a function that's going to determine uh within the data uh if there's any anomalies that are available or anomalies in the data

3:58:33

3 часа 58 минут 33 секунды

uh and report that back to the user and again this is a code first framework it's going to execute within their sort of code interpreter uh what how that

3:58:43

3 часа 58 минут 43 секунды

function would operate and the user has the ability to either control or that execution or not uh depending on your config that you have

3:58:51

3 часа 58 минут 51 секунда

set up so this was a very brief look at the different AI agent Frameworks out there and some of the use cases that you might

3:58:59

3 часа 58 минут 59 секунд

want to use there the complete lesson and for more information do check out the GitHub repo at

3:59:05

3 часа 59 минут 5 секунд

aka.ms genyen beginners as well as other lessons including one call covering

3:59:12

3 часа 59 минут 12 секунд

function calling which is also a very important part when we're talking about working with AI agents as they work hand to hand to execute user tasks that maybe

3:59:20

3 часа 59 минут 20 секунд

users want to complete in our applications thanks and good

Эпизод 17: Fine-Tuning LLMs [Pt 18]

3:59:29

3 часа 59 минут 29 секунд

luck hi my name is Nan Aran I'm a senior AI Advocate on the developer relations team at Microsoft and I'm excited here

3:59:36

3 часа 59 минут 36 секунд

to be here today to talk to you about fine tuning for llm chapter 18 in generative AI for beginners so what are

3:59:44

3 часа 59 минут 44 секунды

we going to cover today today we're going to help you answer four questions first what is fine-tuning second why is

3:59:52

3 часа 59 минут 52 секунды

it useful third when should you use it and fourth and most important of all how do you get started fine-tuning your

3:59:59

3 часа 59 минут 59 секунд

large language models so let's dive in so first a really quick introduction we want to like give you a concept of what

4:00:07

4 часа 7 секунд

fine tuning is why it matters and when you should be using it why is it useful and if you've been following this course

4:00:15

4 часа 15 секунд

you've probably heard of terms like prompt engineering and retrieval augmented generation so how is fine-tuning going to help us given we

4:00:23

4 часа 23 секунды

have all those other Solutions as well so let's start with a very simple definition what is fine tuning fine

4:00:32

4 часа 32 секунды

tuning is a common practice in machine learning where we retrain an existing model with new data to improve its performance on a given

4:00:40

4 часа 40 секунд

task so in some sense this is more of an advanced technique because in order for you to fine-tune the model itself you

4:00:47

4 часа 47 секунд

need to have good data you need to understand how to evaluate that fine-tune model to kind of give you the the accuracy and performance you want

4:00:55

4 часа 55 секунд

and if you don't do it right you might actually hurt yourself by degrading the performance from where you started so when we think about fine tuning we're

4:01:03

4 часа 1 минута 3 секунды

actually thinking of the difference between a fine tune model and a foundation model so when you use large language models today you're actually using a foundation model that's trained

4:01:11

4 часа 1 минута 11 секунд

on a massive amount of data and is really good our general purpose tasks when we think about fine tune model we're looking at how good is this model

4:01:19

4 часа 1 минута 19 секунд

for my specific task so why should I fine tune we've already heard about techniques like prompt engineering that can make the

4:01:27

4 часа 1 минута 27 секунд

responses of a foundation model better for my particular application I might also want to kind of

4:01:35

4 часа 1 минута 35 секунд

use a technique or a design pattern like retrieval augmented generation to ground the responses in my data all of these

4:01:42

4 часа 1 минута 42 секунды

techniques help me improve the response quality of a foundational large language model so why fine-tune fine-tuning is

4:01:52

4 часа 1 минута 52 секунды

appropriate if your desired response quality can't be achieved with those Solutions and there might be many

4:02:00

4 часа 2 минуты

reasons for this one example is tokenization cost if you remember from prompt engineering most of these models have a Max token siiz window and when

4:02:09

4 часа 2 минуты 9 секунд

you want to train them you actually have to add in examples think of like f shot learning where you're putting those examples in with the prompt so now you

4:02:16

4 часа 2 минуты 16 секунд

have limitations based on the token size you have additional tokenization costs so there are limitations with prompt engineering another reason might be the

4:02:26

4 часа 2 минуты 26 секунд

the Skilling like the the capabilities of the underlying model may not give you what you need for your particular application and you want to upskill it

4:02:34

4 часа 2 минуты 34 секунды

the third and again this comes back to cost is that it might be easier and cheaper for you to take a a a lower

4:02:42

4 часа 2 минуты 42 секунды

generation model and upskill it or retrain it for your needs than to pay the cost for a higher uh price Model so

4:02:49

4 часа 2 минуты 49 секунд

does that mean you should always find tune not so fast the most important question to ask yourself is when you

4:02:56

4 часа 2 минуты 56 секунд

should F tune and you should only F tune if the benefits of the fine-tuning are going to outweigh the costs or weaknesses of the

4:03:05

4 часа 3 минуты 5 секунд

approach so here are some questions you should start by asking yourself do you have a good use case for fine tuning in

4:03:14

4 часа 3 минуты 14 секунд

other words does your application really require you to bring in data and R retrain the model or can you get away

4:03:20

4 часа 3 минуты 20 секунд

with decent performance with existing strategies it could be because you have an edge case that's not covered or you

4:03:27

4 часа 3 минуты 27 секунд

want to upskill as we mentioned before it could also be because perhaps the default models don't give you the same kind of like control over the formatting

4:03:36

4 часа 3 минуты 36 секунд

or the personas that you want to adopt next you want to ask yourself have you tried other options have you looked at other options and you valuated them

4:03:44

4 часа 3 минуты 44 секунды

do they give you enough performance are you doing this for a particular measurable attribute third did you factor in the

4:03:53

4 часа 3 минуты 53 секунды

other costs so when we think about it we're always comparing with tokenization you're like oh I'm going to save on token costs or I'm going to kind of have less that I have to ship with every

4:04:01

4 часа 4 минуты 1 секунда

prompt but it turns out that when you want to fine tune you have to pay for the compute for fine tuning you have to pay for the data Gathering and cleanup and then you've got to maintain that

4:04:10

4 часа 4 минуты 10 секунд

model because once you fine-tuned it that model is now yours so if the foundation model evolves or your scenario evolves you got to retune

4:04:18

4 часа 4 минуты 18 секунд

it and finally did you confirm the benefits so if we've come this far and you've said yes I think I want to find

4:04:27

4 часа 4 минуты 27 секунд

tune the next question really is how do we fine-tune right so fine-tuning a model is not a trivial process so you

4:04:36

4 часа 4 минуты 36 секунд

want to first ask questions like is the foundation model actually fine tunable if you go look at and let's talk about open AI models for instance if you go

4:04:44

4 часа 4 минуты 44 секунды

look at open AI models not every open AI model is fine-tunable by default you need to look at it to figure out hey which version or generation of the model

4:04:53

4 часа 4 минуты 53 секунды

can I fine tune and you may also find that providers only allow you to fine tune these or run fine-tuning jobs in certain

4:05:00

4 часа 5 минут

regions next do you have the right data in order for you to retrain this model you better have the data that represents

4:05:07

4 часа 5 минут 7 секунд

the skill or the use case or the feature that you want to actually build in to this fine tune model next do you have a

4:05:14

4 часа 5 минут 14 секунд

compute environment around the job so when it comes to open aai in this particular tutorial I'm going to show you the open aai compute environment but of course you can now bring it to Azure

4:05:23

4 часа 5 минут 23 секунды

open Ai and use the Azure open AI environment for computing and last but not least once you find you the model remember now you've got to host it and

4:05:31

4 часа 5 минут 31 секунда

make sure that's available to your clients for uh inference so you have a hosting environment again this is where trying this out and then using Azure

4:05:39

4 часа 5 минут 39 секунд

open AI makes it fairly seamless so what does that fine tuning process look like think of it as four

4:05:47

4 часа 5 минут 47 секунд

steps first you're going to prepare the data that you need to find tune your model then you're going to train the model then you're going to evaluate

4:05:56

4 часа 5 минут 56 секунд

whether that model is providing you the results you want and once you've done that you're finally going to deploy it so when you look at the data preparation

4:06:04

4 часа 6 минут 4 секунды

some of the things you want to think about is the size of the training data how many examples should you have so in today when in the next uh segment I'm just going to show you a really quick

4:06:13

4 часа 6 минут 13 секунд

demo that you can use to kind of figure out the process on your own and for that it's a toy example so we're only going to have about 10 examples but in real

4:06:20

4 часа 6 минут 20 секунд

well scenario you're going to need about 50 to 100 examples or data records to fine tune your uh model you might even

4:06:28

4 часа 6 минут 28 секунд

need more next you want to look at things like data representation is the data you've collected Fair are you covering all the possible cases so that

4:06:37

4 часа 6 минут 37 секунд

you're not um kind of biasing decisions towards one demographic over another over another is the form of the data appropriate for example we need jonl

4:06:46

4 часа 6 минут 46 секунд

have you actually got that rendered in a way that can be validated and used for training and then of course requirements coverage does your data provide all the

4:06:55

4 часа 6 минут 55 секунд

examples you need to cover the use case for which you're training it in the first place evaluate is where you upload the data for training create the fine-tuning

4:07:04

4 часа 7 минут 4 секунды

job and then run that job for test and then like test that fine tun model for the quality of the responses that it

4:07:11

4 часа 7 минут 11 секунд

provides and let's say you look at it and say for the use cases that I asked for this is doing well and open ey

4:07:18

4 часа 7 минут 18 секунд

actually is a dashboard that allows you to like look at those metrics the last step is for you to then deploy that model so you can hit it either through

4:07:26

4 часа 7 минут 26 секунд

code or from something like the playground in open AI in other words a no code model to actually test it out in

4:07:33

4 часа 7 минут 33 секунды

the real world so let's see what that looks like to do this I have a toy example remember this is only to show you the process this is not really a

4:07:41

4 часа 7 минут 41 секунда

realistic example but but it'll help us walk through the code and understand the steps that you need to take so in this case what I'm saying is hey I want to

4:07:50

4 часа 7 минут 50 секунд

build a factual chatbot that answers questions about the periodic table elements using limeric in order for me to do that today

4:07:57

4 часа 7 минут 57 секунд

what I need to do is I need to provide the system context I and I want that answer in a particular format as you've seen so I need to provide few short

4:08:05

4 часа 8 минут 5 секунд

examples and you know that's all it cost for me so I want to explore how do I finetune the model and I want to use GPT 35 turbo so to start with let's actually

4:08:14

4 часа 8 минут 14 секунд

go and see if we can take a look at what this looks like so over here I have a system prompt that says your l a factual chatboard that answers questions about

4:08:23

4 часа 8 минут 23 секунды

elements in the periodic table with a limeric and I'm just using G GPD 35 turbo and I'm just going to say hey uh

4:08:30

4 часа 8 минут 30 секунд

tell me about carbon right or copper or anything any element you like and you'll notice that this actually will give me

4:08:38

4 часа 8 минут 38 секунд

what I want because I've got a system prompt it's not in the format that I want it doesn't actually have the specific kind of flow that I'm looking

4:08:46

4 часа 8 минут 46 секунд

for but it does the job right so now I want to F tune this how do I go about it before I kind of walk through the

4:08:53

4 часа 8 минут 53 секунды

slides I'm going to point you to our repo and if you go look in the repo and this should be in there today uh there

4:09:02

4 часа 9 минут 2 секунды

is actually under generative AI beginners if you go into chapter 18 and you look at the assignment you will find there's a data file and a notebook and

4:09:11

4 часа 9 минут 11 секунд

if you open up that notebook you will actually see what you're seeing here the easiest way for you to walk through the notebook is to put this into outline mode and then you can kind of just step

4:09:19

4 часа 9 минут 19 секунд

through the different parts so we talked about what the four steps of fine tuning are step one you're

4:09:26

4 часа 9 минут 26 секунд

going to prepare the data and upload it so when you prepare the data set remember we want a chatbot that knows how to speak in liic here is what a

4:09:34

4 часа 9 минут 34 секунды

single record looks like you can see that I've given the system content uh here is the Persona and I've given it examples here's a Content here's a user

4:09:43

4 часа 9 минут 43 секунды

promp tell me about gallium here is what the example should look like see the hyphenation see the kinds of content I have for each step of the limeric now in

4:09:51

4 часа 9 минут 51 секунда

this you're only seeing two examples if you actually look at the data you will find that we have about 10 examples in there and let me see if I can just quickly bring that up for you the most

4:10:00

4 часа 10 минут

important thing you have to pay attention to is that every uh record should be in a single line so don't look for default Json formatting make sure

4:10:09

4 часа 10 минут 9 секунд

it's in this format where each record is a single line and if you don't then your job will fail with validation errors

4:10:16

4 часа 10 минут 16 секунд

next once you've got your data prepared and I have 10 records for this next I want to upload my data set if you've

4:10:24

4 часа 10 минут 24 секунды

been looking at our um notebooks just have an open key I have currently an open AI based notebook and I will have

4:10:31

4 часа 10 минут 31 секунда

an Azure open AI one later but over here you would need to have an open AI key and have that set up and we do have guidelines for how you do that but once

4:10:40

4 часа 10 минут 40 секунд

you do that the code is really simple you create create a job by opening up this Json file give the purpose as

4:10:48

4 часа 10 минут 48 секунд

fine-tuning and submit it and this effectively uploads the data set to the back end at this point it's validating to

4:10:57

4 часа 10 минут 57 секунд

make sure that that data set has the data that you want so your next step is then to create the fine-tuning job with the

4:11:04

4 часа 11 минут 4 секунды

SDK to do that it's a really simple uh method called so you're doing finetuning do jobs. create you're going to pass in

4:11:12

4 часа 11 минут 12 секунд

the five ID from that upload in the previous step tell it the foundation model that you want to fine-tune using

4:11:20

4 часа 11 минут 20 секунд

this data and let it run and the output of this is going to be a file job ID that you can then use to track the

4:11:28

4 часа 11 минут 28 секунд

progress of your job so if you keep going you can check the status of your job and there are many things you can do with that

4:11:37

4 часа 11 минут 37 секунд

particular identifier you can look at the events in at a very low granularity or you can just look at the overall status of the job itself so what I've

4:11:46

4 часа 11 минут 46 секунд

set this notebook up to do is for you to first look at it and say what is the status of the job and it tells you that the job is running in other words it's now in the process of fine like

4:11:54

4 часа 11 минут 54 секунды

validating your data and starting the fine-tuning job but if you want to look at the final granularity of what's Happening you can go ahead and you can

4:12:02

4 часа 12 минут 2 секунды

actually track the events and when you do that you pretty much can sit on this particular cell and just refresh it and

4:12:10

4 часа 12 минут 10 секунд

you will see that it's going to go through that uh list of samples and train it and if you keep refreshing at some point it's going to say the

4:12:19

4 часа 12 минут 19 секунд

training job is done tell your checkpoints are created and now you have a new fine-tune model this is going to take a few minutes but remember I only

4:12:27

4 часа 12 минут 27 секунд

had 10 examples so you're at least able to see a response in Fairly short order if you use some of the more complex examples and we'll talk about that later

4:12:35

4 часа 12 минут 35 секунд

it could take on the order of an hour or more for you to get these results but for you to get the sense of it this

4:12:43

4 часа 12 минут 43 секунды

short example is enough and you'll see that now it says there is a new fine tune model available in open aai and the job has

4:12:51

4 часа 12 минут 51 секунда

completed you can now go into the open a dashboard and look at the status so over here I have the open a dashboard and if

4:12:59

4 часа 12 минут 59 секунд

I actually go in there is a little uh panel here for fine tuning and if I kind of go into this you will see that I actually have a record of all the

4:13:07

4 часа 13 минут 7 секунд

fine-tuning jobs I ran many of them failed before they finally succeeded these failures were actually because there were validation errors in the data

4:13:16

4 часа 13 минут 16 секунд

and you can see this is why having the right format matters but the final version they complete and now I have a

4:13:24

4 часа 13 минут 24 секунды

model that is ready to try out and if I look at this this is the one that succeeded it gives me the checkpoints it

4:13:31

4 часа 13 минут 31 секунда

also gives me and I can go look into this the messages and tells me the events that happened to get me to success I can also go into the metrics

4:13:40

4 часа 13 минут 40 секунд

and look at the metrics for evaluating these jobs uh the the the the kind of status of the job but in the interest of time let's go

4:13:48

4 часа 13 минут 48 секунд

and see what happens next right so we've completed this we've seen the status we know the job is done what do we do next

4:13:57

4 часа 13 минут 57 секунд

now you can actually start using that endpoint to see whether that does the job you expected it to do after fine tuning and this is one of the steps of

4:14:05

4 часа 14 минут 5 секунд

evaluation you want to train it try it out see if the result meets your expectation and if not you may need to retune it retrain it

4:14:13

4 часа 14 минут 13 секунд

again the interesting thing is once this model is deployed that ID is exactly the same as any other model so you can use

4:14:20

4 часа 14 минут 20 секунд

the default uh code that you would use for chat completion get back the ID of this model and use it in the exact same

4:14:30

4 часа 14 минут 30 секунд

a call to see what happens and you'll see over here that when I now use the Open aai chat completion request with

4:14:37

4 часа 14 минут 37 секунд

this new model and ask you to tell me about another element it actually returns it in the format that I had

4:14:45

4 часа 14 минут 45 секунд

tuned it or trained it for but wait there's more so now we can if you run this in your own kind of um environment if you're on the notebook

4:14:54

4 часа 14 минут 54 секунды

you should be able to walk through this and play with it try it out change the prompt change the parameters change the data see how things are are are modified

4:15:03

4 часа 15 минут 3 секунды

but wait you can do more you can actually go and see this model and how it Compares against the foundation model right in the playground and to do that

4:15:12

4 часа 15 минут 12 секунд

what you would basic Bally do is go to the model and if you go all the way to the bottom it's going to let you open this up in a playground and so when you open this up in a

4:15:20

4 часа 15 минут 20 секунд

playground it's actually I'm going to bring this uh screen over for just a second so we can look at it this is what it looks like when I've got it opened up

4:15:29

4 часа 15 минут 29 секунд

in a playground you will see that now it actually has both these uh models is on the left side you see the original model it was trained on on the right side is

4:15:37

4 часа 15 минут 37 секунд

the finetune model let's go and try to copy the same thing that we were using for testing it so we want to say hey I have a factual robot and I wanted to say

4:15:47

4 часа 15 минут 47 секунд

URL a factual robot that answers questions with results and liic so if I put this in note that when I'm using this particular format both models are

4:15:55

4 часа 15 минут 55 секунд

in sync so when I put in a system prompt they both have the exact same system prompt and then I can do something like tell me about uh let's go with gold and

4:16:04

4 часа 16 минут 4 секунды

when I run this it's going to show me how the two of them differ it's going to tell me the latency and it's going to tell me how many tokens it took

4:16:13

4 часа 16 минут 13 секунд

but the most interesting thing you'll see is that the responses are different you'll see that this actually reflects the format that I wanted it's kind of using even the if you if you go look at

4:16:21

4 часа 16 минут 21 секунда

the examples you'll see that the tone of it is very similar to what I expected it's also giving me the latency this was fast at giving me the response but it

4:16:28

4 часа 16 минут 28 секунд

took more tokens so the other thing you think about now this was actually a very trivial example so take that with a grain of salt but this is how you would

4:16:36

4 часа 16 минут 36 секунд

look at it and say am I really fine-tuning it for the right reasons is it a tokenization cost is it a latency and you tune this and get your results

4:16:44

4 часа 16 минут 44 секунды

out of it right so let's recap what we've learned so far and we just looked through this notebook you fine-tuned it you were able

4:16:53

4 часа 16 минут 53 секунды

to call it from the API you're able to go see it in the playground and load it up and compare the notes now you have a fine train mod I mean a fine tune model

4:17:02

4 часа 17 минут 2 секунды

trained on your data and you can go ahead and retune that model give it new data you can evaluate it and so

4:17:09

4 часа 17 минут 9 секунд

on so with that we kind of walk through these steps you create the job track the events retrieve the ID ask the question

4:17:18

4 часа 17 минут 18 секунд

go ahead and monitor its status and compare it with your foundation model so what's left well remember that I said that fine

4:17:27

4 часа 17 минут 27 секунд

tuning requires non-trivial expertise to get the right results so one of the things you need to know is understand the best practices and limitations of

4:17:35

4 часа 17 минут 35 секунд

your approach and evaluate the tradeoffs before you take a decision so first let's recap make sure

4:17:42

4 часа 17 минут 42 секунды

sure you have a valid use case in this particular tutorial I showed you a very toy example but your valid use case could be something that says I need to

4:17:51

4 часа 17 минут 51 секунда

actually have it do a new skill maybe it has to render an image maybe it has to do additional processing that I cannot do within the scope of a prompt

4:17:59

4 часа 17 минут 59 секунд

engineering uh solution so have a valid use case that requires fine tuning then try the existing options first can

4:18:07

4 часа 18 минут 7 секунд

retrieval augmented generation give you the quality you need is prompt engineering enough do you really need to pay the overheads of retraining cleaning

4:18:15

4 часа 18 минут 15 секунд

data hting it deploying it and so on so evaluate your other options then estimate the costs and tradeoffs

4:18:23

4 часа 18 минут 23 секунды

understand not just the cost for retraining the the fine-tuning your model but the cost for maintenance the cost for hosting and so on and last but

4:18:31

4 часа 18 минут 31 секунда

not least and this is super important have a maintenance strategy once you've got your own model that you fine-tuned you are now responsible for its upkeep

4:18:40

4 часа 18 минут 40 секунд

so if the foundation model evolves if there are new capabilities it's up to you to figure out how you're going to evolve your custom model end

4:18:48

4 часа 18 минут 48 секунд

point and with that we come to the end of the segment I hope you had a great time understanding what fine tuning is and let's summarize it with this

4:18:57

4 часа 18 минут 57 секунд

Illustrated guide you learned what fine-tuning was you learned why you should be fine-tuning and when it is

4:19:04

4 часа 19 минут 4 секунды

appropriate to fine-tune your foundation model then once you've decided that it's worth fine tuning we looked at how you would fine tune it and the steps really

4:19:12

4 часа 19 минут 12 секунд

involve three things first find data prepare it JSL is the format we use upload it and then train your foundation

4:19:22

4 часа 19 минут 22 секунды

model on this data to get a fine Cel model evaluate it for quality and once you're ready go ahead deploy it and then

4:19:29

4 часа 19 минут 29 секунд

use it exactly the way you would any other model and with that we come to the end of chapter 18 or lesson 18 of generative

4:19:38

4 часа 19 минут 38 секунд

AI for beginners we hope this was a super fast an easy introduction to F tuning and we can't wait for you to go

4:19:47

4 часа 19 минут 47 секунд

try out the notebooks and tell us what you learned on your own don't forget to check out the collection in the in the

4:19:54

4 часа 19 минут 54 секунды

repository for resources including the open a cookbook and the Azure open a tutorial as well as a hugging Face

4:20:01

4 часа 20 минут 1 секунда

tutorial that will help you explore this topic in more depth with additional providers thank you and let's keep

4:20:09

4 часа 20 минут 9 секунд

learning

4:20:11

4 часа 20 минут 11 секунд

[Music]