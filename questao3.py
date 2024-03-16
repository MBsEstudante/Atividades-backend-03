def fahrenheit_para_celsius(fahrenheit):
    celsius = 5 * ((fahrenheit - 32) / 9)
    return celsius

def main():
    
    fahrenheit = float(input("Digite a temperatura em graus Fahrenheit: "))

    
    celsius = fahrenheit_para_celsius(fahrenheit)

    
    print("A temperatura em Celsius é:", celsius)

if __name__ == "__main__":
    main()
