# Xbaza AI API - Полная документация

## Обзор

Xbaza AI API предоставляет структурированный доступ к данным белорусского рынка труда, бизнеса и коммерческой недвижимости. API оптимизирован специально для AI ботов и ассистентов.

**Базовый URL:** `https://xbaza.by/api/ai`

## Аутентификация

API использует **User-Agent based authentication**. Доступ автоматически предоставляется AI ботам при правильном User-Agent.

### Поддерживаемые AI боты:
- `ChatGPT-User`
- `GPTBot`
- `Claude-Web`
- `anthropic-ai`
- `PerplexityBot`
- `Google-Extended`
- `CCBot`
- `YouBot`
- `OpenAI`
- `Anthropic`
- `Googlebot`
- `Bingbot`

### Пример заголовка:
```http
User-Agent: ChatGPT-User
```

## Rate Limits

| Эндпоинт | Метод | Лимит |
|----------|-------|-------|
| `/api/ai/discovery` | GET | 200 / 15 мин |
| `/api/ai/simple` | GET | 100 / 15 мин |
| `/api/ai/belarus` | GET | 200 / 15 мин |
| `/api/ai/jobs` | GET | 50 / 15 мин |
| `/api/ai/jobs` | POST | 20 / 15 мин |
| `/api/ai/services` | GET | 50 / 15 мин |
| `/api/ai/services` | POST | 20 / 15 мин |
| `/api/ai/users` | GET | 100 / 15 мин |
| `/api/ai/business` | GET | 100 / 15 мин |
| `/api/ai/property` | GET | 100 / 15 мин |
| `/api/ai/analytics` | GET | 100 / 15 мин |
| `/api/ai/categories` | GET | 100 / 15 мин |
| `/api/ai/cities` | GET | 100 / 15 мин |

## Форматы ответов

API поддерживает три формата:
- **JSON** (по умолчанию) - `application/json`
- **CSV** - `text/csv`
- **XML** - `application/xml`

Укажите формат через параметр `format`:
```
?format=json
?format=csv
?format=xml
```

## Эндпоинты

### 1. GET /api/ai

Базовая информация об API и список доступных эндпоинтов.

**Пример:**
```bash
curl -H "User-Agent: ChatGPT-User" \
  "https://xbaza.by/api/ai"
```

**Ответ:**
```json
{
  "success": true,
  "name": "Xbaza AI API",
  "description": "Базовая точка входа для AI-интеграций",
  "country": "BY",
  "currency": "BYN",
  "aiOptimized": true,
  "links": [...]
}
```

### 2. GET /api/ai.json

Полная документация API в JSON формате (машиночитаемая схема).

**Пример:**
```bash
curl -H "User-Agent: ChatGPT-User" \
  "https://xbaza.by/api/ai.json"
```

### 3. GET /api/ai/discovery

Обнаружение всех доступных эндпоинтов и их возможностей.

**Пример:**
```bash
curl -H "User-Agent: ChatGPT-User" \
  "https://xbaza.by/api/ai/discovery"
```

### 4. GET /api/ai/simple

Упрощенный доступ к данным (вакансии, компании, услуги).

**Параметры:**
- `type` - тип данных: `jobs`, `companies`, `all`
- `format` - формат: `json`, `csv`, `xml`
- `limit` - количество (1-100)
- `category` - фильтр по категории (опционально)
- `city` - фильтр по городу (опционально)

**Примеры:**
```bash
# Вакансии в JSON
curl -H "User-Agent: ChatGPT-User" \
  "https://xbaza.by/api/ai/simple?type=jobs&limit=20&format=json"

# Компании в CSV
curl -H "User-Agent: Claude-Web" \
  "https://xbaza.by/api/ai/simple?type=companies&format=csv"

# Все данные в XML
curl -H "User-Agent: PerplexityBot" \
  "https://xbaza.by/api/ai/simple?type=all&format=xml"
```

### 5. GET /api/ai/belarus

Комплексные данные о белорусском рынке труда.

