# ai_web_tests — starter для Lesson 1 «AI in Automation»

Мини-проект: Python + Selenium + pytest на публичном сайте https://www.saucedemo.com/

## Что внутри

| Файл | Зачем |
|---|---|
| `config.py` | URL, логин/пароль, headless, timeout — читается из `.env` |
| `conftest.py` | fixture `driver` (Chrome, закрывается после теста) |
| `pages/login_page.py` | Page Object страницы логина |
| `pages/products_page.py` | Page Object страницы Products |
| `tests/test_login.py` | один рабочий тест (baseline) |

## Подготовка ДО урока (10 минут)

Windows (PowerShell):

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
copy .env.example .env
pytest -v
```

macOS / Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
pytest -v
```

## Ожидаемый результат

```
tests/test_login.py::test_standard_user_can_login PASSED       [100%]
============================== 1 passed in ~5s ==============================
```

**Baseline = 1 passed.** Если у вас не так — напишите преподавателю ДО урока и приложите текст ошибки.

Нужен Google Chrome. Драйвер скачивается автоматически (Selenium Manager), отдельно ставить chromedriver не надо.

## Правила безопасности (важно для всего курса)

- `.env` не коммитим и никогда не отправляем в AI.
- Сегодняшние логин/пароль (`standard_user` / `secret_sauce`) — публичные данные учебного сайта. В реальном проекте так делать нельзя.
