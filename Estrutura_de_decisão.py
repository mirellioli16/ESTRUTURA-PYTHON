print("Testando o comando IF (Digite um núm menor de 18:)")
valor = int(input("Qual sua Idade? "))
if valor < 18:
    print("Você ainda não pode dirigir!")
#------------------------#--------------------#
print("\n")
print("Testando o comando IF..ELSE(Se....Senão)")
valor = int(input("Qual sua idade "))
if valor < 18:
    print("Você ainda não pode dirigir!")
else:
    print("Você pode dirigir!")
    #-------------------#---------------------#
print("\n")
print("Testando o comando IF...ELIF..ELSE(Se..Senão..Senão se)")
valor = int(input("Qual sua idade? "))
if valor < 6:
    print("Que coisa fofa!")
elif valor < 18:
    print("Você ainda não pode dirigir!")
elif valor > 60:
    print("Você está na melhor idade!")
else:
    print("Você pode dirigir!")
