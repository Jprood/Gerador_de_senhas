import random
import string

choice_user = input("Quantos dígitos a senha deve ter? ")
type_pass = input("Você deseja uma senha numérica (N) ou alfanumérica (A)? ")

if choice_user.isdigit():
    choice_user = int(choice_user)
else:
    print("Valor inválido!")
    quit()

def password_generator(len_pass=8, ptype='A'):
    ascii_options = string.ascii_letters
    number_options = string.digits
    punct_options = string.punctuation

    if ptype == 'N':
        options = number_options
    else:
        options = ascii_options + number_options + punct_options

    password_user = ""

    for i in range(0, len_pass):
        digit = random.choice(options)
        password_user = password_user + digit

    return password_user

response = password_generator(len_pass = choice_user, ptype = type_pass)

print(f"Senha gerada:\n{response}")
