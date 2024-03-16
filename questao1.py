def calcular_area_do_circulo(raio):
    
    area = 3.14 * (raio ** 2)
    return area

def main():
    
    raio = float(input("Digite o raio do círculo: "))

    
    area = calcular_area_do_circulo(raio)

    
    print("A área do círculo com raio", raio, "é:", area)

if __name__ == "__main__":
    main()
