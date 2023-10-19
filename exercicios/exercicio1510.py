#-*- coding: utf-8 -*-

# Primeira passo saber a velocidade do veículo

veloc = float(input('Qual a velocidade do carro?: '))


# Segundo passo criar as condições

if veloc == 0:
    print('Carro esta parado')
else:
    if veloc >=1 and veloc <=20:
        print('Esta na primeira marcha')
    else:
        if veloc >=21 and veloc <=40:
            print('O carrro esta em segunda marça')
        else:
            if veloc >=41:
                print('O carro esta na terceira marcha')