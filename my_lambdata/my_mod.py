import pandas as pd
from pandas import DataFrame


class Alterdata():
    def __init__(self, df):
        """
        Class constructor for Alterdata

        This class is designed to take a given DataFrame
        and modify it for further research

        Params: df a pandas.Dataframe that will be modified.

        Example: df2 = my_mod.Alterdata(df)
        """
        self.df = df.copy()

    def return_dataframe(self):
        """
        Use with regards to Alterdata. Takes the modified dataframe
        out of the data alterer

        Returns: a pandas Dataframe as stored in the modifier
        """
        return self.df

    def flto_nc(self, l, col_name):

        """
        Turns a list into a series, then adds it as a new column to the
        end of the Dataframe

        Params: l a list that you want to transform into a series
                col_name the name given to your list converted column

        Example: flto_nc(df, l, 'nameoflist')

        Returns: a pandas.Dataframe with a new named column that incorporates
                 the list passed through.

        """
        self.df[col_name] = l

    def split_column_date(self, df, column_name):

        """
        Splits a date column into multiple columns given in respect to the
        given year-month-day given

        Params: df a pandas.Dataframe that includes a dated column
                column_name a column in the Dataframe with an implied date

        Example: X2 = split_column_date(X, 'First game won')

        Returns: a pandas.Dataframe with the original column, as well as
                1-3 new columns depending on the date split

        """
        df[column_name] = pd.to_datetime(df[column_name])
        df[column_name + '_year'] = df[column_name].dt.year
        df[column_name + '_month'] = df[column_name].dt.month
        df[column_name + '_day'] = df[column_name].dt.day
        df[column_name] = df[column_name].dt.strftime('%Y-%m-%d')
        return self.df

    def add_state_names(self, my_df):

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

        # create new column which maps the existing column using our names map

        # create breakpoint
        # breakpoint()

        new_frame["name"] = new_frame["abbrev"].map(names_map)

        return new_frame

# if __name__ == "__main__":
    # only run following code when we run this script
    # from the command-line
    # otherwise don't invoke this code(for example when importing from another
    # file)
    # df = DataFrame({"abbrev": ["CA", "CO", "CT", "DC", "TX"]})
    # print(df.head())

    # df2 = add_state_names(df)
    # print(df2.head())
