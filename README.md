## Tour de France Analysis

### Data Analysis with Predictive Modeling, Hypothesis Testing, Geospatial Data Visualtion, and Cluster Analysis

### Overview
- Data Analysis and Visualization:
   - Utilizes libraries like pandas, seaborn, and matplotlib for data analysis and visualization
     Presents data on stage distances over the years using line plots and forecasting

- Machine Learning:
   - Implements machine learning models, including RandomForestClassifier for classification tasks
   - Evaluates model performance using metrics like accuracy_score and classification_report

- Time Series Analysis:
   - Applies time series forecasting techniques, such as ARIMA and Exponential Smoothing (Holt-Winters)
   - Visualizes time series data, including forecasts and actual values, using matplotlib and plotly

- Deep Learning (LSTM):
   - Utilizes LSTM (Long Short-Term Memory) neural network architecture for time series forecasting
   - Splits data into training and testing sets

- Geocoding:
   - Uses the opencage library for geocoding, translating location names into geographical coordinates

- Statistical Analysis:
   - Performs statistical tests, including t-tests and ANOVA, to analyze differences in stage distances across years or decades
   - Outputs statistical results and significance levels

### Usage
1. **Clone the Repository:**
   ```bash
   git clone https://github.com/googs0/TourDeFranceStagesAnalysis.git

<br>

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt

<br>

2. **Run**
   ```bash
   python _main.py

<br>

Please note that the code is tailored to analyzing specific Tour de France data and may need adjustments if you want to apply it to a different text source

- Usage:
  - Import CSV data into DataFrame for analysis
  - Preprocess data inclyding feature extraction and data cleaning
  - Perform time series analysis on stage distances over the years
  - Apply predictive modeling techniques to predict stage winners based on features like year, distance, and stage type
  - Conduct hypothesis testing to compare to average stage distances between decades of Tour de France races
  - Enhance functionality as needed for specific use case
- External libraries: fbprophet, matplotlib, pandas, pydrive, plotly.express, scikit-learn, scipy
- Contact Information: [mgug1455@gmail.com](mailto:mgug1455@gmail.com)
  
<br>
<br>

**Example image:**
![Tour de France Example Screen 1](/assets/tdf-screen1.png)

<br>

![Tour de France Example Screen 2](/assets/tdf-screen2.png)
