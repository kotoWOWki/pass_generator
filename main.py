import secrets

password = ""
chars = []

LOWERCASE = "abcdefghijklmnopqrstuvwxyz"
UPPERCASE = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
DIGITS = "0123456789"
SYMBOLS = "!@#$%^&*()-_=+"

alphabet = LOWERCASE + UPPERCASE + DIGITS + SYMBOLS

while True:
    try:
        length = int(input("Введите количество символов из которого должен состоять пароль: "))
        if length < 8:
            print("Длина должна быть не меньше 8!")
            continue
        break
    except ValueError:
        print("Введите число!")
        
guaranteed = [
    secrets.choice(LOWERCASE),
    secrets.choice(UPPERCASE),
    secrets.choice(DIGITS),
    secrets.choice(SYMBOLS),
]        
        
rest = []
for i in range(length - 4):
    rest.append(secrets.choice(alphabet))
    
chars = guaranteed + rest    
    
rng = secrets.SystemRandom()
rng.shuffle(chars)    
password = "".join(chars)              
    
print(password)