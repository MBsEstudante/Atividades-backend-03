def main():
   
    numero_inteiro = int(input("Digite um número inteiro: "))

    
    numero_decimal = float(input("Digite um número decimal: "))

    
    texto = input("Digite um número em texto: ")

    
    numero_inteiro_decimal = float(numero_inteiro)

    
    numero_decimal_texto = str(numero_decimal)

    
    texto_inteiro = int(texto)

    # Imprime os resultados e suas classificações de tipo
    print("Número inteiro convertido para decimal:", numero_inteiro_decimal, "| Tipo:", type(numero_inteiro_decimal))
    print("Número decimal convertido para texto:", numero_decimal_texto, "| Tipo:", type(numero_decimal_texto))
    print("Texto convertido para inteiro:", texto_inteiro, "| Tipo:", type(texto_inteiro))

if __name__ == "__main__":
    main()
