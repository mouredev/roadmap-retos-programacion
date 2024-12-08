calendario = """**** **** **** **** **** ****
*01* *02* *03* *04* *05* *06*
**** **** **** **** **** ****
**** **** **** **** **** ****
*07* *08* *09* *10* *11* *12*
**** **** **** **** **** ****
**** **** **** **** **** ****
*13* *14* *15* *16* *17* *18*
**** **** **** **** **** ****
**** **** **** **** **** ****
*19* *20* *21* *22* *23* *24*
**** **** **** **** **** ****
"""

while True:
    print("CALENDARIO ADEVIENTO\n")
    print(calendario)
    dia = input("\nSelecciona el dia que quieres ver: ")
    
    match dia:
        case "01":
            if calendario[31:33] == "**":
                print("Ya has abierto este dia, selecciona otro por favor.\n")
            else:
                print("El regalo del dia (01) es una subscripcion de un mes a una web de cursos.\n")
                calendario = calendario.replace("01", "**")
        case "02":
            if calendario[36:38] == "**":
                print("Ya has abierto este dia, selecciona otro por favor.\n")
            else:
                print("El regalo del dia (02) es una laptop.\n")
                calendario = calendario.replace("02", "**")  
        case "03":
            if calendario[41:43] == "**":
                print("Ya has abierto este dia, selecciona otro por favor.\n")
            else:
                print("El regalo del dia (03) es un carro.\n")
                calendario = calendario.replace("03", "**")
        case "04":
            if calendario[46:48] == "**":
                print("Ya has abierto este dia, selecciona otro por favor.\n")
            else:
                print("El regalo del dia (04) es un viaje a madrid.\n")
                calendario = calendario.replace("04", "**")
        case "05":
            if calendario[51:53] == "**":
                print("Ya has abierto este dia, selecciona otro por favor.\n")
            else:
                print("El regalo del dia (05) es una TV.\n")
                calendario = calendario.replace("05", "**")
        case "06":
            if calendario[56:58] == "**":
                print("Ya has abierto este dia, selecciona otro por favor.\n")
            else:
                print("El regalo del dia (06) es 100$.\n")
                calendario = calendario.replace("06", "**")
        case "07":
            if calendario[121:123] == "**":
                print("Ya has abierto este dia, selecciona otro por favor.\n")
            else:
                print("El regalo del dia (07) es un libro de programacion.\n")
                calendario = calendario.replace("07", "**")
        case "08":
            if calendario[126:128] == "**":
                print("Ya has abierto este dia, selecciona otro por favor.\n")
            else:
                print("El regalo del dia (08) es una PC.\n")
                calendario = calendario.replace("08", "**")
        case "09":
            if calendario[131:133] == "**":
                print("Ya has abierto este dia, selecciona otro por favor.\n")
            else:
                print("El regalo del dia (09) es una pagina web gratis.\n")
                calendario = calendario.replace("09", "**")
        case "10":
            if calendario[136:138] == "**":
                print("Ya has abierto este dia, selecciona otro por favor.\n")
            else:
                print("El regalo del dia (10) es un dominio web.\n")
                calendario = calendario.replace("10", "**")
        case "11":
            if calendario[141:143] == "**":
                print("Ya has abierto este dia, selecciona otro por favor.\n")
            else:
                print("El regalo del dia (11) es un perro.\n")
                calendario = calendario.replace("1", "**")
        case "12":
            if calendario[146:148] == "**":
                print("Ya has abierto este dia, selecciona otro por favor.\n")
            else:
                print("El regalo del dia (12) es un album musical.\n")
                calendario = calendario.replace("12", "**")
        case "13":
            if calendario[211:213] == "**":
                print("Ya has abierto este dia, selecciona otro por favor.\n")
            else:
                print("El regalo del dia (13) es una clase gratis.\n")
                calendario = calendario.replace("13", "**")
        case "14":
            if calendario[216:218] == "**":
                print("Ya has abierto este dia, selecciona otro por favor.\n")
            else:
                print("El regalo del dia (14) es gato.\n")
                calendario = calendario.replace("14", "**")
        case "15":
            if calendario[221:223] == "**":
                print("Ya has abierto este dia, selecciona otro por favor.\n")
            else:
                print("El regalo del dia (15) es una subscripcion de tres meses a una web de cursos.\n")
                calendario = calendario.replace("15", "**")
        case "16":
            if calendario[226:228] == "**":
                print("Ya has abierto este dia, selecciona otro por favor.\n")
            else:
                print("El regalo del dia (16) es un regalo x.\n")
                calendario = calendario.replace("16", "**")
        case "17":
            if calendario[231:233] == "**":
                print("Ya has abierto este dia, selecciona otro por favor.\n")
            else:
                print("El regalo del dia (17) es una foto con el bicho.\n")
                calendario = calendario.replace("17", "**")
        case "18":
            if calendario[236:238] == "**":
                print("Ya has abierto este dia, selecciona otro por favor.\n")
            else:
                print("El regalo del dia (18) es una avioneta.\n")
                calendario = calendario.replace("18", "**")
        case "19":
            if calendario[301:303] == "**":
                print("Ya has abierto este dia, selecciona otro por favor.\n")
            else:
                print("El regalo del dia (19) es nada.\n")
                calendario = calendario.replace("19", "**")
        case "20":
            if calendario[306:308] == "**":
                print("Ya has abierto este dia, selecciona otro por favor.\n")
            else:
                print("El regalo del dia (20) es no se.\n")
                calendario = calendario.replace("20", "**")
        case "21":
            if calendario[311:313] == "**":
                print("Ya has abierto este dia, selecciona otro por favor.\n")
            else:
                print("El regalo del dia (21) es una subscripcion de un mes a una web de cursos.\n")
                calendario = calendario.replace("21", "**")
        case "22":
            if calendario[316:318] == "**":
                print("Ya has abierto este dia, selecciona otro por favor.\n")
            else:
                print("El regalo del dia (22) es una subscripcion de un mes a una web de cursos.\n")
                calendario = calendario.replace("22", "**")
        case "23":
            if calendario[321:323] == "**":
                print("Ya has abierto este dia, selecciona otro por favor.\n")
            else:
                print("El regalo del dia (23) es una subscripcion de un mes a una web de cursos.\n")
                calendario = calendario.replace("23", "**")
        case "24":
            if calendario[326:328] == "**":
                print("Ya has abierto este dia, selecciona otro por favor.\n")
            else:
                print("El regalo del dia (24) es una subscripcion de un mes a una web de cursos.\n")
                calendario = calendario.replace("24", "**")
        case _:
            print("seleccione una opcion valida.\n")
            
