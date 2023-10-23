import pygame


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
