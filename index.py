import pandas as pd
prison_break = pd.read_html('https://fr.wikipedia.org/wiki/Liste_des_%C3%A9pisodes_de_Prison_Break')
print(prison_break[0])

