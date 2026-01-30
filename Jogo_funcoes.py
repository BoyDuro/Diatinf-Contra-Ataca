# Vamos lá. Os comentários em caixa alta serão mais formais por só indicarem oq aquilo é em si. Os em caixa baixa são mais informais por serem explicações mais completas e q seria bom estar em um fácil entendimento

import pygame
import random

def danos_na_vida(dano_x, vida_x):
  vida_x  = vida_x - dano_x
  return vida_x

def repetir_partida():
  global turno_atual

  Boss['vida'] = Boss['vida_max']
  Personagem['vida'] = Personagem['vida_max']

  turno_atual = vez_do_jogador

def desenhar_creditos_funcao():
  global visivel, frame_da_anim_nomes, matthew__creditos_y, thalis_creditos_y

  if frame_agora_nomes - frame_da_anim_nomes >= tempo_anim_nomes:
    visivel = not visivel
    frame_da_anim_nomes = frame_agora_nomes
  
  if visivel:
    screen.blit(nome1_creditos, (0, 0))
    screen.blit(nome2_creditos, (0, 0))

  screen.blit(pixelart1_creditos, (0, matthew__creditos_y))
  screen.blit(pixelart2_creditos, (0, thalis_creditos_y))

  if matthew__creditos_y < 0:
    matthew__creditos_y += velocidade_dos_personagens
  if thalis_creditos_y > 0:
    thalis_creditos_y -= velocidade_dos_personagens

def tela_creditos_funcao():
  global alpha_dos_creditos, estado_fade_creditos, momento_atual, tempo_creditos, apagar_alpha, fade_tela_inicial

  screen.blit(tela_creditos, (0, 0))
  desenhar_creditos_funcao()

  if estado_fade_creditos == 0:
    alpha_dos_creditos -= 2
    if alpha_dos_creditos <= 0:
      alpha_dos_creditos = 0
      estado_fade_creditos = 1
      tempo_creditos = pygame.time.get_ticks()

  elif estado_fade_creditos == 1:
    if pygame.time.get_ticks() - tempo_creditos >= tempo_final_creditos:
      estado_fade_creditos = 2

  elif estado_fade_creditos == 2:
    alpha_dos_creditos += 2
    if alpha_dos_creditos >= 255:
      alpha_dos_creditos = 255
      estado_fade_creditos = 3

  anim_apagar_tela.set_alpha(alpha_dos_creditos)
  screen.blit(anim_apagar_tela, (0, 0))

  if estado_fade_creditos == 3:
    estado_fade_creditos = 0
    momento_atual = momento_tela_inicial

    apagar_alpha = 255
    fade_tela_inicial = True



def tela_inicial_funcao():
# ESSA É A FUNÇÃO DE TUDO QUE ACONTECE NA TELA INICIAL  
  global anim_titulo, direcao, frame_travado, visivel, frame_da_anim_play, fade_tela_inicial, apagar_alpha

  screen.blit(tela_inicial, (0, 0))
  screen.blit(titulo, (0, anim_titulo))
  


  if anim_titulo >= 20:
    direcao = -4
  elif anim_titulo <= -10:
    direcao = 4
  frame_travado += 1

  if frame_travado >= 15:
    anim_titulo += direcao
    frame_travado = 0

  # AQUI TEM A ANIMAÇÃO DO PLAY PISCANDO
  if frame_agora_play - frame_da_anim_play >= tempo_anim_play:
    visivel = not visivel
    frame_da_anim_play = frame_agora_play
  
  if visivel:
    screen.blit(play, (0, 0))

  if fade_tela_inicial:
    apagar_alpha -= 1
    if apagar_alpha <= 0:
      apagar_alpha = 0
      fade_tela_inicial = False

    anim_apagar_tela.set_alpha(apagar_alpha)
    screen.blit(anim_apagar_tela, (0, 0))

def tela_transicao_funcao():
# ESSA É A FUNÇÃO QUE DEIXA A TELA PRETA TODA VEZ QUE UMA TRANSIÇÃO DE TELA ACONTECE
  screen.blit(tela_inicial_fundo, (0, 0))

