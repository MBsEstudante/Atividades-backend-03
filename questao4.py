def main():
    nome = input("Digite o nome da pessoa: ")
    idade = int(input("Digite a idade da pessoa: "))
    nacionalidade = input("Digite a nacionalidade da pessoa: ")
    hobby = input("Digite o hobby da pessoa: ")

    print(f"Nome: {nome},")
    print(f"Idade: {idade}")
    print("Nacionalidade: {}".format(nacionalidade))
    print("Hobby: " + hobby + f", {nome}, {idade}, {nacionalidade}")

if __name__ == "__main__":
    main()
