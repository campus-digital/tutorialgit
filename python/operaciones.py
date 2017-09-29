#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
  Funcion suma
'''
def suma(a,b):
    return a+b
'''
Se 
generan
comentarios mezclados
en
las 
funciones
Suma
y 
Resta
utilizando
la 
misma
rama
desarrollo
'''

'''
  Funcion resta
'''
def resta(a,b):
    '''
       hjsdgfhjs
       kjsghdfhdsf
       hsgdfhjgds
       kjshdfjkhsdf
       kjsdhfjkhsdf
       ksjdhfkjhdsf
    '''
    return (a-b)


'''
  Funcion multiplicación
'''
def multiplicacion(a,b):
    return a*b

'''
  Funcion division
'''
def division(a,b):
    return 0


'''
  Funcion potencia
'''
def potencia(a,b):
    return 0


'''
  Funcion factorial
'''
def factorial(a):
    return 0


'''
  Funcion logaritmo
'''
def logaritmo(a):
    return 0


'''
  Funcion seno
'''
def seno(a):
    return 0


'''
  Funcion coseno
'''
def coseno(a):
    return 0


'''
  Funcion tangente
'''
def tangente(a):
    return 0


'''
  Funcion principal
'''
def main():
    print('Operaciones matematicas basicas. Ingrese una opción del menu:')
    print(' 1) Suma')
    print(' 2) Resta')
    print(' 3) Multiplicación')
    print(' 4) División')
    print(' 5) Potencia')
    print(' 6) Factorial')
    print(' 7) Logaritmo')
    print(' 8) Seno')
    print(' 9) Coseno')
    print('10) Tangente')
    try:
        menu = raw_input('Escoge una opción: ')
        opcion = int(menu)
    except ValueError:
        print('El valor ingresado no es numerico')
    if(opcion == 1):
        try:
            numa = raw_input('Número A: ')
            a = int(numa)
            numb = raw_input('Número B: ')
            b = int(numb)
            print('Suma: %d' % suma(a,b))
        except ValueError:
            print('Error en la suma, el valor ingresado no es numerico')
    elif(opcion == 2):
        try:
            numa = raw_input('Número A: ')
            a = int(numa)
            numb = raw_input('Número B: ')
            b = int(numb)
            print('Resta: %d' % resta(a,b))
        except ValueError:
            print('Error en la resta, el valor ingresado no es numerico')
    elif(opcion == 3):
        try:
            numa = raw_input('Número A: ')
            a = int(numa)
            numb = raw_input('Número B: ')
            b = int(numb)
            print('Multiplicacion: %d' % multiplicacion(a,b))
        except ValueError:
            print('Error en la multiplicacion, el valor ingresado no es numerico')
    elif(opcion == 4):
        try:
            numa = raw_input('Número A: ')
            a = int(numa)
            numb = raw_input('Número B: ')
            b = int(numb)
            print('Division: %d' % division(a,b))
        except ValueError:
            print('Error en la division, el valor ingresado no es numerico')
    elif(opcion == 5):
        try:
            numa = raw_input('Número A: ')
            a = int(numa)
            numb = raw_input('Número B: ')
            b = int(numb)
            print('Potencia: %d' % potencia(a,b))
        except ValueError:
            print('Error en la potencia, el valor ingresado no es numerico')
    elif(opcion == 6):
        try:
            numa = raw_input('Número A: ')
            a = int(numa)
            print('Factorial: %d' % factorial(a))
        except ValueError:
            print('Error en el factorial, el valor ingresado no es numerico')
    elif(opcion == 7):
        try:
            numa = raw_input('Número A: ')
            a = int(numa)
            print('Logaritmo: %d' % logaritmo(a))
        except ValueError:
            print('Error en el logaritmo, el valor ingresado no es numerico')
    elif(opcion == 8):
        try:
            numa = raw_input('Número A: ')
            a = int(numa)
            print('Seno: %d' % seno(a))
        except ValueError:
            print('Error en el seno, el valor ingresado no es numerico')
    elif(opcion == 9):
        try:
            numa = raw_input('Número A: ')
            a = int(numa)
            print('Coseno: %d' % coseno(a))
        except ValueError:
            print('Error en el coseno, el valor ingresado no es numerico')
    elif(opcion == 10):
        try:
            numa = raw_input('Número A: ')
            a = int(numa)
            print('Tangente: %d' % tangente(a))
        except ValueError:
            print('Error en la tangente, el valor ingresado no es numerico')


if __name__ == '__main__':
    main()
