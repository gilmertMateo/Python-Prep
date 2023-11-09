class Funciones:
    def __init__(self, lista):
        self.lista = lista
    def obtener_moda (self):
        contador = 1;
        l_cant = []
        for n in self.lista:
            cant = self.lista.count(n)
            l_cant.append(cant)
            contador = cant if cant > contador else contador
        return self.lista[l_cant.index(contador)], contador