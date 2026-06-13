import math as M

#Se calcula el area del circulo multiplicando pi por el cuadrado del radio
def AreaCirculo(radio):
    """
    Calcula el área de un círculo utilizando su radio.

    Parámetros:
        radio (int o float): Radio del círculo.

    Retorna:
        float: Área del círculo calculada.

    Excepciones:
        TypeError: Si el radio no es un número.
        ValueError: Si el radio es negativo.
    """

    if not isinstance(radio, (int, float)):
        raise TypeError("El radio debe ser un número")

    if radio < 0:
        raise ValueError("El radio no puede ser negativo")

    area = M.pi * radio ** 2
    return area

#Menu de la aplicacion
def main():
    print("")
    print("===== Area Circulo =====")
    print("=== Escoge una opcion ===")
    print("")
    print("[1]. Calcular area")
    print("[9]. Salir")
    print("")

    option = input("Opcion: ")
    #Opcion de Cierre de la aplicacion
    if option == "9":
        return
    

    if option == "1":
        try:
            #Numero que la persona da para el calculo
            radio = float(input("Escriba el radio: "))
            resultado = AreaCirculo(radio)

        except ValueError as error:
            print(f"Error: {error}")
            
    else:
        print("Opcion invalida")
        return main()
    #La escritura del resultado
    print(f" Resultado: {resultado}")
    return main()

if __name__ == "__main__": main()