def tela_gameplay_funcao():
# ESSA É A FUNÇÃO DE TUDO QUE ACONTECE NA GAMEPLAY 
  global visivel, frame_anim_hover, sem_anim, turno_atual, ordem_do_apagar, apagar_alpha, Boss, Personagem

  screen.blit(cenario, (0, 0))
  todas_sprites.draw(screen)
  todas_sprites.update()
  screen.blit(menu_base, (15, 456))
  screen.blit(logo_diatinf, (20, 463))



  barra_de_vida_boss = int((Boss['vida']/Boss['vida_max'])*largura_da_barra)
  pygame.draw.rect(screen, (0, 230, 0), (549, 40, barra_de_vida_boss, 20))

  screen.blit(barra_vida_diaren, (510, -10))
  
  # usei o rect por ele ser mais fácil de se atualizar, já que a cada frame, essa barrinha de vida tá atualizando graças ao rect

  barra_de_vida_jogador = int((Personagem['vida']/Personagem['vida_max'])*largura_da_barra)
  pygame.draw.rect(screen, (230, 0, 0), (51, 433, barra_de_vida_jogador, 20))

  screen.blit(barra_vida_diatinf, (15,375))

  # os comentários daq são mais antigos, mas tudo isso de dicionário tá lá embaixo dps de todas as funções

  for skill_atual in skills:
    # DESENHA OS ELEMENTOS DO DICIONÁRIO E LISTA DE SKILLS QUE CRIEI PRA FAZER O RECT DA ANIMAÇÃO
    screen.blit(skill_atual['cor'], skill_atual['posicao'].topleft)

    # AQUI TEM A ANIMAÇÃO DO HOVER NAS SKILLS
    # mudei variáveis pq deu problema ao reutilizar algumas da animação do play
    if frame_agora_hover - frame_anim_hover >= tempo_anim_hover:
      visivel = not visivel
      frame_anim_hover = frame_agora_hover

    if visivel:
      if skill_atual['posicao'].collidepoint(posicao_do_mouse):
        pygame.draw.rect(screen,(255, 0, 0), skill_atual['posicao'], 6)

  if turno_atual == vez_do_jogador_anim:
    sem_anim += 1
  # O QUE SERIA vez_do_jogador_anim? Enquanto não tinha animações, deixei já o estado onde a animação aconteceria e por hora ele é só um cooldown até o dano contar

    if sem_anim >= 150:
      # isso aq é oq tira vida do boss. Mais p baixo tem outro q tira a vida do jogador
      Boss['vida'] = danos_na_vida(dano_do_turno, Boss['vida'])
      sem_anim = 0
      turno_atual = vez_do_boss
  
  if turno_atual == vez_do_boss:
    random.shuffle(Boss['ataques'])
    if Boss['ataques'][0] == True:
      random.shuffle(Boss['atk_condicao'])
      if Boss['atk_condicao'][0] == True:
        random.shuffle(Boss['danos'])
        turno_atual = vez_do_boss_anim
        diaren.atk_diaren()
      else:
        turno_atual = vez_do_jogador
    else:
      random.shuffle(Boss['atk_condicao'])
      if Boss['atk_condicao'][0] == True:
        random.shuffle(Boss['danos2'])
        turno_atual = vez_do_boss_anim
        diaren.atk2_diaren()
      else:
        turno_atual = vez_do_jogador

  
  if turno_atual == vez_do_boss_anim:
    sem_anim += 1
  # segue a msm lógica do vez_do_jogador_anim

    if sem_anim >= 150:
      Personagem['vida'] = danos_na_vida(Boss['danos'][0], Personagem['vida'])
      Boss['danos'] = [30, 20, 10]
      # Reinicia a lista após a possibilidade da habilidade de anular o dano
      sem_anim = 0
      turno_atual = vez_do_jogador

  if (Boss['vida'] <= 0 or Personagem['vida'] <= 0) and ordem_do_apagar == 0:
    ordem_do_apagar = 1
    apagar_alpha = 0
    turno_atual = None

