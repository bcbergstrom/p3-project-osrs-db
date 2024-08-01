import sqlite3

class SkillRequirements:
    """
    Class representing skill requirements for a given activity.

    Attributes:
        Attack (int): Required attack level.
        Strength (int): Required strength level.
        Defense (int): Required defense level.
        Ranged (int): Required ranged level.
        Prayer (int): Required prayer level.
        Magic (int): Required magic level.
        Runecraft (int): Required runecraft level.
        Hitpoints (int): Required hitpoints level.
        Mining (int): Required mining level.
        Smithing (int): Required smithing level.
        Fishing (int): Required fishing level.
        Cooking (int): Required cooking level.
        Firemaking (int): Required firemaking level.
        Woodcutting (int): Required woodcutting level.
        Agility (int): Required agility level.
        Herblore (int): Required herblore level.
        Thieving (int): Required thieving level.
        Fletching (int): Required fletching level.
        Slayer (int): Required slayer level.
        Farming (int): Required farming level.
        Construction (int): Required construction level.
        Hunter (int): Required hunting level.
    """
    def __init__(self, Attack=0, Strength=0, Defense=0, Ranged=0, Prayer=0, Magic=0,Runecraft=0,Hitpoints=0,Crafting=0, Mining=0,
                 Smithing=0, Fishing=0, Cooking=0, Firemaking=0, Woodcutting=0,
                 Agility=0, Herblore=0, Thieving=0, Fletching=0, Slayer=0, Farming=0, 
                 Construction=0, Hunter=0):
        """
        Initializes a new instance of SkillRequirements.

        Args:
            Attack (int): Required attack level.
            Strength (int): Required strength level.
            Defense (int): Required defense level.
            Ranged (int): Required ranged level.
            Prayer (int): Required prayer level.
            Magic (int): Required magic level.
            Runecraft (int): Required runecraft level.
            Hitpoints (int): Required hitpoints level.
            Mining (int): Required mining level.
            Smithing (int): Required smithing level.
            Fishing (int): Required fishing level.
            Cooking (int): Required cooking level.
            Firemaking (int): Required firemaking level.
            Woodcutting (int): Required woodcutting level.
            Agility (int): Required agility level.
            Herblore (int): Required herblore level.
            Thieving (int): Required thieving level.
            Fletching (int): Required fletching level.
            Slayer (int): Required slayer level.
            Farming (int): Required farming level.
            Construction (int): Required construction level.
            Hunter (int): Required hunting level.
        """
        self.Attack = Attack
        """Required attack level."""
        
        self.Strength = Strength
        """Required strength level."""
        
        self.Defense = Defense
        """Required defense level."""
        
        self.Ranged = Ranged
        """Required ranged level."""
        
        self.Prayer = Prayer
        """Required prayer level."""
        
        self.Magic = Magic
        """Required magic level."""
        
        self.Runecraft = Runecraft
        """Required runecraft level."""
        
        self.Hitpoints = Hitpoints
        """Required hitpoints level."""
        
        self.Crafting = Crafting
        """Required crafting level."""
        
        self.Mining = Mining
        """Required mining level."""
        
        self.Smithing = Smithing
        """Required smithing level."""
        
        self.Fishing = Fishing
        """Required fishing level."""
        
        self.Cooking = Cooking
        """Required cooking level."""
        
        self.Firemaking = Firemaking
        """Required firemaking level."""
        
        self.Woodcutting = Woodcutting
        """Required woodcutting level."""
        
        self.Agility = Agility
        """Required agility level."""
        
        self.Herblore = Herblore
        """Required herblore level."""
        
        self.Thieving = Thieving
        """Required thieving level."""
        
        self.Fletching = Fletching
        """Required fletching level."""
        
        self.Slayer = Slayer
        """Required slayer level."""
        
        self.Farming = Farming
        """Required farming level."""
        
        self.Construction = Construction
        """Required construction level."""
        
        self.Hunter = Hunter
        """Required hunting level."""

