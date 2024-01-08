from cryptography.fernet import Fernet

# Функция для генерации ключа шифрования
def generate_key():
    return Fernet.generate_key()

# Функция для шифрования пароля
def encrypt_password(key, password):
    cipher_suite = Fernet(key)
    encrypted_password = cipher_suite.encrypt(password.encode())
    return encrypted_password

# Генерация ключа шифрования (ключ должен храниться в безопасном месте)
encryption_key = generate_key()
# Пароль, который нужно сохранить
original_password = "Moresrv1"

# Шифрование пароля
encrypted_password = encrypt_password(encryption_key, original_password)

# Демонстрация зашифрованного пароля
key_string = encryption_key.decode()
password_string = encrypted_password.decode()
with open('pass1.txt','w') as file:
    file.write(f"Key : {key_string}\n")
    file.write(f"pass : {password_string}")