#Crear un diccionario que permita guardar los precios de diversas frutas
'''El código pedirá el nombre de la fruta y la cantidad que se ha vendido y mostrará el precio final
de la fruta a partir de los datos guardados en el diccionario. Si la fruta no existe mostrará un error.
Finalmente cada vez que consultemos, el programa nos preguntará si deseamos realizar otra consulta'''

precios = {"Manzana":1, "Pera":2, "Fresa":3, "Sandía":4}
while True:
    fruta = input("Favor digitar la fruta que ha vendido:").capitalize()
    if fruta not in precios:
        print ("Esa fruta no está en el inventario")
    else:
        cantidad = int(input("Coloque la cantidad de fruta que has vendido: "))
        print ("Total a pagar: ", cantidad*precios[fruta])
    opcion = input("Deseas vender otra futa? (s/n): ").lower()
    if opcion == "n":
        print ("Gracias por su compra")
        break
    else: 
        True
