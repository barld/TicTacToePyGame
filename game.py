import pygame


class Tile:
    def __init__(self, f, x, y):
        self.posX = x
        self.posY = y
        self.state = "-"
        self.onClick = f
        self.rect = None

    def update(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN and self.rect is not None and self.rect.collidepoint(pygame.mouse.get_pos()):
                print("click %i %i" % (self.posX, self.posY))
                self.onClick(self)

    def draw(self, screen):
        self.rect = pygame.draw.rect(screen, (255,255,255), [self.posX * 102,self.posY * 102,100,100])

        # Create a font
        font = pygame.font.Font(None, 100)
        # Render the text
        text = font.render(self.state, True, (255,255,0))
        # Blit the text
        screen.blit(text, [self.posX * 102 + 40,self.posY * 102+18])

class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol



class Game:
    def __init__(self, player1:Player, player2:Player):
        def f(tile):
            if tile.state == "-":
                tile.state = self.currentPlayer.symbol
                self.currentPlayer = player1 if self.currentPlayer.symbol == player2.symbol else player2

        self.currentPlayer = player1

        self.board = [[Tile(f, j, i) for j in range(0,3)] for i in range(0,3)]


    def update(self, events):
        for row in self.board:
            for tile in row:
                tile.update(events)

        return self

    def draw(self, screen):
        for row in self.board:
            for tile in row:
                tile.draw(screen)

        # need code to check if there is a winner
        text = "it is player: %s turn" % self.currentPlayer.name

        # Create a font
        font = pygame.font.Font(None, 80)
        # Render the text
        text = font.render(text, True, (255, 255, 255))
        # Blit the text
        screen.blit(text, [25, 400 + 18])