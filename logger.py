import sys
import pandas as pd

argument = sys.argv[-1]

df = pd.read_csv(argument)
print(df.describe)