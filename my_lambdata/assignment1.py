import pandas as pd 
from pandas import DataFrame 



class WrangledFrame(DataFrame):
    """
    A custom pandas.DataFrame with a column called "abbrev"

    Example: WrangledFrame({"abbrev": ["CA", "CO", "CT", "DC", "TX"]})
    """
    def add_state_names(self):

        """
        Converts a dataframe with a column of state abbreviations, adding a
        corresponding

        H/T: https://pandas.pydata.org/pandas-docs/stables/reference/api/pandas.Series.map.html
        """

        names_map = {"CA": "California", "CO": "Colorado",
                     "CT": "Connecticut", "DC": "District of Columbia"}

        self["name"] = self["abbrev"].map(names_map)

    def inspect_columns(self):
        print(self.columns)

    
if __name__ == "__main__":
    # only run following code when we run this script
    # from the command-line
    # otherwise don't invoke this code(for example when importing from another
    # file)
    #df = DataFrame({"abbrev": ["CA", "CO", "CT", "DC", "TX"]})
    #print(df.head())

    #wrangler = Wrangler(df)
    #print(type(wrangler))
    #wrangler.inspect_columns()
    #df2 = wrangler.add_state_names()
    #print(df2.head())
    #wrangler.add_state_names()
    #print(wrangler.
    wf = WrangledFrame({"abbrev": ["CA", "CO", "CT", "DC", "TX"]})
    print(wf.head)
    wf.add_state_names()
    print(wf.head())
    wf.inspect_columns()