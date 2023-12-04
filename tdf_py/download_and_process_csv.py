from imports import logging, pd, requests


def download_and_process_csv(url, local_filename):
    try:
        response = requests.get(url)
        response.raise_for_status()

        with open(local_filename, 'wb') as file:
            file.write(response.content)
            logging.info(f"File '{local_filename}' downloaded successfully.\n")

        data = pd.read_csv(local_filename)
        return data

    except requests.exceptions.RequestException as req_err:
        logging.error(f"An unexpected error occurred during download: {req_err}\n")
        return pd.DataFrame()

    except FileNotFoundError:
        logging.error(f"File not found: {local_filename}\n")
        return pd.DataFrame()

    except pd.errors.EmptyDataError:
        logging.error("The dataset is empty. Please check the data source.\n")
        return pd.DataFrame()

    except pd.errors.ParserError as pe:
        logging.error(f"Error parsing the CSV file: {pe}\n")
        return pd.DataFrame()

    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}\n")
        return pd.DataFrame()
