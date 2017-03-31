"""MAIN."""

import random

from constants import *

random.seed()


def main():
    """Main execution."""

    game = SteeringBehavior("A Star")
    pygame.mixer.init()
    pygame.mixer.music.load("music.mp3")
    pygame.mixer.music.play()
    pygame.mixer.music.set_volume(0.1)
    game.run()



if __name__ == "__main__":
    main()
