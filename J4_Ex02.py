import pandas as pd

df = pd.read_csv('athlete_events.csv')

# def __init__(self):
#         pass

def proportion_by_sport(df, year, sport, gender):
    given_sport = df.loc[(df.Year == year) & (df.Sport == sport) & (df.Sex == gender), ['ID']]
    other_sport = df.loc[(df.Year == year) & (df.Sport != sport) & (df.Sex == gender), ['ID']]

    given_sport = given_sport.drop_duplicates()
    other_sport = other_sport.drop_duplicates()

    given_sport_size = given_sport.size
    other_sport_size = other_sport.size

    print(given_sport_size / (given_sport_size + other_sport_size))

proportion_by_sport(df, 2004, 'Tennis', 'F')