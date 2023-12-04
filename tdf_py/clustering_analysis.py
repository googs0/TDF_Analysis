from imports import KMeans, logging, pd, plt, re, sns


def create_stage_groups(row, df):
    stage = str(row['Stage'])

    if len(stage) == 1 and stage.isalpha():
        return 00

    numeric_part = re.search(r'(\d+)', str(row['Stage'])).group(1) if re.search(r'(\d+)', str(row['Stage'])) else None

    if numeric_part is None:
        # Filter df to find all rows with the same single character
        filter_condition = (df['Stage'].str.len() == 1) & (df['Stage'] == row['Stage'])
        numeric_part = str(df.loc[filter_condition, 'Stages'].min())

    return numeric_part


# Clustering Analysis
def clustering_analysis(data):
    # Check if 'Stage' column is present
    if 'Stage' not in data.columns:
        logging.warning("'Stage' column not found. Make sure it is created in the preprocessing steps.")
        return

    # Create a new column 'Stages Grouped' based on the 'Stage' column
    data['Stages Grouped'] = data.apply(lambda row: create_stage_groups(row, data), axis=1)

    # Convert 'Stages Grouped' to numeric type
    data['Stages Grouped'] = pd.to_numeric(data['Stages Grouped'], errors='coerce')

    # Features for cluster
    features = data[['Distance (km)', 'Stages Grouped']]

    # K-Means clustering
    num_clusters = 3  
    kmeans = KMeans(n_clusters=num_clusters, random_state=42, n_init='auto')
    data['Cluster'] = kmeans.fit_predict(features)

    # Plot clusters 
    plt.figure(figsize=(12, 8))
    palette = sns.color_palette("husl", num_clusters)

    sns.scatterplot(data=data, x='Distance (km)', y='Stages Grouped',
                    hue='Cluster', palette=palette)

    plt.xlabel('Distance (km)')
    plt.ylabel('Stages Grouped')
    plt.title('Clustering Analysis of Tour de France Stages')
    plt.show()

    # Drop temporary numerical column
    data.drop(columns=['Stages Grouped'], inplace=True)

    # If 'Stages Grouped Numeric' is present, drop it
    if 'Stages Grouped Numeric' in data.columns:
        data.drop(columns=['Stages Grouped Numeric'], inplace=True)