def tela_vitoria_funcao():
  global visivel, frame_da_anim_vitoria

  screen.blit(tela_vitoria, (0, 0))
  
  if frame_agora_vitoria - frame_da_anim_vitoria >= tempo_anim_play:
    visivel = not visivel
    frame_da_anim_vitoria = frame_agora_vitoria
  
  if visivel:
    screen.blit(texto_vitoria, (0, 0))

# AMBAS FUNÇÕES AQUI SÃO PRA DESENHAR A TELA DE VITÓRIA E DERROTA, QUE POR SI SÓ SÃO O MESMO ESQUEMA

def tela_derrota_funcao():
  global visivel, frame_da_anim_derrota

  screen.blit(tela_derrota, (0, 0))

  iniciar_musica_morte()
  toca_musica_morte = False

  if frame_agora_derrota - frame_da_anim_derrota >= tempo_anim_play:
    visivel = not visivel
    frame_da_anim_derrota = frame_agora_derrota
  
  if visivel:
    screen.blit(texto_derrota, (0, 0))

def iniciar_musica_gameplay():
  global toca_musica_gameplay

  if not toca_musica_gameplay:
    pygame.mixer.music.load('gameplay.mp3')
    pygame.mixer.music.play(-1, fade_ms=2000)
    toca_musica_gameplay = True

def iniciar_musica_morte():
  global toca_musica_morte

  if not toca_musica_morte:
    pygame.mixer.music.load('morte.mp3')
    pygame.mixer.music.play(-1, fade_ms=2000)
    toca_musica_morte = True

def animacoes_e_final_de_jogo():
# Essa parte é oq faz as animações de Fade acontecerem. "Ah, mas pq final de jogo?" Bem, no programa original antes das funções, eu definia que o jogo acabou e chegou na tela final por meio desse processo de animação.
  global ordem_do_apagar, apagar_alpha, tempo_de_transicao, momento_atual, toca_musica

# AQUI TEM A ANIMAÇÃO DE FADE DE TRANSIÇÃO
# ordem_do_apagar: 1(escurece a tela), 2(dá um tempo de tela escura), 3(clarea a tela), 4(desenha e finaliza)
  if ordem_do_apagar == 1:
    apagar_alpha += tempo_de_transicao

    if apagar_alpha >= 255:
      apagar_alpha = 255
      ordem_do_apagar = 2
      if momento_atual == momento_tela_inicial:
        momento_atual = momento_gameplay
        iniciar_musica_gameplay()
      elif momento_atual == momento_gameplay and Boss['vida'] <= 0:
        momento_atual = momento_vitoria
        pygame.mixer.music.fadeout(1000)
        toca_musica = False
      elif momento_atual == momento_gameplay and Personagem['vida'] <= 0:
        momento_atual = momento_derrota
        pygame.mixer.music.fadeout(1000)
        toca_musica = False
      elif momento_atual == momento_derrota or momento_atual == momento_vitoria:
        repetir_partida()
        momento_atual = momento_tela_inicial
  
  elif ordem_do_apagar == 2:
    tempo_de_transicao += 1
    if tempo_de_transicao >= 25:
      ordem_do_apagar = 3
      tempo_de_transicao = 3

  elif ordem_do_apagar == 3:
    tempo_de_transicao = 1
    apagar_alpha -= tempo_de_transicao

    if apagar_alpha <= 0:
      tempo_de_transicao = 3
      apagar_alpha = 0
      ordem_do_apagar = 4

  if ordem_do_apagar != 4:
    anim_apagar_tela.set_alpha(apagar_alpha)
    screen.blit(anim_apagar_tela, (0, 0))
  if ordem_do_apagar == 4:
    ordem_do_apagar = 0

