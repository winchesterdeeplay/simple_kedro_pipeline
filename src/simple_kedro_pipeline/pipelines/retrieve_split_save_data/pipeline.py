from kedro.pipeline import Pipeline, node
from .nodes import split_table, save_targets


def create_pipeline(**kwargs):
    return Pipeline(
        [
            node(
                func=lambda x: x,
                inputs="postgres_table_dataset",
                outputs="local_postgres_table_dataset",
                name="load_postgres_table_dataset",
            ),
            node(
                func=split_table,
                inputs=dict(
                    dataset="local_postgres_table_dataset",
                    first_table_column_indexes="params:targets_columns_1",
                    second_table_column_indexes="params:targets_columns_2",
                ),
                outputs=dict(target_1="target_1", target_2="target_2"),
            ),
            node(
                func=save_targets,
                inputs=dict(
                    target_1="target_1",
                    target_2="target_2",
                    target_table_name_1="params:aws_table_name_1",
                    target_table_name_2="params:aws_table_name_2",
                ),
                outputs=None,
            ),
        ]
    )
