from validate import *

# assert PositiveInteger.check(10) == 10
# assert PositiveInteger.check('10')
# # Traceback (most recent call last):
# #   File "<stdin>", line 1, in <module>
# #     raise TypeError(f'Expected {cls.expected_type}')
# # TypeError: Expected <class 'int'>
# assert PositiveInteger.check(-10)
# # Traceback (most recent call last):
# #   File "<stdin>", line 1, in <module>
# #     raise ValueError('Expected >= 0')
# # ValueError: Must be >= 0


NonEmptyString.check('hello') == 'hello'
assert NonEmptyString.check('')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#     raise ValueError('Must be non-empty')
# ValueError: Must be non-empty
# assert