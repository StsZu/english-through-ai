# Manual Pipeline — щотижневий рунбук

Мета: з одного модуля відео зробити комплект матеріалів для уроку.
Робиться вручну доти, доки не буде написаний `lessonfactory` (зустріч №10).

**Головне правило:** усе, що дратує під час ручного проходу, записується
в `friction.md`. Цей файл — технічне завдання для автоматизації.

Очікуваний час: 30–40 хв на модуль.

---

## Крок 0. Папка тижня

```
lessons/wNN/
├── transcript_raw.txt     # сирий транскрипт з Coursera
├── transcript_b1.md       # адаптована версія для читання
├── terms.json             # витягнуті терміни
├── glossary.md            # людиночитний глосарій
├── worksheet.md           # вправи + ключі
├── anki.csv               # імпорт у Anki
├── talk.md                # план 3-хвилинного виступу
└── friction.md            # що бісило
```

```bash
mkdir -p lessons/w01 && touch lessons/w01/friction.md
```

---

## Крок 1. Транскрипт (10 хв)

1. Coursera → відео → вкладка **Transcript** (не Subtitles).
2. Виділити все → скопіювати.
3. Вставити в `transcript_raw.txt`.
4. Для кожного наступного відео модуля додати розділювач:

```
--- video 2: <назва> (MM:SS) ---
```

Записати сумарну тривалість модуля у хвилинах — знадобиться на кроці 2.

---

## Крок 2. Швидкість мовлення (2 хв)

```bash
wc -w lessons/w01/transcript_raw.txt
```

`wpm = слова / хвилини`

| wpm | Висновок для B1 |
|---|---|
| < 130 | комфортно, можна слухати без пауз |
| 130–150 | нормально, але потрібен pre-teaching лексики |
| > 150 | різати на фрагменти по 3–5 хв, слухати двічі |

Записати число у `friction.md`.

---

## Крок 3. Витягнути терміни (5 хв)

Промпт (Claude Project «English Through AI»):

```
You are building vocabulary material for a B1 English learner
who is studying AI in English.

From the transcript below, extract the 12 most useful domain terms.
Prioritise: (a) terms that repeat, (b) terms needed to TALK about AI,
(c) skip terms that are transparent for a Ukrainian speaker
    (e.g. "system", "information", "process").

For EACH term return:
- term
- definition_b1: max 20 words, CEFR B1 vocabulary only
- collocations: exactly 2 natural phrases with this term
- source_sentence: the sentence from the transcript, verbatim
- gapfill: the source sentence with the term replaced by "_____"
- ua: Ukrainian equivalent

Return ONLY a JSON array. No markdown fences, no commentary.

TRANSCRIPT:
<<<paste>>>
```

**Обов'язково перевірити вручну.** Модель стабільно тягне або надто прості
слова, або надто рідкісні. Викинути 2–3, додати свої. Зберегти `terms.json`.

---

## Крок 4. B1-версія тексту (3 хв)

```
Rewrite the transcript below as a clean B1-level reading text.

Rules:
- Keep every technical term unchanged and in **bold**
- Split sentences longer than 15 words
- Remove filler, repetitions and spoken-language artefacts
- Keep ALL facts. Do not summarise, do not shorten the content
- Target length: 400-500 words
- Output plain markdown

TRANSCRIPT:
<<<paste>>>
```

→ `transcript_b1.md`

**Як користуватись:** спершу читати B1-версію, потім оригінальний
транскрипт. Різниця між ними — це і є навчальний матеріал.

---

## Крок 5. Воркшит (3 хв)

```
Using the terms in the JSON below, build a worksheet in markdown:

A. Matching: 12 terms <-> 12 shuffled definitions
B. Gap-fill: the 12 gapfill sentences, shuffled, with a word bank
C. Collocation check: 8 items, "choose the natural phrase" (2 options each)
D. Speaking prompts: 5 questions that FORCE the learner to use
   at least 3 of these terms in the answer

Then an ANSWER KEY section at the end, clearly separated by "---".

TERMS:
<<<paste terms.json>>>
```

→ `worksheet.md`

---

## Крок 6. Anki (5 хв)

```
Convert the JSON to CSV for Anki import.
Columns, semicolon-separated, no header row:
front;back;example
front   = term
back    = definition_b1 + " | " + ua
example = source_sentence with the term wrapped in <b></b>
Output raw CSV only, no fences.
```

Anki → File → Import → роздільник `;` → колода `English Through AI::W01`.

Режим повторення: 10 хв щодня, не пакетно перед уроком.

---

## Крок 7. План виступу (5 хв)

Не генерувати текст промови. Генерувати **тільки скелет**:

```
I will give a 3-minute talk in English about <topic> to my English teacher.
My level is B1.

Give me ONLY a skeleton:
- 4 bullet points (the structure of the talk)
- 8 useful phrases for signposting (e.g. "The first idea is...")
- 3 likely follow-up questions the teacher may ask

Do NOT write the talk itself. I will write and speak it myself.
```

→ `talk.md`

**Заборонено:** просити модель написати сам текст виступу. Це вбиває сенс
вправи. Модель дає каркас — м'ясо пише людина.

---

## Крок 8. Friction log

Дописати в `friction.md` усе, що зайняло час або дратувало. Приклади формату:

```
- [copy] Transcript копіюється вручну для кожного відео -> потрібен експорт
- [terms] ~20% термінів довелося відсіяти -> потрібен стоп-лист
- [anki] CSV-імпорт руками -> потрібен genanki і .apkg одразу
- [wpm] рахував калькулятором -> порахувати скриптом
```

---

## Чек-лист готовності до уроку

- [ ] `transcript_raw.txt` заповнено
- [ ] wpm пораховано
- [ ] `terms.json` перевірено вручну, 12 термінів
- [ ] `transcript_b1.md` прочитано двічі
- [ ] `worksheet.md` **пройдено самостійно**, ключі перевірено
- [ ] `anki.csv` імпортовано, картки повторювались мінімум 3 дні
- [ ] `talk.md` є, виступ відрепетирувано вголос 2 рази
- [ ] `friction.md` заповнено
