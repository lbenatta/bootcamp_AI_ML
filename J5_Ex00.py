import pandas as pd
import numpy as np

 #--------------Foe, ok ------------------
 
class TinyStatistician:
    def __init__(self):
        pass

    def my_mean(self, dataset):
        dataset_df = pd.DataFrame(dataset)
        sum = dataset_df.sum() 
        print ("My_Sum:", sum)
        count = len(dataset_df.index)
        print ("My_len:", count)
        my_mean = sum / count
        print("My_mean:", my_mean)
        return(my_mean)
# #-----------------ne foe pas ---------------------
#     def my_median(self, dataset):
#         dataset_df = pd.DataFrame(dataset)
#         count = len(dataset_df.index)
#         arr = dataset_df.to_numpy()
#         x = (count / 2)
#         print("x", x)
#         #my_median = dataset_df.loc[['x'] , [0]]
#         my_median = arr['x']
#         print("My_meadian:", my_median)
#         return(my_median)


#         import numpy as np

class TinyStatistician:
    def __init__(self):
        """docstring for __init__"""


    def mean(self, lst):
        """docstring for mean"""
        if len(lst) > 0:
            return np.add.reduce(lst) / len(lst)
        return None


    def median(self, lst):
        """docstring for mdian"""
        if len(lst) == 0:
            return None
        a = np.sort(lst)
        m = int(len(a) / 2)
        if len(lst) % 2 == 0:
            return float((a[m - 1] + a[m]) / 2)
        else:
            return float(a[m])


    def quartiles(self, lst):
        """docstring for quartiles"""
        if len(lst) == 0:
            return None
        a = np.sort(lst)
        m = len(a)
        m_q1 = (m + 3) / 4
        m_q3 = (m * 3 + 1) / 4

        def comp_q(m):
            """docstring for compute_quatile"""
            if m - int(m) == 0.25:
                q = (a[int(m) - 1] * 3 + a[int(m)]) / 4
            elif m - int(m) == 0.75:
                q = (a[int(m) - 1] + a[int(m)] * 3) / 4
            elif m - int(m) == 0.50:
                q = (a[int(m) - 1] + a[int(m)]) / 2
            else:
                q = a[int(m) - 1]
            return q

        return np.array([float(comp_q(m_q1)), float(comp_q(m_q3))])


    def percentile(self, x, p):
        """docstring for percentile"""
        if len(x) == 0:
            return None
        a = np.sort(x)
        m = len(a)
        m_p = (p / 100) * (m - 1)

        if m_p - int(m_p) == 0:
            res = a[int(m_p)]
        else:
            res = a[int(m_p) + 1] - a[int(m_p)]
            res = res * (m_p - int(m_p))
            res += a[int(m_p)]
        return res


    def var(self, lst):
        """docstring for variance"""
        if len(lst) == 0:
            return None
        m = self.mean(lst)
        ft = list(map(lambda x: (x - m)**2, lst))
        return np.add.reduce(ft) / len(lst)


    def std(self, lst):
        """docstring for std"""
        if len(lst) == 0:
            return None
        return np.sqrt(self.variance(lst))


tstat = TinyStatistician()
a = [1, 42, 300, 10, 59]
#a = [1, 42]
#print(tstat.mean(a))
#print(tstat.median(a))
print(tstat.quartiles(a))
print("Q1 quantile of arr : ", np.quantile(a, .25))
print("Q3 quantile of arr : ", np.quantile(a, .75))

print(tstat.percentile(a, 10))
print("percentile 10 of arr : ", np.quantile(a, .10))
#print(tstat.percentile(a, 15))
#print(tstat.percentile(a, 20))
#print(tstat.variance(a))
#print(tstat.std(a))


        # df.loc[:, 'A'] : renvoie une series
        # df.loc[:, ['A']] : renvoie un dataframe.
        # df.iloc[3, :] : renvoie une series.
        #df.loc[:,['A']] est un dataframe (avec une seule colonne).
        #df.loc[:,'A'] est une series, comme df['A'].

    # def my_quartile

    # def my_percentile

    # def my_var

    # def my_std
TinyStatistician = TinyStatistician()
dataset = [1,2,3,4,5,6,7,8,9,10,11,12]
TinyStatistician.my_mean(dataset)
TinyStatistician.my_median(dataset)
