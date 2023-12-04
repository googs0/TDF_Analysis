from imports import logging, re


def clean_data_historical_modern(data):
    # Fill missing values
    data['Hour'].fillna(0, inplace=True)
    data['Minutes'].fillna(0, inplace=True)
    data['Seconds'].fillna(0, inplace=True)
    data['Pace'].fillna(0, inplace=True)
    data['Team'].fillna('No Team', inplace=True)

    # Convert types
    data[['Hour', 'Minutes', 'Seconds']] = data[['Hour', 'Minutes', 'Seconds']].astype(int)
    logging.info(f"Hour, Minutes, Seconds to int:\n{data.dtypes}\n")

    # Rename columns and create a new column
    data.rename(columns={'Started': 'Riders Started', 'Ended': 'Riders Finished', 'Distance': 'Distance (km)',
                         'RidersDropped': 'Riders Dropped'}, inplace=True)

    data['Riders Dropped'] = data['Riders Started'] - data['Riders Finished']

    # Miles distance
    miles = data['Distance (km)'] / 1.609344
    data.insert(5, "Distance (mi)", miles)

    # Round to the second decimal
    data = data.round(decimals=2)

    # Move columns to the end
    move_columns = ['Riders Started', 'Riders Finished']
    other_columns = [col for col in data.columns if col not in move_columns]
    data = data[other_columns[:-1] + [move_columns[0]] + [move_columns[1]] + other_columns[-1:]]

    # Log sample
    logging.info(f"Sample of Tour De France after cleaning:\n{data.sample(10)}"
                 f"\n\nTour De France Data Cleaning Complete\n\n")

    return data


def clean_data_stages(data):
    data = data.rename({'Distance': 'Distance (km)', 'Origin': 'Origin City',
                        'Destination': 'Destination City', 'Type': 'Stage Type',
                        'Winner_Country': 'Country'}, axis='columns')

    # Miles distance
    miles = data['Distance (km)'] / 1.609344
    data.insert(3, "Distance (mi)", miles)

    year_list = []
    full_date = data['Date']
    for date in full_date:
        format_date = date.split("/")[-1]
        year_list.append(int(format_date))

    data.insert(2, 'Year', year_list)

    data = data.round(decimals=2)

    data['Country'] = data['Country'].apply(
        lambda x: re.search(r'"(.*?)"', str(x)).group(1).upper() if re.search(r'"(.*?)"', str(x)) else x)

    logging.info(f"Sample of Stages after cleaning:\n{data.head(10)}\n\nStages Data Cleaning Complete\n\n")

    return data
