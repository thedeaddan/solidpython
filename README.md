Принципы SOLID
==============

SOLID - это акроним, используемый для обозначения пяти основных принципов объектно-ориентированного программирования (ООП). Эти принципы описывают, как создавать гибкий, расширяемый и легко поддерживаемый код.

S - Принцип единственной ответственности (Single Responsibility Principle - SRP)
--------------------------------------------------------------------------------

Каждый класс должен иметь только одну ответственность. Это означает, что класс должен выполнять только одну задачу и не должен знать о других задачах.

**Пример**:


```python
# Плохой пример
class Employee:
    def calculate_pay(self):
        pass
    
    def save_to_database(self):
        pass

# Хороший пример
class Employee:
    def calculate_pay(self):
        pass

class EmployeeDatabase:
    def save(self, employee):
        pass
```

O - Принцип открытости/закрытости (Open/Closed Principle - OCP)
---------------------------------------------------------------

Программные сущности должны быть открыты для расширения, но закрыты для изменения. Это означает, что вы можете добавлять новую функциональность, не меняя существующий код.

**Пример**:


```python
# Плохой пример
class Shape:
    def draw(self):
        raise NotImplementedError

class Circle(Shape):
    def draw(self):
        print("Drawing a circle...")

class Square(Shape):
    def draw(self):
        print("Drawing a square...")

# При добавлении новой фигуры нам придется изменить существующий код
class Triangle(Shape):
    def draw(self):
        print("Drawing a triangle...")
```


```python
# Хороший пример
class Shape:
    def draw(self):
        raise NotImplementedError

class Circle(Shape):
    def draw(self):
        print("Drawing a circle...")

class Square(Shape):
    def draw(self):
        print("Drawing a square...")

class Triangle(Shape):
    def draw(self):
        print("Drawing a triangle...")
```

L - Принцип подстановки Барбары Лисков (Liskov Substitution Principle - LSP)
----------------------------------------------------------------------------

Объекты в программе могут быть заменены их наследниками без изменения свойств программы. Это означает, что подклассы должны соответствовать своим суперклассам в терминах интерфейса и поведения.

**Пример**:


```python
# Хороший пример
class Bird:
    def fly(self):
        pass

class Sparrow(Bird):
    def fly(self):
        print("Sparrow is flying...")

class Penguin(Bird):
    def fly(self):
        raise NotImplementedError
```


```python
# Плохой пример
class Bird:
    def fly(self):
        pass

class Sparrow(Bird):
    def fly(self):
        print("Sparrow is flying...")

class Penguin(Bird):
    pass
```

I - Принцип разделения интерфейса (Interface Segregation Principle - ISP)
-------------------------------------------------------------------------

Клиенты не должны зависеть от интерфейсов, которые они не используют. Это означает, что интерфейсы должны быть маленькими и специфичными для каждого клиента.

**Пример**:

```python
# Плохой пример
class Machine:
    def print_document(self):
        raise NotImplementedError

    def scan_document(self):
        raise NotImplementedError

    def fax_document(self):
        raise NotImplementedError

class Printer(Machine):
    def print_document(self):
        print("Printing a document...")

class Scanner(Machine):
    def scan_document(self):
        print("Scanning a document...")

class Fax(Machine):
    def fax_document(self):
        print("Sending a fax...")
```

```python
# Хороший пример
class Printer:
    def print_document(self):
        print("Printing a document...")

class Scanner:
    def scan_document(self):
        print("Scanning a document...")

class Fax:
    def fax_document(self):
        print("Sending a fax...")
```

D - Принцип инверсии зависимостей (Dependency Inversion Principle - DIP)
------------------------------------------------------------------------

Модули верхнего уровня не должны зависеть от модулей нижнего уровня. Оба должны зависеть от абстракций. Абстракции не должны зависеть от деталей. Детали должны зависеть от абстракций.

**Пример**:

```python
# Плохой пример
class Notification:
    def __init__(self):
        self.email = Email()

    def send(self, message):
        self.email.send(message)

class Email:
    def send(self, message):
        print(f"Sending an email: {message}")
```

```python
# Хороший пример
class Notification:
    def __init__(self, sender):
        self.sender = sender

    def send(self, message):
        self.sender.send(message)

class Email:
    def send(self, message):
        print(f"Sending an email: {message}")

class SMS:
    def send(self, message):
        print(f"Sending an SMS: {message}")
```

Заключение
----------

SOLID - это набор принципов, которые помогают создавать гибкий, расширяемый и легко поддерживаемый код. Применение этих принципов в вашем коде может значительно улучшить его качество и упростить поддержку в будущем.  
**Более подробные примеры с описанием в файле SOLID.py**
