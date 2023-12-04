from imports import Dense, LSTM, MinMaxScaler, mplcursors, np, plt, Sequential


def lstm_forecasting(data, dark_mode=False):
    # Extract relevant columns and normalize data
    time_series_data = data[['Year', 'Distance (km)']]
    scaler = MinMaxScaler()
    scaled_data = scaler.fit_transform(time_series_data['Distance (km)'].values.reshape(-1, 1))

    # Define the sequence length for LSTM
    sequence_length = 50  # You can adjust this based on your data

    # Create sequences for training
    sequences = []
    targets = []
    for i in range(len(scaled_data) - sequence_length):
        sequences.append(scaled_data[i:i + sequence_length])
        targets.append(scaled_data[i + sequence_length])

    sequences = np.array(sequences)
    targets = np.array(targets)

    # Split the data into training and testing sets
    split_index = int(0.8 * len(sequences))
    train_sequences, test_sequences = sequences[:split_index], sequences[split_index:]
    train_targets, test_targets = targets[:split_index], targets[split_index:]

    # Build the LSTM model
    model = Sequential()
    model.add(LSTM(50, input_shape=(sequence_length, 1)))
    model.add(Dense(1))
    model.compile(optimizer='adam', loss='mean_squared_error')

    # Train the model
    model.fit(train_sequences, train_targets, epochs=100, batch_size=16, verbose=2)

    # Make predictions on the test set
    predictions = model.predict(test_sequences)

    # Inverse transform the predictions and targets to the original scale
    predictions = scaler.inverse_transform(predictions)
    test_targets = scaler.inverse_transform(test_targets.reshape(-1, 1))

    if dark_mode:
        plt.figure(figsize=(14, 8), facecolor='#1A1A1A')
        ax = plt.axes()

        # Plot lines for actual distances and LSTM forecast
        plt.plot(time_series_data['Year'].values[split_index + sequence_length:], test_targets, label='Actual Distance',
                 linewidth=3, color='#99ddff', alpha=0.8)
        plt.plot(time_series_data['Year'].values[split_index + sequence_length:], predictions, label='LSTM Forecast',
                 color='tomato', linewidth=3, alpha=0.8)

        # Scatter plot to put points on lines
        plt.scatter(time_series_data['Year'].values[split_index + sequence_length:],
                    test_targets, color='dodgerblue', s=40)
        plt.scatter(time_series_data['Year'].values[split_index + sequence_length:],
                    predictions, color='#e60073', s=40)

        # Styling for dark mode
        ax.tick_params(colors='snow')
        ticks = ax.get_xticks()
        ax.set_xticks(ticks)
        ax.set_xticklabels(ax.get_xticklabels(), weight='bold', fontsize=12, color='snow')
        ticks_y = ax.get_yticks()
        ax.set_yticks(ticks_y)
        ax.set_yticklabels(ax.get_yticklabels(), color='snow')
        ax.set_facecolor('#262626')

        # Readability
        plt.title('LSTM Forecasting: Actual vs Predicted Stage Distance', fontsize=16, weight='bold', color='snow')
        plt.xlabel('Year', color='snow', fontsize=14, weight='bold')
        plt.ylabel('Stage Distance (km)', color='snow', fontsize=14, weight='bold')

        # Grid
        plt.grid(markeredgecolor='black', alpha=0.5, linestyle='--')

        # Legend
        plt.legend(loc='upper left', fontsize=12, framealpha=0.7)

    else:
        # Plot
        plt.figure(figsize=(14, 8), facecolor='whitesmoke')

        # Line plot
        plt.plot(time_series_data['Year'].values[split_index + sequence_length:], test_targets,
                 label='Actual Distance', linewidth=3, color='cornflowerblue', alpha=0.8)
        plt.plot(time_series_data['Year'].values[split_index + sequence_length:], predictions,
                 label='LSTM Forecast', color='tomato', linewidth=3, alpha=0.8)

        # Scatter plot to put points on lines
        plt.scatter(time_series_data['Year'].values[split_index + sequence_length:],
                    test_targets, color='#1a1aff', s=40)
        plt.scatter(time_series_data['Year'].values[split_index + sequence_length:],
                    predictions, color='#e60073', s=40)

        # Readability
        plt.title('LSTM Forecasting: Actual vs Predicted Stage Distance', fontsize=16, weight='bold')
        plt.xlabel('Year', fontsize=14, weight='bold')
        plt.ylabel('Stage Distance (km)', fontsize=14, weight='bold')

        # Grid
        plt.grid(markeredgecolor='black', alpha=0.7, linestyle='--')

        # Legend
        plt.legend(loc='upper left', fontsize=12, framealpha=0.7)

    # Hover over values with cursor
    cursor = mplcursors.cursor(hover=True)

    def on_plot_hover(sel):
        sel.annotation.set_text(f"Year: {sel.target[0]:.0f}\nDistance: {sel.target[1]:.2f} km")
    cursor.connect("add", on_plot_hover)

    plt.tight_layout()
    plt.show()
