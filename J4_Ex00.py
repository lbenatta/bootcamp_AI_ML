import pandas as pd
import importlib

class FileLoader:
    def __init__(self):
        pass

    def load(self, path):
        df = pd.read_csv(path)
        #dimensions =df.size
        dimensions = df.shape
        print("Loading dataset of dimensions:", dimensions)
        return(df)
    
    def display(self, dataset, n): 
        if n > 0:
            n = dataset[:n]
        else:
            n = dataset[:n]
        print(n)

fileloader= FileLoader()
dataset = fileloader.load('athlete_events.csv')
fileloader.display(dataset, 5)

