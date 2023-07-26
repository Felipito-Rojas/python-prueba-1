def main():
    fech_nacimineto=input("Ingrese su fecha de nacimiento (dd/mm/aaaa): ")
    dia=fech_nacimineto[:2]
    mes=fech_nacimineto[3:5]
    anno=fech_nacimineto[6:]
    print("Dia: "+dia+"\nMes: "+mes+"\nAÑO: "+anno)

if __name__ == '__main__': #punto de entrada
    main()