# pokemon

1 - créer une liste des pokémons, incluant une chance de spawn (0% - 100%) 
2 - créer une méthode spwan, qui, en fonction de la chance de spawn, fait spawn un pokémon (affiche son nom)
3 - faire spawn 10000 pokémons, calculer le % de chaque pokémon spawn
4 - comparer le % de spawn avec la chance de spawn du pokémon. Afficher pour chaque pokémon spawn, s'il y en a eu + ou - que la proba de spawn initiale
5 - Créer les pokeball (30%), superball (50%), hyperball (70%), masterball (100%). Mettre un % de chance d'attraper le pokemon pour chacune.
6 - Ajouter une "résistance" à chaque pokemon, entre 0 et 50%. La résistance est la diminution de la proba d'attraper les pokémons. Attention, la masterball de ne prend pas en compte la resistance.
7 - Mettre en place un inventaire des objets obtenus :
      -> 1 inventaire pokemon
      -> 1 inventaire pokeballs
8 - Ajouter des stats par pokémon (attaque / défense)
9 - Mettre en place les combats :
      - ratio1 = attaque_pokemon_1 / defense_pokemon_1
      - ratio2 = attaque_pokemon_2 / defense_pokemon_2
      - gagnant = random de 0 à somme(ratio1, ratio2). (meme principe que % spawn)
10 - Mettre en place les pokedollars ($). Chaque combat gagné rapporte entre 1 et 2000 pokedollars
11 - Ajouter un shop, avec les prix suivants : 
      -> pokeball : 200$
      -> superball : 600$
      -> hyperball : 1 200$
      -> masterball : 50 000$
12 - Mettre en place le tout dans un programme en CLI, avec un menu : 
      -> shop
      -> spawn
      -> inventaire objets
      -> inventaire pokemon