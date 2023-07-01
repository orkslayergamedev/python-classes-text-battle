# ------------ class setup ------------
class Weapon:
    def __init__(self,
                 name: str,
                 weapon_type: str,
                 damage: int,
                 value: int
                 ) -> None:
        self.name = name
        self.weapon_type = weapon_type
        self.damage = damage
        self.value = value


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
               damage=2,
               value=0)
