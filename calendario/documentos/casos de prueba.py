#título          :casos de prueba.py
#descripción     :ejemplo comparativo de casos de prueba para precio.
#autor           :Benjamín Valdés
#python_version  :3.5.2  
#===============================================================

# este programa de ejemplo que presenta como crear 
# casos de prueba para una función


#funcion regreasa True o False
def precio(val):
    if(val > 0):
        return True
    else:
        return False
        
#para que el caso de prueba sea exitoso, las salidas deben ser iguales
#puedes incluir segmentos de código como estos en comentarios
# o ponerlos en otros archivos para hacer pruebas automáticas.
print("caso 1 valor %i,  es %r debe ser %r" % (6 ,precio(6), True))
print("caso 2 valor %i,  es %r debe ser %r" % (10000 ,precio(10000), True))
print("caso 3 valor %f,  es %r debe ser %r" % (10.5 ,precio(10.5), True))
print("caso 4 valor %f,  es %r debe ser %r" % (0.1 ,precio(0.1), True))
print("caso 5 valor %i,  es %r debe ser %r" % (0 ,precio(0), False))
print("caso 6 valor %i,  es %r debe ser %r" % (0.0 ,precio(0), False))
print("caso 7 valor %i,  es %r debe ser %r" % (-10 ,precio(-10), False))


#cuando sepas usar condicionales correctamente 
#puedes hacer cosas más avanzadas como: 

pruebas = 0
if precio(6) == True:
    pruebas = pruebas + 1
    print("caso 1 valor %i,  es %r debe ser %r" % (6 ,precio(6), True))
if precio(10000)== True:
    pruebas = pruebas + 1
print("caso 2 valor %i,  es %r debe ser %r" % (10000 ,precio(10000), True))
if precio(10.5)==True:
    pruebas = pruebas + 1
    print("caso 3 valor %f,  es %r debe ser %r" % (10.5 ,precio(10.5), True))
if precio(0.1)== True:
    pruebas = pruebas + 1
    print("caso 4 valor %f,  es %r debe ser %r" % (0.1 ,precio(0.1), True))
if precio(0)== False:
    pruebas = pruebas + 1
    print("caso 5 valor %i,  es %r debe ser %r" % (0 ,precio(0), False))
if precio(0)== False:
    pruebas = pruebas + 1
    print("caso 6 valor %i,  es %r debe ser %r" % (0.0 ,precio(0), False))
if precio(-10)== False:
    pruebas = pruebas + 1
    print("caso 7 valor %i,  es %r debe ser %r" % (-10 ,precio(-10), False))

print("pasaron ", pruebas, " de 7 pruebas")



