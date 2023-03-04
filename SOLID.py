# SOLID - это аббревиатура, которая представляет собой пять основных принципов объектно-ориентированного программирования. Они были впервые предложены Робертом Мартином (Robert C. Martin) и используются для создания гибкого, расширяемого и легко поддерживаемого программного обеспечения.

#1.  Принцип единственной ответственности (Single Responsibility Principle - SRP)
#Каждый класс должен иметь только одну ответственность и должен быть изменен только по одной причине. 
#Это означает, что класс должен содержать только одну логическую функцию или ответственность, и все его методы и свойства должны быть направлены на выполнение этой функции.
    
#2.Принцип открытости/закрытости (Open/Closed Principle - OCP) 
#Программные сущности (классы, модули, функции) должны быть открыты для расширения, но закрыты для изменения. 
#Это означает, что вы можете добавлять новые функциональные возможности, не изменяя существующий код.
    
#3.Принцип подстановки Барбары Лисков (Liskov Substitution Principle - LSP) 
#Объекты в программе должны быть заменяемыми на экземпляры их подтипов без изменения правильности выполнения программы. 
#То есть подклассы должны дополнять, а не изменять функциональность базового класса.
    
#4.Принцип разделения интерфейса (Interface Segregation Principle - ISP) 
#Клиенты не должны зависеть от методов, которые они не используют.
#Интерфейсы должны быть маленькими и специфичными, чтобы клиенты могли реализовывать только те методы, которые им необходимы.
    
#5.Принцип инверсии зависимостей (Dependency Inversion Principle - DIP) 
#Модули высокого уровня не должны зависеть от модулей низкого уровня, оба должны зависеть от абстракций. 
#Абстракции не должны зависеть от деталей, но детали должны зависеть от абстракций. 
#Это означает, что зависимости между объектами должны быть организованы таким образом, чтобы изменение в одном объекте не приводило к изменению в другом объекте.



#Принцип единственной ответственности (Single Responsibility Principle - SRP) 
#заключается в том, что каждый класс должен иметь только одну ответственность. 
#Например, если у нас есть класс, который отвечает за обработку данных и вывод их на экран, то он не соответствует SRP, так как он выполняет две различные функции.

#Пример:
class DataProcessor:
    def __init__(self, data):
        self.data = data
    
    def process_data(self):
        # обработка данных
        return processed_data
    
    def display_data(self):
        # вывод данных на экран
        pass

#В данном примере у нашего класса `DataProcessor` только одна ответственность: 
#обработка данных и вывод их на экран. Конструктор класса инициализирует данные, а метод `process_data()` 
#выполняет их обработку, а метод `display_data()` выводит их на экран.

#Контрпример:
class DataProcessor:
    def __init__(self, data):
        self.data = data
    
    def process_data(self):
        # обработка данных
        return processed_data
    
    def save_data(self):
        # сохранение данных в файл
        pass

#В данном примере класс `DataProcessor` имеет две ответственности: обработка данных и их сохранение в файл. 
#Это нарушает принцип SRP. Чтобы исправить это, можно вынести сохранение данных в отдельный класс, который будет отвечать только за эту функцию. 
#Таким образом, класс `DataProcessor` будет отвечать только за обработку данных, что будет соответствовать принципу SRP.

#Принцип открытости/закрытости (Open/Closed Principle - OCP) заключается в том, 
#что программные сущности должны быть открыты для расширения, но закрыты для изменения.

#Пример:
class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius ** 2

#В данном примере класс `Shape` является абстрактным базовым классом для всех геометрических фигур. 
#Классы `Rectangle` и `Circle` наследуют от него и реализуют метод `area()`, который возвращает площадь фигуры.
#Теперь, если нам нужно добавить новую геометрическую фигуру, мы можем создать новый класс, 
#который будет наследовать от `Shape` и реализовывать метод `area()`, не изменяя при этом существующий код. Это соответствует принципу OCP.

#Контрпример:
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius ** 2

