from imports import accuracy_score, plt


def plot_accuracy_over_time(data, model):
    # Extract relevant features
    features = data[['Year', 'Distance (km)', 'Stage Type']]

    # Calculate accuracy for each year
    accuracy_over_time = data.groupby('Year').apply(
        lambda x: accuracy_score(x['Country'], model.predict(x[features.columns])))

    # Calculate the average accuracy
    avg_accuracy = accuracy_over_time.mean()

    # Plot
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 8), gridspec_kw={'width_ratios': [3, 1]})
    ax1.plot(accuracy_over_time.index, accuracy_over_time, marker='o', color='royalblue', label='Accuracy')

    # Plotting the average accuracy as a horizontal line
    ax1.axhline(y=avg_accuracy, color='tomato', linestyle='--', label=f'Average Accuracy: {avg_accuracy:.2f}',
                linewidth=3, alpha=0.7)

    # Readability
    ax1.set_title('Accuracy Over Time', fontsize=16, weight='bold')
    ax1.set_xlabel('Year', fontsize=14, weight='bold')
    ax1.set_ylabel('Accuracy', fontsize=14, weight='bold')
    ax1.legend()

    # Adding a bar plot for average accuracy
    ax2.bar('Average Accuracy', avg_accuracy, color='royalblue', alpha=0.9, label='Average Accuracy')
    ax2.set_ylabel('Accuracy', weight='bold')
    ax2.set_title('Average Accuracy', weight='bold')

    # Adjust layout to minimize whitespace
    plt.tight_layout()

    plt.show()
