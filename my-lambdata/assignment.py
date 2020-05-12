# State abbreviateion  --> Full Name and vice verse. FL -> Florida, etc

from pandas import DataFrame #class


class MyFrame(DataFrame):

    def add_state_names(self): #add_state_names = function; my_df = is the object
        """
        Adds a column of state names to accompany a corresponding column of state abbreviation.
        """
        names_map = {"CA": "California", "CO": "Colorado", "CT": "Connecticut", "DC": "Washington DC", "TX": "Texas"}
        self["name"] = self["abbrev"].map(names_map)
        # see:https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.map.html
        

if __name__ == "__main__":

    my_frame = MyFrame({"abbrev": ["CA", "CO", "CT", "DC", "TX"]})
    print(my_frame.columns)
    print(my_frame.head())

    my_frame.add_state_names()
    print(my_frame.df.head())

   