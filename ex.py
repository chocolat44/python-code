# coding:utf8
import pandas as pd

mycars = pd.read_table('cars.csv', sep=',')
print(mycars)
# print(type(mycars))
# mycars = pd.read_csv('cars.csv', sep=',', index_col = 0)
# print(mycars)
# mycars = pd.read_table('cars.txt', index_col = 0)
# print(mycars)

print(mycars['country'])


col1  = ["a","a","b","b"]
col2  = [1,2,1,2]
col3  = [0.5,0.2,0.4,0.1]
col4  = [True,False,False,True]
mydf  =  pd.DataFrame({'id':col1,'time':col2,'varA':col3,'varB':col4}) 
mydf.set_index(['id','time'])
print(mydf)
print(mydf.melt(id_vars=['id','time']))

