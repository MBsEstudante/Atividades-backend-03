def calcular_salario(horas_trabalhadas, valor_por_hora):
    
    salario = horas_trabalhadas * valor_por_hora
    return salario

def main():
    
    valor_por_hora = float(input("Digite o valor ganho por hora: "))
    horas_trabalhadas = float(input("Digite o número de horas trabalhadas no mês: "))

    
    salario_mensal = calcular_salario(horas_trabalhadas, valor_por_hora)

   
    print("O salário mensal é:", salario_mensal)

if __name__ == "__main__":
    main()
