from map import Map
from simulation import Simulation

if __name__ == "__main__":
    cells = Map((64, 48))
    simulation = Simulation(cells)
    simulation.start_simulation()
