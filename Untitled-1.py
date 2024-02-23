A = 6
B = 10
H = int(input ("Сколько спит Аня?"))
if H < A:
    print("Недосып")
elif H > B:
    print("Пересып")
if H >= A and H <= B:
    print("Норма")