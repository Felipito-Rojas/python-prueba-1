def paga(rango):
    if rango%0.2 == 0:
        money=round(rango*2400,2)
        print("tu rango actual es "+str(rango)+" por lo cual tu ganancia es de "+str(money)+"€")
        return(money)
    else:
        print("rango ingresado incorrecto")

def main():
    rank=float(input("ingrese su rango actual: "))
    if rank < 0.4:
        paga(rank)
        print("inaceptable")
    elif rank == 0.4:
        paga(rank)
        print("aceptable")
    else:
        paga(rank)
        print("meritorio")

if __name__ == '__main__': #punto de entrada
    main()