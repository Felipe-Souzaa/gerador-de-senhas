import random
import time

caracteres = "qwertyuiopasdfghjklçzxcvbnmQWERTYUIOPASDFGHJKLÇZXCVBNM1234567890!@#$%¨&*()_-+="

num_senha = int(input("Informe a quantidade de senhas: "))
tam = int(input("Informe o tamanho da senha: "))

print("Suas senhas estão feitas abaixo...")

for i in range(num_senha):
    senha = ""
    for t in range(tam):
        senha += random.choice(caracteres)
    time.sleep(1)
    print(senha)
