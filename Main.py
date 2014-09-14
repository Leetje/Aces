__author__ = 'leethomas'

'''
Created on Jan 10, 2013

'''

if __name__ == '__main__':
    pass
import random


# Contains stats derived from str and str_pct { str: { str_pct { damage_modifier : value, Lift : value , carry: value, drag : value } } }
# to get entry table name[15][1]["keyname"]

stre_table = {
    1: {1: {'damage_modifier': -7, 'Lift': 11, 'Carry': 9, 'Drag': 28},
        51: {'damage_modifier': -6, 'Lift': 25, 'Carry': 12, 'Drag': 63}},
    2: {1: {'damage_modifier': -6, 'Lift': 38, 'Carry': 14, 'Drag': 95, },
        51: {'damage_modifier': -5, 'Lift': 51, 'Carry': 17, 'Drag': 128, }},
    3: {1: {'damage_modifier': -5, 'Lift': 64, 'Carry': 20, 'Drag': 160, },
        51: {'damage_modifier': -4, 'Lift': 76, 'Carry': 22, 'Drag': 190, }},
    4: {1: {'damage_modifier': -4, 'Lift': 88, 'Carry': 24, 'Drag': 220, },
        51: {'damage_modifier': -4, 'Lift': 99, 'Carry': 26, 'Drag': 248, }},
    5: {1: {'damage_modifier': -3, 'Lift': 110, 'Carry': 29, 'Drag': 275, },
        51: {'damage_modifier': -3, 'Lift': 120, 'Carry': 31, 'Drag': 300, }},
    6: {1: {'damage_modifier': -3, 'Lift': 130, 'Carry': 32, 'Drag': 325, },
        51: {'damage_modifier': -2, 'Lift': 140, 'Carry': 34, 'Drag': 350, }},
    7: {1: {'damage_modifier': -2, 'Lift': 149, 'Carry': 36, 'Drag': 373, },
        51: {'damage_modifier': -2, 'Lift': 157, 'Carry': 38, 'Drag': 393, }},
    8: {1: {'damage_modifier': -1, 'Lift': 166, 'Carry': 39, 'Drag': 415, },
        51: {'damage_modifier': -1, 'Lift': 173, 'Carry': 40, 'Drag': 433, }},
    9: {1: {'damage_modifier': -1, 'Lift': 181, 'Carry': 42, 'Drag': 453, },
        51: {'damage_modifier': -1, 'Lift': 187, 'Carry': 43, 'Drag': 468, }},
    10: {1: {'damage_modifier': 0, 'Lift': 194, 'Carry': 44, 'Drag': 485, },
         51: {'damage_modifier': 0, 'Lift': 200, 'Carry': 45, 'Drag': 500, }},
    11: {1: {'damage_modifier': 0, 'Lift': 205, 'Carry': 48, 'Drag': 513, },
         51: {'damage_modifier': 0, 'Lift': 210, 'Carry': 52, 'Drag': 525, }},
    12: {1: {'damage_modifier': 1, 'Lift': 215, 'Carry': 56, 'Drag': 538, },
         51: {'damage_modifier': 1, 'Lift': 220, 'Carry': 61, 'Drag': 550, }},
    13: {1: {'damage_modifier': 1, 'Lift': 225, 'Carry': 66, 'Drag': 563, },
         51: {'damage_modifier': 1, 'Lift': 230, 'Carry': 71, 'Drag': 575, }},
    14: {1: {'damage_modifier': 2, 'Lift': 235, 'Carry': 77, 'Drag': 588, },
         51: {'damage_modifier': 2, 'Lift': 240, 'Carry': 84, 'Drag': 600, }},
    15: {1: {'damage_modifier': 2, 'Lift': 245, 'Carry': 91, 'Drag': 613, },
         51: {'damage_modifier': 3, 'Lift': 267, 'Carry': 99, 'Drag': 668, }},
    16: {1: {'damage_modifier': 3, 'Lift': 291, 'Carry': 108, 'Drag': 728, },
         51: {'damage_modifier': 3, 'Lift': 318, 'Carry': 118, 'Drag': 795, }},
    17: {1: {'damage_modifier': 4, 'Lift': 347, 'Carry': 129, 'Drag': 868, },
         51: {'damage_modifier': 4, 'Lift': 380, 'Carry': 142, 'Drag': 950, }},
    18: {1: {'damage_modifier': 4, 'Lift': 417, 'Carry': 156, 'Drag': 1043, },
         51: {'damage_modifier': 5, 'Lift': 458, 'Carry': 171, 'Drag': 1145, }},
    19: {1: {'damage_modifier': 5, 'Lift': 504, 'Carry': 189, 'Drag': 1260, },
         51: {'damage_modifier': 6, 'Lift': 554, 'Carry': 209, 'Drag': 1385, }},
    20: {1: {'damage_modifier': 6, 'Lift': 612, 'Carry': 231, 'Drag': 1530, },
         51: {'damage_modifier': 7, 'Lift': 675, 'Carry': 256, 'Drag': 1688, }},
    21: {1: {'damage_modifier': 7, 'Lift': 747, 'Carry': 285, 'Drag': 1868, },
         51: {'damage_modifier': 8, 'Lift': 828, 'Carry': 317, 'Drag': 2070, }},
    22: {1: {'damage_modifier': 8, 'Lift': 919, 'Carry': 354, 'Drag': 2298, },
         51: {'damage_modifier': 9, 'Lift': 1021, 'Carry': 396, 'Drag': 2553, }},
    23: {1: {'damage_modifier': 10, 'Lift': 1137, 'Carry': 443, 'Drag': 2843, },
         51: {'damage_modifier': 11, 'Lift': 1268, 'Carry': 498, 'Drag': 3170, }},
    24: {1: {'damage_modifier': 12, 'Lift': 1417, 'Carry': 560, 'Drag': 3543, },
         51: {'damage_modifier': 13, 'Lift': 1585, 'Carry': 631, 'Drag': 3963, }},
    25: {1: {'damage_modifier': 14, 'Lift': 1777, 'Carry': 714, 'Drag': 4443, }
    }}

inte_table = {
    1: {"accuracy_modifier": -3, "bp_bonus": 0, "skill_learning_mod": -9},
    2: {"accuracy_modifier": -3, "bp_bonus": 0, "skill_learning_mod": -8},
    3: {"accuracy_modifier": -3, "bp_bonus": 0, "skill_learning_mod": -7},
    4: {"accuracy_modifier": -2, "bp_bonus": 0, "skill_learning_mod": -6},
    5: {"accuracy_modifier": -2, "bp_bonus": 0, "skill_learning_mod": -5},
    6: {"accuracy_modifier": -2, "bp_bonus": 0, "skill_learning_mod": -4},
    7: {"accuracy_modifier": -1, "bp_bonus": 0, "skill_learning_mod": -3},
    8: {"accuracy_modifier": -1, "bp_bonus": 0, "skill_learning_mod": -2},
    9: {"accuracy_modifier": -1, "bp_bonus": 0, "skill_learning_mod": -1},
    10: {"accuracy_modifier": 0, "bp_bonus": 0, "skill_learning_mod": 0},
    11: {"accuracy_modifier": 0, "bp_bonus": 0, "skill_learning_mod": 0},
    12: {"accuracy_modifier": 1, "bp_bonus": 1, "skill_learning_mod": 1},
    13: {"accuracy_modifier": 1, "bp_bonus": 3, "skill_learning_mod": 2},
    14: {"accuracy_modifier": 1, "bp_bonus": 6, "skill_learning_mod": 3},
    15: {"accuracy_modifier": 2, "bp_bonus": 10, "skill_learning_mod": 4},
    16: {"accuracy_modifier": 2, "bp_bonus": 15, "skill_learning_mod": 5},
    17: {"accuracy_modifier": 2, "bp_bonus": 21, "skill_learning_mod": 6},
    18: {"accuracy_modifier": 3, "bp_bonus": 28, "skill_learning_mod": 7},
    19: {"accuracy_modifier": 3, "bp_bonus": 36, "skill_learning_mod": 8},
    20: {"accuracy_modifier": 3, "bp_bonus": 45, "skill_learning_mod": 9},
    21: {"accuracy_modifier": 4, "bp_bonus": 55, "skill_learning_mod": 10},
    22: {"accuracy_modifier": 4, "bp_bonus": 66, "skill_learning_mod": 11},
    23: {"accuracy_modifier": 4, "bp_bonus": 78, "skill_learning_mod": 12},
    24: {"accuracy_modifier": 5, "bp_bonus": 91, "skill_learning_mod": 13},
    25: {"accuracy_modifier": 5, "bp_bonus": 105, "skill_learning_mod": 14},
}

