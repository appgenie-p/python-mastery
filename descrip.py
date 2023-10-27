class Descriptor:
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, cls):
        print(f"{self.name}:__get__")

    def __set__(self, instance, value):
        print(f"{self.name}:__set__ {value}")

    def __delete__(self, instance):
        print(f"{self.name}:__delete__")


class Foo:
    a = Descriptor()
    b = Descriptor()
    c = Descriptor()
