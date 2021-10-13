import random

# ["Name", minSpawn, maxSpawn, %Spawn, nbSpawn, attack, defense]
pokemons = [
    ["Bulbasaur", 0, 60, 0, 0, 49, 49], ["Charmander", 61, 121, 0, 0, 52, 43], ["Squirtle", 122, 182, 0, 0, 48, 65], ["Caterpie", 183, 263, 0, 0, 30, 35], 
    ["Weedle", 264, 344, 0, 0, 35, 30], ["Pidgey", 345, 425, 0, 0, 45, 40], ["Rattata", 426, 506, 0, 0, 56, 35], ["Spearow", 507, 587, 0, 0, 60, 30], 
    ["Ekans", 588, 658, 0, 0, 60, 44], ["Pikachu", 659, 719, 0, 0, 55, 40], ["Sandshrew", 720, 770, 0, 0, 75, 85], ["Nidoran ♀️", 771, 821, 0, 0, 47, 52], 
    ["Nidoran ♂️", 822, 872, 0, 0, 57, 40], ["Clefairy", 873, 923, 0, 0, 45, 48], ["Vulpix", 924, 974, 0, 0, 41, 40], ["Jigglypuff", 975, 1025, 0, 0, 45, 20], 
    ["Zubat", 1026, 1076, 0, 0, 45, 35], ["Golbat", 1077, 1127, 0, 0, 80, 70], ["Oddish", 1128, 1178, 0, 0, 50, 55], ["Paras", 1179, 1229, 0, 0, 70, 55], 
    ["Venonat", 1230, 1280, 0, 0, 55, 50], ["Diglett", 1281, 1351, 0, 0, 55, 25], ["Meowth", 1352, 1412, 0, 0, 45, 35], ["Psyduck", 1413, 1483, 0, 0, 52, 48], 
    ["Mankey", 1484, 1544, 0, 0, 80, 35], ["Growlithe", 1545, 1605, 0, 0, 70, 45], ["Poliwag", 1606, 1666, 0, 0, 50, 40], ["Abra", 1667, 1727, 0, 0, 20, 15], 
    ["Machop", 1728, 1788, 0, 0, 80, 50], ["Bellsprout", 1789, 1849, 0, 0, 75, 35], ["Tentacool", 1850, 1910, 0, 0, 40, 35], ["Geodude", 1911, 1971, 0, 0, 80, 100], 
    ["Ponyta", 1972, 2032, 0, 0, 85, 55], ["Slowpoke", 2033, 2093, 0, 0, 65, 65], ["Magnemite", 2094, 2154, 0, 0, 35, 70], ["Doduo", 2155, 2215, 0, 0, 85, 45], 
    ["Seel", 2216, 2276, 0, 0, 45, 55], ["Grimer", 2277, 2337, 0, 0, 80, 50], ["Shellder", 2338, 2398, 0, 0, 65, 100], ["Gastly", 2399, 2459, 0, 0, 35, 30], 
    ["Onix", 2460, 2500, 0, 0, 45, 160], ["Drowzee", 2501, 2561, 0, 0, 48, 45], ["Krabby", 2561, 2621, 0, 0, 105, 90], ["Voltorb", 2622, 2682, 0, 0, 30, 50], 
    ["Exeggcute", 2683, 2733, 0, 0, 40, 80], ["Cubone", 2734, 2784, 0, 0, 50, 80], ["Lickitung", 2785, 2845, 0, 0, 55, 75], ["Koffing", 2846, 2906, 0, 0, 65, 95], 
    ["Rhyhorn", 2907, 2967, 0, 0, 85, 95], ["Chansey", 2968, 3028, 0, 0, 5, 5], ["Tangela", 3029, 3089, 0, 0, 55, 115], ["Kangaskhan", 3090, 3140, 0, 0, 95, 80], 
    ["Horsea", 3141, 3201, 0, 0, 40, 70], ["Goldeen", 3202, 3252, 0, 0, 67, 60], ["Seaking", 3253, 3303, 0, 0, 92, 65], ["Staryu", 3304, 3354, 0, 0, 45, 55], 
    ["Mr. Mime", 3355, 3405, 0, 0, 45, 65], ["Scyther", 3406, 3446, 0, 0, 110, 80], ["Jynx", 3447, 3497, 0, 0, 50, 35], ["Electabuzz", 3498, 3558, 0, 0, 83, 57], 
    ["Magmar", 3559, 3619, 0, 0, 95, 57], ["Pinsir", 3620, 3680, 0, 0, 125, 100], ["Tauros", 3681, 3721, 0, 0, 100, 95], ["Magikarp", 3722, 3752, 0, 0, 10, 55], 
    ["Gyarados", 3753, 3773, 0, 0, 125, 79], ["Lapras", 3774, 3794, 0, 0, 85, 80], ["Ditto", 3795, 3845, 0, 0, 48, 48], ["Eevee", 3846, 3926, 0, 0, 55, 50], 
    ["Porygon", 3927, 3977, 0, 0, 60, 70], ["Omanyte", 3978, 4038, 0, 0, 40, 100], ["Kabuto", 4039, 4099, 0, 0, 80, 90], ["Aerodactyl", 4100, 4140, 0, 0, 105, 65], 
    ["Snorlax", 4141, 4181, 0, 0, 110, 65], ["Articuno", 4182, 4192, 0, 0, 85, 100], ["Zapdos", 4193, 4203, 0, 0, 90, 85], ["Moltres", 4204, 4214, 0, 0, 100, 90], 
    ["Dratini", 4215, 4245, 0, 0, 64, 45], ["Dragonair", 4246, 4276, 0, 0, 84, 65], ["Dragonite", 4277, 4297, 0, 0, 134, 95], ["Mewtwo", 4298, 4308, 0, 0, 110, 90], 
    ["Mew", 4309, 4319, 0, 0, 100, 100], ["Vaporeon", 4320, 4380, 0, 0, 65, 60], ["Jolteon", 4381, 4441, 0, 0, 65, 60], ["Pyroli", 4442, 4502, 0, 0, 130, 60], 
    ["Espeon", 4503, 4563, 0, 0, 65, 60], ["Umbreon", 4564, 4624, 0, 0, 65, 110], ["Togepi", 4625, 4695, 0, 0, 20, 65], ["Scizor", 4696, 4736, 0, 0, 130, 100], 
    ["Porygon2", 4737, 4787, 0, 0, 80, 90], ["Raikou", 4788, 4808, 0, 0, 85, 75], ["Entei", 4809, 4829, 0, 0, 115, 85], ["Suicune", 4830, 4850, 0, 0, 75, 115], 
    ["Larvitar", 4851, 4881, 0, 0, 64, 50], ["Pupitar", 4882, 4912, 0, 0, 84, 70], ["Tyranitar", 4913, 4933, 0, 0, 134, 110], ["Lugia", 4934, 4944, 0, 0, 90, 130], 
    ["Ho-Oh", 4945, 4955, 0, 0, 130, 90], ["Celebi", 4956, 4976, 0, 0, 100, 100], ["Latios", 4977, 5007, 0, 0, 90, 80], ["Latias", 5008, 5038, 0, 0, 80, 90]
]
resistance = 0
inventorypoke = []
inventoryball = ["pokeball",random.randint(0,30),"superball",random.randint(0,30),"hyperball",random.randint(0,30),"masterball",random.randint(0,30)]
inventorydoll = 0
print("wanna play ?","\n","0: no || 1: yes")
play = input()

