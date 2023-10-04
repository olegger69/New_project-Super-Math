import modules.perimeter as perimeter
import modules.factorial as factorial
import modules.test as t
import modules.tests.test_all as ta

f1 = factorial.factorial_rec(5)
print(f1)

f2 = factorial.factorial_rec(15)
print(f2)

f3 = factorial.factorial_rec(5)
print(f3)

f4 = factorial.factorial_rec(17)
print(f4)

print(f1 == f3, f2 == f4)

p1 = perimeter.perimeter_func([1, 2, 5])
print(p1)

p2 = perimeter.perimeter_func([1, 2, 5, 7, 3])
print(p2)
print("hello world")
