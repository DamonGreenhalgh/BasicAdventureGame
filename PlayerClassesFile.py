""" PlayerClasses File
This file contains multiple player classes, each class behaves
differently in the game. These classes have custom skills and resources.

Classes: (DEV)
 - Barbarian
   The Barbarian class is the fighter class with melee focused abilities.
   Methods:
    - skill_rage()
    - skill_brutal_critical()
    - skill_primal_champion()

- Ranger
  The Ranger class focuses on ranged combat and companions.

- Wizard
  The Wizard class focuses on fire - based spells.
    

Author: Damon Greenhalgh
"""

# Import/s
import random
from PlayerClass import Player
from DieClass import Die

# List of player classes.
# Barbarian, Ranger, Wizard
class Barbarian(Player):

    def __init__(self, name = "Barbarian"):
        stats = [name, 15, 10, 5, 6, 3, 1]
        Player.__init__(self, stats)
        self.player_class = "Barbarian"
        self.skills = [("Rage", self.skill_rage), ("Brutal Critical", self.skill_brutal_critical), ("Primal Champion", self.skill_primal_champion)]

        # Class Specific Stat
        # Rage Builds up when the player takes damage, or after a turn.
        # Rage is the resource cost for the Barbarian's abilities.
        self.class_stat_name = "Rage"
        self.mp = 0     # Start at 0 rage.

    def skill_rage(self):    # Halves incoming damage.
        if self.buff == []:
            self.buff += [["*", 1/2, f"{self.name} takes half damage.(Rage)"] for i in range(5)]     # Reduces damage
        else:
            print("Cannot cast 'Rage' while under another buff effect.")
        
    def skill_brutal_critical(self):    # When the player critically strikes, deal bonus damage.
        pass

    def skill_primal_champion(self):
        # Double Strength, roll advantage.
        print("primal champion")


class Ranger(Player):

    def __init__(self, name = "Ranger"):
        stats = [name, 6, 15, 9, 2, 5, 3]
        Player.__init__(self, stats)
        self.player_class = "Ranger"
    
        # Class Specific Stat
        # The ranger uses ARROWS as a resource.
        self.class_stat_name = "Arrows"

class Wizard(Player):
    
    def __init__(self, name = "Wizard"):
        stats = [name, 4, 8, 18, 1, 3, 6]
        Player.__init__(self, stats)
        self.player_class = "Wizard"
        
        # Class Specific Stat
        # The wizard uses MANA as a resource.
        self.class_stat_name = "Mana"

