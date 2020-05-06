# my_script.py

from pandas import DataFrame
# from my_mod import enlarge
from my_mod import enlarge # this works

print('Hello')

df = DataFrame({"a":[1, 2, 3], "b":[4,5,6]})
print(df.head(n=5))

x = 11
print(enlarge(x))