wis_table = {
    1: {'speed_mod': 5, 'bp_bonus': 0, 'skill_learning_mod': -9},
    2: {'speed_mod': 5, 'bp_bonus': 0, 'skill_learning_mod': -8},
    3: {'speed_mod': 5, 'bp_bonus': 0, 'skill_learning_mod': -7},
    4: {'speed_mod': 4, 'bp_bonus': 0, 'skill_learning_mod': -6},
    5: {'speed_mod': 4, 'bp_bonus': 0, 'skill_learning_mod': -5},
    6: {'speed_mod': 4, 'bp_bonus': 0, 'skill_learning_mod': -4},
    7: {'speed_mod': 3, 'bp_bonus': 0, 'skill_learning_mod': -3},
    8: {'speed_mod': 3, 'bp_bonus': 0, 'skill_learning_mod': -2},
    9: {'speed_mod': 3, 'bp_bonus': 0, 'skill_learning_mod': -1},
    10: {'speed_mod': 2, 'bp_bonus': 0, 'skill_learning_mod': 0},
    11: {'speed_mod': 2, 'bp_bonus': 0, 'skill_learning_mod': 0},
    12: {'speed_mod': 1, 'bp_bonus': 1, 'skill_learning_mod': 1},
    13: {'speed_mod': 1, 'bp_bonus': 3, 'skill_learning_mod': 2},
    14: {'speed_mod': 1, 'bp_bonus': 6, 'skill_learning_mod': 3},
    15: {'speed_mod': 0, 'bp_bonus': 10, 'skill_learning_mod': 4},
    16: {'speed_mod': 0, 'bp_bonus': 15, 'skill_learning_mod': 5},
    17: {'speed_mod': 0, 'bp_bonus': 21, 'skill_learning_mod': 6},
    18: {'speed_mod': -1, 'bp_bonus': 28, 'skill_learning_mod': 7},
    19: {'speed_mod': -1, 'bp_bonus': 36, 'skill_learning_mod': 8},
    20: {'speed_mod': -1, 'bp_bonus': 45, 'skill_learning_mod': 9},
    21: {'speed_mod': -2, 'bp_bonus': 55, 'skill_learning_mod': 10},
    22: {'speed_mod': -2, 'bp_bonus': 66, 'skill_learning_mod': 11},
    23: {'speed_mod': -2, 'bp_bonus': 78, 'skill_learning_mod': 12},
    24: {'speed_mod': -3, 'bp_bonus': 91, 'skill_learning_mod': 13},
    25: {'speed_mod': -3, 'bp_bonus': 105, 'skill_learning_mod': 14},
}

dex_table = {
    1: {1: {"speed_mod": 8, "accuracy_mod": -5},
        51: {"speed_mod": 8, "accuracy_mod": -4}},
    2: {1: {"speed_mod": 8, "accuracy_mod": -4},
        51: {"speed_mod": 7, "accuracy_mod": -4}},
    3: {1: {"speed_mod": 7, "accuracy_mod": -4},
        51: {"speed_mod": 7, "accuracy_mod": -3}},
    4: {1: {"speed_mod": 6, "accuracy_mod": -3},
        51: {"speed_mod": 6, "accuracy_mod": -3}},
    5: {1: {"speed_mod": 6, "accuracy_mod": -3},
        51: {"speed_mod": 5, "accuracy_mod": -2}},
    6: {1: {"speed_mod": 5, "accuracy_mod": -2},
        51: {"speed_mod": 5, "accuracy_mod": -2}},
    7: {1: {"speed_mod": 4, "accuracy_mod": -2},
        51: {"speed_mod": 4, "accuracy_mod": -1}},
    8: {1: {"speed_mod": 4, "accuracy_mod": -1},
        51: {"speed_mod": 3, "accuracy_mod": -1}},
    9: {1: {"speed_mod": 3, "accuracy_mod": -1},
        51: {"speed_mod": 3, "accuracy_mod": 0}},
    10: {1: {"speed_mod": 2, "accuracy_mod": 0},
         51: {"speed_mod": 2, "accuracy_mod": 0}},
    11: {1: {"speed_mod": 2, "accuracy_mod": 0},
         51: {"speed_mod": 1, "accuracy_mod": 0}},
    12: {1: {"speed_mod": 1, "accuracy_mod": 1},
         51: {"speed_mod": 1, "accuracy_mod": 1}},
    13: {1: {"speed_mod": 0, "accuracy_mod": 1},
         51: {"speed_mod": 0, "accuracy_mod": 1}},
    14: {1: {"speed_mod": 0, "accuracy_mod": 2},
         51: {"speed_mod": -1, "accuracy_mod": 2}},
    15: {1: {"speed_mod": -1, "accuracy_mod": 2},
         51: {"speed_mod": -1, "accuracy_mod": 2}},
    16: {1: {"speed_mod": -2, "accuracy_mod": 3},
         51: {"speed_mod": -2, "accuracy_mod": 3}},
    17: {1: {"speed_mod": -2, "accuracy_mod": 3},
         51: {"speed_mod": -3, "accuracy_mod": 3}},
    18: {1: {"speed_mod": -3, "accuracy_mod": 4},
         51: {"speed_mod": -3, "accuracy_mod": 4}},
    19: {1: {"speed_mod": -4, "accuracy_mod": 4},
         51: {"speed_mod": -4, "accuracy_mod": 4}},
    20: {1: {"speed_mod": -4, "accuracy_mod": 5},
         51: {"speed_mod": -5, "accuracy_mod": 5}},
    21: {1: {"speed_mod": -5, "accuracy_mod": 5},
         51: {"speed_mod": -5, "accuracy_mod": 5}},
    22: {1: {"speed_mod": -6, "accuracy_mod": 6},
         51: {"speed_mod": -6, "accuracy_mod": 6}},
    23: {1: {"speed_mod": -6, "accuracy_mod": 6},
         51: {"speed_mod": -7, "accuracy_mod": 6}},
    24: {1: {"speed_mod": -7, "accuracy_mod": 7},
         51: {"speed_mod": -7, "accuracy_mod": 7}},
    25: {1: {"speed_mod": -8, "accuracy_mod": 7},
    }}

con_table = {
    1: {"hp_mod": -9},
    2: {"hp_mod": -8},
    3: {"hp_mod": -7},
    4: {"hp_mod": -6},
    5: {"hp_mod": -5},
    6: {"hp_mod": -4},
    7: {"hp_mod": -3},
    8: {"hp_mod": -2},
    9: {"hp_mod": -1},
    10: {"hp_mod": 0},
    11: {"hp_mod": 0},
    12: {"hp_mod": 1},
    13: {"hp_mod": 2},
    14: {"hp_mod": 3},
    15: {"hp_mod": 4},
    16: {"hp_mod": 5},
    17: {"hp_mod": 6},
    18: {"hp_mod": 7},
    19: {"hp_mod": 8},
    20: {"hp_mod": 9},
    21: {"hp_mod": 10},
    22: {"hp_mod": 11},
    23: {"hp_mod": 12},
    24: {"hp_mod": 13},
    25: {"hp_mod": 14},
}

looks_table = {
    1: {"charisma_mod": -7, "rep_mod": -9, "fame_mod": -9},
    2: {"charisma_mod": -6, "rep_mod": -8, "fame_mod": -8},
    3: {"charisma_mod": -5, "rep_mod": -7, "fame_mod": -7},
    4: {"charisma_mod": -4, "rep_mod": -6, "fame_mod": -6},
    5: {"charisma_mod": -3, "rep_mod": -5, "fame_mod": -5},
    6: {"charisma_mod": -2, "rep_mod": -4, "fame_mod": -4},
    7: {"charisma_mod": -2, "rep_mod": -3, "fame_mod": -3},
    8: {"charisma_mod": -1, "rep_mod": -2, "fame_mod": -2},
    9: {"charisma_mod": -1, "rep_mod": -1, "fame_mod": -1},
    10: {"charisma_mod": 0, "rep_mod": 0, "fame_mod": 0},
    11: {"charisma_mod": 0, "rep_mod": 0, "fame_mod": 0},
    12: {"charisma_mod": 0, "rep_mod": 1, "fame_mod": 1},
    13: {"charisma_mod": 1, "rep_mod": 1, "fame_mod": 2},
    14: {"charisma_mod": 1, "rep_mod": 2, "fame_mod": 3},
    15: {"charisma_mod": 2, "rep_mod": 2, "fame_mod": 4},
    16: {"charisma_mod": 2, "rep_mod": 3, "fame_mod": 5},
    17: {"charisma_mod": 3, "rep_mod": 4, "fame_mod": 6},
    18: {"charisma_mod": 4, "rep_mod": 5, "fame_mod": 7},
    19: {"charisma_mod": 5, "rep_mod": 6, "fame_mod": 8},
    20: {"charisma_mod": 6, "rep_mod": 7, "fame_mod": 9},
    21: {"charisma_mod": 7, "rep_mod": 8, "fame_mod": 10},
    22: {"charisma_mod": 8, "rep_mod": 9, "fame_mod": 11},
    23: {"charisma_mod": 9, "rep_mod": 10, "fame_mod": 12},
    24: {"charisma_mod": 10, "rep_mod": 11, "fame_mod": 13},
    25: {"charisma_mod": 11, "rep_mod": 12, "fame_mod": 14},
}
cha_table = {
    1: {"bp_bonus": 0, "skill_learning_mod": -9, "max_comp": 0, "rep_mod": -9},
    2: {"bp_bonus": 0, "skill_learning_mod": -8, "max_comp": 0, "rep_mod": -8},
    3: {"bp_bonus": 0, "skill_learning_mod": -7, "max_comp": 0, "rep_mod": -7},
    4: {"bp_bonus": 0, "skill_learning_mod": -6, "max_comp": 1, "rep_mod": -6},
    5: {"bp_bonus": 0, "skill_learning_mod": -5, "max_comp": 1, "rep_mod": -5},
    6: {"bp_bonus": 0, "skill_learning_mod": -4, "max_comp": 1, "rep_mod": -4},
    7: {"bp_bonus": 0, "skill_learning_mod": -3, "max_comp": 2, "rep_mod": -3},
    8: {"bp_bonus": 0, "skill_learning_mod": -2, "max_comp": 2, "rep_mod": -2},
    9: {"bp_bonus": 0, "skill_learning_mod": -1, "max_comp": 3, "rep_mod": -1},
    10: {"bp_bonus": 0, "skill_learning_mod": 0, "max_comp": 3, "rep_mod": 0},
    11: {"bp_bonus": 0, "skill_learning_mod": 0, "max_comp": 4, "rep_mod": 0},
    12: {"bp_bonus": 1, "skill_learning_mod": 1, "max_comp": 5, "rep_mod": 1},
    13: {"bp_bonus": 3, "skill_learning_mod": 2, "max_comp": 6, "rep_mod": 2},
    14: {"bp_bonus": 6, "skill_learning_mod": 3, "max_comp": 8, "rep_mod": 3},
    15: {"bp_bonus": 10, "skill_learning_mod": 4, "max_comp": 10, "rep_mod": 4},
    16: {"bp_bonus": 15, "skill_learning_mod": 5, "max_comp": 12, "rep_mod": 5},
    17: {"bp_bonus": 21, "skill_learning_mod": 6, "max_comp": 15, "rep_mod": 6},
    18: {"bp_bonus": 28, "skill_learning_mod": 7, "max_comp": 20, "rep_mod": 7},
    19: {"bp_bonus": 36, "skill_learning_mod": 8, "max_comp": 25, "rep_mod": 8},
    20: {"bp_bonus": 45, "skill_learning_mod": 9, "max_comp": 30, "rep_mod": 9},
    21: {"bp_bonus": 55, "skill_learning_mod": 10, "max_comp": 40, "rep_mod": 10},
    22: {"bp_bonus": 66, "skill_learning_mod": 11, "max_comp": 50, "rep_mod": 11},
    23: {"bp_bonus": 78, "skill_learning_mod": 12, "max_comp": 60, "rep_mod": 12},
    24: {"bp_bonus": 91, "skill_learning_mod": 13, "max_comp": 70, "rep_mod": 13},
    25: {"bp_bonus": 105, "skill_learning_mod": 14, "max_comp": 90, "rep_mod": 14},
}

