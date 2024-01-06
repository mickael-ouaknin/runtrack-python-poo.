class Operation:
    def __init__(self, nombre1, nombre2):
        self.nombre1 = nombre1
        self.nombre2 = nombre2

    def print_values(self):
        print("Le nombre1 est", self.nombre1)
        print("Le nombre2 est", self.nombre2)

operation = Operation(12, 3)
operation.print_values()