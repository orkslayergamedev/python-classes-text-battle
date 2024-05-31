from random import randint


# ------------ class setup ------------
class Weapon:
    def __init__(self,
                 name: str,
                 weapon_type: str,
                 damage: int,
                 value: int = 0
                 ) -> None:
        self.name = name
        self.weapon_type = weapon_type
        self.value = value
        self.dmg_min = max(damage - 2, 1)
        self.dmg_max = damage + 2

    @property
    def damage(self) -> int:
        return randint(self.dmg_min, self.dmg_max)


# ------------ object creation ------------
iron_sword = Weapon(name="Iron Sword",
                    weapon_type="sharp",
                    damage=5,
                    value=10)

short_bow = Weapon(name="Short Bow",
                   weapon_type="ranged",
                   damage=4,
                   value=8)

fists = Weapon(name="Fists",
               weapon_type="blunt",
               damage=2)

claws = Weapon(name="Claws",
               weapon_type="sharp",
               damage=3)

jaws = Weapon(name="Jaws",
              weapon_type="sharp",
              damage=4)
