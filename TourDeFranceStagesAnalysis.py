import os, re
from fbprophet import Prophet
import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
import seaborn as sns
from scipy import stats
from sklearn.metrics import accuracy_score, classification_report
from sklearn.cluster import KMeans
from sklearn.ensemble import RandomForestClassifier
from statsmodels.tsa.holtwinters import ExponentialSmoothing
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.arima_model import ARIMA

# Function to download a file from Google Drive by its shared link
def download_file_from_google_drive(shared_link, local_filename):
  # Extract the file ID from the shared link using regex
  file_id = re.findall(r"/d/([A-Za-z0-9_-]+)", shared_link)[0]

  # Authenticate and create a GoogleDrive instance
  gauth = GoogleAuth()
  gauth.LocalWebserverAuth()
  drive = GoogleDrive(gauth)

  # Download the file
  file = drive.CreateFile({'id': file_id})
  file.GetContentFile(local_filename)

# Define a function to preprocess the DataFrame
def preprocess_data(data):
  # Extract the year from the 'Date' column and add it as a new 'Year' column
  data['Year'] = data['Date'].apply(lambda date: date.split('/')[2])

  # Convert 'Distance' column to numeric
  data['Distance'] = data['Distance'].str.replace(' km', '').str.replace(',', '').astype(float)

  # Convert 'Time' column to datetime format
  data['Time'] = pd.to_datetime(data['Time'], format='%H:%M:%S')

# Implement ARIMA
def arima_forecasting(data):
  # Prepare the data (use 'Year' as the time index and 'Distance' as the target variable)
  data_arima = data[['Year', 'Distance']]
  data_arima = data_arima.set_index('Year')

  # Split the data into training and testing sets
  train_arima = data_arima.iloc[:-test_size]
  test_arima = data_arima.iloc[-test_size:]

  # Fit ARIMA model
  model_arima = ARIMA(train_arima, order=(5,1,0))
  model_fit_arima = model_arima.fit(disp=0)

  # Forecast
  forecast_arima = model_fit_arima.forecast(steps=test_size)

  # Plot the results
  plt.figure(figsize=(12, 6))
  plt.plot(train_arima, label='Training Data')
  plt.plot(test_arima, label='Test Data')
  plt.plot(test_arima.index, forecast_arima, label='ARIMA Forecast', color='red')
  plt.title('ARIMA Forecasting')
  plt.legend()
  plt.show()

# Implement Prophet
def prophet_forecasting(data):
  # Prepare the data for Prophet (Prophet expects columns 'ds' and 'y')
  data_prophet = data[['Year', 'Distance']]
  data_prophet = data_prophet.rename(columns={'Year': 'ds', 'Distance': 'y'})

  # Initialize and fit Prophet model
  model_prophet = Prophet()
  model_prophet.fit(data_prophet)

  # Create a dataframe for future predictions
  future = model_prophet.make_future_dataframe(periods=test_size)

  # Generate forecasts
  forecast_prophet = model_prophet.predict(future)

  # Plot the results
  fig = model_prophet.plot(forecast_prophet)
  plt.title('Prophet Forecasting')
  plt.show()

# Time Series Analysis (Place this section after preprocessing data)
def time_series_analysis(data):
  # Time Series Plot for Stage Distances
  plt.figure(figsize=(12, 6))
  sns.lineplot(data=data, x='Year', y='Distance')
  plt.xlabel('Year')
  plt.ylabel('Stage Distance (km)')
  plt.title('Time Series Analysis of Stage Distances')
  plt.xticks(rotation=45)
  plt.show()

  def time_series_forecasting(data):
  # Select the relevant time series data (e.g., stage distances over the years)
  time_series_data = data[['Year', 'Distance']]

  # Fit a time series forecasting model (e.g., Holt-Winters)
  model = ExponentialSmoothing(time_series_data['Distance'], trend='add', seasonal='add', seasonal_periods=1)
  fit_model = model.fit()

  # Forecast future stage distances
  forecast_steps = 5  # Adjust the number of future steps as needed
  forecast = fit_model.forecast(steps=forecast_steps)

  # Plot the time series and forecast
  plt.figure(figsize=(12, 6))
  sns.lineplot(data=time_series_data, x='Year', y='Distance', label='Observed')
  forecast.index = (range(time_series_data['Year'].max() + 1, 
                          time_series_data['Year'].max() + forecast_steps + 1)
                   )
  sns.lineplot(data=forecast, label='Forecast', color='red')
  plt.xlabel('Year')
  plt.ylabel('Stage Distance (km)')
  plt.title('Time Series Forecasting of Stage Distances')
  plt.xticks(rotation=45)
  plt.legend()
  plt.show()

  # Adjust the period if there's seasonality.
  result = seasonal_decompose(data['Distance'], model='additive', period=1)  
  result.plot()
  plt.show()

