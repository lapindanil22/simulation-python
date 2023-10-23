import pygame
# from action import PlaceEntities
import actions


class Simulation:
    entity_size = 10

    def __init__(self, cells) -> None:
        self.epochs_counter = 0
        self.__cells = cells
        pygame.init()
        self.screen = pygame.display.set_mode((self.__cells.size[0] * self.entity_size,
                                               self.__cells.size[1] * self.entity_size))

    def get_cells(self):
        return self.__cells

    def render(self):
        # self.screen.fill("black")
        pygame.draw.rect(self.screen, "black",
                         (0, 0, self.__cells.size[0] * self.entity_size, self.__cells.size[1] * self.entity_size))
        for coords, entity in self.get_cells().as_dict().items():
            pygame.draw.rect(self.screen, entity.color, (coords[0] * self.entity_size,
                                                         coords[1] * self.entity_size,
                                                         self.entity_size,
                                                         self.entity_size))

        pygame.display.update()

    def next_turn(self):
        actions.move_all_entities(self.get_cells())
        self.render()

    def pause_simulation(self):
        pygame.quit()
        quit()

    def start_simulation(self):

        actions.place_entities(self.get_cells())

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.pause_simulation()

            self.next_turn()
            pygame.time.delay(1000)
