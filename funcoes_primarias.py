#Vinicius Camargo Reis | Raciocionio Computacional | ATP2-2022 | Nome: Zombie Dice
from time import sleep
import random
import os

def numeroJogadores(qtd_jogadores, confirma):
  """
  Pergunta a quantidade de jogadores. Se a quantidade for menor que 2 ele repetira a pergunta se for maior continua
  """
  confirmado = False
  while confirmado == False: #o codigo vai continuar rodando a menos que chegue no elif
    qtd_jogadores = int(input("\n\tQuantos \033[1;31mZombies\033[m vão participar? "))
    confirma = input("\tVão participar {}{}{} Zombies. Esta certo? [sim/não]: ".format("\033[31m",qtd_jogadores,"\033[m")).strip().lower()  
   

    if qtd_jogadores < 2: #caso tenha menos que 2 jogadores voltara em comfirmar =
      print("\n\tVocê não tem a minima chance sozinho!\n\tVolte mais tarde, com mais Zombies...\n") 
      continue
    
    elif confirma == "sim": #se a pessoa responder sim quebra o loop
      return qtd_jogadores 
      break

def nomeJogadores(qtd_jogadores):
  """
  Cria lista com os nomes dos jogadores e 3 listas de pontos para cada nome 
  """
  #lista de pontos
  lista_pontos_c = []
  lista_pontos_p = []
  lista_pontos_t = []
  #lista de nomes dos jogadores
  lista_jogadores = [] 
  contador1 = 0  #contador para a função while
  while contador1 < qtd_jogadores:
    lista_jogadores.append(input("\n\tColoque o nome do jogador {}: ".format(contador1 + 1)))
    lista_pontos_c.append(0)
    lista_pontos_p.append(0)
    lista_pontos_t.append(0)
    contador1 += 1

  return lista_pontos_c, lista_pontos_p, lista_pontos_t, lista_jogadores


def sorteioJogadores(lista_jogadores):
  """
  vai sortear um dos jogadores e retornar com um na variavel jogador_vez
  """
  os.system("cls")
  jogador_vez = random.randint(0, len(lista_jogadores)- 1) #sortear o primeiro jogador 
  print("\n\t\033[33m{}\033[m vai ser o \033[1;31mZombie\033[m da vez".format(lista_jogadores[jogador_vez]))
  return jogador_vez

def lista_cores():
  """
  criara o copo de dados
  """
  return ["Vermelho","Vermelho","Vermelho", "Amarelo","Amarelo","Amarelo","Amarelo", "Verde","Verde","Verde","Verde","Verde","Verde"]

def lista_face_verde():
  """
  criara as faces do dado verde
  """    
  return ["cerebro", "passo", "cerebro", "tiro","passo","cerebro"]

def lista_face_amarelo():
  """
  criara as faces do dado amarelo
  """  
  return ["tiro", "passo", "cerebro", "tiro","passo","cerebro"]

def lista_face_vermelho():
  """
  criara as faces do dado vermelho
  """  
  return ["tiro", "passo", "tiro", "cerebro","passo","tiro"]


def sortearDados(lista_cores, cores_sorteadas):
  """
  vai sortear a cor de um numero x de dados que depende de quantos estiveres na lista cores_sorteadas
  """
  if(len(cores_sorteadas) == 0 ):
    for i in range(0, 3):
      index_cores = random.randint(0, len(lista_cores) - 1)
      cores_sorteadas.append(lista_cores[index_cores]) #sorteando cor e colocando na lista 
  
  elif(len(cores_sorteadas) == 1 ):
    for i in range(0, 2):
      index_cores = random.randint(0, len(lista_cores) - 1)
      cores_sorteadas.append(lista_cores[index_cores]) #sorteando cor e colocando na lista 
  
  elif(len(cores_sorteadas) == 2 ):
    for i in range(0, 1):
      index_cores = random.randint(0, len(lista_cores) - 1)
      cores_sorteadas.append(lista_cores[index_cores]) #sorteando cor e colocando na lista 

  else:
    for i in range(0, 1):
      break
  return cores_sorteadas

