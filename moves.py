from maze import START , END , MAZE , ROWS , COLS 
DIRECTIONS = ['UP' , 'DOWN' , 'LEFT' , 'RIGHT']

def apply_move(position , move, maze):
    x,y = position
    rows , cols = len(maze) , len(maze[0])

    if move == 'UP' and y>0 and maze[y-1][x] ==0:
        return (x,y-1)
    elif move=='DOWN' and y<rows-1 and maze[y+1][x] ==0:
        return (x,y+1)
    elif move=='LEFT' and x>0 and maze[y][x-1]==0:
        return (x-1,y)
    elif move=='RIGHT' and x<cols-1 and maze[y][x+1]==0:
        return (x+1,y)
    return (x,y) #no move if blocked or invalid

def reaches_end(individual):
        x, y = START
        for move in individual.genes:
            if (x, y) == END:
                return True
            if move == 'UP' and y > 0 and MAZE[y-1][x] == 0:
                y -= 1
            elif move == 'DOWN' and y < ROWS - 1 and MAZE[y+1][x] == 0:
                y += 1
            elif move == 'LEFT' and x > 0 and MAZE[y][x-1] == 0:
                x -= 1
            elif move == 'RIGHT' and x < COLS - 1 and MAZE[y][x+1] == 0:
                x += 1
        return (x, y) == END 
    