rep_table = {
    1: {"bp_bonus": 0},
    2: {"bp_bonus": 0},
    3: {"bp_bonus": 0},
    4: {"bp_bonus": 0},
    5: {"bp_bonus": 0},
    6: {"bp_bonus": 5},
    7: {"bp_bonus": 10},
    8: {"bp_bonus": 15},
    9: {"bp_bonus": 20},
    10: {"bp_bonus": 25},
    11: {"bp_bonus": 25},
    12: {"bp_bonus": 25},
    13: {"bp_bonus": 30},
    14: {"bp_bonus": 30},
    15: {"bp_bonus": 35},
    16: {"bp_bonus": 40},
    17: {"bp_bonus": 45},
    18: {"bp_bonus": 50},
    19: {"bp_bonus": 55},
    20: {"bp_bonus": 60},
    21: {"bp_bonus": 65},
    22: {"bp_bonus": 70},
    23: {"bp_bonus": 75},
    24: {"bp_bonus": 80},
    25: {"bp_bonus": 85},
}

skills_table = {
    "Accounting": {"bp_cost": 3, "die": 8, "universal": False, "tally": 0, "skill": 100,
                   "relevantabilities": {"inte": None}, "req": {"Mathematics": 85}},
    "Administration": {"bp_cost": 5, "die": 6, "universal": True, "tally": 0, "skill": 100,
                       "relevantabilities": {"inte": None, "wis": None, "cha": None}, "req": {}},
    "Agriculture": {"bp_cost": 2, "die": 10, "universal": True, "tally": 0, "skill": 100,
                    "relevantabilities": {"wis": None}, "req": {}},
    "AnimalEmpathy": {"bp_cost": 2, "die": 10, "universal": False, "tally": 0, "skill": 100,
                      "relevantabilities": {"wis": None, "cha": None}, "req": {}},
    "AnimalHerding": {"bp_cost": 1, "die": 10, "universal": False, "tally": 0, "skill": 100,
                      "relevantabilities": {"wis": None}, "req": {}},
    "AnimalHusbandry": {"bp_cost": 1, "die": 10, "universal": True, "tally": 0, "skill": 100,
                        "relevantabilities": {"wis": None}, "req": {}},
    "AnimalLore": {"bp_cost": 1, "die": 10, "universal": False, "tally": 0, "skill": 100,
                   "relevantabilities": {"inte": None}, "req": {}},
    "AnimalMimicry": {"bp_cost": 1, "die": 8, "universal": True, "tally": 0, "skill": 100,
                      "relevantabilities": {"wis": None}, "req": {}},
    "AnimalTraining": {"bp_cost": 10, "die": 10, "universal": False, "tally": 0, "skill": 100,
                       "relevantabilities": {"inte": None, "wis": None},
                       "req": {"AnimalEmpathy": 49, "AnimalLore": 49}},
    "Appraisal": {"bp_cost": 1, "die": 8, "universal": False, "tally": 0, "skill": 100,
                  "relevantabilities": {"inte": None, "wis": None}, "req": {}},
    "ArtisticAbility": {"bp_cost": 1, "die": 6, "universal": True, "tally": 0, "skill": 100,
                        "relevantabilities": {"dex": None, "wis": None}, "req": {}},
    "Blacksmithing/Metalworking": {"bp_cost": 7, "die": 8, "universal": False, "tally": 0, "skill": 100,
                                   "relevantabilities": {"stre": None, "inte": None}, "req": {}},
    "Boating": {"bp_cost": 2, "die": 8, "universal": True, "tally": 0, "skill": 100, "relevantabilities": {"wis": None},
                "req": {}},
    "Bookbinding": {"bp_cost": 1, "die": 10, "universal": False, "tally": 0, "skill": 100,
                    "relevantabilities": {"dex": None, "inte": None},
                    "req": {"Seamstress/Tailor": 85, "Leatherworking": 85}},
    "Botany": {"bp_cost": 1, "die": 8, "universal": False, "tally": 0, "skill": 100,
               "relevantabilities": {"inte": None}, "req": {}},
    "Brewing": {"bp_cost": 1, "die": 12, "universal": False, "tally": 0, "skill": 100,
                "relevantabilities": {"inte": None}, "req": {}},
    "BroncBusting": {"bp_cost": 2, "die": 6, "universal": True, "tally": 0, "skill": 100,
                     "relevantabilities": {"stre": None, "wis": None, "cha": None}, "req": {"Riding": 80}},
    "Calligraphy/Signmaking": {"bp_cost": 1, "die": 10, "universal": False, "tally": 0, "skill": 100,
                                   "relevantabilities": {"dex": None}, "req": {"ReadingComp./Penmanship": 90}},
    "Camouflage": {"bp_cost": 6, "die": 10, "universal": True, "tally": 0, "skill": 100,
                        "relevantabilities": {"wis": None}, "req": {}},
    "Carpentry": {"bp_cost": 2, "die": 10, "universal": True, "tally": 0, "skill": 100,
                  "relevantabilities": {"inte": None}, "req": {}},
    "Cartography": {"bp_cost": 1, "die": 8, "universal": True, "tally": 0, "skill": 100,
                    "relevantabilities": {"inte": None}, "req": {"ReadingComp./Penmanship": 90}},
    "Chemistry": {"bp_cost": 4, "die": 6, "universal": False, "tally": 0, "skill": 100,
                  "relevantabilities": {"inte": None}, "req": {"Mathematics": 85}},
    "Climbing": {"bp_cost": 2, "die": 8, "universal": True, "tally": 0, "skill": 100,
                 "relevantabilities": {"stre": None, "dex": None}, "req": {}},
    "Cobbling": {"bp_cost": 1, "die": 12, "universal": False, "tally": 0, "skill": 100,
                 "relevantabilities": {"dex": None}, "req": {"Leatherworking": 85}},
    "Cooking": {"bp_cost": 1, "die": 12, "universal": True, "tally": 0, "skill": 100,
                "relevantabilities": {"wis": None}, "req": {}},
    "Culture": {"bp_cost": 1, "die": 12, "universal": False, "tally": 0, "skill": 100,
                "relevantabilities": {"inte": None}, "req": {}},
    "CurrentAffairs": {"bp_cost": 2, "die": 6, "universal": True, "tally": 0, "skill": 100,
                            "relevantabilities": {"wis": None}, "req": {}},
    "Deception": {"bp_cost": 4, "die": 6, "universal": True, "tally": 0, "skill": 100,
                  "relevantabilities": {"inte": None, "cha": None}, "req": {}},
    "Demolition": {"bp_cost": 6, "die": 4, "universal": True, "tally": 0, "skill": 100,
                   "relevantabilities": {"inte": None}, "req": {}},
    "Dentistry": {"bp_cost": 5, "die": 8, "universal": False, "tally": 0, "skill": 100,
                  "relevantabilities": {"inte": None}, "req": {}},
    "Diplomacy": {"bp_cost": 4, "die": 8, "universal": True, "tally": 0, "skill": 100,
                       "relevantabilities": {"inte": None, "cha": None}, "req": {}},
    "Disguise": {"bp_cost": 4, "die": 6, "universal": True, "tally": 0, "skill": 100,
                      "relevantabilities": {"inte": None, "cha": None}, "req": {}},
    "Distraction": {"bp_cost": 1, "die": 8, "universal": True, "tally": 0, "skill": 100,
                    "relevantabilities": {"cha": None}, "req": {}},
    "Driving(Stage or Wagon)": {"bp_cost": 3, "die": 20, "universal": True, "tally": 0, "skill": 100,
                                   "relevantabilities": {"wis": None}, "req": {}},
    "EngineeringDesign": {"bp_cost": 7, "die": 4, "universal": False, "tally": 0, "skill": 100,
                          "relevantabilities": {"inte": None}, "req": {"Mathematics": 60}},
    "EscapeArtist": {"bp_cost": 8, "die": 6, "universal": True, "tally": 0, "skill": 100,
                          "relevantabilities": {"dex": None, "inte": None}, "req": {}},
    "FastTalking": {"bp_cost": 1, "die": 8, "universal": True, "tally": 0, "skill": 100,
                    "relevantabilities": {"cha": None}, "req": {}},
    "Fire-Building/Extinguishing": {"bp_cost": 1, "die": 6, "universal": True, "tally": 0, "skill": 100,
                                    "relevantabilities": {"wis": None}, "req": {}},
    "Fishing": {"bp_cost": 1, "die": 10, "universal": True, "tally": 0, "skill": 100,
                     "relevantabilities": {"wis": None}, "req": {}},
    "Forgery": {"bp_cost": 10, "die": 4, "universal": True, "tally": 0, "skill": 100,
                "relevantabilities": {"dex": None, "inte": None}, "req": {"ReadingComp./Penmanship": 65}},
    "FortuneTelling": {"bp_cost": 1, "die": 8, "universal": True, "tally": 0, "skill": 100,
                            "relevantabilities": {"cha": None}, "req": {}},
    "Gambling": {"bp_cost": 7, "die": 6, "universal": False, "tally": 0, "skill": 100,
                      "relevantabilities": {"wis": None, "cha": None}, "req": {}},
    "Gaming": {"bp_cost": 1, "die": 8, "universal": True, "tally": 0, "skill": 100,
               "relevantabilities": {"dex": None, "inte": None}, "req": {}},
    "Geology": {"bp_cost": 4, "die": 6, "universal": False, "tally": 0, "skill": 100,
                     "relevantabilities": {"inte": None}, "req": {}},
    "GleanInformation": {"bp_cost": 2, "die": 8, "universal": True, "tally": 0, "skill": 100,
                         "relevantabilities": {"inte": None, "wis": None, "cha": None}, "req": {}},
    "GracefulEntrance/Exit": {"bp_cost": 1, "die": 6, "universal": True, "tally": 0, "skill": 100,
                                   "relevantabilities": {"cha": None}, "req": {}},
    "Gunsmithing": {"bp_cost": 8, "die": 6, "universal": False, "tally": 0, "skill": 100,
                    "relevantabilities": {"dex": None, "inte": None}, "req": {}},
    "Hiding": {"bp_cost": 3, "die": 6, "universal": True, "tally": 0, "skill": 100,
               "relevantabilities": {"dex": None, "inte": None}, "req": {}},
    "History": {"bp_cost": 1, "die": 12, "universal": False, "tally": 0, "skill": 100,
                "relevantabilities": {"inte": None}, "req": {"ReadingComp./Penmanship": 80}},
    "Hunting": {"bp_cost": 5, "die": 6, "universal": True, "tally": 0, "skill": 100,
                "relevantabilities": {"dex": None, "wis": None}, "req": {}},
    "IdleGossip": {"bp_cost": 1, "die": 12, "universal": True, "tally": 0, "skill": 100,
                   "relevantabilities": {"cha": None}, "req": {}},
    "Interrogation": {"bp_cost": 5, "die": 6, "universal": True, "tally": 0, "skill": 100,
                      "relevantabilities": {"stre": None, "wis": None}, "req": {}},
    "Intimidation": {"bp_cost": 2, "die": 4, "universal": True, "tally": 0, "skill": 100,
                     "relevantabilities": {"cha": None}, "req": {}},
    "Jeweler": {"bp_cost": 9, "die": 6, "universal": False, "tally": 0, "skill": 100,
                "relevantabilities": {"inte": None}, "req": {"Appraisal(minerals)": 90}},
    "JokeTelling": {"bp_cost": 1, "die": 4, "universal": True, "tally": 0, "skill": 100,
                    "relevantabilities": {"cha": None}, "req": {}},
    "Journalism/Composition": {"bp_cost": 2, "die": 6, "universal": False, "tally": 0, "skill": 100,
                               "relevantabilities": {"inte": None}, "req": {"ReadingComp./Penmanship": 80}},
    "Juggling": {"bp_cost": 2, "die": 8, "universal": True, "tally": 0, "skill": 100,
                 "relevantabilities": {"dex": None}, "req": {}},
    "Language": {"bp_cost": 5, "die": 8, "universal": False, "tally": 0, "skill": 100,
                 "relevantabilities": {"inte": None}, "req": {}},
    "Law": {"bp_cost": 6, "die": 6, "universal": False, "tally": 0, "skill": 100, "relevantabilities": {"inte": None},
            "req": {"ReadingComp./Penmanship": 60}},
    "Leatherworking": {"bp_cost": 1, "die": 8, "universal": False, "tally": 0, "skill": 100,
                       "relevantabilities": {"dex": None, "inte": None}, "req": {}},
    "Listening": {"bp_cost": 5, "die": 6, "universal": True, "tally": 0, "skill": 100,
                  "relevantabilities": {"wis": None}, "req": {}},
    "LockPicking": {"bp_cost": 8, "die": 6, "universal": True, "tally": 0, "skill": 100,
                    "relevantabilities": {"dex": None, "inte": None}, "req": {"Listening": 85}},
    "Locksmithing": {"bp_cost": 4, "die": 6, "universal": False, "tally": 0, "skill": 100,
                          "relevantabilities": {"dex": None, "inte": None}, "req": {}},
    "Logging": {"bp_cost": 3, "die": 20, "universal": False, "tally": 0, "skill": 100,
                "relevantabilities": {"stre": None, "inte": None}, "req": {}},
    "MachineOperating/Repairing": {"bp_cost": 2, "die": 8, "universal": False, "tally": 0, "skill": 100,
                                        "relevantabilities": {"inte": None}, "req": {}},
    "Mathematics": {"bp_cost": 6, "die": 8, "universal": False, "tally": 0, "skill": 100,
                    "relevantabilities": {"inte": None}, "req": {"ReadingComp./Penmanship": 90}},
    "Medicine": {"bp_cost": 10, "die": 4, "universal": False, "tally": 0, "skill": 100,
                      "relevantabilities": {"dex": None, "inte": None}, "req": {}},
    "MilitaryEngineering": {"bp_cost": 2, "die": 4, "universal": False, "tally": 0, "skill": 100,
                            "relevantabilities": {"inte": None}, "req": {"EngineeringDesign": 80}},
    "MilitaryStrategy/Tactics": {"bp_cost": 5, "die": 6, "universal": False, "tally": 0, "skill": 100,
                                      "relevantabilities": {"inte": None}, "req": {}},
    "Millinery": {"bp_cost": 1, "die": 10, "universal": False, "tally": 0, "skill": 100,
                  "relevantabilities": {"inte": None}, "req": {}},
    "MimicDialect": {"bp_cost": 1, "die": 8, "universal": True, "tally": 0, "skill": 100,
                          "relevantabilities": {"cha": None}, "req": {}},
    "Nursing": {"bp_cost": 3, "die": 8, "universal": False, "tally": 0, "skill": 100,
                "relevantabilities": {"wis": None}, "req": {}},
    "Observation": {"bp_cost": 6, "die": 8, "universal": True, "tally": 0, "skill": 100,
                    "relevantabilities": {"wis": None}, "req": {}},
    "Oration": {"bp_cost": 2, "die": 8, "universal": True, "tally": 0, "skill": 100,
                "relevantabilities": {"inte": None, "cha": None}, "req": {}},
    "Photography": {"bp_cost": 1, "die": 8, "universal": False, "tally": 0, "skill": 100,
                    "relevantabilities": {"inte": None}, "req": {"Chemistry": 85}},
    "PickPocket": {"bp_cost": 9, "die": 6, "universal": True, "tally": 0, "skill": 100,
                   "relevantabilities": {"dex": None}, "req": {}},
    "Pottery": {"bp_cost": 1, "die": 10, "universal": False, "tally": 0, "skill": 100,
                     "relevantabilities": {"dex": None, "wis": None}, "req": {}},
    "PrimitiveRangedWeaponUse": {"bp_cost": 4, "die": 12, "universal": False, "tally": 0, "skill": 100,
                                      "relevantabilities": {"dex": None}, "req": {}},
    "PrimitiveWeaponMaking": {"bp_cost": 6, "die": 8, "universal": False, "tally": 0, "skill": 100,
                              "relevantabilities": {"dex": None}, "req": {}},
    "Prospecting": {"bp_cost": 9, "die": 6, "universal": True, "tally": 0, "skill": 100,
                    "relevantabilities": {"wis": None}, "req": {}},
    "ReadingComp./Penmanship": {"bp_cost": 4, "die": 6, "universal": False, "tally": 0, "skill": 100,
                                "relevantabilities": {"inte": None}, "req": {}},
    "ReadingLips": {"bp_cost": 7, "die": 4, "universal": True, "tally": 0, "skill": 100,
                    "relevantabilities": {"inte": None}, "req": {}},
    "Recruiting": {"bp_cost": 4, "die": 8, "universal": True, "tally": 0, "skill": 100,
                   "relevantabilities": {"cha": None}, "req": {}},
    "Religion": {"bp_cost": 5, "die": 12, "universal": True, "tally": 0, "skill": 100,
                 "relevantabilities": {"inte": None}, "req": {}},
    "ResistPersuasion": {"bp_cost": 2, "die": 8, "universal": True, "tally": 0, "skill": 100,
                         "relevantabilities": {"wis": None}, "req": {}},
    "Riding": {"bp_cost": 3, "die": 8, "universal": True, "tally": 0, "skill": 100,
               "relevantabilities": {"dex": None, "wis": None}, "req": {}},
    "RopeUse": {"bp_cost": 2, "die": 8, "universal": True, "tally": 0, "skill": 100, "relevantabilities": {"dex": None},
                "req": {}},
    "Salesmanship": {"bp_cost": 7, "die": 6, "universal": True, "tally": 0, "skill": 100,
                     "relevantabilities": {"inte": None, "wis": None, "cha": None}, "req": {}},
    "Seamstress/Tailor": {"bp_cost": 1, "die": 12, "universal": False, "tally": 0, "skill": 100,
                          "relevantabilities": {"dex": None}, "req": {}},
    "Searching": {"bp_cost": 5, "die": 8, "universal": True, "tally": 0, "skill": 100,
                       "relevantabilities": {"wis": None}, "req": {}},
    "Seduction": {"bp_cost": 1, "die": 6, "universal": True, "tally": 0, "skill": 100,
                       "relevantabilities": {"cha": None, "lks    ": None}, "req": {}},
    "SetTraps": {"bp_cost": 10, "die": 8, "universal": False, "tally": 0, "skill": 100,
                 "relevantabilities": {"dex": None}, "req": {}},
    "Skinning/Tanning": {"bp_cost": 3, "die": 8, "universal": True, "tally": 0, "skill": 100,
                         "relevantabilities": {"stre": None, "wis": None}, "req": {}},
    "Slaughter": {"bp_cost": 2, "die": 10, "universal": True, "tally": 0, "skill": 100,
                  "relevantabilities": {"stre": None, "inte": None}, "req": {}},
    "SleightofHand": {"bp_cost": 2, "die": 6, "universal": True, "tally": 0, "skill": 100,
                      "relevantabilities": {"dex": None}, "req": {}},
    "SlickTalker": {"bp_cost": 4, "die": 4, "universal": False, "tally": 0, "skill": 100,
                    "relevantabilities": {"inte": None, "cha": None}, "req": {}},
    "Sneaking": {"bp_cost": 8, "die": 6, "universal": True, "tally": 0, "skill": 100,
                 "relevantabilities": {"dex": None}, "req": {}},
    "SocialEtiquette": {"bp_cost": 4, "die": 6, "universal": False, "tally": 0, "skill": 100,
                        "relevantabilities": {"cha": None}, "req": {}},
    "Stonemasonry": {"bp_cost": 2, "die": 10, "universal": False, "tally": 0, "skill": 100,
                     "relevantabilities": {"stre": None, "inte": None}, "req": {}},
    "Survival": {"bp_cost": 7, "die": 6, "universal": True, "tally": 0, "skill": 100,
                 "relevantabilities": {"con": None, "wis": None, "inte": None}, "req": {}},
    "Swimming": {"bp_cost": 1, "die": 12, "universal": False, "tally": 0, "skill": 100,
                 "relevantabilities": {"stre": None, "con": None}, "req": {}},
    "TelegraphOperating": {"bp_cost": 4, "die": 8, "universal": False, "tally": 0, "skill": 100,
                           "relevantabilities": {"inte": None}, "req": {"ReadingComp./Penmanship": 90}},
    "Tracking": {"bp_cost": 9, "die": 4, "universal": True, "tally": 0, "skill": 100,
                 "relevantabilities": {"wis": None}, "req": {}},
    "Ventriloquism": {"bp_cost": 8, "die": 4, "universal": True, "tally": 0, "skill": 100,
                      "relevantabilities": {"inte": None}, "req": {}},
    "WeatherSense": {"bp_cost": 3, "die": 4, "universal": True, "tally": 0, "skill": 100,
                     "relevantabilities": {"stre": None}, "req": {}},
    "Weaving": {"bp_cost": 1, "die": 8, "universal": False, "tally": 0, "skill": 100,
                "relevantabilities": {"dex": None, "inte": None}, "req": {}},
}

