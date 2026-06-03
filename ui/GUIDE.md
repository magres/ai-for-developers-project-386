# Руководство программиста

## Calendar Booking UI — Фронтенд для самых маленьких

*Чтобы понять этот текст, достаточно уметь включать компьютер и читать по слогам.*

---

# Оглавление

1. [Введение — ЧТО ВООБЩЕ ПРОИСХОДИТ?](#глава-1-введение--что-вообще-происходит)
   - 1.1. Аналогия с рестораном
   - 1.2. Анатомия URL
   - 1.3. Что такое порт
   - 1.4. Что такое localhost
   - 1.5. HTTP-методы: GET, POST, DELETE
   - 1.6. Полная схема работы приложения
   - 1.7. Почему Vite? Почему не просто открыть HTML?

2. [Экскурсия по файлам — А ЧТО ТУТ У НАС?](#глава-2-экскурсия-по-файлам--а-что-тут-у-нас)
   - 2.1. Дерево файлов
   - 2.2. package.json — список покупок
   - 2.3. index.html — дверь в приложение
   - 2.4. vite.config.ts — настройки рации
   - 2.5. tsconfig.json — правила русского языка
   - 2.6. postcss.config.js — рецепт для Mantine-соусов
   - 2.7. openapi.json — поддельный бэкенд
   - 2.8. .gitignore — что не пихать в git
   - 2.9. src/main.tsx — швейцар в клубе
   - 2.10. src/App.tsx — пульт маршрутов
   - 2.11. src/types.ts — фотороботы данных
   - 2.12. src/api.ts — телефонистка
   - 2.13. src/components/Layout.tsx — шапка и рамка
   - 2.14. src/components/EventTypeCard.tsx — визитка
   - 2.15. src/components/SlotPicker.tsx — календарь + бронь
   - 2.16. src/pages/EventTypesPage.tsx — страница гостя
   - 2.17. src/pages/BookingPage.tsx — страница брони
   - 2.18. src/pages/AdminPage.tsx — админ-панель

3. [Жизненный цикл брони — ДАННЫЕ ПУТЕШЕСТВУЮТ](#глава-3-жизненный-цикл-брони--данные-путешествуют)
   - 3.1. Полный путь запроса
   - 3.2. Шаг 1: Загрузка типов событий
   - 3.3. Шаг 2: Выбор типа и переход к слотам
   - 3.4. Шаг 3: Показ календаря
   - 3.5. Шаг 4: Выбор времени
   - 3.6. Шаг 5: Подтверждение брони
   - 3.7. Что если бэкенд упал?

4. [React для новичка — МАГИЯ БЕЗ МАГИИ](#глава-4-react-для-новичка--магия-без-магии)
   - 4.1. Что такое React
   - 4.2. JSX — HTML внутри JavaScript
   - 4.3. Компонент — функция, которая возвращает HTML
   - 4.4. Props — аргументы функции
   - 4.5. State — память компонента
   - 4.6. Как React понимает, что пора перерисоваться
   - 4.7. useEffect — сделай это, когда проснёшься
   - 4.8. Условный рендеринг
   - 4.9. Списки и ключи (key)
   - 4.10. Обработка событий (onClick, onSubmit)
   - 4.11. Подъём состояния (lifting state up)
   - 4.12. React Router — навигация без перезагрузки

5. [Mantine — СТРОИТЕЛЬНЫЙ НАБОР ЛЕГО](#глава-5-mantine--строительный-набор-лего)
   - 5.1. Что такое Mantine
   - 5.2. Установка и подключение
   - 5.3. Каталог компонентов нашего проекта
   - 5.4. AppShell — каркас страницы
   - 5.5. Тёмная тема и кастомизация

6. [TypeScript — JAVASCRIPT С НАМОРДНИКОМ](#глава-6-typescript--javascript-с-намордником)
   - 6.1. Что такое TypeScript
   - 6.2. Типы — Interface и Type
   - 6.3. Зачем нужны типы в этом проекте
   - 6.4. Откуда берутся типы для API
   - 6.5. Что будет, если типы не совпадут

7. [Как это всё запускается — ПОД КАПОТОМ](#глава-7-как-это-всё-запускается--под-капотом)
   - 7.1. Что происходит при npm install
   - 7.2. Что происходит при npm run dev
   - 7.3. Что происходит при npm run dev:mock
   - 7.4. Что происходит при npm run build
   - 7.5. Папка dist/ — что внутри

8. [Как вносить изменения — А ТЕПЕРЬ СЛОМАЙ ЭТО](#глава-8-как-вносить-изменения--а-теперь-сломай-это)
   - 8.1. Хочу добавить новую страницу
   - 8.2. Хочу изменить цвет кнопки
   - 8.3. Хочу добавить новый API-вызов
   - 8.4. Хочу изменить название сайта
   - 8.5. Хочу убрать Prism и подключить реальный бэкенд
   - 8.6. Хочу другую библиотеку компонентов
   - 8.7. Хочу изменить календарь (не 14 дней)
   - 8.8. Хочу добавить новое поле в форму

9. [Словарик — ЧТО ЭТА ХРЕНЬ ЗНАЧИТ?](#глава-9-словарик--что-эта-хрень-значит)

10. [Часто задаваемые вопросы — А ЧТО, ЕСЛИ...](#глава-10-часто-задаваемые-вопросы--а-что-если)
    - 10.1. Prism не сохраняет данные
    - 10.2. Календарь показывает только 14 дней
    - 10.3. Приложение не работает без Prism
    - 10.4. Синие точки на календаре
    - 10.5. UI выглядит не так
    - 10.6. Ошибка в консоли браузера
    - 10.7. Не могу найти, где менять текст

11. [Git для самых маленьких — КАК НЕ УБИТЬ ВСЁ](#глава-7-git-для-самых-маленьких--как-не-убить-всё)
    - 11.1. git status — что изменилось
    - 11.2. git diff — покажи подробности
    - 11.3. git add — подготовить
    - 11.4. git commit — сохранить
    - 11.5. git checkout — откатить
    - 11.6. Что делать, если всё сломалось

---

# Глава 1. Введение — ЧТО ВООБЩЕ ПРОИСХОДИТ?

## 1.1. Аналогия с рестораном

Представь, что наш сайт — это ресторан.

| Кто в ресторане | В реальности | В нашем проекте |
|----------------|--------------|-----------------|
| **Посетитель** | Ты с открытым ртом | **Браузер** (Chrome, Firefox, Edge) |
| **Официант** | Принимает заказ, носит еду | **Vite** — раздаёт HTML/JS/CSS браузеру |
| **Повар** | Готовит блюда | **Бэкенд** — программа на порту 3000 или **Prism**-заглушка |
| **Менеджер зала** | Следит, чтобы всё работало | **React** — рисует кнопки, обновляет страницу без перезагрузки |
| **Набор красивых тарелок** | Сервировка | **Mantine** — готовые компоненты: кнопки, карточки, календарь |
| **Меню** | Список блюд | **openapi.json** — описание того, что умеет бэкенд |
| **Кухонный комбайн** | Месит тесто | **Vite** — превращает TSX в обычный JS |

Посетитель (браузер) приходит в ресторан (наш сайт). Официант (Vite) приносит меню (HTML/JS/CSS). Посетитель выбирает блюдо из меню (кликает на кнопку). Официант несёт заказ на кухню (вызов API). Повар (бэкенд) готовит блюдо и отдаёт официанту. Менеджер (React) накрывает на стол — обновляет страницу.

## 1.2. Анатомия URL

Когда ты вводишь `http://localhost:5173/admin`, браузер разбирает это так:

```
http://localhost:5173/admin
│      │         │     │
│      │         │     └── путь (path) — какая страница
│      │         └──────── порт (port) — какой вход в программу
│      └────────────────── хост (host) — имя компьютера
└───────────────────────── протокол (scheme) — как общаться
```

**Протокол**: `http` или `https`. HTTP — обычный, HTTPS — с шифрованием. Для разработки на своём компьютере достаточно HTTP.

**Хост**: `localhost` — это «мой собственный компьютер». В интернете было бы `google.com` или `example.com`.

**Порт**: `5173` — номер входа. Представь многоквартирный дом: хост — это адрес дома, порт — номер квартиры. У каждой программы свой порт:
- Vite (фронтенд) — порт 5173
- Prism (мок-бэкенд) — порт 4010
- Настоящий бэкенд — порт 3000

**Путь**: `/admin` — что именно мы хотим. Корень — `/`, страница админа — `/admin`, страница конкретного типа события — `/book/et-1`.

## 1.3. Что такое порт

Порт — это номер двери в программу. У каждой программы, которая работает с сетью, есть свой номер.

```
Твой компьютер
┌─────────────────────────────────┐
│  Порт 80     — веб-сервер       │
│  Порт 443    — HTTPS            │
│  Порт 3000   — бэкенд (API)     │
│  Порт 4010   — Prism (заглушка) │
│  Порт 5173   — Vite (фронтенд)  │
│  Порт 3306   — база данных      │
│  Порт 22     — SSH              │
└─────────────────────────────────┘
```

Если две программы попробуют занять один порт — вторая не запустится. Поэтому у каждой свой номер.

## 1.4. Что такое localhost

`localhost` — это зарезервированное имя для «этого компьютера». Когда ты запускаешь Vite на своём ноутбуке, он открывает порт 5173 на `localhost`. Это значит: «слушай запросы только с этого компьютера».

Если бы Vite слушал на `0.0.0.0`, к нему могли бы обращаться другие компьютеры в сети. Для разработки это не нужно, поэтому мы используем `localhost`.

Альтернатива: вместо `localhost` можно использовать `127.0.0.1` — это IP-адрес этого компьютера. Разницы нет.

## 1.5. HTTP-методы: GET, POST, DELETE

Когда браузер говорит с сервером, он использует один из методов:

| Метод | Что делает | Пример из проекта |
|-------|-----------|-------------------|
| **GET** | Получить данные (прочитать) | `GET /api/event-types` — получить список типов |
| **POST** | Создать новые данные | `POST /api/bookings` — создать бронь |
| **PUT** | Обновить данные целиком | (не используется) |
| **PATCH** | Обновить часть данных | (не используется) |
| **DELETE** | Удалить данные | (не используется) |

**GET** — это как посмотреть меню. Можно делать сколько угодно раз, ничего не меняется.
**POST** — это как сделать заказ. После него что-то меняется на сервере.

В проекте используются только GET и POST.

## 1.6. Полная схема работы приложения

Вот что происходит от момента, когда ты нажимаешь Enter в браузере, до появления картинки:

```
ШАГ 1: Ты вводишь http://localhost:5173
         │
         ▼
ШАГ 2: Браузер стучится на порт 5173
         │
         ▼
ШАГ 3: Vite получает запрос
         │
         ├── Если запрос / или /index.html
         │     └→ Отдаёт index.html
         │
         ├── Если запрос /src/что-то.tsx
         │     └→ Vite превращает TSX → JS на лету, отдаёт JS
         │
         └── Если запрос /api/что-то
               └→ Vite перенаправляет (proxy) на localhost:4010 (Prism)
         │
         ▼
ШАГ 4: Браузер получает index.html
         │
         ▼
ШАГ 5: Браузер видит <script src="/src/main.tsx">
         │
         ▼
ШАГ 6: Браузер просит Vite отдать /src/main.tsx
         │
         ▼
ШАГ 7: Vite превращает main.tsx → обычный JavaScript, отдаёт
         │
         ▼
ШАГ 8: Браузер выполняет JavaScript:
         ├── React запускается
         ├── React Router смотрит URL: path = "/"
         ├── React понимает: надо показать EventTypesPage
         └── React рисует EventTypesPage
         │
         ▼
ШАГ 9: EventTypesPage:
         ├── Вызывает fetch('/api/event-types')
         ├── Vite перенаправляет на Prism (порт 4010)
         ├── Prism отвечает: [{"id":"et-1","name":"30-min Chat",...}, ...]
         └── React получает данные, рисует карточки
```

**Ключевой момент**: Vite работает как умный прокси. Когда браузер запрашивает `/api/...`, он думает, что идёт на `localhost:5173` (сам Vite). Но Vite втихаря перенаправляет запрос на `localhost:4010` (Prism). Браузер ничего не подозревает, CORS не ругается, все счастливы.

## 1.7. Почему Vite? Почему не просто открыть HTML?

Можно же просто написать HTML-файл и открыть его в браузере, зачем все эти сложности?

Проблемы с простым HTML:

1. **TypeScript не работает в браузере**. Браузер понимает только JavaScript. TypeScript нужен на этапе разработки, а для браузера его надо превратить в JS. Vite делает это автоматически.

2. **JSX не работает в браузере**. `<div>привет</div>` внутри JS-файла — это не HTML, это JSX. Браузер его не поймёт. Vite превращает JSX в обычные вызовы JavaScript.

3. **Модули**. Современный React использует `import/export`. Старые браузеры это не поддерживают. Vite собирает всё в один файл.

4. **Горячая перезагрузка (HMR)**. Когда ты меняешь код, Vite автоматически обновляет страницу без перезагрузки. Ты меняешь цвет кнопки — через секунду видишь новый цвет. Простой HTML пришлось бы перезагружать вручную.

5. **Proxy**. Vite может перенаправлять запросы API на другой сервер. Простой HTML не умеет этого без дополнительных настроек.

6. **Сборка (build)**. Когда проект готов, Vite сжимает файлы, убирает лишнее, добавляет хэши к именам для кеширования. Вручную это делать никто не хочет.

---

# Глава 2. Экскурсия по файлам — А ЧТО ТУТ У НАС?

## 2.1. Дерево файлов

```
ui/                                          ← корень фронтенда
│
├── package.json                             ← список зависимостей (npm)
├── package-lock.json                        ← зафиксированные версии (не трогать!)
├── index.html                               ← точка входа для браузера
├── vite.config.ts                           ← настройки Vite
├── tsconfig.json                            ← главный конфиг TypeScript
├── tsconfig.app.json                        ← настройки TS для src/
├── tsconfig.node.json                       ← настройки TS для vite.config.ts
├── postcss.config.js                        ← настройки обработки CSS
├── openapi.json                             ← спецификация API для Prism
├── .gitignore                               ← какие файлы git должен игнорировать
├── README.md                                ← short readme
├── GUIDE.md                                 ← то, что ты сейчас читаешь
├── node_modules/                            ← папка со скачанными пакетами (НЕ ТРОГАТЬ!)
│
├── dist/                                    ← собранная версия (появляется после build)
│
└── src/                                     ← исходный код
    ├── main.tsx                             ← входная точка React
    ├── App.tsx                              ← корневой компонент (роутер)
    ├── types.ts                             ← TypeScript-типы
    ├── api.ts                               ← функции для вызова API
    ├── vite-env.d.ts                        ← типы для Vite (не трогать)
    │
    ├── components/                          ← переиспользуемые компоненты
    │   ├── Layout.tsx                       ← шапка и рамка для всех страниц
    │   ├── EventTypeCard.tsx                ← карточка одного типа события
    │   └── SlotPicker.tsx                   ← календарь + список слотов + модалка
    │
    └── pages/                               ← страницы (по одной на маршрут)
        ├── EventTypesPage.tsx               ← список типов событий (гость)
        ├── BookingPage.tsx                  ← выбор слота (гость)
        └── AdminPage.tsx                    ← админ-панель
```

## 2.2. package.json — «Список покупок на AliExpress»

Этот файл — сердце проекта. В нём написано:
- Какие пакеты (библиотеки) нужны
- Какие команды можно запускать
- Как проект называется

### dependencies — «То, без чего приложение не заведётся»

```json
"dependencies": {
  "react": "^18.3.1",
  "react-dom": "^18.3.1",
  "react-router-dom": "^6.26.0",
  "@mantine/core": "^7.12.0",
  "@mantine/dates": "^7.12.0",
  "@mantine/form": "^7.12.0",
  "@mantine/notifications": "^7.12.0",
  "dayjs": "^1.11.12",
  "@tabler/icons-react": "^3.11.0"
}
```

| Пакет | Зачем | Альтернативы |
|-------|-------|-------------|
| `react` | Сама библиотека React | Vue, Angular, Svelte |
| `react-dom` | React для браузера (рисует в DOM) | — |
| `react-router-dom` | Навигация между страницами без перезагрузки | — |
| `@mantine/core` | Основные компоненты Mantine | Ant Design, Material UI, Chakra UI |
| `@mantine/dates` | Календарь, DatePicker от Mantine | react-day-picker, react-datepicker |
| `@mantine/form` | Работа с формами (валидация, отправка) | react-hook-form, Formik |
| `@mantine/notifications` | Всплывающие уведомления (тосты) | react-toastify |
| `dayjs` | Работа с датами (форматирование, сравнение) | date-fns, moment.js |
| `@tabler/icons-react` | Иконки | react-icons, heroicons |

### devDependencies — «Инструменты для разработки, в продакшене не нужны»

```json
"devDependencies": {
  "@vitejs/plugin-react": "^4.3.1",
  "@stoplight/prism-cli": "^5.4.0",
  "concurrently": "^8.2.2",
  "postcss": "^8.4.41",
  "postcss-preset-mantine": "^1.17.0",
  "typescript": "^5.5.4",
  "vite": "^5.4.0"
}
```

| Пакет | Зачем |
|-------|-------|
| `vite` | Сборщик — превращает TSX → JS, запускает dev-сервер, собирает build |
| `@vitejs/plugin-react` | Плагин, который учит Vite понимать React-овский JSX |
| `@stoplight/prism-cli` | Prism — заглушка бэкенда для разработки |
| `concurrently` | Умеет запускать две программы в одном окне терминала |
| `postcss` | Обработчик CSS (Mantine использует PostCSS для своих стилей) |
| `postcss-preset-mantine` | Набор PostCSS-правил для Mantine |
| `typescript` | Компилятор TypeScript — проверяет типы |

### scripts — «Кнопки на пульте управления»

```json
"scripts": {
  "dev": "vite",
  "dev:mock": "concurrently \"vite\" \"prism mock openapi.json\"",
  "build": "tsc -b && vite build",
  "preview": "vite preview"
}
```

| Команда | Что делает | Когда использовать |
|---------|-----------|-------------------|
| `npm run dev` | Запускает только Vite (фронтенд). Prism нужно запустить отдельно. | Если Prism уже работает или подключён реальный бэкенд. |
| `npm run dev:mock` | Запускает Vite + Prism одновременно в одном окне. | **Каждый день для разработки.** |
| `npm run build` | Сначала проверяет типы (tsc -b), потом собирает проект в dist/. | Перед загрузкой на сервер. |
| `npm run preview` | Показывает, как выглядит собранный dist/ в браузере. | Чтобы проверить build перед деплоем. |

**Символ `^` в версиях**: `"react": "^18.3.1"` означает «версия 18.3.1 или любая 18.x новее». `^` разрешает минорные обновления, но не мажорные (19.0.0 уже не подойдёт).

### package-lock.json

Этот файл создаётся автоматически при `npm install`. В нём записаны точные версии всех пакетов и их зависимостей. **Не трогай его руками.** Если удалишь — npm пересоздаст, но может подтянуть новые версии.

## 2.3. index.html — «Дверь, через которую React заходит в дом»

```html
<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Calendar Booking</title>
  </head>
  <body>
    <div id="root"></div>
    <script type="module" src="/src/main.tsx"></script>
  </body>
</html>
```

Это минимальный HTML-файл. Он делает ровно две вещи:

1. **Создаёт пустой контейнер**: `<div id="root"></div>`. React возьмёт этот div и построит внутри него всё приложение. Без этого div React некуда будет вставиться.

2. **Подключает main.tsx**: `<script type="module" src="/src/main.tsx"></script>`. Браузер увидит эту строчку и скажет Vite: «дай мне этот файл». Vite превратит main.tsx в обычный JS и отдаст браузеру.

Всё остальное (стили, скрипты, контент) подключается через main.tsx — в HTML больше ничего дописывать не нужно.

**Почему `<div id="root">`?** Это просто соглашение. Можно назвать `app`, `container` или `main` — главное, чтобы в main.tsx было написано то же самое.

## 2.4. vite.config.ts — «Настройки рации»

```ts
import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

export default defineConfig({
  plugins: [react()],
  server: {
    port: 5173,
    proxy: {
      '/api': {
        target: 'http://localhost:4010',
        changeOrigin: true,
      },
    },
  },
});
```

Разберём построчно:

| Строка | Что значит |
|--------|-----------|
| `import { defineConfig } from 'vite'` | Берём функцию `defineConfig` из пакета Vite |
| `plugins: [react()]` | Подключаем React-плагин. Без него Vite не поймёт JSX. |
| `server.port: 5173` | Vite будет слушать порт 5173 |
| `proxy: { '/api': { target: 'http://localhost:4010' } }` | Все запросы, начинающиеся на `/api`, перенаправлять на порт 4010 (Prism) |
| `changeOrigin: true` | Менять заголовок Host на целевой. Нужно, чтобы Prism не ругался. |

**Как работает proxy (очень важно понять):**

```
Браузер думает:                         А на самом деле:
                                         
fetch('/api/event-types')                fetch('/api/event-types')
         │                                        │
         ▼                                        ▼
Идёт на localhost:5173 ...         Vite перехватывает и отправляет
(сам Vite)                         на localhost:4010 (Prism)
         │                                        │
         ▼                                        ▼
Vite отвечает: «ща,                   Prism отвечает: «держи
схожу на ту сторону»                  данные»

```

Браузер НИЧЕГО не знает про localhost:4010. Он думает, что общается с Vite. Это гениально, потому что:
- Не нужно настраивать CORS на бэкенде
- Не нужно менять URL в коде при переключении между Prism и реальным бэкендом
- В продакшене proxy не нужен — фронтенд и бэкенд обычно на одном домене

## 2.5. tsconfig.json — «Правила русского языка (TypeScript)»

На самом деле файлов три: `tsconfig.json`, `tsconfig.app.json`, `tsconfig.node.json`. Они работают в связке.

### tsconfig.json (главный)

```json
{
  "files": [],
  "references": [
    { "path": "./tsconfig.app.json" },
    { "path": "./tsconfig.node.json" }
  ]
}
```

Он ничего не делает сам — просто указывает на два других конфига.

### tsconfig.app.json (для src/)

```json
{
  "compilerOptions": {
    "target": "ES2020",
    "lib": ["ES2020", "DOM", "DOM.Iterable"],
    "module": "ESNext",
    "moduleResolution": "bundler",
    "jsx": "react-jsx",
    "strict": true,
    "noUnusedLocals": true,
    "noUnusedParameters": true,
    "noFallthroughCasesInSwitch": true
  },
  "include": ["src"]
}
```

Ключевые настройки:

| Настройка | Что значит |
|-----------|-----------|
| `target: ES2020` | Какой стандарт JavaScript использовать. 2020 — современный, все браузеры понимают. |
| `lib: ["DOM"]` | Разрешаем использовать document, window, fetch и другие браузерные штуки. |
| `jsx: react-jsx` | Как Vite будет превращать JSX в JS. |
| `strict: true` | Включаем все проверки типов. Больше ошибок — меньше багов. |
| `noUnusedLocals: true` | Если объявил переменную, но не используешь — ошибка. (Держит код чистым.) |
| `noUnusedParameters: true` | Если функция принимает параметр, но не использует — ошибка. |

### tsconfig.node.json (для vite.config.ts)

Почти то же самое, но для Node.js-окружения (vite.config.ts работает в Node, а не в браузере).

## 2.6. postcss.config.js — «Рецепт для Mantine-соусов»

```js
export default {
  plugins: {
    'postcss-preset-mantine': {},
  },
};
```

Mantine использует PostCSS для обработки стилей. `postcss-preset-mantine` — это набор правил, которые применяются к CSS-файлам Mantine.

**Что это даёт**: Mantine можно кастомизировать (менять цвета, размеры, отступы). PostCSS-пресет подготавливает CSS для этого. Если убрать этот файл, Mantine-компоненты всё равно будут работать, но кастомизация сломается.

## 2.7. openapi.json — «Поддельный бэкенд (симулятор)»

Этот файл — **самый важный для разработки без бэкенда**. Prism читает его и притворяется настоящим сервером.

### Формат и структура

OpenAPI — это стандарт описания REST API. Файл состоит из нескольких разделов:

```
openapi.json
├── info              ← название и версия API
├── servers           ← где работает API (список URL)
├── paths             ← сами эндпоинты
│   ├── /api/event-types
│   │   └── get       ← GET запрос
│   ├── /api/event-types/{eventTypeId}/slots
│   │   └── get       ← GET с параметрами
│   ├── /api/bookings
│   │   └── post      ← POST запрос
│   ├── /api/admin/event-types
│   │   └── post      ← POST
│   └── /api/admin/bookings
│       └── get       ← GET
└── components
    └── schemas       ← типы данных (EventType, Booking, TimeSlot...)
```

### 5 эндпоинтов, которые мы описали

| Метод | Путь | Что делает | request body | response |
|-------|------|-----------|-------------|----------|
| GET | `/api/event-types` | Список всех типов событий | — | Массив EventType[] |
| GET | `/api/event-types/{id}/slots` | Свободные слоты для типа | — | Массив TimeSlot[] |
| POST | `/api/bookings` | Создать бронь | BookingCreate | Booking |
| POST | `/api/admin/event-types` | Создать тип события (админ) | EventTypeCreate | EventType |
| GET | `/api/admin/bookings` | Все будущие брони (админ) | — | Массив Booking[] |

### Примеры данных (examples)

Для эндпоинта `/api/event-types` мы добавили `example`:

```json
"example": [
  { "id": "et-1", "name": "30-min Chat", "description": "Quick call to discuss anything", "durationMinutes": 30 },
  { "id": "et-2", "name": "1-on-1 Meeting", "description": "Weekly sync-up", "durationMinutes": 60 },
  { "id": "et-3", "name": "Coffee Chat", "description": "Casual meetup over coffee", "durationMinutes": 15 }
]
```

Без example Prism генерировал бы случайные названия вроде `"id": "adf789gh"`, `"name": "Producto de prueba"`. С example ты видишь осмысленные данные.

Для эндпоинта слотов пример использует конкретные даты:

```json
"example": [
  { "startTime": "2026-05-31T09:00:00Z", "endTime": "2026-05-31T09:30:00Z" },
  ...
]
```

**Почему даты именно такие?** Потому что Prism генерирует случайные даты (1970 год, 2099 год). Они не попадают в окно «сегодня + 14 дней» на календаре, и дни становятся некликабельными. С примером даты реальные — календарь работает.

### Схемы (schemas)

Внизу файла описаны схемы — типы данных:

```json
"EventType": {
  "type": "object",
  "required": ["id", "name", "description", "durationMinutes"],
  "properties": {
    "id":    { "type": "string" },
    "name":  { "type": "string" },
    "description": { "type": "string" },
    "durationMinutes": { "type": "integer" }
  }
}
```

Если бэкенд изменит формат, нужно:
1. Поменять схему в openapi.json
2. Поменять тип в src/types.ts
3. Поменять обработку в компонентах

## 2.8. .gitignore — «Что не пихать в git»

```
node_modules
dist
*.local
```

- `node_modules` — папка с пакетами. Она весит 200+ МБ, каждый раз npm install создаёт её заново. В git её класть бессмысленно.
- `dist` — собранная версия. Она создаётся командой `npm run build`. В git не нужна.
- `*.local` — локальные конфиги. Никто не хочет случайно закоммитить пароль от базы данных.

## 2.9. src/main.tsx — «Швейцар в клубе»

```tsx
import React from 'react';
import ReactDOM from 'react-dom/client';
import { BrowserRouter } from 'react-router-dom';
import { MantineProvider } from '@mantine/core';
import { Notifications } from '@mantine/notifications';
import App from './App';

import '@mantine/core/styles.css';
import '@mantine/dates/styles.css';
import '@mantine/notifications/styles.css';

ReactDOM.createRoot(document.getElementById('root')!).render(
  <React.StrictMode>
    <BrowserRouter>
      <MantineProvider defaultColorScheme="light">
        <Notifications />
        <App />
      </MantineProvider>
    </BrowserRouter>
  </React.StrictMode>,
);
```

Этот файл — первое, что выполняется после загрузки страницы. Построчный разбор:

**Строка 1: Импорт React**
```tsx
import React from 'react';
```
Нужен, чтобы работал JSX. Без React `<div>` превратится в ошибку.

**Строка 2: ReactDOM**
```tsx
import ReactDOM from 'react-dom/client';
```
ReactDOM — мост между React и браузером. React умеет рисовать интерфейс, а ReactDOM умеет вставлять его в HTML.

**Строки 3-6: Импорт библиотек**
```tsx
import { BrowserRouter } from 'react-router-dom';
import { MantineProvider } from '@mantine/core';
import { Notifications } from '@mantine/notifications';
import App from './App';
```
Подключаем всё, что нужно для работы.

**Строки 8-10: Импорт стилей**
```tsx
import '@mantine/core/styles.css';
import '@mantine/dates/styles.css';
import '@mantine/notifications/styles.css';
```
Импортируем CSS для Mantine. Без них компоненты будут выглядеть как HTML из 1998 года.

**Строка 12: createRoot**
```tsx
ReactDOM.createRoot(document.getElementById('root')!).render(...)
```
Находим `<div id="root">` в index.html и говорим React: «рисуй здесь».

Восклицательный знак `!` — это оператор `non-null assertion`. Он говорит TypeScript: «я уверен, что этот div существует, не проверяй». Если бы div не существовал, приложение бы упало с ошибкой — но мы знаем, что он есть.

**Строка 13: StrictMode**
```tsx
<React.StrictMode>
```
Режим строгой проверки. В разработке React будет дважды вызывать некоторые функции, чтобы найти потенциальные проблемы. В продакшене не влияет.

**Строка 14: BrowserRouter**
```tsx
<BrowserRouter>
```
Включает маршрутизацию. React Router будет слушать изменения URL и показывать нужные компоненты.

**Строка 15: MantineProvider**
```tsx
<MantineProvider defaultColorScheme="light">
```
Оборачивает приложение в Mantine. Все дочерние компоненты получат доступ к Mantine-теме (цвета, размеры, шрифты). `defaultColorScheme="light"` — светлая тема по умолчанию.

**Строка 16: Notifications**
```tsx
<Notifications />
```
Добавляет контейнер для всплывающих уведомлений. Сам по себе ничего не показывает, но когда код вызывает `notifications.show(...)`, уведомление появляется в этом контейнере.

**Строка 17: App**
```tsx
<App />
```
Запускает корневой компонент. Всё приложение живёт внутри.

**Итоговая вложенность:**
```
React.StrictMode
  └── BrowserRouter
       └── MantineProvider
            ├── Notifications (контейнер для уведомлений)
            └── App (корневой компонент)
                 └── ...
```

## 2.10. src/App.tsx — «Пульт маршрутов»

```tsx
import { Routes, Route, Navigate } from 'react-router-dom';
import Layout from './components/Layout';
import EventTypesPage from './pages/EventTypesPage';
import BookingPage from './pages/BookingPage';
import AdminPage from './pages/AdminPage';

export default function App() {
  return (
    <Routes>
      <Route element={<Layout />}>
        <Route path="/" element={<EventTypesPage />} />
        <Route path="/book/:eventTypeId" element={<BookingPage />} />
        <Route path="/admin" element={<AdminPage />} />
        <Route path="*" element={<Navigate to="/" replace />} />
      </Route>
    </Routes>
  );
}
```

**Что делает Routes?** Смотрит на текущий URL и выбирает первый подходящий Route.

**Что такое `:eventTypeId` в пути?** Это динамический параметр. В URL может быть `/book/et-1` или `/book/abc123` — React Router запишет значение в переменную `eventTypeId`, и его можно получить через `useParams()`.

**Route с element={<Layout />}** — это родительский маршрут. Он не имеет `path` (или path="/" — пустой), значит, совпадает со всеми URL. Layout покажет шапку, а внутри — текущую дочернюю страницу через `<Outlet />`.

**Route path="\*"** — если URL не подходит ни под один маршрут, перенаправляем на `/`. Это обработчик 404.

**Таблица маршрутов:**

| URL | Layout | Страница внутри |
|-----|--------|----------------|
| `/` | Шапка сверху | EventTypesPage |
| `/book/et-1` | Шапка сверху | BookingPage |
| `/admin` | Шапка сверху | AdminPage |
| `/что-то-левое` | Шапка сверху | Перенаправление на `/` |

## 2.11. src/types.ts — «Фотороботы данных»

```ts
export interface EventType {
  id: string;
  name: string;
  description: string;
  durationMinutes: number;
}

export interface Booking {
  id: string;
  eventTypeId: string;
  startTime: string;    // ISO 8601: "2026-05-30T12:00:00Z"
  endTime: string;      // ISO 8601: "2026-05-30T12:30:00Z"
}

export interface TimeSlot {
  startTime: string;
  endTime: string;
}

export interface EventTypeCreate {
  name: string;
  description: string;
  durationMinutes: number;
}

export interface BookingCreate {
  eventTypeId: string;
  startTime: string;
}
```

Каждый интерфейс — это описание формы данных, которые приходят с API или уходят на API.

**EventType** — приходит с `GET /api/event-types`. Содержит:
- `id` — уникальный идентификатор (строка)
- `name` — название (строка)
- `description` — описание (строка)
- `durationMinutes` — длительность в минутах (число)

**Booking** — приходит с `GET /api/admin/bookings` и возвращается из `POST /api/bookings`.

**TimeSlot** — приходит с `GET /api/event-types/{id}/slots`. Содержит начало и конец слота.

**EventTypeCreate** — то, что отправляется в `POST /api/admin/event-types`. Отличается от EventType отсутствием id (id создаёт сервер).

**BookingCreate** — то, что отправляется в `POST /api/bookings`.

**Почему не class, а interface?** В TypeScript классы — это полноценные объекты с методами и конструкторами. Интерфейсы — это просто описания формы данных. Для данных с API интерфейсы подходят идеально: они легче, не создают лишнего кода при компиляции.

**Почему `startTime` string, а не Date?** Потому что API возвращает строку (JSON не умеет в даты). Мы получаем строку в ISO 8601 формате: `"2026-05-30T12:00:00Z"` и работаем с ней через dayjs.

## 2.12. src/api.ts — «Телефонистка»

```ts
import type { EventType, Booking, TimeSlot, BookingCreate, EventTypeCreate } from './types';

const BASE_URL = '/api';

async function request<T>(url: string, options?: RequestInit): Promise<T> {
  const response = await fetch(`${BASE_URL}${url}`, {
    headers: { 'Content-Type': 'application/json' },
    ...options,
  });
  if (!response.ok) {
    const text = await response.text().catch(() => 'Unknown error');
    throw new Error(`API Error (${response.status}): ${text}`);
  }
  if (response.status === 204) return undefined as T;
  return response.json();
}
```

### Функция request — основа всего

Это обёртка вокруг встроенного браузерного `fetch`. Она делает три вещи:

1. **Добавляет BASE_URL** — любой вызов типа `/event-types` превращается в `/api/event-types`.
2. **Добавляет Content-Type** — все запросы отправляются как JSON.
3. **Обрабатывает ошибки** — если сервер ответил 4xx или 5xx, выбрасывает исключение с текстом ошибки.

**Шаблон типа `<T>`**: `async function request<T>(...)` — функция может работать с любым типом. Когда вызываешь `request<EventType[]>('/event-types')`, TypeScript знает, что результат будет массивом EventType.

### 5 функций-обёрток

```ts
export function fetchEventTypes(): Promise<EventType[]> {
  return request<EventType[]>('/event-types');
}

export function fetchSlots(eventTypeId: string, dateFrom?: string, dateTo?: string): Promise<TimeSlot[]> {
  const params = new URLSearchParams();
  if (dateFrom) params.set('dateFrom', dateFrom);
  if (dateTo) params.set('dateTo', dateTo);
  const qs = params.toString();
  return request<TimeSlot[]>(`/event-types/${eventTypeId}/slots${qs ? `?${qs}` : ''}`);
}

export function createBooking(data: BookingCreate): Promise<Booking> {
  return request<Booking>('/bookings', {
    method: 'POST',
    body: JSON.stringify(data),
  });
}

export function createEventType(data: EventTypeCreate): Promise<EventType> {
  return request<EventType>('/admin/event-types', {
    method: 'POST',
    body: JSON.stringify(data),
  });
}

export function fetchUpcomingBookings(): Promise<Booking[]> {
  return request<Booking[]>('/admin/bookings');
}
```

Каждая функция:
1. Принимает参数 (параметры), нужные для запроса.
2. Вызывает `request` с правильным URL и методом.
3. Возвращает Promise с правильным типом.

**GET-запросы** (fetchEventTypes, fetchSlots, fetchUpcomingBookings) — просто передают URL. Параметры query-string добавляются через `URLSearchParams`.

**POST-запросы** (createBooking, createEventType) — передают `method: 'POST'` и `body: JSON.stringify(data)`. `JSON.stringify` превращает JavaScript-объект в JSON-строку.

### Как использовать в компоненте

```tsx
import { fetchEventTypes } from '../api';

function MyPage() {
  const [data, setData] = useState<EventType[]>([]);

  useEffect(() => {
    fetchEventTypes()
      .then(setData)          // успех: сохраняем данные
      .catch(err => ...);     // ошибка: показываем сообщение
  }, []);
}
```

### Что будет, если API вернёт 500

```
fetch → сервер ответил 500
  │
request читает response.ok === false
  │
request читает текст ошибки
  │
request выбрасывает Error("API Error (500): Internal Server Error")
  │
  ↓
Компонент ловит ошибку в .catch()
  │
Показывает красный Alert с текстом ошибки
```

## 2.13. src/components/Layout.tsx — «Шапка и рамка»

```tsx
import { Outlet, useNavigate, useLocation } from 'react-router-dom';
import { AppShell, Group, Title, Switch, Text } from '@mantine/core';

export default function Layout() {
  const navigate = useNavigate();
  const location = useLocation();
  const isAdmin = location.pathname.startsWith('/admin');

  const toggle = () => {
    navigate(isAdmin ? '/' : '/admin');
  };

  return (
    <AppShell header={{ height: 60 }} padding="md">
      <AppShell.Header>
        <Group h="100%" px="md" justify="space-between">
          <Title order={3} onClick={() => navigate('/')} style={{ cursor: 'pointer' }}>
            Calendar Booking
          </Title>
          <Group>
            <Text size="sm" c={!isAdmin ? 'blue' : 'dimmed'} fw={!isAdmin ? 600 : 400}>Guest</Text>
            <Switch checked={isAdmin} onChange={toggle} />
            <Text size="sm" c={isAdmin ? 'blue' : 'dimmed'} fw={isAdmin ? 600 : 400}>Admin</Text>
          </Group>
        </Group>
      </AppShell.Header>
      <AppShell.Main>
        <Outlet />
      </AppShell.Main>
    </AppShell>
  );
}
```

**useNavigate** — функция для программной навигации. `navigate('/admin')` переходит на страницу админа.

**useLocation** — информация о текущем URL. `location.pathname` — это строка вроде `/admin` или `/book/et-1`.

**isAdmin** — вычисляем, находимся ли мы в админской части. Если путь начинается с `/admin` — значит, да.

**toggle** — функция, которая переключает между гостем и админом. Если сейчас админ — идём на `/`, если гость — на `/admin`.

**AppShell** — компонент Mantine, который создаёт каркас страницы:
- `header={{ height: 60 }}` — шапка высотой 60px
- `padding="md"` — отступы по краям

**AppShell.Header** — содержимое шапки. Здесь:
- Название слева (кликабельно — ведёт на главную)
- Переключатель Guest/Admin справа

**AppShell.Main** — основное содержимое. `<Outlet />` — это место, куда React Router вставит текущую страницу.

**Стилизация переключателя**: текст «Guest» подсвечивается синим, когда isAdmin=false. Текст «Admin» подсвечивается синим, когда isAdmin=true. Визуально понятно, какой режим активен.

## 2.14. src/components/EventTypeCard.tsx — «Визитка»

```tsx
import { Card, Text, Badge, Button, Group } from '@mantine/core';
import { useNavigate } from 'react-router-dom';
import type { EventType } from '../types';

interface EventTypeCardProps {
  eventType: EventType;
}

export default function EventTypeCard({ eventType }: EventTypeCardProps) {
  const navigate = useNavigate();

  return (
    <Card shadow="sm" padding="lg" radius="md" withBorder>
      <Group justify="space-between" mb="xs">
        <Text fw={500}>{eventType.name}</Text>
        <Badge color="blue">{eventType.durationMinutes} min</Badge>
      </Group>
      <Text size="sm" c="dimmed" mb="md">
        {eventType.description}
      </Text>
      <Button
        fullWidth
        variant="light"
        onClick={() => navigate(`/book/${eventType.id}`)}
      >
        Select Slot
      </Button>
    </Card>
  );
}
```

### Как выглядит результат

```
┌───────────────────────────────────┐
│  30-min Chat              30 min │  ← название + бейдж с длительностью
│  Quick call to discuss anything  │  ← описание серым цветом
│                                   │
│  [         Select Slot         ] │  ← кнопка на всю ширину
└───────────────────────────────────┘
```

### Mantine-компоненты в деталях

**Card** — карточка с тенью (`shadow="sm"`), скруглёнными углами (`radius="md"`), рамкой (`withBorder`).

**Group** — горизонтальный ряд элементов. `justify="space-between"` — элементы прижимаются к краям: название слева, бейдж справа.

**Badge** — цветная плашка. `color="blue"` — синий фон.

**Text** — текст. `fw={500}` — полужирный. `c="dimmed"` — серый цвет. `size="sm"` — мелкий шрифт.

**Button** — кнопка. `fullWidth` — на всю ширину. `variant="light"` — полупрозрачный фон. `onClick` — переход на страницу бронирования.

### Props

Компонент принимает один prop — `eventType`. TypeScript гарантирует, что у этого объекта есть поля `id`, `name`, `description`, `durationMinutes`. Если передать что-то другое — компилятор заорёт.

## 2.15. src/components/SlotPicker.tsx — «Календарь + время + бронь»

Самый сложный компонент проекта. Разберём его по частям.

### Пропсы (входные данные)

```tsx
interface SlotPickerProps {
  slots: TimeSlot[];       // слоты, полученные от API
  eventTypeId: string;     // ID типа события (для POST /api/bookings)
  loading: boolean;        // флаг загрузки
}
```

### Состояние (useState)

```tsx
const [selectedDate, setSelectedDate] = useState<Date | null>(null);
```

`selectedDate` — дата, которую выбрал пользователь на календаре. Изначально null (ничего не выбрано).

### Вычисляемые значения

**datesWithSlots** — Set строк вида `"2026-05-31"`. Используется для быстрой проверки: есть ли слоты в этот день?

```tsx
const datesWithSlots = new Set(
  effectiveSlots.slots.map((s) => dayjs(s.startTime).format('YYYY-MM-DD')),
);
```

**selectedDateSlots** — слоты для выбранной даты, отсортированные по времени.

```tsx
const selectedDateSlots = selectedDate
  ? effectiveSlots.slots
      .filter((s) => dayjs(s.startTime).isSame(selectedDate, 'day'))
      .sort((a, b) => dayjs(a.startTime).unix() - dayjs(b.startTime).unix())
  : [];
```

### Демо-данные (useMemo)

Когда API возвращает пустой массив (Prism заглючил, бэкенд не запущен), компонент генерирует демо-слоты:

```tsx
const effectiveSlots = useMemo(() => {
  if (slots.length > 0) return { slots, isDemo: false };

  const demo: TimeSlot[] = [];
  for (let hour = 9; hour < 18; hour++) {
    if (hour === 12) { hour++; continue; } // пропускаем обед
    const t = dayjs().add(1, 'day').hour(hour).minute(0).second(0).millisecond(0);
    demo.push({
      startTime: t.toISOString(),
      endTime: t.add(30, 'minute').toISOString(),
    });
  }
  return { slots: demo, isDemo: true };
}, [slots]);
```

**useMemo** — запоминает результат вычисления. Пересчитывает только когда меняется `slots`.

**Как генерируются слоты**: берём завтрашний день, для каждого часа с 9 до 18 (кроме 12 — обед) создаём 30-минутный слот. Получается 8 слотов на завтра.

### Календарь (Calendar из @mantine/dates)

```tsx
<Calendar
  minDate={today}
  maxDate={maxDate}
  getDayProps={(date) => {
    const key = dayjs(date).format('YYYY-MM-DD');
    const hasSlots = datesWithSlots.has(key);
    return {
      onClick: hasSlots ? () => setSelectedDate(date) : undefined,
      selected: selectedDate ? dayjs(date).isSame(selectedDate, 'day') : false,
    };
  }}
  renderDay={(date) => {
    const key = dayjs(date).format('YYYY-MM-DD');
    const hasSlots = datesWithSlots.has(key);
    return (
      <div style={{ position: 'relative' }}>
        <div>{date.getDate()}</div>
        {hasSlots && (
          <div style={{ ... }} />  // синяя точка под числом
        )}
      </div>
    );
  }}
/>
```

**minDate / maxDate** — календарь показывает только 14 дней (сегодня + 13).

**getDayProps** — для каждого дня решает:
- Есть слоты? → назначить onClick (день кликабельный)
- Нет слотов? → onClick не назначается (день серый, не реагирует на клик)
- Этот день выбран? → подсветить синим

**renderDay** — рисует содержимое каждого дня. Добавляет синюю точку под числом, если в этот день есть слоты.

### Подтверждение брони (SlotButton)

```tsx
function SlotButton({ slot, eventTypeId }: { slot: TimeSlot; eventTypeId: string }) {
  const [opened, setOpened] = useState(false);    // модалка открыта?
  const [confirming, setConfirming] = useState(false);  // идёт отправка?

  const handleConfirm = async () => {
    setConfirming(true);
    try {
      await createBooking({ eventTypeId, startTime: slot.startTime });
      notifications.show({ title: 'Booked!', message: 'Slot booked successfully.', color: 'green' });
      window.location.href = '/';
    } catch (err: any) {
      notifications.show({ title: 'Error', message: err.message, color: 'red' });
    } finally {
      setConfirming(false);
      setOpened(false);
    }
  };

  return (
    <>
      <Button variant="outline" onClick={() => setOpened(true)}>
        {dayjs(slot.startTime).format('HH:mm')}
      </Button>

      <Modal opened={opened} onClose={() => setOpened(false)} title="Confirm Booking" centered>
        <Stack>
          <Text size="sm"><strong>Date:</strong> {dayjs(slot.startTime).format('MMMM D, YYYY')}</Text>
          <Text size="sm"><strong>Time:</strong> {dayjs(slot.startTime).format('HH:mm')} – {dayjs(slot.endTime).format('HH:mm')}</Text>
          <Group justify="flex-end">
            <Button variant="default" onClick={() => setOpened(false)}>Cancel</Button>
            <Button onClick={handleConfirm} loading={confirming}>Confirm</Button>
          </Group>
        </Stack>
      </Modal>
    </>
  );
}
```

**Последовательность действий:**
1. Пользователь кликает на кнопку с временем — модалка открывается
2. В модалке — дата, время, Cancel/Confirm
3. Confirm → `handleConfirm`:
   - Показываем спиннер на кнопке (loading)
   - Отправляем POST /api/bookings
   - Успех → зелёное уведомление, кидаем на главную
   - Ошибка → красное уведомление, остаёмся на месте

**Почему window.location.href, а не useNavigate?** SlotButton — дочерний компонент внутри SlotPicker, который не имеет доступа к navigate (компонент не внутри Router). Можно было бы прокинуть navigate через props, но для простоты используем прямой переход.

## 2.16. src/pages/EventTypesPage.tsx — «Страница гостя»

```tsx
export default function EventTypesPage() {
  const [eventTypes, setEventTypes] = useState<EventType[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    fetchEventTypes()
      .then(setEventTypes)
      .catch((err) => setError(err.message))
      .finally(() => setLoading(false));
  }, []);
  ...
}
```

**Три состояния страницы:**

1. **loading** — крутилка Loader. Пока данные не пришли.
2. **error** — красный Alert с текстом ошибки. Если API ответил ошибкой.
3. **success** — список карточек. Данные загружены.

**Жизненный цикл:**

```
Компонент появился на экране
  │
useEffect(() => { ... }, [])
  │
fetchEventTypes()  ← асинхронный запрос
  │
  ├── успех → setEventTypes(data) → перерисовка → карточки
  │
  └── ошибка → setError(msg) → перерисовка → красный Alert
  │
  finally → setLoading(false) → скрываем крутилку
```

**SimpleGrid** — сетка, которая адаптируется под ширину экрана:
- на телефоне (base) — 1 колонка
- на планшете (sm) — 2 колонки
- на десктопе (lg) — 3 колонки

## 2.17. src/pages/BookingPage.tsx — «Страница брони»

```tsx
export default function BookingPage() {
  const { eventTypeId } = useParams<{ eventTypeId: string }>();
  ...
  useEffect(() => {
    if (!eventTypeId) return;

    const dateFrom = dayjs().startOf('day').toISOString();
    const dateTo = dayjs().add(14, 'day').endOf('day').toISOString();

    Promise.all([
      fetchEventTypes().then((types) => types.find((t) => t.id === eventTypeId) || null),
      fetchSlots(eventTypeId, dateFrom, dateTo),
    ]).then(([et, slotsData]) => {
      setEventType(et);
      setSlots(slotsData);
    });
  }, [eventTypeId]);
  ...
}
```

**useParams** — получает параметры из URL. Если URL `/book/et-1`, то `eventTypeId = "et-1"`.

**Promise.all** — запускает два запроса параллельно:
1. Загружаем все типы событий и находим нужный по id.
2. Загружаем слоты для этого типа.

Дата начала — сегодня 00:00. Дата конца — сегодня + 14 дней 23:59. Range строки — 14 полных дней.

## 2.18. src/pages/AdminPage.tsx — «Админ-панель»

Страница админа состоит из двух секций:

### Секция 1: Форма создания типа события

```tsx
const form = useForm({
  initialValues: {
    name: '',
    description: '',
    durationMinutes: 30,
  },
  validate: {
    name: (v) => (v.trim().length > 0 ? null : 'Name is required'),
    description: (v) => (v.trim().length > 0 ? null : 'Description is required'),
    durationMinutes: (v) => (v > 0 ? null : 'Duration must be positive'),
  },
});
```

**useForm** — хук из `@mantine/form`. Упрощает работу с формами:
- `initialValues` — начальные значения полей
- `validate` — функции проверки: если вернуть null, поле валидно; если строку — это сообщение об ошибке

**При отправке** (onSubmit):
1. Вызывается `createEventType(values)`
2. При успехе: зелёное уведомление, сброс формы, перезагрузка данных
3. При ошибке: красное уведомление

### Секция 2: Таблица броней

```tsx
<Table striped highlightOnHover>
  <Table.Thead>
    <Table.Tr>
      <Table.Th>Date</Table.Th>
      <Table.Th>Time</Table.Th>
      <Table.Th>Event Type</Table.Th>
    </Table.Tr>
  </Table.Thead>
  <Table.Tbody>
    {bookings.map(b => (
      <Table.Tr key={b.id}>
        <Table.Td>{dayjs(b.startTime).format('MMMM D, YYYY')}</Table.Td>
        <Table.Td>{dayjs(b.startTime).format('HH:mm')} – {dayjs(b.endTime).format('HH:mm')}</Table.Td>
        <Table.Td>{typeMap.get(b.eventTypeId) || b.eventTypeId}</Table.Td>
      </Table.Tr>
    ))}
  </Table.Tbody>
</Table>
```

**striped** — полосатая таблица (чередование цвета строк).
**highlightOnHover** — подсветка строки при наведении.

**typeMap** — Map из id → name (создаётся из массива eventTypes). Нужен, чтобы показывать название типа события вместо его id.

Форматирование даты через dayjs:
- `MMMM D, YYYY` → "May 31, 2026"
- `HH:mm` → "09:00"

---

# Глава 3. Жизненный цикл брони — ДАННЫЕ ПУТЕШЕСТВУЮТ

## 3.1. Полный путь запроса (схема)

```
[Браузер]                           [Vite]                          [Prism/Бэкенд]
   │                                   │                                │
   │ 1. GET /                          │                                │
   │──────────────────────────────────>│                                │
   │                                   │                                │
   │ 2. index.html                     │                                │
   │<──────────────────────────────────│                                │
   │                                   │                                │
   │ 3. GET /src/main.tsx              │                                │
   │──────────────────────────────────>│                                │
   │                                   │                                │
   │ 4. main.tsx → JS                  │                                │
   │<──────────────────────────────────│                                │
   │                                   │                                │
   │ 5. React запускается             │                                │
   │    Router: path="/"              │                                │
   │    → EventTypesPage              │                                │
   │                                   │                                │
   │ 6. GET /api/event-types           │                                │
   │──────────────────────────────────>│                                │
   │                                   │ 7. GET /api/event-types        │
   │                                   │──────────────────────────────>│
   │                                   │                                │
   │                                   │ 8. [{id:"et-1",...},...]      │
   │                                   │<──────────────────────────────│
   │ 9. JSON с типами                  │                                │
   │<──────────────────────────────────│                                │
   │                                   │                                │
   │10. React рисует карточки         │                                │
   │                                   │                                │
   │11. Клик на "Select Slot"         │                                │
   │    navigate('/book/et-1')        │                                │
   │                                   │                                │
   │12. Router: path="/book/et-1"     │                                │
   │    → BookingPage                 │                                │
   │                                   │                                │
   │13. GET /api/event-types/et-1/    │                                │
   │         slots?dateFrom=...&      │                                │
   │         dateTo=...               │                                │
   │──────────────────────────────────>│                                │
   │                                   │ 14. GET /api/event-types/...  │
   │                                   │──────────────────────────────>│
   │                                   │                                │
   │                                   │ 15. [{startTime, endTime},..] │
   │                                   │<──────────────────────────────│
   │16. JSON со слотами               │                                │
   │<──────────────────────────────────│                                │
   │                                   │                                │
   │17. SlotPicker: календарь +       │                                │
   │    кнопки времени                │                                │
   │                                   │                                │
   │18. Клик на [Confirm]             │                                │
   │    POST /api/bookings            │                                │
   │    {eventTypeId, startTime}      │                                │
   │──────────────────────────────────>│                                │
   │                                   │ 19. POST /api/bookings        │
   │                                   │──────────────────────────────>│
   │                                   │                                │
   │                                   │ 20. {id:"...",...}            │
   │                                   │<──────────────────────────────│
   │21. Уведомление "Booked!"         │                                │
   │    Редирект на /                 │                                │
```

## 3.2. Шаг 1: Загрузка типов событий

1. Пользователь открывает `http://localhost:5173`
2. Vite отдаёт `index.html`
3. Браузер загружает `main.tsx`, React запускается
4. React Router видит путь `/`, рендерит `EventTypesPage`
5. `EventTypesPage` в `useEffect` вызывает `fetchEventTypes()`
6. `fetchEventTypes()` вызывает `fetch('/api/event-types')`
7. Vite проксирует запрос на Prism (`localhost:4010`)
8. Prism ищет в `openapi.json` ответ для GET /api/event-types
9. Находит `example` с тремя типами событий
10. Отвечает JSON: `[{"id":"et-1","name":"30-min Chat",...}, ...]`
11. `fetchEventTypes()` получает JSON, превращает в массив `EventType[]`
12. `setEventTypes(data)` — обновляет состояние
13. React перерисовывает компонент — появляются 3 карточки

## 3.3. Шаг 2: Выбор типа и переход к слотам

1. Пользователь нажимает «Select Slot» на карточке «30-min Chat»
2. `EventTypeCard` вызывает `navigate('/book/et-1')`
3. React Router видит изменение URL, рендерит `BookingPage`
4. `BookingPage` в `useEffect`:
   - Берёт `eventTypeId = "et-1"` из URL
   - Вычисляет dateFrom (сегодня) и dateTo (сегодня + 14 дней)
   - Запускает `Promise.all([fetchEventTypes(), fetchSlots()])`
   - FetchEventTypes возвращает массив, из него выбираем тип с id="et-1"
   - FetchSlots возвращает слоты

## 3.4. Шаг 3: Показ календаря

1. `BookingPage` передаёт слоты в `SlotPicker`
2. `SlotPicker` вычисляет `datesWithSlots` — даты, в которых есть слоты
3. Рисует календарь с синими точками на этих датах
4. Пользователь видит: синие точки на 31 мая и 1 июня

## 3.5. Шаг 4: Выбор времени

1. Пользователь кликает на 31 мая
2. `setSelectedDate(new Date(2026, 4, 31))` — обновляется состояние
3. React перерисовывает: под календарём появляется список кнопок со временем
4. Пользователь нажимает [09:00]
5. `setOpened(true)` — открывается модалка подтверждения

## 3.6. Шаг 5: Подтверждение брони

1. Пользователь видит в модалке:
   - Date: May 31, 2026
   - Time: 09:00 – 09:30
   - Cancel | Confirm
2. Нажимает [Confirm]
3. `SlotButton.handleConfirm`:
   - `setConfirming(true)` — кнопка показывает спиннер
   - `await createBooking({ eventTypeId: "et-1", startTime: "..." })`
   - Prism отвечает: `{"id":"random123","eventTypeId":"et-1",...}`
   - Успех → зелёное уведомление «Slot booked successfully»
   - `window.location.href = '/'` → возврат на главную

## 3.7. Что если бэкенд упал?

```
fetchEventTypes()
  │
  └→ fetch('/api/event-types')
       │
       └→ Ошибка: сеть не отвечает (Prism не запущен)
       │
       └→ response.ok === false
            │
            └→ request выбрасывает Error("API Error (0): Failed to fetch")
                 │
                 └→ .catch в компоненте
                      │
                      └→ setError("Failed to fetch")
                           │
                           └→ Alert: "Failed to load event types"
                                │
                                └→ Пользователь видит красное сообщение
```

Пользователь никогда не увидит белый экран — будет красный Alert с понятным текстом.

То же самое для любого запроса — все ошибки обрабатываются и показываются.

---

# Глава 4. React для новичка — МАГИЯ БЕЗ МАГИИ

## 4.1. Что такое React

React — это библиотека для построения интерфейсов. Она придумана Facebook в 2013 году и сейчас используется почти везде.

**Проблема, которую решает React:**

Без React, когда данные меняются, ты пишешь что-то вроде:

```js
// Старый способ (jQuery / vanilla JS):
const button = document.getElementById('my-button');
button.textContent = 'Новый текст';
button.style.backgroundColor = 'red';
```

Это работает, но когда страница большая (100+ элементов), уследить за всеми изменениями невозможно. React делает так:

```tsx
// React-способ:
function MyButton({ text }) {
  return <button style={{ backgroundColor: 'red' }}>{text}</button>;
}
// React сам решит, когда и что обновлять на экране
```

**Главная идея React**: ты описываешь, как интерфейс выглядит в каждый момент времени, а React сам разбирается, что изменилось и как это обновить в браузере.

## 4.2. JSX — HTML внутри JavaScript

```tsx
const element = <div className="container">Привет, мир!</div>;
```

Это не строка, не HTML, не шаблон. Это **JSX** — расширение JavaScript, которое выглядит как HTML.

**JSX → обычный JS** (делает Vite):

```js
// JSX:
<div className="container">Привет, мир!</div>

// После компиляции (упрощённо):
React.createElement('div', { className: 'container' }, 'Привет, мир!');
```

**Правила JSX:**

| Правило | Пример |
|---------|--------|
| class → className | `<div className="x">` вместо `<div class="x">` |
| for → htmlFor | `<label htmlFor="x">` |
| Закрывать все теги | `<br />`, `<img />` |
| JavaScript в {} | `<div>{name}</div>`, `<div>{2 + 2}</div>` |
| Стили — объект | `<div style={{ color: 'red', fontSize: 16 }}>` |

## 4.3. Компонент — функция, которая возвращает HTML

```tsx
function Greeting() {
  return <h1>Привет!</h1>;
}
```

Компонент — это обычная функция. Она возвращает JSX. Используется как HTML-тег:

```tsx
function App() {
  return (
    <div>
      <Greeting />    ← вызов компонента
      <Greeting />    ← можно много раз
    </div>
  );
}
```

React превращает это в:

```html
<div>
  <h1>Привет!</h1>
  <h1>Привет!</h1>
</div>
```

**Имя компонента с большой буквы** — это важно. Если написать `<greeting />`, React подумает, что это HTML-тег, а не компонент.

## 4.4. Props — аргументы функции

```tsx
function Greeting({ name, age }: { name: string; age: number }) {
  return <h1>Привет, {name}! Тебе {age} лет.</h1>;
}

// Использование:
<Greeting name="Вася" age={25} />
<Greeting name="Петя" age={30} />
```

**Props** — это объект, который родительский компонент передаёт дочернему.

```
Родитель: <Greeting name="Вася" age={25} />
              │
              ▼
Дочерний: function Greeting(props) {
  props = { name: "Вася", age: 25 }
  ...
}
```

В примере выше мы используем **деструктуризацию** — сразу разбираем props на отдельные переменные.

**Типизация props:**

```tsx
// Плохо (без типа):
function Greeting(props) { ... }    // TypeScript не знает, что в props

// Хорошо (с типом):
interface GreetingProps {
  name: string;
  age?: number;   // ? — необязательный prop
}
function Greeting({ name, age }: GreetingProps) { ... }
```

## 4.5. State — память компонента

```tsx
function Counter() {
  const [count, setCount] = useState(0);

  return (
    <div>
      <p>Счёт: {count}</p>
      <button onClick={() => setCount(count + 1)}>+1</button>
    </div>
  );
}
```

**useState** — это хук (функция с приставкой use). Он создаёт ячейку памяти, которая живёт внутри компонента.

```
useState(0) → [count, setCount]
              │       │
              │       └── функция, которая меняет значение
              │
              └── текущее значение (0)
```

**Как это работает:**

1. Компонент рендерится первый раз → `useState(0)` создаёт ячейку со значением 0
2. Пользователь нажимает кнопку → `setCount(count + 1)` → count становится 1
3. React видит, что состояние изменилось → перерисовывает компонент
4. Компонент рендерится снова → `useState(0)` возвращает [1, setCount]

**Важно**: никогда не меняй state напрямую:

```tsx
// НЕПРАВИЛЬНО:
count = 5;          // React не узнает об изменении, экран не обновится

// ПРАВИЛЬНО:
setCount(5);        // React узнает, экран обновится
```

## 4.6. Как React понимает, что пора перерисоваться

React перерисовывает компонент когда:

1. **Изменился state** — вызвана функция `set...`
2. **Изменились props** — родитель передал новые значения
3. **Родитель перерисовался** — все дочерние компоненты тоже перерисовываются

Что НЕ вызывает перерисовку:
- Изменение обычной переменной (`let x = 5`)
- Изменение поля объекта без setState (`obj.name = 'new'`)
- Изменение элемента массива без setState (`arr[0] = 'x'`)

## 4.7. useEffect — «Сделай это, когда проснёшься»

```tsx
useEffect(() => {
  // Этот код выполнится после того, как компонент появится на экране
  fetchData();
}, []);   // ← массив зависимостей
```

**useEffect** выполняет код ПОСЛЕ рендеринга. Используется для:
- Загрузки данных с API (fetch)
- Подписки на события
- Таймеров и интервалов
- Работы с DOM напрямую

**Правила зависимостей:**

| Зависимости | Когда выполняется |
|-------------|-------------------|
| `[]` | Один раз при монтировании |
| `[id]` | При монтировании и каждый раз, когда меняется id |
| `[id, name]` | При монтировании и когда меняется id ИЛИ name |
| без массива | При каждом рендере (почти никогда не нужно) |

**Практический пример:**

```tsx
function UserProfile({ userId }: { userId: string }) {
  const [user, setUser] = useState(null);

  useEffect(() => {
    // Загружаем данные пользователя
    fetch(`/api/users/${userId}`)
      .then(r => r.json())
      .then(setUser);
  }, [userId]);  // ← перезагружаем, если userId изменился

  return <div>{user?.name}</div>;
}
```

## 4.8. Условный рендеринг

В JSX нельзя использовать if, но можно использовать логические операторы:

```tsx
function Greeting({ isLoggedIn }: { isLoggedIn: boolean }) {
  return (
    <div>
      {/* if (isLoggedIn) покажи приветствие */}
      {isLoggedIn && <p>Добро пожаловать!</p>}

      {/* if/else через тернарный оператор */}
      {isLoggedIn ? <p>Привет!</p> : <p>Войдите в систему</p>}
    </div>
  );
}
```

**Три способа:**

```tsx
// 1. && — показать/скрыть
{error && <Alert color="red">{error}</Alert>}

// 2. Тернарный — выбрать один из двух
{loading ? <Loader /> : <Content />}

// 3. if/return — разные компоненты целиком
if (loading) return <Loader />;
if (error) return <Alert />;
return <Content />;     // ← используется в нашем проекте
```

## 4.9. Списки и ключи (key)

```tsx
function EventList({ events }: { events: EventType[] }) {
  return (
    <div>
      {events.map(event => (
        <EventTypeCard key={event.id} eventType={event} />
      ))}
    </div>
  );
}
```

**key** — уникальный идентификатор для каждого элемента списка. React использует key, чтобы понять, какой элемент добавился, удалился или изменился.

**Правило**: key должен быть уникальным и стабильным. Используй id из данных.

```tsx
// ПРАВИЛЬНО:
{items.map(item => <Item key={item.id} />)}

// НЕПРАВИЛЬНО (нет key):
{items.map(item => <Item />)}

// ПЛОХО (key = индекс — меняется при добавлении/удалении):
{items.map((item, i) => <Item key={i} />)}
```

## 4.10. Обработка событий (onClick, onSubmit)

```tsx
function MyForm() {
  const handleClick = () => {
    alert('Клик!');
  };

  const handleSubmit = (event: React.FormEvent) => {
    event.preventDefault();  // ← ОЧЕНЬ ВАЖНО: не даём форме перезагрузить страницу
    console.log('Форма отправлена');
  };

  return (
    <form onSubmit={handleSubmit}>
      <button type="submit" onClick={handleClick}>Нажми меня</button>
    </form>
  );
}
```

**Правила обработчиков:**
- Имя начинается с `handle` — соглашение, не обязательное, но удобное
- `onClick`, `onSubmit`, `onChange` — пишутся с большой буквы
- `event.preventDefault()` — в формах ОБЯЗАТЕЛЬНО, иначе страница перезагрузится

## 4.11. Подъём состояния (lifting state up)

Когда два компонента должны делить одно состояние, его «поднимают» в общего родителя:

```tsx
function Parent() {
  const [value, setValue] = useState('');

  return (
    <div>
      <Input value={value} onChange={setValue} />
      <Display value={value} />
    </div>
  );
}

function Input({ value, onChange }: { value: string; onChange: (v: string) => void }) {
  return <input value={value} onChange={e => onChange(e.target.value)} />;
}

function Display({ value }: { value: string }) {
  return <p>Ты написал: {value}</p>;
}
```

В нашем проекте: `BookingPage` загружает слоты и передаёт их в `SlotPicker`. Состояние (массив слотов) живёт в `BookingPage`, потому что `SlotPicker` — просто отображатель.

## 4.12. React Router — навигация без перезагрузки

```tsx
// В main.tsx: оборачиваем приложение
<BrowserRouter>
  <App />
</BrowserRouter>

// В App.tsx: определяем маршруты
<Routes>
  <Route path="/" element={<Home />} />
  <Route path="/admin" element={<Admin />} />
  <Route path="/book/:id" element={<Book />} />
</Routes>

// В компоненте: переходим по ссылке
const navigate = useNavigate();
navigate('/admin');       // ← не перезагружает страницу!

// Получаем параметры из URL:
const { id } = useParams();
```

**useNavigate** — программная навигация (без клика по ссылке).
**useParams** — получение параметров из URL (`:id` из `/book/:id`).
**Link** — компонент для ссылок (как `<a>`, но без перезагрузки):

```tsx
<Link to="/admin">Админка</Link>
```

---

# Глава 5. Mantine — СТРОИТЕЛЬНЫЙ НАБОР ЛЕГО

## 5.1. Что такое Mantine

Mantine — это библиотека готовых React-компонентов. Вместо того чтобы писать CSS для каждой кнопки, карточки, календаря, мы берём готовые.

Без Mantine пришлось бы писать:

```css
.my-card {
  background: white;
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
  padding: 16px;
}
```

С Mantine:

```tsx
<Card shadow="sm" padding="lg" radius="md" withBorder>
  ...
</Card>
```

## 5.2. Установка и подключение

Mantine уже включён в `package.json`. Для подключения нужно:

1. **MantineProvider** в main.tsx — включает тему Mantine для всего приложения.
2. **Импорт CSS** — `@mantine/core/styles.css` и т.д.
3. **postcss.config.js** — для кастомизации.

## 5.3. Каталог компонентов нашего проекта

### AppShell — каркас страницы

```
┌─────────────────────────────────────┐
│  Calendar Booking    Guest [○] Admin │  ← Header
├─────────────────────────────────────┤
│                                     │
│                                     │
│       <Outlet /> — содержимое       │  ← Main
│                                     │
│                                     │
└─────────────────────────────────────┘
```

### Card — карточка

```
┌─────────────────────────────────────┐
│  Заголовок                    Badge │
│  Описание текстом                   │
│                                     │
│  [ Кнопка ]                         │
└─────────────────────────────────────┘
```

### Calendar — календарь

```
     May 2026
  Mo Tu We Th Fr Sa Su
              1  2  3
   4  5  6  7  8  9 10
  11 12 13 14 15 16 17
  18 19 20 21 22 23 24
  25 26 27 28 29 30 31●  ← синяя точка = есть слоты
   1● 2● 3  4  5  6  7
```

### Table — таблица

```
┌────────────┬──────────┬─────────────┐
│ Date       │ Time     │ Event Type  │
├────────────┼──────────┼─────────────┤
│ May 31     │ 09:00    │ 30-min Chat │
│ May 31     │ 10:00    │ 30-min Chat │
│ June 1     │ 09:00    │ 1-on-1 Mtg  │
└────────────┴──────────┴─────────────┘
```

### Modal — модальное окно

```
┌─────────────────────────────────────┐
│  Confirm Booking                 [X]│
├─────────────────────────────────────┤
│                                     │
│  Date: May 31, 2026                 │
│  Time: 09:00 – 09:30               │
│                                     │
│          [Cancel]  [Confirm]        │
│                                     │
└─────────────────────────────────────┘
```

### Notifications — уведомления

```
┌─────────────────────────────────────┐
│  ✓  Booked!                         │
│     Slot booked successfully.       │
└─────────────────────────────────────┘
     (зелёный, исчезает через 5 сек)

┌─────────────────────────────────────┐
│  ✗  Error                           │
│     API Error (500): Server error   │
└─────────────────────────────────────┘
     (красный, исчезает через 5 сек)
```

### Где что используется

| Компонент | Где | Зачем |
|-----------|-----|-------|
| `AppShell` | Layout.tsx | Каркас: шапка + контент |
| `Title` | Все страницы | Заголовки h1-h6 |
| `Text` | Везде | Текст с настройками размера/цвета |
| `Group` | Везде | Горизонтальный ряд элементов |
| `Stack` | Везде | Вертикальная стопка элементов |
| `Card` | EventTypeCard | Карточка с тенью |
| `Badge` | EventTypeCard | Плашка «30 min» |
| `Button` | Везде | Кнопки |
| `Switch` | Layout | Переключатель Guest/Admin |
| `Calendar` | SlotPicker | Календарь на 14 дней |
| `Modal` | SlotButton | Окно подтверждения |
| `Notifications` | SlotButton | Всплывающие сообщения (через хук) |
| `Loader` | EventTypesPage, BookingPage | Крутилка загрузки |
| `Alert` | EventTypesPage, BookingPage | Сообщение об ошибке |
| `SimpleGrid` | EventTypesPage | Адаптивная сетка карточек |
| `Table` | AdminPage | Таблица броней |
| `TextInput` | AdminPage | Поле ввода текста |
| `NumberInput` | AdminPage | Поле ввода числа |
| `Paper` | AdminPage | Область с рамкой |

## 5.4. Тёмная тема и кастомизация

Mantine поддерживает светлую и тёмную тему. Сейчас включена светлая:

```tsx
<MantineProvider defaultColorScheme="light">
```

Чтобы добавить переключатель темы, достаточно:
1. Создать кнопку, которая вызывает `useMantineColorScheme().toggleColorScheme()`
2. Добавить кнопку в шапку

### Основные цвета Mantine

```
blue    — основной (синий)
gray    — серый (фон, рамки)
red     — опасный (удалить, ошибка)
green   — успех (сохранить, готово)
yellow  — предупреждение
orange  — акцент
violet  — креатив
cyan    — информационный
teal    — спокойный
pink    — весёлый
grape   — необычный
```

### Как изменить цвет кнопки

```tsx
<Button color="red">Удалить</Button>
<Button color="grape">Что-то фиолетовое</Button>
```

---

# Глава 6. TypeScript — JAVASCRIPT С НАМОРДНИКОМ

## 6.1. Что такое TypeScript

JavaScript — это язык, где можно написать:

```js
function add(a, b) {
  return a + b;
}

add(5, 3)       // → 8 (ок)
add("5", 3)     // → "53" (странно, но работает)
add([], {})     // → "[object Object]" (что?!)
```

Ошибки проявляются только в рантайме (когда код уже работает). TypeScript добавляет типы — «намордник», который ловит ошибки на этапе написания кода:

```ts
function add(a: number, b: number): number {
  return a + b;
}

add(5, 3)       // → 8 (ок)
add("5", 3)     // → ❌ Ошибка: string нельзя передавать в number
add([], {})     // → ❌ Ошибка: не те типы
```

**TypeScript не работает в браузере**. Браузер понимает только обычный JavaScript. Vite сначала проверяет типы, потом превращает TS → JS и отдаёт браузеру чистый JS без типов.

## 6.2. Типы — Interface и Type

**Interface** — описание формы объекта:

```ts
interface EventType {
  id: string;
  name: string;
  description: string;
  durationMinutes: number;
}
```

**Type** — альтернативный способ, умеет больше (объединения, пересечения):

```ts
type Status = 'loading' | 'success' | 'error';
type ID = string | number;
```

В нашем проекте используем в основном interface, потому что они лучше работают с классами и наследованием.

## 6.3. Зачем нужны типы в этом проекте

1. **Самодокументация** — открыв `types.ts`, сразу видно, какие данные приходят с API.
2. **Автодополнение в IDE** — когда пишешь `eventType.`, редактор подсказывает поля: name, description, durationMinutes.
3. **Защита от опечаток** — `eventType.nam` → ошибка компиляции (нет такого поля).
4. **Рефакторинг** — переименовал поле в API → меняешь в одном месте (types.ts) → компилятор подсвечивает все места, где это поле используется.

## 6.4. Откуда берутся типы для API

Типы в `src/types.ts` созданы вручную на основе `specs/protocol.tsp`.

Процесс:
1. Смотрим в `protocol.tsp`: какие поля у модели EventType?
2. Создаём interface EventType в `types.ts` с теми же полями.
3. Смотрим в эндпоинты: что приходит и что уходит?
4. Создаём интерфейсы для запросов (BookingCreate, EventTypeCreate).

Если бы проект был bigger, можно было бы генерировать типы из OpenAPI-спецификации автоматически (openapi-typescript, openapi-generator). Но для 5 эндпоинтов проще написать 30 строк вручную.

## 6.5. Что будет, если типы не совпадут

Ситуация: бэкенд поменял API и теперь возвращает `"durationMins"` вместо `"durationMinutes"`.

1. TypeScript ничего не заметит (он проверяет только код, не данные).
2. В рантайме `eventType.durationMinutes` будет `undefined`.
3. При попытке показать «undefined min» — пользователь увидит странное.
4. Или хуже: `durationMinutes` используется в вычислениях → NaN → баг.

**Как этого избежать:**
- Менять типы синхронно с изменением API.
- Использовать валидацию на границе (zod, io-ts) — проверять, что данные с API соответствуют ожидаемому формату.

---

# Глава 7. Как это всё запускается — ПОД КАПОТОМ

## 7.1. Что происходит при `npm install`

```
Ты: npm install
  │
npm читает package.json
  │
npm смотрит: какие пакеты нужны, какие версии
  │
npm лезет в интернет (registry.npmjs.org)
  │
npm скачивает все пакеты и их зависимости
  │
  └── react 18.3.1
  └── @mantine/core 7.12.0
      └── @mantine/hooks 7.12.0 (зависимость Mantine)
      └── ...
  └── vite 5.4.0
  └── typescript 5.5.4
  └── ... (всего ~300 пакетов)
  │
npm раскладывает всё в node_modules/
  │
npm создаёт package-lock.json (фиксирует версии)
  │
Готово!
```

**node_modules/** — это ад. Папка весит ~200 МБ и содержит сотни папок. Никогда не смотри внутрь, если не хочешь сойти с ума.

## 7.2. Что происходит при `npm run dev`

```
Ты: npm run dev
  │
npm читает package.json → scripts → "dev": "vite"
  │
npm запускает: node node_modules/.bin/vite
  │
Vite загружается
  │
Vite читает vite.config.ts → плагины, proxy, порт
  │
Vite запускает dev-сервер на порту 5173
  │
Vite начинает следить за файлами в src/
  │
  ┌──────────────────────────────────────┐
  │  VITE v5.4.0  ready in 150ms        │
  │                                      │
  │  ➜  Local:   http://localhost:5173  │
  │  ➜  Network: http://192.168.1.2:5173│
  └──────────────────────────────────────┘
  │
Когда ты открываешь браузер:
  │
Vite получает запрос на /
  │
Vite отдаёт index.html
  │
Когда браузер просит /src/main.tsx:
  │
Vite компилирует main.tsx НА ЛЕТУ:
  ├── Превращает TS → JS
  ├── Превращает JSX → JS
  ├── Добавляет HMR (hot reload)
  └── Отдаёт браузеру
```

**HMR (Hot Module Replacement)**: когда ты меняешь любой файл в src/, Vite отслеживает изменение и отправляет обновление в браузер. Браузер применяет изменения без полной перезагрузки страницы.

## 7.3. Что происходит при `npm run dev:mock`

```
Ты: npm run dev:mock
  │
npm читает package.json → "dev:mock": "concurrently \"vite\" \"prism mock openapi.json\""
  │
concurrently запускает ДВЕ программы в одном окне:
  │
  ├── ПРОГРАММА 1: vite
  │   └── Dev-сервер на порту 5173
  │
  └── ПРОГРАММА 2: prism mock openapi.json
      └── Мок-сервер на порту 4010
      │
      Prism читает openapi.json
      │
      Prism создаёт 5 фейковых эндпоинтов
      │
      Prism готов отвечать на запросы
  │
Ты видишь в терминале:
  │
  [vite]  Local:   http://localhost:5173
  [prism] Prism is listening on http://127.0.0.1:4010
```

Когда ты нажимаешь Ctrl+C, concurrently останавливает обе программы сразу.

## 7.4. Что происходит при `npm run build`

```
Ты: npm run build
  │
npm читает package.json → "build": "tsc -b && vite build"
  │
ШАГ 1: tsc -b (TypeScript компиляция)
  │
  tsc читает tsconfig.json
  │
  tsc проверяет ВСЕ файлы в src/ на ошибки типов
  │
  │
  ├── Есть ошибки? → ❌ процесс останавливается, ошибки выводятся
  │
  └── Нет ошибок? → ✓ продолжаем
  │
ШАГ 2: vite build
  │
  Vite читает index.html
  │
  Vite находит все импорты (main.tsx → App.tsx → ...)
  │
  Vite собирает всё в один граф зависимостей
  │
  Vite применяет:
  │   ├── Tree-shaking: убирает неиспользуемый код
  │   ├── Minification: сжимает JS (убирает пробелы, переименовывает)
  │   ├── CSS extraction: собирает CSS отдельно
  │   └── Hashing: добавляет хэши к именам файлов
  │
  Vite пишет результат в dist/:
  │
  dist/
  ├── index.html               ← тот же, но со ссылками на собранные файлы
  ├── assets/index-DAMFDw3G.css ← весь CSS в одном файле
  └── assets/index-CxpkO7cI.js  ← весь JS в одном файле
```

**Итог**: папка `dist/` — это готовый к загрузке на сервер сайт. Её можно кинуть на любой статический хостинг (Netlify, Vercel, GitHub Pages).

## 7.5. Папка dist/ — что внутри

```
dist/
├── index.html                 ← 0.4 KB (только ссылки на assets)
│
└── assets/
    ├── index-DAMFDw3G.css     ← 213 KB (весь Mantine + наши стили)
    └── index-CxpkO7cI.js      ← 397 KB (React + Mantine + наш код)
```

**Почему так много?** Mantine весит ~200 KB, React ~130 KB, React Router ~50 KB, наш код ~15 KB. В сжатом виде (gzip) это ~150 KB — нормально для современного приложения.

---

# Глава 8. Как вносить изменения — А ТЕПЕРЬ СЛОМАЙ ЭТО

## 8.1. Хочу добавить новую страницу

Допустим, нужна страница «О проекте» (About).

**Шаг 1:** Создай файл `src/pages/AboutPage.tsx`:

```tsx
import { Container, Title, Text } from '@mantine/core';

export default function AboutPage() {
  return (
    <Container>
      <Title>О проекте</Title>
      <Text>Это приложение для бронирования слотов.</Text>
    </Container>
  );
}
```

**Шаг 2:** Добавь маршрут в `src/App.tsx`:

```tsx
import AboutPage from './pages/AboutPage';
...
<Route path="/about" element={<AboutPage />} />
```

**Шаг 3:** Добавь ссылку в `src/components/Layout.tsx` (в шапку):

```tsx
<Button variant="subtle" onClick={() => navigate('/about')}>About</Button>
```

**Готово.** Открой `http://localhost:5173/about`.

## 8.2. Хочу изменить цвет кнопки

```tsx
<Button color="red">Удалить</Button>
<Button color="green">Сохранить</Button>
<Button color="grape">Фиолетовая</Button>
```

**Если нужен нестандартный цвет**, можно задать в MantineProvider или изменить тему. Для простых случаев — используй один из 14 стандартных цветов.

## 8.3. Хочу добавить новый API-вызов

Допустим, нужно удалять брони.

**Шаг 1:** Добавь функцию в `src/api.ts`:

```ts
export function deleteBooking(id: string): Promise<void> {
  return request<void>(`/bookings/${id}`, {
    method: 'DELETE',
  });
}
```

**Шаг 2:** Добавь тип в `src/types.ts` (если нужно).

**Шаг 3:** Добавь эндпоинт в `openapi.json` (для Prism):

```json
"/api/bookings/{id}": {
  "delete": {
    "operationId": "deleteBooking",
    "parameters": [
      { "name": "id", "in": "path", "required": true, "schema": { "type": "string" } }
    ],
    "responses": {
      "204": { "description": "Deleted" }
    }
  }
}
```

**Шаг 4:** Используй в компоненте:

```tsx
<Button color="red" onClick={() => deleteBooking(bookingId)}>Удалить</Button>
```

## 8.4. Хочу изменить название сайта

Находится в двух местах:

1. **Вкладка браузера** — `ui/index.html`, строка `<title>Calendar Booking</title>`.
2. **Шапка сайта** — `ui/src/components/Layout.tsx`, строка `Calendar Booking`.

Меняй в обоих.

## 8.5. Хочу убрать Prism и подключить реальный бэкенд

**Способ 1 (через proxy, рекомендуется для разработки):**

В `vite.config.ts` измени `target`:

```ts
proxy: {
  '/api': {
    target: 'http://localhost:3000',  // ← твой бэкенд
    changeOrigin: true,
  },
}
```

Запускай `npm run dev` (без `:mock`). Все запросы `/api/*` пойдут на реальный бэкенд.

**Способ 2 (через полный URL в api.ts, если бэкенд на другом домене):**

```ts
const BASE_URL = 'http://192.168.1.100:3000/api';
```

Тогда на бэкенде нужно настроить CORS (разрешить запросы с `localhost:5173`).

**Способ 3 (продакшен — фронтенд и бэкенд на одном домене):**

В продакшене фронтенд и бэкенд обычно работают на одном домене:
- `https://mysite.com` — отдаёт index.html (статику)
- `https://mysite.com/api/...` — обрабатывает бэкенд

В этом случае proxy не нужен, а в `api.ts` BASE_URL = `/api`.

## 8.6. Хочу другую библиотеку компонентов

Если Mantine надоел:

1. Удали пакеты: `npm uninstall @mantine/core @mantine/hooks @mantine/dates @mantine/form @mantine/notifications @tabler/icons-react`
2. Удали `postcss.config.js` и `postcss-preset-mantine` из `package.json`.
3. Удали импорты CSS-стилей из `main.tsx`.
4. Удали `<MantineProvider>` из `main.tsx`.
5. Установи новую библиотеку (например, `npm install @chakra-ui/react`).
6. Замени все Mantine-компоненты на компоненты новой библиотеки.
7. ...на самом деле проще оставить Mantine.

## 8.7. Хочу изменить календарь (не 14 дней)

Два места:

1. В `SlotPicker.tsx` — `maxDate`:

```tsx
const maxDate = dayjs().add(30, 'day').endOf('day').toDate();  // 30 дней вместо 14
```

2. В `BookingPage.tsx` — параметры запроса:

```tsx
const dateTo = dayjs().add(30, 'day').endOf('day').toISOString();
```

## 8.8. Хочу добавить новое поле в форму создания типа

**Шаг 1:** Добавь поле в `types.ts`:

```ts
export interface EventTypeCreate {
  name: string;
  description: string;
  durationMinutes: number;
  maxAttendees: number;    // ← новое поле
}
```

**Шаг 2:** Добавь поле в форму `AdminPage.tsx`:

```tsx
<NumberInput label="Max attendees" min={1} {...form.getInputProps('maxAttendees')} />
```

**Шаг 3:** Добавь поле в `initialValues` и `validate`.

**Шаг 4:** Обнови `openapi.json` — добавь поле в схему `EventTypeCreate`.

---

# Глава 9. Словарик — ЧТО ЭТА ХРЕНЬ ЗНАЧИТ?

| Термин | Простыми словами | Синонимы |
|--------|-----------------|----------|
| **API** | Способ для программ общаться друг с другом | REST API, эндпоинт, веб-сервис |
| **BrowserRouter** | Компонент, который учит React понимать URL | — |
| **Build** | Сборка проекта в готовые файлы | Сборка, билд, компиляция |
| **Component** | Кусочек интерфейса (кнопка, карточка, страница) | Компонент, виджет, блок |
| **CORS** | Полиция браузера, блокирует запросы на другие домены | — |
| **CSS** | Язык описания внешнего вида (цвета, отступы, шрифты) | Стили, стилизация |
| **dependencies** | Пакеты, нужные для работы приложения | Зависимости, libs |
| **devDependencies** | Пакеты, нужные только для разработки | Инструменты |
| **DOM** | Внутреннее представление страницы в браузере | Document Object Model |
| **Endpoint** | Конкретный URL API (например, `/api/bookings`) | Ручка, точка входа |
| **ESModule** | Современный формат JavaScript-модулей (import/export) | ESM, модули |
| **fetch** | Встроенная в браузер функция для HTTP-запросов | — |
| **Git** | Система контроля версий | — |
| **HMR** | Горячая перезагрузка — обновление страницы без перезагрузки | Hot Module Replacement |
| **Hook** | Функция с приставкой `use` (useState, useEffect) | Хук |
| **HTML** | Язык разметки страницы | — |
| **HTTP** | Протокол передачи данных в интернете | — |
| **ISO 8601** | Формат даты: `2026-05-30T12:00:00Z` | — |
| **JSON** | Формат данных для обмена между программами | JavaScript Object Notation |
| **JSX** | HTML-подобный синтаксис внутри JavaScript | — |
| **localhost** | Адрес твоего собственного компьютера | 127.0.0.1 |
| **Mantine** | Библиотека готовых компонентов (кнопки, карточки, календарь) | UI Kit, библиотека компонентов |
| **npm** | Менеджер пакетов, скачивает библиотеки | Менеджер пакетов |
| **node_modules** | Папка со скачанными пакетами (НЕ ТРОГАТЬ) | Чёрная дыра, помойка |
| **OpenAPI** | Формат описания API в JSON/YAML | Swagger |
| **Port** | Номер входа в программу (5173, 4010, 3000) | Порт |
| **Prism** | Заглушка бэкенда для разработки | Mock-сервер, симулятор |
| **Props** | Данные, которые родитель передаёт дочернему компоненту | Свойства, пропы, атрибуты |
| **Proxy** | Подмена адреса запроса | Прокси, посредник |
| **React** | Библиотека для построения интерфейсов | — |
| **React Router** | Библиотека для навигации между страницами | Роутер, маршрутизатор |
| **SPA** | Всё приложение в одной странице, без перезагрузок | Single Page Application |
| **State** | Память компонента (данные, которые меняются) | Состояние, стейт |
| **Tree-shaking** | Удаление неиспользуемого кода при сборке | — |
| **TypeScript** | JavaScript с типами | TS, тайпскрипт |
| **URL** | Адрес страницы в интернете | Uniform Resource Locator |
| **useEffect** | Хук, выполняющий код после рендеринга | Эффект, side effect |
| **useState** | Хук для создания переменной состояния | Стейт-хук |
| **Vite** | Сборщик и dev-сервер | Сборщик, билд-система |

---

# Глава 10. Часто задаваемые вопросы — А ЧТО, ЕСЛИ...

## 10.1. Почему после бронирования я не вижу новую бронь в админке?

Prism — это заглушка. Он **не сохраняет данные** между запросами.

```
POST /api/bookings → Prism отвечает: { id: "random123", ... }
  (данные выдуманы, никуда не записаны)

GET /api/admin/bookings → Prism отвечает: [] (пустой массив)
  (Prism ничего не помнит)
```

**На реальном бэкенде** данные будут сохраняться в базе данных, и бронь будет видна в админке. На этапе разработки с Prism это нормально.

## 10.2. Почему календарь показывает только 14 дней?

Так написано в спецификации: «Доступные слоты формируются на 14 дней, начиная с текущей даты».

Если нужно больше — меняй:

1. В `BookingPage.tsx`:
```tsx
const dateTo = dayjs().add(30, 'day').endOf('day').toISOString();
```

2. В `SlotPicker.tsx`:
```tsx
const maxDate = dayjs().add(30, 'day').endOf('day').toDate();
```

## 10.3. Почему приложение не работает без Prism?

Vite настроен проксировать `/api/*` запросы на `localhost:4010`. Если Prism не запущен, соединение отклоняется, fetch выбрасывает ошибку.

**Решение**: запусти `npm run dev:mock` — Prism стартанёт автоматически.

**Если нужен реальный бэкенд** — см. Главу 8.5.

## 10.4. Что за синие точки на календаре?

Это дни, в которые есть свободные слоты. Только на эти дни можно кликнуть. Если день серый — слотов нет.

Синие точки берутся из данных API: в каких днях есть TimeSlot, там и точки.

## 10.5. Почему некоторые дни не кликабельны?

Потому что на них нет слотов. Причины:
- Выходной день
- Все слоты заняты (бэкенд не отдаёт занятые)
- Prism не настроен возвращать слоты на этот день
- Бэкенд вернул пустой массив

## 10.6. UI выглядит не так / ошибка в консоли браузера

**Порядок действий:**

1. Открой консоль (F12 → Console).
2. Посмотри, есть ли красные ошибки.
3. Скопируй текст ошибки.
4. Определи тип:
   - `Failed to fetch` / `NetworkError` → Prism не запущен
   - `Cannot read property 'map' of undefined` → данные пришли не те (проверь API)
   - `Cannot find module` → не хватает пакета (запусти `npm install`)
   - TypeScript-ошибки → проверь терминал с Vite

## 10.7. Не могу найти, где менять текст

- **Заголовок страницы** (вкладка браузера): `index.html`, строка `<title>`
- **Заголовок в шапке**: `Layout.tsx`, строка `Calendar Booking`
- **Текст на странице типов**: `EventTypesPage.tsx`
- **Текст в модалке**: `SlotPicker.tsx`
- **Текст в админке**: `AdminPage.tsx`
- **Текст ошибок**: `api.ts` (общие), компоненты страниц (конкретные)

---

# Глава 11. Git для самых маленьких — КАК НЕ УБИТЬ ВСЁ

Git — это как «сохранения» в видеоигре. Ты можешь откатиться к любому сохранению, если что-то сломал.

## 11.1. git status — что изменилось

```bash
git status
```

Показывает, какие файлы изменены, какие новые, какие удалены.

## 11.2. git diff — покажи подробности

```bash
git diff           # изменения в unstaged файлах
git diff --staged  # изменения в staged файлах
```

## 11.3. git add — подготовить к сохранению

```bash
git add src/components/SlotPicker.tsx   # один файл
git add .                                # все файлы (осторожно)
```

## 11.4. git commit — сохранить

```bash
git commit -m "Что я сделал"
```

Хороший commit message: кратко и понятно. Плохо: `fix`, `upd`, `123`. Хорошо: `fix: пустой календарь при выборе даты`.

## 11.5. git checkout — откатить

```bash
git checkout -- src/components/SlotPicker.tsx   # откатить один файл
git checkout -- .                                # откатить всё (ОПАСНО)
```

**ВНИМАНИЕ**: `git checkout -- .` откатывает ВСЕ изменения, которые не были закоммичены. Изменения пропадут навсегда.

Более безопасный вариант — посмотреть изменения перед откатом:

```bash
git diff src/components/SlotPicker.tsx   # посмотреть изменения
git checkout -- src/components/SlotPicker.tsx  # если не нравится — откатить
```

## 11.6. Что делать, если всё сломалось

```bash
# Вариант 1: откатить конкретный файл
git checkout -- src/pages/AdminPage.tsx

# Вариант 2: откатить всё (незакоммиченное)
git checkout -- .

# Вариант 3: откатиться к последнему коммиту (удалит незакоммиченные изменения)
git reset --hard HEAD

# Вариант 4: посмотреть историю коммитов и откатиться к конкретному
git log --oneline
git reset --hard abc123
```

**Если не уверен — спроси. Лучше спросить, чем потерять код.**

---

*Конец руководства. Если ты прочитал всё это и ничего не понял — перечитай Главу 1. Если понял — ты готов править код.*

*Последнее правило программиста: если что-то сломалось — не паникуй. `git checkout -- .` вернёт всё как было.*

*Второе последнее правило: если `git checkout -- .` не помог — подожди 5 минут, паника пройдёт, решение найдётся.*

---

*Создано с любовью и чаем. Май 2026.*
