# 1 - créer une liste des pokémons, incluant une chance de spawn (0% - 100%) 
# 2 - créer une méthode spwan, qui, en fonction de la chance de spawn, fait spawn un pokémon (affiche son nom)
# 3 - faire spawn 10000 pokémons, calculer le % de chaque pokémon spawn
# 4 - comparer le % de spawn avec la chance de spawn du pokémon. Afficher pour chaque pokémon spawn, s'il y en a eu + ou - que la proba de spawn initiale
# 5 - Créer les pokeball (30%), superball (50%), hyperball (70%), masterball (100%). Mettre un % de chance d'attraper le pokemon pour chacune.
# 6 - Ajouter une "résistance" à chaque pokemon, entre 0 et 50%. La résistance est la diminution de la proba d'attraper les pokémons. Attention, la masterball de ne prend pas en compte la resistance.
# 7 - Mettre en place un inventaire des objets obtenus :
#       -> 1 inventaire pokemon
#       -> 1 inventaire pokeballs
# 8 - Ajouter des stats par pokémon (attaque / défense)
# 9 - Mettre en place les combats :
#       - ratio1 = attaque_pokemon_1 / defense_pokemon_1
#       - ratio2 = attaque_pokemon_2 / defense_pokemon_2
#       - gagnant = random de 0 à somme(ratio1, ratio2). (meme principe que % spawn)
# 10 - Mettre en place les pokedollars ($). Chaque combat gagné rapporte entre 1 et 2000 pokedollars
# 11 - Ajouter un shop, avec les prix suivants : 
#       -> pokeball : 200$
#       -> superball : 600$
#       -> hyperball : 1 200$
#       -> masterball : 50 000$
# 12 - Mettre en place le tout dans un programme en CLI, avec un menu : 
#       -> shop
#       -> spawn
#       -> inventaire objets
#       -> inventaire pokemon

import random, string, time, pypokedex

class Pokemon():
    max = 0

    def __init__(self, id):
        self.timeStart = time.time_ns()           
        self.pokemon = pypokedex.get(dex = id)
        self.spawnrate = random.randint(0,100)
        self.startSpawn = self.__class__.max
        self.__class__.max += self.spawnrate
        self.endSpawn = self.__class__.max
        self.catchrate = random.randint(0,50)

    def __repr__(self):
        return self.pokemon.name
    

if __name__ == "__main__" :
    sum = 0
    sample = 1000
    pokedex = 30
    test = {}
    result = {}
    catch = {}
    for i in range (1, pokedex):
        j = i
        test[i] = Pokemon(i)
        print(test[i].pokemon.name)
        sum += test[i].spawnrate
        result[test[i].pokemon.name] = 0
        test[j] = Pokemon(j)
        sum += test[j].spawnrate
        result[test[j].pokemon.name] = 0
    
    for i in test:
        print("le pokémon : ", test[i].pokemon.name, "  a une chance de spawn de : ", "{:.2f}".format(test[i].spawnrate/(test[i].max/100)), "%")

    for j in catch:
        print("le pokémon : ", test[j].pokemon.name, "  a une chance de capture de : ", "{:.2f}".format(test[j].catchrate/(test[i].max/100)), "%")

    for i in range(sample):
        spawn = random.randint(1, test[1].max)
        for i in test:
            if spawn >= test[i].startSpawn and spawn < test[i].endSpawn:
                result[test[i].pokemon.name] += 1
                break
    
    #for i in catch:


    for i in result:
        print("pokémon: ", i, "  quantité: ", result[i], "  pourcentage: ", "{:.2f}".format(result[i]/(sample/100)),"%", "  son taux de capture est de: ", )




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