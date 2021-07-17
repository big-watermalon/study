import numpy as np
import pandas as pd

obj = pd.Series([x for x in range(10)],index=[chr(x) for x in range(ord('a'),ord('j')+1)])
print(obj)

