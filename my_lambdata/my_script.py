import pandas as pd

# import my mod
# from my-mod import flto_nc and dato_cl
from my_lambdata.my_mod import flto_nc
from my_lambdata.my_mod import split_column_date

# Instantiate df to test mod.py
df = pd.DataFrame({"Friends": ['Gene, Aaron, Dom, Scott, Zack'],
                   "Times won setback": [3, 1, 2, 0, 5072],
                   "First game won": [12-31-2012, 2-13-2015, 10-9-2008,
                                      5-6-2007, 10-2-1991]})

# List also to test mod.py
l = [5, 10, 15, 20, 25]
