import logging
import pandas as pd
import sys

log_format = "[% (name)s][%(levelname)-6s] %(message) s"
logging.basicConfig(format=log_format)
logger = logging.getLogger("describe")
logger.setLevel(logging.ERROR)

argument = sys.argv[-1]
logger.debug("processing input file: %s", argument)
try:
    df = pd.read_csv(argument)
    print(df.describe())
except Exception:
    logger.exception("Had a problem trying to read CSV file")