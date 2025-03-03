import pandas as pd
import pickle

df = pd.read_excel('Baz.xlsx')
df.columns = ["column"]
mylist = df["column"].tolist()

my_list_1 = [x.replace("+", "") for x in mylist]

my_list2 = [x.replace(" ", "") for x in my_list_1]

my_list_3 = [x.replace("-", "") for x in my_list2]

my_list_4 = ["79996552266"] + my_list_3



with open("my_list", "wb") as fp:
    pickle.dump(my_list_4, fp)

