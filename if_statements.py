cijfer1 = 6
cijfer2 = 7
cijfer3 = 5

gemiddelde = (cijfer1 + cijfer2 + cijfer3) / 3

print("Gemiddelde:", gemiddelde)

if cijfer1 < 4 or cijfer2 < 4 or cijfer3 < 4:
    print("Gezakt!")
elif gemiddelde >= 5.5:
    print("Geslaagd!")
else:
    print("Gezakt!")