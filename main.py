# ------------ imports ------------
import os
from character import Hero, Enemy, enemies
from weapon import short_bow, iron_sword

# ------------ setup ------------
hero = Hero(name="Hero", health=200)
hero.equip(iron_sword)
# enemy = Enemy(name="Enemy", health=100, weapon=short_bow)


# ------------ game class ------------
class Game:
    def __init__(self):
        self.running = True

    @staticmethod
    def clear() -> None:
        os.system("cls")

    @staticmethod
    def spawn_enemy() -> Enemy:
        Game.clear()
        if enemies:
            enemy = enemies[0]
            input(f"Spawning {enemy.name}...")
            return enemy
        else:
            input("YOU WIN!")
            exit()

    def run(self):
        enemy = self.spawn_enemy()
        while self.running:
            Game.clear()

            hero.attack(enemy)
            enemy.attack(hero)

            hero.health_bar.draw()
            enemy.health_bar.draw()

            input()

            self.running = hero.alive

            if not enemy.alive:
                enemies.pop(0)
                enemy = self.spawn_enemy()

        input("GAME OVER")
        exit()


# ------------ game loop ------------
if __name__ == "__main__":
    game = Game()
    game.run()
