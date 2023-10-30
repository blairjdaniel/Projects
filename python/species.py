import pandas as pd

def species(data, col, list):
    """ 
    Given a dataframe, a species name, and a column, return a dataframe that has been grouped by the column and the aggregate function applied.

    Parameters
    ----------  
    data : pandas.core.frame.DataFrame
        The dataframe to use for the study
    col: 
        the col being used
    list : str   
        The list of species

    Returns
    -------
        pandas.core.frame.DataFrame 
            A dataframe with the group by column and the result of the action applied.

    Raises
    ------
    TypeError
        If the input argument data is not of type pandas.core.frame.DataFrame
    
    Examples
    --------
    species(data, 'PLATANOIDES', 'species_name')      
    """

    # Checks if a dataframe is the type of object being passed into the data argument
    if not isinstance(data, pd.DataFrame): 
        raise TypeError("The data argument is not of type DataFrame")

    

    

    #Create a df with only the species name
    #species_df = data[data[grouping_col] == species_name]
    species_df = data[data[col].isin([species_name])]
