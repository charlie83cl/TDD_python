class Package:
    def __init__(self, id, peso, valor, descripcion):
        self.id = id
        self.peso = peso
        self.valor= valor
        self.descripcion = descripcion

    def calculo_impuesto(self):
        if self.valor > 30:
            derecho_aduanero = self.valor * 0.06
            seguro = self.valor * 0.02
            iva = self.valor * 0.19
            impuesto = derecho_aduanero + seguro + iva
            return impuesto
        return 0
    
    def info_package(self):
        return f"ID:{self.id} | Descripcion: {self.descripcion} | Peso:{self.peso}Kg. | Valor: ${self.valor} | Impuestos: {self.calculo_impuesto()}"
        