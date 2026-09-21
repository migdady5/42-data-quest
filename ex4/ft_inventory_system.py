import sys


def main() -> None:
    print("=== Inventory System Analysis ===")

    inventory: dict[str, int] = {}

    i = 1
    while i < len(sys.argv):
        arg = sys.argv[i]
        i = i + 1

        if ":" not in arg:
            print(f"Error - invalid parameter '{arg}'")
            continue

        parts = arg.split(":")

        if len(parts) != 2:
            print(f"Error - invalid parameter '{arg}'")
            continue

        item = parts[0]
        quantity_text = parts[1]

        if item == "" or quantity_text == "":
            print(f"Error - invalid parameter '{arg}'")
            continue

        if item in inventory.keys():
            print(f"Redundant item '{item}' - discarding")
            continue

        try:
            quantity = int(quantity_text)
        except ValueError as error:
            print(f"Quantity error for '{item}': {error}")
            continue

        if quantity <= 0:
            print(f"Quantity error for '{item}': quantity must be positive")
            continue

        inventory.update({item: quantity})

    print("Got inventory:", inventory)

    items = list(inventory.keys())
    print("Item list:", items)

    total = sum(inventory.values())
    print("Total quantity of the", len(items), "items:", total)

    if total > 0:
        for item in inventory.keys():
            percentage = round(inventory[item] / total * 100, 1)
            print(f"Item {item} represents {percentage}%")

        first_item = items[0]
        most_item = first_item
        least_item = first_item

        for item in inventory.keys():
            if inventory[item] > inventory[most_item]:
                most_item = item

            if inventory[item] < inventory[least_item]:
                least_item = item

        print(
            "Item most abundant:",
            most_item,
            "with quantity",
            inventory[most_item],
        )

        print(
            "Item least abundant:",
            least_item,
            "with quantity",
            inventory[least_item],
        )

    inventory.update({"magic_item": 1})
    print("Updated inventory:", inventory)


if __name__ == "__main__":
    main()
