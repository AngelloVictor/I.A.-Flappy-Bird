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
        self.imagem = IMGS[0]
        
        
    def pular(self):
        self.velocidade = -10.5
        self.tempo = 0
        


# Classe que representa o cano
class Cano:
    pass


# Classe que representa o chão
class Chao:
    pass
