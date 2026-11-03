boodschappen = ["brood", "melk", "kaas", "appels", "eieren"]

boodschappen.append("cola")
boodschappen.append("chips")

boodschappen.remove("kaas")

print("Aantal producten:", len(boodschappen))
print("Boodschappenlijst:", boodschappen)

if "melk" in boodschappen:
    print("Melk staat in de lijst")
else:
    print("Melk staat niet in de lijst")