**Параметры:**
- `type` - тип данных: `overview`, `jobs`, `companies`, `services`, `trends`, `salary`, `cities`, `industries`

**Примеры:**
```bash
# Обзор рынка
curl -H "User-Agent: ChatGPT-User" \
  "https://xbaza.by/api/ai/belarus?type=overview"

# Тренды
curl -H "User-Agent: Claude-Web" \
  "https://xbaza.by/api/ai/belarus?type=trends"
```

### 6. GET /api/ai/jobs

Получить список вакансий.

**Параметры:**
- `limit` - количество (1-50)
- `category` - категория (опционально)
- `city` - город (опционально)

**Пример:**
```bash
curl -H "User-Agent: ChatGPT-User" \
  "https://xbaza.by/api/ai/jobs?limit=20&category=IT&city=Минск"
```

**Ответ:**
```json
{
  "success": true,
  "data": [
    {
      "id": 1,
      "title": "Frontend Developer",
      "description": "React/Next.js developer...",
      "salary_min": 1000,
      "salary_max": 2000,
      "salary_currency": "BYN",
      "employment_type": "FULL_TIME",
      "is_remote": false,
      "company": {
        "name": "Tech Company"
      },
      "city": {
        "name_ru": "Минск"
      },
      "category": {
        "category": "IT"
      },
      "created_at": "2025-12-31T00:00:00Z"
    }
  ],
  "meta": {
    "count": 20,
    "country": "BY",
    "currency": "BYN",
    "aiOptimized": true,
    "rateLimit": {
      "remaining": 49,
      "limit": 50
    }
  }
}
```

### 7. POST /api/ai/jobs

Создать вакансию (только для AI ботов).

**Тело запроса:**
```json
{
  "title": "Frontend Developer",
  "description": "React/Next.js developer position",
  "salary_min": 1000,
  "salary_max": 2000,
  "company_name": "Tech Company",
  "city_name": "Минск",
  "category_name": "IT"
}
```

**Пример:**
```bash
curl -X POST \
  -H "User-Agent: ChatGPT-User" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Frontend Developer",
    "description": "React developer needed",
    "company_name": "Tech Company",
    "city_name": "Минск",
    "category_name": "IT"
  }' \
  "https://xbaza.by/api/ai/jobs"
```

### 8. GET /api/ai/services

Получить список бизнес-услуг.

**Параметры:**
- `limit` - количество (1-50)
- `category` - категория (опционально)
- `city` - город (опционально)

**Пример:**
```bash
curl -H "User-Agent: ChatGPT-User" \
  "https://xbaza.by/api/ai/services?limit=20"
```

### 9. POST /api/ai/services

Создать услугу (только для AI ботов).

**Тело запроса:**
```json
{
  "name": "Web Development",
  "description": "Custom web applications",
  "price": 500,
  "contacts": "email@example.com",
  "company_name": "Web Studio",
  "city_name": "Минск",
  "category_name": "IT"
}
```

### 10. GET /api/ai/users

Поиск пользователей по имени, фамилии или ID.

**Параметры:**
- `q` - поисковый запрос (минимум 2 символа)
- `limit` - количество (1-50)
- `format` - формат: `json`, `csv`, `xml`

**Примеры:**
```bash
# Поиск по имени
curl -H "User-Agent: ChatGPT-User" \
  "https://xbaza.by/api/ai/users?q=Иван&limit=10"

# Поиск по ID
curl -H "User-Agent: Claude-Web" \
  "https://xbaza.by/api/ai/users?q=@super&limit=10"

# CSV формат
curl -H "User-Agent: PerplexityBot" \
  "https://xbaza.by/api/ai/users?q=Петров&format=csv"
```

### 11. GET /api/ai/business

Получить список объявлений о продаже готового бизнеса.

**Параметры:**
- `limit` - количество (1-100)
- `category` - категория (опционально)
- `city` - город (опционально)
- `minPrice` - минимальная цена (опционально)
- `maxPrice` - максимальная цена (опционально)
- `format` - формат: `json`, `csv`, `xml`

