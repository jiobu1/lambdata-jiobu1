# State abbreviateion  --> Full Name and vice verse. FL -> Florida, etc

from pandas import DataFrame



def add_state_names(my_df):
    #TODO: add a column of correstponding state names
    #dict with abbrev/name.mappingsc
    #create a new columns that is a copy of the first. but mapped with names
    #concat with axis=1

    new_df = my_df.copy()
    
    names_map = {"CA":"California", "CO":"Colorado", "CT":"Connecticut"}
     
    # type(my_df["abbrev"]) #> class 'pandas.core.series.Series

    new_df["name"] = new_df["abbrev"].map(names_map)
    # see: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.map.html
     
    return my_df



if __name__ == "__main__":

    df = DataFrame({"abbrev":["CA","CO","CT","DC","TX"]})
    print(df.head())
    
    df2 = add_state_names(df)
    print(df2.head())