lmc_status = (
    (3, "Agent",()),
    (5, "Auctioneer",()),
    (7, "Bank Clerk",()),
    (9, "Barber",()),
    (11, "Bartender",()),
    (13, "Bording house keeper",()),
    (15, "Book Keeper",()),
    (18, "Clerk",()),
    (20, "Confectioner",()),
    (22, "Druggist",()),
    (24, "Editor",()),
    (26, "furniture Maker ",()),
    (30, "Grocer",()),
    (32, "Hostler",()),
    (34, "Insurance Agent",()),
    (36, "Hotel Keeper",()),
    (38, "Poor House Keeper",()),
    (40, "Land Agent",()),
    (43, "Landlord",()),
    (45, "Lightening rod seller",()),
    (47, "Lumber Merchant",()),
    (54, "Merchant Other",()),
    (57, "Clergyman Preacher",()),
    (58, "Music Teacher",()),
    (60, "Peddler",()),
    (62, "Produce Dealer",()),
    (66, "Brewer",()),
    (68, "Speculator",()),
    (72, "Tobacconist",()),
    (74, "Saloon Keeper",()),
    (80, "Teacher",()),
    (82, "Constable",()),
    (84, "Express Agent",()),
    (86, "Fireman",()),
    (88, "Justice of the Peace",()),
    (90, "Mail Carrier",()),
    (92, "Public Notary",()),
    (94, "Post Master",()),
    (96, "Rail Road Agent",()),
    (98, "Deputy Sherrif",()),
    (100, "Street Inspector",()),
)

