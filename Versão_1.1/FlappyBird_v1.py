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
        sel
        
        
        

# Classe que representa o cano
class Cano:
    pass


# Classe que representa o chão
class Chao:
    pass