def conferir_momento_funcao():
# SIMPLES. FUNÇÃO QUE VAI DEFINIR QUAL MOMENTO ACONTECE NA TELA
  if momento_atual == momento_creditos:
    tela_creditos_funcao()
  elif momento_atual == momento_tela_inicial:
    tela_inicial_funcao()
  elif momento_atual == momento_transicao:
    tela_transicao_funcao()
  elif momento_atual == momento_gameplay:
    tela_gameplay_funcao()
  elif momento_atual == momento_vitoria:
    tela_vitoria_funcao()
  elif momento_atual == momento_derrota:
    tela_derrota_funcao()
 
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((784, 588))
clock = pygame.time.Clock()
running = True

tela_inicial = pygame.image.load('Pasta das telas/PNG das telas/Tela sem nada inicial.png')
tela_inicial = tela_inicial.convert()
tela_inicial = pygame.transform.scale(tela_inicial, (784, 588))

tela_inicial_fundo = pygame.image.load('Pasta das telas/PNG das telas/Tela inicial jpg.png')
tela_inicial_fundo = tela_inicial_fundo.convert()
tela_inicial_fundo = pygame.transform.scale(tela_inicial_fundo, (784, 588))

tela_vitoria = pygame.image.load('Pasta das telas/PNG das telas/Tela de vitória vazia.png')
tela_vitoria = tela_vitoria.convert()
tela_vitoria = pygame.transform.scale(tela_vitoria, (784, 588))

texto_vitoria = pygame.image.load('Pasta das telas/PNG das telas/vc venceu.png')
texto_vitoria = texto_vitoria.convert_alpha()
texto_vitoria = pygame.transform.scale(texto_vitoria, (784, 588))

tela_derrota = pygame.image.load('Pasta das telas/PNG das telas/Tela de morte vazia.png')
tela_derrota = tela_derrota.convert()
tela_derrota = pygame.transform.scale(tela_derrota, (784, 588))

texto_derrota = pygame.image.load('Pasta das telas/PNG das telas/vc morreu.png')
texto_derrota = texto_derrota.convert_alpha()
texto_derrota = pygame.transform.scale(texto_derrota, (784, 588))


titulo = pygame.image.load('Pasta das telas/PNG das telas/Titulo.png')
titulo = titulo.convert_alpha()
titulo = pygame.transform.scale(titulo, (784, 588))

play = pygame.image.load('Pasta das telas/PNG das telas/Play.png')
play = play.convert_alpha()
play = pygame.transform.scale(play, (784, 588))

teste = pygame.image.load('Pasta das telas/PNG das telas/Tela de partida.png')
teste = teste.convert()
teste = pygame.transform.scale(teste, (784, 588))

cenario = pygame.image.load('Cenário/cenario-novo.png')
cenario = cenario.convert()
cenario = pygame.transform.scale(cenario, (784, 588))

menu_base = pygame.Surface([475, 122])
menu_base.fill((0, 1, 50))

diaren = pygame.image.load('Personagens Diaren/diaren.png')
diaren = diaren.convert_alpha()
diaren = pygame.transform.scale(diaren, (400, 400))

tela_creditos = pygame.image.load('Pasta das telas/PNG das telas/Creditos base.png')
tela_creditos = tela_creditos.convert()
tela_creditos = pygame.transform.scale(tela_creditos, (784, 588))

nome1_creditos = pygame.image.load('Pasta das telas/PNG das telas/creditos nome1.png')
nome1_creditos = nome1_creditos.convert_alpha()
nome1_creditos = pygame.transform.scale(nome1_creditos, (784, 588))

pixelart1_creditos = pygame.image.load('Pasta das telas/PNG das telas/creditos matthew.png')
pixelart1_creditos = pixelart1_creditos.convert_alpha()
pixelart1_creditos = pygame.transform.scale(pixelart1_creditos, ((784, 588)))

nome2_creditos = pygame.image.load('Pasta das telas/PNG das telas/creditos nome2.png')
nome2_creditos = nome2_creditos.convert_alpha()
nome2_creditos = pygame.transform.scale(nome2_creditos, (784, 588))

pixelart2_creditos = pygame.image.load('Pasta das telas/PNG das telas/creditos thalis.png')
pixelart2_creditos = pixelart2_creditos.convert_alpha()
pixelart2_creditos = pygame.transform.scale(pixelart2_creditos, (784, 588))

