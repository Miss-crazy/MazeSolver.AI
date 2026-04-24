# MazeSolver.AI

A **Genetic Algorithm-based Maze Solver** that searches for a path through a maze by simulating evolution.  
The project visualizes the maze-solving process on screen and reports progress in the terminal until a solution is found.

![Maze Solver](images/maze solver.jpg)

> Example terminal output:
> `Solution found at generation 9 ! Fitness: 0.3333333333333333`

---

## Overview

MazeSolver.AI is an AI-inspired pathfinding project that uses a genetic algorithm to evolve candidate routes through a maze.  
Instead of using classical search only, the solver treats possible paths like a population of individuals, improves them over generations, and gradually converges toward a valid solution.

The result is displayed visually with the maze, explored path, and final solution path highlighted on screen.  
This makes the project useful both as a learning tool and as a demonstration of evolutionary computation in action.

---

## How It Works

The solver follows the standard genetic algorithm workflow:

1. **Initialize a population** of random candidate paths.
2. **Evaluate fitness** based on how close each path gets to the goal and how valid the movement is.
3. **Select the best candidates** to act as parents.
4. **Perform crossover** to combine path segments from strong candidates.
5. **Apply mutation** to introduce variation and avoid premature convergence.
6. **Repeat across generations** until a valid path reaches the goal.

A solution is reported when the algorithm finds a path that successfully reaches the destination, along with its generation number and fitness score.  
For example, your run shows the solver finding a solution at generation 9 with fitness `0.3333333333333333`, which confirms the evolutionary search successfully converged [file:1].

---

## Project Build

This project was built by combining maze representation, evolutionary search, and graphical visualization.  
The maze is encoded in a format the algorithm can process, and each candidate solution is evaluated against the maze walls and the target endpoint.

The implementation typically includes:
- Maze grid setup.
- Path encoding for each individual in the population.
- Fitness function to score solutions.
- Selection, crossover, and mutation operators.
- A rendering layer to display the maze and the final path.



---

## Features

- Genetic algorithm-based maze solving.
- Generation-by-generation progress reporting.
- Fitness-based evolution of candidate paths.
- On-screen visualization of the solution.
- Terminal output showing when the solution is found.
- Useful for experimenting with mutation, crossover, and fitness tuning.

---

## Example Output

When the solver succeeds, it may print something like:

```bash
Solution found at generation 9 ! Fitness: 0.3333333333333333
```

The visualization then highlights the found route through the maze, making the result easy to understand at a glance [file:1].

---


**Reference:**  
Maze Navigation via Genetic Optimization. Scientific Research Publishing. [web:7]

---

## Applications

Maze solving with genetic algorithms has practical and educational applications:

- **Path planning in robotics**, where an agent must navigate an environment.
- **Game AI**, for enemy movement or route selection.
- **Optimization research**, to study evolutionary search techniques.
- **Education**, as a visual example of genetic algorithms.
- **Autonomous navigation**, where route selection is part of a larger decision-making system.

These applications make the project useful beyond a simple maze demo, since the same approach can be adapted to real optimization and navigation problems [web:7][web:8].

---

## Technologies Used

- Python
- Genetic Algorithm concepts
- Visualization library used in the project
- Maze/grid-based path representation

---

## How to Run

```bash
git clone https://github.com/Miss-crazy/MazeSolver.AI.git
cd MazeSolver.AI
pip install requirements.txt
python main.py
```

If your entry file has a different name, replace `main.py` with the correct script.

---

## Future Improvements

- Better fitness function for faster convergence.
- Smarter mutation and crossover strategies.
- Support for larger and more complex mazes.
- Step-by-step animation of population evolution.
- Performance comparison with BFS, DFS, and A*.

---

## Acknowledgment

This project demonstrates how evolutionary algorithms can be applied to maze navigation and pathfinding.  
The visual output and terminal feedback make it a strong example of AI-inspired problem solving.