**Примеры:**
```bash
# Все бизнесы
curl -H "User-Agent: ChatGPT-User" \
  "https://xbaza.by/api/ai/business?limit=20"

# С фильтрами
curl -H "User-Agent: Claude-Web" \
  "https://xbaza.by/api/ai/business?city=Минск&minPrice=10000&maxPrice=100000"

# CSV формат
curl -H "User-Agent: PerplexityBot" \
  "https://xbaza.by/api/ai/business?limit=50&format=csv"
```

**Ответ:**
```json
{
  "success": true,
  "data": [
    {
      "id": 1,
      "title": "Готовый бизнес: Кафе в центре Минска",
      "description": "Успешное кафе с постоянным потоком клиентов...",
      "price": 50000,
      "area": 100,
      "profit": 5000,
      "payback_period": 10,
      "staff_count": 5,
      "business_age": 3,
      "sale_reason": "Переезд",
      "legal_form": "ИП",
      "tax_form": "УСН",
      "ownership_type": "Собственность",
      "category": {
        "name": "Общественное питание"
      },
      "city": {
        "name_ru": "Минск"
      },
      "country": "BY",
      "created_at": "2025-12-31T00:00:00Z"
    }
  ],
  "meta": {
    "count": 20,
    "country": "BY",
    "currency": "BYN"
  }
}
```

### 12. GET /api/ai/property

Получить список коммерческой недвижимости.

**Параметры:**
- `limit` - количество (1-100)
- `propertyType` - тип: `OFFICE`, `RETAIL`, `WAREHOUSE`, `PRODUCTION`, `LAND`, `OTHER`
- `dealType` - тип сделки: `SALE`, `RENT`
- `city` - город (опционально)
- `minPrice` - минимальная цена (опционально)
- `maxPrice` - максимальная цена (опционально)
- `minArea` - минимальная площадь (опционально)
- `maxArea` - максимальная площадь (опционально)
- `format` - формат: `json`, `csv`, `xml`

**Примеры:**
```bash
# Офисы в аренду
curl -H "User-Agent: ChatGPT-User" \
  "https://xbaza.by/api/ai/property?propertyType=OFFICE&dealType=RENT&limit=20"

# Торговые площади на продажу в Минске
curl -H "User-Agent: Claude-Web" \
  "https://xbaza.by/api/ai/property?propertyType=RETAIL&dealType=SALE&city=Минск"

# XML формат с фильтрами
curl -H "User-Agent: PerplexityBot" \
  "https://xbaza.by/api/ai/property?minPrice=50000&maxPrice=500000&minArea=50&maxArea=200&format=xml"
```

**Ответ:**
```json
{
  "success": true,
  "data": [
    {
      "id": 1,
      "title": "Офисное помещение 100 м² в центре Минска",
      "description": "Современный офис с ремонтом...",
      "property_type": "OFFICE",
      "deal_type": "RENT",
      "price": 2000,
      "area": 100,
      "rental_revenue": null,
      "utilities_cost": 500,
      "payback_period": null,
      "is_rented": false,
      "city": {
        "name_ru": "Минск"
      },
      "country": "BY",
      "created_at": "2025-12-31T00:00:00Z"
    }
  ],
  "meta": {
    "count": 20,
    "country": "BY",
    "currency": "BYN"
  }
}
```

### 13. GET /api/ai/analytics

Аналитика рынка.

**Параметры:**
- `type` - тип аналитики: `overview`, `bots`, `daily`, `pages`, `types`, `geographic`, `quality`, `all`
- `days` - количество дней (по умолчанию 30)
- `limit` - количество (по умолчанию 20)

**Примеры:**
```bash
# Обзор
curl -H "User-Agent: ChatGPT-User" \
  "https://xbaza.by/api/ai/analytics?type=overview"

# Статистика ботов за 7 дней
curl -H "User-Agent: Claude-Web" \
  "https://xbaza.by/api/ai/analytics?type=bots&days=7"

# Вся аналитика
curl -H "User-Agent: PerplexityBot" \
  "https://xbaza.by/api/ai/analytics?type=all"
```

