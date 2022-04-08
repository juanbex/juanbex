from functools import reduce


def run():
    
    def saludo(func):
        func()

    def hola():
        print("Hola!!")

    def adios():
        print("Adios!!")

    saludo(hola)
    saludo(adios)

    #Funciones de orden superior 
    # 1. Filter
    my_list = [1, 4, 5, 6, 9, 13, 19, 21]

    odd = list(filter(lambda x: x%2 != 0, my_list))
    

    #2. Map
    my_list_2 = [1, 2, 3, 4, 5]
    squares = list(map(lambda x: x**2, my_list_2))

    #3. Reduce

    my_list_3 = [2, 2, 2, 2, 2]
    all_multipled = reduce(lambda a, b: a * b, my_list_3)

    #Imprimimos en pantalla
    print(all_multipled)


if __name__ == '__main__':
    run()