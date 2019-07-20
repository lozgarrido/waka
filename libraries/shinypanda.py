import pandas as pd
import numpy as np

def wipe_empty_columns(df, max_empty=0.7, exceptions=[]):
    """
    Removes columns with too many empty values from a dataframe

    Args:
        df: Dataframe to clean
        max_empty: the minimum percentage of valid values in a column (by default, 70%)
        exceptions: list of names of columns that should not be deleted

    Returns:
        df: The cleaned dataframe
    """

    # Convert empty strings into NaN
    df = df.replace(r'^\s+$', np.nan, regex=True)

    columns = list(df)
    rows = len(df)

    for column_name in columns:
        if column_name in exceptions:
            pass
        else:
            # Find NaN percentage
            nan_percentage = (df[column_name].isna().sum() / rows)
            if nan_percentage < max_empty:
                pass
            else:
                del df[column_name]

    return df