### 14. GET /api/ai/categories

Получить все доступные категории вакансий.

**Пример:**
```bash
curl -H "User-Agent: ChatGPT-User" \
  "https://xbaza.by/api/ai/categories"
```

### 15. GET /api/ai/cities

Получить все города Беларуси с координатами.

**Пример:**
```bash
curl -H "User-Agent: ChatGPT-User" \
  "https://xbaza.by/api/ai/cities"
```

## Обработка ошибок

### Коды ошибок:

- **400** - Неверные параметры запроса
- **403** - Доступ запрещен (не AI бот)
- **429** - Превышен rate limit
- **500** - Внутренняя ошибка сервера

### Формат ошибки:
```json
{
  "success": false,
  "error": "Rate limit exceeded",
  "message": "Too many requests. Please try again later.",
  "retryAfter": 900
}
```

## Метаданные ответа

Каждый успешный ответ содержит метаданные:

```json
{
  "meta": {
    "count": 20,
    "country": "BY",
    "currency": "BYN",
    "language": "ru",
    "timezone": "Europe/Minsk",
    "aiOptimized": true,
    "rateLimit": {
      "remaining": 49,
      "limit": 50,
      "resetTime": 1735689600
    }
  }
}
```

## Best Practices

1. **Всегда используйте правильный User-Agent** для AI ботов
2. **Следите за rate limits** через заголовки ответа
3. **Используйте параметр `limit`** для контроля объема данных
4. **Кэшируйте статические данные** (категории, города)
5. **Обрабатывайте ошибки** и retry логику
6. **Используйте формат JSON** для лучшей производительности

## Дополнительные ресурсы

- **API Schema:** https://xbaza.by/api/ai.json
- **Discovery:** https://xbaza.by/api/ai/discovery
- **AI-Friendly Page:** https://xbaza.by/ai-friendly
- **Sandbox:** https://xbaza.by/ai-sandbox

---

## English Version

# Xbaza AI API - Complete Documentation

## Overview

Xbaza AI API provides structured access to data about the Belarusian job market, business, and commercial real estate. The API is optimized specifically for AI bots and assistants.

**Base URL:** `https://xbaza.by/api/ai`

## Authentication

The API uses **User-Agent based authentication**. Access is automatically granted to AI bots with the correct User-Agent.

### Supported AI Bots:
- `ChatGPT-User`
- `GPTBot`
- `Claude-Web`
- `anthropic-ai`
- `PerplexityBot`
- `Google-Extended`
- `CCBot`
- `YouBot`
- `OpenAI`
- `Anthropic`
- `Googlebot`
- `Bingbot`

### Example Header:
```http
User-Agent: ChatGPT-User
```

## Rate Limits

| Endpoint | Method | Limit |
|----------|--------|-------|
| `/api/ai/discovery` | GET | 200 / 15 min |
| `/api/ai/simple` | GET | 100 / 15 min |
| `/api/ai/belarus` | GET | 200 / 15 min |
| `/api/ai/jobs` | GET | 50 / 15 min |
| `/api/ai/jobs` | POST | 20 / 15 min |
| `/api/ai/services` | GET | 50 / 15 min |
| `/api/ai/services` | POST | 20 / 15 min |
| `/api/ai/users` | GET | 100 / 15 min |
| `/api/ai/business` | GET | 100 / 15 min |
| `/api/ai/property` | GET | 100 / 15 min |
| `/api/ai/analytics` | GET | 100 / 15 min |
| `/api/ai/categories` | GET | 100 / 15 min |
| `/api/ai/cities` | GET | 100 / 15 min |

## Response Formats

The API supports three formats:
- **JSON** (default) - `application/json`
- **CSV** - `text/csv`
- **XML** - `application/xml`

Specify format via `format` parameter:
```
?format=json
?format=csv
?format=xml
```

## Endpoints

### 1. GET /api/ai
Basic API information and list of available endpoints.

### 2. GET /api/ai.json
Complete API documentation in JSON format (machine-readable schema).

