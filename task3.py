#Гасимова Аміна 141 група
#Лабораторна робота 3
#15Дано ціле число N (> 0). Послідовність дійсних чисел AK визначається наступним чином:
#A0 = 1, AK = (AK-1 + 1) / K, K = 1, 2, ....Вивести елементи A1, A2, ..., AN.

n = int(input("Введіть ціле число N > 0: "))
a_0 = 1
i = 1
Ak = 0
rez = 0
if n > 0:
    for i in range(1,(n+1)):
        Ak = (a_0+1)/i
        a_0 = Ak
        print("A",i,": ", Ak)
else:
    print("Помилка!Введіть ціле число N > 0")