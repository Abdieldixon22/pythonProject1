def linea(car,tam):
    print(car*tam)


def cuadro(car, nfil, ncol):
    linea(car, ncol)
    for i in range(nfil-2):
        print(car + ' '*(ncol-2) + car)
    linea(car, ncol)
