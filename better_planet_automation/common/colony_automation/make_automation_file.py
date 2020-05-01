import os

# You need 00_mining_automation.txt, 00_research_automation.txt, 00_habitat_mining_automation.txt files.
# Because this file makes
# 00_farming_automation.txt and 00_generator_automation.txt using 00_farming_automation.txt,
# 00_bureau_automation.txt using 00_research_automation.txt,
# 00_habitat_energy_automation.txt and 00_habitat_fortress_automation.txt using 00_habitat_mining_automation.txt.


MINING_DICT = {"filename" : "00_mining_automation.txt", "words" : ["mining", "building_mineral_purification_plant"]}
GENERATOR_DICT = {"filename" : "00_generator_automation.txt", "words" : ["generator", "building_energy_grid"]}
FARMING_DICT = {"filename" : "00_farming_automation.txt", "words" : ["farming", "building_food_processing_facility"]}

RESEARCH_DICT = {"filename" : "00_research_automation.txt", "words" : ["automate_research_planet", "col_research", "building_research_lab_1"]}
BUREAU_DICT = {"filename" : "00_bureau_automation.txt", "words" : ["automate_bureau_planet", "col_bureau", "building_bureaucratic_1"]}

MINING_HABITAT_DICT = {"filename" : "00_habitat_mining_automation.txt", "words" : ["district_hab_mining", "mining", "building_mineral_purification_plant"]}
GENERATOR_HABITAT_DICT = {"filename" : "00_habitat_energy_automation.txt", "words" : ["district_hab_energy", "energy", "building_energy_grid"]}
FORTRESS_HABITAT_DICT = {"filename" : "00_habitat_fortress_automation.txt", "words" : ["district_hab_housing", "fortress", "building_stronghold"]}


def make_automation_file(original_dict, *target_dicts):
    if not os.path.isfile(original_dict["filename"]):
        print(original_dict["filename"] + " does not exist.")
        return

    with open(original_dict["filename"], encoding="utf-8", mode="r") as f:
        original_text = f.read()

    for target_dict in target_dicts:
        text = original_text

        for idx, original_word in enumerate(original_dict["words"]):
            text = text.replace(original_dict["words"][idx],target_dict["words"][idx])

        with open(target_dict["filename"], encoding="utf-8", mode="w") as f:
            f.write(text)

if __name__ == '__main__':
    make_automation_file(MINING_DICT, GENERATOR_DICT, FARMING_DICT)
    make_automation_file(RESEARCH_DICT, BUREAU_DICT)
    make_automation_file(MINING_HABITAT_DICT, GENERATOR_HABITAT_DICT, FORTRESS_HABITAT_DICT)
