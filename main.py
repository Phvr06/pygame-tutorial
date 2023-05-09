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
            
            if obstaculo.bottom == 300:
                tela.blit(superficie_lesma,obstaculo)
            else:
                tela.blit(superficie_mosca,obstaculo)
        
        obstaculo_lista = [obstaculo for obstaculo in obstaculo_lista if obstaculo.x > -100]

    return obstaculo_lista

def colisoes(player, obstaculos):
    if obstaculos:
        for obstaculo in obstaculos:
            if player.colliderect(obstaculo):
                return False
    return True

def player_animation():
    global superficie_player, player_index
    if retangulo_player.bottom < 300:
        superficie_player = player_jump
    else:
        player_index += 0.1
        if player_index >= len(player_walk):
            player_index = 0
        superficie_player = player_walk[int(player_index)]

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
frame_lesma_1 = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
frame_lesma_2 = pygame.image.load('graphics/snail/snail2.png').convert_alpha()
frames_lesma = [frame_lesma_1, frame_lesma_2]
lesma_frame_index = 0
superficie_lesma = frames_lesma[lesma_frame_index]
frame_mosca_1 = pygame.image.load('graphics/fly/fly1.png').convert_alpha()
frame_mosca_2 = pygame.image.load('graphics/fly/fly2.png').convert_alpha()
frames_mosca = [frame_mosca_1, frame_mosca_2]
mosca_frame_index = 0
superficie_mosca = frames_mosca[mosca_frame_index]
obstaculo_lista = []
player_walk_1 = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()
player_walk_2 = pygame.image.load('graphics/Player/player_walk_2.png').convert_alpha()
player_walk = [player_walk_1, player_walk_2]
player_index = 0
player_jump = pygame.image.load('graphics/Player/jump.png').convert_alpha()
superficie_player = player_walk[player_index]
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

animacao_lesma_timer = pygame.USEREVENT + 2
pygame.time.set_timer(animacao_lesma_timer, 500)

animacao_mosca_timer = pygame.USEREVENT + 3
pygame.time.set_timer(animacao_mosca_timer, 200)

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
                if randint(0,2):
                    obstaculo_lista.append(superficie_lesma.get_rect(bottomright = (randint(900,1100), 300)))
                else:
                    obstaculo_lista.append(superficie_lesma.get_rect(bottomright = (randint(900,1100), 200)))
            if evento.type == animacao_lesma_timer:
                if lesma_frame_index == 0:
                    lesma_frame_index = 1
                else:
                    lesma_frame_index = 0
                superficie_lesma = frames_lesma[lesma_frame_index]
            if evento.type == animacao_mosca_timer:
                if mosca_frame_index == 0:
                    mosca_frame_index = 1
                else:
                    mosca_frame_index = 0
                superficie_mosca = frames_mosca[mosca_frame_index]
        else:
            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_SPACE:
                jogando = True
                tempo_inicial = pygame.time.get_ticks()

    if jogando:
        tela.blit(superficie_sky, (0, 0))
        tela.blit(superficie_ground, (0, 300))
        tempo_jogo = placar()

        gravidade += 1
        retangulo_player.y += gravidade
        if retangulo_player.bottom >= 300:
            retangulo_player.bottom = 300
        player_animation()
        tela.blit(superficie_player, retangulo_player)

        obstaculo_lista = movimento_obstaculo(obstaculo_lista)

        jogando = colisoes(retangulo_player, obstaculo_lista)

    else:
        tela.fill((94,129,162))
        tela.blit(player_parado, retangulo_player_parado)
        tela.blit(comecar, comecar_retangulo)
        obstaculo_lista.clear()
        retangulo_player.midbottom = (80, 300)
        gravidade = 0
        if tempo_jogo == 0:
            tela.blit(nome_jogo, nome_retangulo)
        else:
            tempo_jogo_texto = fonte.render(f'Seu tempo: {tempo_jogo}', False, (111,196,169))
            tempo_jogo_retangulo = tempo_jogo_texto.get_rect(center = (400, 75))
            tela.blit(tempo_jogo_texto, tempo_jogo_retangulo)

    pygame.display.update()

    clock.tick(60)