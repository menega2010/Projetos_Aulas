class Calculadora:
    area_paredes: float
    area_teto: float

    def calcular_area_parede(self, largura, profundidade, altura):
        self.area_paredes = 2 * (largura + profundidade) * altura
        return self.area_paredes

    def calcula_area_teto(self, largura, profundidade):
        self.area_teto = largura * profundidade
        return self.area_teto

    def calcula_litragem_necessaria(self):
        return (self.area_paredes + self.area_teto) / 10