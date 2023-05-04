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

# Superfícies são os elementos visuais que serão mostrados na tela
# Superfície de céu para o fundo
superficie_sky = pygame.image.load('graphics/Sky.png')
# Superfície de chão para o fundo
superficie_ground = pygame.image.load('graphics/ground.png')

while True:
    # Loop para pegar os possíveis inputs do jogador
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            print("\nNão me deixe sozinho :(\n")
            pygame.quit()
            exit()

    # Mostra na tela as superfícies do céu e do chão
    tela.blit(superficie_sky, (0, 0))
    tela.blit(superficie_ground, (0, 300))

    # Atualiza a tela que foi gerada anteriormente com novas informações que tenham ocorrido durante o loop
    pygame.display.update()

    # Define o framerate máximo em 60 fps
    clock.tick(60)