mmc_status = (
    (10, "Civil Engineer",()),
    (20, "Watchmaker",()),
    (27, "Dentist",()),
    (31, "Engineer",()),
    (35, "Steam/Locomotive Engineer",()),
    (43, "Jeweler",()),
    (51, "Miller Steam",()),
    (59, "Nurse",()),
    (68, "Doctor",()),
    (76, "Railroad Boss",()),
    (84, "Silversmith",()),
    (92, "Steamboat Captain",()),
    (100, "Surveyor",()),
)

umc_status = (
    (10, "Banker", ("Accounting", "Mathematics")),
    (20, "Jeweler", ("Jeweler", "Appraisal")),
    (30, "Land Owner", ("Administration")),
    (40, "Lawyer",("Law")),
    (50, "Established Merchant",("Diplomacy")),
    (60, "Military Officer(retired)",("MilitaryStrategy/Tactics")),
    (70, "Mine Owner",()),
    (80, "Ranch Owner",()),
    (90, "Established Physician",()),
    (100, "Railroad Shareholder",()),
)


def upfinds(table):
    roll = dice(100, 1)
    for index, job, _ in table:
        if roll <= index:
            return job


def dice(die, number_of_dice):
    i = 0
    total = 0
    while i != number_of_dice:
        i = i + 1
        roll = random.randint(1, die)
        total = total + roll
    return total


def percentile_dice():  #calls dice rolls 1D10 -1 (Value between 0-9) * 10 to make tens the rolls and adds 1d10 for the units 
    pct = (dice(10, 1) - 1) * 10 + dice(10, 1)
    return pct


def card_deck():
    card = dice(13, 1)  # gets a value of 1-13 for the card 1 is ace 11 jack 12 queen 13 is king
    if card == 11:
        card = "Jack"
    if card == 12:
        card = "Queen"
    if card == 13:
        card = "King"
    if card == 1:
        card = "Ace"
    suit = dice(4, 1)  # gets a value 1-4 replaces number with suit
    if suit == 1:
        return str(card) + " of Hearts"
    if suit == 2:
        return str(card) + " of Diamonds"
    if suit == 3:
        return str(card) + " of Clubs"
    if suit == 4:
        return str(card) + " of Spades "


def coin():
    flip = dice(2, 1)
    if flip == 1:
        return "Heads"
    else:
        return "Tails"

        # Makes the roll need to create the base attributes of a character  eg STRE DEX etc


def upfind(table):
    roll = 80
    for index, job, *skills, in table:
        if roll <= index:
            print (index, job, skills)
            for sk in skills:
                if sk != ():
                    skills_table[sk]["skill"] -= dice(skills_table[sk]["die"], 2)
                    print (sk, skills_table[sk]["skill"])
            return job


print (upfind(umc_status))


def mk_stat():
    ability = dice(6, 3)
    pct = percentile_dice()
    if pct == 100:
        ability = ability + 1
        pct = 0
    return (ability, pct)


