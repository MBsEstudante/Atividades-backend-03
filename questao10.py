def main():
    
    nome = input("Digite o nome: ")
    telefone = int(input("Digite o telefone: "))

    
    print("Saída com vírgula:", nome, ",", telefone)

    
    print("Saída com concatenação: " + nome + ", " + str(telefone))

    
    print(f"Saída com f-string: {nome}, {telefone}")

    
    print("Saída com format: {}, {}".format(nome, telefone))

if __name__ == "__main__":
    main()
