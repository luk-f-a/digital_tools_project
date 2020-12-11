"""
Module for handling data in the project. It will use a full database API
even though it will be based on text files, in case it had to be upgraded to
SQL. For example, it will have a dummy connection object.
"""

import os
import pandas as pd


def get_connection():
    return None


def get_simulations(stock_name: str) -> pd.DataFrame:
    folder = os.path.expandvars("$DT4F_PROJECT/data")
    assert os.path.exists(folder)
    filepath = os.path.join(folder, stock_name + ".parquet")
    if os.path.exists(filepath):
        return pd.read_parquet(filepath)
    else:
        raise ValueError(f"Stock {stock_name} is not in the database")


def insert_simulations(stock_name:str, simulations: pd.DataFrame) -> None:
    folder = os.path.expandvars("$DT4F_PROJECT/data")
    assert os.path.exists(folder)
    filepath = os.path.join(folder, stock_name + ".parquet")
    if os.path.exists(filepath):
        current_data = pd.read_parquet(filepath)
        new_data = pd.concat(current_data, simulations)
        new_data.to_parquet(filepath)
    else:
        simulations.to_parquet(filepath)


def update_simulations(stock_name: str, simulations: pd.DataFrame) -> None:
    folder = os.path.expandvars("$DT4F_PROJECT/data")
    assert os.path.exists(folder)
    filepath = os.path.join(folder, stock_name + ".parquet")
    if os.path.exists(filepath):
        simulations.to_parquet(filepath)
    else:
        raise ValueError(f"Stock {stock_name} is not in the database")
