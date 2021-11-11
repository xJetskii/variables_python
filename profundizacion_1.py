# Tipos de variables [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

# Ejercicios de práctica con números
'''
Enunciado:
Realice un calculadora, se ingresará por línea de comando dos
números reales y se deberá calcular todas las operaciones entre ellos:
A) Suma
B) Resta
C) Multiplicación
D) División
E) Exponente/Potencia

- Para todos los casos se debe imprimir en pantalla el resultado aclarando
  la operación realizada en cada caso y con que números
  se ha realizado la operación
  ej: La suma entre 4.2 y 6.5 es 10.7
'''

print('¡Nuestra primera calculadora!')
# Empezar aquí la resolución del ejercicio
print('Ingrese el primer numero:')
numero1 = float(input())
print('Ingrese el segundo numero:')
numero2 = float(input())
suma = numero1 + numero2
resta = numero1 - numero2
multi = numero1 * numero2
divi = numero1 / numero2
exp = numero1 ** numero2

print('El resultado de sumar:' ,numero1, 'y' ,numero2, 'es:' ,suma)
print('El resultado de restar:' ,numero1, 'y' ,numero2, 'es:' ,resta)
print('El resultado de multiplicar:' ,numero1, 'y' ,numero2, 'es' ,multi)
print('El resultado de dividir:' ,numero1, 'y' ,numero2, 'es' ,divi)
print('El resultado de potenciar:' ,numero1, 'y' ,numero2, 'es' ,exp)