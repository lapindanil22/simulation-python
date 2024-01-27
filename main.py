import pygame

from entities import Grass, Tree, Rock, Herbivore, Predator
from simulation import Simulation

population = {
    Grass: 500,
    Tree: 50,
    Rock: 50,
    Herbivore: 5,
    Predator: 2
}

if __name__ == "__main__":
    pygame.init()
    simulation = Simulation(map_size=(80, 60), cell_size_px=10)
    simulation.start(population=population, fps_limit=10)
