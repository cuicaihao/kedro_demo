from kedro.pipeline import node, Pipeline
from kedro_tutorial.pipelines.data_engineering.nodes import (
    preprocess_companies,
    preprocess_shuttles,
    create_master_table,
    log_running_time,
)


def create_pipeline(**kwargs):
    """Create the data engineering  pipeline.

    Args:
        kwargs: Ignore any additional arguments added in the future.

    Returns:
        A mapping from a pipeline name to a ``Pipeline`` object.

    """
    return Pipeline(
        [
            node(
                func=preprocess_companies,
                inputs="companies",
                outputs="preprocessed_companies",
                name="preprocessing_companies",
            ),
            node(
                func=preprocess_shuttles,
                inputs="shuttles",
                outputs="preprocessed_shuttles",
                name="preprocessing_shuttles",
            ),
            node(
                func=create_master_table,
                inputs=["preprocessed_shuttles",
                        "preprocessed_companies", "reviews"],
                outputs="master_table",
                name="master_table",
            ),
        ],
        tags=["de_tag"]
    )
