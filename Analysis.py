import pandas as pd
import matplotlib.pyplot as plt

# Path to the original CSV file
input_file_path = '/Users/jacobscheer/Desktop/all_apps_wide-2024-07-19.csv'

# Reading the original CSV file
df = pd.read_csv(input_file_path)


# Creating a new DataFrame for the evaluation
# Filling the first column with numbers from 1 to 10
auswertung_df = pd.DataFrame({'Player.ID': range(1, 11)})

new_df = pd.DataFrame()

for i in range(1, 11): #Daten Sinnvoll Sortieren
    round_df = df[[f"topad.{i}.player.position", f"topad.{i}.player.take"]].sort_values(by=f'topad.{i}.player.position').iloc[:, 1:].T
    round_df.columns = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # die spalten umbennen um sie konkatienieren zu können
    new_df=pd.concat([new_df, round_df])

# Index in eine neue Spalte umwandeln und neuen Index zuweisen
new_df.reset_index(inplace=True)

# Index-Spalte in Round umbenennen
new_df.rename(columns={'index': 'Round'}, inplace=True)

# Index neu benennen
new_index = [f'Round {i+1}' for i in range(len(new_df))]
new_df.index = new_index
# Erste Spalte löschen
(new_df.drop(columns=['Round'], inplace=True))
#new_df.insert(0, 'Round', [f'Round {i+1}' for i in range(len(new_df))])
# Erste Zeile mit den Werten 0.03, 0.06, 0.12, etc. erstellen
new_row = [0.03 * (2 ** i) for i in range(len(new_df))]

# Neue Zeile einfügen
new_df.loc['poss_payoff'] = new_row

# DataFrame neu sortieren, um die neue Zeile an den Anfang zu setzen
new_df = pd.concat([new_df.loc[['poss_payoff']], new_df.drop('poss_payoff')])
# Ersetze alle Einsen durch 'x' und alle Nullen durch 'o'
new_df = new_df.replace({1: 'x', 0: 'o'})

# Ergebnis anzeigen
#print(df)


#winner = pd.DataFrame()
#show winner
for i in range(1,11):
    new_df.at[f"Round {i}", 'winner']=str(df.at[0,f"topad.{i}.group.winner"])

#show winner Payoff
for i in range(1,11):
    new_df.at[f"Round {i}", 'payoff']=str(df.at[0,f"topad.{i}.group.winner_payoff"])
#Den Gewinn einer jeden Runde in einer Zeile
'''for i in range(1,11):
    new_df.at["Payoff", i] = str(df.at[0, f"topad.{i}.group.winner_payoff"])'''


for i in range(1,11):
    new_df.loc['.', (i)] = str(".")

sum=0
pos=0
new_df.loc['.', "winner"] = str("Ratio")
new_df.loc['.', "payoff"] = str("payoff")
#show decision by player
for i in range(1,11):
    for j in range(1,11):
        #pos=f"topad.{j}.player.position)
        new_df.at[f"Player {i}", j] = str(df.at[ (i-1) , f"topad.{j}.player.take"])+' ('+str(df.at[ (i-1) , f"topad.{j}.player.position"])+')'
        #add Ratio
        sum=sum+int(df.at[ (i-1) , f"topad.{j}.player.take"])
        #replace 1 mit x o mit 0 und füge position hinzu
        str(new_df.at[f"Player {i}", j]).replace("1","x")
        #new_df.at[f"Player {i}", j] = df.at[(i - 1), f"topad.{j}.player.position"]
    new_df.at[f"Player {i}", "winner"] = f"{sum}0%"
    sum=0
    #add payoff
    new_df.at[f"Player {i}", "payoff"]=df.at[i-1, "participant.payoff"]

#(topad.{j}.player.position))]

print(new_df)


# Path to the new CSV file
output_file_path = '/Users/jacobscheer/Desktop/Auswertung.csv'

# Saving the new CSV file
new_df.to_csv(output_file_path, index=False)



# Payoff-Daten extrahieren
payoff_data = new_df.iloc[1:11]['payoff'].astype(float)
payoff_data.index = range(0,10)
#payoff_data.concat(new_df.iloc[1:11]['payoff'])
#winner-Daten etrahieren
winner_data = new_df.iloc[1:11]['winner'].astype(int)
winner_data.index = range(0,10)
#Merge die beiden Tabellen
#payoff_data=payoff_data.merge(winner_data)
rounds = range(1, len(payoff_data) + 1)

#Merge die beiden Tabellen
payoff_data = pd.concat([payoff_data, winner_data], axis=1)
#print(payoff_data)
#print(winner_data)

#.astype(float)