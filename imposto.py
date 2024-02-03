print("Qual o valor do seu salario?")
salario = float(input())

print("Qual a porcentagem do imposto?")
imposto = float(input())

porcentagem_imposto = (imposto / 100)

def IMP(salario, porcentagem_imposto):
    return (salario * porcentagem_imposto)

print(f"O valor do seu imposto é {IMP(salario, porcentagem_imposto)}")
