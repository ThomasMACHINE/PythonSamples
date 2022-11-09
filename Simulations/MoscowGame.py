from random import randint
import matplotlib.pyplot as plt
import numpy as np

# tolerance = bets in a row they can lose
# goal = Percentage increase wanted
def doGamble(start, goal, tolerance):
    total = start
    goal = start * (1+(goal/100))
    bet = 0
    while(total < goal):
        # Set bet
        if bet == 0:
            bet = total * 2/2**tolerance
            if bet < goal - total:
                bet = goal - total
        else:
            bet *= 2
        # Gamble is lost if the total is higher than the bet
        if(bet > total):
            return 0

        win = randint(0,1)
        if(win == 1):
            total += bet
            bet = 0
        else:
            total = total - bet
    return total

# Conditions, start and end is the tolerances (amount of times you can lose)
# Participants = number of simulations for each tolerance
# StartMoney = Start value, Any value grants same results but grants meaning to the calculations
# Wealth Increase = Percentage of wealth increase wanted
start = 1
end = 17
participants = 10000
startMoney = 100_000
wealthIncrease = 50
loserCount = []

for i in range(start,end):
    count = 0
    for j in range(participants):
        res = doGamble(startMoney, wealthIncrease, i)
        if res == 0:
            count += 1
    perc = 1 - (count / participants)
    loserCount.append(perc)

xpoints = np.array(loserCount)

plt.plot(xpoints)
plt.xlabel("tolerance (bets they can lose in a row)")
plt.ylabel("Percentage winners")
plt.title("Start low and double your bet until you reach your goal!")
plt.show()