# Predictive Modeling (Place this section after preprocessing data)
def predictive_modeling(data):
  # Feature Engineering (create relevant features)
  data['StageType'] = data['Type'].apply(lambda x: 1 if x == 'Mountain' else 0)

  # Data Splitting
  from sklearn.model_selection import train_test_split

  # Define your features and target variable
  X = data[['Year', 'Distance', 'StageType']]
  y = data['Winner']

  # Split the data into training and testing sets
  X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

  # Create and train the model
  model = RandomForestClassifier(n_estimators=100, random_state=42)
  model.fit(X_train, y_train)

  # Make predictions
  y_pred = model.predict(X_test)

  # Evaluate the model
  accuracy = accuracy_score(y_test, y_pred)
  report = classification_report(y_test, y_pred)

  print(f"Accuracy: {accuracy:.2f}")
  print("Classification Report:\n", report)

# Clustering Analysis (Place this section after preprocessing data)
def clustering_analysis(data):
  # Select features for clustering (e.g., Distance and StageType)
  features = data[['Distance', 'StageType']]

  # Apply K-Means clustering with a specified number of clusters
  num_clusters = 3  # Adjust the number of clusters as needed
  kmeans = KMeans(n_clusters=num_clusters, random_state=42)
  data['Cluster'] = kmeans.fit_predict(features)

  # Visualize the clusters (e.g., scatter plot)
  plt.figure(figsize=(8, 6))
  sns.scatterplot(data=data, x='Distance', y='StageType', hue='Cluster', palette='viridis')
  plt.xlabel('Distance')
  plt.ylabel('Stage Type')
  plt.title('Clustering Analysis of Tour de France Stages')
  plt.show()

def advanced_visualization(data):
  # Create an interactive map of Tour de France routes using Plotly Express
  fig = px.scatter_geo(data, lat='Latitude', lon='Longitude', text='Location',
                       color='StageType', size='Distance',
                       title='Interactive Map of Tour de France Routes',
                       projection='natural earth')
  fig.update_geos(showcoastlines=True, coastlinecolor="Black", showland=True, landcolor="white")
  fig.show()

def hypothesis_testing(data):
  # Separate data into two decades (e.g., 2000-2009 and 2010-2019)
  data_2000s = data[(data['Year'] >= 2000) & (data['Year'] < 2010)]
  data_2010s = data[(data['Year'] >= 2010) & (data['Year'] < 2020)]

  # Perform a t-test to compare average stage distances between the two decades
  t_stat, p_value = stats.ttest_ind(data_2000s['Distance'], data_2010s['Distance'])

  # Interpret the results
  significance_level = 0.05  # Adjust the significance level as needed
  if p_value < significance_level:
    result = "statistically significant"
  else:
    result = "not statistically significant"

  print(f"Average stage distances between 2000-2009 and 2010-2019 are {result}.")
  print(f"T-Statistic: {t_stat:.2f}, P-Value: {p_value:.4f}")

if __name__ == "__main__":
  # Define file paths and URLs
  shared_link = 'https://drive.google.com/file/d/10ztDH5gUoFNciJFeFg4UZsfIUvE8tBwB/view?usp=sharing'
  local_filename = "stages_TourDeFrance.csv"

  # Check if the file already exists locally, if not, download it
  if not os.path.isfile(local_filename):
    download_file_from_google_drive(shared_link, local_filename)
    print(f"Downloaded file: {local_filename}")

  # Read the CSV data into a DataFrame
  tdfstages = pd.read_csv(local_filename)

  print(f"Importing CSV data from {local_filename}.\n")

  # Preprocess the data
  preprocess_data(tdfstages)

  # Time Series Analysis
  time_series_analysis(tdfstages)

  # Predictive Modeling
  predictive_modeling(tdfstages)
  
  # Hypothesis Testing
  hypothesis_testing(tdfstages)
