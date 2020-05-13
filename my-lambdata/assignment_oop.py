#assignment_oop.py

from pandas import DataFrame #class

class DataProcessor ():
    def __init__(self, my_df):
        """
         Params:
            my_df (pandas.DataFrame) has a column called "abbrev" with state abbreviations.
        """
        self.df = my_df

    def add_state_names(self): #add_state_names = function; my_df = is the object
        """
        Adds a column of state names to accompany a corresponding column of state abbreviation.

        Returns:
        copy of the orginal dataframe, with another column
        """
        names_map = {"CA": "California", "CO": "Colorado", "CT": "Connecticut", "DC": "Washington DC", "TX": "Texas"}
        self.df["name"] = self.df["abbrev"].map(names_map)
        # see:
        # https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.map.html
        return self.df


if __name__ == "__main__":
    df = DataFrame({"abbrev":["CA","CO","CT","DC","TX"]})

    processor = DataProcessor(df)
    print(processor.df.head())
    
    processor.add_state_names()
    print(processor.df.head())

