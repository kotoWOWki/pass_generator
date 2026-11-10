import secrets

chars = []

LOWERCASE = "abcdefghijklmnopqrstuvwxyz"
UPPERCASE = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
DIGITS = "0123456789"
SYMBOLS = "!@#$%^&*()-_=+"

alphabet = LOWERCASE + UPPERCASE + DIGITS + SYMBOLS

while True:
    try:
        raw = input("Введите количество символов из которого должен состоять пароль (Выйти — 'x'): ")
        if raw.lower() == "x":
            print("Благодарю за использование!")
            break
        length = int(raw)    
        if length < 8:
            print("Длина должна быть не меньше 8!")
            continue
        elif length >=129:
            print("Длина не должна превышать 128 символов!")
            continue
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
        print(f"\nВаш пароль: {password} состоящий из {length} символов\n")    
    except ValueError:
        print("Введите число!")