import pygame

from entity import Grass, Herbivore, Predator, Tree, Rock
from simulation import Simulation

population = {
    Grass: 500,
    Herbivore: 5,
    Predator: 2,
    Tree: 50,
    Rock: 50
}
map_size = (80, 60)
cell_size_px = 10
fps_limit = 10

if __name__ == "__main__":
    pygame.init()
    simulation = Simulation(map_size, cell_size_px)
    simulation.start(population, fps_limit)