barra_vida_diatinf = pygame.image.load('Personagens Diatinf/barra_de_vida_diatinf.png')
barra_vida_diatinf = barra_vida_diatinf.convert_alpha()
barra_vida_diatinf = pygame.transform.scale(barra_vida_diatinf, (200,80))

barra_vida_diaren = pygame.image.load('Personagens Diaren/barra de vida diaren.png')
barra_vida_diaren = barra_vida_diaren.convert_alpha()
barra_vida_diaren = pygame.transform.scale(barra_vida_diaren, (200,80))

skill_infoweb = pygame.image.load('Skills/skill info.png')
skill_infoweb = skill_infoweb.convert()
skill_infoweb = pygame.transform.scale(skill_infoweb, (88, 88))

skill_msi = pygame.image.load('Skills/skill msi.png')
skill_msi = skill_msi.convert()
skill_msi = pygame.transform.scale(skill_msi, (88, 88))

skill_adm = pygame.image.load('Skills/skill adm.png')
skill_adm = skill_adm.convert()
skill_adm = pygame.transform.scale(skill_adm, (88, 88))


# BARRA DE SKILLS
skills = [
  {'posicao': pygame.Rect(158, 473, 88, 88), 'cor': skill_infoweb, 'nome': 'Infoweb', 'danos': [60, 50, 40, 40, 40, 10]},
  {'posicao': pygame.Rect(271, 473, 88, 88), 'cor': skill_msi, 'nome': 'MSI', 'danos': [70, 30, 30, 30, 20]},
  {'posicao': pygame.Rect(384, 473, 88, 88), 'cor': skill_adm, 'nome': 'Adm'},
]


frame_anim_hover = pygame.time.get_ticks()
tempo_anim_hover = 400



logo_diatinf = pygame.image.load('Skills/diatinf logo.png')
logo_diatinf = logo_diatinf.convert()
logo_diatinf = pygame.transform.scale(logo_diatinf, (108, 108))

# FIM DA BARRA DE SKILLS



# ÁREA DE BOSS E PERSONAGEM
Boss = {'vida': 250, 'vida_max': 250,  'atk_condicao': [False, True, True, True, True,], 'danos': [50, 40, 40, 40, 30], 'danos2': [70,60,50], 'ataques': [False, True]}

Personagem = {'vida': 150, 'vida_max': 150}

cooldown = 0

