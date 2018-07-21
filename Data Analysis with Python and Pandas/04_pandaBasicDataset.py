import quandl
import pandas as pd 

fiddy_states = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')

for abbv in fiddy_states[0][1][1:]:
    print("FMAC/HPI_"+str(abbv))
