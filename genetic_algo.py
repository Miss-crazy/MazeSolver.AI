import random 
from moves import DIRECTIONS , apply_move 
from maze import MAZE , START , END 

class Individual :
    def __init__(self, gene_length = 100):
        self.genes = [random.choice(DIRECTIONS) for _ in range(gene_length)]
        self.fitness = 0
        
    def move(self):
        pos = START 
        for m in self.genes:
            pos = apply_move(pos , m , MAZE)
        return pos 
    def calculate_fitness(self):
        pos = self.move()
        end_x , end_y = END
        dist = abs(pos[0] - end_x)+abs(pos[1]- end_y)
        self.fitness = 1/(dist+1)
    
def crossover(parent1 , parent2):
    split = random.randint(1 , len(parent1.genes)-1)
    child = Individual()
    child.genes = parent1.genes[:split] + parent2.genes[split:]
    return child 

def mutate(individual , mutation_rate = 0.01):
    for i in range(len(individual.genes)):
        if random.random() < mutation_rate :
            individual.genes[i] = random.choice(DIRECTIONS)
            
def selection(population):
    population.sort(key = lambda ind: ind.fitness , reverse =True)
    return population[:len(population)//2]
