def get_recipes(namespace, item_type, item, pack_format_values, minecraft_version, slab_only_list) -> dict:
    item_recipes = {}

    # ****************************************************************************************************
    # 1.21.1 recipe syntax
    # ****************************************************************************************************
    if pack_format_values[minecraft_version] == 48:
        # **************************************************
        # Create slab from blocks
        item_recipes["slab_from_block"] = {
            "type": "minecraft:crafting_shaped",
            "category": "building",
            "pattern": [
                "##"
            ],
            "key": {
                "#": {
                    "item": f"{namespace}:{item}_planks" if item_type == "wooden" else f"{namespace}:{item}"
                }
            },
            "result": {
                "id": f"{namespace}:{item}_slab",
                "count": 4
            }
        }

        # Only add these recipes if item has stair variants
        if item not in slab_only_list:
            # **************************************************
            # Create slab from stairs (only if has stair recipe)
            item_recipes["slab_from_stairs"] = {
                "type": "minecraft:crafting_shaped",
                "category": "building",
                "pattern": [
                    "##"
                ],
                "key": {
                    "#": {
                        "item": f"{namespace}:{item}_stairs"
                    }
                },
                "result": {
                    "id": f"{namespace}:{item}_slab",
                    "count": 3
                }
            }

            # **************************************************
            # Create stairs from block (only if has stair recipe)
            item_recipes["stairs_from_block"] = {
                "type": "minecraft:crafting_shaped",
                "category": "building",
                "pattern": [
                    "# ",
                    "##"
                ],
                "key": {
                    "#": {
                        "item": f"{namespace}:{item}_planks" if item_type == "wooden" else f"{namespace}:{item}"
                    }
                },
                "result": {
                    "id": f"{namespace}:{item}_stairs",
                    "count": 4
                }
            }

            # **************************************************
            # Create stairs from slab (only if has stair recipe)
            item_recipes["stairs_from_slab"] = {
                "type": "minecraft:crafting_shaped",
                "category": "building",
                "pattern": [
                    "# ",
                    "##"
                ],
                "key": {
                    "#": {
                        "item": f"{namespace}:{item}_slab"
                    }
                },
                "result": {
                    "id": f"{namespace}:{item}_stairs",
                    "count": 2
                }
            }

            # **************************************************
            # Create block from stairs (only if has stair recipe)
            item_recipes["block_from_stairs"] = {
                "type": "minecraft:crafting_shaped",
                "category": "building",
                "pattern": [
                    "##",
                    "##"
                ],
                "key": {
                    "#": {
                        "item": f"{namespace}:{item}_stairs"
                    }
                },
                "result": {
                    "id": f"{namespace}:{item}_planks" if item_type == "wooden" else f"{namespace}:{item}",
                    "count": 3
                }
            }

        # **************************************************
        # Create block from slab
        item_recipes["block_from_slab"] = {
            "type": "minecraft:crafting_shaped",
            "category": "building",
            "pattern": [
                "##",
                "##"
            ],
            "key": {
                "#": {
                    "item": f"{namespace}:{item}_slab"
                }
            },
            "result": {
                "id": f"{namespace}:{item}_planks" if item_type == "wooden" else f"{namespace}:{item}",
                "count": 2
            }
        }

        # **************************************************
        # Special conditions for purpur and quartz blocks, since all variants make slabs/stairs
        if item in ["purpur", "quartz"]:
            # Make purpur/quarts stairs craftable from blocks or pillars
            item_recipes["stairs_from_block"]["key"]["#"] = [
                {"item": f"minecraft:{item}_block"},
                {"item": f"minecraft:{item}_pillar"}
            ]

            # Make purpur/quarts slabs craftable from blocks or pillars
            item_recipes["slab_from_block"]["key"]["#"] = [
                {"item": f"minecraft:{item}_block"},
                {"item": f"minecraft:{item}_pillar"}
            ]

            if item == "quartz":
                # Add chiseled variant for quartz recipes
                item_recipes["stairs_from_block"]["key"]["#"].append(
                    {"item": "minecraft:chiseled_quartz_block"})
                item_recipes["slab_from_block"]["key"]["#"].append(
                    {"item": "minecraft:chiseled_quartz_block"})

            # Append "_block" keyword to recipe result for purpur and quartz items
            item_recipes["block_from_stairs"]["result"]["id"] = f"minecraft:{item}_block"
            item_recipes["block_from_slab"]["result"]["id"] = f"minecraft:{item}_block"

        # **************************************************
        # Append "s" to brick and tile items
        if item[-5:] == "brick" or item[-4:] == "tile":
            item_recipes["stairs_from_block"]["key"]["#"]["item"] += "s"
            item_recipes["slab_from_block"]["key"]["#"]["item"] += "s"
            item_recipes["block_from_stairs"]["result"]["id"] += "s"
            item_recipes["block_from_slab"]["result"]["id"] += "s"

    # ****************************************************************************************************
    # 1.21.5 recipe syntax
    # ****************************************************************************************************
    elif pack_format_values[minecraft_version] == 71:
        # **************************************************
        # Create slab from blocks
        item_recipes["slab_from_block"] = {
            "type": "minecraft:crafting_shaped",
            "category": "building",
            "pattern": [
                "##"
            ],
            "key": {
                "#": [
                    f"{namespace}:{item}_planks" if item_type == "wooden" else f"{namespace}:{item}"
                ]
            },
            "result": {
                "id": f"{namespace}:{item}_slab",
                "count": 4
            }
        }

        # Only add these recipes if item has stair variants
        if item not in slab_only_list:
            # **************************************************
            # Create slab from stairs (only if has stair recipe)
            item_recipes["slab_from_stairs"] = {
                "type": "minecraft:crafting_shaped",
                "category": "building",
                "pattern": [
                    "##"
                ],
                "key": {
                    "#": [
                        f"{namespace}:{item}_stairs"
                    ]
                },
                "result": {
                    "id": f"{namespace}:{item}_slab",
                    "count": 3
                }
            }

            # **************************************************
            # Create stairs from block (only if has stair recipe)
            item_recipes["stairs_from_block"] = {
                "type": "minecraft:crafting_shaped",
                "category": "building",
                "pattern": [
                    "# ",
                    "##"
                ],
                "key": {
                    "#": [
                        f"{namespace}:{item}_planks" if item_type == "wooden" else f"{namespace}:{item}"
                    ]
                },
                "result": {
                    "id": f"{namespace}:{item}_stairs",
                    "count": 4
                }
            }

            # **************************************************
            # Create stairs from slab (only if has stair recipe)
            item_recipes["stairs_from_slab"] = {
                "type": "minecraft:crafting_shaped",
                "category": "building",
                "pattern": [
                    "# ",
                    "##"
                ],
                "key": {
                    "#": [
                        f"{namespace}:{item}_slab"
                    ]
                },
                "result": {
                    "id": f"{namespace}:{item}_stairs",
                    "count": 2
                }
            }

            # **************************************************
            # Create block from stairs (only if has stair recipe)
            item_recipes["block_from_stairs"] = {
                "type": "minecraft:crafting_shaped",
                "category": "building",
                "pattern": [
                    "##",
                    "##"
                ],
                "key": {
                    "#": [
                        f"{namespace}:{item}_stairs"
                    ]
                },
                "result": {
                    "id": f"{namespace}:{item}_planks" if item_type == "wooden" else f"{namespace}:{item}",
                    "count": 3
                }
            }

        # **************************************************
        # Create block from slab
        item_recipes["block_from_slab"] = {
            "type": "minecraft:crafting_shaped",
            "category": "building",
            "pattern": [
                "##",
                "##"
            ],
            "key": {
                "#": [
                    f"{namespace}:{item}_slab"
                ]
            },
            "result": {
                "id": f"{namespace}:{item}_planks" if item_type == "wooden" else f"{namespace}:{item}",
                "count": 2
            }
        }

        # **************************************************
        # Special conditions for purpur and quartz blocks, since all variants make slabs/stairs
        if item in ["purpur", "quartz"]:
            # Make purpur/quarts stairs craftable from blocks or pillars
            item_recipes["stairs_from_block"]["key"]["#"] = [
                f"minecraft:{item}_block",
                f"minecraft:{item}_pillar"
            ]

            # Make purpur/quarts slabs craftable from blocks or pillars
            item_recipes["slab_from_block"]["key"]["#"] = [
                f"minecraft:{item}_block",
                f"minecraft:{item}_pillar"
            ]

            if item == "quartz":
                # Add chiseled variant for quartz recipes
                item_recipes["stairs_from_block"]["key"]["#"].append(
                    "minecraft:chiseled_quartz_block")
                item_recipes["slab_from_block"]["key"]["#"].append(
                    "minecraft:chiseled_quartz_block")

            # Append "_block" keyword to recipe result for purpur and quartz items
            item_recipes["block_from_stairs"]["result"]["id"] = f"minecraft:{item}_block"
            item_recipes["block_from_slab"]["result"]["id"] = f"minecraft:{item}_block"

        # **************************************************
        # Append "s" to brick and tile items
        if item[-5:] == "brick" or item[-4:] == "tile":
            item_recipes["stairs_from_block"]["key"]["#"][0] += "s"
            item_recipes["slab_from_block"]["key"]["#"][0] += "s"
            item_recipes["block_from_stairs"]["result"]["id"] += "s"
            item_recipes["block_from_slab"]["result"]["id"] += "s"

    # Return dictionary
    return item_recipes
