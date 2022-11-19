#Vinicius Camargo Reis | Raciocionio Computacional | ATP2-2022 | Nome: Zombie Dice
from time import sleep
import random
import os

def apresentacao():
  """
  inicializa cabeçaçho e apaga informações superiores
  """
  os.system("cls")
  print("\033[31m=\033[m" * 100) #usei o codigo \033[m para aplicar uma cor na str e repiti 30 vezes
  print("\t\033[1;31mZombie Dice\033[m")
  print("\033[31m=\033[m" * 100)

  print("\n\tInicializando...\n")
  sleep(2) #vai esperar 2 segundos para continuar


def regrasDeJogo():
  """
  Perguta ao jogador se ele gostaria de ler as regras. caso a resposta seja sim ele imprime as regras, caso seja não somente pula
  """
  regras = input("\tGostaria de ler as regras do jogo? Responda com sim ou não: ").strip().lower()
  if regras == "sim" or regras == "s":
    print("\n\t Coma 13 cerebros e ganhe o jogo. Caso o jogador leve 3 tiros na rodada, sua vez será passada\n\t e seus pontos da rodada não serão contabilizados. Boa sorte!!!") #colocar regras do jogo em """


def inicializar():
  """
  animação
  """
  print("\n\tInicializando rodada...\n")
  sleep(2)
  os.system("cls")

def sorteandoDados():
  """
  animação
  """
  os.system("cls")    
  print("\n\tsorteando os dados...")
  sleep(2)
  os.system("cls")

def resultadoJogada(lista_jogadores, jogador_vez, cores_sorteadas, faces_sorteadas, lista_pontos_c, lista_pontos_p, lista_pontos_t):
  """
  imprime os resultados da jogada
  """
  print(f"\n\tVez do \033[1;31mZombie\033[m {lista_jogadores[jogador_vez]}")
  sleep(2)
  print(f"\n\tO primeiro dado era {cores_sorteadas[0]} e caiu com a face {faces_sorteadas[0]}")
  sleep(1)
  print(f"\tO segundo dado era {cores_sorteadas[1]} e caiu com a face {faces_sorteadas[1]}")
  sleep(1)
  print(f"\tO terceiro dado era {cores_sorteadas[2]} e caiu com a face {faces_sorteadas[2]}")
  sleep(1)    
  print(f"\n\t\033[32mCerebros = {lista_pontos_c[jogador_vez]}\033[m | \033[33mPassos = {lista_pontos_p[jogador_vez]}\033[m | \033[31mTiros = {lista_pontos_t[jogador_vez]}\033[m\n")
  