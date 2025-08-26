import json
from datapack_recipe_creator import get_recipes

# Minecraft version (1.16.5, 1.21.1, etc.)
# Set each time you want to generate for specific version
minecraft_version = "1.21.5"

# Dictionary for data pack format number based on Minecraft version
pack_format_values = {
    "1.21.1": 48,
    "1.21.5": 71
}

# Namespace variable for datapack
datapack_namespace = "bps_stairs_and_slabs"


# ****************************************************************************************************
# ITEM LISTS
# ****************************************************************************************************

# Master list of all items that need custom recipes
custom_recipe_items = {
    "wooden": [
        "acacia",
        "bamboo",
        "birch",
        "cherry",
        "crimson",
        "dark_oak",
        "jungle",
        "mangrove",
        "oak",
        "spruce",
        "warped"
    ],
    "non-wooden": [
        "andesite",
        "bamboo_mosaic",
        "blackstone",
        "brick",
        "cobblestone",
        "cobbled_deepslate",
        "cut_copper",
        "cut_red_sandstone",
        "cut_sandstone",
        "dark_prismarine",
        "deepslate_brick",
        "deepslate_tile",
        "diorite",
        "end_stone_brick",
        "exposed_cut_copper",
        "granite",
        "mossy_cobblestone",
        "mossy_stone_brick",
        "mud_brick",
        "nether_brick",
        "oxidized_cut_copper",
        "polished_andesite",
        "polished_blackstone",
        "polished_blackstone_brick",
        "polished_deepslate",
        "polished_diorite",
        "polished_granite",
        "polished_tuff",
        "prismarine",
        "prismarine_brick",
        "purpur",
        "quartz",
        "red_nether_brick",
        "red_sandstone",
        "sandstone",
        "smooth_quartz",
        "smooth_red_sandstone",
        "smooth_sandstone",
        "smooth_stone",
        "stone",
        "stone_brick",
        "tuff",
        "tuff_brick",
        "waxed_cut_copper",
        "waxed_exposed_cut_copper",
        "waxed_oxidized_cut_copper",
        "waxed_weathered_cut_copper",
        "weathered_cut_copper"
    ]
}

# Filter list for items with only slab recipes
slab_only_list = [
    "cut_red_sandstone",
    "cut_sandstone",
    "smooth_stone"
]

# List of items that need vanilla recipes overriden for datapack to work
minecraft_recipe_overrides = {
    "pressure_plate": {
        "wooden": [
            "acacia",
            "bamboo",
            "birch",
            "cherry",
            "crimson",
            "dark_oak",
            "jungle",
            "mangrove",
            "oak",
            "spruce",
            "warped"
        ],
        "non-wooden": [
            "polished_blackstone",
            "stone",
        ]
    }
}

# If using version 1.21.4+, then add blocks from "Garden Awakens" update
if pack_format_values[minecraft_version] >= 61:
    custom_recipe_items["non-wooden"].append("resin_brick")
    custom_recipe_items["wooden"].append("pale_oak")
    minecraft_recipe_overrides["pressure_plate"]["wooden"].append("pale_oak")


# Cycle through item types: wooden and non-wooden
for item_type, item_list in custom_recipe_items.items():
    # Cycle through each item you want custom recipes for: wood, stone, etc
    for item in item_list:
        # Dictionary to hold the item recipe types and their corresponding JSON data for recipe files
        recipes = get_recipes(
            item_type, item, pack_format_values, minecraft_version, slab_only_list
        )

        # **************************************************
        # Cycle through recipe types to create files
        for recipe_type, recipe in recipes.items():
            if item_type == "wooden":
                # If item is wooden then add Minecraft recipe group attribute to recipe
                recipe["group"] = f"wooden_{recipe_type.split('_')[0]}"

                # Set file name using wooden item name and recipe type
                if recipe_type[-5:] == "block":
                    # Change wording from "block" to "planks" for wooden items
                    recipe_file_name = item + '_' + recipe_type[:-5] + "planks"
                elif recipe_type[:5] == "block":
                    # Change wording from "block" to "planks" for wooden items
                    recipe_file_name = item + '_' + "planks" + recipe_type[5:]
                else:
                    recipe_file_name = item + '_' + recipe_type
            else:
                recipe["group"] = f"{item}_{recipe_type.split('_')[0]}"
                recipe_file_name = item + '_' + recipe_type

            # Set dictionary key order for resulting JSON data
            custom_order = ["type", "category",
                            "group", "pattern", "key", "result"]
            sorted_keys = sorted(recipe.keys(), key=lambda x: custom_order.index(
                x) if x in custom_order else len(custom_order))
            sorted_recipe = {key: recipe[key] for key in sorted_keys}

            # Write to new file/overwrite to existing file
            with open(f"./minecraft_versions/{minecraft_version}/data/{datapack_namespace}/recipe/{recipe_file_name}.json", 'w') as json_file:
                json.dump(sorted_recipe, json_file, indent=4)

            # **************************************************
            # Change vanilla recipe for stairs
            if recipe_type == "stairs_from_block":
                # Replace vanilla result from 4 to 8 stairs to match datapack
                sorted_recipe["pattern"] = ["#  ", "## ", "###"]
                sorted_recipe["result"]["count"] = 8
                with open(f"./minecraft_versions/{minecraft_version}/data/minecraft/recipe/{item}_stairs.json", 'w') as json_file:
                    json.dump(sorted_recipe, json_file, indent=4)

        # **************************************************
        # Other vanilla recipe overrides
        if item in minecraft_recipe_overrides["pressure_plate"]["wooden"] or item in minecraft_recipe_overrides["pressure_plate"]["non-wooden"]:
            # My best solution was to switch all vanilla pressure plate recipes to stone cutting, since pressure plates aren't as common to craft
            if pack_format_values[minecraft_version] == 48:
                # 1.21.1 formatting
                recipes["pressure_plate"] = {
                    "type": "minecraft:stonecutting",
                    "ingredient": {
                        "item": f"minecraft:{item}_planks" if item in minecraft_recipe_overrides["pressure_plate"]["wooden"] else f"minecraft:{item}"
                    },
                    "result": {
                        "id": f"minecraft:{item}_pressure_plate",
                        "count": 9
                    }
                }
            elif pack_format_values[minecraft_version] == 71:
                # 1.21.5 formatting
                recipes["pressure_plate"] = {
                    "type": "minecraft:stonecutting",
                    "ingredient": [
                        f"minecraft:{item}_planks" if item in minecraft_recipe_overrides[
                            "pressure_plate"]["wooden"] else f"minecraft:{item}"
                    ],
                    "result": {
                        "id": f"minecraft:{item}_pressure_plate",
                        "count": 9
                    }
                }

            # Write to new file/overwrite to existing file in Minecraft namespace
            with open(f"./minecraft_versions/{minecraft_version}/data/minecraft/recipe/{item}_pressure_plate.json", 'w') as json_file:
                json.dump(recipes["pressure_plate"], json_file, indent=4)

print("Finished")
