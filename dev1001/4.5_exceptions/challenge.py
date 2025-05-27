'''
Task:
Fix the GameEngine.run_turn() method. It loads data from a file, interprets a command, and checks health. Use:

- try...except
- specific error types
- custom exception
- raise
'''
class GameError(Exception):
    pass

class GameEngine:
    def __init__(self, player_health):
        self.health = player_health

    def run_turn(self, command, data_file):
        # You complete this
        pass

engine = GameEngine(5)
engine.run_turn("jump", "bad_file.txt")
