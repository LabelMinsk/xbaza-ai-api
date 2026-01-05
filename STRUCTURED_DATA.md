# Xbaza Structured Data - Структурированные данные для парсинга

## Обзор

Этот документ описывает структурированные данные Xbaza API для легкого парсинга AI ботами.

## Формат данных

Все данные возвращаются в стандартизированном формате:

```json
{
  "success": true,
  "data": [...],
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

## Схемы данных

### 1. Вакансия (Job)

```json
{
  "id": 1,
  "title": "Frontend Developer",
  "description": "Разработка веб-приложений на React/Next.js...",
  "salary_min": 1000,
  "salary_max": 2000,
  "salary_currency": "BYN",
  "employment_type": "FULL_TIME",
  "is_remote": false,
  "company": {
    "id": 1,
    "name": "Tech Company"
  },
  "city": {
    "id": 1,
    "name_ru": "Минск"
  },
  "category": {
    "id": 1,
    "category": "IT"
  },
  "created_at": "2025-12-31T00:00:00Z"
}
```

**Поля:**
- `id` - Уникальный идентификатор
- `title` - Название вакансии
- `description` - Описание
- `salary_min` - Минимальная зарплата (опционально)
- `salary_max` - Максимальная зарплата (опционально)
- `salary_currency` - Валюта (обычно "BYN")
- `employment_type` - Тип занятости (FULL_TIME, PART_TIME, CONTRACT, etc.)
- `is_remote` - Удаленная работа (boolean)
- `company` - Объект компании
- `city` - Объект города
- `category` - Объект категории
- `created_at` - Дата создания (ISO 8601)

### 2. Пользователь (User)

```json
{
  "id": 1,
  "firstName": "Иван",
  "lastName": "Петров",
  "headline": "Senior Frontend Developer",
  "profilePicture": "https://xbaza.by/uploads/users/1.jpg",
  "location": {
    "city": "Минск",
    "country": "BY"
  },
  "searchType": "JOB_SEEKER"
}
```

**Поля:**
- `id` - Уникальный идентификатор
- `firstName` - Имя
- `lastName` - Фамилия
- `headline` - Заголовок профиля (опционально)
- `profilePicture` - URL фото профиля (опционально)
- `location` - Объект местоположения
- `searchType` - Тип поиска (JOB_SEEKER, EMPLOYER)

### 3. Бизнес-листинг (Business Listing)

```json
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
  "images": [
    "https://xbaza.by/uploads/business/1/1.jpg"
  ],
  "category": {
    "id": 1,
    "name": "Общественное питание"
  },
  "city": {
    "id": 1,
    "name_ru": "Минск"
  },
  "country": "BY",
  "created_at": "2025-12-31T00:00:00Z"
}
```

**Поля:**
- `id` - Уникальный идентификатор
- `title` - Название объявления
- `description` - Описание
- `price` - Цена продажи (BYN)
- `area` - Площадь (м²)
- `profit` - Прибыль в месяц (BYN, опционально)
- `payback_period` - Срок окупаемости (месяцев, опционально)
- `staff_count` - Количество сотрудников
- `business_age` - Возраст бизнеса (лет)
- `sale_reason` - Причина продажи
- `legal_form` - Организационно-правовая форма
- `tax_form` - Форма налогообложения
- `ownership_type` - Форма собственности
- `images` - Массив URL изображений
- `category` - Объект категории
- `city` - Объект города
- `country` - Код страны ("BY")
- `created_at` - Дата создания (ISO 8601)

### 4. Коммерческая недвижимость (Property)

```json
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
  "images": [
    "https://xbaza.by/uploads/property/1/1.jpg"
  ],
  "city": {
    "id": 1,
    "name_ru": "Минск"
  },
  "country": "BY",
  "created_at": "2025-12-31T00:00:00Z"
}
```

**Поля:**
- `id` - Уникальный идентификатор
- `title` - Название объявления
- `description` - Описание
- `property_type` - Тип недвижимости:
  - `OFFICE` - Офис
  - `RETAIL` - Торговая площадь
  - `WAREHOUSE` - Склад
  - `PRODUCTION` - Производственное помещение
  - `LAND` - Земельный участок
  - `OTHER` - Другое
- `deal_type` - Тип сделки:
  - `SALE` - Продажа
  - `RENT` - Аренда
- `price` - Цена (BYN)
  - Для продажи: общая стоимость
  - Для аренды: стоимость в месяц
- `area` - Площадь (м²)
- `rental_revenue` - Доходность в месяц (BYN, опционально)
- `utilities_cost` - Коммунальные расходы (BYN, опционально)
- `payback_period` - Срок окупаемости (лет, опционально)
- `is_rented` - Сдано в аренду (boolean, для аренды)
- `images` - Массив URL изображений
- `city` - Объект города
- `country` - Код страны ("BY")
- `created_at` - Дата создания (ISO 8601)

### 5. Бизнес-услуга (Service)

```json
{
  "id": 1,
  "name": "Web Development",
  "description": "Разработка веб-приложений на заказ...",
  "price": 500,
  "contacts": "email@example.com",
  "created_at": "2025-12-31T00:00:00Z",
  "expiration_date": "2026-12-31T00:00:00Z",
  "company": {
    "id": 1,
    "name": "Web Studio"
  },
  "city": {
    "id": 1,
    "name_ru": "Минск"
  },
  "category": {
    "id": 1,
    "name": "IT"
  }
}
```

**Поля:**
- `id` - Уникальный идентификатор
- `name` - Название услуги
- `description` - Описание
- `price` - Цена (BYN, опционально)
- `contacts` - Контакты
- `created_at` - Дата создания (ISO 8601)
- `expiration_date` - Дата окончания действия (ISO 8601, опционально)
- `company` - Объект компании
- `city` - Объект города
- `category` - Объект категории

### 6. Компания (Company)

```json
{
  "id": 1,
  "name": "Tech Company",
  "description": "Разработка программного обеспечения...",
  "logo": "https://xbaza.by/uploads/companies/1/logo.jpg",
  "city": {
    "id": 1,
    "name_ru": "Минск"
  },
  "created_at": "2025-12-31T00:00:00Z"
}
```

**Поля:**
- `id` - Уникальный идентификатор
- `name` - Название компании
- `description` - Описание (опционально)
- `logo` - URL логотипа (опционально)
- `city` - Объект города
- `created_at` - Дата создания (ISO 8601)

## Общие объекты

### Город (City)

```json
{
  "id": 1,
  "name_ru": "Минск",
  "name_en": "Minsk",
  "latitude": 53.9045,
  "longitude": 27.5615
}
```

### Категория (Category)

```json
{
  "id": 1,
  "category": "IT",
  "name": "Информационные технологии"
}
```

## Метаданные ответа

Каждый ответ содержит метаданные:

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

**Поля метаданных:**
- `count` - Количество элементов в ответе
- `country` - Код страны ("BY")
- `currency` - Валюта ("BYN")
- `language` - Язык ("ru")
- `timezone` - Часовой пояс ("Europe/Minsk")
- `aiOptimized` - Оптимизировано для AI (boolean)
- `rateLimit` - Информация о rate limit:
  - `remaining` - Оставшееся количество запросов
  - `limit` - Лимит запросов
  - `resetTime` - Время сброса лимита (Unix timestamp)

## Форматы экспорта

### JSON (по умолчанию)

```bash
GET /api/ai/jobs?limit=20&format=json
```

Стандартный JSON формат с вложенными объектами.

### CSV

```bash
GET /api/ai/jobs?limit=20&format=csv
```

Плоская структура CSV для анализа в таблицах.

**Пример CSV:**
```csv
id,title,company,city,salary_min,salary_max,currency
1,Frontend Developer,Tech Company,Минск,1000,2000,BYN
2,Backend Developer,IT Studio,Минск,1200,2500,BYN
```

### XML

```bash
GET /api/ai/jobs?limit=20&format=xml
```

Структурированный XML формат.

**Пример XML:**
```xml
<?xml version="1.0" encoding="UTF-8"?>
<belarus-jobs>
  <item id="1">
    <id>1</id>
    <title>Frontend Developer</title>
    <company>Tech Company</company>
    <city>Минск</city>
    <salary_min>1000</salary_min>
    <salary_max>2000</salary_max>
    <currency>BYN</currency>
  </item>
