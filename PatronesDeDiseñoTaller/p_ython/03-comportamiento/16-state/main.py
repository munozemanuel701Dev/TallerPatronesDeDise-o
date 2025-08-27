from context import MusicPlayer
from state import PausedState
from state import PlayerState
from state import StoppedState

def main():
    
    player = MusicPlayer()
    player.press_play()
    player.press_play()
    player.press_play()
    player.press_play()
    
if __name__ == '__main__':
    main()