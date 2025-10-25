#jago da cobunha com python
import random
class JogoDaCobrinha:
    def __init__(self, tamanho_campo):
        self.tamanho_campo = tamanho_campo
        self.cobra_posicao = [tamanho_campo // 2, tamanho_campo // 2]
        self.comida_posicao = self.gerar_comida()
        self.pontuacao = 0

    def gerar_comida(self):
        return [random.randint(0, self.tamanho_campo - 1), random.randint(0, self.tamanho_campo - 1)]

    def mover_cobra(self, direcao):
        if direcao == 'w':
            self.cobra_posicao[1] -= 1
        elif direcao == 's':
            self.cobra_posicao[1] += 1
        elif direcao == 'a':
            self.cobra_posicao[0] -= 1
        elif direcao == 'd':
            self.cobra_posicao[0] += 1

        self.verificar_colisao()

    def verificar_colisao(self):
        if (self.cobra_posicao[0] < 0 or self.cobra_posicao[0] >= self.tamanho_campo or
            self.cobra_posicao[1] < 0 or self.cobra_posicao[1] >= self.tamanho_campo):
            print("Game Over! Voce bateu na parede.")
            exit()

        if self.cobra_posicao == self.comida_posicao:
            self.pontuacao += 1
            print(f"Comida comida! Pontuacao: {self.pontuacao}")
            self.comida_posicao = self.gerar_comida()

    def exibir_campo(self):
        for y in range(self.tamanho_campo):
            for x in range(self.tamanho_campo):
                if [x, y] == self.cobra_posicao:
                    print("C", end=" ")
                elif [x, y] == self.comida_posicao:
                    print("F", end=" ")
                else:
                    print(".", end=" ")
            print()
        print()
jogo = JogoDaCobrinha(5)
while True:
    jogo.exibir_campo()
    direcao = input("Mover (w/a/s/d): ")
    jogo.mover_cobra(direcao)
