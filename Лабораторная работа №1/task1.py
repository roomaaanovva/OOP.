class Book:
    """
    Класс, описывающий книгу.
    """

    def __init__(self, title: str, author: str, pages: int):
        """
        Инициализирует объект Book.

        Args:
            title (str): Название книги.  Не может быть пустой строкой.
            author (str): Автор книги. Не может быть пустой строкой.
            pages (int): Количество страниц. Должно быть положительным числом.

        Raises:
            ValueError: Если title, author пустые строки или pages не положительное число.
        """
        if not title:
            raise ValueError("Название книги не может быть пустым.")
        if not author:
            raise ValueError("Автор книги не может быть пустым.")
        if pages <= 0:
            raise ValueError("Количество страниц должно быть положительным числом.")
        self.title: str = title
        self.author: str = author
        self.pages: int = pages

    def get_info(self) -> str:
        """
        Возвращает информацию о книге.

        Returns:
            str: Строка с информацией о книге.

        >>> book = Book("Python для начинающих", "Иван Иванов", 200)
        >>> book.get_info()
        'Название: Python для начинающих, Автор: Иван Иванов, Страниц: 200'
        """
        return f"Название: {self.title}, Автор: {self.author}, Страниц: {self.pages}"

    def add_bookmark(self, page_number: int) -> None:
        """
        Добавляет закладку на указанную страницу.

        Args:
            page_number (int): Номер страницы для закладки.  Должен быть в пределах количества страниц книги.

        Raises:
            ValueError: Если номер страницы вне допустимого диапазона.
        """
        if not 1 <= page_number <= self.pages:
            raise ValueError("Номер страницы вне допустимого диапазона.")
        print(f"Закладка добавлена на страницу {page_number}")


class Website:
    """
    Класс, описывающий веб-сайт.
    """

    def __init__(self, url: str, domain: str = "example.com"):
        """
        Инициализирует объект Website.

        Args:
            url (str): URL сайта. Не может быть пустой строкой.
            domain (str, optional): Домен сайта. Значение по умолчанию - "example.com".
        """
        if not url:
            raise ValueError("URL не может быть пустым.")
        self.url: str = url
        self.domain: str = url.split('/')[2]

    def get_domain(self) -> str:
        """
        Возвращает домен сайта.

        Returns:
            str: Домен сайта.

        >>> website = Website("https://www.google.com")
        >>> website.get_domain()
        'www.google.com'
        """
        return self.domain

    def check_url(self, test_url: str) -> bool:
        """
        Проверяет, содержит ли URL сайта указанную подстроку.

        Args:
            test_url (str): Подстрока для поиска в URL.

        Returns:
            bool: True, если подстрока найдена, False - иначе.

        >>> website = Website("https://www.example.com/path/to/page")
        >>> website.check_url("example")
        True
        >>> website.check_url("google")
        False

        """
        return test_url in self.url


class Stack:
    """
    Класс, описывающий стек (структура данных).
    """

    def __init__(self, values: list = [], isempty: bool = True):
        """Инициализирует пустой стек."""
        self.items: list = values
        self.empty: bool = isempty

    def push(self, item: object) -> None:
        """
        Добавляет элемент в стек.

        Args:
            item (object): Элемент для добавления.
        """
        self.items.append(item)

    def pop(self) -> object:
        """
        Удаляет и возвращает верхний элемент стека.

        Raises:
            IndexError: Если стек пуст.

        Returns:
            object: Верхний элемент стека.

        >>> stack = Stack()
        >>> stack.push(1)
        >>> stack.push(2)
        >>> stack.pop()
        2
        """
        if not self.items:
            raise IndexError("Стек пуст")
        return self.items.pop()
