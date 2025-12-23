import pygame
import sys 
import random 
from maze import  MAZE , START , END , ROWS , COLS
from genetic_algo import Individual , crossover , mutate , selection 
from moves import reaches_end

#pygame setting 
WIDTH , HEIGHT = 600 , 600 
CELL_SIZE = WIDTH // COLS 

def draw_maze(win , maze):
    for y in range(ROWS):
        for x in range(COLS):
            color = (0,0,0) if maze[y][x]==1 else (255, 55, 150)
            pygame.draw.rect(win , color ,(x*CELL_SIZE , y*CELL_SIZE , CELL_SIZE , CELL_SIZE))

def draw_path(win , individual ):
    x , y = START 
    for move in individual.genes:
        pos = (x*CELL_SIZE + CELL_SIZE//2 , y*CELL_SIZE + CELL_SIZE//2)
        if move=='UP' and y>0 and MAZE[y-1][x]==0 :
            y-=1
        elif move == 'DOWN' and y < ROWS-1 and MAZE[y+1][x] == 0:
            y += 1
        elif move == 'LEFT' and x > 0 and MAZE[y][x-1] == 0:
            x -= 1
        elif move == 'RIGHT' and x < COLS-1 and MAZE[y][x+1] == 0:
            x += 1
        pygame.draw.circle(win , (255,255,255),pos, CELL_SIZE//4)

def main():
    pygame.init()
    win = pygame.display.set_mode((WIDTH , HEIGHT))
    pygame.display.set_caption("GENETIC ALGORITHM MAZE SOLVER")

    population_size = 100 
    gene_length = 100 
    generations = 200
    mutation_rate  = 0.01

    population = [Individual(gene_length)for _ in range(population_size)]
    clock = pygame.time.Clock()

    for gen in range(generations):
        #calculate fitness
        for ind in population:
            ind.calculate_fitness()
        solution_found =False
        best_solution = None
        for ind in population :
            if reaches_end(ind):
                solution_found = True
                best_solution = ind
                print(f"Solution found at generation {gen} ! Fitness: {ind.fitness}")
                break
            
        if solution_found:
            win.fill((255,255,255))
            draw_maze(win , MAZE)
            draw_path(win , best_solution)

            #add success text
            font = pygame.font.SysFont(None,48)
            text = font.render("SOLUTION FOUND!",True,(255,255,255))
            win.blit(text , (WIDTH//2-150 , 20))
            pygame.display.flip()

            #keep window open until user closes it 
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()

        #selection 
        population = selection(population)
        next_gen = []
        #crossover and mutate 
        while len(next_gen)<population_size:
            parent1 , parent2 = random.sample(population , 2)
            child = crossover(parent1 , parent2)
            mutate(child , mutation_rate)
            next_gen.append(child)
        population = next_gen

        #draw maze and best individual path 
        win.fill((255,255,255))
        draw_maze(win , MAZE)
        best = max(population , key = lambda ind:ind.fitness)
        draw_path(win , best)
        
        pygame.display.flip()
        clock.tick(5)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

if __name__ =="__main__":
    main()


