#triangulo de pascal
from math import factorial as f
[print([int(f(j)/(f(i)*f(j-i))) for i in range(j+1)]) for j in range(int(input()))]