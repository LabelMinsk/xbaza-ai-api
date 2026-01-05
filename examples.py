"""
Xbaza AI API - Python Examples

Примеры использования Xbaza AI API для AI ботов и ассистентов.
"""

import requests
import json
from typing import Dict, List, Optional, Any
from datetime import datetime


class XbazaAIClient:
    """Клиент для работы с Xbaza AI API"""
    
    BASE_URL = "https://xbaza.by/api/ai"
    
    def __init__(self, user_agent: str = "ChatGPT-User"):
        """
        Инициализация клиента
        
        Args:
            user_agent: User-Agent для идентификации AI бота
        """
        self.headers = {
            "User-Agent": user_agent,
            "Accept": "application/json"
        }
    
    def _request(
        self, 
        method: str, 
        endpoint: str, 
        params: Optional[Dict] = None,
        data: Optional[Dict] = None
    ) -> Dict[str, Any]:
        """
        Базовый метод для выполнения запросов
        
        Args:
            method: HTTP метод (GET, POST, etc.)
            endpoint: Эндпоинт API
            params: Параметры запроса
            data: Тело запроса (для POST)
        
        Returns:
            Ответ API в виде словаря
        """
        url = f"{self.BASE_URL}{endpoint}"
        
        response = requests.request(
            method=method,
            url=url,
            headers=self.headers,
            params=params,
            json=data
        )
        
        response.raise_for_status()
        return response.json()
    
    # ==================== Discovery & Info ====================
    
    def get_api_info(self) -> Dict[str, Any]:
        """Получить базовую информацию об API"""
        return self._request("GET", "")
    
    def get_api_schema(self) -> Dict[str, Any]:
        """Получить полную схему API в JSON формате"""
        response = requests.get(
            f"{self.BASE_URL}.json",
            headers=self.headers
        )
        response.raise_for_status()
        return response.json()
    
    def discover_endpoints(self) -> Dict[str, Any]:
        """Обнаружить все доступные эндпоинты"""
        return self._request("GET", "/discovery")
    
    # ==================== Jobs ====================
    
    def get_jobs(
        self, 
        limit: int = 20,
        category: Optional[str] = None,
        city: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Получить список вакансий
        
        Args:
            limit: Количество вакансий (1-50)
            category: Фильтр по категории
            city: Фильтр по городу
        
        Returns:
            Список вакансий с метаданными
        """
        params = {"limit": limit}
        if category:
            params["category"] = category
        if city:
            params["city"] = city
        
        return self._request("GET", "/jobs", params=params)
    
    def create_job(
        self,
        title: str,
        description: str,
        company_name: str,
        city_name: str,
        category_name: Optional[str] = None,
        salary_min: Optional[int] = None,
        salary_max: Optional[int] = None
    ) -> Dict[str, Any]:
        """
        Создать вакансию (только для AI ботов)
        
        Args:
            title: Название вакансии
            description: Описание
            company_name: Название компании
            city_name: Название города
            category_name: Категория (опционально)
            salary_min: Минимальная зарплата (опционально)
            salary_max: Максимальная зарплата (опционально)
        
        Returns:
            Созданная вакансия
        """
        data = {
            "title": title,
            "description": description,
            "company_name": company_name,
            "city_name": city_name
        }
        
        if category_name:
            data["category_name"] = category_name
        if salary_min:
            data["salary_min"] = salary_min
        if salary_max:
            data["salary_max"] = salary_max
        
        return self._request("POST", "/jobs", data=data)
    
    # ==================== Services ====================
    
    def get_services(
        self,
        limit: int = 20,
        category: Optional[str] = None,
        city: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Получить список бизнес-услуг
        
        Args:
            limit: Количество услуг (1-50)
            category: Фильтр по категории
            city: Фильтр по городу
        
        Returns:
            Список услуг с метаданными
        """
        params = {"limit": limit}
        if category:
            params["category"] = category
        if city:
            params["city"] = city
        
        return self._request("GET", "/services", params=params)
    
    def create_service(
        self,
        name: str,
        description: str,
        company_name: str,
        city_name: str,
        price: Optional[float] = None,
        contacts: Optional[str] = None,
        category_name: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Создать услугу (только для AI ботов)
        
        Args:
            name: Название услуги
            description: Описание
            company_name: Название компании
            city_name: Название города
            price: Цена (опционально)
            contacts: Контакты (опционально)
            category_name: Категория (опционально)
        
        Returns:
            Созданная услуга
        """
        data = {
            "name": name,
            "description": description,
            "company_name": company_name,
            "city_name": city_name
        }
        
        if price:
            data["price"] = price
        if contacts:
            data["contacts"] = contacts
        if category_name:
            data["category_name"] = category_name
        
        return self._request("POST", "/services", data=data)
    
    # ==================== Users ====================
    
    def search_users(
        self,
        query: str,
        limit: int = 20,
        format: str = "json"
    ) -> Dict[str, Any]:
        """
        Поиск пользователей по имени, фамилии или ID
        
        Args:
            query: Поисковый запрос (минимум 2 символа)
            limit: Количество результатов (1-50)
            format: Формат ответа (json, csv, xml)
        
        Returns:
            Список пользователей
        """
        params = {
            "q": query,
            "limit": limit,
            "format": format
        }
        
        return self._request("GET", "/users", params=params)
    
    # ==================== Business ====================
    
    def get_business_listings(
        self,
        limit: int = 20,
        category: Optional[str] = None,
        city: Optional[str] = None,
        min_price: Optional[int] = None,
        max_price: Optional[int] = None,
        format: str = "json"
    ) -> Dict[str, Any]:
        """
        Получить список объявлений о продаже готового бизнеса
        
        Args:
            limit: Количество объявлений (1-100)
            category: Фильтр по категории
            city: Фильтр по городу
            min_price: Минимальная цена
            max_price: Максимальная цена
            format: Формат ответа (json, csv, xml)
        
        Returns:
            Список объявлений о бизнесе
        """
        params = {"limit": limit, "format": format}
        
        if category:
            params["category"] = category
        if city:
            params["city"] = city
        if min_price:
            params["minPrice"] = min_price
        if max_price:
            params["maxPrice"] = max_price
        
        return self._request("GET", "/business", params=params)
    
    # ==================== Property ====================
    
    def get_property_listings(
        self,
        limit: int = 20,
        property_type: Optional[str] = None,
        deal_type: Optional[str] = None,
        city: Optional[str] = None,
        min_price: Optional[int] = None,
        max_price: Optional[int] = None,
        min_area: Optional[float] = None,
        max_area: Optional[float] = None,
        format: str = "json"
    ) -> Dict[str, Any]:
        """
        Получить список коммерческой недвижимости
        
        Args:
            limit: Количество объявлений (1-100)
            property_type: Тип недвижимости (OFFICE, RETAIL, WAREHOUSE, etc.)
            deal_type: Тип сделки (SALE, RENT)
            city: Фильтр по городу
            min_price: Минимальная цена
            max_price: Максимальная цена
            min_area: Минимальная площадь
            max_area: Максимальная площадь
            format: Формат ответа (json, csv, xml)
        
        Returns:
            Список объявлений о недвижимости
        """
        params = {"limit": limit, "format": format}
        
        if property_type:
            params["propertyType"] = property_type
        if deal_type:
            params["dealType"] = deal_type
        if city:
            params["city"] = city
        if min_price:
            params["minPrice"] = min_price
        if max_price:
            params["maxPrice"] = max_price
        if min_area:
            params["minArea"] = min_area
        if max_area:
            params["maxArea"] = max_area
        
        return self._request("GET", "/property", params=params)
    
    # ==================== Simple API ====================
    
    def get_simple_data(
        self,
        data_type: str = "jobs",
        limit: int = 50,
        category: Optional[str] = None,
        city: Optional[str] = None,
        format: str = "json"
    ) -> Dict[str, Any]:
        """
        Упрощенный доступ к данным
        
        Args:
            data_type: Тип данных (jobs, companies, all)
            limit: Количество (1-100)
            category: Фильтр по категории
            city: Фильтр по городу
            format: Формат ответа (json, csv, xml)
        
        Returns:
            Данные в упрощенном формате
        """
        params = {
            "type": data_type,
            "limit": limit,
            "format": format
        }
        
        if category:
            params["category"] = category
        if city:
            params["city"] = city
        
        return self._request("GET", "/simple", params=params)
    
    # ==================== Belarus Data ====================
    
    def get_belarus_data(
        self,
        data_type: str = "overview"
    ) -> Dict[str, Any]:
        """
        Получить комплексные данные о белорусском рынке
        
        Args:
            data_type: Тип данных (overview, jobs, companies, services, trends, salary, cities, industries)
        
        Returns:
            Данные о белорусском рынке
        """
        params = {"type": data_type}
        return self._request("GET", "/belarus", params=params)
    
    # ==================== Analytics ====================
    
    def get_analytics(
        self,
        analytics_type: str = "overview",
        days: int = 30,
        limit: int = 20
    ) -> Dict[str, Any]:
        """
        Получить аналитику рынка
        
        Args:
            analytics_type: Тип аналитики (overview, bots, daily, pages, types, geographic, quality, all)
            days: Количество дней
            limit: Количество результатов
        
        Returns:
            Аналитические данные
        """
        params = {
            "type": analytics_type,
            "days": days,
            "limit": limit
        }
        return self._request("GET", "/analytics", params=params)
    
    # ==================== Categories & Cities ====================
    
    def get_categories(self) -> Dict[str, Any]:
        """Получить все доступные категории вакансий"""
        return self._request("GET", "/categories")
    
    def get_cities(self) -> Dict[str, Any]:
        """Получить все города Беларуси с координатами"""
        return self._request("GET", "/cities")


# ==================== Примеры использования ====================

def example_basic_usage():
    """Базовое использование API"""
    client = XbazaAIClient(user_agent="ChatGPT-User")
    
    # Получить информацию об API
    info = client.get_api_info()
    print("API Info:", json.dumps(info, indent=2, ensure_ascii=False))
    
    # Получить вакансии
    jobs = client.get_jobs(limit=10, category="IT")
    print(f"\nНайдено вакансий: {jobs['meta']['count']}")
    for job in jobs['data'][:3]:
        print(f"- {job.get('title', 'N/A')}")

def example_search_users():
    """Поиск пользователей"""
    client = XbazaAIClient(user_agent="Claude-Web")
    
    # Поиск по имени
    users = client.search_users("Иван", limit=10)
    print(f"Найдено пользователей: {len(users.get('data', []))}")
    
    for user in users.get('data', [])[:3]:
        print(f"- {user.get('firstName', '')} {user.get('lastName', '')}")

def example_business_listings():
    """Работа с объявлениями о бизнесе"""
    client = XbazaAIClient(user_agent="PerplexityBot")
    
    # Получить бизнесы в Минске
    businesses = client.get_business_listings(
        limit=20,
        city="Минск",
        min_price=10000,
        max_price=100000
    )
    
    print(f"Найдено бизнесов: {businesses['meta']['count']}")
    for business in businesses['data'][:3]:
        print(f"- {business.get('title', 'N/A')}: {business.get('price', 0)} BYN")

def example_property_listings():
    """Работа с коммерческой недвижимостью"""
    client = XbazaAIClient(user_agent="ChatGPT-User")
    
    # Офисы в аренду
    properties = client.get_property_listings(
        limit=20,
        property_type="OFFICE",
        deal_type="RENT",
        city="Минск"
    )
    
    print(f"Найдено объектов: {properties['meta']['count']}")
    for prop in properties['data'][:3]:
        print(f"- {prop.get('title', 'N/A')}: {prop.get('price', 0)} BYN/мес")

def example_market_analysis():
    """Анализ рынка"""
    client = XbazaAIClient(user_agent="Claude-Web")
    
    # Получить обзор рынка
    overview = client.get_belarus_data("overview")
    print("Обзор белорусского рынка:")
    print(json.dumps(overview, indent=2, ensure_ascii=False))
    
    # Получить тренды
    trends = client.get_belarus_data("trends")
    print("\nТренды рынка:")
    print(json.dumps(trends, indent=2, ensure_ascii=False))

def example_create_job():
    """Создание вакансии (только для AI ботов)"""
    client = XbazaAIClient(user_agent="ChatGPT-User")
    
    try:
        job = client.create_job(
            title="Python Developer",
            description="Разработка на Python, Django, FastAPI",
            company_name="Tech Company",
            city_name="Минск",
            category_name="IT",
            salary_min=1500,
            salary_max=2500
        )
        print("Вакансия создана:", job.get('data', {}).get('title', 'N/A'))
    except requests.exceptions.HTTPError as e:
        print(f"Ошибка: {e}")

if __name__ == "__main__":
    print("=== Xbaza AI API Examples ===\n")
    
    # Раскомментируйте нужные примеры:
    
    # example_basic_usage()
    # example_search_users()
    # example_business_listings()
    # example_property_listings()
    # example_market_analysis()
    # example_create_job()
    
    print("\nДля использования примеров раскомментируйте нужные функции в коде.")

