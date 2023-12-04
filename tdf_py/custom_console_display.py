from imports import np, pd

# PyCharm better viewing options for dataframe (see more than 5 col)
desired_width = 320
pd.set_option('display.width', desired_width)
np.set_printoptions(linewidth=desired_width)
pd.set_option('display.max_columns', None)
