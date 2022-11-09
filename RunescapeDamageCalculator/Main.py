'''
To learn more about Ability, look in Ability.py
'''
from Ability import Ability

AbilityInfo = open("Abilities.csv", "r")
AbilityInfo.readline()
WriteFile = open("AbilityAverages.csv", "w")
WriteFile.write("__NAME__, __AVERAGE__" + "\n")

# Iterate and write ability averages
for line in AbilityInfo:
    line = line[:-1]
    info = line.split(",")
    
    name = info[0]
    minimumDamage = float(info[1])
    maximumDamage = float(info[2])

    ability = Ability(name=name, min = minimumDamage, max= maximumDamage)
    ability.setAvg()
    damage = round(ability.average,2)
    WriteFile.write(ability.name + "," + str(damage) + "\n")
    
print("Finished Calculating")
WriteFile.close()
AbilityInfo.close()