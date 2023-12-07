from project import gameloop,main,gameover,playsound
import pytest
import pygame
import sys

pygame.init()

def test_gameloop():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            with pytest.raises(SystemExit):
                gameloop()

def test_main():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            with pytest.raises(SystemExit):
                main()

def test_gameover():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            with pytest.raises(SystemExit):
                gameover()

def test_playsound():
    with pytest.raises(SystemExit):
        playsound()

if __name__ == "__main__":
    main()