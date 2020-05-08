# State abbreviateion  --> Full Name and vice verse. FL -> Florida, etc

from pandas import DataFrame


def add_state_names(my_df):
    """
    Adds a column of state names to accompany a corresponding column of state abbreviation.

    Params:
        my_df (pandas.DataFrame) has a column called "abbrev" with state abbreviations.

    Returns:
        copy of the orginal dataframe, with another column
    """
    new_df = my_df.copy()
    names_map = {"CA": "California", "CO": "Colorado", "CT": "Connecticut"}
    new_df["name"] = new_df["abbrev"].map(names_map)
    # see:
    # https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.map.html
    return my_df


if __name__ == "__main__":

    df = DataFrame({"abbrev": ["CA", "CO", "CT", "DC", "TX"]})
    print(df.head())

    df2 = add_state_names(df)
    print(df2.head())
