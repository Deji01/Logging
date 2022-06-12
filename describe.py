import sys
import pandas as pd

argument = sys.argv[-1]
try:
    df = pd.read_csv(argument)
    print(df.describe())
except Exception:
    print("Had a problem trying to read CSV file")