#В данном примере классы `Rectangle` и `Circle` реализуют метод `area()` и не имеют общего базового класса. 
#Если мы захотим добавить новую геометрическую фигуру, мы должны будем создать новый класс и повторно реализовать метод `area()`. 
#Это нарушает принцип OCP, так как при добавлении новой фигуры нам придется изменять существующий код.

#Принцип подстановки Барбары Лисков (Liskov Substitution Principle - LSP) заключается в том, 
#что объекты должны быть заменяемыми своими наследниками без изменения свойств программы.

#Пример:
class Bird:
    def fly(self):
        print("I am flying")

class Penguin(Bird):
    def fly(self):
        raise Exception("I can't fly")

def make_bird_fly(bird):
    bird.fly()

bird = Bird()
penguin = Penguin()

make_bird_fly(bird)    # выведет "I am flying"
make_bird_fly(penguin) # выбросит исключение "I can't fly"

#В данном примере класс `Penguin` наследуется от класса `Bird`. Хотя пингвин не умеет летать, мы все равно можем использовать его вместо класса `Bird` в функции `make_bird_fly()`.
#Функция `make_bird_fly()` принимает объект типа `Bird` и вызывает его метод `fly()`. 
#Мы можем передавать как объекты класса `Bird`, так и объекты класса `Penguin`, и программа будет работать корректно. Это соответствует принципу LSP.

#Контрпример:
class Bird:
    def fly(self):
        print("I am flying")

class Ostrich(Bird):
    def run(self):
        print("I am running")

def make_bird_fly(bird):
    bird.fly()

bird = Bird()
ostrich = Ostrich()

make_bird_fly(bird)    # выведет "I am flying"
make_bird_fly(ostrich) # вызовет AttributeError, так как объект класса Ostrich не имеет метода fly()

#В данном примере класс `Ostrich` наследуется от класса `Bird`. 
#Однако, он не имеет метода `fly()`, который есть у его базового класса. 
#Поэтому, если мы передадим объект класса `Ostrich` в функцию `make_bird_fly()`, программа вызовет ошибку, нарушая принцип LSP.

#Принцип разделения интерфейса (Interface Segregation Principle - ISP) утверждает, что клиенты не должны зависеть от методов, которые они не используют.

#Пример:
class Printer:
    def print(self, document):
        raise NotImplementedError

class Scanner:
    def scan(self):
        raise NotImplementedError

class Fax:
    def fax(self, document):
        raise NotImplementedError

class AllInOnePrinter(Printer, Scanner, Fax):
    def print(self, document):
        print("Printing...")
    
    def scan(self):
        print("Scanning...")
    
    def fax(self, document):
        print("Faxing...")

class PrinterClient:
    def __init__(self, printer):
        self.printer = printer

    def print_document(self, document):
        self.printer.print(document)

class ScannerClient:
    def __init__(self, scanner):
        self.scanner = scanner
    
    def scan_document(self):
        self.scanner.scan()

printer = AllInOnePrinter()
printer_client = PrinterClient(printer)
printer_client.print_document("Example Document") # выведет "Printing..."

scanner = AllInOnePrinter()
scanner_client = ScannerClient(scanner)
scanner_client.scan_document() # выведет "Scanning..."

#В данном примере мы имеем три различных устройства: `Printer`, `Scanner`, `Fax`. 
#Устройства наследуются от базового интерфейса, который содержит единственный метод `print()`, `scan()`, `fax()`, соответственно.
#Затем мы имеем класс `AllInOnePrinter`, который реализует все три интерфейса, тем самым предоставляя все три метода.
#Далее у нас есть два клиента - `PrinterClient`, который работает только с методом `print()`, и `ScannerClient`, который работает только с методом `scan()`. 
#Вместо того, чтобы передавать объект `AllInOnePrinter` обоим клиентам, мы передаем каждому клиенту соответствующий объект - `Printer` для `PrinterClient` и `Scanner` для `ScannerClient`. 
#Таким образом, клиенты не зависят от методов, которые они не используют.

#Контрпример:
class Printer:
    def print(self, document):
        print("Printing...")

    def scan(self):
        raise NotImplementedError

    def fax(self, document):
        raise NotImplementedError

