"""Demostrando os loops do python"""
from random import randint

print('Loop tipico, for:', end=' ')

for x in range(10):
    print(x, end=' ')

print()
print('Loop tipico, while:', end=' ')

c = 0
while c < 10:
    print(c, end=' ')
    c += 1

print()
print('Loop Multiplos de 3 até 20 for:', end=' ')

for x in range(3, 21, 3):
    print(x, end=' ')

print()
print('Loop Multiplos de 3 até 20 while:', end=' ')

c = 3
while c <= 20:
    print(c, end=' ')
    c += 3

print()

lista = [randint(10, 99) for x in range(1, 15)]
for item in lista:
    print(item, end=' ')

print()
print(lista)

lista = [x for x in range(15)]
print(lista)
