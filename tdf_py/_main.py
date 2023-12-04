from func_imports import *

# Tour De France Files
stages = "https://raw.githubusercontent.com/googs0/TourDeFranceStagesAnalysis/main/assets/csv/historical_stages_TDF.csv"
filename_1 = "historical_stages_TDF.csv"

historical = "https://raw.githubusercontent.com/googs0/TourDeFranceStagesAnalysis/main/assets/csv/historical_TDF.csv"
filename_2 = "historical_TDF.csv"

modern = "https://raw.githubusercontent.com/googs0/TourDeFranceStagesAnalysis/main/assets/csv/modern_TDF.csv"
filename_3 = "modern_TDF.csv"

# Put your Opencage api key
opencage_api_key = ''


def main():
    # Download and process data for each set
    stages_data = download_and_process_csv(stages, filename_1)
    historical_data = download_and_process_csv(historical, filename_2)
    modern_data = download_and_process_csv(modern, filename_3)

    if stages_data.empty or historical_data.empty or modern_data.empty:
        logging.error("Error: One or more DataFrames is empty.")

    else:
        logging.info(f"Dataframes before concatenation:\nmodern_data columns: {modern_data.columns}"
                     f"\nhistorical_data columns: {historical_data.columns}\n")

        # Concatenate Modern and Historic CSV files into a tdf_modern_and_historic df
        tdf_modern_and_historic = pd.concat([historical_data, modern_data], axis=0, ignore_index=True)
        logging.info(f"Concatenated Data Tail Sample\n{tdf_modern_and_historic.tail(10)}\n\n")

        # Clean tdf_modern_and_historic
        cleaned_historical_modern = clean_data_historical_modern(tdf_modern_and_historic)

        # Clean stages_data (3rd file)
        logging.info(f"stages_data columns: {stages_data.columns}\n")
        cleaned_stages = clean_data_stages(stages_data)

        # Opencage geo plot
        aggregate_and_plot(cleaned_stages, api_key=opencage_api_key)

        # Long short-term memory neural
        lstm_forecasting(cleaned_historical_modern)

        # Winner Country Predictions
        result = winner_country_prediction(cleaned_stages)
        logging.info(result)

        # Winning class distribution and Accuracy over time
        plot_winning_class_distribution(cleaned_stages, result['model'])
        plot_accuracy_over_time(cleaned_stages, result['model'])

        # Time series analysis and forecasting
        time_series_analysis(cleaned_historical_modern)
        time_series_forecasting(cleaned_historical_modern)

        # Arima
        arima_results = arima_forecasting(cleaned_stages)
        plot_arima_results(arima_results)

        # Clustering
        clustering_analysis(cleaned_stages)

        # F-stat, t-stat, p-value
        hypothesis_testing(cleaned_historical_modern)


if __name__ == "__main__":
    main()
