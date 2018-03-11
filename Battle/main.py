from classes.game import Person, Bcolours
from classes.magic import Spell
from classes.inventory import Item
import random

# Create Black magic
fire = Spell("Fire", 10, 600, "black")
thunder = Spell("Thunder", 10, 600, "black")
blizzard = Spell("Blizzard", 10, 600, "black")
meteor = Spell("Meteor", 20, 1200, "black")
quake = Spell("Quake", 14, 800, "black")

# Create White Magic
cure = Spell("Cure", 12, 620, "white")
cura = Spell("Cura", 18, 1500, "white")
curaga = Spell("Curaga", 20, 3000, "white")

# Create some Items
potion = Item("Potion", "potion", "Heals 200 HP", 200)
hipotion = Item("Hi-Potion", "potion", "Heals 500 HP", 500)
superpotion = Item("Super Potion", "potion", "Heals 1000 HP", 1000)
elixer = Item("Elixer", "elixer", "Fully restores HP/MP of one party member", 9999)
megaelixer = Item("Mega Elixer", "elixer", "Fully restores party's HP/MP", 9999)

grenade = Item("Grenade", "attack", "Deals 500 damage", 500)

player_spells = [fire, thunder, blizzard, meteor, cure, cura]
enemy_spells1 = [fire, cure]
enemy_spells2 = [blizzard, cure]
enemy_spells3 = [curaga, meteor, thunder]
player_items = [{"item": potion, "quantity": 15}, {"item": hipotion, "quantity": 5},
                {"item": superpotion, "quantity": 5}, {"item": elixer, "quantity": 5},
                {"item": megaelixer, "quantity": 2}, {"item": grenade, "quantity": 5}]

# Instantiate People
player1 = Person("T-Wizzle ", 3260, 132, 300, 34, player_spells, player_items)
player2 = Person("C3-BPO   ", 4160, 188, 311, 34, player_spells, player_items)
player3 = Person("Lizard   ", 3089, 174, 288, 34, player_spells, player_items)

enemy1 = Person("Blood-Imp           ", 1000, 100, 450, 325, enemy_spells1, [])
enemy2 = Person("Zargoth-the-Terrible", 11200, 221, 615, 25, enemy_spells3, [])
enemy3 = Person("Ice-Imp             ", 800, 200, 250, 270, enemy_spells2, [])

players = [player1, player2, player3]
enemies = [enemy1, enemy2, enemy3]

running = True
i = 0

print(Bcolours.FAIL + Bcolours.BOLD + "AN ENEMY ATTACKS!" + Bcolours.ENDC)

