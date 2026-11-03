
monster_health = 150
player_damage = 25
aantal_aanvallen = 0

while monster_health > 0:
    monster_health -= player_damage

    # Zorg dat health niet onder 0 komt
    monster_health = max(0, monster_health)

    aantal_aanvallen += 1

    print("Monster health:", monster_health)

print("Monster verslagen!")
print("Aantal aanvallen:", aantal_aanvallen)

monsters = [100, 150, 200]
player_damage = 25

for monster_health in monsters:
    aantal_aanvallen = 0

    print("Nieuw monster!")

    while monster_health > 0:
        monster_health -= player_damage
        monster_health = max(0, monster_health)

        aantal_aanvallen += 1

        print("Monster health:", monster_health)

    print("Monster verslagen!")
    print("Aantal aanvallen:", aantal_aanvallen)
    print("--------------------")
