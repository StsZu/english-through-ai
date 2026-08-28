# Baseline & Error Loop — протокол

Мета: отримати вимірювану нульову точку і потім щотижня бачити дельту
в цифрах, а не у відчуттях.

---

## Частина 1. Baseline (робиться ОДИН раз, до першого уроку)

### Правила

1. **Англійською. Усно. Записом.** Письмовий текст не годиться — він не
   діагностує ні часи, ні артиклі, ні швидкість, ні вимову.
2. **Без нотаток, без плану, без підготовки.**
3. **Без перезапису.** Перший дубль і є baseline. Затинання — це дані,
   а не провал.
4. Рівно 3 хвилини. Таймер.

### Процедура

1. Диктофон на телефоні. Файл → `recordings/w00_baseline.m4a`
2. Питання: **"What do you know about AI?"**
3. Говорити 3 хвилини. Не знаєте слова — опишіть іншими словами і йдіть далі.
4. Зупинити. Не слухати. Не переробляти.

### Транскрипція

Завантажити аудіо в ChatGPT або Gemini:

```
Transcribe this audio verbatim, including hesitations, false starts,
repetitions and grammatical errors. Do not correct anything.
Do not clean it up. Output plain text only.
```

→ `recordings/w00_baseline.txt`

### Діагностика

Транскрипт → Claude Project:

```
You are an ESL diagnostician. Learner level: B1. Target: B2.

TRANSCRIPT OF A SPOKEN MONOLOGUE:
<<<paste>>>

DURATION_SECONDS: <<<number>>>

Return ONLY JSON, no fences:
{
 "wpm": int,
 "cefr_estimate": "A2|B1|B1+|B2",
 "type_token_ratio": float,
 "filler_count": int,
 "errors": [
   {"type":"tense|article|preposition|word_order|lexis|pronunciation",
    "utterance":"...",
    "correction":"...",
    "why_b1":"one short explanation a B1 learner will understand"}
 ],
 "top5_drill": ["five specific things to practise before the next session"],
 "strengths": ["..."],
 "content_accuracy": [
   {"claim":"...","verdict":"correct|imprecise|wrong","fix":"..."}
 ]
}
```

→ `errors/w00.json`

**Блок `content_accuracy` важливий не менше за граматику.** Він ловить
концептуальні помилки — наприклад, плутанину між `training` (ваги моделі,
назавжди) і `runtime loop` (контекстне вікно, зникає після сесії).

---

## Частина 2. Error Loop (щотижня)

Після кожного 3-хвилинного виступу на уроці:

```
recordings/wNN_talk.m4a
   -> транскрипція (той самий промпт)
   -> діагностика (той самий промпт + блок нижче)
   -> errors/wNN.json
```

Додати до промпту діагностики:

```
RECURRING ERRORS FROM PREVIOUS SESSIONS:
<<<paste the "errors" arrays from earlier errors/*.json>>>

For every error, set "recurring": true if it appears in the history above.
Sort the output so recurring errors come first.
```

Помилки з `recurring: true` йдуть у блок 10–20 хв наступного уроку —
це і є персональна програма граматики, зібрана з реальних даних, а не
з підручника.

---

## Частина 3. Метрики прогресу

Раз на 4 тижні звести в `errors/progress.md`:

| Метрика | w00 | w04 | w08 | w12 | Напрям |
|---|---|---|---|---|---|
| wpm | | | | | вгору (ціль 110–130) |
| type_token_ratio | | | | | вгору |
| filler_count | | | | | вниз |
| errors total | | | | | вниз |
| recurring errors | | | | | вниз швидше за total |
| терміни в активі | | | | | вгору |

**Фінальний замір (тиждень 12):** той самий запис, те саме питання
"What do you know about AI?", та сама діагностика. Порівняти з w00.
