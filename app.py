from calculator import sumar,restar,Dividir,Multiplicar

def main():
    print("")
    print("===== Calculadora =====")
    print("== Escoge una opcion ==")
    print("")
    print("[1]. Sumar")
    print("[2]. Restar")
    print("[3]. Dividir")
    print("[4]. Multiplicar")
    print("[9]. Salir")
    print("")
    
    option = input("Opcion: ")

    if option == "9":
        return
    
    a = float(input("Escriba un numero: "))
    b = float(input("Escriba otro numero: "))
    
    if option == "1":
        resultado = sumar(a,b)
    elif option == "2":
        resultado = restar(a,b)
    elif option == "3":
        resultado = Dividir(a,b)
    elif option == "4":
        resultado = Multiplicar(a,b)
    else:
        print("Opcion invalida")
        return main()
    
    print(f" Resultado: {resultado}")
    return main()

if __name__ == "__main__": main()