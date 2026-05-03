"""
GridCells Ontology Module.

Defines the data structure for grid cells.
"""

from mosaicolabs.models import MosaicoField
from mosaicolabs.models.data.geometry import Point2d
from mosaicolabs.models.types import MosaicoType

from ..serializable import Serializable


class GridCells(Serializable):
    """
    Grid Cells data.

    This class represents the grid cells.

    Attributes:
        cell_width: A `MosaicoType.float32` that represents the width of each cell.
        cell_height: A `MosaicoType.float32` that represents the width of each cell.
        cells: A `MosaicoType.list_(Point2d)` that represents the center point of
            each cell.

    ### Querying with the **`.Q` Proxy**
    This class is fully queryable via the **`.Q` proxy**. You can filter grid cells data based
    on grid field values within a [`QueryOntologyCatalog`][mosaicolabs.models.query.builders.QueryOntologyCatalog].

    Example:
        ```python
        from mosaicolabs import MosaicoClient, GridCells, QueryOntologyCatalog

        with MosaicoClient.connect("localhost", 6726) as client:
            # Filter for cell grid width field values within a specific range
            qresponse = client.query(
                QueryOntologyCatalog(GridCells.Q.cell_width.between(100, 200))
            )

            # Inspect the response
            if qresponse is not None:
                # Results are automatically grouped by Sequence for easier data management
                for item in qresponse:
                    print(f"Sequence: {item.sequence.name}")
                    print(f"Topics: {[topic.name for topic in item.topics]}")

            # Filter for a specific component value and extract the first and last occurrence times
            qresponse = client.query(
                QueryOntologyCatalog(GridCells.Q.cell_width.between(100, 200), include_timestamp_range=True)
            )

            # Inspect the response
            if qresponse is not None:
                # Results are automatically grouped by Sequence for easier data management
                for item in qresponse:
                    print(f"Sequence: {item.sequence.name}")
                    print(f"Topics: {{topic.name:
                                [topic.timestamp_range.start, topic.timestamp_range.end]
                                for topic in item.topics}}")
        ```
    """

    cell_width: MosaicoType.float32 = MosaicoField(description="Width of each cell.")
    """
    Width of each cell.

    ### Querying with the **`.Q` Proxy**
    The grid cells width is queryable via the `cell_width` field.

    | Field Access Path | Queryable Type | Supported Operators |
    | :--- | :--- | :--- |
    | `GridCells.Q.cell_width` | `Numeric` | `.eq()`, `.neq()`, `.lt()`, `.gt()`, `.leq()`, `.geq()`, `.in_()`, `.between()` |
    
    
    Example:
        ```python
        from mosaicolabs import MosaicoClient, GridCells, QueryOntologyCatalog

        with MosaicoClient.connect("localhost", 6726) as client:
            # Filter for cell width within a specific range
            qresponse = client.query(
                QueryOntologyCatalog(GridCells.Q.cell_width.between([100, 200]))
            )

            # Inspect the response
            if qresponse is not None:
                # Results are automatically grouped by Sequence for easier data management
                for item in qresponse:
                    print(f"Sequence: {item.sequence.name}")
                    print(f"Topics: {[topic.name for topic in item.topics]}")

            # Filter for a specific component value and extract the first and last occurrence times
            qresponse = client.query(
                QueryOntologyCatalog(GridCells.Q.cell_width.between([100, 200]), include_timestamp_range=True)
            )

            # Inspect the response
            if qresponse is not None:
                # Results are automatically grouped by Sequence for easier data management
                for item in qresponse:
                    print(f"Sequence: {item.sequence.name}")
                    print(f"Topics: {{topic.name:
                                [topic.timestamp_range.start, topic.timestamp_range.end]
                                for topic in item.topics}}")
        ```
    """

    cell_height: MosaicoType.float32 = MosaicoField(description="Height of each cell.")
    """
    Height of each cell.

    ### Querying with the **`.Q` Proxy**
    The grid cells height is queryable via the `cell_height` field.

    | Field Access Path | Queryable Type | Supported Operators |
    | :--- | :--- | :--- |
    | `GridCells.Q.cell_height` | `Numeric` | `.eq()`, `.neq()`, `.lt()`, `.gt()`, `.leq()`, `.geq()`, `.in_()`, `.between()` |
    
    
    Example:
        ```python
        from mosaicolabs import MosaicoClient, GridCells, QueryOntologyCatalog

        with MosaicoClient.connect("localhost", 6726) as client:
            # Filter for cell width within a specific range
            qresponse = client.query(
                QueryOntologyCatalog(GridCells.Q.cell_height.between([100, 200]))
            )

            # Inspect the response
            if qresponse is not None:
                # Results are automatically grouped by Sequence for easier data management
                for item in qresponse:
                    print(f"Sequence: {item.sequence.name}")
                    print(f"Topics: {[topic.name for topic in item.topics]}")

            # Filter for a specific component value and extract the first and last occurrence times
            qresponse = client.query(
                QueryOntologyCatalog(GridCells.Q.cell_height.between([100, 200]), include_timestamp_range=True)
            )

            # Inspect the response
            if qresponse is not None:
                # Results are automatically grouped by Sequence for easier data management
                for item in qresponse:
                    print(f"Sequence: {item.sequence.name}")
                    print(f"Topics: {{topic.name:
                                [topic.timestamp_range.start, topic.timestamp_range.end]
                                for topic in item.topics}}")
        ```
    """

    cells: MosaicoType.list_(Point2d) = MosaicoField(
        description="The cell represented by a point at it's center."
    )
    """
    The cell represented by a point at it's center.

    ### Querying with the **`.Q` Proxy**
    The cells field is not queryable via the `.Q` proxy (lists are not supported yet).
    """
