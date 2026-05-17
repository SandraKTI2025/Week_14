from character import Dog, Cat
from file_utils import get_random_from_file

dog_name = get_random_from_file(r"data/dogs.txt")
dog_weapon = get_random_from_file(r"data/weapons.txt")

cat_name = get_random_from_file(r"data/cats.txt")
cat_weapon = get_random_from_file(r"data/weapons.txt")

dog = Dog(dog_name, dog_weapon)
cat = Cat(cat_name, cat_weapon)

print("=== BATTLE Begins ===")

print(f"Dog: {dog.name} | HP: {dog.hp} | Weapon: {dog.weapon}")
print(f"Cat: {cat.name} | HP: {cat.hp} | Weapon: {cat.weapon}")

round_number = 1

while dog.is_alive() and cat.is_alive():
    print(f"--- Round {round_number} ---")

    dog.attack(cat)

    if not cat.is_alive():
        break

    cat.attack(dog)

    round_number += 1

print("=== BATTLE ENDS ===")

if dog.is_alive():
    print("Dog wins!")
else:
    print("Cat wins!")
