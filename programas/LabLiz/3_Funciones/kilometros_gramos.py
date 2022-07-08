def kilometros_millas(km):
    return km / 1.6

def gramos_onzas(gramos):
    return gramos / 28.35

def going_to_usa(km, gramos):
    millas = kilometros_millas(km)
    onzas = gramos_onzas(gramos)
    return millas, onzas

def main():
    km = float(input("Introduce los kilómetros: "))
    gramos = float(input("Introduce los gramos: "))
    millas, onzas = going_to_usa(km, gramos)
    print("Millas = %.2f y Onzas = %.2f" % (millas, onzas))

main()
