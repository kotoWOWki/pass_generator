import secrets
password = ""

while True:
    try:
        length = int(input("Введите количество символов из которого должен состоять пароль: "))
        if length <= 0:
            print("Длина должна быть больше нуля!")
            continue
        break
    except ValueError:
        print("Введите число!")
        
for i in range(length):
    password += secrets.choice("abcdefghijklmnopqrstuvwxyz0123456789")
    
print(password)