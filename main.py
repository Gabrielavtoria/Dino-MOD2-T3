from dino_runner.components.game import Game

musica_de_fundo = pygame.mixer.music.load('BoxCat Games - CPU Talk.mp3')
pygame.mixer.music.play(-1)

if __name__ == "__main__":
    game = Game()
    game.execute()
