# def divisao(a, b):
#     try:
#         print(a/b)
#     except Exception as e:
#         print('Divisão inválida')
#         print(e)

# divisao(2, 0)


try:
    a = float(input('Digite o numero A: ')) #ValueError
    b = float(input('Digite o numero B: '))

    print(a/b)  #ZeroDivisionError

except ValueError as error:
    print('Input inválido, digite apenas números.')
except ZeroDivisionError as error:
    print('Não pode ser feita divisão por zero.')
except Exception as error:
    print('Algum erro ocorreu')
    print(error)    
finally:
    print('Fim do programa')