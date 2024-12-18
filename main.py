# Generating function
def fibonacci(l):
    print("Generowanie ciągu, proszę czekać....")
    string = [1,1]
    i = 2
    while i in range(l+3):
        # print(i)
        # j = i-1
        # print(string[j])
        # j = i-2
        # print(string[j])
        string.append(string[i-1] + string[i-2])
        i+= 1
    print(*string)




#CLI
print("Witaj w generatorze ciągu liczb Fibonacciego")
lenght = int(input("Jaką długość ma mieć ciąg? :"))

# Unexpected value handler:
if lenght <1:
    print("Niepoprawna wartość, spróbój ponownie!")
else:
    lenght = lenght - 3
    fibonacci(lenght)