# Importuokite reikiamus modulius, kad veiktų žemiau nurodytos funkcijos

from modules.math.composition import composition
from modules.math.division import division
from modules.math.multiplication import multiplication
from modules.math.subtraction import substraction

# Kitų failų ir žemiau esančio kodo nekeiskite

a = composition(1, 4)
b = division(4, 2)
c = substraction(3, 2)
d = multiplication(5, 2)

print('Composition:', a)
print('Division:', b)
print('Subtraction:', c)
print('Multiplication:', d)

def veiksmas(skaicius, daugiklis=1):
    print(skaicius * daugiklis)

veiksmas(20)