def sortearFaces_verde(lista_face_verde, faces_sorteadas):
  """
  sortea a face do dado se ele for verde
  """
  index_faces = random.randint(0, len(lista_face_verde)- 1) #se o dado da ultima posição for verde o jogo sorteara esse
  faces_sorteadas.append(lista_face_verde[index_faces])
  return faces_sorteadas, index_faces

def sortearFaces_amarelo(lista_face_amarelo, faces_sorteadas):
  """
  sortea a face do dado se ele for amarelo
  """
  index_faces = random.randint(0, len(lista_face_amarelo)- 1) #se o dado da ultima posição for amarelo o jogo sorteara esse
  faces_sorteadas.append(lista_face_amarelo[index_faces])
  return faces_sorteadas, index_faces

def sortearFaces_vermelho(lista_face_vermelho, faces_sorteadas):
  """
  sortea a face do dado se ele for vermelho
  """
  index_faces = random.randint(0, len(lista_face_vermelho)- 1) #se o dado da ultima posição for verde o jogo sorteara esse
  faces_sorteadas.append(lista_face_vermelho[index_faces])
  return faces_sorteadas, index_faces

def contarPontos(faces_sorteadas, lista_pontos_c, lista_pontos_p, lista_pontos_t, jogador_vez, cerebros_rodada, index_faces):
  """
  vai fazer a contagem de pontos de cada jogador
  """
  if faces_sorteadas[index_faces] == "cerebro":
      lista_pontos_c[jogador_vez] += 1
      cerebros_rodada += 1

  elif faces_sorteadas[index_faces] == "passo":
      lista_pontos_p[jogador_vez] += 1

  elif faces_sorteadas[index_faces] == "tiro":
      lista_pontos_t[jogador_vez] += 1

  return lista_pontos_c, lista_pontos_p, lista_pontos_t, cerebros_rodada

def tresTiros(lista_pontos_c, lista_pontos_p, lista_pontos_t, jogador_vez, cerebros_rodada):
  """
  vai ser acionada caso o jogador leve 3 tiros. Vai tirar os pontos de cerebro da jogada e retorna as listas
  """
  print("\n\tVocê levou 3 tiros, seus pontos não serão contabilizados e sua rodada acabou!")
  sleep(3)
  lista_pontos_t[jogador_vez] = 0
  lista_pontos_p[jogador_vez] = 0
  lista_pontos_c[jogador_vez] = lista_pontos_c[jogador_vez] - cerebros_rodada #não vai contabilizar o c da rodada
  cerebros_rodada = 0
  return lista_pontos_c, lista_pontos_p, lista_pontos_t, cerebros_rodada

def passaVez(jogador_vez, lista_jogadores):
  """
  passa a vez para o proximo jogador
  """
  if jogador_vez == len(lista_jogadores)- 1:
    jogador_vez = 0
    os.system("cls") 
  else:
    jogador_vez += 1
    os.system("cls")
  return jogador_vez

def vencedor(lista_jogadores, jogador_vez):
  """
  criterio de vitoria
  """
  print(f"\n\t\033[32mPARABÉNS!!!\033[m O \033[31mZombie\033[m {lista_jogadores[jogador_vez]} ganhou o jogo.\n")
  print("\033[1;31m-=-\033[m" * 100)
  quit()
    
def manterDados(faces_sorteadas,cores_sorteadas):
  """
  mantem os dados na mesa caso o dado caia em passo e o jogador queira continuar
  """
  listaPassos = []
  for i in range(0,3):
    if (faces_sorteadas[i] == "passo"):
      listaPassos.append(cores_sorteadas[i])
  
  cores_sorteadas.clear()
  cores_sorteadas = listaPassos
  print("\n\tdados mantidos da ultima jogada")
  sleep(1)
  if(len(cores_sorteadas) > 0):
    for i in cores_sorteadas:
      print(f"\t{i}")
      
  else:
    print("\n\tnenhum dado matido na mesa")
  
  sleep(2)
  return cores_sorteadas



