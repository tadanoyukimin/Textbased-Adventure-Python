class Item():
    def __init__(self, name, description, value):
        self.name = name
        self.description = description
        self.value = value
    
    def check_value(self):
        return f"This is worth {self.value} gold pieces."

    def __str__(self):
        return f"{self.name}: {self.description}."

class Gold(Item):
    def __init__(self, amount):
        self.amount = amount
        super().__init__(
            name = "Gold",
            description = f"{self.amount} gold pieces",
            value = self.amount
            )

class Weapon(Item):
    def __init__(self, name, description, value, damage):
        self.damage = damage
        super().__init__(name, description, value)

class Armor(Item):
    def __init__(self, name, description, value, defense):
        self.defense = defense
        super().__init__(name, description, value)

bronze_sword = Weapon("Bronze Sword", "A sword made of bronze.", 2, 3)
bronze_shield = Armor("Bronze Shield", "A shield made of bronze.", 2, 2)
bronze_armor = Armor("Bronze Armor", "An armor made of bronze.", 2, 3)

dict_item_stats = {  #always [NAME, DAMAGE/DEFENSE, VALUE]
    "Bronze Sword": [
        bronze_sword.name,
        bronze_sword.damage,
        bronze_sword.value
    ],
    "Bronze Shield": [
        bronze_shield.name,
        bronze_shield.defense,
        bronze_shield.value
    ],
    "Bronze Armor": [
        bronze_armor.name,
        bronze_armor.defense,
        bronze_armor.value
    ]
}
print(dict_item_stats)