pc_stats = {"Strength": {'stat': 0, 'pct': 0},
            "Inteligence": {'stat': 0, 'pct': 0},
            "Wisdom": {'stat': 0, 'pct': 0, },
            "Dexterity": {'stat': 0, 'pct': 0},
            "Consitution": {'stat': 0, 'pct': 0},
            "Looks": {'stat': 0, 'pct': 0},
            "Charisma": {'stat': 0, 'pct': 0},
}


def mk_pcstats():
    for s in pc_stats:
        for i, _ in pc_stats[s].items():
            if i == 'pct':
                j = percentile_dice()
                pc_stats[s][i] = j
            else:
                j = dice(6, 3)
                pc_stats[s][i] = j


mk_pcstats()
print (pc_stats)


def table_check(stat, table):
    if table is (stre_table or dex_table):
        if stat["pct"] < 50:
            stat_pctLookup = 1
        else:
            stat_pctLookup = 51
            der = table[stat["stat"]][stat_pctLookup]
    else:
        der = table[stat["stat"]]
    return der


def chk_stre():
    chk = table_check(pc_stats['Strength'], stre_table)
    return chk


def chk_con():
    chk = table_check(pc_stats['Consitution'], con_table)
    return chk


def chk_looks():
    chk = table_check(pc_stats['Looks'], looks_table)
    return chk


def chk_cha():
    chk = table_check(pc_stats['Charisma'], cha_table)
    return chk


def chk_wis():
    chk = table_check(pc_stats['Wisdom'], wis_table)
    return chk


def chk_inte():
    chk = table_check(pc_stats['Inteligence'], inte_table)
    return chk


def chk_dex():
    chk = table_check(pc_stats['Dexterity'], dex_table)
    return chk


print (chk_looks())

ruUrBk = "Urban"
rep = 0
fame = 0
money = 0
social_class = None
pob = None
sex = "Male"


def mk_rep():
    a = 0
    b = 0
    for s in pc_stats:
        for i, k in pc_stats[s].items():
            if i == 'pct':
                a = a + k
            else:
                b = b + k
        a /= 100
        a = round((a + b) / 7)
        a = a + looks_table[(pc_stats['Looks']['stat'])]["rep_mod"] + cha_table[(pc_stats['Charisma']['stat'])][
            "rep_mod"]
    return a, rep_table[a]


def mk_age():
    age = 14
    roll = dice(12, 1)
    age = age + roll
    while roll == 12:
        roll = dice(12, 1)
        age = age + roll
    return age


def mk_placeOfBirth():
    roll = dice(100, 1)
    if roll <= 10:
        roll2 = dice(20, 1)
        if roll2 in range(1, 3):
            return "England"
        elif roll2 == 3:
            return "Scotland"
        elif roll2 in range(4, 11):
            return "Ireland"
        elif roll2 in range(11, 13):
            return "China"
        elif roll2 in range(13, 18):
            return "Germanic"
        elif roll2 == 18:
            return "Benelux"
        elif roll2 in range(19, 21):
            return "Scandinavia"
    elif roll in range(11, 13):
        return "Mexico Indigenous"
    elif roll in range(13, 20):
        return "Mexico"
    elif roll in range(20, 22):
        return "Texas Louisiana"
    elif roll in range(22, 29):
        return "Texas Gulf Coast"
    elif roll == 29:
        return "West Texas"
    elif roll in range(29, 31):
        return "Sequoyah"
    elif roll in range(32, 35):
        return "Indian Native"
    elif roll in range(35, 37):
        return "Deseret"
    elif roll in range(37, 40):
        return "Canada English"
    elif roll in range(40, 42):
        return "Canada French"
    elif roll in range(42, 48):
        return "USA New England( ME, NH, VT, MA, CT, RI)"
    elif roll in range(48, 57):
        return "USA East(NY,PA,NJ,KN)"
    elif roll in range(57, 64):
        return "USA Central(OH, IN, IL, WI, MI)"
    elif roll in range(64, 70):
        return "USA South(KY, MO)"
    elif roll in range(70, 75):
        return "USA West(MN, IA, Territories)"
    elif roll in range(75, 81):
        return "CSA NorthEast(DE,MD,ColumbiaCounty was DC)"
    elif roll in range(81, 88):
        return "CSA Atlantic Seaboard(Old South, VA, Carolinas, GA)"
    elif roll in range(88, 92):
        return "CSA Southeast(FL, Cuba)"
    elif roll in range(92, 100):
        return "CSA West(MS, AL, TN)"
    else:
        return "French Oreleans"


def mk_RuUrBk():
    global pob
    global ruUrBk
    pob = mk_placeOfBirth()
    if pob == ("England" or "Scotland" or "Ireland" or "China" or "Germanic" or "Scandinavia" or "Benelux"):
        if dice(100, 1) in range(1, 61):
            ruUrBk = "Rural"
            return "Rural", pob,
        else:
            ruUrBk = "Urban"
            return "Urban", pob
    elif pob == ("Mexico" or "Mexico Indigenous" or "Deseret" or "Indian Native"):
        if dice(100, 1) in range(1, 96):
            ruUrBk = "Rural"
            return "Rural", pob
        else:
            ruUrBk = "Urban"
            return "Urban", pob
    elif pob == ("Texas Louisiana" or "French Oreleans" or "Texas Gulf Coast" or "West Texas"):
        if dice(100, 1) in range(1, 92):
            ruUrBk = "Rural"
            return "Rural", pob
        else:
            ruUrBk = "Urban"
            return "Urban", pob
    elif "USA" in pob:
        if dice(100, 1) in range(1, 56):
            ruUrBk = "Rural"
            return "Rural", pob
        else:
            ruUrBk = "Urban"
            return "Urban", pob
    else:
        if dice(100, 1) in range(1, 88):
            ruUrBk = "Rural"
            return "Rural", pob
        else:
            ruUrBk = "Urban"
            return "Urban", pob


def mk_handed():
    roll = dice(100, 1)
    if roll in range(1, 91):
        return "Right"
    elif roll in range(91, 100):
        return "Left"
    else:
        return "Ambidextrous"


def mk_height(sex):
    roll = dice(100, 1)
    if sex == "Female":
        if roll == 1:
            return 60 - dice(12, 1)
        elif roll in range(2, 4):
            return 58
        elif roll in range(4, 6):
            return 59
        elif roll in range(6, 13):
            return 60
        elif roll in range(13, 21):
            return 61
        elif roll in range(21, 30):
            return 62
        elif roll in range(30, 42):
            return 63
        elif roll in range(42, 62):
            return 64
        elif roll in range(62, 76):
            return 65
        elif roll in range(76, 86):
            return 66
        elif roll in range(86, 92):
            return 67
        elif roll in range(92, 97):
            return 68
        elif roll in range(97, 99):
            return 69
        elif roll == 99:
            return 70
        else:
            return 67 + dice(12, 1)
    if sex == "Male":
        if roll == 1:
            return 65 - dice(12, 1)
        elif roll in range(2, 4):
            return 63
        elif roll in range(4, 6):
            return 64
        elif roll in range(6, 13):
            return 65
        elif roll in range(13, 21):
            return 66
        elif roll in range(21, 30):
            return 67
        elif roll in range(30, 42):
            return 68
        elif roll in range(42, 62):
            return 69
        elif roll in range(62, 76):
            return 70
        elif roll in range(76, 86):
            return 71
        elif roll in range(86, 92):
            return 72
        elif roll in range(92, 97):
            return 73
        elif roll in range(97, 99):
            return 74
        elif roll == 99:
            return 75
        else:
            return 72 + dice(12, 1)


def mk_weight(height, sex, age):
    roll = dice(20, 1)
    result = 0
    if sex == "Female":
        if roll == 1:
            result = 28 - dice(6, 1)
        elif roll == 2:
            result = 27
        elif roll in range(3, 5):
            result = 28
        elif roll in range(5, 9):
            result = 29
        elif roll in range(9, 12):
            result = 30
        elif roll in range(12, 14):
            result = 31
        elif roll == 14:
            result = 32
        elif roll == 15:
            result = 33
        elif roll == 16:
            result = 34
        elif roll == 17:
            result = 35
        elif roll == 18:
            result = 36
        elif roll == 19:
            result = 37
        else:
            result = 35 + dice(12, 1)
    if sex == "Male":
        if roll == 1:
            result = 30 - dice(6, 1)
        elif roll == 2:
            result = 29
        elif roll in range(3, 5):
            result = 30
        elif roll in range(5, 9):
            result = 31
        elif roll in range(9, 12):
            result = 32
        elif roll in range(12, 14):
            result = 33
        elif roll == 14:
            result = 34
        elif roll == 15:
            result = 35
        elif roll == 16:
            result = 36
        elif roll == 17:
            result = 37
        elif roll == 18:
            result = 38
        elif roll == 19:
            result = 39
        else:
            result = 37 + dice(12, 1)
    if age in range(30, 36):
        result = result + 2
    if age in range(36, 41):
        result = result + 3
    if age in range(41, 46):
        result = result + 4
    if age in range(46, 61):
        result = result + 6
    if age > 60:
        result = result + 7
    a = result * (height * height) / 1000.0
    return int(round(a, 0))


