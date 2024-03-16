def main():
    
    numero = int(input("Digite um número inteiro: "))

    
    tamanho = 8 

   
    numero_formatado = f"{numero:0{tamanho}d}"

    
    print("Número formatado:", numero_formatado)

if __name__ == "__main__":
    main()
