import sys
import numpy as np
import pandas as pd
from scipy.stats.mstats import theilslopes

def main():
    if(len(sys.argv) != 5):  # file_name, spreed_sheet_num, x_column, y_column
        return
    
    file_name = sys.argv[1]
    spreed_sheet = int(sys.argv[2])
    x_column = sys.argv[3]
    y_column = sys.argv[4]
    df = pd.read_excel(file_name, sheet_name = spreed_sheet)
    x = np.array(df[x_column])
    y = np.array(df[y_column])
    slope, intercept, low, up = theilslopes(y, x, 0.95)
    print("Slope: {}. Interval: [{},{}]  Intercept: {}".format(slope, low, up, intercept))

if __name__ == "__main__":

    main()

