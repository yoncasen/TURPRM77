import random 

characters = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

number = int(input("Parolanın uzunluğu kaç olsun?"))

password = ""

for i in range(number):
  character = random.choice(characters)
  password += character
  #password += random.choice(characters)

print("Parola:", password)

