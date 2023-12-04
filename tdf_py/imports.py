import logging
import re
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import requests
import seaborn as sns
from scipy import stats
from sklearn.cluster import KMeans
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import MinMaxScaler, LabelEncoder
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.holtwinters import ExponentialSmoothing
from statsmodels.tsa.seasonal import seasonal_decompose
from keras.layers import LSTM, Dense
from keras.models import Sequential
import plotly.graph_objects as go
import opencage.geocoder
import matplotlib.dates as mdates
import mplcursors
from scipy.stats import f_oneway
import log_config

log_config.setup_logging()