def mk_money():
    global money
    roll = dice(100, 1)
    if roll in range(0, 6):
        money = 0 - dice(60, 1) * 10
        return money
    elif roll in range(6, 11):
        money = 0
        return money
    elif roll in range(11, 16):
        money = 5
        return money
    elif roll in range(16, 21):
        money = 5 + dice(4, 1)
        return money
    elif roll in range(21, 26):
        money = 10
        return money
    elif roll in range(26, 31):
        money = 10 + dice(4, 1)
        return money
    elif roll in range(31, 36):
        money = 15
        return money
    elif roll in range(36, 41):
        money = 15 + dice(6, 1)
        return money
    elif roll in range(41, 46):
        money = 20
        return money
    elif roll in range(46, 51):
        money = 20 + dice(6, 1)
        return money
    elif roll in range(51, 56):
        money = 25
        return money
    elif roll in range(56, 61):
        money = 25 + dice(6, 1)
        return money
    elif roll in range(61, 66):
        money = 30
        return money
    elif roll in range(66, 71):
        money = 30 + dice(8, 1)
        return money
    elif roll in range(71, 76):
        money = 35
        return money
    elif roll in range(76, 81):
        money = 35 + dice(8, 1)
        return money
    elif roll in range(81, 86):
        money = 40
        return money
    elif roll in range(86, 91):
        money = 40 + dice(8, 1)
        return money
    elif roll in range(91, 96):
        money = 45
        return money
    elif roll in range(96, 101):
        money = 45 + dice(8, 1)
        return money
    elif roll in range(101, 106):
        money = 50
        return money
    elif roll in range(106, 111):
        money = 50 + dice(10, 1)
        return money
    elif roll in range(111, 116):
        money = 60 + dice(10, 2)
        return money
    else:
        money = 70 + dice(10, 3)
        return money


def mk_circOfBirth():
    roll = dice(100, 1)
    if roll in range(1, 93):
        return "Legitimate"
    if roll in range(93, 101):
        roll2 = dice(100, 1)
        if roll2 in range(1, 4):
            return "Illegitimate abandoned at birth"
        elif roll2 in range(4, 9):
            return "Illegitimate Mother was a whore, Father unknown"
        elif roll2 in range(10, 13):
            return "Illegitimate Mother was a whore, Father known"
        elif roll2 in range(13, 24):
            return "Illegitimate Result of sex before marriage, Father unknown"
        elif roll2 in range(24, 57):
            return "Illegitimate Result of sex before marriage, Father known"
        elif roll2 in range(57, 68):
            return "Illegitimate Result of an affair, Father unknown"
        else:
            return "Illegitimate Result of an affair, Father known"


def mk_parentStatus():
    roll = dice(100, 1)
    onecount = 0
    celebrity = "Parent is a celebrity"
    while roll == 1:
        roll = dice(100, 1)
        onecount = onecount + 1
        if roll in range(2, 51):
            return "Both Parents Living" + " " + celebrity + " " + str(onecount)
        elif roll in range(51, 71):
            return "Father Deceased" + " " + celebrity + " " + str(onecount)
        elif roll in range(71, 81):
            return "Mother Deceased" + " " + celebrity + " " + str(onecount)
        elif roll in range(81, 91):
            return "Both Deceased after you reached Teens" + " " + celebrity + " " + str(onecount)
        else:
            return "Both parents are deceased. Character is an Orphan" + " " + celebrity + " " + str(onecount)
    if roll in range(2, 51):
        return "Both Parents Living"
    elif roll in range(51, 71):
        roll = dice(20, 1)
        if roll > 15:
            return "Father Deceased. Mother Remarried"
        return "Father Deceased"
    elif roll in range(71, 81):
        roll = dice(20, 1)
        if roll > 15:
            return "Mother Deceased. Father Remarried"
        return "Mother Deceased"
    elif roll in range(81, 91):
        return "Both Deceased after you reached Teens"
    else:
        return "Both parents are deceased. Character is an Orphan"


def mk_nosiblings():
    roll = dice(20, 1)
    if roll == 1:
        siblings = 0
    elif roll == 2:
        siblings = 1
    elif roll == 3:
        siblings = 2
    elif roll == 4:
        siblings = 3
    elif roll in range(5, 7):
        siblings = 4
    elif roll in range(7, 10):
        siblings = 5
    elif roll in range(10, 15):
        siblings = 6
    elif roll in range(15, 18):
        siblings = 7
    elif roll == 18:
        siblings = 8
    elif roll == 19:
        siblings = 9
    else:
        siblings = 10
    return siblings


def mk_siblingRelations():
    roll = dice(12, 2)
    roll = roll + cha_table[(pc_stats['Charisma']['stat'])]["rep_mod"]
    if roll in range(1, 5):
        return "Bitter Enemy. These rivals hold an intense hate for some past offense, real or imagined."
    elif roll in range(5, 10):
        return "Argumentative. For some reason, the character and his sibling just cant get along without bickering."
    elif roll in range(10, 17):
        return "Natural. The character and sibling are close, with good family ties, but few intense feelings except during special times of hurt or celebration."
    elif roll in range(17, 22):
        return "Very Close. The sibling and character communicate often, and always try to help the other in times of need."
    else:
        return "Devoted. An extremely close bond exists between these two, and one would easily lay down his life for the other."


def disease_rural():
    roll = dice(100, 1)
    if roll in range(1, 23):
        living = False
        cause = "Died in infancy from Infectious disease"
    elif roll in range(23, 27):
        living = False
        cause = "Died in childhood from Diarrhea"
    elif roll in range(27, 30):
        living = False
        cause = "Died from Pneumonia"
    elif roll in range(30, 33):
        living = False
        cause = "Died from Smallpox"
    elif roll in range(33, 38):
        living = False
        cause = "Died from Tuberculosis"
    elif roll == 38:
        living = False
        cause = "Died from Typhoid fever"
    elif roll in range(39, 43):
        living = False
        cause = "Died from Influenza"
    elif roll in range(43, 48):
        living = False
        cause = "Died from Accidental Causes"
    else:
        living = True
        cause = " "
    return living, cause


def disease_urban():
    roll = dice(100, 1)
    if roll in range(1, 27):
        living = False
        cause = "Died in infancy from Infectious disease"
    elif roll in range(27, 34):
        living = False
        cause = "Died in childhood from Diarrhea"
    elif roll in range(34, 40):
        living = False
        cause = "Died from Pneumonia"
    elif roll in range(40, 42):
        living = False
        cause = "Died from Smallpox"
    elif roll in range(42, 48):
        living = False
        cause = "Died from Tuberculosis"
    elif roll in range(48, 50):
        living = False
        cause = "Died from Typhoid fever"
    elif roll in range(50, 54):
        living = False
        cause = "Died from Influenza"
    elif roll in range(54, 58):
        living = False
        cause = "Died from Cholera"
    elif roll in range(58, 67):
        living = False
        cause = "Died from Accidental Causes"
    else:
        living = True
        cause = " "
    return living, cause


def mk_siblingStatus():
    nosiblings = mk_nosiblings()
    sibling = 0
    siblingStatus = {}
    while nosiblings != sibling:
        if dice(2, 1) == 1:
            sex = "Male"
        else:
            sex = "Female"
        # if rural or urban background calls disease rural or urban which returns if the sibling is alive is not returns cause of death            
        if ruUrBk == "Urban":
            living, cause = disease_urban()
        else:
            living, cause = disease_rural()
        # adds current sibbling to the siblingStatus dictionary        
        siblingStatus[sibling] = {"sibling": sibling, "sex": sex, "living": living, "cause": cause}
        sibling = sibling + 1
    # Loops through sibling status looking for living  siblings calls mk_siblingRelations to create a relationship for each surviving sibling        
    for s in siblingStatus:
        if siblingStatus[s]["living"] == True:
            relation = mk_siblingRelations()
            siblingStatus[s]["Relation"] = relation

    for s in siblingStatus:
        print (siblingStatus[s])
    #change this later to return instead of print
    print (mk_upBringing(siblingStatus))
    return siblingStatus


def mk_upBringing(siblingStatus):
    roll = dice(100, 1)
    siblings = 0
    for s in siblingStatus:
        if siblingStatus[s]["living"] == True:
            siblings = siblings + 1
    roll2 = dice(siblings + 1, 1)
    if roll2 == 1:
        orderOfBirth = "First Born Surviving Child"
    elif roll2 == 2:
        orderOfBirth = "Second Born Surviving Child"
    else:
        orderOfBirth = "Dang! outa luck for inheritance"
    roll = roll + siblings
    if roll in range(1, 13):
        return "Extraordinary Parents. You grew up extremely well nurtured and properly cared for", orderOfBirth
    elif roll in range(13, 25):
        return "Loving Parents. Child grew up well nurtured and properly cared-for", orderOfBirth
    elif roll in range(25, 55):
        return "Average Parents. Parent did an adequate job", orderOfBirth
    elif roll in range(55, 77):
        return "Ill-Equipped.  Parent was well intentioned, but poor at raising children.", orderOfBirth
    elif roll in range(77, 87):
        return "Abusive.You were abused by parent", orderOfBirth
    else:
        return "Indifferent. Parent viewed you child as a burden. You grew up feeling inadequate and unloved.", orderOfBirth


