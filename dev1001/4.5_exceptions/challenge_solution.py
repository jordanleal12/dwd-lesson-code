class GameError(Exception):
    pass

class InvalidCommand(GameError):
    pass

class LowHealth(GameError):
    pass

class GameEngine:
    def __init__(self, player_health):
        self.health = player_health

    def run_turn(self, command, data_file):
        try:
            with open(data_file, "r") as f:
                data = f.read()
            if command not in ["look", "move", "attack"]:
                raise InvalidCommand(f"Unknown command: {command}")
            if self.health < 10:
                raise LowHealth("Health is dangerously low.")
            print(f"Command {command} with data: {data}")
        except FileNotFoundError:
            print("Turn failed: Missing game data.")
        except InvalidCommand as ic:
            print(f"Turn failed: {ic}")
        except LowHealth as lh:
            print(f"Turn failed: {lh}")
        except Exception as e:
            print(f"Unexpected error: {e}")
