"""
OccupancyGrid Ontology Module.

Defines the data structure for occupancy grid.
"""

from mosaicolabs.models import MosaicoField
from mosaicolabs.models.data.map_metadata import MapMetadata
from mosaicolabs.models.types import MosaicoType

from ..serializable import Serializable


class OccupancyGrid(Serializable):
    """
    Occupancy Grid data.

    This class represents the occupancy grid.

    Attributes:
        info: A `MapMetadata` describing the occupancy grid.
        data: A `MosaicoType.list_(MosaicoType.int8)` representing data contained in the occupancy grid.

    ### Querying with the **`.Q` Proxy**
    This class is fully queryable via the **`.Q` proxy**. You can filter occupancy grid data based
    on grid field values within a [`QueryOntologyCatalog`][mosaicolabs.models.query.builders.QueryOntologyCatalog].

    Example:
        ```python
        from mosaicolabs import MosaicoClient, OccupancyGrid, QueryOntologyCatalog

        with MosaicoClient.connect("localhost", 6726) as client:
            # Filter for grid width field values within a specific range
            qresponse = client.query(
                QueryOntologyCatalog(OccupancyGrid.Q.info.width.between(-100, 100))
            )

            # Inspect the response
            if qresponse is not None:
                # Results are automatically grouped by Sequence for easier data management
                for item in qresponse:
                    print(f"Sequence: {item.sequence.name}")
                    print(f"Topics: {[topic.name for topic in item.topics]}")

            # Filter for a specific component value and extract the first and last occurrence times
            qresponse = client.query(
                QueryOntologyCatalog(OccupancyGrid.Q.info.width.between(-100, 100), include_timestamp_range=True)
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

    info: MapMetadata = MosaicoField(
        description="Info about the map like it's width and height."
    )
    """
    Info about the map like it's width and height.

    ### Querying with the **`.Q` Proxy**
    The occupancy grid info is queryable via the `info` field.

    | Field Access Path | Queryable Type | Supported Operators |
    | :--- | :--- | :--- |
    | `OccupancyGrid.Q.info.time.seconds` | `Numeric` | `.eq()`, `.neq()`, `.lt()`, `.gt()`, `.leq()`, `.geq()`, `.in_()`, `.between()` |
    | `OccupancyGrid.Q.info.time.nanoseconds` | `Numeric` | `.eq()`, `.neq()`, `.lt()`, `.gt()`, `.leq()`, `.geq()`, `.in_()`, `.between()` |
    | `OccupancyGrid.Q.info.resolution` | `Numeric` | `.eq()`, `.neq()`, `.lt()`, `.gt()`, `.leq()`, `.geq()`, `.in_()`, `.between()` |
    | `OccupancyGrid.Q.info.width` | `Numeric` | `.eq()`, `.neq()`, `.lt()`, `.gt()`, `.leq()`, `.geq()`, `.in_()`, `.between()` |
    | `OccupancyGrid.Q.info.height` | `Numeric` | `.eq()`, `.neq()`, `.lt()`, `.gt()`, `.leq()`, `.geq()`, `.in_()`, `.between()` |
    | `OccupancyGrid.Q.info.origin.position.x` | `Numeric` | `.eq()`, `.neq()`, `.lt()`, `.gt()`, `.leq()`, `.geq()`, `.in_()`, `.between()` |
    | `OccupancyGrid.Q.info.origin.position.y` | `Numeric` | `.eq()`, `.neq()`, `.lt()`, `.gt()`, `.leq()`, `.geq()`, `.in_()`, `.between()` |
    | `OccupancyGrid.Q.info.origin.position.z` | `Numeric` | `.eq()`, `.neq()`, `.lt()`, `.gt()`, `.leq()`, `.geq()`, `.in_()`, `.between()` |
    | `OccupancyGrid.Q.info.origin.orientation.x` | `Numeric` | `.eq()`, `.neq()`, `.lt()`, `.gt()`, `.leq()`, `.geq()`, `.in_()`, `.between()` |
    | `OccupancyGrid.Q.info.origin.orientation.y` | `Numeric` | `.eq()`, `.neq()`, `.lt()`, `.gt()`, `.leq()`, `.geq()`, `.in_()`, `.between()` |
    | `OccupancyGrid.Q.info.origin.orientation.z` | `Numeric` | `.eq()`, `.neq()`, `.lt()`, `.gt()`, `.leq()`, `.geq()`, `.in_()`, `.between()` |
    | `OccupancyGrid.Q.info.origin.orientation.w` | `Numeric` | `.eq()`, `.neq()`, `.lt()`, `.gt()`, `.leq()`, `.geq()`, `.in_()`, `.between()` |

    
    Example:
        ```python
        from mosaicolabs import MosaicoClient, OccupancyGrid, QueryOntologyCatalog

        with MosaicoClient.connect("localhost", 6726) as client:
            # Filter for time seconds within a specific range
            qresponse = client.query(
                QueryOntologyCatalog(OccupancyGrid.Q.info.time.seconds.between([100000, 200000]))
            )

            # Inspect the response
            if qresponse is not None:
                # Results are automatically grouped by Sequence for easier data management
                for item in qresponse:
                    print(f"Sequence: {item.sequence.name}")
                    print(f"Topics: {[topic.name for topic in item.topics]}")

            # Filter for a specific component value and extract the first and last occurrence times
            qresponse = client.query(
                QueryOntologyCatalog(OccupancyGrid.Q.info.time.seconds.between([100000, 200000]), include_timestamp_range=True)
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

    data: MosaicoType.list_(MosaicoType.int8) = MosaicoField(
        description="Map data: 1 means occupied, 0 means unoccupied and -1 means unkown."
    )
    """
    Map data: 1 means occupied, 0 means unoccupied and -1 means unkown.

    ### Querying with the **`.Q` Proxy**
    The data field is not queryable via the `.Q` proxy (lists are not supported yet).
    """
