#assignment.py
# State abbreviateion  --> Full Name and vice verse. FL -> Florida, etc

from pandas import DataFrame #class


def add_state_names(my_df): #add_state_names = function; my_df = is the object
    """
    Adds a column of state names to accompany a corresponding column of state abbreviation.

    Params:
        my_df (pandas.DataFrame) has a column called "abbrev" with state abbreviations.

    Returns:
        copy of the orginal dataframe, with another column
    """
    new_df = my_df.copy()
    names_map = {"CA": "California", "CO": "Colorado", "CT": "Connecticut", "DC": "Washington DC", "TX": "Texas"}
    new_df["name"] = new_df["abbrev"].map(names_map)
    # see:
    # https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.map.html
    return new_df


if __name__ == "__main__":

    df = DataFrame({"abbrev": ["CA", "CO", "CT", "DC", "TX"]})
    #breakpoint()
    print(df.columns) #property
    print(df.head()) #method

    df2 = add_state_names(df)
    print(df2.head())

    # df3 = DataFrame({"a": [1, 2, 3, 4]})
    # print(df3.head())