### 3. GET /api/ai/discovery
Discover all available endpoints and their capabilities.

### 4. GET /api/ai/simple
Simplified data access (jobs, companies, services).

**Parameters:**
- `type` - data type: `jobs`, `companies`, `all`
- `format` - format: `json`, `csv`, `xml`
- `limit` - count (1-100)
- `category` - category filter (optional)
- `city` - city filter (optional)

### 5. GET /api/ai/belarus
Comprehensive Belarus job market data.

**Parameters:**
- `type` - data type: `overview`, `jobs`, `companies`, `services`, `trends`, `salary`, `cities`, `industries`

### 6. GET /api/ai/jobs
Get list of job listings.

**Parameters:**
- `limit` - count (1-50)
- `category` - category (optional)
- `city` - city (optional)

### 7. POST /api/ai/jobs
Create job listing (AI bots only).

**Request Body:**
```json
{
  "title": "Frontend Developer",
  "description": "React/Next.js developer position",
  "salary_min": 1000,
  "salary_max": 2000,
  "company_name": "Tech Company",
  "city_name": "Минск",
  "category_name": "IT"
}
```

### 8. GET /api/ai/services
Get list of business services.

### 9. POST /api/ai/services
Create service (AI bots only).

### 10. GET /api/ai/users
Search users by name, surname, or ID.

**Parameters:**
- `q` - search query (minimum 2 characters)
- `limit` - count (1-50)
- `format` - format: `json`, `csv`, `xml`

### 11. GET /api/ai/business
Get list of business for sale listings.

**Parameters:**
- `limit` - count (1-100)
- `category` - category (optional)
- `city` - city (optional)
- `minPrice` - minimum price (optional)
- `maxPrice` - maximum price (optional)
- `format` - format: `json`, `csv`, `xml`

### 12. GET /api/ai/property
Get list of commercial real estate.

**Parameters:**
- `limit` - count (1-100)
- `propertyType` - type: `OFFICE`, `RETAIL`, `WAREHOUSE`, `PRODUCTION`, `LAND`, `OTHER`
- `dealType` - deal type: `SALE`, `RENT`
- `city` - city (optional)
- `minPrice` - minimum price (optional)
- `maxPrice` - maximum price (optional)
- `minArea` - minimum area (optional)
- `maxArea` - maximum area (optional)
- `format` - format: `json`, `csv`, `xml`

### 13. GET /api/ai/analytics
Market analytics.

**Parameters:**
- `type` - analytics type: `overview`, `bots`, `daily`, `pages`, `types`, `geographic`, `quality`, `all`
- `days` - number of days (default 30)
- `limit` - count (default 20)

### 14. GET /api/ai/categories
Get all available job categories.

### 15. GET /api/ai/cities
Get all Belarus cities with coordinates.

## Error Handling

### Error Codes:

- **400** - Invalid request parameters
- **403** - Access denied (not AI bot)
- **429** - Rate limit exceeded
- **500** - Internal server error

### Error Format:
```json
{
  "success": false,
  "error": "Rate limit exceeded",
  "message": "Too many requests. Please try again later.",
  "retryAfter": 900
}
```

## Response Metadata

Each successful response contains metadata:

```json
{
  "meta": {
    "count": 20,
    "country": "BY",
    "currency": "BYN",
    "language": "ru",
    "timezone": "Europe/Minsk",
    "aiOptimized": true,
    "rateLimit": {
      "remaining": 49,
      "limit": 50,
      "resetTime": 1735689600
    }
  }
}
```

## Best Practices

1. **Always use the correct User-Agent** for AI bots
2. **Monitor rate limits** through response headers
3. **Use the `limit` parameter** to control data volume
4. **Cache static data** (categories, cities)
5. **Handle errors** and retry logic
6. **Use JSON format** for better performance

## Additional Resources

- **API Schema:** https://xbaza.by/api/ai.json
- **Discovery:** https://xbaza.by/api/ai/discovery
- **AI-Friendly Page:** https://xbaza.by/ai-friendly
- **Sandbox:** https://xbaza.by/ai-sandbox

