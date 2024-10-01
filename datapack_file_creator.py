import json

# Namespace variable for datapack
datapack_namespace = "bps_stairs_and_slabs"

# Master list of all items that need custom recipes
custom_recipe_items = {
    "wooden": [
        'acacia',
        'bamboo',
        'birch',
        'cherry',
        'crimson',
        'dark_oak',
        'jungle',
        'mangrove',
        'oak',
        'spruce',
        'warped'
    ],
    "non-wooden": [
        'andesite',
        'bamboo_mosaic',
        'blackstone',
        'brick',
        'cobblestone',
        'cobbled_deepslate',
        'cut_copper',
        'cut_red_sandstone',
        'cut_sandstone',
        'dark_prismarine',
        'deepslate_brick',
        'deepslate_tile',
        'diorite',
        'end_stone_brick',
        'exposed_cut_copper',
        'granite',
        'mossy_cobblestone',
        'mossy_stone_brick',
        'mud_brick',
        'nether_brick',
        'oxidized_cut_copper',
        'polished_andesite',
        'polished_blackstone',
        'polished_blackstone_brick',
        'polished_deepslate',
        'polished_diorite',
        'polished_granite',
        'polished_tuff',
        'prismarine',
        'prismarine_brick',
        'purpur',
        'quartz',
        'red_nether_brick',
        'red_sandstone',
        'sandstone',
        'smooth_quartz',
        'smooth_red_sandstone',
        'smooth_sandstone',
        'smooth_stone',
        'stone',
        'stone_brick',
        'tuff',
        'tuff_brick',
        'waxed_cut_copper',
        'waxed_exposed_cut_copper',
        'waxed_oxidized_cut_copper',
        'waxed_weathered_cut_copper',
        'weathered_cut_copper'
    ]
}

# Filter list for items with only slab recipes
slab_only_list = [
    'cut_red_sandstone',
    'cut_sandstone',
    'smooth_stone'
]

# List of items that need vanilla recipes overriden for datapack to work
minecraft_recipe_overrides = {
    "pressure_plate" : {
        "wooden": [
            'acacia',
            'bamboo',
            'birch',
            'cherry',
            'crimson',
            'dark_oak',
            'jungle',
            'mangrove',
            'oak',
            'spruce',
            'warped'
        ],
        "non-wooden": [
            'polished_blackstone',
            'stone',
        ]
    }
}

# TODO: delete this later
test_list = {
    "wooden": ['acacia'],
    "non-wooden": [
        'brick',
        'deepslate_tile',
        "polished_blackstone",
        "purpur",
        "quartz",
        "smooth_stone",
        'cut_copper',
        'waxed_exposed_cut_copper',
        'waxed_oxidized_cut_copper',
        'waxed_weathered_cut_copper',
        'weathered_cut_copper'
    ]
}


