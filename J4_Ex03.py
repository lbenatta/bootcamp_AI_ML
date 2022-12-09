import pandas as pd

df = pd.read_csv('athlete_events.csv')
dimensions = df.shape
print(dimensions)

df2= df.iloc[:, 14].isnull() 
dict = {"Gold" : 'G', "Bronze" : 'B' , "Silver" : 'S'}
df2 = df.replace({"Medal" : dict})
print("df2", df2)

def medal_type(df, year):
    G_medal = df.loc[(df.Year == year) & (df.Medal == G_medal)]
    print('G_medal', G_medal)

medal_type(df, 1992)