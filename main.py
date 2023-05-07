import pygame
from sys import exit
from random import randint

def placar():
    tempo = pygame.time.get_ticks()
    superficie_tempo = fonte.render(f'Pontos: {int((tempo-tempo_inicial)/1000)}',False,(64,64,64))
    retangulo_tempo = superficie_tempo.get_rect(center = (400,50))
    tela.blit(superficie_tempo,retangulo_tempo)
    return int((tempo-tempo_inicial)/1000)

def movimento_obstaculo(obstaculo_lista):
    if obstaculo_lista:
        for obstaculo in obstaculo_lista:
            obstaculo.x -= 5

            tela.blit(superficie_lesma,obstaculo)
        
        obstaculo_lista = [obstaculo for obstaculo in obstaculo_lista if obstaculo.x > -100]

    return obstaculo_lista

WIDTH = 800
HEIGHT = 400

pygame.init()
tela = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('JOGO DO DINOSSAURO FAKE')
clock = pygame.time.Clock()
fonte = pygame.font.Font('font/Pixeltype.ttf', 50)
jogando = False
tempo_inicial = 0
tempo_jogo = 0
superficie_sky = pygame.image.load('graphics/Sky.png').convert()
superficie_ground = pygame.image.load('graphics/ground.png').convert()
superficie_lesma = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
retangulo_lesma = superficie_lesma.get_rect(midbottom = (600, 300))
obstaculo_lista = []
superficie_player = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()
retangulo_player = superficie_player.get_rect(midbottom = (80, 300))
player_parado = pygame.image.load('graphics/Player/player_stand.png').convert_alpha()
player_parado = pygame.transform.rotozoom(player_parado, 0, 2)
retangulo_player_parado = player_parado.get_rect(center = (400,200))
nome_jogo = fonte.render("JOGO DO DINOSSAURO FAKE", False, (111,196,169))
nome_retangulo = nome_jogo.get_rect(center = (400, 75))
comecar = fonte.render("Aperte ESPACO para iniciar o jogo", False, (111,196,169))
comecar_retangulo = comecar.get_rect(center = (400, 330))
gravidade = 0

timer_obstaculo = pygame.USEREVENT + 1
pygame.time.set_timer(timer_obstaculo, 1500)

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            print("\nNão me deixe sozinho :(\n")
            pygame.quit()
            exit()
        if jogando:
            if evento.type == pygame.MOUSEBUTTONDOWN and retangulo_player.collidepoint(evento.pos) and retangulo_player.bottom >= 300:
                gravidade = -20
            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_SPACE and retangulo_player.bottom >= 300:
                gravidade = -20
            if evento.type == timer_obstaculo:
                obstaculo_lista.append(superficie_lesma.get_rect(bottomright = (randint(900,1100), 300)))
        else:
            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_SPACE:
                jogando = True
                retangulo_lesma.left = 800
                tempo_inicial = pygame.time.get_ticks()

    if jogando:
        tela.blit(superficie_sky, (0, 0))
        tela.blit(superficie_ground, (0, 300))
        tempo_jogo = placar()
        # if retangulo_lesma.right > 0:
        #     retangulo_lesma.x -= 4
        # else:
        #     retangulo_lesma.left = 800
        # tela.blit(superficie_lesma, retangulo_lesma)

        gravidade += 1
        retangulo_player.y += gravidade
        if retangulo_player.bottom >= 300:
            retangulo_player.bottom = 300
        tela.blit(superficie_player, retangulo_player)

        obstaculo_lista = movimento_obstaculo(obstaculo_lista)

        if retangulo_lesma.colliderect(retangulo_player):
            jogando = False

    else:
        tela.fill((94,129,162))
        tela.blit(player_parado, retangulo_player_parado)
        tela.blit(comecar, comecar_retangulo)
        if tempo_jogo == 0:
            tela.blit(nome_jogo, nome_retangulo)
        else:
            tempo_jogo_texto = fonte.render(f'Seu tempo: {tempo_jogo}', False, (111,196,169))
            tempo_jogo_retangulo = tempo_jogo_texto.get_rect(center = (400, 75))
            tela.blit(tempo_jogo_texto, tempo_jogo_retangulo)

    pygame.display.update()

    clock.tick(60)