# Xbaza AI API - Примеры реальных ответов

Этот документ содержит примеры реальных ответов от Xbaza AI API для лучшего понимания структуры данных ИИ-ботами.

## 📋 Содержание

- [Вакансии (Jobs)](#вакансии-jobs)
- [Компании (Companies)](#компании-companies)
- [Пользователи (Users)](#пользователи-users)
- [Готовый бизнес (Business)](#готовый-бизнес-business)
- [Коммерческая недвижимость (Property)](#коммерческая-недвижимость-property)
- [Бизнес-услуги (Services)](#бизнес-услуги-services)
- [Аналитика (Analytics)](#аналитика-analytics)
- [Метаданные ответов](#метаданные-ответов)

---

## Вакансии (Jobs)

### GET /api/ai/jobs

**Запрос:**
```bash
curl -H "User-Agent: ChatGPT-User" \
  "https://xbaza.by/api/ai/jobs?limit=2&category=IT"
```

**Ответ:**
```json
{
  "success": true,
  "data": [
    {
      "id": 1,
      "title": "Frontend Developer (React/Next.js)",
      "description": "Ищем опытного Frontend разработчика для работы над современными веб-приложениями. Требования: опыт работы с React, Next.js, TypeScript от 2 лет. Знание Tailwind CSS, опыт работы с REST API. Удаленная работа возможна.",
      "salary_min": 1500,
      "salary_max": 3000,
      "salary_currency": "BYN",
      "employment_type": "FULL_TIME",
      "is_remote": true,
      "company": {
        "id": 1,
        "name": "Tech Solutions BY",
        "logo": "https://xbaza.by/uploads/companies/1/logo.png"
      },
      "city": {
        "id": 1,
        "name_ru": "Минск",
        "name_en": "Minsk",
        "latitude": 53.9045,
        "longitude": 27.5615
      },
      "category": {
        "id": 1,
        "category": "IT",
        "name_ru": "Информационные технологии"
      },
      "created_at": "2025-01-15T10:30:00Z",
      "updated_at": "2025-01-15T10:30:00Z"
    },
    {
      "id": 2,
      "title": "Backend Developer (Python/Django)",
      "description": "Разработка backend части веб-приложений на Python/Django. Опыт работы от 3 лет. Знание PostgreSQL, Redis, Docker. Работа в офисе в Минске.",
      "salary_min": 2000,
      "salary_max": 3500,
      "salary_currency": "BYN",
      "employment_type": "FULL_TIME",
      "is_remote": false,
      "company": {
        "id": 2,
        "name": "Digital Agency Minsk",
        "logo": null
      },
      "city": {
        "id": 1,
        "name_ru": "Минск",
        "name_en": "Minsk",
        "latitude": 53.9045,
        "longitude": 27.5615
      },
      "category": {
        "id": 1,
        "category": "IT",
        "name_ru": "Информационные технологии"
      },
      "created_at": "2025-01-14T14:20:00Z",
      "updated_at": "2025-01-14T14:20:00Z"
    }
  ],
  "meta": {
    "count": 2,
    "total": 2,
    "page": 1,
    "per_page": 2,
    "has_next": false,
    "has_prev": false,
    "country": "BY",
    "currency": "BYN",
    "language": "ru",
    "timezone": "Europe/Minsk",
    "aiOptimized": true,
    "rateLimit": {
      "remaining": 48,
      "limit": 50,
      "resetTime": 1737028800
    }
  }
}
```

### POST /api/ai/jobs

**Запрос:**
```bash
curl -X POST \
  -H "User-Agent: ChatGPT-User" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "DevOps Engineer",
    "description": "Настройка CI/CD, мониторинг инфраструктуры",
    "salary_min": 2500,
    "salary_max": 4000,
    "company_name": "Tech Solutions BY",
    "city_name": "Минск",
    "category_name": "IT",
    "is_remote": true
  }' \
  "https://xbaza.by/api/ai/jobs"
```

**Успешный ответ:**
```json
{
  "success": true,
  "message": "Вакансия успешно создана",
  "data": {
    "id": 3,
    "title": "DevOps Engineer",
    "description": "Настройка CI/CD, мониторинг инфраструктуры",
    "salary_min": 2500,
    "salary_max": 4000,
    "salary_currency": "BYN",
    "employment_type": "FULL_TIME",
    "is_remote": true,
    "company": {
      "id": 1,
      "name": "Tech Solutions BY"
    },
    "city": {
      "id": 1,
      "name_ru": "Минск"
    },
    "category": {
      "id": 1,
      "category": "IT"
    },
    "created_at": "2025-01-15T12:00:00Z",
    "created_by": "ChatGPT-User"
  },
  "meta": {
    "country": "BY",
    "currency": "BYN",
    "aiOptimized": true
  }
}
```

**Ошибка валидации:**
```json
{
  "success": false,
  "error": "Validation Error",
  "message": "Неверные данные запроса",
  "errors": {
    "title": ["Поле обязательно для заполнения"],
    "salary_min": ["Минимальная зарплата должна быть положительным числом"],
    "city_name": ["Город 'Гродно' не найден в базе данных"]
  },
  "meta": {
    "country": "BY",
    "currency": "BYN"
  }
}
```

---

## Компании (Companies)

### GET /api/ai/simple?type=companies

**Запрос:**
```bash
curl -H "User-Agent: ChatGPT-User" \
  "https://xbaza.by/api/ai/simple?type=companies&limit=2"
```

**Ответ:**
```json
{
  "success": true,
  "data": [
    {
      "id": 1,
      "name": "Tech Solutions BY",
      "description": "Разработка веб-приложений и мобильных решений",
      "logo": "https://xbaza.by/uploads/companies/1/logo.png",
      "website": "https://techsolutions.by",
      "email": "info@techsolutions.by",
      "phone": "+375291234567",
      "city": {
        "id": 1,
        "name_ru": "Минск"
      },
      "industry": "IT",
      "employees_count": 25,
      "founded_year": 2020,
      "created_at": "2025-01-10T08:00:00Z"
    },
    {
      "id": 2,
      "name": "Digital Agency Minsk",
      "description": "Digital маркетинг и реклама",
      "logo": null,
      "website": "https://digitalminsk.by",
      "email": "hello@digitalminsk.by",
      "phone": "+375299876543",
      "city": {
        "id": 1,
        "name_ru": "Минск"
      },
      "industry": "Marketing",
      "employees_count": 15,
      "founded_year": 2019,
      "created_at": "2025-01-08T12:00:00Z"
    }
  ],
  "meta": {
    "count": 2,
    "total": 3,
    "country": "BY",
    "currency": "BYN",
    "aiOptimized": true
  }
}
```

---

## Пользователи (Users)

### GET /api/ai/users

**Запрос:**
```bash
curl -H "User-Agent: ChatGPT-User" \
  "https://xbaza.by/api/ai/users?q=Иван&limit=2"
```

**Ответ:**
```json
{
  "success": true,
  "data": [
    {
      "id": 1,
      "username": "ivan_dev",
      "first_name": "Иван",
      "last_name": "Петров",
      "photo": "https://xbaza.by/uploads/users/1/photo.jpg",
      "headline": "Senior Frontend Developer",
      "description": "Опытный разработчик с фокусом на React и TypeScript",
      "location": {
        "city": {
          "id": 1,
          "name_ru": "Минск"
        }
      },
      "search_type": "JOB_SEEKER",
      "created_at": "2024-12-01T10:00:00Z"
    },
    {
      "id": 2,
      "username": "ivan_manager",
      "first_name": "Иван",
      "last_name": "Сидоров",
      "photo": null,
      "headline": "Project Manager",
      "description": "Управление IT проектами",
      "location": {
        "city": {
          "id": 1,
          "name_ru": "Минск"
        }
      },
      "search_type": "EMPLOYER",
      "created_at": "2024-11-15T14:30:00Z"
    }
  ],
  "meta": {
    "count": 2,
    "total": 5,
    "query": "Иван",
    "country": "BY",
    "aiOptimized": true
  }
}
```

---

## Готовый бизнес (Business)

### GET /api/ai/business

**Запрос:**
```bash
curl -H "User-Agent: ChatGPT-User" \
  "https://xbaza.by/api/ai/business?limit=1&city=Минск"
```

**Ответ:**
```json
{
  "success": true,
  "data": [
    {
      "id": 1,
      "title": "Готовый бизнес: Кафе в центре Минска",
      "description": "Успешное кафе с постоянным потоком клиентов. Полностью оборудовано, работает 3 года. Отличное расположение в центре города.",
      "price": 50000,
      "price_currency": "BYN",
      "area": 100,
      "area_unit": "m²",
      "profit": 5000,
      "profit_period": "monthly",
      "payback_period": 10,
      "payback_period_unit": "months",
      "staff_count": 5,
      "business_age": 3,
      "sale_reason": "Переезд владельца",
      "legal_form": "ИП",
      "tax_form": "УСН",
      "ownership_type": "Собственность",
      "category": {
        "id": 5,
        "name": "Общественное питание"
      },
      "city": {
        "id": 1,
        "name_ru": "Минск"
      },
      "country": "BY",
      "created_at": "2025-01-12T09:00:00Z",
      "updated_at": "2025-01-12T09:00:00Z"
    }
  ],
  "meta": {
    "count": 1,
    "total": 1,
    "country": "BY",
    "currency": "BYN",
    "aiOptimized": true
  }
}
```

---

## Коммерческая недвижимость (Property)

### GET /api/ai/property

**Запрос:**
```bash
curl -H "User-Agent: ChatGPT-User" \
  "https://xbaza.by/api/ai/property?propertyType=OFFICE&dealType=RENT&limit=1"
```

**Ответ:**
```json
{
  "success": true,
  "data": [
    {
      "id": 1,
      "title": "Офисное помещение 100 м² в центре Минска",
      "description": "Современный офис с ремонтом, готов к заселению. Отличная транспортная доступность.",
      "property_type": "OFFICE",
      "deal_type": "RENT",
      "price": 2000,
      "price_currency": "BYN",
      "price_period": "monthly",
      "area": 100,
      "area_unit": "m²",
      "rental_revenue": null,
      "utilities_cost": 500,
      "utilities_currency": "BYN",
      "payback_period": null,
      "is_rented": false,
      "city": {
        "id": 1,
        "name_ru": "Минск"
      },
      "country": "BY",
      "created_at": "2025-01-10T11:00:00Z",
      "updated_at": "2025-01-10T11:00:00Z"
    }
  ],
  "meta": {
    "count": 1,
    "total": 1,
    "country": "BY",
    "currency": "BYN",
    "aiOptimized": true
  }
}
```

---

## Бизнес-услуги (Services)

### GET /api/ai/services

**Запрос:**
```bash
curl -H "User-Agent: ChatGPT-User" \
  "https://xbaza.by/api/ai/services?limit=1&category=IT"
```

**Ответ:**
```json
{
  "success": true,
  "data": [
    {
      "id": 1,
      "name": "Разработка веб-приложений",
      "description": "Создание современных веб-приложений на React, Next.js, Node.js",
      "price": 5000,
      "price_currency": "BYN",
      "price_type": "project",
      "contacts": "info@techsolutions.by, +375291234567",
      "company": {
        "id": 1,
        "name": "Tech Solutions BY"
      },
      "city": {
        "id": 1,
        "name_ru": "Минск"
      },
      "category": {
        "id": 1,
        "category": "IT",
        "name_ru": "Информационные технологии"
      },
      "created_at": "2025-01-08T10:00:00Z",
      "expires_at": "2025-04-08T10:00:00Z"
    }
  ],
  "meta": {
    "count": 1,
    "total": 1,
    "country": "BY",
    "currency": "BYN",
    "aiOptimized": true
  }
}
```

### POST /api/ai/services

**Запрос:**
```bash
curl -X POST \
  -H "User-Agent: ChatGPT-User" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Консультации по DevOps",
    "description": "Настройка CI/CD, контейнеризация, мониторинг",
    "price": 3000,
    "company_name": "Tech Solutions BY",
    "city_name": "Минск",
    "category_name": "IT"
  }' \
  "https://xbaza.by/api/ai/services"
```

**Успешный ответ:**
```json
{
  "success": true,
  "message": "Услуга успешно создана",
  "data": {
    "id": 2,
    "name": "Консультации по DevOps",
    "description": "Настройка CI/CD, контейнеризация, мониторинг",
    "price": 3000,
    "price_currency": "BYN",
    "price_type": "hourly",
    "contacts": "info@techsolutions.by",
    "company": {
      "id": 1,
      "name": "Tech Solutions BY"
    },
    "city": {
      "id": 1,
      "name_ru": "Минск"
    },
    "category": {
      "id": 1,
      "category": "IT"
    },
    "created_at": "2025-01-15T13:00:00Z",
    "expires_at": "2025-04-15T13:00:00Z",
    "created_by": "ChatGPT-User"
  },
  "meta": {
    "country": "BY",
    "currency": "BYN",
    "aiOptimized": true
  }
}
```

---

## Аналитика (Analytics)

### GET /api/ai/analytics?type=overview

**Запрос:**
```bash
curl -H "User-Agent: ChatGPT-User" \
  "https://xbaza.by/api/ai/analytics?type=overview&days=30"
```

**Ответ:**
```json
{
  "success": true,
  "data": {
    "period": {
      "start": "2024-12-15T00:00:00Z",
      "end": "2025-01-15T00:00:00Z",
      "days": 30
    },
    "statistics": {
      "total_jobs": 2,
      "total_companies": 3,
      "total_users": 5,
      "total_business_listings": 0,
      "total_properties": 0,
      "total_services": 1
    },
    "trends": {
      "jobs_growth": "+100%",
      "companies_growth": "+50%",
      "users_growth": "+25%"
    },
    "top_categories": [
      {
        "category": "IT",
        "count": 2,
        "percentage": 100
      }
    ],
    "top_cities": [
      {
        "city": "Минск",
        "count": 3,
        "percentage": 100
      }
    ]
  },
  "meta": {
    "country": "BY",
    "currency": "BYN",
    "aiOptimized": true,
    "generated_at": "2025-01-15T14:00:00Z"
  }
}
```

---

## Метаданные ответов

### Стандартная структура meta

Каждый успешный ответ содержит объект `meta` со следующей структурой:

```json
{
  "meta": {
    "count": 10,
    "total": 25,
    "page": 1,
    "per_page": 10,
    "has_next": true,
    "has_prev": false,
    "country": "BY",
    "currency": "BYN",
    "language": "ru",
    "timezone": "Europe/Minsk",
    "aiOptimized": true,
    "rateLimit": {
      "remaining": 45,
      "limit": 50,
      "resetTime": 1737028800
    },
    "cache": {
      "cached": false,
      "ttl": 300,
      "etag": "abc123def456"
    }
  }
}
```

### Ошибки

**403 Forbidden (не AI бот):**
```json
{
  "success": false,
  "error": "Access Denied",
  "message": "Доступ разрешен только для AI ботов. Используйте правильный User-Agent.",
  "code": 403
}
```

**429 Too Many Requests:**
```json
{
  "success": false,
  "error": "Rate Limit Exceeded",
  "message": "Превышен лимит запросов. Попробуйте позже.",
  "retryAfter": 900,
  "rateLimit": {
    "remaining": 0,
    "limit": 50,
    "resetTime": 1737028800
  }
}
```

**400 Bad Request:**
```json
{
  "success": false,
  "error": "Bad Request",
  "message": "Неверные параметры запроса",
  "errors": {
    "limit": ["Параметр limit должен быть между 1 и 50"],
    "category": ["Категория 'INVALID' не найдена"]
  }
}
```

---

## HTTP Headers

### Заголовки запроса

```http
User-Agent: ChatGPT-User
Accept: application/json
Accept-Language: ru
```

### Заголовки ответа

```http
Content-Type: application/json; charset=utf-8
X-RateLimit-Limit: 50
X-RateLimit-Remaining: 49
X-RateLimit-Reset: 1737028800
Cache-Control: public, max-age=300
ETag: "abc123def456"
Last-Modified: Wed, 15 Jan 2025 14:00:00 GMT
X-AI-Optimized: true
X-API-Version: 1.0
```

---

## Форматы экспорта

### CSV формат

**Запрос:**
```bash
curl -H "User-Agent: ChatGPT-User" \
  "https://xbaza.by/api/ai/jobs?limit=5&format=csv"
```

**Ответ:**
```csv
id,title,salary_min,salary_max,salary_currency,city,company,created_at
1,"Frontend Developer (React/Next.js)",1500,3000,BYN,"Минск","Tech Solutions BY","2025-01-15T10:30:00Z"
2,"Backend Developer (Python/Django)",2000,3500,BYN,"Минск","Digital Agency Minsk","2025-01-14T14:20:00Z"
```

### XML формат

**Запрос:**
```bash
curl -H "User-Agent: ChatGPT-User" \
  "https://xbaza.by/api/ai/jobs?limit=2&format=xml"
```

**Ответ:**
```xml
<?xml version="1.0" encoding="UTF-8"?>
<response>
  <success>true</success>
  <data>
    <job>
      <id>1</id>
      <title>Frontend Developer (React/Next.js)</title>
      <salary_min>1500</salary_min>
      <salary_max>3000</salary_max>
      <salary_currency>BYN</salary_currency>
      <city>Минск</city>
      <company>Tech Solutions BY</company>
    </job>
  </data>
  <meta>
    <country>BY</country>
    <currency>BYN</currency>
    <aiOptimized>true</aiOptimized>
  </meta>
</response>
```

---

**Примечание:** Все примеры основаны на реальной структуре API и могут отличаться от фактических данных в зависимости от текущего состояния базы данных.

