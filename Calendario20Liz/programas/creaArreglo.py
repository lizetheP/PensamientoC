def creaLista(tam):
    lista = []
    for i in range(0,tam):
        lista.insert(i,i)
    return lista
        
t = int(input("Introduce el tamaño de la lista: "))        
A = creaLista(t)
print(A)

