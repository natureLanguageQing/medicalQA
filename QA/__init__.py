import os

import pandas as pd

instructions = pd.read_csv(os.path.join("../data", "ims_ldy_500.csv"))
drug_names = pd.read_csv(os.path.join("../data", "drug_name.csv"))
