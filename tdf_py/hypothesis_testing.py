from imports import f_oneway, stats


def hypothesis_testing(data):
    # Separate data into decades
    decades_data = [
        data[(data['Year'] >= 1940) & (data['Year'] < 1950)],
        data[(data['Year'] >= 1950) & (data['Year'] < 1960)],
        data[(data['Year'] >= 1960) & (data['Year'] < 1970)],
        data[(data['Year'] >= 1970) & (data['Year'] < 1980)],
        data[(data['Year'] >= 1980) & (data['Year'] < 1990)],
        data[(data['Year'] >= 1990) & (data['Year'] < 2000)],
        data[(data['Year'] >= 2000) & (data['Year'] < 2010)],
        data[(data['Year'] >= 2010) & (data['Year'] < 2020)],
    ]

    # Perform ANOVA
    f_stat, p_value = f_oneway(*[decade['Distance (km)'] for decade in decades_data])

    # Interpret the results
    significance_level = 0.05  # Adjust the significance level as needed
    if p_value < significance_level:
        result = "statistically significant"
    else:
        result = "not statistically significant"

    print(f"\nAverage stage distances across decades are {result}.")
    print(f"F-Statistic: {f_stat:.2f}, P-Value: {p_value:.4f}\n")

    # Separate data into 2 separate decades for t-stat
    data_1940s = data[(data['Year'] >= 1940) & (data['Year'] < 1950)]
    data_2000s = data[(data['Year'] >= 2000) & (data['Year'] < 2010)]
    data_2010s = data[(data['Year'] >= 2010) & (data['Year'] < 2020)]
    # Perform a t-test to compare average stage distances between the two decades
    t_stat, p_value = stats.ttest_ind(data_1940s['Distance (km)'], data_2010s['Distance (km)'])

    # Interpret the results
    significance_level = 0.05  # Adjust the significance level as needed
    if p_value < significance_level:
        result = "statistically significant"
    else:
        result = "not statistically significant"

    print(f"Average stage distances between 1940-1949 and 2010-2019 are {result}.")
    print(f"T-Statistic: {t_stat:.2f}, P-Value: {p_value:.4f}\n")

    t_stat, p_value = stats.ttest_ind(data_2000s['Distance (km)'], data_2010s['Distance (km)'])
    # Interpret the results
    significance_level = 0.05  # Adjust the significance level as needed
    if p_value < significance_level:
        result = "statistically significant"
    else:
        result = "not statistically significant"

    print(f"Average stage distances between 2000-2009 and 2010-2019 are {result}.")
    print(f"T-Statistic: {t_stat:.2f}, P-Value: {p_value:.4f}\n")
