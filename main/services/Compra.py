from main.repositories import CompraRepository

compra_repository = CompraRepository()

class CompraService:

    def obtener_compra_con_descuento(self, id):
        compra = compra_repository.find_one(id)
        # Aca podria agregarle algun tipo de logica a la compra para calcular el descuento
        # compra.total = compra.total - (compra.total * 0.1)
        return compra

    def agregar_compra(self, compra):
        # Agregar logica antes de guardar fisicamente la compra en la db
        compra = compra_repository.create(compra)
        return compra
