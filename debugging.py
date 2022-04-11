def divisors(num):
    divisors = []
    for i in range (1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors

def palindrome(string):
    return string == string[::-1]

def fibonacci():
    # Fibonacci series:
    # the sum of two elements defines the next
    a, b = 0, 1
    while a < 10:
        print(a)
        a, b = b, a + b

def run():
    try:
        num = int(input("Ingrese un numero: "))
        print(divisors(num))
        print("Terminó el programa.")

        #print(palindrome('ana'))
        #fibonacci()
    except ValueError: 
        print('Debes ingresar un numero')


if __name__ == '__main__':
    run()