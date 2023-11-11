import pygame

from entity import Grass, Herbivore, Predator, Tree, Rock
from simulation import Simulation

population = {
    Grass: 200,
    Herbivore: 10,
    Predator: 1,
    Tree: 50,
    Rock: 50
}

if __name__ == "__main__":
    pygame.init()
    simulation = Simulation((64, 48))
    simulation.start(population)
