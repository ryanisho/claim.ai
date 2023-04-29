import pandas as pd
import numpy as np
from scipy.stats import wilcoxon

# read in the description_cost_data.csv from data


def read_csv():
    df = pd.read_csv('CLAIM.ai\data\description_cost_data.csv')
    return df


print(read_csv())
