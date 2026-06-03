# Руководство программиста

## Calendar Booking API — Бэкенд для тех, кто уже поел

*Если ты читаешь этот текст — ты уже пережил фронтенд. Здесь будет больно, но честно.*

---

# Оглавление

1. [Введение — ЗАЧЕМ ВСЁ ЭТО?](#глава-1-введение--зачем-всё-это)
   - 1.1. Аналогия с кухней
   - 1.2. Почему Python, а не Node.js
   - 1.3. FastAPI — что это и с чем едят
   - 1.4. SQLAlchemy — ORM, который не бесит
   - 1.5. SQLite — база данных в одном файле
   - 1.6. Схема работы приложения

2. [Как это запустить — ЖМИ НА КНОПКИ](#глава-2-как-это-запустить--жми-на-кнопки)
   - 2.1. Установка зависимостей
   - 2.2. Запуск сервера
   - 2.3. Swagger UI — твой лучший друг
   - 2.4. ReDoc — альтернативная документация
   - 2.5. Запуск тестов
   - 2.6. Миграции через Alembic

3. [Экскурсия по файлам — А ЧТО ТУТ У НАС?](#глава-3-экскурсия-по-файлам--а-что-тут-у-нас)
   - 3.1. Дерево файлов
   - 3.2. requirements.txt — список покупок
   - 3.3. .env — секретный файл
   - 3.4. .gitignore — что не пихать в git
   - 3.5. app/main.py — точка входа
   - 3.6. app/config.py — настройки
   - 3.7. app/database.py — движок базы данных
   - 3.8. app/models.py — описание таблиц
   - 3.9. app/schemas.py — что можно и что нельзя
   - 3.10. app/dependencies.py — шприц с данными
   - 3.11. app/routers/ — эндпоинты
   - 3.12. app/services/slots.py — мозг
   - 3.13. alembic.ini — миграции

4. [Жизненный цикл запроса — ДАННЫЕ ПУТЕШЕСТВУЮТ](#глава-4-жизненный-цикл-запроса--данные-путешествуют)
   - 4.1. Полный путь запроса
   - 4.2. Шаг 1: GET /api/event-types
   - 4.3. Шаг 2: GET /api/event-types/{id}/slots
   - 4.4. Шаг 3: POST /api/bookings
   - 4.5. Шаг 4: POST /api/admin/event-types
   - 4.6. Шаг 5: GET /api/admin/bookings
   - 4.7. Что если что-то пошло не так

5. [Тесты — КАК НЕ ОБОСРАТЬСЯ В ПРОДАКШЕНЕ](#глава-5-тесты--как-не-обосраться-в-продакшене)
   - 5.1. Почему тесты важны
   - 5.2. Структура тестов
   - 5.3. conftest.py — подготовка сцены
   - 5.4. Тест-кейсы: что покрываем
   - 5.5. Как работает in-memory SQLite
   - 5.6. Фикстуры pytest-asyncio

6. [FastAPI для начинающих — МАГИЯ БЕЗ МАГИИ](#глава-6-fastapi-для-начинающих--магия-без-магии)
   - 6.1. Что такое FastAPI
   - 6.2. Роутеры и декораторы
   - 6.3. Path и Query параметры
   - 6.4. Request Body (Pydantic)
   - 6.5. Depends — внедрение зависимостей
   - 6.6. HTTP статус-коды
   - 6.7. Обработка ошибок

7. [SQLAlchemy для выживших — ORM БЕЗ СЛЁЗ](#глава-7-sqlalchemy-для-выживших--orm-без-слёз)
   - 7.1. Что такое ORM
   - 7.2. Модели — отражение таблиц
   - 7.3. Типы колонок и их маппинг
   - 7.4. Запросы: select, where, order_by
   - 7.5. AsyncSession — асинхронные запросы
   - 7.6. Отношения (relationship)
   - 7.7. Миграции через Alembic

8. [Словарик — ЧТО ЭТА ХРЕНЬ ЗНАЧИТ?](#глава-8-словарик--что-эта-хрень-значит)

9. [Часто задаваемые вопросы — А ЧТО, ЕСЛИ...](#глава-9-часто-задаваемые-вопросы--а-что-если)
   - 9.1. База данных не создаётся
   - 9.2. SQLite выговорит "database is locked"
   - 9.3. Двойная бронь не блокируется
   - 9.4. Хочу перейти на PostgreSQL
   - 9.5. Порт 8000 уже занят
   - 9.6. Фронтенд не видит бэкенд
   - 9.7. Тесты падают с timezone-ошибками

---

# Глава 1. Введение — ЗАЧЕМ ВСЁ ЭТО?

## 1.1. Аналогия с кухней

Представь, что наше приложение — это ресторан. Фронтенд — это зал с официантами. Бэкенд — это кухня.

| На кухне | В реальности | В нашем проекте |
|----------|--------------|-----------------|
| **Повар** | Готовит блюда | **FastAPI** — обрабатывает запросы |
| **Холодильник** | Хранит продукты | **SQLite** — база данных |
| **Поварская книга** | Рецепты блюд | **SQLAlchemy** — описание таблиц |
| **Меню** | Что можно заказать | **Pydantic схемы** — что можно прислать/получить |
| **Нож** | Режет продукты | **Alembic** — миграции БД |
| **Формы для выпечки** | Шаблоны блюд | **Роутеры** — шаблоны эндпоинтов |

Официант (фронтенд) приносит заказ на кухню (HTTP-запрос). Повар (FastAPI) читает рецепт (роутер), достаёт продукты из холодильника (SQLite через SQLAlchemy), готовит блюдо и отдаёт официанту.

## 1.2. Почему Python, а не Node.js

Потому что фронтенд уже на том стеке, а бэкенд на Python — это классика. Python — язык для бэкенда, Node.js — для фронтенда. Можно было взять Django, но он как комбайн — для пяти эндпоинтов тащить целый Django — это стрелять из пушки по воробьям.

FastAPI даёт:
- Асинхронность (не блокируется пока ждёт БД)
- Автоматический Swagger (дока сама себя пишет)
- Pydantic-валидацию (типы на входе и выходе)
- Стартует за секунду

## 1.3. FastAPI — что это и с чем едят

FastAPI — это фреймворк для REST API на Python. Он:
- Берёт твою функцию с аннотациями типов
- Автоматически валидирует входные данные
- Генерирует OpenAPI спецификацию
- Рисует Swagger UI

Пример минимального эндпоинта:

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/hello")
async def say_hello(name: str = "World") -> dict:
    return {"message": f"Hello, {name}!"}
```

FastAPI видит: `name: str = "World"` — это query-параметр. По умолчанию `"World"`. Возвращаемый тип — `dict`, но можно указать Pydantic-схему.

Запускаешь — открываешь `/docs` — видишь интерактивную документацию.

## 1.4. SQLAlchemy — ORM, который не бесит

SQLAlchemy — это прослойка между Python и базой данных. Вместо того чтобы писать:

```sql
SELECT * FROM event_types WHERE name = 'Chat';
```

Ты пишешь:

```python
result = await db.execute(select(EventType).where(EventType.name == "Chat"))
```

SQLAlchemy превратит это в SQL, выполнит, вернёт Python-объекты.

**Зачем это нужно:**
- Не пишешь SQL руками (меньше ошибок)
- Можно сменить базу данных (SQLite → PostgreSQL) без изменения кода
- Типизация: IDE подсказывает поля
- Безопасность: SQLAlchemy экранирует значения (защита от SQL-инъекций)

## 1.5. SQLite — база данных в одном файле

SQLite — это БД, которая живёт в одном файле `app.db`. Не нужно устанавливать сервер, настраивать пользователей, открывать порты. Файл есть — база работает.

**Когда подходит:**
- Разработка на локальной машине
- Прототипы и пет-проекты
- Приложения с одним пользователем-админом

**Когда не подходит:**
- Много одновременных записей (SQLite блокирует файл при записи)
- Нагрузка > 100 запросов в секунду

Наш проект — ровно первый случай: один админ, горстка гостей.

## 1.6. Схема работы приложения

```
Браузер (фронтенд)                    FastAPI (бэкенд)              SQLite (БД)
      │                                      │                         │
      │  GET /api/event-types                │                         │
      │─────────────────────────────────────>│                         │
      │                                      │  SELECT * FROM          │
      │                                      │  event_types            │
      │                                      │────────────────────────>│
      │                                      │                         │
      │                                      │  ┌──────────────────┐   │
      │                                      │  │ EventType(id=..) │   │
      │                                      │  │ EventType(id=..) │   │
      │                                      │  │ EventType(id=..) │   │
      │                                      │  └──────────────────┘   │
      │                                      │<────────────────────────│
      │                                      │                         │
      │  [{"id":"...","name":"Chat",...}]    │                         │
      │<─────────────────────────────────────│                         │
      │                                      │                         │
```

**Ключевой момент:** FastAPI — асинхронный. Пока он ждёт ответ от SQLite, он может обслуживать другие запросы. Это не значит, что запросы летят быстрее — но сервер не зависает на одном медленном запросе.

---

# Глава 2. Как это запустить — ЖМИ НА КНОПКИ

## 2.1. Установка зависимостей

Убедись, что у тебя установлен Python 3.10+. Проверить:

```bash
python --version
# Python 3.14.3 — ок
```

Создай виртуальное окружение (чтобы не засирать систему) и установи пакеты:

```bash
cd backend
python -m venv .venv           # создать изолированное окружение

# Windows:
.\.venv\Scripts\pip install -r requirements.txt

# macOS / Linux:
# source .venv/bin/activate
# pip install -r requirements.txt
```

**Что такое виртуальное окружение?** Представь, что каждая программа — это ребёнок с чемоданом игрушек. Если все дети сложат игрушки в общую кучу — начнётся ад (один хочет Pydantic v1, другой v2). Виртуальное окружение даёт каждому свой чемодан. `.venv` — этот чемодан.

**Что скачается:**

| Пакет | Зачем | Вес |
|-------|-------|-----|
| `fastapi` | Сам фреймворк | 15 MB |
| `uvicorn` | Сервер, который запускает FastAPI | 5 MB |
| `sqlalchemy` | ORM для работы с БД | 10 MB |
| `alembic` | Миграции (версионирование БД) | 3 MB |
| `pydantic` | Валидация данных (FastAPI использует внутри) | 8 MB |
| `aiosqlite` | Асинхронный драйвер для SQLite | 1 MB |
| `pytest` | Тесты | 7 MB |
| `httpx` | Клиент для тестов | 5 MB |

## 2.2. Запуск сервера

```bash
cd backend

# Способ 1: fastapi dev (рекомендуется)
fastapi dev app/main.py --port 8000

# Способ 2: uvicorn напрямую
uvicorn app.main:app --reload --port 8000
```

Разницы почти нет. `fastapi dev` — это обёртка над uvicorn с авторелоадом.

**Флаг `--reload`**: сервер перезапускается сам, когда ты меняешь файлы. Как `runserver` в Django. Не используй на продакшене — жрёт память.

После запуска:
- API доступно на `http://localhost:8000`
- Swagger UI на `http://localhost:8000/docs`
- ReDoc на `http://localhost:8000/redoc`

## 2.3. Swagger UI — твой лучший друг

Открой `http://localhost:8000/docs`. Ты увидишь страницу со списком всех эндпоинтов:

```
Calendar Booking API
┌─────────────────────────────────────────────────┐
│  GET  /api/event-types          [Try it out]    │
│  GET  /api/event-types/{id}/slots [Try it out]  │
│  POST /api/bookings             [Try it out]    │
│  POST /api/admin/event-types    [Try it out]    │
│  GET  /api/admin/bookings       [Try it out]    │
└─────────────────────────────────────────────────┘
```

**Как тестировать:**

1. Нажми на нужный эндпоинт → раскроется
2. Нажми **Try it out** — появится форма ввода
3. Заполни параметры (если нужны)
4. Нажми **Execute**
5. Смотри результат: статус-код, заголовки, тело ответа

**Твой первый тестовый сценарий:**

```
Шаг 1: POST /api/admin/event-types
Body: {"name": "30-min Chat", "description": "Quick call", "duration_minutes": 30}
Ожидаем: 201 Created + объект с id

Шаг 2: GET /api/event-types
Ожидаем: 200 OK + массив с одним элементом

Шаг 3: GET /api/event-types/{id}/slots
Подставь id из шага 1
Ожидаем: 200 OK + массив слотов на 14 дней

Шаг 4: POST /api/bookings
Body: {"event_type_id": "<id>", "start_time": "2026-06-02T10:00:00"}
Ожидаем: 201 Created

Шаг 5: POST /api/bookings (снова с тем же временем)
Ожидаем: 409 Conflict — "This time slot is already booked"
```

## 2.4. ReDoc — альтернативная документация

Открой `http://localhost:8000/redoc`. Это та же OpenAPI-спецификация, но в другом оформлении. Swagger удобнее для тестирования, ReDoc — для чтения и печати.

## 2.5. Запуск тестов

```bash
cd backend
pytest -v
```

Флаг `-v` (verbose) — показывает каждый тест по имени. Без него — только точки и итог.

Ты увидишь что-то вроде:

```
tests/test_admin.py::test_admin_bookings_empty PASSED
tests/test_admin.py::test_admin_bookings_shows_upcoming PASSED
tests/test_bookings.py::test_create_booking PASSED
tests/test_bookings.py::test_double_booking_conflict PASSED
tests/test_bookings.py::test_double_booking_different_event_types PASSED
...
============================= 13 passed in 0.41s ==============================
```

13 тестов, 0.41 секунды. Быстро, потому что in-memory SQLite.

## 2.6. Миграции через Alembic

Alembic — это система контроля версий для базы данных. Она отслеживает изменения схемы и позволяет применять/откатывать их.

**Создать новую миграцию:**

```bash
alembic revision --autogenerate -m "add new field"
```

Но в этом проекте мы не используем автогенерацию (она работает нестабильно с асинхронным SQLAlchemy). Миграции пишем руками.

**Применить миграции:**

```bash
alembic upgrade head
```

**Откатить последнюю:**

```bash
alembic downgrade -1
```

**Текущая миграция (`0001`)** создаёт две таблицы: `event_types` и `bookings`. Она уже написана, применять необязательно — FastAPI сам создаёт таблицы при старте (`create_all` в `lifespan`). Миграция — на случай, если хочешь контролируемый процесс.

---

# Глава 3. Экскурсия по файлам — А ЧТО ТУТ У НАС?

## 3.1. Дерево файлов

```
backend/                                          ← корень бэкенда
│
├── .env                                          ← настройки (не в git!)
├── .env.example                                  ← пример настроек (шаблон)
├── .gitignore                                    ← что не пихать в git
├── requirements.txt                              ← список зависимостей (pip)
├── alembic.ini                                   ← конфиг миграций
├── GUIDE.md                                      ← то, что ты сейчас читаешь
│
├── migrations/                                   ← миграции (версии БД)
│   ├── env.py                                    ← настройка окружения для миграций
│   ├── script.py.mako                            ← шаблон для новых миграций
│   └── versions/
│       └── 0001_add_event_types_and_bookings.py  ← первая миграция
│
├── app/                                          ← исходный код
│   ├── __init__.py                               ← пустой, нужен Python
│   ├── main.py                                   ← точка входа, запуск FastAPI
│   ├── config.py                                 ← настройки из .env
│   ├── database.py                               ← движок SQLAlchemy + сессия
│   ├── models.py                                 ← SQLAlchemy модели (таблицы)
│   ├── schemas.py                                ← Pydantic схемы (валидация)
│   ├── dependencies.py                           ← функции для Depends()
│   │
│   ├── routers/                                  ← эндпоинты
│   │   ├── __init__.py                           ← пустой
│   │   ├── event_types.py                        ← GET /api/event-types
│   │   ├── slots.py                              ← GET /api/event-types/{id}/slots
│   │   ├── bookings.py                           ← POST /api/bookings
│   │   └── admin.py                              ← POST admin/event-types + GET admin/bookings
│   │
│   └── services/                                 ← бизнес-логика
│       ├── __init__.py                           ← пустой
│       └── slots.py                              ← генерация слотов
│
└── tests/                                        ← тесты
    ├── __init__.py                               ← пустой
    ├── conftest.py                               ← фикстуры для тестов
    ├── test_event_types.py
    ├── test_slots.py
    ├── test_bookings.py
    └── test_admin.py
```

## 3.2. requirements.txt — «Список покупок в Пятёрочке»

```txt
fastapi>=0.115.0
uvicorn[standard]>=0.30.0
sqlalchemy>=2.0.0
alembic>=1.13.0
pydantic>=2.0.0
pydantic-settings>=2.0.0
aiosqlite>=0.20.0

pytest>=8.0.0
pytest-asyncio>=0.24.0
httpx>=0.27.0
```

**Символ `>=`**: «возьми версию не ниже указанной». Если у тебя уже стоит 0.30.0 — оставь. Если стоит 0.28.0 — обнови.

**Разделение пустой строкой**: зависимости (нужны для работы) и dev-зависимости (нужны только для разработки). Чисто визуально.

**`[standard]` у uvicorn**: устанавливает дополнительный набор инструментов — поддержка WebSocket, watchfiles (авторелоад), поддержка HTTP/2. Без `[standard]` авторелоад не работает.

**Зачем столько всего?** Каждый пакет делает ровно одну вещь:

| Задача | Пакет |
|--------|-------|
| Обработать HTTP-запрос | `fastapi` |
| Запустить сервер | `uvicorn` |
| Сгенерировать SQL | `sqlalchemy` |
| Версионировать БД | `alembic` |
| Валидировать JSON | `pydantic` |
| Читать .env файл | `pydantic-settings` |
| Стучаться в SQLite асинхронно | `aiosqlite` |
| Писать тесты | `pytest` + `pytest-asyncio` |
| Делать HTTP-запросы в тестах | `httpx` |

Django делает всё это в одном флаконе. FastAPI — конструктор Lego. Ты сам собираешь то, что нужно.

## 3.3. .env — «Секретный файл»

```
DATABASE_URL=sqlite+aiosqlite:///./app.db
```

В этом файле — настройки окружения. Сейчас одна: URL базы данных. Он разбирается так:

```
sqlite+aiosqlite:///./app.db
│      │              │    │
│      │              │    └── имя файла БД (app.db)
│      │              └────── директория ./ (рядом с main.py)
│      └───────────────────── асинхронный драйвер
└──────────────────────────── тип БД (SQLite)
```

Когда перейдёшь на PostgreSQL, строка станет:

```
DATABASE_URL=postgresql+asyncpg://user:password@localhost:5432/calendar
```

**Почему `.env` в `.gitignore`?** Потому что в `.env` могут быть пароли, токены, ключи. Даже если их нет сейчас — привычка должна быть. В git попадает только `.env.example` — шаблон без секретов.

**Как это работает:** `pydantic-settings` читает `.env` при старте, загружает значения в объект `Settings`. В коде обращаешься к `settings.database_url`.

```python
from app.config import settings

print(settings.database_url)  # sqlite+aiosqlite:///./app.db
```

## 3.4. .gitignore — «Что не пихать в git»

```
__pycache__/
*.pyc
*.pyo
*.db
.env
.venv/
venv/
*.egg-info/
dist/
build/
.pytest_cache/
.mypy_cache/
```

Почти всё то же самое, что в UI, но добавлено:
- `*.db` — файлы SQLite (они разные на каждой машине)
- `__pycache__/`, `*.pyc` — скомпилированные Python-файлы (создаются автоматически)
- `.venv/`, `venv/` — виртуальные окружения (их не носят в git, каждый создаёт своё)
- `.pytest_cache/` — кеш тестов

## 3.5. app/main.py — «Точка входа, где всё начинается»

```python
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import Base, engine
from app.routers import admin, bookings, event_types, slots


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield


app = FastAPI(title="Calendar Booking API", lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(event_types.router)
app.include_router(slots.router)
app.include_router(bookings.router)
app.include_router(admin.router)
```

### lifespan — «Жизненный цикл приложения»

`lifespan` — это корутина, которая выполняется:
- При старте сервера (до первого запроса)
- При остановке сервера (после последнего запроса)

В нашем случае при старте выполняется:

```python
async with engine.begin() as conn:
    await conn.run_sync(Base.metadata.create_all)
```

Это создаёт таблицы в базе данных, если их ещё нет. Таблицы описаны в `models.py`, а `Base` — в `database.py`.

`run_sync` — мост между async и sync: SQLAlchemy умеет создавать таблицы только в синхронном режиме, a `run_sync` позволяет вызвать синхронную функцию внутри асинхронного кода.

`yield` — разделяет код при старте (до yield) и при остановке (после yield). После yield у нас ничего нет — при остановке ничего делать не надо.

### CORSMiddleware — «Пропуск для чужих доменов»

CORS (Cross-Origin Resource Sharing) — механизм безопасности браузера. Если фронтенд на `localhost:5173`, а бэкенд на `localhost:8000` — это разные домены. Браузер не даст им общаться без специального разрешения.

```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],      # разрешить с любого домена
    allow_methods=["*"],      # разрешить GET, POST и т.д.
    allow_headers=["*"],      # разрешить любые заголовки
)
```

В продакшене `allow_origins` лучше ограничить конкретным доменом (`["https://myapp.com"]`). Но для разработки `*` — норма.

### include_router — «Подключение эндпоинтов»

```python
app.include_router(event_types.router)
```

Каждый файл в `routers/` создаёт свой `APIRouter` с группой эндпоинтов. `include_router` подключает их к главному приложению. Без этой строки эндпоинты не будут работать — FastAPI о них просто не узнает.

## 3.6. app/config.py — «Настройки из .env»

```python
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    database_url: str = "sqlite+aiosqlite:///./app.db"
    model_config = {"env_file": ".env"}


settings = Settings()
```

Класс `Settings` — это Pydantic-модель. При создании (`Settings()`) она:
1. Проверяет переменные окружения (например, `DATABASE_URL`)
2. Если не найдено — читает `.env`
3. Если и там нет — использует значение по умолчанию (`"sqlite+aiosqlite:///./app.db"`)

`database_url: str` — тип str, Pydantic не будет преобразовывать, просто проверит, что это строка.

**Почему не `os.getenv`?** `pydantic-settings` даёт типизацию, подсказки в IDE, валидацию и значение по умолчанию в одном месте.

## 3.7. app/database.py — «Движок базы данных»

```python
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine, AsyncSession
from sqlalchemy.orm import DeclarativeBase
from app.config import settings


engine = create_async_engine(settings.database_url, echo=False)
async_session = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


class Base(DeclarativeBase):
    pass
```

**engine** — движок SQLAlchemy. Он:
- Хранит пул подключений к базе
- Преобразует Python-типы в SQL-типы и обратно
- Логирует запросы (если `echo=True`)

`create_async_engine` — асинхронная версия. Для работы нужен асинхронный драйвер (у нас `aiosqlite`).

**async_session** — фабрика сессий. `async_sessionmaker(...)` возвращает не сессию, а фабрику, которая умеет создавать сессии. При каждом запросе мы вызываем `async_session()`, получаем новую сессию, делаем запросы и закрываем её.

**Base** — базовый класс для всех моделей. Каждая модель наследуется от `Base`. SQLAlchemy знает: всё, что наследуется от `Base` — это таблица.

## 3.8. app/models.py — «Описание таблиц»

```python
import uuid
from datetime import datetime
from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database import Base


def new_uuid() -> str:
    return str(uuid.uuid4())


class EventType(Base):
    __tablename__ = "event_types"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=new_uuid)
    name: Mapped[str] = mapped_column(String(255))
    description: Mapped[str] = mapped_column(String(1000))
    duration_minutes: Mapped[int]

    bookings: Mapped[list["Booking"]] = relationship(back_populates="event_type")


class Booking(Base):
    __tablename__ = "bookings"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=new_uuid)
    event_type_id: Mapped[str] = mapped_column(ForeignKey("event_types.id"))
    start_time: Mapped[datetime] = mapped_column()
    end_time: Mapped[datetime] = mapped_column()

    event_type: Mapped["EventType"] = relationship(back_populates="bookings")
```

### Что такое `Mapped[тип]`

`Mapped[str]` — аннотация, которая говорит SQLAlchemy: «это поле типа str». Используется вместо старомодного `Column(String)`.

### Поля модели EventType

| Поле | Тип в Python | Тип в SQLite | Назначение |
|------|-------------|-------------|------------|
| `id` | `str` (36 символов) | `TEXT` | UUID — уникальный идентификатор |
| `name` | `str` (макс 255) | `TEXT` | Название типа события |
| `description` | `str` (макс 1000) | `TEXT` | Описание |
| `duration_minutes` | `int` | `INTEGER` | Длительность в минутах |

**Почему id — строка, а не int?** UUID — это 36 символов вида `"a1b2c3d4-e5f6-7890-abcd-ef1234567890"`. Они не повторяются даже если два админа одновременно создадут типы. Int-автоинкремент может пересечься при миграции данных.

### Поля модели Booking

| Поле | Тип | Назначение |
|------|-----|-----------|
| `id` | `str` | UUID |
| `event_type_id` | `str` (FK → event_types.id) | Какой тип события бронируют |
| `start_time` | `datetime` | Когда начинается бронь (UTC) |
| `end_time` | `datetime` | Когда заканчивается (start + duration) |

### ForeignKey — внешний ключ

```python
event_type_id: Mapped[str] = mapped_column(ForeignKey("event_types.id"))
```

Это говорит SQLite: «поле `event_type_id` ссылается на `id` в таблице `event_types`». SQLite проверит, что при создании брони такой тип события существует. Если нет — ошибка.

### relationship — связи между таблицами

```python
# В EventType:
bookings: Mapped[list["Booking"]] = relationship(back_populates="event_type")

# В Booking:
event_type: Mapped["EventType"] = relationship(back_populates="bookings")
```

Это **не колонки в таблице**. Это удобные обращения:
- `event_type.bookings` — получить все брони для этого типа
- `booking.event_type` — получить тип события для этой брони

Без `relationship` пришлось бы писать запросы вручную. С ним — просто обращение к свойству.

### Почему start_time и end_time — `datetime`, а `end_time` не вычисляется каждый раз?

`end_time` мог бы вычисляться как `start_time + duration_minutes`, но мы явно храним его в БД. Почему?

**Чтобы быстро проверять пересечения броней.** Запрос на поиск пересечений:

```sql
SELECT * FROM bookings
WHERE start_time < :new_end AND end_time > :new_start
```

Работает мгновенно, если `end_time` уже есть в таблице. Если бы его не было, пришлось бы делать JOIN с `event_types` и вычислять на лету — запрос был бы медленнее и сложнее.

## 3.9. app/schemas.py — «Что можно и что нельзя»

```python
from datetime import datetime
from pydantic import BaseModel, field_validator


class EventTypeCreate(BaseModel):
    name: str
    description: str
    duration_minutes: int

    @field_validator("duration_minutes")
    @classmethod
    def must_be_positive(cls, v: int) -> int:
        if v < 1:
            raise ValueError("duration_minutes must be positive")
        return v


class EventTypeResponse(BaseModel):
    id: str
    name: str
    description: str
    duration_minutes: int


class BookingCreate(BaseModel):
    event_type_id: str
    start_time: datetime


class BookingResponse(BaseModel):
    id: str
    event_type_id: str
    start_time: datetime
    end_time: datetime


class TimeSlot(BaseModel):
    start_time: datetime
    end_time: datetime
```

Pydantic-схемы — это «фотороботы» данных. Они описывают:
- Какие поля есть
- Какого они типа
- Какие значения допустимы

**EventTypeCreate** — что нужно отправить, чтобы создать тип события. Отличается от `EventTypeResponse` отсутствием `id` (ID присваивает сервер).

**BookingCreate** — что нужно для бронирования. Только `event_type_id` и `start_time`. `end_time` вычисляет сервер.

**BookingResponse** — что возвращает сервер после бронирования. Содержит `end_time`.

**TimeSlot** — слот времени. Возвращается списком для календаря.

### Валидация через field_validator

```python
@field_validator("duration_minutes")
@classmethod
def must_be_positive(cls, v: int) -> int:
    if v < 1:
        raise ValueError("duration_minutes must be positive")
    return v
```

`field_validator` — декоратор, который вешается на метод класса. Он проверяет значение поля после парсинга JSON, но до сохранения.

Проверка: если `duration_minutes` меньше 1 — ошибка 422. Это защита от:

```json
{"name": "Chat", "description": "x", "duration_minutes": 0}
```

Сервер не упадёт с загадочной ошибкой «деление на ноль» — он вежливо скажет: «длительность должна быть положительной».

## 3.10. app/dependencies.py — «Шприц с данными»

```python
from app.database import async_session


async def get_db():
    async with async_session() as session:
        yield session
```

Это **зависимость** (dependency). Функция, которая:
1. Создаёт сессию БД (async_session())
2. Отдаёт её тому, кто запросил (yield)
3. После использования закрывает сессию (выход из async with)

**Внедрение зависимостей** (Dependency Injection) — это когда функция не создаёт ресурс сама, а просит его "на вход". FastAPI связывает поставщика (get_db) и потребителя (роутер) автоматически.

```python
@router.get("/api/event-types", response_model=list[EventTypeResponse])
async def list_event_types(db: AsyncSession = Depends(get_db)):
    # db уже открыта, можно работать
    result = await db.execute(select(EventType).order_by(EventType.name))
    return result.scalars().all()
    # после return db закроется автоматически
```

`Depends(get_db)` — FastAPI видит эту аннотацию, вызывает `get_db()`, получает сессию и передаёт её в параметр `db`. Магия.

**Что даёт**: для каждого запроса создаётся своя сессия. Если один запрос упадёт — сессия другого не пострадает. Нет утечек подключений.

## 3.11. app/routers/ — «Эндпоинты»

### event_types.py — список типов событий

```python
from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.dependencies import get_db
from app.models import EventType
from app.schemas import EventTypeResponse

router = APIRouter(prefix="/api/event-types", tags=["Guest: Event Types"])


@router.get("", response_model=list[EventTypeResponse])
async def list_event_types(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(EventType).order_by(EventType.name))
    return result.scalars().all()
```

Что здесь происходит:

1. `APIRouter` — создаём группу эндпоинтов с префиксом `/api/event-types`
2. `@router.get("")` — пустой путь, конечный URL: `GET /api/event-types`
3. `response_model=list[EventTypeResponse]` — обещаем вернуть список схем EventTypeResponse
4. `Depends(get_db)` — просим сессию БД
5. `select(EventType)` — SQL: `SELECT * FROM event_types ORDER BY name`
6. `result.scalars().all()` — достаём все строки как Python-объекты
7. FastAPI автоматически превращает объекты в JSON по схеме EventTypeResponse

**Почему `EventType` (модель) превращается в `EventTypeResponse` (схема)?** Потому что FastAPI видит `response_model=list[EventTypeResponse]`, берёт объекты EventType, достаёт из них поля (id, name, description, duration_minutes) и пакует в JSON по шаблону EventTypeResponse. Поля, которых нет в схеме (например, relationship `bookings`), игнорируются.

### slots.py — слоты

```python
@router.get("/api/event-types/{event_type_id}/slots", response_model=list[TimeSlot])
async def get_slots(
    event_type_id: str,
    date_from: datetime | None = None,
    date_to: datetime | None = None,
    db: AsyncSession = Depends(get_db),
):
    event_type = await db.get(EventType, event_type_id)
    if event_type is None:
        raise HTTPException(status_code=404, detail="Event type not found")

    now = datetime.now(timezone.utc)
    today_start = now.replace(hour=0, minute=0, second=0, microsecond=0)

    date_from = (date_from or today_start).replace(tzinfo=None)
    date_to = (date_to or (date_from + timedelta(days=14))).replace(tzinfo=None)

    if date_from >= date_to:
        return []

    return await generate_slots(
        duration_minutes=event_type.duration_minutes,
        date_from=date_from,
        date_to=date_to,
        db=db,
    )
```

Разбор по строкам:

**`{event_type_id}`** — динамический параметр пути. Часть URL, которая меняется (`/api/event-types/abc-123/slots`). FastAPI автоматически кладёт его в параметр `event_type_id`.

**`date_from: datetime | None = None`** — опциональный query-параметр. Можно передать `?date_from=2026-06-01T00:00:00`. Если не передан — `None`.

**Проверка существования:**
```python
event_type = await db.get(EventType, event_type_id)
```
Пытаемся найти тип события по ID. Если нет — 404.

**Формирование дат:**
```python
date_from = (date_from or today_start).replace(tzinfo=None)
```
Если дата не указана — берём сегодня. `.replace(tzinfo=None)` — отрезаем часовой пояс.

**Валидация диапазона:**
```python
if date_from >= date_to:
    return []
```
Если from позже to — слотов не будет.

**Делегирование:**
```python
return await generate_slots(...)
```
Вся логика генерации слотов — в `services/slots.py`. Роутер только готовит данные и вызывает.

### bookings.py — создание брони

```python
@router.post("", response_model=BookingResponse, status_code=status.HTTP_201_CREATED)
async def create_booking(body: BookingCreate, db: AsyncSession = Depends(get_db)):
    event_type = await db.get(EventType, body.event_type_id)
    if event_type is None:
        raise HTTPException(status_code=404, detail="Event type not found")

    start_time = _naive(body.start_time)
    end_time = start_time + timedelta(minutes=event_type.duration_minutes)

    if end_time <= _naive(datetime.now(timezone.utc)):
        raise HTTPException(status_code=400, detail="Cannot book a slot in the past")

    result = await db.execute(
        select(Booking).where(
            Booking.start_time < end_time,
            Booking.end_time > start_time,
        )
    )
    if result.first() is not None:
        raise HTTPException(status_code=409, detail="This time slot is already booked")

    booking = Booking(
        event_type_id=body.event_type_id,
        start_time=start_time,
        end_time=end_time,
    )
    db.add(booking)
    await db.commit()
    await db.refresh(booking)
    return booking
```

**Логика проверки на двойную бронь:**

```python
result = await db.execute(
    select(Booking).where(
        Booking.start_time < end_time,
        Booking.end_time > start_time,
    )
)
```

Этот запрос ищет любую существующую бронь, которая пересекается с новой. Условие пересечения двух отрезков [A, B) и [C, D):

```
A < D AND B > C
```

Расшифровка: A (начало существующей) раньше, чем D (конец новой), И B (конец существующей) позже, чем C (начало новой). Если оба условия верны — отрезки пересекаются.

**Проверка на прошлое:**

```python
if end_time <= _naive(datetime.now(timezone.utc)):
    raise HTTPException(status_code=400, detail="Cannot book a slot in the past")
```

Не даём бронировать время, которое уже прошло.

**`status_code=409`** — Conflict. Специальный код для «конфликт с существующими данными». Клиент (фронтенд) поймёт, что нужно показать «время занято».

### admin.py — админские эндпоинты

```python
@router.post("/event-types", response_model=EventTypeResponse, status_code=status.HTTP_201_CREATED)
async def create_event_type(body: EventTypeCreate, db: AsyncSession = Depends(get_db)):
    event_type = EventType(**body.model_dump())
    db.add(event_type)
    await db.commit()
    await db.refresh(event_type)
    return event_type


@router.get("/bookings", response_model=list[BookingResponse])
async def list_upcoming_bookings(db: AsyncSession = Depends(get_db)):
    now = datetime.now(timezone.utc).replace(tzinfo=None)
    result = await db.execute(
        select(Booking)
        .where(Booking.start_time >= now)
        .order_by(Booking.start_time)
    )
    return result.scalars().all()
```

**create_event_type:**
- Принимает `EventTypeCreate` (name, description, duration_minutes)
- Превращает в модель `EventType` через `body.model_dump()` (словарь)
- `**` распаковывает словарь в аргументы конструктора
- Добавляет в сессию, сохраняет, обновляет объект из БД (чтобы получить сгенерированный id)

**list_upcoming_bookings:**
- `Booking.start_time >= now` — только будущие брони
- `order_by(Booking.start_time)` — сортировка по времени (скоро ближайшие)

## 3.12. app/services/slots.py — «Мозг»

```python
async def generate_slots(
    duration_minutes: int,
    date_from: datetime,
    date_to: datetime,
    db: AsyncSession,
) -> list[TimeSlot]:
```

**Что делает:**
1. Запрашивает все брони в указанном окне дат
2. Генерирует сетку слотов (с шагом `duration_minutes`)
3. Исключает слоты, которые пересекаются с существующими бронями

**Генерация:**

Для каждого дня: от 00:00 до 23:59:59, шаг = duration_minutes.

Если duration_minutes = 30, то слоты:
```
00:00 - 00:30
00:30 - 01:00
01:00 - 01:30
...
23:30 - 00:00 (след. дня)
```

Последний слот обрывается на полуночи. Слотов, переходящих на следующий день, нет.

**Проверка пересечения:**

```python
overlap = any(
    existing_start < slot_end and existing_end > cursor
    for existing_start, existing_end in existing
)
```

Берём каждую бронь из списка и проверяем, пересекается ли она с кандидатом в слоты. Если хоть одна пересекается — слот недоступен.

**Два ключевых момента:**
- Все даты приводятся к naive (часовые пояса отрезаются) — чтобы сравнивать можно было
- В `existing` хранятся пары (start, end) — не нужно каждый раз обращаться к БД

## 3.13. alembic.ini — «Миграции»

Этот файл — конфиг для Alembic. В нём только одна важная строка:

```
sqlalchemy.url = sqlite+aiosqlite:///./app.db
```

URL базы данных. Alembic использует его, чтобы подключаться к БД и применять миграции.

Остальное — настройки логирования и форматирования. Можно не трогать.

**migrations/env.py** — настройка окружения:
- Загружает `Base.metadata` из `models.py` (чтобы Alembic знал о таблицах)
- Настраивает подключение (offline/online режим)

**migrations/versions/0001_...py** — первая миграция:

```python
def upgrade() -> None:
    op.create_table("event_types", ...)
    op.create_table("bookings", ...)

def downgrade() -> None:
    op.drop_table("bookings")
    op.drop_table("event_types")
```

`upgrade` — создать таблицы. `downgrade` — удалить (откат).

---

# Глава 4. Жизненный цикл запроса — ДАННЫЕ ПУТЕШЕСТВУЮТ

## 4.1. Полный путь запроса

```
Фронтенд (браузер)
    │
    │  HTTP-запрос (GET /api/event-types)
    ▼
Vite (прокси, порт 5173)
    │
    │  Перенаправляет на localhost:8000
    ▼
Uvicorn (принимает соединение)
    │
    │  Передаёт FastAPI
    ▼
FastAPI (разбирает запрос)
    │
    ├── Проверяет: есть ли такой путь?
    ├── Проверяет: правильные ли типы параметров?
    ├── Создаёт: сессию БД через get_db()
    ├── Вызывает: функцию-обработчик
    │
    ▼
Обработчик (роутер)
    │
    │  SQLAlchemy-запрос
    ▼
БД (SQLite)
    │
    │  Ответ
    ▼
Обработчик
    │
    │  Pydantic-схема → JSON
    ▼
FastAPI
    │
    │  HTTP-ответ
    ▼
Фронтенд (браузер)
```

## 4.2. Шаг 1: GET /api/event-types

```
Запрос: GET /api/event-types
       ↓
FastAPI находит роутер event_types.list_event_types
       ↓
get_db() создаёт сессию БД
       ↓
db.execute(select(EventType).order_by(EventType.name))
       ↓
SQL: SELECT id, name, description, duration_minutes
     FROM event_types ORDER BY name
       ↓
SQLite возвращает строки
       ↓
SQLAlchemy превращает строки в объекты EventType
       ↓
FastAPI превращает EventType → EventTypeResponse (JSON)
       ↓
Ответ: 200 [{"id":"...","name":"Chat",...}, ...]
```

## 4.3. Шаг 2: GET /api/event-types/{id}/slots

```
Запрос: GET /api/event-types/abc-123/slots?date_from=...&date_to=...
       ↓
FastAPI достаёт event_type_id = "abc-123" из URL
date_from и date_to из query-параметров
       ↓
Проверка: существует ли EventType с id="abc-123"?
       ↓
Если нет → 404
Если да → вычисляем date_from и date_to (по умолчанию сегодня + 14 дней)
       ↓
generate_slots(duration=30, date_from=..., date_to=..., db)
       ↓
1. SELECT * FROM bookings WHERE start_time < date_to AND end_time > date_from
   (все брони в этом окне)
       ↓
2. Для каждого дня в [date_from, date_to):
     для каждого 30-минутного интервала:
       если интервал не пересекается ни с одной бронью:
         добавить в список
       ↓
3. Вернуть список TimeSlot[]
       ↓
Ответ: 200 [{"start_time":"...","end_time":"..."}, ...]
```

## 4.4. Шаг 3: POST /api/bookings

```
Запрос: POST /api/bookings
Body: {"event_type_id": "abc-123", "start_time": "2026-06-02T10:00:00"}
       ↓
Pydantic валидирует тело: поля есть, типы правильные
       ↓
Проверка: существует ли EventType "abc-123"?
  Нет  → 404
  Да   → вычисляем end_time = start_time + 30 мин
       ↓
Проверка: end_time в прошлом?
  Да   → 400 "Cannot book a slot in the past"
       ↓
Проверка пересечений:
  SELECT * FROM bookings
  WHERE start_time < :end_time AND end_time > :start_time
       ↓
  Найдена бронь? → 409 "Time slot is already booked"
  Нет → создаём Booking, сохраняем в БД
       ↓
Ответ: 201 {"id":"...","event_type_id":"...","start_time":"...","end_time":"..."}
```

## 4.5. Шаг 4: POST /api/admin/event-types

```
Запрос: POST /api/admin/event-types
Body: {"name": "Consultation", "description": "1-on-1", "duration_minutes": 60}
       ↓
Pydantic валидация: duration_minutes >= 1? → да
       ↓
EventType(name="Consultation", description="1-on-1", duration_minutes=60)
       ↓
db.add(event_type) — планируем запись
db.commit() — выполняем INSERT
db.refresh(event_type) — загружаем сгенерированный id из БД
       ↓
Ответ: 201 {"id":"new-uuid","name":"Consultation",...}
```

## 4.6. Шаг 5: GET /api/admin/bookings

```
Запрос: GET /api/admin/bookings
       ↓
db.execute(
  select(Booking)
  .where(Booking.start_time >= now)
  .order_by(Booking.start_time)
)
       ↓
SQL: SELECT * FROM bookings
     WHERE start_time >= '2026-06-01T22:00:00'
     ORDER BY start_time
       ↓
SQLite возвращает будущие брони (с сегодняшнего момента)
       ↓
FastAPI превращает в JSON
       ↓
Ответ: 200 [{"id":"...","event_type_id":"...",...}, ...]
```

## 4.7. Что если что-то пошло не так

| Ситуация | Что возвращает | Где ловить |
|----------|---------------|------------|
| Тип события не найден | 404 Not Found | Роутер проверяет `db.get()` |
| Время в прошлом | 400 Bad Request | Роутер сравнивает с `datetime.now()` |
| Слот занят | 409 Conflict | Запрос на пересечение броней |
| duration_minutes = 0 | 422 Validation Error | Pydantic validator |
| Объект невалиден | 422 Validation Error | FastAPI автоматически |
| Внутренняя ошибка | 500 Internal Server Error | FastAPI автоматически |

Формат ошибки:

```json
{
  "detail": "Time slot is already booked"
}
```

FastAPI всегда возвращает ошибки в едином формате. Фронтенд может не гадать — структура одна для всех случаев.

---

# Глава 5. Тесты — КАК НЕ ОБОСРАТЬСЯ В ПРОДАКШЕНЕ

## 5.1. Почему тесты важны

Ты меняешь одну строчку — и сломалась двойная бронь. Без тестов ты узнаешь об этом от пользователя. С тестами — через 0.4 секунды после `pytest`.

В проекте 4 тестовых файла, 13 тестов. Покрывают:
- Создание типов событий
- Валидацию полей
- Генерацию слотов
- Двойную бронь (один тип и разные типы)
- Бронирование несуществующего типа
- Список предстоящих броней

**Золотое правило:** если ты нашёл баг, сначала напиши тест, который его воспроизводит, потом чини код.

## 5.2. Структура тестов

```
tests/
├── conftest.py              ← общие фикстуры (клиент, БД)
├── test_event_types.py      ← 4 теста
├── test_slots.py            ← 3 теста
├── test_bookings.py         ← 4 теста
└── test_admin.py            ← 2 теста
```

Каждый файл тестирует свой роутер. Имена тестов говорят сами за себя:
- `test_list_event_types_empty` — проверить, что пустой список — это `[]`, а не ошибка
- `test_double_booking_conflict` — дважды забронировать одно и то же → 409
- `test_create_event_type_invalid_duration` — duration_minutes = -5 → 422

## 5.3. conftest.py — «Подготовка сцены»

```python
import pytest_asyncio
from httpx import ASGITransport, AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from app.database import Base
from app.dependencies import get_db
from app.main import app

TEST_DATABASE_URL = "sqlite+aiosqlite:///:memory:"


@pytest_asyncio.fixture
async def db_session():
    engine = create_async_engine(TEST_DATABASE_URL, echo=False)
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    factory = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
    async with factory() as session:
        yield session

    await engine.dispose()


@pytest_asyncio.fixture
async def client(db_session: AsyncSession):
    async def _override():
        yield db_session

    app.dependency_overrides[get_db] = _override
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        yield ac

    app.dependency_overrides.clear()
```

**db_session:**
1. Создаёт in-memory SQLite (`:memory:`)
2. Создаёт все таблицы (`Base.metadata.create_all`)
3. Возвращает сессию
4. После теста закрывает соединение

**client:**
1. Подменяет `get_db` на тестовую сессию (`dependency_overrides`)
2. Создаёт `AsyncClient` на ASGI-транспорте (без реального HTTP)
3. После теста убирает подмену

**Что значит ASGI-транспорт?** Обычно HTTP-запрос идёт через сетевой стек: localhost → порт → сервер. ASGI-транспорт вызывает FastAPI напрямую, без сети. Это:
- Быстрее (нет накладных расходов на TCP)
- Не требует запущенного сервера
- Изолированно (каждый тест со своей БД)

## 5.4. Тест-кейсы: что покрываем

**test_event_types.py:**

| Тест | Что проверяет |
|------|---------------|
| `test_list_event_types_empty` | GET без данных → 200 [] |
| `test_create_event_type` | POST с валидными данными → 201 + id |
| `test_create_event_type_invalid_duration` | POST с duration=-5 → 422 |
| `test_list_event_types_after_creation` | Создали 2, получили 2, сортировка по имени |

**test_slots.py:**

| Тест | Что проверяет |
|------|---------------|
| `test_get_slots_nonexistent_event_type` | Несуществующий тип → 404 |
| `test_get_slots_default_range` | Без дат → 200 + массив слотов |
| `test_slots_exclude_booked_times` | Занятый слот не появляется в списке |

**test_bookings.py:**

| Тест | Что проверяет |
|------|---------------|
| `test_create_booking` | Валидная бронь → 201 + end_time |
| `test_create_booking_nonexistent_event_type` | Несуществующий тип → 404 |
| `test_double_booking_conflict` | Та же бронь дважды → 409 |
| `test_double_booking_different_event_types` | Разные типы, одно время → 409 |

**test_admin.py:**

| Тест | Что проверяет |
|------|---------------|
| `test_admin_bookings_empty` | Нет броней → 200 [] |
| `test_admin_bookings_shows_upcoming` | Есть брони → 200 [список] |

## 5.5. Как работает in-memory SQLite

`sqlite+aiosqlite:///:memory:` — специальный URL, который говорит SQLite: «не создавай файл, храни всё в оперативной памяти».

Плюсы:
- **Скорость**: 13 тестов за 0.4 секунды
- **Изоляция**: каждый тест — свежая БД
- **Никакого мусора**: не нужно удалять test.db после тестов

Минусы:
- **Данные не сохраняются** — для production не подходит
- **Нельзя проверить миграции** — таблицы создаются через `create_all`, не через Alembic

Для миграций нужно отдельное тестирование с файловой БД. Но для модульных тестов in-memory — идеал.

## 5.6. Фикстуры pytest-asyncio

Обычный pytest не умеет в асинхронные фикстуры. `pytest-asyncio` добавляет:

- `@pytest_asyncio.fixture` — асинхронная фикстура
- `@pytest.mark.asyncio` — асинхронный тест

```python
@pytest.mark.asyncio
async def test_create_booking(client):
    resp = await client.post("/api/bookings", json={...})
```

Без `pytest-asyncio` ты бы не смог написать `await client.post(...)` в тесте — pytest бы упал с ошибкой "async def outside async context".

**Важно:** все асинхронные фикстуры и тесты должны быть помечены. Если забыть `@pytest.mark.asyncio`, тест выполнится, но `await` не сработает.

---

# Глава 6. FastAPI для начинающих — МАГИЯ БЕЗ МАГИИ

## 6.1. Что такое FastAPI

FastAPI — это веб-фреймворк для создания REST API на Python. Главная фишка: он использует аннотации типов Python для автоматической валидации и генерации документации.

Базовый пример:

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}
```

FastAPI видит:
- `@app.get("/")` — это GET-запрос к корню
- `async def root()` — асинхронная функция
- **Нет типов** → никакой валидации, но всё работает

С типами:

```python
@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}
```

FastAPI видит:
- `item_id: int` — это path-параметр, должен быть числом
- `q: str = None` — это query-параметр, строка, необязательный

Если передать `item_id=abc` — FastAPI вернёт 422 с описанием ошибки.

## 6.2. Роутеры и декораторы

```python
from fastapi import APIRouter

router = APIRouter(prefix="/api/event-types", tags=["Guest: Event Types"])

@router.get("")
async def list_event_types():
    ...

@router.get("/{id}")
async def get_event_type(id: str):
    ...
```

`APIRouter` — группа эндпоинтов. Параметры:
- `prefix` — общий префикс URL для всех эндпоинтов в этом роутере
- `tags` — метка для группировки в Swagger

Декораторы:
- `@router.get("")` — GET-запрос
- `@router.post("")` — POST-запрос
- `@router.put("")` — PUT-запрос
- `@router.delete("")` — DELETE-запрос

Путь может быть пустым (`""`) — тогда URL = prefix. Или с параметром (`"/{id}"`) — URL = prefix + /{id}.

## 6.3. Path и Query параметры

```python
@router.get("/api/event-types/{event_type_id}/slots")
async def get_slots(
    event_type_id: str,                    # path — из URL
    date_from: datetime | None = None,     # query — ?date_from=...
    date_to: datetime | None = None,       # query — ?date_to=...
):
```

Правила:
1. Параметр, имя которого совпадает с `{имя}` в URL → path-параметр
2. Параметр с типом `Body` (из Pydantic) → тело запроса
3. Всё остальное → query-параметр

`datetime | None = None` — опциональный query-параметр. FastAPI распарсит ISO-строку в datetime.

## 6.4. Request Body (Pydantic)

```python
from pydantic import BaseModel

class BookingCreate(BaseModel):
    event_type_id: str
    start_time: datetime

@router.post("/api/bookings")
async def create_booking(body: BookingCreate):
    ...
```

FastAPI видит `body: BookingCreate` и понимает: «это тело запроса, схема — BookingCreate». Автоматически:
1. Читает JSON из тела
2. Проверяет, что все поля есть и правильных типов
3. Создаёт объект `BookingCreate`
4. Если что-то не так — 422 Validation Error

## 6.5. Depends — внедрение зависимостей

```python
from fastapi import Depends

async def get_db():
    async with async_session() as session:
        yield session

@router.get("/api/event-types")
async def list_event_types(db: AsyncSession = Depends(get_db)):
    ...
```

`Depends(get_db)` — FastAPI вызывает `get_db` перед обработчиком. Результат передаётся в параметр `db`. После обработчика — закрывает сессию.

Можно вкладывать зависимости:

```python
async def get_current_user(token: str = Depends(oauth2_scheme)):
    ...

@router.get("/users/me")
async def read_users_me(current_user: User = Depends(get_current_user)):
    ...
```

В нашем проекте простая цепочка: `get_db` → сессия БД.

## 6.6. HTTP статус-коды

| Код | Когда использовать |
|-----|-------------------|
| 200 | Успешный GET-запрос (данные найдены) |
| 201 | Успешный POST (объект создан) |
| 400 | Ошибка в запросе (некорректные данные) |
| 404 | Ресурс не найден |
| 409 | Конфликт (слот уже занят) |
| 422 | Ошибка валидации Pydantic |
| 500 | Внутренняя ошибка сервера |

FastAPI задаёт код по умолчанию:
- GET → 200
- POST → 200

Чтобы изменить:

```python
@router.post("", status_code=status.HTTP_201_CREATED)
```

## 6.7. Обработка ошибок

```python
from fastapi import HTTPException

raise HTTPException(status_code=404, detail="Event type not found")
```

FastAPI перехватывает `HTTPException` и возвращает JSON:

```json
{
  "detail": "Event type not found"
}
```

Детали:
- `status_code` — HTTP-код
- `detail` — сообщение об ошибке (строка или словарь)

---

# Глава 7. SQLAlchemy для выживших — ORM БЕЗ СЛЁЗ

## 7.1. Что такое ORM

ORM (Object-Relational Mapping) — прослойка между Python и SQL. Вместо:

```python
cursor.execute("INSERT INTO event_types (id, name) VALUES (?, ?)", (id, name))
```

Ты пишешь:

```python
db.add(EventType(name="Chat", ...))
await db.commit()
```

SQLAlchemy сам превращает это в `INSERT`. Преимущества:
- **Безопасность**: экранирование значений (нет SQL-инъекций)
- **Абстракция**: код не меняется при смене БД
- **Типизация**: IDE подсказывает поля и типы

## 7.2. Модели — отражение таблиц

Каждая модель — это класс, наследующий от `Base`. Один класс = одна таблица.

```python
class EventType(Base):
    __tablename__ = "event_types"

    id: Mapped[str] = mapped_column(primary_key=True)
    name: Mapped[str]
    duration_minutes: Mapped[int]
```

- `__tablename__` — имя таблицы в БД
- `id: Mapped[str]` — поле id типа str
- `mapped_column(...)` — настройки колонки (первичный ключ, внешний ключ, длина)

## 7.3. Типы колонок и их маппинг

| Python | SQLite | PostgreSQL |
|--------|--------|------------|
| `str` | TEXT | VARCHAR / TEXT |
| `int` | INTEGER | INTEGER |
| `float` | REAL | FLOAT / REAL |
| `bool` | INTEGER (0/1) | BOOLEAN |
| `datetime` | TEXT (ISO-8601) | TIMESTAMP |
| `bytes` | BLOB | BYTEA |

SQLAlchemy автоматически выбирает SQL-тип под БД. Для явного указания:

```python
name: Mapped[str] = mapped_column(String(255))
```

`String(255)` — VARCHAR(255) в PostgreSQL, просто TEXT в SQLite (SQLite игнорирует длину для VARCHAR).

## 7.4. Запросы: select, where, order_by

```python
from sqlalchemy import select

# Все записи
result = await db.execute(select(EventType))
items = result.scalars().all()

# С фильтром
result = await db.execute(
    select(Booking).where(Booking.start_time >= now)
)
bookings = result.scalars().all()

# С сортировкой
result = await db.execute(
    select(Booking).order_by(Booking.start_time)
)

# Поиск по ID
item = await db.get(EventType, "some-id")

# Сложное условие
result = await db.execute(
    select(Booking).where(
        Booking.start_time < end_time,
        Booking.end_time > start_time,
    )
)
```

**scalars()** — достаёт первое значение каждой строки (не кортеж). Если строка — Booking, то `scalars()` вернёт Booking, а не `(Booking,)`.

**first()** — первый результат или None.

**all()** — все результаты.

## 7.5. AsyncSession — асинхронные запросы

Обычный SQLAlchemy — синхронный. Вызов `db.execute(...)` блокирует программу, пока БД не ответит. Для веб-сервера это плохо: пока один запрос ждёт БД, другие висят в очереди.

AsyncSession решает проблему:

```python
# Асинхронный вызов — сервер может обрабатывать другие запросы
result = await db.execute(select(EventType))
```

Пока SQLite читает данные, FastAPI принимает новые запросы.

**Цена**: код сложнее (везде `async/await`). Но для веб-сервера это окупается.

## 7.6. Отношения (relationship)

```python
class EventType(Base):
    bookings: Mapped[list["Booking"]] = relationship(back_populates="event_type")

class Booking(Base):
    event_type: Mapped["EventType"] = relationship(back_populates="bookings")
```

Что это даёт:

```python
# Получить тип события для брони
booking.event_type.name  # "30-min Chat"

# Получить все брони типа события
event_type.bookings  # [Booking, Booking, ...]
```

Без `relationship` пришлось бы писать:

```python
event_type = await db.get(EventType, booking.event_type_id)
bookings = await db.execute(
    select(Booking).where(Booking.event_type_id == event_type.id)
)
```

С `relationship` — просто обращение к свойству.

## 7.7. Миграции через Alembic

Alembic отслеживает изменения схемы БД и позволяет применять/откатывать их.

**Создать новую миграцию:**

```bash
alembic revision -m "add column is_active to event_types"
```

В папке `versions/` появится файл. Открываешь, пишешь изменения:

```python
def upgrade():
    op.add_column("event_types", sa.Column("is_active", sa.Boolean(), default=True))

def downgrade():
    op.drop_column("event_types", "is_active")
```

**Применить:**

```bash
alembic upgrade head
```

**Откатить:**

```bash
alembic downgrade -1
```

**Проверить статус:**

```bash
alembic current
```

---

# Глава 8. Словарик — ЧТО ЭТА ХРЕНЬ ЗНАЧИТ?

| Термин | По-русски | Что это |
|--------|-----------|---------|
| **API** | Интерфейс программы | Как программы общаются друг с другом |
| **REST** | Стиль API | GET — читать, POST — создавать, PUT — менять, DELETE — удалять |
| **Endpoint** | Точка входа | Конкретный URL + метод (`GET /api/event-types`) |
| **OpenAPI** | Спецификация API | JSON-файл, описывающий все эндпоинты |
| **Swagger** | Документация | Страница, где можно тестировать API |
| **ORM** | Прослойка для БД | Превращает SQL в Python-объекты |
| **Model** | Модель | Класс, описывающий таблицу БД |
| **Schema** | Схема | Класс, описывающий формат JSON |
| **Migration** | Миграция | Изменение структуры БД (новая колонка, таблица) |
| **Fixture** | Фикстура | Функция, подготавливающая данные для теста |
| **Dependency** | Зависимость | Функция, которую FastAPI вызывает перед обработчиком |
| **ASGI** | Асинхронный сервер | Как FastAPI общается с Uvicorn |
| **Lifespan** | Жизненный цикл | Код при запуске и остановке сервера |
| **CORS** | Политика безопасности | Разрешение запросов с других доменов |
| **UTC** | Всемирное время | Единый часовой пояс для всего мира |
| **Naive datetime** | «Наивное» время | datetime без часового пояса |
| **Aware datetime** | «Осознанное» время | datetime с часовым поясом |
| **UUID** | Уникальный ID | Строка вида `a1b2c3d4-e5f6-...` |
| **Foreign Key** | Внешний ключ | Ссылка на ID другой таблицы |
| **Relationship** | Отношение | Связь между таблицами |
| **Validation** | Валидация | Проверка данных на корректность |
| **409 Conflict** | Конфликт | HTTP-код: запрос конфликтует с существующими данными |
| **In-memory DB** | БД в памяти | SQLite, которая живёт только в RAM |

---

# Глава 9. Часто задаваемые вопросы — А ЧТО, ЕСЛИ...

## 9.1. База данных не создаётся

Симптом: при старте сервера ошибка "no such table: event_types".

Причина: `lifespan` не выполнился, таблицы не создались.

Решение: удали `app.db` и перезапусти сервер. FastAPI заново создаст таблицы через `create_all`.

Если не помогло — проверь права на запись в папку `backend/`. SQLite должен создать файл `app.db`.

## 9.2. SQLite выдаёт "database is locked"

Симптом: ошибка при нескольких одновременных запросах.

Причина: SQLite блокирует файл при записи. Если два запроса пишут одновременно — второй ждёт или падает.

Решение для разработки: это редкая ситуация (один админ, мало запросов). Если возникает — увеличь таймаут:

```python
engine = create_async_engine(
    settings.database_url,
    connect_args={"timeout": 30},  # ждать 30 секунд
)
```

Для продакшена: перейти на PostgreSQL.

## 9.3. Двойная бронь не блокируется

Симптом: два запроса на одно и то же время создают две брони.

Причина: гонка состояний (race condition). Оба запроса проверили пересечение одновременно, оба решили «свободно», оба создали бронь.

Решение: для SQLite это маловероятно (он блокирует файл при записи). Для PostgreSQL — использовать `SELECT ... FOR UPDATE` (блокировка строки).

В текущей реализации риск есть, но для учебного проекта — допустимо.

## 9.4. Хочу перейти на PostgreSQL

1. Установи PostgreSQL и создай БД
2. Добавь в `requirements.txt`: `asyncpg`
3. Поменяй `.env`:
   ```
   DATABASE_URL=postgresql+asyncpg://user:password@localhost:5432/calendar
   ```
4. Примени миграции: `alembic upgrade head`
5. Перезапусти сервер

SQLAlchemy скроет разницу. Менять придётся только URL и драйвер. Модели, запросы, роутеры — без изменений.

## 9.5. Порт 8000 уже занят

Симптом: при запуске ошибка "Address already in use".

Решение:
```bash
# Узнать, кто занял порт
netstat -ano | findstr :8000

# Завершить процесс (Windows)
taskkill /PID <номер> /F

# Или запустить на другом порту
fastapi dev app/main.py --port 8001
```

## 9.6. Фронтенд не видит бэкенд

Симптом: фронтенд на `localhost:5173`, запросы к `/api` возвращают ошибки.

Причина: Vite прокси перенаправляет `/api` на `localhost:4010` (Prism), а не на `localhost:8000`.

Решение: поменять `vite.config.ts`:
```ts
proxy: {
  '/api': {
    target: 'http://localhost:8000',  // было 4010
    changeOrigin: true,
  },
},
```

Или запустить бэкенд на порту 4010:
```bash
fastapi dev app/main.py --port 4010
```

## 9.7. Тесты падают с timezone-ошибками

Симптом: "TypeError: can't compare offset-naive and offset-aware datetimes".

Причина: одно значение datetime с часовым поясом, другое — без. SQLite через aiosqlite не сохраняет timezone.

Решение: все времена приводятся к naive (без tzinfo) на входе в систему. Если ошибка возникла — проверь, что в новом коде используется `_naive()` или `.replace(tzinfo=None)`.

---

*Если ты дочитал до конца — ты официально выжил. Поздравляю. Теперь иди настрой Vite proxy на 8000 и соединяй фронт с бэком.*