def mk_socialClass():
    global rep
    global money
    global fame
    global social_class
    roll = dice(100, 1)
    if pob == ("England" or "Scotland" or "Ireland" or "China" or "Germanic" or "Scandinavia" or "Benelux"):
        while roll < 21:
            roll = dice(100, 1)
    if roll < 9:
        social_class = "Below Lower Class"
        job = blc_status()
        rep = rep - 10
        money = money - 40
    elif roll in range(9, 21):
        social_class = "Lower Lower Class"
        job = llc_status()
        rep = rep - 5
        money = money - 20
    elif roll in range(21, 51):
        social_class = "Middle Lower Class"
        if ruUrBk == "Urban":
            job = upfind(mlcR_status)
        else:
            job = upfind(mlcU_status)
        rep = rep - 3
        money = money - 15
    elif roll in range(51, 81):
        social_class = "Upper Lower Class"
        if ruUrBk == "Urban":
            job = upfind(mlcR_status)
        else:
            job = upfind(mlcU_status)
        rep = rep - 1
        money = money - 10
    elif roll in range(81, 88):
        social_class = "Lower Middle Class"
        job = upfind(lmc_status)
        money = money - 5
    elif roll in range(88, 93):
        social_class = "Middle Middle Class"
        job = upfind(mmc_status)
    elif roll in range(93, 98):
        social_class = "Upper Middle Class"
        job = upfind(umc_status)
        money = money + 5
    elif roll == 98:
        social_class = "Lower Upper Class"
        job = "Child of a Military Officer/New Money Industrialist or Political Leader"
        fame = fame + 1
        rep = rep + 1
        money = money - 10
    elif roll == 99:
        social_class = "Middle Upper Class"
        job = "Child of a Wealthy Land Owner"
        fame = fame + 5
        rep = rep + 5
        money = money + 15
    else:
        social_class = "Upper Upper Class"
        job = "Child of Old Money/Minor Nobility"
        fame = fame + 10
        rep = rep + 10
        money = money + 20
    return (social_class, job
    )


def previous_Socialclass():
    roll = dice(100, 1)
    if pob == ("England" or "Scotland" or "Ireland" or "China" or "Germanic" or "Scandinavia" or "Benelux"):
        while roll < 21:
            roll = dice(100, 1)
    if roll < 9:
        psocial_class = "Below Lower Class"
    elif roll in range(9, 21):
        psocial_class = "Lower Lower Class"
    elif roll in range(21, 51):
        psocial_class = "Middle Lower Class"
    elif roll in range(51, 81):
        psocial_class = "Upper Lower Class"
    elif roll in range(81, 88):
        psocial_class = "Lower Middle Class"
    elif roll in range(88, 93):
        psocial_class = "Middle Middle Class"
    elif roll in range(93, 98):
        psocial_class = "Upper Middle Class"
    elif roll == 98:
        psocial_class = "Lower Upper Class"
    elif roll == 99:
        psocial_class = "Middle Upper Class"
    else:
        psocial_class = "Upper Upper Class"
    return psocial_class


def freeEscapedSlave():
    roll = dice(100, 1)
    if roll in range(1, 9):
        prof = "Cook"
        #example of how the table should be manipulated. Gets 2 free tallies in cooking for prof. Rolls 2 times the die in the skills_table for cooking removes the roll from skill in cooking
        skills_table["Cooking"]["skill"] = skills_table["Cooking"]["skill"] - dice(skills_table["Cooking"]["die"], 2)
    elif roll in range(9, 80):
        prof = "Farm Hand"
    else:
        prof = "Laborer"
    return prof


mlcR_status = (
    (2, "Cook",()),
    (4, "Drover",()),
    (64, "Farm Hand",()),
    (84, "Farmer",()),
    (85, "Fisherman",()),
    (86, "Sailor",()),
    (88, "Gardener",()),
    (90, "Hunter",()),
    (92, "Labourer",()),
    (94, "Mill Hand",()),
    (96, "Miller",()),
    (98, "Railroad Hand",()),
    (100, "Lumberjack",()),
)

artisan_status = (
    (2, "Artist",()),
    (4, "Baker",()),
    (6, "Basket Maker",()),
    (9, "Blacksmith",()),
    (10, "Brickmaker",()),
    (15, "Brick Mason",()),
    (17, "Broom Maker",()),
    (19, "Butcher",()),
    (21, "Cabinet Maker",()),
    (26, "Carpenter",()),
    (27, "Coach Maker",()),
    (29, "Cooper",()),
    (31, "Dress Maker",()),
    (34, "Founderer",()),
    (35, "Gunsmith",()),
    (37, "Saddler",()),
    (39, "Hatter",()),
    (40, "Ligtening Rod Maker",()),
    (45, "Livery Stable Worker",()),
    (47, "Machinist",()),
    (48, "Master Carpenter",()),
    (49, "Master Mason",()),
    (51, "Mechanic",()),
    (54, "Grist Miller",()),
    (56, "Millinery",()),
    (58, "Moulder",()),
    (61, "Comercial Painter",()),
    (63, "Pattern Maker",()),
    (65, "Plasterer",()),
    (67, "Potter",()),
    (68, "Printer",()),
    (70, "Rock Dresser",()),
    (73, "Wood Sawyer",()),
    (75, "Tailor/Seamstress",()),
    (77, "Shoemaker",()),
    (79, "Stonecutter",()),
    (81, "Stonemason",()),
    (83, "Tailor/Seamstress",()),
    (86, "Tanner",()),
    (91, "Textile Mill Worker",()),
    (93, "Tinsmith",()),
    (95, "Wagon Maker",()),
    (97, "Weaver",()),
    (99, "Wheelwright",()),
    (100, "Whitewasher",()),
)

mlcU_status = (
    (20, upfinds(artisan_status)),
    (30, "Cook", ()),
    (35, "Gardener", ()),
    (65, "Labourer", ()),
    (85, "Domestic Servant", ()),
    (95, "Servant Other", ()),
    (100, "Laundry Worker", ()),
)


def blc_status():
    roll = dice(6, 1)
    if "CSA" in pob:
        if roll in range(1, 5):
            job = "Escaped Slave"
        elif roll == 5:
            job = "Deserter"
        elif roll == 6:
            job = "Felon"
    elif "USA" in pob:
        if roll in range(1, 4):
            job = "Felon"
        elif roll in range(4, 7):
            job = "Deserter"
    elif pob == ("Texas Louisiana" or "French Oreleans" or "Texas Gulf Coast" or "West Texas"):
        if roll in range(3, 7):
            job = "Felon"
        elif roll in range(1, 3):
            job = "Deserter"
    elif pob == "Deseret":
        job = "Banished"
    else:
        job = "Felon"

    if job == "Felon":
        if dice(8, 1) == 1:
            job = "Felon and wanted out west"
    elif job == "Deserter":
        psocial_class = previous_Socialclass()
        if dice(6, 1) in range(1, 5):
            job = "Deserter fled conscription previous social class " + psocial_class
        else:
            job = "Deserter Fled after enrollment previous social class " + psocial_class
    elif job == "Escaped Slave":
        prof = freeEscapedSlave()
        job = "Escaped Slave previously working as " + prof
    return job


def llc_status():
    roll = dice(6, 1)
    if "CSA" in pob:
        if roll in range(1, 5):
            job = "Freed Slave"
        elif roll == 5:
            job = "Vagrant"
        elif roll == 6:
            job = "Petty Criminal"
    elif "USA" in pob:
        if roll in range(1, 4):
            job = "Freed Slave"
        elif roll in range(4, 6):
            job = "Vagrant"
        elif roll == 6:
            job = "Petty Criminal"
    elif pob == ("Texas Louisiana" or "French Oreleans" or "Texas Gulf Coast" or "West Texas"):
        if roll in range(1, 4):
            job = "Freed Slave"
        elif roll in range(4, 6):
            job = "Vagrant"
        elif roll == 6:
            job = "Petty Criminal"
    elif pob == "Deseret":
        if roll in range(1, 4):
            job = "Vagrent"
        elif roll in range(4, 7):
            job = "Criminal"
    else:
        if roll == 1:
            job = "Freed Slave"
        elif roll in range(2, 5):
            job = "Vagrant"
        elif roll in range(5, 7):
            job = "Criminal"

    if job == "Freed Slave":
        prof = freeEscapedSlave()
        job = "Freed Slave previously working as " + prof
    return job


#freeskill = dice(skills_table["Cooking"]["die"],2)
#skills_table["Cooking"]["skill"] = skills_table["Cooking"]["skill"] - freeskill
#print skills_table["Cooking"]      


#def testy(stat,pct):
#    if pct < 50:
#        stat_pctLookup = 1
#   else:
#        stat_pctLookup = 51
#   der = stat_table[stat][stat_pctLookup]
#    return(stat,stat_pct,der)




#print str_table[stre][stre_pct]
#print pc_stats['Looks']['stat']

print (mk_rep())
print ("Background and Place of Birth ", mk_RuUrBk())
age = (mk_age())
print ("Age ", age)
height = mk_height(sex)
print ("Height Inches ", height)
weight = mk_weight(height, sex, age)
print ("weight ", weight, " Pounds")
print (mk_handed(), " Handed ")
mk_siblingStatus()
print (mk_parentStatus())
print ("base money ", mk_money())
print (mk_socialClass())
print (skills_table["Accounting"])

