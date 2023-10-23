from map import Map
from simulation import Simulation
from entity import *

if __name__ == "__main__":
    simulation = Simulation(Map((64, 48)))

    simulation.get_map().set_entity((14, 34), Predator())
    simulation.get_map().set_entity((15, 35), Herbivore())
    simulation.get_map().set_entity((23, 35), Tree())
    simulation.get_map().set_entity((24, 36), Grass())
    simulation.get_map().set_entity((25, 37), Rock())

    simulation.run()
