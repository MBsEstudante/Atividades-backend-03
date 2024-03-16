def formatar_para_dinheiro(numero):
    
    valor_formatado = "{:,.2f}".format(numero)
    
    valor_formatado = "R$ " + valor_formatado
    return valor_formatado

def main():
    
    numero_decimal = float(input("Digite um número decimal: "))

    
    valor_monetario = formatar_para_dinheiro(numero_decimal)

    
    print("Valor em dinheiro:", valor_monetario)

if __name__ == "__main__":
    main()
