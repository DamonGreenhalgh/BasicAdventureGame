""" Entity Class
This file contains the entity class, and is a basis for all
objects within the project.

Methods:
 - attack()
   Handles the attack action of an entity.
 - edit_hp()
   Edits the hp of the entity.

Author: Damon Greenhalgh
"""

# Import/s
import math
from DieClass import Die

class Entity:

    def __init__(self, stats = ["Entity", 10, 10, 10]):
        self.name = stats[0]    # Name

        # Stats
        self.str = stats[1]
        self.dex = stats[2]
        self.int = stats[3]
     
        # Status Array
        self.buff = []    
        self.debuff = []

        # Determine the entity's highest statistic.
        stats = stats[1 : ]
        highest_stat = max(stats)
        self.prof = [stats[i] for i in range(len(stats)) if stats[i] == highest_stat][0]
        
        # Calculate Health
        self.hp = (self.str * 10)     
        self.max_hp = self.hp

        # Calculate Armor
        self.armor = min((self.dex // 2), 15)

    def attack(self):    # Basic attack.
        """
        This function handles the attack action of an entity.
         - param: None
         - return: int damage
        """
        die = Die()    # Create Die
        idx = 2
        
        # Roll to hit.
        roll = die.roll()

        # Roll for damage.
        type = min(self.prof // 6, 5)    # Determine the type of die, based on the main stat of the entity.
        rolls = max(self.prof // 6, 1)    # Determine the number of rolls for the type of die.
        damage = die.roll(rolls, type)

        if roll == 1:    # Fumble
            damage = 0 
            idx = 0

        elif roll == 20:    # Critical hit
            damage = damage * 2
            idx = 1

        # Display
        disp_str = ["Fumble! ", "Critical Hit! ", ""]
        print(f"{disp_str[idx]}{self.name} deals {damage} damage!(rolled a {roll})")
        return damage

    def edit_hp(self, value):
        """
        This function changes the hp value of the entity.
         - param: int value
         - return: None
        """
        new_hp = self.hp + value
        if new_hp <= 0:
            self.hp = 0
        elif new_hp >= self.max_hp:
            self.hp = self.max_hp
        else:
            self.hp = new_hp
        
    def edit_status(self, damage):
        """
        This function handles statuses the entity has.
         - param: str type
         - param: int damage
         - return: int damage
        """

        if not self.buff == []:    # Check there exist buff
            operator = self.buff[0][0]    # Determine the operation
            if operator == "*":
                damage = damage * self.buff[0][1]    # Edit damage value
            elif operator == "+":
                damage = damage + self.buff[0][1] 

            # Display
            print(self.buff[0][2])
            
            damage = math.ceil(damage)
            self.buff.pop(0)    # Remove buff


        return damage