</belarus-jobs>
```

## Парсинг данных

### Python пример

```python
import requests
import json

# Получить вакансии
response = requests.get(
    'https://xbaza.by/api/ai/jobs?limit=20',
    headers={'User-Agent': 'ChatGPT-User'}
)
data = response.json()

# Парсинг
if data['success']:
    jobs = data['data']
    meta = data['meta']
    
    print(f"Найдено вакансий: {meta['count']}")
    print(f"Страна: {meta['country']}")
    print(f"Валюта: {meta['currency']}")
    
    for job in jobs:
        print(f"\nВакансия: {job['title']}")
        print(f"Компания: {job['company']['name']}")
        print(f"Город: {job['city']['name_ru']}")
        if job.get('salary_min'):
            print(f"Зарплата: {job['salary_min']}-{job['salary_max']} {job['salary_currency']}")
```

### JavaScript пример

```javascript
// Получить вакансии
const response = await fetch('https://xbaza.by/api/ai/jobs?limit=20', {
  headers: {
    'User-Agent': 'ChatGPT-User'
  }
});
const data = await response.json();

// Парсинг
if (data.success) {
  const jobs = data.data;
  const meta = data.meta;
  
  console.log(`Найдено вакансий: ${meta.count}`);
  console.log(`Страна: ${meta.country}`);
  console.log(`Валюта: ${meta.currency}`);
  
  jobs.forEach(job => {
    console.log(`\nВакансия: ${job.title}`);
    console.log(`Компания: ${job.company.name}`);
    console.log(`Город: ${job.city.name_ru}`);
    if (job.salary_min) {
      console.log(`Зарплата: ${job.salary_min}-${job.salary_max} ${job.salary_currency}`);
    }
  });
}
```

## Валидация данных

Все данные проходят валидацию:
- ✅ Обязательные поля присутствуют
- ✅ Типы данных корректны
- ✅ Форматы дат валидны (ISO 8601)
- ✅ Числовые значения в допустимых диапазонах
- ✅ Строки не пустые и не превышают лимиты

## Обработка ошибок

При ошибке структура ответа:

```json
{
  "success": false,
  "error": "Rate limit exceeded",
  "message": "Too many requests. Please try again later.",
  "retryAfter": 900
}
```

**Коды ошибок:**
- `400` - Неверные параметры запроса
- `403` - Доступ запрещен (не AI бот)
- `429` - Превышен rate limit
- `500` - Внутренняя ошибка сервера

## Best Practices для парсинга

1. **Всегда проверяйте `success`** в ответе
2. **Используйте метаданные** для понимания контекста
3. **Обрабатывайте опциональные поля** (могут отсутствовать)
4. **Проверяйте типы данных** перед использованием
5. **Используйте формат JSON** для лучшей производительности
6. **Кэшируйте статические данные** (категории, города)

## Заключение

Xbaza API предоставляет структурированные, валидированные данные в стандартизированном формате, что делает парсинг простым и надежным для AI ботов.

---

## English Version

# Xbaza Structured Data - Structured Data for Parsing

## Overview

This document describes structured data from Xbaza API for easy parsing by AI bots.

## Data Format

All data is returned in a standardized format:

```json
{
  "success": true,
  "data": [...],
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

## Data Schemas

### 1. Job

**Fields:**
- `id` - Unique identifier
- `title` - Job title
- `description` - Description
- `salary_min` - Minimum salary (optional)
- `salary_max` - Maximum salary (optional)
- `salary_currency` - Currency (usually "BYN")
- `employment_type` - Employment type (FULL_TIME, PART_TIME, CONTRACT, etc.)
- `is_remote` - Remote work (boolean)
- `company` - Company object
- `city` - City object
- `category` - Category object
- `created_at` - Creation date (ISO 8601)

### 2. User

**Fields:**
- `id` - Unique identifier
- `firstName` - First name
- `lastName` - Last name
- `headline` - Profile headline (optional)
- `profilePicture` - Profile photo URL (optional)
- `location` - Location object
- `searchType` - Search type (JOB_SEEKER, EMPLOYER)

### 3. Business Listing

**Fields:**
- `id` - Unique identifier
- `title` - Listing title
- `description` - Description
- `price` - Sale price (BYN)
- `area` - Area (m²)
- `profit` - Monthly profit (BYN, optional)
- `payback_period` - Payback period (months, optional)
- `staff_count` - Staff count
- `business_age` - Business age (years)
- `sale_reason` - Sale reason
- `legal_form` - Legal form
- `tax_form` - Tax form
- `ownership_type` - Ownership type
- `images` - Array of image URLs
- `category` - Category object
- `city` - City object
- `country` - Country code ("BY")
- `created_at` - Creation date (ISO 8601)

### 4. Property

**Fields:**
- `id` - Unique identifier
- `title` - Listing title
- `description` - Description
- `property_type` - Property type (OFFICE, RETAIL, WAREHOUSE, PRODUCTION, LAND, OTHER)
- `deal_type` - Deal type (SALE, RENT)
- `price` - Price (BYN)
- `area` - Area (m²)
- `rental_revenue` - Monthly revenue (BYN, optional)
- `utilities_cost` - Utilities cost (BYN, optional)
- `payback_period` - Payback period (years, optional)
- `is_rented` - Rented (boolean, for rent)
- `images` - Array of image URLs
- `city` - City object
- `country` - Country code ("BY")
- `created_at` - Creation date (ISO 8601)

### 5. Service

**Fields:**
- `id` - Unique identifier
- `name` - Service name
- `description` - Description
- `price` - Price (BYN, optional)
- `contacts` - Contacts
- `created_at` - Creation date (ISO 8601)
- `expiration_date` - Expiration date (ISO 8601, optional)
- `company` - Company object
- `city` - City object
- `category` - Category object

### 6. Company

**Fields:**
- `id` - Unique identifier
- `name` - Company name
- `description` - Description (optional)
- `logo` - Logo URL (optional)
- `city` - City object
- `created_at` - Creation date (ISO 8601)

## Common Objects

### City

```json
{
  "id": 1,
  "name_ru": "Минск",
  "name_en": "Minsk",
  "latitude": 53.9045,
  "longitude": 27.5615
}
```

### Category

```json
{
  "id": 1,
  "category": "IT",
  "name": "Информационные технологии"
}
```

## Response Metadata

Each response contains metadata:

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

## Export Formats

### JSON (default)

Standard JSON format with nested objects.

### CSV

Flat CSV structure for table analysis.

### XML

Structured XML format.

## Data Parsing

### Python Example

```python
import requests
import json

# Get jobs
response = requests.get(
    'https://xbaza.by/api/ai/jobs?limit=20',
    headers={'User-Agent': 'ChatGPT-User'}
)
data = response.json()

# Parsing
if data['success']:
    jobs = data['data']
    meta = data['meta']
    
    print(f"Found jobs: {meta['count']}")
    print(f"Country: {meta['country']}")
    print(f"Currency: {meta['currency']}")
    
    for job in jobs:
        print(f"\nJob: {job['title']}")
        print(f"Company: {job['company']['name']}")
        print(f"City: {job['city']['name_ru']}")
        if job.get('salary_min'):
            print(f"Salary: {job['salary_min']}-{job['salary_max']} {job['salary_currency']}")
```

### JavaScript Example

```javascript
// Get jobs
const response = await fetch('https://xbaza.by/api/ai/jobs?limit=20', {
  headers: {
    'User-Agent': 'ChatGPT-User'
  }
});
const data = await response.json();

// Parsing
if (data.success) {
  const jobs = data.data;
  const meta = data.meta;
  
  console.log(`Found jobs: ${meta.count}`);
  console.log(`Country: ${meta.country}`);
  console.log(`Currency: ${meta.currency}`);
  
  jobs.forEach(job => {
    console.log(`\nJob: ${job.title}`);
    console.log(`Company: ${job.company.name}`);
    console.log(`City: ${job.city.name_ru}`);
    if (job.salary_min) {
      console.log(`Salary: ${job.salary_min}-${job.salary_max} ${job.salary_currency}`);
    }
  });
}
```

## Data Validation

All data is validated:
- ✅ Required fields are present
- ✅ Data types are correct
- ✅ Date formats are valid (ISO 8601)
- ✅ Numeric values are in valid ranges
- ✅ Strings are not empty and don't exceed limits

## Error Handling

On error, response structure:

```json
{
  "success": false,
  "error": "Rate limit exceeded",
  "message": "Too many requests. Please try again later.",
  "retryAfter": 900
}
```

**Error Codes:**
- `400` - Invalid request parameters
- `403` - Access denied (not AI bot)
- `429` - Rate limit exceeded
- `500` - Internal server error

## Best Practices for Parsing

1. **Always check `success`** in response
2. **Use metadata** to understand context
3. **Handle optional fields** (may be absent)
4. **Check data types** before use
5. **Use JSON format** for better performance
6. **Cache static data** (categories, cities)

## Conclusion

Xbaza API provides structured, validated data in a standardized format, making parsing simple and reliable for AI bots.

