# ------------ imports ------------
from abc import ABC
from random import randint

from weapon import fists, jaws, claws, short_bow, iron_sword
from health_bar import HealthBar


# ------------ parent class setup ------------
class Character(ABC):
    health_bar: HealthBar
    counter_chance: int = 20

    def __init__(self,
                 name: str,
                 health: int,
                 eva_ch: int,
                 crit_ch: int,
                 armor: int
                 ) -> None:
        self.name = name
        self.health = health
        self.health_max = health

        self.evade_chance = eva_ch
        self.crit_chance = crit_ch
        self.armor = armor

        self.weapon = fists

    @property
    def alive(self) -> bool:
        return self.health > 0

    def attack(self, target, is_counter: bool = False) -> None:
        # skip the attack if own health reached zero
        if not self.alive:
            print(f"{self.name} has fallen in battle...")
            return

        # calculate if enemy evades attack - return if so
        if target.roll_event(target.evade_chance):
            print(f"{self.name} missed the attack!")
            return

        # calculate base damage
        dmg = self.weapon.damage

        # calculate damage based on critical hit
        crit_dmg = self.deal_crit(dmg)

        # calculate damage based on armor
        final_dmg = max(crit_dmg - target.armor, 0)

        # withdraw damage from enemy health
        target.get_damaged(final_dmg, self)

        # roll for counter
        if not is_counter and target.alive and target.roll_event(target.counter_chance):
            print(f"{target.name} initiated counter-attack!")
            target.attack(self, is_counter=True)

    def evade(self) -> bool:
        rolled_evade = randint(1, 100)
        return rolled_evade <= self.evade_chance

    def crit(self) -> bool:
        rolled_crit = randint(1, 100)
        return rolled_crit <= self.crit_chance

    def counter(self) -> bool:
        rolled_counter = randint(1, 100)
        return rolled_counter <= self.counter_chance

    @staticmethod
    def roll_event(stat_chance: int) -> bool:
        rolled_event = randint(1, 100)
        return rolled_event <= stat_chance

    def deal_crit(self, base_dmg: int) -> int:
        if self.roll_event(self.crit_chance):
            print("CRITICAL HIT!")
            return base_dmg * 2
        return base_dmg

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
        super().__init__(
            name=name,
            health=health,
            eva_ch=10,
            crit_ch=10,
            armor=2
        )

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
                 eva_ch: int,
                 crit_ch: int,
                 armor: int,
                 weapon,
                 ) -> None:
        super().__init__(
            name=name,
            health=health,
            eva_ch=eva_ch,
            crit_ch=crit_ch,
            armor=armor
        )
        self.weapon = weapon

        self.health_bar = HealthBar(self, color="red")

        enemies.append(self)


enemies = []
rat = Enemy(
    "Rat",
    health=12,
    eva_ch=10,
    crit_ch=5,
    armor=0,
    weapon=claws
)
slime = Enemy(
    "Slime",
    health=20,
    eva_ch=0,
    crit_ch=0,
    armor=0,
    weapon=jaws
)
wolf = Enemy(
    "Wolf",
    health=30,
    eva_ch=20,
    crit_ch=10,
    armor=0,
    weapon=jaws
)
goblin = Enemy(
    "Goblin",
    health=40,
    eva_ch=5,
    crit_ch=5,
    armor=2,
    weapon=short_bow
)
ork = Enemy(
    "Ork",
    health=60,
    eva_ch=0,
    crit_ch=10,
    armor=4,
    weapon=iron_sword
)

