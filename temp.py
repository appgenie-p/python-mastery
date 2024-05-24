class MyMeta(type):
    def __new__(cls, name, bases, dct):
        print(f"Creating class {name}")
        # Вы можете изменить или добавить атрибуты класса здесь
        dct["created_by"] = "MyMeta"
        return super().__new__(cls, name, bases, dct)


class MyClass(metaclass=MyMeta):
    def __init__(self, value):
        self.value = value

    def display(self):
        print(f"Value: {self.value}")


# Создание экземпляра класса MyClass
obj = MyClass(42)
obj.display()

# Проверка дополнительного атрибута, добавленного метаклассом
print(obj.created_by)