class Matthew(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.animacoes = {
          'idle': [
            pygame.image.load('sprites/matthew/matthew-idle-1.png').convert_alpha(),
            pygame.image.load('sprites/matthew/matthew-idle-2.png').convert_alpha(),
            pygame.image.load('sprites/matthew/matthew-idle-3.png').convert_alpha(),
            pygame.image.load('sprites/matthew/matthew-idle-4.png').convert_alpha()
          ],
          'atk_info': [
            pygame.image.load('sprites/matthew/atk-info-1.png').convert_alpha(),
            pygame.image.load('sprites/matthew/atk-info-2.png').convert_alpha(),
            pygame.image.load('sprites/matthew/atk-info-3.png').convert_alpha(),
            pygame.image.load('sprites/matthew/atk-info-4.png').convert_alpha(),
            pygame.image.load('sprites/matthew/atk-info-5.png').convert_alpha(),
            pygame.image.load('sprites/matthew/atk-info-6.png').convert_alpha(),
            pygame.image.load('sprites/matthew/atk-info-7.png').convert_alpha(),
            pygame.image.load('sprites/matthew/atk-info-8.png').convert_alpha()
          ],
          'atk_msi': [
            pygame.image.load('sprites/matthew/atk-msi-1.png').convert_alpha(),
            pygame.image.load('sprites/matthew/atk-msi-2.png').convert_alpha(),
            pygame.image.load('sprites/matthew/atk-msi-3.png').convert_alpha(),
            pygame.image.load('sprites/matthew/atk-msi-4.png').convert_alpha(),
            pygame.image.load('sprites/matthew/atk-msi-5.png').convert_alpha(),
            pygame.image.load('sprites/matthew/atk-msi-6.png').convert_alpha(),
            pygame.image.load('sprites/matthew/atk-msi-7.png').convert_alpha(),
            pygame.image.load('sprites/matthew/atk-msi-8.png').convert_alpha()
          ],
          'levou_dano': [
            pygame.image.load('sprites/matthew/matthew-dano-1.png').convert_alpha(),
            pygame.image.load('sprites/matthew/matthew-dano-2.png').convert_alpha(),
            pygame.image.load('sprites/matthew/matthew-dano-3.png').convert_alpha(),
            pygame.image.load('sprites/matthew/matthew-dano-4.png').convert_alpha(),
            pygame.image.load('sprites/matthew/matthew-dano-5.png').convert_alpha()
          ],
          'atk_adm': [
            pygame.image.load('sprites/matthew/atk-adm-1.png').convert_alpha(),
            pygame.image.load('sprites/matthew/atk-adm-2.png').convert_alpha(),
            pygame.image.load('sprites/matthew/atk-adm-3.png').convert_alpha(),
            pygame.image.load('sprites/matthew/atk-adm-4.png').convert_alpha(),
          ]
        }

        self.estado = 'idle'
        self.frame = 0
        self.velocidade = 0.1

        self.image = self.animacoes[self.estado][0]
        self.rect = self.image.get_rect(topleft=(-50, 50))

        self.animacao_terminou = False

    def atk_info(self):
        self.estado = 'atk_info'
        self.frame = 0
        self.animacao_terminou = False

    def atk_msi(self):
      self.estado = 'atk_msi'
      self.frame = 0
      self.animacao_terminou = False

    def levou_dano(self):
      self.estado = 'levou_dano'
      self.frame = 0
      self.animacao_terminou = False

    def atk_adm(self):
      self.estado = 'atk_adm'
      self.frame = 0
      self.animacao_terminou = False

    def update(self):
        global turno_atual
        global cooldown
        if self.estado == 'levou_dano':
          self.image = self.animacoes[self.estado][0]
          self.rect = self.image.get_rect(topleft=(-78, 50))
        elif self.estado == 'atk_msi':
          self.image = self.animacoes[self.estado][0]
          self.rect = self.image.get_rect(topleft=(59.6, 45))
        elif self.estado == 'atk_adm':
          self.image = self.animacoes[self.estado][0]
          self.rect = self.image.get_rect(topleft=(0, 0))
        else:
          self.image = self.animacoes[self.estado][0]
          self.rect = self.image.get_rect(topleft=(-50, 50))

        self.frame += self.velocidade

        animacao_atual = self.animacoes[self.estado]

        if self.frame >= len(animacao_atual):
            if self.estado == 'atk_info':
              self.estado = 'idle'
              self.frame = 0
              cooldown = 0
              diaren.dano_diaren()
            elif self.estado == 'atk_msi':
              self.estado = 'idle'
              self.frame= 0
              diaren.dano_diaren()
              cooldown += 1
            elif self.estado == 'levou_dano':
              self.estado = 'idle'
              self.frame = 0
            elif self.estado == 'atk_adm':
              self.estado = 'idle'
              self.frame = 0
              cooldown += 1
              turno_atual = vez_do_boss
            else:
              self.frame = 0

        self.image = animacao_atual[int(self.frame)]
        if self.estado == 'atk_adm':
          self.image = pygame.transform.scale(self.image, (784, 588))
        else:
          self.image = pygame.transform.scale(self.image, (550, 550))

class Diaren(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.animacoes = {
          'idle': [
            pygame.image.load('sprites/diaren/diaren-idle-1.png').convert_alpha(),
            pygame.image.load('sprites/diaren/diaren-idle-2.png').convert_alpha(),
            pygame.image.load('sprites/diaren/diaren-idle-3.png').convert_alpha(),
            pygame.image.load('sprites/diaren/diaren-idle-4.png').convert_alpha(),
          ],
          'atk_diaren': [
            pygame.image.load('sprites/diaren/atk-diaren-1.png').convert_alpha(),
            pygame.image.load('sprites/diaren/atk-diaren-2.png').convert_alpha(),
            pygame.image.load('sprites/diaren/atk-diaren-3.png').convert_alpha(),
            pygame.image.load('sprites/diaren/atk-diaren-4.png').convert_alpha(),
            pygame.image.load('sprites/diaren/atk-diaren-5.png').convert_alpha(),
          ],
          'dano_diaren': [
            pygame.image.load('sprites/diaren/dano-diaren-1.png').convert_alpha(),
            pygame.image.load('sprites/diaren/dano-diaren-2.png').convert_alpha(),
            pygame.image.load('sprites/diaren/dano-diaren-3.png').convert_alpha(),
            pygame.image.load('sprites/diaren/dano-diaren-4.png').convert_alpha(),
          ],
          'atk2_diaren': [
            pygame.image.load('sprites/diaren/atk2-diaren-1.png').convert_alpha(),
            pygame.image.load('sprites/diaren/atk2-diaren-2.png').convert_alpha(),
            pygame.image.load('sprites/diaren/atk2-diaren-3.png').convert_alpha(),
            pygame.image.load('sprites/diaren/atk2-diaren-4.png').convert_alpha(),
            pygame.image.load('sprites/diaren/atk2-diaren-5.png').convert_alpha(),
            pygame.image.load('sprites/diaren/atk2-diaren-6.png').convert_alpha(),
            pygame.image.load('sprites/diaren/atk2-diaren-7.png').convert_alpha(),
            pygame.image.load('sprites/diaren/atk2-diaren-8.png').convert_alpha(),
            pygame.image.load('sprites/diaren/atk2-diaren-9.png').convert_alpha(),
            pygame.image.load('sprites/diaren/atk2-diaren-10.png').convert_alpha(),
            pygame.image.load('sprites/diaren/atk2-diaren-11.png').convert_alpha(),
            pygame.image.load('sprites/diaren/atk2-diaren-12.png').convert_alpha(),
          ]
          }
        self.estado = 'idle'
        self.frame = 0
        self.velocidade = 0.1

        self.image = self.animacoes[self.estado][0]
        self.rect = self.image.get_rect(topleft=(333, 15))

        self.animacao_terminou = False

    def atk_diaren(self):
        self.estado = 'atk_diaren'
        self.frame = 0
        self.animacao_terminou = False

    def atk2_diaren(self):
        self.estado = 'atk2_diaren'
        self.frame = 0
        self.animacao_terminou = False

    def dano_diaren(self):
      self.estado = 'dano_diaren'
      self.frame = 0
      self.animacao_terminou = False

    def update(self):
        if self.estado == 'atk_diaren':
          self.image = self.animacoes[self.estado][0]
          self.rect = self.image.get_rect(topleft=(380, 15))
        elif self.estado == 'dano_diaren':
          self.image = self.animacoes[self.estado][0]
          self.rect = self.image.get_rect(topleft=(375, 10))
        elif self.estado == 'atk2_diaren':
          self.image = self.animacoes[self.estado][0]
          self.rect = self.image.get_rect(topleft=(333, 15))
        else:
          self.image = self.animacoes[self.estado][0]
          self.rect = self.image.get_rect(topleft=(333, 15))
        self.frame += self.velocidade

        animacao_atual = self.animacoes[self.estado]

        if self.frame >= len(animacao_atual):
            if self.estado == 'atk_diaren':
                self.estado = 'idle'
                self.frame = 0
                matthew.levou_dano()
            if self.estado == 'atk2_diaren':
                self.estado = 'idle'
                self.frame = 0
                matthew.levou_dano()
            elif self.estado == 'dano_diaren':
                self.estado = 'idle'
                self.frame = 0
            else:
                self.frame = 0

        self.image = animacao_atual[int(self.frame)]
        self.image = pygame.transform.scale(self.image, (400, 400))

todas_sprites = pygame.sprite.Group()

diaren = Diaren()
todas_sprites.add(diaren)
matthew = Matthew()
todas_sprites.add(matthew)

largura_da_barra = 150

# FIM DA ÁREA DE BOSS E PERSONAGEM





# ANIMAÇÃO DE ESCURECER A TELA (FADE)
tempo_de_transicao = 3
anim_apagar_tela = pygame.Surface((784, 588))
anim_apagar_tela.fill((0, 0, 0))

apagar_alpha = 0
ordem_do_apagar = 0
# FIM DE ANIMAÇÃO DE ESCURECER A TELA (FADE)


# ANIMAÇÕES DA TELA INICIAL
anim_titulo = 0
direcao = -10
frame_travado = 0

frame_da_anim_play = pygame.time.get_ticks()
tempo_anim_play = 700
visivel = True

fade_tela_inicial = True
# FIM DE ANIMAÇÕES DA TELA INICIAL

# ANIMAÇÕES DAS TELAS FINAIS
frame_da_anim_derrota = pygame.time.get_ticks()
tempo_anim_derrota = 700

frame_da_anim_vitoria = pygame.time.get_ticks()
tempo_anim_vitoria = 700

# FIM DE ANIMAÇÕES DAS TELAS FINAIS


# ÁREA DOS CRÉDITOS
alpha_dos_creditos = 255
estado_fade_creditos = 0

tempo_creditos = pygame.time.get_ticks()
tempo_final_creditos = 2500

matthew__creditos_y = -600
thalis_creditos_y = 600
velocidade_dos_personagens = 2

frame_da_anim_nomes = pygame.time.get_ticks()
tempo_anim_nomes = 450

# FIM DA ÁREA DOS CRÉDITOS



# GERENCIAMENTO DE FASES DO JOGO
momento_tela_inicial = 0
momento_transicao = 1
momento_gameplay = 2
momento_derrota = 3
momento_vitoria = 4
momento_creditos = 5

momento_atual = momento_creditos

vez_do_jogador = 10
vez_do_jogador_anim = 20
vez_do_boss = 30
vez_do_boss_anim = 40

turno_atual = vez_do_jogador

toca_musica_gameplay = False
toca_musica_morte = False

som_dano = pygame.mixer.Sound('dano.mp3')
# FIM DE GERENCIAMENTO DE FASES DO JOGO

sem_anim = 0

while running:

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    
    # CHAVES DO JOGO
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_RETURN:
        if momento_atual == momento_tela_inicial and ordem_do_apagar != 1:
          ordem_do_apagar = 1
          apagar_alpha = 0
        if momento_atual == momento_derrota or momento_atual == momento_vitoria:
          ordem_do_apagar = 1
          apagar_alpha = 0
    
    if event.type == pygame.MOUSEBUTTONDOWN:
      if momento_atual == momento_gameplay:
        if turno_atual == vez_do_jogador:
          for skill_clicada in skills:
            if skill_clicada['posicao'].collidepoint(event.pos):
              if skill_clicada['nome'] == 'Infoweb':
                if cooldown >= 2:
                  random.shuffle(skill_clicada['danos'])
                  dano_do_turno = skill_clicada['danos'][1]
                  matthew.atk_info()         
                  turno_atual = vez_do_jogador_anim
              elif skill_clicada['nome'] == 'Adm':
                Boss['danos'][0] //= 2
                Boss['danos'][1] //= 2
                Boss['danos'][2] //= 2
                # Tira todos os danos do boss
                matthew.atk_adm()
              elif skill_clicada['nome'] == 'MSI':
                random.shuffle(skill_clicada['danos'])
                dano_do_turno = skill_clicada['danos'][1]
                matthew.atk_msi()
                turno_atual = vez_do_jogador_anim


  
  
  posicao_do_mouse = pygame.mouse.get_pos()

  frame_agora_play = pygame.time.get_ticks()
  frame_agora_hover = pygame.time.get_ticks()
  frame_agora_derrota = pygame.time.get_ticks()
  frame_agora_vitoria = pygame.time.get_ticks()
  frame_agora_nomes = pygame.time.get_ticks()


  conferir_momento_funcao()

  animacoes_e_final_de_jogo()


  pygame.display.flip()

  clock.tick(60)

pygame.quit()