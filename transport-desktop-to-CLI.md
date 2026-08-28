# transport-desktop-to-CLI

**Від:** Claude (desktop, claude.ai)
**Кому:** Claude CLI (локально, `/Users/szubar/Projects/Educational_courses_2026/english-through-ai/`)
**Дата:** 2026-08-28
**Тікет:** T-001

---

## Протокол обміну

- Цей файл — **вхідні завдання**. Читай, виконуй, не редагуй.
- Відповідь пиши **тільки** у `transport-CLI-to-desktop.md`, дописуючи новий
  блок згори (найновіше — першим), за шаблоном у кінці цього файлу.
- Не видаляй нічого. Тільки переміщуй, створюй і дописуй. Якщо щось
  здається зайвим — не видаляй, а внеси в секцію `Questions` свого звіту.
- Папку `legacy/` не чіпай взагалі. Це архів.
- Якщо якась вимога суперечить іншій — не вгадуй, зупинись і запитай
  у звіті.

---

## Контекст проєкту

Курс «English Through AI»: студент рівня B1 вивчає англійську через
матеріали про AI. Формат — 1:1 з викладачем, 12 тижнів, зустріч 90 хв.
Ініціатива на студенті: він готує матеріал, веде урок, презентує.

Основне джерело: Coursera → Anthropic → *AI Fluency: Framework & Foundations*.

**Ключове рішення, ухвалене щойно:** урок — це один HTML-файл, який студент
відкриває і презентує. Усередині: матеріал, словник, аудіо, quiz, завдання
на говоріння.

---

## Завдання 1 — реорганізація репозиторію

### Поточний стан

```
.
├── Course Idea.md
├── artifacts/          (порожня)
├── errors/             (порожня)
├── files/
│   ├── baseline-protocol.md
│   ├── lesson-01-agenda.md
│   ├── manual-pipeline.md
│   └── prep.md
├── legacy/
│   ├── AI Course Sources.md
│   ├── English_Through_AI.pdf
│   ├── English_Through_AI.pptx
│   ├── Full_Series_Generative_AI_for_Beginners/
│   │   └── Microsoft_Developer_Generative_AI_for_Beginners.md
│   └── Vibe-coding.md
├── recordings/         (порожня)
└── termbank/           (порожня)
```

### Цільовий стан

```
.
├── README.md                          # створити
├── transport-desktop-to-CLI.md
├── transport-CLI-to-desktop.md
├── .gitignore                         # створити
├── docs/
│   ├── course-idea.md                 # ← Course Idea.md
│   ├── manual-pipeline.md             # ← files/
│   ├── baseline-protocol.md           # ← files/
│   └── conventions.md                 # створити
├── lessons/
│   └── w01/
│       ├── index.html                 # створити (Завдання 2)
│       ├── lesson.json                # створити (Завдання 2)
│       ├── prep.md                    # ← files/prep.md
│       ├── agenda.md                  # ← files/lesson-01-agenda.md
│       ├── friction.md                # створити порожній з шапкою
│       └── audio/                     # створити, .gitkeep
├── templates/
│   ├── lesson-template.html           # створити (Завдання 2)
│   ├── lesson.schema.json             # створити (Завдання 2)
│   └── week-scaffold/                 # створити (Завдання 3)
├── termbank/
│   └── termbank.csv                   # створити з заголовком
├── recordings/  (.gitkeep)
├── errors/      (.gitkeep)
└── legacy/                            # НЕ ЧІПАТИ
```

### Деталі

1. `artifacts/` перейменувати на `lessons/`. Причина: урок тепер артефакт
   сам по собі, назва `artifacts` стала неоднозначною.
2. `files/` розформувати згідно з деревом вище, потім видалити порожню
   папку `files/`.
3. У `docs/manual-pipeline.md`, `docs/baseline-protocol.md`,
   `lessons/w01/prep.md`, `lessons/w01/agenda.md` **оновити всі шляхи**,
   які посилаються на стару структуру (`artifacts/wNN/` → `lessons/wNN/`,
   `docs/manual-pipeline.md` лишається). Перевір кожне посилання.
4. `.gitignore`:

```
recordings/*.m4a
recordings/*.mp3
recordings/*.wav
lessons/*/audio/*.mp3
lessons/*/audio/*.m4a
.DS_Store
node_modules/
__pycache__/
.venv/
```

   Аудіо не в git — файли великі й персональні. Транскрипти (`.txt`, `.json`)
   у git лишаються.

5. `termbank/termbank.csv` — накопичувальний майстер-файл, заголовок:

```
week;term;definition_b1;collocation_1;collocation_2;ua;source_sentence;added_at
```

