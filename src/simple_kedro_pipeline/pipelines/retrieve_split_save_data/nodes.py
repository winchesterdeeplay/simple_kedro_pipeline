import pandas as pd
from typing import Dict, List, Union
from dynamo_pandas import put_df


def _retrieve_targets(columns: Union[List[int], List[str]], source: pd.DataFrame) -> pd.DataFrame:
    if all(isinstance(column, str) for column in source):
        target = source[columns]
    elif all(isinstance(column, int) for column in source):
        target = source.iloc[:, columns]
    else:
        raise Exception("Don't mix column indexes and column names")
    return target


def split_table(
    dataset: pd.DataFrame,
    first_table_column_indexes: Union[List[int], List[str]],
    second_table_column_indexes: Union[List[int], List[str]],
) -> Dict[str, pd.DataFrame]:
    target_1 = _retrieve_targets(first_table_column_indexes, dataset)
    target_2 = _retrieve_targets(second_table_column_indexes, dataset)
    return dict(target_1=target_1, target_2=target_2)


def save_targets(target_1: pd.DataFrame, target_2: pd.DataFrame, target_table_name_1: str, target_table_name_2) -> None:
    put_df(target_1, table=target_table_name_1)
    put_df(target_2, table=target_table_name_2)
