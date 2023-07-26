def area_circulo():
    radio=int(input("ingrese el radio: "))
    area=3.14*(radio**2)
    return(area)

def vol_cilindro():
    area_ci=area_circulo()
    altura=int(input("ingrese la altura:"))
    volumen=area_ci*altura
    return(volumen)

def main():
    opcion=int(input("""que desea calcular: 
                    (1)area circulo
                    (2)volumen cilindro
                    (3)salir
                    """))
    if opcion == 1:
        resultado=area_circulo()
        print("el area del circulo es: "+str(resultado))
    elif opcion == 2:
        resultado=vol_cilindro()
        print("el volumen del cilindro es de: "+str(round(resultado,2)))
    else:
        print("QUE tenga buien dia")

if __name__ == '__main__': #punto de entrada
    main()