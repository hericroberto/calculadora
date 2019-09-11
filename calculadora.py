#Complete as funcoes a seguir

def soma(a, b):
	#Insira o codigo aqui
  print(a+b)

def subtrai(a, b):
  print(a-b)

def multiplica(a, b):
  print(a*b)

def divide(a, b):
  if b == 0:
    print('"b" não pode ser 0')
  else:
    print(a/b)

#Programa principal

print("Calculadora simples")

num1 = float(input("Insira o primeiro numero: "))
num2 = float(input("Insira o segundo numero: "))



soma(num1, num2)
subtrai(num1, num2)
multiplica(num1, num2)
divide(num1, num2)

