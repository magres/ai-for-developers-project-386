# Calendar Booking UI

Фронтенд для Calendar Booking API на TypeScript + Vite + Mantine.

## Быстрый старт

```bash
cd ui
npm install
npm run dev:mock
```

Эта команда запускает одновременно:
- **Vite** (фронтенд) на http://localhost:5173
- **Prism** (мок-сервер API) на http://localhost:4010

Vite проксирует запросы `/api/*` на Prism, поэтому фронтенд работает «из коробки» без настоящего бэкенда.

## Режимы

| URL | Режим | Описание |
|-----|-------|----------|
| `/` | Гость | Список типов событий → выбор слота → бронь |
| `/book/:eventTypeId` | Гость | Календарь свободных слотов (14 дней) |
| `/admin` | Админ | Создание типа события + список броней |

Переключение между Guest/Admin — в шапке сайта.

## Команды

```bash
npm run dev       # Только Vite (без мок-сервера)
npm run dev:mock  # Vite + Prism одновременно
npm run build     # Сборка для продакшена
npm run preview   # Предпросмотр собранного
```

## Структура

```
ui/
├── src/
│   ├── main.tsx                 # Входная точка
│   ├── App.tsx                  # Роутер
│   ├── types.ts                 # TypeScript типы
│   ├── api.ts                   # Вызовы API
│   ├── components/
│   │   ├── Layout.tsx           # Шапка + обёртка
│   │   ├── EventTypeCard.tsx    # Карточка типа события
│   │   └── SlotPicker.tsx       # Календарь + выбор слота
│   └── pages/
│       ├── EventTypesPage.tsx   # Список типов событий
│       ├── BookingPage.tsx      # Выбор слота и бронь
│       └── AdminPage.tsx        # Админ-панель
├── openapi.json                 # Спецификация для Prism
├── vite.config.ts               # Vite + proxy на Prism
└── package.json
```

## API (проксируется на Prism)

| Метод | Путь | Описание |
|-------|------|----------|
| GET | `/api/event-types` | Список типов событий |
| GET | `/api/event-types/:id/slots?dateFrom=&dateTo=` | Свободные слоты |
| POST | `/api/bookings` | Создать бронь |
| POST | `/api/admin/event-types` | Создать тип события |
| GET | `/api/admin/bookings` | Все будущие брони |
