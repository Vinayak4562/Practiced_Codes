# import pandas as pd


# a = pd.read_excel("HR_Employee_Data.xlsx")
# print(a)

import pandas as pd
import numpy as np
dict1 = {
    "Name":['Vinayak','Vishal','Ramesh','Suhas'],
    "Marks":[98,65,60,99],
    "City":['Vijapur','Bijapur','Hebbal','Bnagar']
}

df = pd.DataFrame(dict1)
print(df)
# ________________________ to export it in csv(exel) to_csv.
df.to_csv('friends.csv')

df.to_csv('friends_indexing_nill', index = False) # To eliminate the index num


print(df.head(2)) # To display only starting 2 rows
print()
print(df.tail(2)) # To display only ending 2 rows
print()
print(df.describe()) # To display Statistical Analysis








