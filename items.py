class Item():
    def __init__(self, name, category, description, value):
        self.name = name
        self.category = category
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
    def __init__(self, name, category, description, value, damage):
        self.damage = damage
        super().__init__(name, category, description, value)

class Armor(Item):
    def __init__(self, name, category, description, value, defense):
        self.defense = defense
        super().__init__(name, category, description, value)

bronze_sword = Weapon("Bronze Sword", "Weapon", "A sword made of bronze.", 2, 3)
bronze_shield = Armor("Bronze Shield", "Shield", "A shield made of bronze.", 2, 2)
bronze_armor = Armor("Bronze Armor", "Armor", "An armor made of bronze.", 2, 3)

dict_item_stats = {  #always [NAME, CATEGORY, DESCRIPTION, DAMAGE/DEFENSE, VALUE]
    "Bronze Sword": [
        bronze_sword.name,
        bronze_sword.category,
        bronze_sword.description,
        bronze_sword.damage,
        bronze_sword.value
    ],
    "Bronze Shield": [
        bronze_shield.name,
        bronze_shield.category,
        bronze_shield.description,
        bronze_shield.defense,
        bronze_shield.value
    ],
    "Bronze Armor": [
        bronze_armor.name,
        bronze_armor.category,
        bronze_armor.description,
        bronze_armor.defense,
        bronze_armor.value
    ]
}