6. `README.md` — коротко: що це, структура папок, як запустити урок
   (`open lessons/w01/index.html`), як додати новий тиждень, посилання
   на `docs/`. Українською. Без води, до 60 рядків.

7. `docs/conventions.md` — правила проєкту:
   - нумерація тижнів `w01`…`w12`, завжди два розряди
   - імена файлів `kebab-case`, крім `index.html`
   - записи: `recordings/wNN_talk.m4a`, `recordings/w00_baseline.m4a`
   - діагностика: `errors/wNN.json`
   - мова документації — українська; мова навчального контенту — англійська
   - коміти: `w01: add glossary`, `docs: fix paths`, `feat(template): quiz`

8. Якщо `git` ще не ініціалізовано — `git init`, зробити перший коміт
   `chore: restructure repository`. Якщо вже є — просто коміт.

---

## Завдання 2 — HTML-шаблон уроку

Це ядро. Читай уважно.

### Призначення

Студент відкриває файл у браузері і **презентує з нього урок вчителю**.
Файл має працювати офлайн, з `file://`, без сервера, без збірки.

### Жорсткі технічні обмеження

| # | Обмеження | Причина |
|---|---|---|
| 1 | Один самодостатній `.html`. CSS і JS inline | працює з флешки, з пошти, звідусіль |
| 2 | **Жодного CDN, жодного зовнішнього `<script src>`** | має працювати без інтернету |
| 3 | Vanilla JS, без фреймворків, без збірки | студент має розуміти код |
| 4 | Дані уроку — inline в `<script id="lesson-data" type="application/json">` | `fetch()` зовнішнього JSON падає на `file://` через CORS. Це не обговорюється |
| 5 | `lesson.json` лежить поруч **як джерело правди**; білд-скрипт вшиває його в HTML | редагувати зручно JSON, а не HTML |
| 6 | `localStorage` для прогресу — можна, ключ `etai:w01:*` | локальний файл, обмежень немає |
| 7 | Адаптив: працює на 13" MacBook і на зовнішньому моніторі | презентація |

### Структура уроку (секції)

1. **Header** — номер тижня, тема, джерело, тривалість
2. **Objectives** — 3–5 пунктів «By the end of this lesson I can…»
3. **Vocabulary** — картки з термінами. Клік → перевертається:
   лицьова = термін, зворот = B1-визначення + 2 колокації + UA
4. **Reading** — перемикач `B1 version` / `Original transcript`.
   Терміни з блоку 3 підсвічені, при наведенні — tooltip з визначенням
5. **Audio** — `<audio controls>` для локальних файлів з `./audio/`
   + список зовнішніх посилань, якщо аудіо не завантажене
6. **Quiz** — див. окрему специфікацію нижче
7. **Speaking prompts** — 5 питань, великим шрифтом, з таймером на 60 с
8. **Homework** — чек-лист з чекбоксами, стан у `localStorage`

### Режим презентації

- Клавіші `←` / `→` — між секціями
- `F` — повноекранний режим
- `P` — перемикання presentation mode: шрифт +40%, одна секція на екран,
  прихована навігація
- Індикатор прогресу зверху

### Специфікація quiz — читай двічі

Це найважливіша частина. Студент прямо вказав формат.

**Механіка:**

1. Питання + рівно **три** варіанти відповіді.
2. Студент обирає один.
3. Після вибору зʼявляється фідбек **саме до обраного варіанта**.
4. Фідбек є в **усіх трьох** варіантів, не тільки в правильного.
5. Фідбек не просто каже «правильно / неправильно» — він **пояснює
   і додає нову інформацію**, якої не було в питанні.
6. Після відповіді варіанти блокуються, зʼявляється кнопка `Next`.
7. Повернутись і перевибрати не можна — це псує чесність вправи.
   Кнопка `Restart quiz` є в кінці.
8. У кінці — підсумок: рахунок + список термінів, які варто повторити.

**Схема даних:**

```json
{
  "week": "w01",
  "title": "AI Fluency — Module 1",
  "source": "Coursera / Anthropic / AI Fluency: Framework & Foundations",
  "duration_min": 90,
  "objectives": ["..."],
  "vocabulary": [
    {
      "term": "delegation",
      "definition_b1": "max 20 words, B1 vocabulary only",
      "collocations": ["...", "..."],
      "ua": "...",
      "source_sentence": "verbatim from transcript"
    }
  ],
  "reading": {
    "b1": "markdown string",
    "original": "markdown string"
  },
  "audio": [
    {"label": "Module 1 — video 1", "src": "./audio/w01-v1.mp3", "url": null}
  ],
  "quiz": [
    {
      "id": "q1",
      "prompt": "...",
      "term_refs": ["delegation"],
      "options": [
        {
          "id": "a",
          "text": "...",
          "correct": false,
          "feedback": "40-80 words, CEFR B1. Explain WHY this option is wrong, and add one new fact or nuance the learner did not know."
        },
        {
          "id": "b",
          "text": "...",
          "correct": true,
          "feedback": "40-80 words, CEFR B1. Confirm, then EXTEND: give an example or a related idea not mentioned in the question."
        },
        {
          "id": "c",
          "text": "...",
          "correct": false,
          "feedback": "..."
        }
      ]
    }
  ],
  "speaking_prompts": ["..."],
  "homework": ["..."]
}
```

