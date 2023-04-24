import pygame
import colors
from params import *
from Environment import Board
from Agent import Agent

# initialize:
FPS = 60
pygame.init()
WIN = pygame.display.set_mode((width, height))
pygame.display.set_caption("Search Game")

# setting start and end point :
start = {'x': 6, 'y': 0}
end = {'x': 12, 'y': 0}

gameBoard = Board(start, end)
agent = Agent(gameBoard)



def main():
    req = input("Enter your request number => [1:bfs, 2:dfs, 3:a_star]:")
    req = int(req)
    run = True
    clock = pygame.time.Clock()
    WIN.fill(colors.black)

    NEW_bfs = False
    NEW_dfs = False
    NEW_a = False
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            gameBoard.draw_world(WIN)
            pos = pygame.mouse.get_pos()  # gets the current mouse coords
            if event.type == pygame.MOUSEBUTTONDOWN:
                for i in range(rows):
                    for j in range(cols):
                         rect = gameBoard.boardArray[i][j]
                         if rect.is_inside_me(pos):
                            if event.button == 1:
                                gameBoard.boardArray[i][j].block()
                                if req==1 :
                                    NEW_bfs=True
                                elif req==2 :
                                    NEW_dfs=True
                                elif req==3 :
                                    NEW_a=True
                            if event.button == 3:
                                gameBoard.boardArray[i][j].unblock()
                                if req == 1:
                                    NEW_bfs = True
                                elif req == 2:
                                    NEW_dfs = True
                                elif req == 3:
                                    NEW_a = True
        # agent.bfs(gameBoard)
        if NEW_bfs:
         agent.bfs(gameBoard)
         NEW_bfs = False
        if NEW_dfs:
            agent.dfs(gameBoard)
            NEW_dfs=False
        if NEW_a:
            agent.a_star(gameBoard)
            NEW_a=False
    pygame.quit()

main()
