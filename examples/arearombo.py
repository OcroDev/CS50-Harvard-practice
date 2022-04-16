def decoradora1 (funcion_parametro):
    def interna(*args, **kwargs):
        print("area del rombo perfecto")
        global mult
        mult = 2
        funcion_parametro(*args, **kwargs)
        print("fin de la operacion")
    return interna

@decoradora1
def area_rombo(base, h=float):
    global mult
    print(((base*h)/2)*2)

area_rombo(3,7.2)


