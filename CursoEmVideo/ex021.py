""""
faca um programa que abre e reproduza
o audio de um arquivo MP3.
"""
import pygame
pygame.init()
pygame.mixer.music.load('C:/Users/Welson/Documents/Development/EstudosPython/Arquivos_Aulas/mag.mp3')
pygame.mixer.music.play()
pygame.event.wait()
input()





