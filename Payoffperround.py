import pandas as pd
import matplotlib.pyplot as plt
from Analysis import payoff_data
'''
# Erstellen des DataFrames mit den angegebenen payoff_data-Werten
data = {
    'Round': ['Round 1', 'Round 2', 'Round 3', 'Round 4', 'Round 5', 'Round 6', 'Round 7', 'Round 8', 'Round 9', 'Round 10'],
    'payoff': [0.48, 0.96, 0.48, 3.84, 0.96, 0.96, 0.48, 0.96, 0.96, 0.06],
    'winner': [5, 6, 5, 8, 6, 6, 5, 6, 6, 2]
}
'''
df = pd.DataFrame(payoff_data)

# Payoff-Daten extrahieren
payoff_data = df['payoff']
winners = df['winner']

# Runden als X-Achse festlegen
rounds = range(1, len(payoff_data) + 1)

# Aktualisierte Werte für die Y-Achse
yticks = [0.24, 0.48, 0.96, 1.92, 3.84]

# Balkendiagramm erstellen
plt.figure(figsize=(10, 6))
bars = plt.bar(rounds, payoff_data, color='#ADD8E6')  # Hellblau: #ADD8E6
plt.title('Payoff per Round')
plt.xlabel('Round')
plt.ylabel('Payoff')
plt.grid(True, axis='y', linestyle='--')  # gestrichelte Linien
plt.xticks(rounds)
plt.yticks(yticks)  # Setzt die aktualisierten Werte für die Y-Achse
plt.ylim(bottom=0)  # Setzt den unteren Grenzwert der Y-Achse auf 0

# Gewinner über den Balken anzeigen
for bar, winner in zip(bars, winners):
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width() / 2, height + 0.03, str(winner), ha='center', va='bottom')

plt.show()