while running:
    print("=================")

    print("\n")
    print(Bcolours.OKGREEN + Bcolours.BOLD + "Super Best Friends" + Bcolours.ENDC + "\n")
    print("NAME                       HP                                     MP")

    for player in players:
        player.get_stats()

    print("\n" + Bcolours.BOLD + Bcolours.FAIL + "The Forces of Evil" + Bcolours.ENDC)

    for enemy in enemies:
        enemy.get_enemy_stats()

    for player in players:
        player.choose_action()
        choice = input("    Choose action: ")
        index = int(choice) - 1

        if index == 0:
            dmg = player.generate_damage()
            enemy = player.choose_target(enemies)
            enemies[enemy].take_damage(dmg)
            print("You attacked " + enemies[enemy].name.replace(" ", "") + " for", dmg, "points of damage.")

            if enemies[enemy].get_hp() == 0:
                print(Bcolours.FAIL + enemies[enemy].name.replace(" ", "") +
                      " has been defeated in battle. 💀" + Bcolours.ENDC)
                del enemies[enemy]

        elif index == 1:
            player.choose_magic()
            magic_choice = int(input("Choose magic: ")) - 1

            if magic_choice == -1:
                continue

            spell = player.magic[magic_choice]
            magic_dmg = spell.generate_damage()

            current_mp = player.get_mp()

            if spell.cost > current_mp:
                print(Bcolours.FAIL + "\nNot enough MP\n" + Bcolours.ENDC)
                continue

            player.reduce_mp(spell.cost)

            if spell.type == "white":
                player.heal(magic_dmg)
                print(Bcolours.OKBLUE + "\n" + spell.name + " heals for", str(magic_dmg), "HP." + Bcolours.ENDC)
            elif spell.type == "black":
                enemy = player.choose_target(enemies)
                enemies[enemy].take_damage(magic_dmg)
                print(Bcolours.OKBLUE + "\n" + spell.name + " deals", str(magic_dmg), "points of damage to " +
                      enemies[enemy].name + Bcolours.ENDC)

                if enemies[enemy].get_hp() == 0:
                    print(Bcolours.FAIL + enemies[enemy].name.replace(" ", "") + " has been defeated in battle. 💀" +
                    Bcolours.ENDC)
                    del enemies[enemy]

        elif index == 2:
            player.choose_item()
            item_choice = int(input("Choose Item: ")) - 1

            if item_choice == -1:
                continue

            item = player.items[item_choice]["item"]

            if player.items[item_choice]["quantity"] == 0:
                print(Bcolours.FAIL + "\n" + "None left..." + Bcolours.ENDC)
                continue

            player.items[item_choice]["quantity"] -= 1

            if item.type == "potion":
                player.heal(item.prop)
                print(Bcolours.OKGREEN + "\n" + item.name + " heals for", str(item.prop), "HP" + Bcolours.ENDC)
            elif item.type == "elixer":

                if item.name == "Mega Elixer":
                    for i in players:
                        i.hp = i.maxhp
                        i.mp = i.maxmp
                else:
                    player.hp = player.maxhp
                    player.mp = player.maxmp
                print(Bcolours.OKGREEN + "\n" + item.name + " fully restores HP/MP" + Bcolours.ENDC)

            elif item.type == "attack":
                enemy = player.choose_target(enemies)
                enemies[enemy].take_damage(item.prop)
                enemy.take_damage(item.prop)

                print(Bcolours.FAIL + "\n" + item.name + " deals", str(item.prop), "points of damage to " +
                      enemies[enemy].name + Bcolours.ENDC)

                if enemies[enemy].get_hp() == 0:
                    print(Bcolours.FAIL + enemies[enemy].name.replace(" ", "") + " has been defeated in battle. 💀"
                    + Bcolours.ENDC)
                    del enemies[enemy]

# Check if battle is over
    defeated_enemies = 0
    defeated_players = 0

    for player in players:
        if player.get_hp() == 0:
            defeated_players += 1

    for enemy in enemies:
        if enemy.get_hp() == 0:
            defeated_enemies += 1
# Check if player won
    if defeated_enemies == 3:
        print(Bcolours.OKGREEN + "You win!" + Bcolours.ENDC)
        running = False
# Check if enemy won
    elif defeated_players == 3:
        print(Bcolours.FAIL + "Your enemies have defeated you!" + Bcolours.ENDC)
        running = False

# Enemy attack phase
    for enemy in enemies:
        enemy_choice = random.randrange(0, 2)

        if enemy_choice == 0:
            # Choose attack
            target = random.randrange(0, 3)
            enemy_dmg = enemy.generate_damage()

            players[target].take_damage(enemy_dmg)
            print(enemy.name.replace(" ", "") + " attacks " + players[target].name.replace(" ", "") + " for", enemy_dmg)

        elif enemy_choice == 1:
            spell, magic_dmg = enemy.choose_enemy_spell()
            enemy.reduce_mp(spell.cost)

            if spell.type == "white":
                enemy.heal(magic_dmg)
                print(Bcolours.OKBLUE + spell.name + " heals " + enemy.name + " for", str(magic_dmg),
                      "HP." + Bcolours.ENDC)
            elif spell.type == "black":

                target = random.randrange(0, 3)

                players[target].take_damage(magic_dmg)

                print(Bcolours.OKBLUE + "\n" + enemy.name.replace(" ", "") + "'s " + spell.name + " deals",
                      str(magic_dmg), "points of damage to " + players[target].name.replace(" ", "") + Bcolours.ENDC)

                if players[target].get_hp() == 0:
                    print(players[target].name.replace(" ", "") + " has died.")
                    del players[target]


    print("-----------------------")