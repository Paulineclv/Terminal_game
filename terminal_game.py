import random

print("Welcome to the Magic Dungeon!")
print("A perilous adventure awaits you...")

player_name = input("What's your name, brave adventurer?")

print(f"\nWelcome, {player_name}! Get ready to face terrifying creatures and survive the traps of the dungeon...")

player_hp = 20
enemies_defeated = 0

print("\nYour mission is to defeat 3 monsters to escape the dungeon alive!")
print("Let the adventure begin...\n")

while player_hp > 0 and enemies_defeated < 3:
    print(f"\nYou have {player_hp} HP.")
    print("What do you want to do ?")
    print("1. Attack the monster")
    print("2. Heal yourself")
    print("3. Try to run away")

    choice = input("> ")
    if choice == "1":
        enemy_hp = random.randint(5, 10)
        enemy_attack = random.randint(1, 4)
        player_attack = random.randint(3, 6)

        print(f"\nYou attack the monster and deal {player_attack} damage!")
        print(f'\nThe monster attacks you back and deals {enemy_attack} damage!')

        player_hp -= enemy_attack
        enemy_hp -= player_attack

        if enemy_hp <= 0:
            print("You defeated the monster!")
            enemies_defeated += 1
        else:
            print("The monster is still alive...")
    elif choice == "2":
        heal = random.randint(4, 8)
        enemy_attack = random.randint(1, 4)

        player_hp += heal
        player_hp -= enemy_attack

        print(f"\nYou heal yourself for {heal} HP")
        print(f"\nBut while you're healing, a monster attacks you for {enemy_attack} damage!")
    elif choice == "3":
        run_chance = random.randint(1, 2)

        if run_chance == 1:
            print("\nYou managed to escape safely")
        else:
            enemy_attack = random.randint(2, 5)
            player_hp -= enemy_attack
            print(f"\nYou failed to escape! The monster hits you for {enemy_attack} damage as you run away!")

if player_hp <= 0:
    print(f"\n{player_name}, you have fallen in the dungeon... Game Over.")
elif enemies_defeated >= 3:
    print(f"\nCongratulations, {player_name}! You defeated 3 monsters and escaped the Magic Dungeon!")