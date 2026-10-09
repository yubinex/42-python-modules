import sys


def main() -> None:
    print("=== Inventory System Analysis ===")

    inventory: dict[str, int] = {}

    for item in sys.argv[1:]:
        parts = item.split(":")
        if len(parts) != 2 or parts[0] == "":
            print(f"Error - invalid parameter '{item}'")
            continue
        item_name, quantity_text = parts
        if item_name in inventory:
            print(f"Redundant item '{item_name}' - discarding")
            continue
        try:
            quantity = int(quantity_text)
        except ValueError as e:
            print(f"Quantity error for '{item_name}': {e}")
        else:
            inventory[item_name] = quantity

    print(f"Got inventory: {inventory}")

    item_list = list(inventory.keys())
    print(f"Item list: {item_list}")

    total_quantity = sum(list(inventory.values()))
    print(f"Total quantity of the {len(item_list)} items: {total_quantity}")

    if len(item_list) > 0:
        for item_name in item_list:
            quantity = inventory[item_name]
            if total_quantity == 0:
                percentage = 0.0
            else:
                percentage = round((quantity / total_quantity) * 100, 1)
            print(f"Item {item_name} represents {percentage}%")

        max_item = item_list[0]
        min_item = item_list[0]
        for item_name in item_list:
            if inventory[item_name] > inventory[max_item]:
                max_item = item_name
            if inventory[item_name] < inventory[min_item]:
                min_item = item_name
        print(
            f"Item most abundant: {max_item} "
            f"with quantity {inventory[max_item]}"
        )
        print(
            f"Item least abundant: {min_item} "
            f"with quantity {inventory[min_item]}"
        )

    inventory.update({"magic_item": 1})
    print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    main()
