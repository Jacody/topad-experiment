import pandas as pd
import matplotlib.pyplot as plt
import os

# Definition des DataFrames
'''data = {
    '1': ['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'],
    '2': ['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'x'],
    '3': ['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'],
    '4': ['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'x'],
    '5': ['x', 'o', 'x', 'o', 'o', 'o', 'x', 'o', 'o', 'o'],
    '6': ['x', 'x', 'o', 'o', 'x', 'x', 'o', 'x', 'x', 'o'],
    '7': ['x', 'x', 'o', 'o', 'o', 'o', 'x', 'o', 'o', 'o'],
    '8': ['o', 'x', 'x', 'x', 'o', 'x', 'x', 'o', 'o', 'o'],
    '9': ['o', 'x', 'x', 'x', 'x', 'o', 'o', 'x', 'x', 'x'],
    '10': ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'o', 'x', 'x']
}'''

index = ['Round 1', 'Round 2', 'Round 3', 'Round 4', 'Round 5', 'Round 6', 'Round 7', 'Round 8', 'Round 9', 'Round 10']

decisions = pd.DataFrame(data, index=index)

# Farben für die Zellen definieren
cell_colors = decisions.applymap(lambda x: '#FFA07A' if x == 'x' else '#98FB98').values  # Anpassung der Farben

# Plotting
fig, ax = plt.subplots(figsize=(10, 12))  # Größeres Diagramm für bessere Lesbarkeit
ax.set_axis_off()
table = ax.table(cellText=decisions.values, cellColours=cell_colors, colLabels=decisions.columns, rowLabels=decisions.index, cellLoc='center', loc='center')
table.auto_set_font_size(False)
table.set_fontsize(14)
table.scale(1.5, 1.5)  # Angepasste Skalierung für größere Zellen

# Zellenränder hinzufügen
for key, cell in table.get_celld().items():
    cell.set_edgecolor('black')

# Achsenbeschriftungen hinzufügen, direkt an den Achsen
ax.annotate('Position', xy=(0.5, -0.05), xycoords='axes fraction', ha='center', fontsize=16, fontweight='bold')
#ax.annotate('Round', xy=(-0.05, 0.5), xycoords='axes fraction', va='center', rotation='vertical', fontsize=16, fontweight='bold')

# Pfad zum Desktop
file_path = '/Users/jacobscheer/Desktop/decisions_plot.png'

# Grafik speichern
plt.savefig(file_path, bbox_inches='tight', dpi=300)  # Höhere Auflösung für bessere Qualität

plt.show()

print(f"Grafik wurde gespeichert unter: {file_path}")
