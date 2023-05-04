import pygame
# Import para poder parar a execução de todo o código caso o jogador feche o jogo
from sys import exit

WIDTH = 800 # pixels
HEIGHT = 400 # pixel

# Inicia o pygame
pygame.init()

# Gera a tela na qual o jogo será jogado. Recebe como argumento um tuple que consiste da largura e da altura
tela = pygame.display.set_mode((WIDTH, HEIGHT))

# Muda o nome da janela do jogo
pygame.display.set_caption('JOGO DO DINOSSAURO FAKE')

# Clock para definir o framerate do jogo
clock = pygame.time.Clock()

# Superfície para testar
# Superfícies são os elementos visuais que serão mostrados na tela
superficie_teste = pygame.Surface((100, 200))

# Adiciona a cor vermelha à essa superfície teste 
superficie_teste.fill('Red')

while True:
    # Loop para pegar os possíveis inputs do jogador
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            print("\nNão me deixe sozinho :(\n")
            pygame.quit()
            exit()

    # Mostra na tela a superfície teste criada
    tela.blit(superficie_teste, (200, 100))

    # Atualiza a tela que foi gerada anteriormente com novas informações que tenham ocorrido durante o loop
    pygame.display.update()

    # Define o framerate máximo em 60 fps
    clock.tick(60)