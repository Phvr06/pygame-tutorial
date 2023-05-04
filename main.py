import pygame
# Import para poder parar a execução de todo o código caso o jogador feche o jogo
from sys import exit

WIDTH = 800 # pixels
HEIGHT = 400 # pixel

# Inicia o pygame
pygame.init()

# Gera a tela na qual o jogo será jogado. Recebe como argumento um tuple que consiste da largura e da altura
tela = pygame.display.set_mode((WIDTH, HEIGHT))

while True:
    # Loop para pegar os possíveis inputs do jogador
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            exit()

    # Atualiza a tela que foi gerada anteriormente com novas informações que tenham ocorrido durante o loop
    pygame.display.update()