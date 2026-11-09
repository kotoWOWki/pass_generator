import secrets

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
        
chars = []
for i in range(length - 4):
    chars.append(secrets.choice(alphabet))
    
chars = guaranteed + chars
    
rng = secrets.SystemRandom()
rng.shuffle(chars)    
password = "".join(chars)              
    
print(password)