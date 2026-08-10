# Qodo: Test this class
class Carro:
    # Qodo: Test this method
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    # Qodo: Test this method
    def exibir_info(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}"

# meu_carro = Carro("Chevrolet", "Camaro")
meu_carro = Carro("Ford", "Mustang")
print(meu_carro.exibir_info())