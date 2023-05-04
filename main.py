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

# Define uma fonte para ser utilizada ao escrever textos que vão ser exibidos no jogo como uma superfície
fonte = pygame.font.Font('font/Pixeltype.ttf', 50)

# Superfícies são os elementos visuais que serão mostrados na tela
# Superfície de céu para o fundo
superficie_sky = pygame.image.load('graphics/Sky.png').convert()
# Superfície de chão para o fundo
superficie_ground = pygame.image.load('graphics/ground.png').convert()
# Superfície do texto
superficie_texto = fonte.render("Dinossaurinho :(", False, 'Black')
# Superfície do inimigo
superficie_lesma = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
lesma_x_pos = 600

while True:
    # Loop para pegar os possíveis inputs do jogador
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            print("\nNão me deixe sozinho :(\n")
            pygame.quit()
            exit()

    # Mostra na tela as superfícies do céu e do chão e do texto
    tela.blit(superficie_sky, (0, 0))
    tela.blit(superficie_ground, (0, 300))
    tela.blit(superficie_texto, (300, 50))
    # If/else para voltar a lesma para a tela quando ela sair dela
    if lesma_x_pos >= -100:
        # Mexe a lesma 4 pixel para a esquerda
        lesma_x_pos -= 4
    else:
        lesma_x_pos = 800
    # Mostra na tela a superfície da lesma
    tela.blit(superficie_lesma, (lesma_x_pos, 250))

    # Atualiza a tela que foi gerada anteriormente com novas informações que tenham ocorrido durante o loop
    pygame.display.update()

    # Define o framerate máximo em 60 fps
    clock.tick(60)