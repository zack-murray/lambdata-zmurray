import pandas as pd
from pandas import DataFrame

# Turn list into series then add it as a new column to the dataframe
# df = dataframe, l = list, col_name = column name


def flto_nc(df, l, col_name):
    df[col_name] = l

# Split date into multiple columns
# X = dataframe, column_name = self explanatory


def split_column_date(X, column_name):
    X[column_name] = pd.to_datetime(X[column_name])
    X[column_name + '_year'] = X[column_name].dt.year
    X[column_name + '_month'] = X[column_name].dt.month
    X[column_name + '_day'] = X[column_name].dt.day
    X[column_name] = X[column_name].dt.strftime('%Y-%m-%d')
    return X

# Convert state abbreviations to full names
# FL -> Florida, etc.


def add_state_names(my_df):

    """
    Converts a dataframe with a column of state abbreviations, adding a
    corresponding

    Params: my_df a pandas.DataFrame with a column called "abbrev".

    Example: add_state_names(DataFrame({"abbrev":["CA", "CO", "CT",
    "DC", "TX"]})

    Returns: a pandas.DataFrame with the original col as well as a
    "name" column.
    """

    new_frame = my_df.copy()

    # need a list with abbrev/name mappings
    names_map = {"CA": "California", "CO": "Colorado",
                 "CT": "Connecticut", "DC": "District of Columbia"}

    # create a new column which maps the existing column using our names map

    # create breakpoint
    # breakpoint()

    new_frame["name"] = new_frame["abbrev"].map(names_map)

    return new_frame

if __name__ == "__main__":
    # only run following code when we run this script
    # from the command-line
    # otherwise don't invoke this code(for example when importing from another
    # file)
    df = DataFrame({"abbrev": ["CA", "CO", "CT", "DC", "TX"]})
    print(df.head())

    df2 = add_state_names(df)
    print(df2.head())
