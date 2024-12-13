from task_1 import Book, Website, Stack  # TODO: импортируйте классы, созданные в ходе выполнения прошлого задания

if __name__ == "__main__":
    # TODO: инстанцировать все описанные классы, создав три объекта.C()
    try:
        book1 = Book("Война и мир", "Лев Толстой", 1225)
        book1.add_bookmark(1500)  # некорректное использование - ожидается исключение
    except ValueError:
        print(f"Ошибка: неправильные данные")

    # Тестирование класса Website
    try:
        website1 = Website("")
    except ValueError:
        print(f"Ошибка: неправильные данные")

    # Тестирование класса Stack
    stack1 = Stack()
    stack1.push(10)
    stack1.push(20)
    try:
        stack1.pop()
        stack1.pop()
        print(stack1.pop())  # некорректное использование - ожидается исключение
    except IndexError as e:
        print(f"Ошибка: неправильные данные")
\