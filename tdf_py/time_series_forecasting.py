from imports import ExponentialSmoothing, np, plt, seasonal_decompose, sns


def dark_mode_time_series_forecasting(data):
    # Select the relevant time series data (e.g., stage distances over the years)
    time_series_data = data[['Year', 'Distance (km)']]

    # Fit a time series forecasting model (e.g., Holt-Winters)
    model = ExponentialSmoothing(time_series_data['Distance (km)'], trend='add', seasonal='add',
                                 seasonal_periods=12)
    fit_model = model.fit()

    # Forecast future stage distances
    forecast_steps = 5  # Adjust the number of future steps as needed
    forecast = fit_model.forecast(steps=forecast_steps)

    # Plot the time series and forecast
    plt.figure(figsize=(14, 8), facecolor='#262626', edgecolor='#262626')
    o_font = {'fontname': 'Helvetica'}

    ax = plt.axes()
    ax.set_facecolor('#262626')
    ax.grid(color='#595959', linestyle='--', linewidth=0.5, alpha=0.5)
    ax.tick_params(colors='#bfbfbf')

    # Use the entire 'turbo' colormap for line
    palette = sns.color_palette('turbo', n_colors=len(data), as_cmap=True)

    # Plot
    for i in range(len(data) - 1):
        color = palette(i / (len(data) - 1))
        plt.plot([data['Year'].iloc[i], data['Year'].iloc[i + 1]],
                 [data['Distance (km)'].iloc[i], data['Distance (km)'].iloc[i + 1]],
                 color=color, linewidth=2)

    plt.fill_between(data['Year'],
                     data['Distance (km)'] - (data['Distance (km)'].std() * 0.5),
                     data['Distance (km)'] + (data['Distance (km)'].std() * 0.5),
                     color='#ccccff', alpha=0.5)

    # Mark the first and last points
    plt.scatter(data['Year'].iloc[0], data['Distance (km)'].iloc[0], color='tomato', s=20, zorder=5)
    plt.scatter(data['Year'].iloc[-1], data['Distance (km)'].iloc[-1], color='tomato', s=20, zorder=5)

    # Annotate the first point with 'Year'
    plt.annotate(text=str(data['Year'].iloc[0]),
                 xy=(data['Year'].iloc[0], data['Distance (km)'].iloc[0]),
                 xytext=(-6, -4), textcoords='offset points',
                 ha='right', va='bottom', fontsize=8, color='#cceeff', weight='bold')

    # Annotate the last point with 'Year'
    plt.annotate(text=str(data['Year'].iloc[-1]),
                 xy=(data['Year'].iloc[-1], data['Distance (km)'].iloc[-1]),
                 xytext=(27, 3), textcoords='offset points',
                 ha='right', va='bottom', fontsize=8, color='#cceeff', weight='bold')

    # Plot forecasted values
    forecast_years = np.arange(data['Year'].iloc[-1] + 1, data['Year'].iloc[-1] + 1 + forecast_steps)
    plt.plot(forecast_years, forecast, label='Forecast', color='#ffcc00', linestyle='--', linewidth=2)

    plt.ylabel('Stage Distance (km)', **o_font, fontsize=14, color='#bfbfbf', labelpad=10)
    plt.xticks()
    plt.title('Time Series Forecasting of Stage Distances', **o_font, fontsize=20, color='#bfbfbf')

    # Legend
    plt.legend(loc='upper left', fontsize=12, framealpha=0.4)


def plot_seasonal_decomp(data, period=5):
    # Adjust the period if there's seasonality.
    result = seasonal_decompose(data['Distance (km)'], model='additive', period=period)

    # Plot the seasonal decomposition components
    plt.figure(figsize=(12, 8), facecolor='#e6e6e6')
    plt.subplot(4, 1, 1)
    plt.plot(result.observed, label='Original', color='#4d4dff', linewidth=2)
    plt.grid(alpha=0.5)
    plt.legend()
    plt.title('Original Time Series', weight='bold')

    plt.subplot(4, 1, 2)
    plt.plot(result.trend, label='Trend', color='#ff661a', linewidth=2)
    plt.grid(alpha=0.5)
    plt.legend()
    plt.title('Trend Component', weight='bold')

    plt.subplot(4, 1, 3)
    plt.plot(result.seasonal, label='Seasonal', color='#00e600', linewidth=2)
    plt.grid(alpha=0.5)
    plt.legend()
    plt.title('Seasonal Component', weight='bold')

    plt.subplot(4, 1, 4)
    plt.plot(result.resid, label='Residual', color='#ff0066', linewidth=2)
    plt.grid(alpha=0.5)
    plt.legend()
    plt.title('Residual Component', weight='bold')


