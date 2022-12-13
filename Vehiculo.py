import pickle


class Vehiculo:
    def __init__(self, modelo, color, puertas):
        self.modelo = modelo
        self.color = color
        self.puertas = puertas

    def __str__(self):
        return f'Mi carro es {self.modelo} {self.color} {self.puertas} de puertas'


vehiculo = Vehiculo('Toyota', 'Azul', 4)
print(vehiculo)

with open('vehiculo.pkl', 'wb') as file:
    pickle.dump(vehiculo, file)
with open('vehiculo.pkl', 'rb') as file:
    vehiculo = pickle.load(file)
    print(vehiculo, file)
