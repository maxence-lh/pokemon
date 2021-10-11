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




