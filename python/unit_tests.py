helper_dict = {'movie': ['Batman', 'Lord of the Rings', 'Steel Magnolia', 'Barbie', 'Oppenhiemer'],
               'year': [1925, 2001, 1989, 2023, 2023]}

helper_data = pd.DataFrame.from_dict(helper_dict)

def decades(data, new_col, div_col, num=10):

# Checks that the num is = 10
     assert num == 10, "Wrong floor division number, must be 10!"
# Checks if a dataframe is the type of object being passed into the data argument
    if not isinstance(data, pd.DataFrame): 
        raise TypeError("The data argument is not of type DataFrame")
    
# Tests that the the grouping column is in the dataframe
    assert div_col in data.columns, "The grouping column does not exist in the dataframe"


    new_data = data.assign(decades = (data[div_col] // num) * num)
    
    new_data = pd.DataFrame(new_data)
    
    new_data = new_data.reset_index()
    
    return new_data

new_df = decades(helper_data, 'decade', 'year')
new_df

	i	movie	          year	decades
0	0	Batman	          1989	1980
1	1	Lord of the Rings 2001	2000
2	2	Steel Magnolia	  1989	1980
3	3	Barbie	          2023	2020
4	4	Oppenhiemer	      2023	2020


