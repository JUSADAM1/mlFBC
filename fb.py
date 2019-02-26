
import numpy as np
import matplotlib.pyplot as plt

#This Graph and data will tell you who has more
# of, when it comes down to heros and villains over all universe.

Marvel = 1000
marvelHeros = 1000
marvelVill =1000
DC = 1000
DcHeros =1000
DcVill =1000




#this are more rounded and a rough estimation but
#The amount of charcters in both universes are right.
#but apparently their are more character in marvel
    #HEROS IN BOTH ARE COUNTING TEAMS AND GROUPS
    #ALSO VILLAINS
#MARVEL DATA
marvelUni = 8000 + 1000 * np.random.randn(Marvel)
marvelH = 3300 + 1000 * np.random.randn(marvelHeros)
marvelV = 4700 + 1000 * np.random.randn(marvelVill)
#DC DATA
dcUni = 10000 + 1000 * np.random.randn(DC)
DCV = 6000 + 1000 * np.random.randn(DcVill)
DCH = 4000 + 1000 * np.random.randn(DcHeros)

#visualize our data in a histogram
# Bombers in blue and fighters in red
plt.hist([marvelUni, marvelV, marvelH, dcUni, DCV, DCH], stacked=True, color=['r', 'g', 'w', 'b', 'k', 'c'], edgecolor = 'k')


plt.suptitle("Marvel VS DC")
plt.axis('tight')

plt.show()

