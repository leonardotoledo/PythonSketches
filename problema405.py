# def contaDigitosPares(number):
#     sum = 0
#     for i in range(len(number)):
#         if int(number[i])%2==0:
#             sum+=1
#     return sum

def contaDigitosPares(number):
    sum = 0
    i=0
    while i<len(number):
        if int(number[i])%2==0:
            sum +=1
        i += 1
        contaDigitosPares(number[i:len(number)])
    return sum

numero = input()
print(contaDigitosPares(numero))