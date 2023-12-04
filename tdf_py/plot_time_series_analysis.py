from imports import plt, sns


def dark_mode_time_series_analysis(data):
    # Time Series Plot for Stage Distances
    plt.figure(figsize=(14, 8), facecolor='#333333', edgecolor='black')
    o_font = {'fontname': 'Open Sans'}

    ax = plt.axes()
    ax.set_facecolor('#262626')
    ax.grid(color='#595959', linestyle='--', linewidth=0.5)
    ax.tick_params(colors='#f2f5f5')

    # Use the entire 'Spectral' palette for the standard deviation line
    palette = sns.color_palette('Spectral', n_colors=12)

    # Iterate through each segment of the standard deviation and fill with a gradient color
    for i in range(len(data) - 1):
        plt.fill_between(data['Year'].iloc[i:i + 2],
                         data['Distance (km)'].iloc[i:i + 2] - data['Distance (km)'].std(),
                         data['Distance (km)'].iloc[i:i + 2] + data['Distance (km)'].std(),
                         color=palette[i % len(palette)], alpha=0.5)

    # Plot the main line
    sns.lineplot(data=data, x='Year', y='Distance (km)', linewidth=2, color='#99ccff')

    # Mark the first and last points with circle markers
    plt.scatter(data['Year'].iloc[0], data['Distance (km)'].iloc[0], color='tomato', s=50, zorder=5)
    plt.scatter(data['Year'].iloc[-1], data['Distance (km)'].iloc[-1], color='tomato', s=50, zorder=5)

    # Annotate the first point with 'Year'
    plt.annotate(text=str(data['Year'].iloc[0]),
                 xy=(data['Year'].iloc[0], data['Distance (km)'].iloc[0]),
                 xytext=(-8, -10), textcoords='offset points',
                 ha='right', va='bottom', fontsize=12, color='#80b3ff', weight='bold')

    # Annotate the last point with 'Year'
    plt.annotate(text=str(data['Year'].iloc[-1]),
                 xy=(data['Year'].iloc[-1], data['Distance (km)'].iloc[-1]),
                 xytext=(40, -7), textcoords='offset points',
                 ha='right', va='bottom', fontsize=12, color='#80b3ff', weight='bold')

    plt.title('Time Series Analysis of Stage Distances', **o_font, fontsize=20, color='#cccccc')
    plt.xlabel('Year', **o_font, fontsize=14, color='#cccccc', labelpad=10)
    plt.ylabel('Stage Distance (km)', **o_font, fontsize=14, color='#cccccc', labelpad=10)
    plt.xticks(rotation=45)

    plt.tight_layout(pad=1.4)
    plt.show()


# Time Series Analysis (Place this section after preprocessing data)
def time_series_analysis(data, dark_mode=True):
    if dark_mode:
        dark_mode_time_series_analysis(data)
    else:
        # Time Series Plot for Stage Distances
        plt.figure(figsize=(14, 8), facecolor='#f2f2f2', edgecolor='#262626')
        o_font = {'fontname': 'Arial'}

        ax = plt.axes()
        ax.set_facecolor('#f2f2f2')
        ax.grid(color='#595959', linestyle='--', linewidth=0.5, alpha=0.5)
        ax.tick_params(colors='#262626')

        # Use the entire 'Spectral' palette for the standard deviation line
        palette = sns.color_palette('Spectral', n_colors=12)

        # Iterate through each segment of the standard deviation and fill with a gradient color
        for i in range(len(data) - 1):
            plt.fill_between(data['Year'].iloc[i:i + 2],
                             data['Distance (km)'].iloc[i:i + 2] - data['Distance (km)'].std(),
                             data['Distance (km)'].iloc[i:i + 2] + data['Distance (km)'].std(),
                             color=palette[i % len(palette)], alpha=0.5)

        # Plot
        sns.lineplot(data=data, x='Year', y='Distance (km)', linewidth=2, color='#0080ff')

        # Mark the first and last points with circle markers
        plt.scatter(data['Year'].iloc[0], data['Distance (km)'].iloc[0], color='#ff0066', s=50, zorder=5)
        plt.scatter(data['Year'].iloc[-1], data['Distance (km)'].iloc[-1], color='#ff0066', s=50, zorder=5)

        # Annotate the first point with 'Year'
        plt.annotate(text=str(data['Year'].iloc[0]),
                     xy=(data['Year'].iloc[0], data['Distance (km)'].iloc[0]),
                     xytext=(-6, -9), textcoords='offset points',
                     ha='right', va='bottom', fontsize=12, color='#000a1a', weight='bold')

        # Annotate the last point with 'Year'
        plt.annotate(text=str(data['Year'].iloc[-1]),
                     xy=(data['Year'].iloc[-1], data['Distance (km)'].iloc[-1]),
                     xytext=(39, -7), textcoords='offset points',
                     ha='right', va='bottom', fontsize=12, color='#000a1a', weight='bold')

        plt.title('Time Series Analysis of Stage Distances', **o_font, fontsize=20, color='#262626')
        plt.xlabel('Year', **o_font, fontsize=14, color='#262626', labelpad=10)
        plt.ylabel('Stage Distance (km)', **o_font, fontsize=14, color='#262626', labelpad=10)
        plt.xticks(rotation=45)

        plt.tight_layout(pad=1.4)
        plt.show()
