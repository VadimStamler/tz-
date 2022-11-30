# -*- coding: utf-8 -*-
"""Task2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ADGKLBu_WyT1glZncIrIHGmiXFwaGdE9
"""

per1 = input('Введите путь к файлу file1.txt: ')
per2 = input('Введите путь к файлу file2.txt: ')


with open(per1, "r") as f:
      circle = list(map(float, f.read().split()))
# print(circle)

with open(per2, "r") as f:
     point = [list(map(float, line.split())) for line in f ]
# print(point)

x0, y0, r0 = circle


import math

for k in point:
  if   (k[0] - x0)**2 + (k[1] - y0)**2 == r0**2:
    # print(f'Точка на окружности {k[0], k[1]}')
    print(0)
  elif  math.sqrt((k[0] - x0)**2 + (k[1] -y0)**2) < r0:
    # print(f'Точка внутри окружности {k[0], k[1]}')
    print(1)
  else: 
    # print(f'Точка снаружи {k[0], k[1]}')
    print(2)