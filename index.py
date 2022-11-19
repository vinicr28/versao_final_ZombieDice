#Vinicius Camargo Reis | Raciocionio Computacional | ATP2-2022 | Nome: Zombie Dice

from time import sleep
import random
import os

import funcoes_primarias
import funcoes_secundarias

funcoes_secundarias.apresentacao()

funcoes_secundarias.regrasDeJogo()

qtd_jogadores = funcoes_primarias.numeroJogadores(0, confirma = False)
os.system("cls")

lista_pontos_c, lista_pontos_p, lista_pontos_t, lista_jogadores = funcoes_primarias.nomeJogadores(qtd_jogadores)

jogador_vez = funcoes_primarias.sorteioJogadores(lista_jogadores)

funcoes_secundarias.inicializar()

lista_cores = funcoes_primarias.lista_cores()
lista_face_verde = funcoes_primarias.lista_face_verde()
lista_face_amarelo = funcoes_primarias.lista_face_amarelo()
lista_face_vermelho = funcoes_primarias.lista_face_vermelho()

########### listas sorteadas ##############
index_cores = 0
index_faces = "n"
continuar = "s"
cerebros_rodada = 0# vai ser adicionado quantos cerebros o jogador da vez comeu 
passos_rodada = 0
cores_sorteadas = [] 

while continuar == "s": #repetição da jogada
    
    faces_sorteadas = []
    
    cores_sorteadas = funcoes_primarias.sortearDados(lista_cores, cores_sorteadas) #mudar para sem ser teste
      
    for i in range(0, 3):
      if cores_sorteadas[i] == "Verde":
        faces_sorteadas, index_faces = funcoes_primarias.sortearFaces_verde(lista_face_verde, faces_sorteadas)
        lista_pontos_c, lista_pontos_p, lista_pontos_t, cerebros_rodada = funcoes_primarias.contarPontos(faces_sorteadas, lista_pontos_c, lista_pontos_p, lista_pontos_t, jogador_vez, cerebros_rodada, i)
        
      elif cores_sorteadas[i] == "Amarelo":
        faces_sorteadas, index_faces = funcoes_primarias.sortearFaces_amarelo(lista_face_amarelo, faces_sorteadas)
        lista_pontos_c, lista_pontos_p, lista_pontos_t, cerebros_rodada = funcoes_primarias.contarPontos(faces_sorteadas, lista_pontos_c, lista_pontos_p, lista_pontos_t, jogador_vez, cerebros_rodada, i)
        
      elif cores_sorteadas[i] == "Vermelho":
        faces_sorteadas, index_faces = funcoes_primarias.sortearFaces_vermelho(lista_face_vermelho, faces_sorteadas)
        lista_pontos_c, lista_pontos_p, lista_pontos_t, cerebros_rodada = funcoes_primarias.contarPontos(faces_sorteadas, lista_pontos_c, lista_pontos_p, lista_pontos_t, jogador_vez, cerebros_rodada, i)
        
    funcoes_secundarias.sorteandoDados()
    funcoes_secundarias.resultadoJogada(lista_jogadores, jogador_vez, cores_sorteadas, faces_sorteadas, lista_pontos_c, lista_pontos_p, lista_pontos_t) 

    if lista_pontos_t[jogador_vez] >= 3: #condições caso o jogador leve 3 tiros
      lista_pontos_c, lista_pontos_p, lista_pontos_t, cerebros_rodada = funcoes_primarias.tresTiros(lista_pontos_c, lista_pontos_p, lista_pontos_t, jogador_vez, cerebros_rodada)
      jogador_vez = funcoes_primarias.passaVez(jogador_vez, lista_jogadores)
      cores_sorteadas = []
      continue

    if lista_pontos_c[jogador_vez] >= 13:
      funcoes_primarias.vencedor(lista_jogadores, jogador_vez)  

    resposta_continuar = input("\n\tGostaria de tentar a sorte mais uma vez? " )

    if resposta_continuar == "sim" or resposta_continuar == "s": # se o jogador responder sim, ele jogara novamente
      cores_sorteadas = funcoes_primarias.manterDados(faces_sorteadas,cores_sorteadas)
      
      os.system("cls")

    else:
        cerebros_rodada = 0
        cores_sorteadas = [] #vai zerar as listas sempre que der o looping
        
        if jogador_vez == len(lista_jogadores)- 1:
            lista_pontos_t[jogador_vez] = 0
            lista_pontos_p[jogador_vez] = 0
            jogador_vez = 0
        else:
            lista_pontos_t[jogador_vez] = 0
            lista_pontos_p[jogador_vez] = 0            
            jogador_vez += 1
        

            