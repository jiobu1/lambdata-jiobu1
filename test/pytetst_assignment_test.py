#pytest

from pandas import DataFrame

from my_lambdata.assignment import add_state_names

#OBJECTIVE:

def test_add_state_names():
    
    df = DataFrame({"abbrev":["CA","CO","CT","DC","TX"]})
    assert list(df.columns) == ['abbrev']

    result = df #add_state_names(df)

    assert list(result.columns) == ['abbrev', 'name']
    assert result.iloc[0]['abbrev'] == 'CA'
    assert result.iloc[0]['name'] == 'California'