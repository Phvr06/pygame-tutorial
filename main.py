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
# Retângulos são elementos utilizados para posicionar melhor superfícies
# Superfície de céu para o fundo
superficie_sky = pygame.image.load('graphics/Sky.png').convert()
# Superfície de chão para o fundo
superficie_ground = pygame.image.load('graphics/ground.png').convert()
# Superfície do texto
superficie_texto = fonte.render("Alien :)", False, 'Black')
# Retângulo do texto
retangulo_texto = superficie_texto.get_rect(center = (400, 50))
# Superfície do inimigo
superficie_lesma = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
# Retângulo lesma
retangulo_lesma = superficie_lesma.get_rect(midbottom = (600, 300))
# Superfície do jogador
superficie_player = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()
# Retângulo do jogador
retangulo_player = superficie_player.get_rect(midbottom = (80, 300))

while True:
    # Loop para pegar os possíveis inputs do jogador
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            print("\nNão me deixe sozinho :(\n")
            pygame.quit()
            exit()
        # Colisão com o mouse
        # if evento.type == pygame.MOUSEMOTION and retangulo_player.collidepoint(evento.pos):
        #     print("Na mira!")            

    # Mostra na tela as superfícies do céu e do chão e do texto
    tela.blit(superficie_sky, (0, 0))
    tela.blit(superficie_ground, (0, 300))
    pygame.draw.rect(tela, 'Pink', retangulo_texto)
    pygame.draw.rect(tela, 'Pink', retangulo_texto, 10)
    tela.blit(superficie_texto, retangulo_texto)
    # If/else para voltar a lesma para a tela quando ela sair dela
    if retangulo_lesma.right > 0:
        # Mexe a lesma 4 pixel para a esquerda
        retangulo_lesma.x -= 4
    else:
        retangulo_lesma.left = 800
    # Mostra na tela a superfície da lesma
    tela.blit(superficie_lesma, retangulo_lesma)
    # Mostra na tela a superfície do jogador
    tela.blit(superficie_player, retangulo_player)

    # Verificar colisão entre o jogador e a lesma
    # if retangulo_player.colliderect(retangulo_lesma):
    #     print('Porra, o ET bilu morreu!')

    # Atualiza a tela que foi gerada anteriormente com novas informações que tenham ocorrido durante o loop
    pygame.display.update()

    # Define o framerate máximo em 60 fps
    clock.tick(60)