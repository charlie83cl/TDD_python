from package import Package
from container import Container

contenedor = Container(100)
package1 = Package("SCL001", 20.5,2000,"Respuestas Bicicleta")
package2 = Package("SCL002", 10,10000,"Respuestas Ferrari")
package3 = Package("SCL003", 10,25500,"Respuestas Mercedez")
package4 = Package("VAP001", 10,2000,"Respuestas Camioneta")
package5 = Package("SCL001", 10,15,"Respuestas Jeepeta")
package6 = Package("VAP002", 10,20000,"Respuestas Maquinon")
package7 = Package("IQQ001", 10,280000,"Respuestas Mustang")


print("="*100)
print("TE PEGAREMOS EL ADUANAZO HIJO")
print("="*100)
print('Se agrego el paquete!!!' if contenedor.subir_paquete(package1) == True else 'Algun problema tuvo tu Drop')
print('Se agrego el paquete!!!' if contenedor.subir_paquete(package2) == True else 'Algun problema tuvo tu Drop')
print('Se agrego el paquete!!!' if contenedor.subir_paquete(package3) == True else 'Algun problema tuvo tu Drop')
print('Se agrego el paquete!!!' if contenedor.subir_paquete(package4) == True else 'Algun problema tuvo tu Drop')
print('Se agrego el paquete!!!' if contenedor.subir_paquete(package5) == True else 'Algun problema tuvo tu Drop')
print('Se agrego el paquete!!!' if contenedor.subir_paquete(package6) == True else 'Algun problema tuvo tu Drop')
print('Se agrego el paquete!!!' if contenedor.subir_paquete(package7) == True else 'Algun problema tuvo tu Drop')
print("="*100)
print()

print("="*100)
print("ESTO ES LO QUE PODRAS PASAR NOMAS HIJO")
print("="*100)

print('Esta es la Impresion de todos los Paquetes que existen en el contenedor')
for paquetillo in contenedor.packages:
    print(paquetillo.info_package())


print("="*100)
print()
print("="*100)
print("VOY A ELIMINARTE UN DROP HIJO EL (VAP002)")
print("Eliminado el Drop" if contenedor.eliminar_paquete("VAP002") == True else "NO SE ENCONTRO EL DROP ELIMINADO")
print("VOY A ELIMINARTE UN DROP HIJO EL (VAP008)")
print("Eliminado el Drop" if contenedor.eliminar_paquete("VAP008") == True else "NO SE ENCONTRO EL DROP ELIMINADO")

print("="*100)
print()
print("="*100)
print("Determinar el total de impuestos por pagar")
print(contenedor.agregar_impuesto())