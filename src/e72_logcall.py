# e72_logcall.py


from functools import wraps


def logformat(fmt: str):
    def decorator(func):
        original_func = None
        if isinstance(func, (staticmethod, classmethod)):
            original_func = func
            func = func.__func__
        elif isinstance(func, property):
            original_func = func
            func = func.fget

        print("Adding logging to", func.__name__)

        @wraps(func)
        def wrapper(*args, **kwargs):
            print(fmt.format(func=func))
            return func(*args, **kwargs)

        if isinstance(original_func, staticmethod):
            return staticmethod(wrapper)
        elif isinstance(original_func, classmethod):
            return classmethod(wrapper)
        elif isinstance(original_func, property):
            return property(wrapper)
        else:
            return wrapper

    return decorator


logged = logformat("Calling {func.__name__}")


if __name__ == "__main__":

    class Spam:
        @logged
        def instance_method(self):
            pass

        @logged
        @classmethod
        def class_method(cls):
            pass

        @logged
        @staticmethod
        def static_method():
            pass

        @logged
        @property
        def property_method(self):
            pass

    s = Spam()

    s.instance_method()
    Spam.class_method()
    Spam.static_method()
    s.property_method
