import pandas as pd

ex = pd.read_excel('test.xlsx',engine='openpyxl')
data = ex.head()
print('\n(0)',format(data))
