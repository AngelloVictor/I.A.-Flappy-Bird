import pygame
import os
import random

# Configurações da tela
LARGURA_TELA = 500
ALTURA_TELA = 800

# Imagens do jogo
IMAGEM_CANO = pygame.transform.scale2x(pygame.image.load("imgs/pipe.png"))
IMAGEM_CHAO = pygame.transform.scale2x(pygame.image.load("imgs/base.png"))
IMAGEM_BACKGROUND = pygame.transform.scale2x(pygame.image.load("imgs/bg.png"))
IMAGENS_PASSARO = [
    pygame.transform.scale2x(pygame.image.load("imgs/bird1.png")),
    pygame.transform.scale2x(pygame.image.load("imgs/bird2.png")),
    pygame.transform.scale2x(pygame.image.load("imgs/bird3.png")),
]

# Definição das fontes do jogo
pygame.font.init()
FONTE_PONTOS = pygame.font.SysFont("Arial", 40)

# ====== #
# Classe #
# ====== #

# Classe que representa o passaro
class Passaro:

    # Atributos do passaro (constantes)
    IMGS = IMAGENS_PASSARO

    # Animações da rotação do passaro (Valores testados)
    ROTACAO_MAX = 25
    VELOCIDADE_ROTACAO = 20
    TEMPO_ANIMACAO = 5

    # Atributos do passaro (variáveis)
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.angulo = 0
        self.velocidade = 0
        self.altura = self.y

        # Parametros auxiliares
        self.tempo = 0
        self.contagem_imagem = 0
        self.imagem = self.IMGS[0]

    def pular(self):
        self.velocidade = -10.5
        self.tempo = 0
        self.altura = self.y

    def mover(self):
        # Calculo do deslocamento
        self.tempo += 1

        # S = so +vot + at2/2
        deslocamento = 1.5 * (self.tempo ** 2) + self.velocidade * self.tempo

        # Restringir o deslocamento, evitar bugs no jogo
        if deslocamento > 16:
            deslocamento = 16

        elif deslocamento < 0:
            deslocamento -= 2

        # Deslocamento efetivo
        self.y = +deslocamento

        # Angulo do passaro
        if deslocamento < 0 or self.y < (self.altura + 50):
            if self.angulo < self.ROTACAO_MAX:
                self.angulo += self.ROTACAO_MAX

            else:
                if self.angulo > -90:
                    self.angulo -= self.VELOCIDADE_ROTACAO

    def desenhar(self, tela):
        # Definir a imagem do passaro a ser usada
        self.contagem_imagem += 1
        if self.contagem_imagem < self.TEMPO_ANIMACAO:
            self.imagem = self.IMGS[0]

        elif self.contagem_imagem < self.TEMPO_ANIMACAO * 2:
            self.imagem = self.IMGS[1]

        elif self.contagem_imagem < self.TEMPO_ANIMACAO * 3:
            self.imagem = self.IMGS[2]

        elif self.contagem_imagem < self.TEMPO_ANIMACAO * 4:
            self.imagem = self.IMGS[1]

        elif self.contagem_imagem >= self.TEMPO_ANIMACAO * 4 + 1:
            self.imagem = self.IMGS[0]
            self.contagem_imagem = 0

        # Se o passaro tiver caindo, nao bater asas
        if self.angulo <= -80:
            self.imagem = self.IMGS[1]
            self.contagem_imagem = self.TEMPO_ANIMACAO * 2

        # Desenhar a imagem
        imagem_rotacionada = pygame.transform.rotate(self.imagem, self.angulo)
        pos_centro_imagem = self.imagem.get_rect(topleft=(self.x, self.y)).center
        retangulo = imagem_rotacionada.get_rect(center=pos_centro_imagem)
        tela.blit(imagem_rotacionada, retangulo)

    # Mascarando a imagem para colisao
    def get_mask(self):
        pygame.mask.from_surface(self.imagem)
    
        
    
# Classe que representa o cano
class Cano:
    pass


# Classe que representa o chão
class Chao:
    pass