**Валідація** (білд-скрипт має падати з помилкою, а не мовчки збирати):

- рівно 3 опції на питання
- рівно одна з `correct: true`
- `feedback` непорожній в **усіх трьох**
- `feedback` довжиною 40–120 слів
- `term_refs` посилається на терміни, які реально є у `vocabulary`

Схему записати в `templates/lesson.schema.json` (JSON Schema draft-07).

### Дизайн

- Мінімалізм, високий контраст, читається з відстані 2 м
- Базовий шрифт ≥ 18px, у presentation mode ≥ 26px
- Системні шрифти (`-apple-system, BlinkMacSystemFont, ...`) — без вебфонтів
- Кольори: нейтральний фон, один акцентний. Правильна відповідь — зелений,
  неправильна — не червоний, а бурштиновий. Червоний демотивує, а фідбек
  тут інформативний, а не каральний
- Плавні переходи для фідбеку (fade-in 200ms), без анімаційного цирку
- Друк: `@media print` — quiz згорнутий, reading розгорнутий

### Що зібрати

1. `templates/lesson-template.html` — шаблон із заглушкою даних
2. `templates/lesson.schema.json`
3. `lessons/w01/lesson.json` — **скелет із `TODO`-плейсхолдерами**.
   Контент студент заповнить сам після перегляду Module 1.
   Наповни лише 2 демо-питання quiz, щоб механіка була видима і клікабельна.
4. `lessons/w01/index.html` — зібраний з шаблону + `lesson.json`
5. `scripts/build_lesson.py` — збірка: читає `lesson.json`, валідує за схемою,
   вшиває в шаблон, пише `index.html`.
   Запуск: `python3 scripts/build_lesson.py w01`
   Тільки стандартна бібліотека + `jsonschema`. Без інших залежностей.

**Не вигадуй навчальний контент.** Демо-питання можуть бути про сам
4D-фреймворк на базі загальновідомого, але все інше — `TODO`.
Наповнення уроку — робота студента, і в цьому весь сенс.

---

## Завдання 3 — скаффолд тижня

`templates/week-scaffold/` — набір порожніх файлів із шапками:
`lesson.json` (скелет), `prep.md`, `agenda.md`, `friction.md`, `audio/.gitkeep`.

`scripts/new_week.sh w02` — копіює скаффолд у `lessons/w02/`, підставляє
номер тижня в шапки, не перезаписує наявне.

---

## Acceptance criteria

- [ ] `tree -L 3` збігається з цільовим деревом
- [ ] `legacy/` не змінено (перевір `git status`)
- [ ] Жоден файл не видалено
- [ ] Усі шляхи в перенесених `.md` оновлено, битих посилань немає
- [ ] `open lessons/w01/index.html` — сторінка відкривається з `file://`,
      без консольних помилок, без запитів у мережу
- [ ] Quiz працює: вибір → фідбек саме до обраної опції → блокування → Next
- [ ] Фідбек показується і для правильної, і для обох неправильних
- [ ] `python3 scripts/build_lesson.py w01` відпрацьовує без помилок
- [ ] Навмисно зламай `lesson.json` (прибери один `feedback`) — білд має
      **впасти з чітким повідомленням**. Поверни назад
- [ ] `bash scripts/new_week.sh w02` створює папку, потім видали її
- [ ] Зроблено коміт

---

## Шаблон звіту

Пиши у `transport-CLI-to-desktop.md`, новий блок **згори**:

```markdown
## T-001 — <дата, час>

### Done
- ...

### Tree after
```
<вивід tree -L 3>
```

### Decisions
Рішення, які довелось ухвалити самостійно, і чому.

### Questions
Що незрозуміло або суперечливо. Нумерований список — на них буде відповідь.

### Blockers
Що не вдалося зробити і чому.

### Files changed
- created: ...
- moved: ...
- edited: ...
```

---

## Обмеження

- Нічого не видаляти
- Не встановлювати залежності без запиту в `Questions`
- Не чіпати `legacy/`
- Не наповнювати навчальний контент — тільки структуру і механіку
- Не додавати зовнішні бібліотеки в HTML за жодних обставин
