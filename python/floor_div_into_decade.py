import pandas as pd


def decades(data, new_col, div_col, num=10):
    """
     Given a dataframe, a new col, a col to use floor division on,
     return a dataframe that has been floor divided from one col and
     create a new col with the results.
    Parameters
    ----------
    data : pandas.core.frame.DataFrame
        The dataframe to use for the study
    new_col : str
        The column to be created with the results from floor dividing
        the div_col
    div_col : str
        The column to floor divide into
    num = int
            The number used as a default = 10 to floor divide the
            div_col by.
    Returns
    -------
    pandas.core.frame.DataFrame
       A dataframe with a new col that has contains the result of floor
       divided the div_col
    Raises
    ------
    TypeError
        If the input argument data is not of type pandas.core.frame.DataFrame
    AssertError
        If the input argument div_col is not in the data columns
    AssertError
        If the num != 10 then an error pops up as it is meant to divide year
        into decades

    Examples
    --------
    helper_data = pd.DataFrame.from_dict(helper_dict)

        i   movie	           year	decades
        0	Batman	           1989	1980
        1	Lord of the Rings  2001	2000
        2	Steel Magnolia	   1989	1980
        3	Barbie	           2023	2020
        4	Oppenhiemer	       2023	2020
    """

    # Checks if a dataframe is type object being passed into the data argument
    if not isinstance(data, pd.DataFrame):
        raise TypeError("The data argument is not of type DataFrame")

    # Tests that the the grouping column is in the dataframe
    assert div_col in data.columns, "The grouping column does not exist"

    # Checks if the num is = 10
    assert num == 10, "Wrong floor division number, must be 10!"

    new_data = data.assign(decades=(data[div_col] // num) * num)

    new_data = pd.DataFrame(new_data)

    new_data = new_data.reset_index()

    return new_data
