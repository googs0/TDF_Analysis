from imports import mplcursors, plt, sns


def dark_mode_winning_class_distribution(data, model):
    # Extract relevant columns
    features = data[['Year', 'Distance (km)', 'Stage Type']]
    target = data['Country']

    # Make predictions on the entire dataset
    y_pred = model.predict(features)
    # Class Distribution
    plt.figure(figsize=(16, 8), facecolor='#1a1a1a', edgecolor='black')

    # Set custom hatch patterns for better distinction
    hatch_predicted = ['////', '\\\\\\']
    hatch_actual = ['']

    # Plot predicted class distribution
    sns.countplot(x=y_pred, palette='viridis', hue=y_pred, label='Predicted', hatch=hatch_predicted,
                  edgecolor='black', linewidth=0.5)

    # Plot actual class distribution
    ax = sns.countplot(x=target, palette='turbo_r', hue=target, label='Actual', hatch=hatch_actual,
                       edgecolor='black', alpha=0.7, linewidth=0.5)

    # Rotate x-axis labels for better readability
    ticks = ax.get_xticks()
    ax.set_xticks(ticks)
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right', weight='bold', fontsize=12, color='#e6e6e6')
    ticks_y = ax.get_yticks()
    ax.set_yticks(ticks_y)
    ax.set_yticklabels(ax.get_yticklabels(), color='#e6e6e6')
    ax.set_facecolor('#404040')

    plt.xlabel('Countries', color='#e6e6e6', labelpad=10, fontsize=14)
    plt.ylabel('Frequency', color='#e6e6e6', labelpad=10, fontsize=14)

    plt.title('Actual vs Predicted Class Distribution', weight='bold', color='#e6e6e6', fontsize=16)
    plt.title('**Pattern = Predicted', weight='bold', loc='right', fontsize=10, color='#8c8c8c')


def plot_winning_class_distribution(data, model, scale_factor=1, dark_mode=True):
    # Extract relevant columns
    features = data[['Year', 'Distance (km)', 'Stage Type']]
    target = data['Country']

    # Make predictions on the entire dataset
    y_pred = model.predict(features)

    if dark_mode:
        dark_mode_winning_class_distribution(data, model)
    else:
        # Class Distribution
        plt.figure(figsize=(16, 8), facecolor='#d9d9d9', edgecolor='black')

        # Set custom hatch patterns for better distinction
        hatch_predicted = ['////', '\\\\\\']
        hatch_actual = ['']

        # Plot predicted class distribution
        sns.countplot(x=y_pred, palette='viridis', hue=y_pred, label='Predicted', hatch=hatch_predicted,
                      edgecolor='black', linewidth=0.5)

        # Plot actual class distribution
        ax = sns.countplot(x=target, palette='turbo_r', hue=target, label='Actual', hatch=hatch_actual,
                           edgecolor='black', alpha=0.7, linewidth=0.5)

        # Rotate x-axis labels for better readability
        ticks = ax.get_xticks()
        ax.set_xticks(ticks)
        ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right', weight='bold', fontsize=12, color='#333333')
        ax.set_facecolor('#f2f2f2')

        # Scale up the entire plot

        plt.xlabel('Countries', color='#333333', labelpad=10, fontsize=14)
        plt.ylabel('Frequency', color='#333333', labelpad=10, fontsize=14)

        plt.title('Actual vs Predicted Class Distribution', weight='bold', color='#333333', fontsize=16)
        plt.title('**Pattern = Predicted', weight='bold', loc='right', fontsize=10, color='#777777')

    plt.ylim(top=plt.ylim()[1] * scale_factor)

    # Add mplcursors for interactive hover information
    mplcursors.cursor(hover=True)
    # Remove top and right spines
    sns.despine()

    plt.tight_layout()
    plt.show()
