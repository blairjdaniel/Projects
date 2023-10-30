import pandas as pd

def data_grouping(data, grouping_col, action_col, action = 'mean'):
    

   
    """
    Given a dataframe, a column to group, and an action, return a dataframe that has been grouped by the column and the aggregate function applied.
    
    Parameters
    ----------
    
     data : pandas.core.frame.DataFrame
        The dataframe to use for the study
    grouping_col : str
        The column to group the data on
    action_col : str
        After grouping, the column to applying the action to
    action : str, optional
        The action to apply to the specified action_col. The default is the 
        mean action.      
    
    Returns
    -------
    
    pandas.core.frame.DataFrame 
        A dataframe with the group by column and the result of the action applied.
        
    Raises
    ------
    TypeError
        If the input argument data is not of type pandas.core.frame.DataFrame
    AssertError
        If the input argument grouping_col is not in the data columns
    AssertError
        If the input argument action_col is not in the data columns
    
    Examples
    --------
    data_grouping(helper_data, 'type')
    
    helper_dict = {
               'year': ['1930 - 1980','1930 - 1980', "2010's"],
               'total_gross': [5.228953e+09, 2.188229e+09, 2.460820e+08]
               }
    
    helper_data = pd.DataFrame.from_dict(helper_dict)

	type	mean
	        	 
    1930 - 1980  5.228953e+09
    2010's 2.460820e+08	
    
    """
    
    # Checks if a dataframe is the type of object being passed into the data argument
    if not isinstance(data, pd.DataFrame): 
        raise TypeError("The data argument is not of type DataFrame")
    
    # Tests that the the grouping column is in the dataframe
    assert grouping_col in data.columns, "The grouping column does not exist in the dataframe"
    
    # Tests that the the action column is in the dataframe
    assert action_col in data.columns, "The action column does not exist in the dataframe"

    
    # group the grouping_col from the dataframe
    new_data = data.groupby(grouping_col)[action_col].agg([action])
    # new dataframe
    
    new_data = pd.DataFrame(new_data)
    
    # reset the index
    new_data = new_data.reset_index()
       
    return new_data