# Cycle through item types: wooden and non-wooden
for item_type, item_list in custom_recipe_items.items(): # TODO: change to custom_recipe_items | test_list
    # Cycle through each item you want custom recipes for: wood, stone, etc
    for item in item_list:
        # Dictionary to hold the item recipe types and their corresponding JSON data for recipe files
        recipe_types = {}

        # **************************************************
        # Create slab from blocks
        recipe_types["slab_from_block"] = {
            "type": "minecraft:crafting_shaped",
            "category": "building",
            "pattern": [
                "##"
            ],
            "key": {
                "#": {
                    "item": f"minecraft:{item}_planks" if item_type == "wooden" else f"minecraft:{item}"
                }
            },
            "result": {
                "id": f"minecraft:{item}_slab",
                "count": 4
            }
        }

        # Only add these recipes if item has stair variants
        if item not in slab_only_list:
            # **************************************************
            # Create slab from stairs (only if has stair recipe)
            recipe_types["slab_from_stairs"] = {
                "type": "minecraft:crafting_shaped",
                "category": "building",
                "pattern": [
                    "##"
                ],
                "key": {
                    "#": {
                        "item": f"minecraft:{item}_stairs"
                    }
                },
                "result": {
                    "id": f"minecraft:{item}_slab",
                    "count": 3
                }
            }

            # **************************************************
            # Create stairs from block (only if has stair recipe)
            recipe_types["stairs_from_block"] = {
                "type": "minecraft:crafting_shaped",
                "category": "building",
                "pattern": [
                    "# ",
                    "##"
                ],
                "key": {
                    "#": {
                        "item": f"minecraft:{item}_planks" if item_type == "wooden" else f"minecraft:{item}"
                    }
                },
                "result": {
                    "id": f"minecraft:{item}_stairs",
                    "count": 4
                }
            }

            # **************************************************
            # Create stairs from slab (only if has stair recipe)
            recipe_types["stairs_from_slab"] = {
                "type": "minecraft:crafting_shaped",
                "category": "building",
                "pattern": [
                    "# ",
                    "##"
                ],
                "key": {
                    "#": {
                        "item": f"minecraft:{item}_slab"
                    }
                },
                "result": {
                    "id": f"minecraft:{item}_stairs",
                    "count": 2
                }
            }

            # **************************************************
            # Create block from stairs (only if has stair recipe)
            recipe_types["block_from_stairs"] = {
                "type": "minecraft:crafting_shaped",
                "category": "building",
                "pattern": [
                    "##",
                    "##"
                ],
                "key": {
                    "#": {
                        "item": f"minecraft:{item}_stairs"
                    }
                },
                "result": {
                    "id": f"minecraft:{item}_planks" if item_type == "wooden" else f"minecraft:{item}",
                    "count": 3
                }
            }

        # **************************************************
        # Create block from slab
        recipe_types["block_from_slab"] = {
            "type": "minecraft:crafting_shaped",
            "category": "building",
            "pattern": [
                "##",
                "##"
            ],
            "key": {
                "#": {
                    "item": f"minecraft:{item}_slab"
                }
            },
            "result": {
                "id": f"minecraft:{item}_planks" if item_type == "wooden" else f"minecraft:{item}",
                "count": 2
            }
        }

        # **************************************************
        # Create block from wall
        recipe_types["block_from_slab"] = {
            "type": "minecraft:crafting_shaped",
            "category": "building",
            "pattern": [
                "##",
                "##"
            ],
            "key": {
                "#": {
                    "item": f"minecraft:{item}_slab"
                }
            },
            "result": {
                "id": f"minecraft:{item}_planks" if item_type == "wooden" else f"minecraft:{item}",
                "count": 2
            }
        }

        # **************************************************
        # Create block from slab
        recipe_types["block_from_slab"] = {
            "type": "minecraft:crafting_shaped",
            "category": "building",
            "pattern": [
                "##",
                "##"
            ],
            "key": {
                "#": {
                    "item": f"minecraft:{item}_slab"
                }
            },
            "result": {
                "id": f"minecraft:{item}_planks" if item_type == "wooden" else f"minecraft:{item}",
                "count": 2
            }
        }

        # **************************************************
        # Special conditions for purpur and quartz blocks, since all variants make slabs/stairs
        if item in ["purpur", "quartz"]:
            # Make purpur/quarts stairs craftable from blocks or pillars
            recipe_types["stairs_from_block"]["key"]["#"] = [
                {"item": f"minecraft:{item}_block"},
                {"item": f"minecraft:{item}_pillar"}
            ]

            # Make purpur/quarts slabs craftable from blocks or pillars
            recipe_types["slab_from_block"]["key"]["#"] = [
                {"item": f"minecraft:{item}_block"},
                {"item": f"minecraft:{item}_pillar"}
            ]

            if item == "quartz":
                # Add chiseled variant for quartz recipes
                recipe_types["stairs_from_block"]["key"]["#"].append({"item": "minecraft:chiseled_quartz_block"})
                recipe_types["slab_from_block"]["key"]["#"].append({"item": "minecraft:chiseled_quartz_block"})

            # Append "_block" keyword to recipe result for purpur and quartz items
            recipe_types["block_from_stairs"]["result"]["id"] = f"minecraft:{item}_block"
            recipe_types["block_from_slab"]["result"]["id"] = f"minecraft:{item}_block"

        # **************************************************
        # Append "s" to brick and tile items
        if item[-5:] == "brick" or item[-4:] == "tile":
            recipe_types["stairs_from_block"]["key"]["#"]["item"] += "s"
            recipe_types["slab_from_block"]["key"]["#"]["item"] += "s"
            recipe_types["block_from_stairs"]["result"]["id"] += "s"
            recipe_types["block_from_slab"]["result"]["id"] += "s"
        
        # **************************************************
        # Cycle through recipe types to create files
        for recipe_type, recipe in recipe_types.items():
            if item_type == "wooden":
                # If item is wooden then add Minecraft recipe group attribute to recipe
                recipe["group"] = f"wooden_{recipe_type.split('_')[0]}"
                
                # Set file name using wooden item name and recipe type
                if recipe_type[-5:] == "block":
                    # Change wording from "block" to "planks" for wooden items
                    recipe_file_name = item + "_" + recipe_type[:-5] + "planks"
                elif recipe_type[:5] == "block":
                    # Change wording from "block" to "planks" for wooden items
                    recipe_file_name = item + "_" + "planks" + recipe_type[5:]
                else:
                    recipe_file_name = item + "_" + recipe_type
            else:
                recipe_file_name = item + "_" + recipe_type
            
            # Set dictionary key order for resulting JSON data
            custom_order = ["type", "category", "group", "pattern", "key", "result"]
            sorted_keys = sorted(recipe.keys(), key=lambda x: custom_order.index(x) if x in custom_order else len(custom_order))
            sorted_recipe = {key: recipe[key] for key in sorted_keys}
            
            # Write to new file/overwrite to existing file
            with open(f"./data/{datapack_namespace}/recipe/{recipe_file_name}.json", 'w') as json_file:
                json.dump(sorted_recipe, json_file, indent=4)

            # **************************************************
            # Change vanilla recipe for stairs
            if recipe_type == "stairs_from_block":
                # Replace vanilla result from 4 to 8 stairs to match datapack
                sorted_recipe["pattern"] = ["#  ", "## ", "###"]
                sorted_recipe["result"]["count"] = 8
                with open(f"./data/minecraft/recipe/{item}_stairs.json", 'w') as json_file:
                    json.dump(sorted_recipe, json_file, indent=4)

        # **************************************************
        # Other vanilla recipe overrides
        if item in minecraft_recipe_overrides["pressure_plate"]["wooden"] or item in minecraft_recipe_overrides["pressure_plate"]["non-wooden"]:
            # My best solution was to switch all vanilla pressure plate recipes to stone cutting, since pressure plates aren't as common to craft
            recipe_types["pressure_plate"] = {
                "type": "minecraft:stonecutting",
                "ingredient": {
                    "item": f"minecraft:{item}_planks" if item in minecraft_recipe_overrides["pressure_plate"]["wooden"] else f"minecraft:{item}"
                },
                "result": {
                    "id": f"minecraft:{item}_pressure_plate",
                    "count": 9
                }
            }

            # Write to new file/overwrite to existing file in Minecraft namespace
            with open(f"./data/minecraft/recipe/{item}_pressure_plate.json", 'w') as json_file:
                json.dump(recipe_types["pressure_plate"], json_file, indent=4)
