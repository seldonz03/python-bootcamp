from xml.dom.pulldom import CHARACTERS
class Character:
    def __init__(self, health=10, strength=10, defence=10):
        self.h=health
        self.s=strength
        self.d=defence

    def attack(self, other):
        damage= self.s - other.d
        other.h -= damage

class Knight:
    def __init__(self, health=10, defense=10):
        self.health = health
        self.defense = defense
def attack(self, other):
        damage = self.defense - other.defense
        other.health -= damage

player = Knight(defense=20)
enemy = Character()
if hasattr(player,"attack"):
    player.attack(enemy)
    print(enemy.health)

