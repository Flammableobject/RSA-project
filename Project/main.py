import AES as AES
import RSA as RSA


def RSA_encrypt(password, Public_Key):
    e, N = Public_Key
    intpassword = int.from_bytes(password.encode('utf-8'), byteorder='big')
    print("plain password =")
    print(intpassword)
    encrypted_key = effModuloExp(intpassword, e, N)
    return encrypted_key


def RSA_decrypt(encrypted_key, Private_Key):
    d, N = Private_Key
    decrypted_key = effModuloExp(encrypted_key, d, N)
    return decrypted_key


def effModuloExp(a, n, m):
    r = 1
    while n > 0:
        if n & 1 == 1:
            r = (r * a) % m
        a = (a * a) % m
        n >>= 1
    return r


def main():
    inputtext = input("enter text:")
    password = input("Password: ")
    print(".................................................")
    # First let us encrypt secret message(AES)
    encrypted_Message = AES.encrypt(inputtext, password)
    print(encrypted_Message)  # encrypted AES message & password
    Public_Key, Private_Key = RSA.RSA_keygen()
    encrypted_key = RSA_encrypt(password, Public_Key)
    print(".................................................")
    print("encrypted_key =")
    print(encrypted_key)  # encrypted RSA only password
    decrypted_key = RSA_decrypt(encrypted_key, Private_Key)
    print(".................................................")
    print("decrypted_key =")
    print(decrypted_key)
    print("Public key = (e,n) = ", Public_Key)
    print("Private key = (d,n) = ", Private_Key)
    print(".................................................")
    # Let us decrypt using our original password
    decrypted_key_text = int.to_bytes(decrypted_key, length=len(
        password), byteorder='big').decode('utf-8')
    decrypted = AES.decrypt(encrypted_Message, decrypted_key_text)
    print("decrypted message = " + bytes.decode(decrypted))


main()