def time_series_forecasting(data, dark_mode=False, seasonal_decomposition=False):

    if dark_mode:
        dark_mode_time_series_forecasting(data)
    else:
        # Select the relevant time series data (e.g., stage distances over the years)
        time_series_data = data[['Year', 'Distance (km)']]

        # Fit a time series forecasting model (e.g., Holt-Winters)
        model = ExponentialSmoothing(time_series_data['Distance (km)'], trend='add', seasonal='add',
                                     seasonal_periods=12)
        fit_model = model.fit()

        # Forecast future stage distances
        forecast_steps = 5  # Adjust the number of future steps as needed
        forecast = fit_model.forecast(steps=forecast_steps)

        # Plot the time series and forecast
        plt.figure(figsize=(14, 8), facecolor='#f2f2f2', edgecolor='#262626')
        o_font = {'fontname': 'Helvetica'}

        ax = plt.axes()
        ax.set_facecolor('#f2f2f2')
        ax.grid(color='#595959', linestyle='--', linewidth=0.5, alpha=0.5)
        ax.tick_params(colors='#262626')

        # Use the entire 'turbo' colormap
        palette = sns.color_palette('turbo', n_colors=len(data), as_cmap=True)

        # Plot
        for i in range(len(data) - 1):
            color = palette(i / (len(data) - 1))
            plt.plot([data['Year'].iloc[i], data['Year'].iloc[i + 1]],
                     [data['Distance (km)'].iloc[i], data['Distance (km)'].iloc[i + 1]],
                     color=color, linewidth=2)

        plt.fill_between(data['Year'],
                         data['Distance (km)'] - (data['Distance (km)'].std() * 0.5),
                         data['Distance (km)'] + (data['Distance (km)'].std() * 0.5),
                         color='#b3e6ff', alpha=0.5)

        # Mark the first and last points
        plt.scatter(data['Year'].iloc[0], data['Distance (km)'].iloc[0], color='#003d99', s=20, zorder=5)
        plt.scatter(data['Year'].iloc[-1], data['Distance (km)'].iloc[-1], color='#003d99', s=20, zorder=5)

        # Annotate the first point with 'Year'
        plt.annotate(text=str(data['Year'].iloc[0]),
                     xy=(data['Year'].iloc[0], data['Distance (km)'].iloc[0]),
                     xytext=(-6, -4), textcoords='offset points',
                     ha='right', va='bottom', fontsize=8, color='#000a1a', weight='bold')

        # Annotate the last point with 'Year'
        plt.annotate(text=str(data['Year'].iloc[-1]),
                     xy=(data['Year'].iloc[-1], data['Distance (km)'].iloc[-1]),
                     xytext=(27, 3), textcoords='offset points',
                     ha='right', va='bottom', fontsize=8, color='#000a1a', weight='bold')

        # Plot forecasted values
        forecast_years = np.arange(data['Year'].iloc[-1] + 1, data['Year'].iloc[-1] + 1 + forecast_steps)
        plt.plot(forecast_years, forecast, label='Forecast', color='#ffd11a', linestyle='--', linewidth=2)

        # result.plot()
        plt.xlabel('Year', **o_font, fontsize=14, color='#262626', labelpad=10)
        plt.ylabel('Stage Distance (km)', **o_font, fontsize=14, color='#262626', labelpad=10)
        plt.xticks()
        plt.title('Time Series Forecasting of Stage Distances', **o_font, fontsize=20, color='#262626')

        # Legend
        plt.legend(loc='upper left', fontsize=12)

    # Plot seasonal decomposition
    if seasonal_decomposition:
        plot_seasonal_decomp(data, period=10)

    plt.tight_layout(pad=1.4)
    plt.show()
