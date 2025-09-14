import pandas as pd


def load_from_file(file_path: str) -> pd.DataFrame:
    """Load a CSV file into a pandas DataFrame."""
    try:
        # Load data
        population_df = pd.read_csv(file_path)

        # Check if the DataFrame is empty
        if population_df.empty:
            raise ValueError(f"The file exists but contains no data: {file_path}") from None

        return population_df

    except FileNotFoundError as e:
        raise FileNotFoundError(f"File not found. {file_path}") from e
