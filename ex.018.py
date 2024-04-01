import math
a = float(input('digite o valor do ângulo:'))

sen = math.sin(math.radians(a))
print(f'o ângulo de {a} tem o seno de {sen:.2f}.')
cos = math.cos(math.radians(a))
print(f'O ângulo de {a} tem o cosseno de {cos:.2f}')
tan = math.tan(math.radians(a))
print(f'O ângulo de {a} tem a tangente de {tan:.2f}')

