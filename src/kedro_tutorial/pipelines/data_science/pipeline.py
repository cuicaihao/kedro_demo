
from kedro.pipeline import node, Pipeline
from kedro_tutorial.pipelines.data_science.nodes import (
    split_data,
    train_model,
    evaluate_model,
)


def create_pipeline(**kwargs):
    """Create the data science pipeline.

    Args:
        kwargs: Ignore any additional arguments added in the future.

    Returns:
        A mapping from a pipeline name to a ``Pipeline`` object.

    """
    return Pipeline(
        [
            node(
                func=split_data,
                inputs=["master_table", "params:test_size",
                        "params:random_state"],
                outputs=["X_train", "X_test", "y_train", "y_test"],
            ),
            node(func=train_model, inputs=[
                 "X_train", "y_train"], outputs="regressor", tags=["regressor-node"]),
            node(
                func=evaluate_model,
                inputs=["regressor", "X_test", "y_test"],
                outputs=None,
            ),
        ],
        tags=["ds_tag"]
    )