class PrinterClient:
    def __init__(self, printer):
        self.printer = printer

    def print_document(self, document):
        self.printer.print(document)

class ScannerClient:
    def __init__(self, scanner):
        self.scanner = scanner
    
    def scan_document(self):
        self.scanner.scan()

printer = Printer()
printer_client = PrinterClient(printer)
printer_client.print_document("Example Document") # выведет "Printing..."

scanner = Printer()
scanner_client = ScannerClient(scanner)
scanner_client.scan_document() # вызовет AttributeError, так как объект класса Printer не имеет метода scan()

#В данном примере класс `Printer` реализует все три метода - `print()`, `scan()`, `fax()`. 
#Затем у нас есть два клиента - `PrinterClient`, который работает только с методом `print()`, и `ScannerClient`, который работает только с методом `scan()`.
#Однако, класс `Printer` не реализует метод `scan()`. Поэтому при попытке использовать `Printer` как объект класса `ScannerClient`, вызов метода `scan_document()` приведет к ошибке `AttributeError`, 
#так как объект класса `Printer` не имеет метода `scan()`.
#Этот пример нарушает принцип разделения интерфейса, так как класс `Printer` наследует все три метода, хотя не использует два из них. 
#Как результат, клиенты, которые используют только один метод, вынуждены зависеть от всех трех методов, что может привести к проблемам при изменении и расширении кода.


#Принцип инверсии зависимостей (Dependency Inversion Principle - DIP) утверждает, что высокоуровневые модули не должны зависеть от низкоуровневых модулей, а оба типа модулей должны зависеть от абстракций.
class AbstractDatabase:
    def save(self, data):
        raise NotImplementedError

class MongoDB(AbstractDatabase):
    def save(self, data):
        print(f"Saving {data} to MongoDB...")

class PostgreSQL(AbstractDatabase):
    def save(self, data):
        print(f"Saving {data} to PostgreSQL...")

class User:
    def __init__(self, name, database):
        self.name = name
        self.database = database
    
    def save(self):
        self.database.save(f"{self.name} user")

database = MongoDB()
user = User("John", database)
user.save() # выведет "Saving John user to MongoDB..."

database = PostgreSQL()
user = User("Jane", database)
user.save() # выведет "Saving Jane user to PostgreSQL..."

# В данном примере мы имеем две реализации баз данных - `MongoDB` и `PostgreSQL`, которые наследуют абстрактный класс `AbstractDatabase`. 
# Класс `User` использует базу данных для сохранения данных. При создании объекта класса `User`, мы передаем соответствующий объект базы данных. 
# Таким образом, класс `User` зависит от абстракции `AbstractDatabase`, а не от конкретной реализации базы данных.

# Контрпример:
class MongoDB:
    def save(self, data):
        print(f"Saving {data} to MongoDB...")

class PostgreSQL:
    def save(self, data):
        print(f"Saving {data} to PostgreSQL...")

class User:
    def __init__(self, name, database):
        self.name = name
        self.database = database
    
    def save(self):
        if isinstance(self.database, MongoDB):
            self.database.save(f"{self.name} user")
        elif isinstance(self.database, PostgreSQL):
            self.database.save(f"{self.name} user")

database = MongoDB()
user = User("John", database)
user.save() # выведет "Saving John user to MongoDB..."

database = PostgreSQL()
user = User("Jane", database)
user.save() # выведет "Saving Jane user to PostgreSQL..."

#В данном примере класс `User` зависит от конкретных реализаций баз данных - `MongoDB` и `PostgreSQL`. 
#Вместо того, чтобы зависеть от абстракции, класс `User` проверяет тип переданного объекта базы данных и вызывает соответствующий метод `save()`. 
#Такой подход нарушает принцип инверсии зависимостей, так как высокоуровневый модуль `User` зависит от низкоуровневых модулей - `MongoDB` и `PostgreSQL`. 
#Кроме того, такой подход делает код менее гибким и не позволяет добавлять новые реализации баз данных без изменения кода класса `User`.