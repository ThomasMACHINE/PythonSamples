'''
Damage dealt by abilities are picked uniformally within the lower and higher boundary
[0, 1000] -> average = 500

@min - Lower boundary
@max - Higher boundary
@cap - Damage cap, no instance of damage can be higher than this
@critBoost - an instance of damage can crit, this infers a hit within the 95-100%
            of the abilitys damage range
'''
class Ability:
    '''
    These are variables on a character and based set as the highest achieveable stats
    '''
    # Static variables
    AD = 1686
    base_level = 99
    boosted_level = 128
    precise_rank = 5
    equilibrium_rank = 3
    soft_cap = 10000
    crit_hard_cap  = 12000
    aura = 1.1
    critBoost = 0

    def __init__(self,name, min, max):
        self.name = name
        self.min = min
        self.max = max

    def setAvg(self):
        # Game system floors after each calculation
        fixed_base = ((self.AD * 0.01 * self.min)) // 1
        fixed_boosted = (fixed_base + 4 * (self.boosted_level - self.base_level)) // 1
        fixed_final = (fixed_boosted) // 1

        variable_base = (self.AD * (0.01*(self.max- self.min))- 0.01) // 1
        variable_boosted = (variable_base + 4 *(self.boosted_level - self.base_level))
        variable_final = (variable_boosted) // 1

        final_max = fixed_final + variable_final
        natural_crit_min = (0.95 * final_max) // 1

        # Account for Precise 
        precise_impact = (0.015 * self.precise_rank * final_max) // 1
        precise_fixed = (fixed_final + (precise_impact))  
        precise_variable = (variable_final - precise_impact) 

        # Account for equilibrium impact       
        equil_fixed = (precise_fixed + (0.03 * self.equilibrium_rank * precise_variable)) // 1
        equil_variable = ((1 - 0.04 * self.equilibrium_rank) * precise_variable) // 1
        equil_max = equil_fixed + equil_variable
        
        equil_fixed2 = (equil_fixed * 1.1) // 1
        equil_variable2 = (equil_variable * 1.1) // 1
        equil_max = equil_fixed2 + equil_variable2

        # Account for criticial hit chance
        forced_crit_chance = self.critBoost 
        # crit shit man cant understand
        natural_crit_chance = ((0.05 * (precise_fixed + precise_variable))//1) / precise_variable
        non_crit_chance = (1 - forced_crit_chance) * (1 - natural_crit_chance)
        natural_crit_min = ((equil_fixed2 + equil_variable2) * 0.95) // 1
        forced_crit_min = (equil_fixed2 + 0.95)

        # Find chances of max value
        forced_cap_percentage = (equil_max - self.crit_hard_cap) / (equil_max - forced_crit_min)
        natural_cap_percentage = (equil_max- self.crit_hard_cap) / (equil_max - natural_crit_min)
        soft_cap_percentage = (natural_crit_min - self.soft_cap) / (natural_crit_min - equil_fixed2)

        # If maximum value is not past cap, set percentages to 0
        if (equil_max - self.crit_hard_cap) < 0:
            forced_cap_percentage = 0
            natural_cap_percentage = 0 

        if (natural_crit_min - self.soft_cap) < 0:
            soft_cap_percentage = 0 

        # For the three scenarios, forced, natural and non crit, find out their contributions to the average
        forcedCritContribution  = forced_crit_chance * (forced_cap_percentage * self.crit_hard_cap + (1 - forced_cap_percentage) * 0.5 * (self.crit_hard_cap + forced_crit_min))
        naturalCritContribution = natural_crit_chance * (natural_cap_percentage * self.crit_hard_cap + (1 - natural_cap_percentage) * 0.5 * (natural_crit_min + equil_max))
        nonCritContribution     = non_crit_chance * (soft_cap_percentage * 10000 + (1 - soft_cap_percentage) * 0.5 * (natural_crit_min + equil_fixed2))
        # Average is the sum of all these
        self.average = forcedCritContribution + naturalCritContribution + nonCritContribution

class Player:
    def __init__(self, AD, baseLevel, boostedLevel, preciseRank, equilibriumRank, softCap, hardCap, damageModifier, critBoost):
        self.AD = AD
        self.base_level = baseLevel
        self.boosted_level = boostedLevel
        self.precise_rank = preciseRank
        self.equilibrium_rank = equilibriumRank
        self.softCap = softCap
        self.hardCap  = hardCap
        self.damageModifier = damageModifier
        self.critBoost = critBoost
        


if __name__ == '__main__':
    a = Ability("Wrack", 18.8, 94)
    a.setAvg()
    print("Checking if calculations are still working")
    print("Is full value is same?")
    print(a.average == 1345.5204490777867)
    print("Is rounded value is same?")
    print(a.average // 1 == 1345)