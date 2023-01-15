"""Project pipelines."""
from typing import Dict

from kedro.pipeline import Pipeline

from simple_kedro_pipeline.pipelines.retrieve_split_save_data.pipeline import create_pipeline as s1


def register_pipelines() -> Dict[str, Pipeline]:
    """Register the project's pipelines.

    Returns:
        A mapping from pipeline names to ``Pipeline`` objects.
    """
    step1 = s1()
    return {"__default__": step1}
