class Character:
    def __init__(self, health=10, strength=10, defence=10):
        self.h=health
        self.s=strength
        self.d=defence

    def attack(self, other):
        damage= self.s - other.d
        other.h -= damage



player=Character(strength=50)
enemy=Character()

player.attack(enemy)
print(enemy.h)