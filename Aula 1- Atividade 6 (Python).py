cpf = str(input("Digite os números do seu CPF: "))
nome= str(input("Digite somente seu nome: "))
sobrenome= str(input("Digite seu sobrenome: "))
valor1= float(input("A quantia do valor da venda do Fiat Uno 99 é: "))
valor2= float(input("A quantia do valor da venda da moto X1 é: "))
valor3=(valor1+valor2)

print(cpf+"/"+nome+" "+sobrenome)
print("A quantidade de digitos do seu CPF é:", len(cpf))
print("A ultima letra do nome é: ", nome[-1])
print("Eu " ,nome+" "+sobrenome, " do documento " ,cpf, " declaro que recebi no mês de novembro"
      " a quantia de " ,valor1, " na venda do Fiat Uno 99 e a quantia de" ,valor2, " na venda da moto x1, somando a quantia de: " ,valor3, )