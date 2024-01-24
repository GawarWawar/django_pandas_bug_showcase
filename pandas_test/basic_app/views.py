from django.http import HttpResponse

import pandas as pd
import numpy as np
import random

# Create your views here.

def test_simple_raise_KeyError (request):
    """
    Test function to intentionally raises a KeyError without Pandas for error handling testing.
    """
    raise KeyError("Just a random KeyError without Pandas here. Django works fine")

def create_basic_dataframe():
    """
    Creates a basic Pandas DataFrame with three columns, each containing 100 random integers between 1 and 100.

    Returns:
    pandas.DataFrame: A DataFrame with the following columns:
        - column_0: Contains 100 random integers between 1 and 100.
        - column_1: Contains 100 random integers between 1 and 100.
        - column_2: Contains 100 random integers between 1 and 100.
    """
    column_0 = [random.randint(1, 100) for _ in range(100)]
    column_1 = [random.randint(1, 100) for _ in range(100)]
    column_2 = [random.randint(1, 100) for _ in range(100)]
    
    df = pd.DataFrame(
        {
            'column_0':column_0,
            'column_1':column_1,
            'column_2':column_2,
        }
    )
    
    return df

def test_show_dataframe(request):
    """
    Test function to check if the DataFrame is created successfully without any issues.
    """
    df = create_basic_dataframe()
    
    return HttpResponse(df.to_json(indent=2))

def test_catch_KeyError_with_using_pandas(request):
    """
    Test function to catch and handle a KeyError when attempting to access a non-existing column.
    """
    df = create_basic_dataframe()
    try:
        not_existing_element = df.loc[:, "column_3"]
    except KeyError as KE:
        message = f"We found  that calling {KE} caused KeyError and prevented it with try-exept structure. However, if we raise KeyError here it will also cause a bug"
    
    return HttpResponse(message)

def recreate_bug_with_raise_error_after_catching_KeyError(request):
    """
    Test function to catch and then raise again a KeyError when attempting to access a non-existing column.
    """
    df = create_basic_dataframe()
    try:
        not_existing_element = df.loc[:, "column_3"]
    except KeyError as KE:
        raise (f"We found  that calling caused KeyError and prevented it with try-exept structure. However, if we raise KeyError here it will also cause a bug")

def recreate_bug(request):
    """
    Test function intentionally causing a KeyError by accessing a non-existing column.
    """
    df = create_basic_dataframe()
    
    not_existing_element = df.loc[:, "column_3"]
    
    return HttpResponse(df.to_json(indent=2))

def recreate_bug_without_loc(request):
    """
    Test function intentionally causing a KeyError by accessing a non-existing column.
    """
    df = create_basic_dataframe()
    
    not_existing_element = df["column_3"]
    
    return HttpResponse(df.to_json(indent=2))