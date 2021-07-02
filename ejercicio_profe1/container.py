from package import Package


class Container:
    def __init__(self, capacidad_max, packages = []):
        self.capacidad_max = capacidad_max
        self.packages = packages

    def obtener_peso(self):
        sumaPesos = 0
        for paquete in self.packages: # por cada paquete que va a la lista contenedor, necesito sumar el peso de todos juntos
            sumaPesos += paquete.peso
        return sumaPesos
    
    def subir_paquete(self, new_package):
        if self.capacidad_max - self.obtener_peso() >= new_package.peso:
            self.packages.append(new_package)
            return True
        return False

    def eliminar_paquete(self, id):
        for paquete in self.packages:
            if paquete.id == id:
                print(paquete.info_package())
                self.packages.remove(paquete)
                return True
        return False

    def agregar_impuesto(self):
        sumaImpuestos = 0
        for paquete in self.packages:
            sumaImpuestos += paquete.calculo_impuesto()
        return sumaImpuestos
        