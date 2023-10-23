from map import Map
from simulation import Simulation
from entity import *

if __name__ == "__main__":
    simulation_map = Map((64, 48))
    simulation = Simulation(simulation_map)

    simulation_map.set_entity((14, 34), Predator())
    simulation_map.set_entity((15, 35), Herbivore())
    simulation_map.set_entity((23, 35), Tree())
    simulation_map.set_entity((24, 36), Grass())
    simulation_map.set_entity((25, 37), Rock())

    # simulation.get_map().clear_cell((23, 36))
    simulation_map.move_entity((14, 34), (20, 34))

    simulation.run()
