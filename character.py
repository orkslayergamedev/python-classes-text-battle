# ------------ imports ------------
from abc import ABC

from weapon import fists, jaws, claws, short_bow, iron_sword
from health_bar import HealthBar


# ------------ parent class setup ------------
class Character(ABC):
    health_bar: HealthBar

    def __init__(self,
                 name: str,
                 health: int,
                 ) -> None:
        self.name = name
        self.health = health
        self.health_max = health

        self.weapon = fists

    @property
    def alive(self) -> bool:
        return self.health > 0

    def attack(self, target) -> None:
        # skip the attack if own health reached zero
        if not self.alive:
            print(f"{self.name} has fallen in battle...")
            return

        # calculate base damage
        dmg = self.weapon.damage

        # withdraw damage from enemy health
        target.get_damaged(dmg, self)

    def get_damaged(self, dmg: int, attacker) -> None:
        self.health -= dmg
        self.health = max(self.health, 0)
        self.health_bar.update()
        print(f"{attacker.name} dealt {dmg} damage to "
              f"{self.name} with {attacker.weapon.name}")


# ------------ subclass setup ------------
class Hero(Character):
    def __init__(self,
                 name: str,
                 health: int
                 ) -> None:
        super().__init__(name=name, health=health)

        self.default_weapon = self.weapon
        self.health_bar = HealthBar(self, color="green")

    def equip(self, weapon) -> None:
        self.weapon = weapon
        print(f"{self.name} equipped a(n) {self.weapon.name}!")

    def drop(self) -> None:
        print(f"{self.name} dropped the {self.weapon.name}!")
        self.weapon = self.default_weapon


# ------------ subclass setup ------------
class Enemy(Character):
    def __init__(self,
                 name: str,
                 health: int,
                 weapon,
                 ) -> None:
        super().__init__(name=name, health=health)
        self.weapon = weapon

        self.health_bar = HealthBar(self, color="red")

        enemies.append(self)


enemies = []
rat = Enemy("Rat", 12, claws)
slime = Enemy("Slime", 20, jaws)
wolf = Enemy("Wolf", 30, jaws)
goblin = Enemy("Goblin", 40, short_bow)
ork = Enemy("Ork", 60, iron_sword)
