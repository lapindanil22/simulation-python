from abc import ABC, abstractmethod

import pygame


class Entity(ABC):
    pass


class Creature(Entity):
    @abstractmethod
    def make_move(self):
        pass


class Predator(Creature):
    color = "red"

    def make_move(self):
        ...

    def do_attack(self):
        ...


class Herbivore(Creature):
    color = "green"

    def make_move(self):
        ...

    def do_eat(self):
        ...


class Grass(Entity):
    color = "olivedrab"


class Rock(Entity):
    color = "darkgray"


class Tree(Entity):
    color = "saddlebrown"


class Map:
    def __init__(self, size) -> None:
        self.size = size
        self.map = {}

    def set_entity(self, coords, entity):  # TODO boundary check
        self.map[coords] = entity

    def as_dict(self):
        return self.map


class Simulation:
    entity_size = 10

    def __init__(self, map) -> None:
        self.epochs_counter = 0
        self.__map = map
        pygame.init()
        self.screen = pygame.display.set_mode((self.__map.size[0] * self.entity_size,
                                               self.__map.size[1] * self.entity_size))

    def get_map(self):
        return self.__map

    def render(self):
        for coords, entity in self.get_map().as_dict().items():
            pygame.draw.rect(self.screen, entity.color, (coords[0] * self.entity_size,
                                                         coords[1] * self.entity_size,
                                                         self.entity_size,
                                                         self.entity_size))

        pygame.display.update()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            # print(simulation.get_map().as_dict())
            self.render()
            pygame.time.delay(1000)


if __name__ == "__main__":
    simulation = Simulation(Map((64, 48)))

    simulation.get_map().set_entity((14, 34), Predator())
    simulation.get_map().set_entity((15, 35), Herbivore())
    simulation.get_map().set_entity((23, 35), Tree())
    simulation.get_map().set_entity((24, 36), Grass())
    simulation.get_map().set_entity((25, 37), Rock())

    simulation.run()