def game():
    global play
    while play != "0":
        spawn()
    else:
        play = "0"

def spawn():
    total_range = 0
    global resistance
    global pokemon_spawn
    global pokemon_spawn_stats
    for i in range (0, len(pokemons)):
        total_range += pokemons[i][2] - pokemons[i][1]
    random_pokemon = (random.randint(0, total_range))
    for i in range (0, len(pokemons)-1):
        if random_pokemon >= pokemons[i][1] and random_pokemon <= pokemons[i][2]:
            pokemon_spawn = pokemons[i][0]
            pokemon_spawn_stats = pokemons[i]
            print("\n",pokemon_spawn, end=" ")
            resistance = random.randint(0,50)
            print (resistance,"%")
    menu()

def menu():
    global play
    print("\n"," 0:exit || 1:catching || 2:attack || 3:run || 4:inventory || 5:shop","\n")
    menu = input()
    if menu == "0":
        play="0"
        game()
    elif menu=="1":
        catch()
    elif menu=="2":
        attack()
    elif menu=="3":
        print("you were too scared, you ran away")
    elif menu=="4":
        inventory()
    elif menu=="5":
        shop()
    else: menu()

def catch():
    global pokemon_spawn
    ball = 0
    print("\n","1:pokeball || 2:superball || 3:hyperball || 4:masterball", "\n")
    ball = input()
    print("\n")
    if ball=="1":
        if inventoryball[1] > 0:
            if random.randint(0,100) <= (30/100)/(resistance/100) :
                print("pokemon catch !")
                inventorypoke.append(pokemon_spawn)
                inventoryball[1] = inventoryball[1]-1
            else:
                inventoryball[1] = inventoryball[1]-1
                print("fail")
        else:
            print("not enought balls")
            catch()
    elif ball=="2":
        if inventoryball[3] > 0:
            if random.randint(0,100) <= (50/100)/(resistance/100) :
                print("pokemon catch !")
                inventorypoke.append(pokemon_spawn)
                inventoryball[3] = inventoryball[3]-1
            else:
                inventoryball[3] = inventoryball[3]-1
                print("fail")
        else:
            print("not enought balls")
            catch()
    elif ball=="3":
        if inventoryball[5] > 0:
            if random.randint(0,100) <= (70/100)/(resistance/100) :
                print("pokemon catch !")
                inventorypoke.append(pokemon_spawn)
                inventoryball[5] = inventoryball[5]-1
            else:
                inventoryball[5] = inventoryball[5]-1
                print("fail")
        else:
            print("not enought balls")
            catch()
    elif ball=="4":
        if inventoryball[7] > 0:
            print("pokemon catch !")
            inventorypoke.append(pokemon_spawn)
            inventoryball[7] = inventoryball[7]-1
        else:
            print("not enought balls")
            catch()
    else:
        catch()

