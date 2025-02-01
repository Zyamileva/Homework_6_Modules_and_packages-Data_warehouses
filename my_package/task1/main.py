from string_utils import strip_text, to_uppercase
from math_utils import factor_custom, greatest_common_divisor

n = 4
print(f"factorial of {n} is {factor_custom(n)}")

a = 10
b = 4
print(f"The greatest common divisor of {a} and {b} is {greatest_common_divisor(a, b)}")

text_to_change = "  Hello World   "
print(strip_text(to_uppercase(text_to_change)))
