import pandas as pd 
import matplotlib.pyplot as plt 
from dataclasses import dataclass
import numpy as np

#Einlesen des Datensatzes 
pokedex = pd.read_csv('../Database/pokemon.csv')

#Header ausgeben lassen 
#print(pokedex.head())

#Die Anzahl der einzelnen Werte pro Spalte angeben, um die Vollstänigkeit zu checken
#print(pokedex.count())

#Print Charmander
# print(pokedex[pokedex['Name'] == 'Bulbasaur'])
# print(pokedex[pokedex['Name'] == 'Charmander'])

#Einlesen des Datensatzes
str_weak = pd.read_csv('../Database/chart.csv')
str_weak = str_weak.set_index("Attacking")

#print(str_weak.head())
#print(str_weak.count())
#print(pokedex[pokedex['Name'] == 'Bulbasaur']['Name'])

@dataclass 
class Pokemon:
    name: str
    type_1: str
    type_2: str

    def __init__(self, name):
        self.name = name 
        pk = pokedex[pokedex['Name'] == name]
        self.type_1 = pk['Type 1']
        self.type_2 = pk['Type 2']

        

    def get_weaknesses(self):
        if pd.isnull([self.type_2]):
            pk_weakness = str_weak[self.type_1.item()]
        else:
            pk_weakness = str_weak[self.type_1[0]] * str_weak[self.type_2[0]]
        not_neutral = pk_weakness[pk_weakness != 1]
        
        weak_res = {}
        for value in not_neutral:
            if value not in weak_res:
                weak_res[str(value)] = not_neutral[not_neutral==value].index.tolist()
        return weak_res



    def show_resistance(self):
        fig,ax = plt.subplots()
        # ind,label = [],[] 
        # pos,neg = 0,0
        keys = ["0.0","0.25","0.5","2.0","4.0"]
        weak_res = self.get_weaknesses()
        data = []
        resistance = []
        types = []
        for key in keys:
            if key in weak_res:
                data.append(len(weak_res[key]))
                resistance.append(key)
                types.append(weak_res[key])
        wedges, texts = ax.pie(data, wedgeprops=dict(width=0.5), startangle=-40)
        bbox_props = dict(boxstyle="square,pad=0.3", fc="w", ec="k", lw=0.72)
        kw = dict(arrowprops=dict(arrowstyle="-"), bbox=bbox_props, zorder=0, va="center")
        for i, p in enumerate(wedges):
            ang = (p.theta2 - p.theta1)/2. + p.theta1
            y = np.sin(np.deg2rad(ang))
            x = np.cos(np.deg2rad(ang))
            horizontalalignment = {-1: "right", 1: "left"}[int(np.sign(x))]
            connectionstyle = f"angle,angleA=0,angleB={ang}"
            kw["arrowprops"].update({"connectionstyle": connectionstyle})
            ax.annotate(types[i], xy=(x, y), xytext=(1.35*np.sign(x), 1.4*y), horizontalalignment=horizontalalignment, **kw)
            # Add text inside the wedge
            ax.text(0.75 * x, 0.75 * y, resistance[i], ha='center', va='center', fontsize=10, fontweight='bold')

        ax.set_title(f"Resistance: {self.name}")
        return fig


Bulbasaur = Pokemon('Bulbasaur')
# Charmander = Pokemon('Charmander')
# print(Bulbasaur.get_weaknesses())
# # print(Charmander.get_weaknesses())
# Charmander.show_resistance()
Bulbasaur.show_resistance()
# plt.show()