def inventory():
    print(inventorypoke)
    print("\n",inventoryball[0],":",inventoryball[1],"\n",inventoryball[2],":",inventoryball[3],"\n",inventoryball[4],":",inventoryball[5],"\n",inventoryball[6],":",inventoryball[7],"\n")
    print(inventorydoll, "pokedollars")
    menu()

def attack():
    global pokemon_spawn_stats
    print(inventorypoke)
    print("select your pokemon")
    pokemon1 = input()
    print(pokemon1)
    print(pokemon_spawn[5])

def shop():
    global inventorydoll
    print("1:buy || 2:return to menu")
    action = input()
    if action == "1":
        print("1:pokeball 200 || 2:superball 600 || 3:hyperball 1200 || 4:masterball 50000")
        choice = input()
        print("how many ?")
        quantity = int(input())
        if choice == "1":
            if inventorydoll - (200*quantity) > 0:
                inventorydoll -= (200*quantity)
        elif choice == "2":
            if inventorydoll - (600*quantity) > 0:
                inventorydoll -= (600*quantity)
        elif choice == "3":
            if inventorydoll - (1200*quantity) > 0:
                inventorydoll -= (1200*quantity)
        elif choice == "4":
            if inventorydoll - (50000*quantity) > 0:
                inventorydoll -= (50000*quantity)
        else:
            shop()
    else:
        menu()
    print(inventorydoll)



game()