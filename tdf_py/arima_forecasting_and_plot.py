from imports import ARIMA, mdates, pd, plt


def arima_forecasting(data, test_size=30, order=(5, 1, 0)):
    # Ensure the 'Year' column is in Datetime format
    data['Year'] = pd.to_datetime(data['Year'])

    # Prepare the data (use 'Year' as the time index and 'Distance' as the target variable)
    data_arima = data[['Year', 'Distance (km)']]
    data_arima.set_index('Year')

    # Split the data into training and testing sets
    train_arima = data_arima.iloc[:-test_size]
    test_arima = data_arima.iloc[-test_size:]

    # Fit ARIMA model
    model_arima = ARIMA(train_arima['Distance (km)'], order=order)
    model_fit_arima = model_arima.fit()

    arima_forecast_steps = 30

    forecast_index = pd.date_range(start=test_arima.index[-1], periods=arima_forecast_steps + 1, freq='Y')[1:]
    forecast_arima = model_fit_arima.get_forecast(steps=arima_forecast_steps).predicted_mean

    results = pd.DataFrame({
        'Year': forecast_index,
        'Actual Distance': test_arima['Distance (km)'].values,
        'ARIMA Forecast': forecast_arima.values
    })

    return results


def dark_mode_arima_plot(arima_results):
    plt.figure(figsize=(14, 8), facecolor='#333333', edgecolor='black')

    o_font = {'fontname': 'Open Sans'}

    ax = plt.axes()
    ax.set_facecolor('#262626')
    ax.grid(color='#595959', linestyle='-', linewidth=0.8)
    ax.tick_params(colors='#f2f5f5')

    plt.plot(arima_results['Year'], arima_results['Actual Distance'],
             label='Actual Distance', linestyle='-', color='royalblue',
             marker='o', markersize=8, markeredgecolor='snow', linewidth=2)

    # Plot ARIMA forecast with orange color
    plt.plot(arima_results['Year'], arima_results['ARIMA Forecast'],
             label='ARIMA Forecast', linestyle='-', color='darkorange',
             marker='o', markersize=8, markeredgecolor='snow', linewidth=2)

    plt.title('ARIMA Forecasting', **o_font, fontsize=18, color='#cccccc')
    plt.xlabel('Year', **o_font, fontsize=14, color='#cccccc', labelpad=10)
    plt.ylabel('Distance', **o_font, fontsize=14, color='#cccccc', labelpad=10)
    plt.legend(fontsize=12)
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
    plt.tight_layout(pad=1.5)
    plt.show()


def plot_arima_results(arima_results, dark_mode=False):

    if dark_mode:
        dark_mode_arima_plot(arima_results)
    else:
        plt.figure(figsize=(14, 8), facecolor='#f2f2f2')

        o_font = {'fontname': 'Open Sans'}

        ax = plt.axes()
        ax.set_facecolor('#f4f4f4')
        ax.grid(color='#8c8c8c', linestyle='-', linewidth=0.8)

        # Plot actual distance with blue color
        plt.plot(arima_results['Year'], arima_results['Actual Distance'],
                 label='Actual Distance', linestyle='-', color='steelblue',
                 marker='o', markersize=8, markeredgecolor='navy', linewidth=2)

        # Plot ARIMA forecast with orange color
        plt.plot(arima_results['Year'], arima_results['ARIMA Forecast'],
                 label='ARIMA Forecast', linestyle='-', color='darkorange',
                 marker='o', markersize=8, markeredgecolor='darkred', linewidth=2)

        plt.title('ARIMA Forecasting', **o_font, fontsize=18, color='#1a1a1a')
        plt.xlabel('Year', **o_font, fontsize=14, color='#1a1a1a')
        plt.ylabel('Distance', **o_font, fontsize=14, color='#1a1a1a')
        plt.legend(fontsize=12)
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
        plt.tight_layout(pad=1.5)

        plt.show()
