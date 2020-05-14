#assignment_inheritance.py

from pandas import DataFrame

class MyFrame(DataFrame): #writing a class that inherits from the DataFrame class
    # most classes do not have an argument passing through

    def add_state_names(self): #adding methods to the DataFrame class
        """
        Adds a column of state names to accompany a corresponding column of state abbreviation.
        """
        names_map = {"CA": "California", "CO": "Colorado", "CT": "Connecticut", "DC": "Washington DC", "TX": "Texas"}
        self["name"] = self["abbrev"].map(names_map) 
        # see: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.map.html

if __name__ == "__main__":

    #df = DataFrame({"abbrev":["CA","CO","CT","DC","TX"]})

    my_frame = MyFrame({"abbrev":["CA","CO","CT","DC","TX"]})
    print(my_frame.columns) #invoking DataFrame methods on self
    print(my_frame.head())

    my_frame.add_state_names()
    print(my_frame.head())