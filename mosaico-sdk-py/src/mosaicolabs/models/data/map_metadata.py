from mosaicolabs.models.serializable import Serializable
from mosaicolabs.models.types import MosaicoField, MosaicoType
from mosaicolabs.types.time import Time

from .kinematics import Pose


class MapMetadata(
    Serializable,  # Adds Registry/Factory logic
):
    """
    Represents metadata about the map, like it's width and height.

    Attributes:
        time: A `Time` representing the time at which the map has
            been loaded.
        resolution: A `MosaicoType.float32` representing the resolution
            of the map.
        width: A `MosaicoType.uint32` representing the number of cells that
            represent the width of the map.
        height: A `MosaicoType.uint32` representing the number of cells that
            represent the height of the map.
        origin: A `Pose` that represents where the map starts in the real world.

    ### Querying with the **`.Q` Proxy**
    This class fields are queryable when constructing a [`QueryOntologyCatalog`][mosaicolabs.models.query.builders.QueryOntologyCatalog]
    via the **`.Q` proxy**. Check the fields documentation for detailed description.

    Example:
        ```python
        from mosaicolabs import MosaicoClient, MapMetadata, QueryOntologyCatalog

        with MosaicoClient.connect("localhost", 6726) as client:
            # Filter MapMetadatas with width AND height
            qresponse = client.query(
                QueryOntologyCatalog(MapMetadata.Q.width.gt(100))
                .with_expression(MapMetadata.Q.height.lt(200))
            )

            # Inspect the response
            if qresponse is not None:
                # Results are automatically grouped by Sequence for easier data management
                for item in qresponse:
                    print(f"Sequence: {item.sequence.name}")
                    print(f"Topics: {[topic.name for topic in item.topics]}")

            # Filter for a specific component value and extract the first and last occurrence times
            qresponse = client.query(
                QueryOntologyCatalog(MapMetadata.Q.width.between(100, 200), include_timestamp_range=True)
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

    time: Time = MosaicoField(description="Time at which the map has been loaded.")
    """
    Time at which the map has been loaded.

    ### Querying with the **`.Q` Proxy**
    The map metadata time is queryable via the `time` field.

    | Field Access Path | Queryable Type | Supported Operators |
    | :--- | :--- | :--- |
    | `MapMetadata.Q.time.seconds` | `Numeric` | `.eq()`, `.neq()`, `.lt()`, `.gt()`, `.leq()`, `.geq()`, `.in_()`, `.between()` |
    | `MapMetadata.Q.time.nanoseconds` | `Numeric` | `.eq()`, `.neq()`, `.lt()`, `.gt()`, `.leq()`, `.geq()`, `.in_()`, `.between()` |

    
    Example:
        ```python
        from mosaicolabs import MosaicoClient, MapMetadata, QueryOntologyCatalog

        with MosaicoClient.connect("localhost", 6726) as client:
            # Filter for time seconds within a specific range
            qresponse = client.query(
                QueryOntologyCatalog(MapMetadata.Q.time.seconds.between([100000, 200000]))
            )

            # Inspect the response
            if qresponse is not None:
                # Results are automatically grouped by Sequence for easier data management
                for item in qresponse:
                    print(f"Sequence: {item.sequence.name}")
                    print(f"Topics: {[topic.name for topic in item.topics]}")

            # Filter for a specific component value and extract the first and last occurrence times
            qresponse = client.query(
                QueryOntologyCatalog(MapMetadata.Q.time.seconds.between([100000, 200000]), include_timestamp_range=True)
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

    resolution: MosaicoType.float32 = MosaicoField(description="Resolution of the map.")
    """
    Resolution of the map.

    ### Querying with the **`.Q` Proxy**
    The map metadata resolution is queryable via the `resolution` field.

    | Field Access Path | Queryable Type | Supported Operators |
    | :--- | :--- | :--- |
    | `MapMetadata.Q.resolution` | `Numeric` | `.eq()`, `.neq()`, `.lt()`, `.gt()`, `.leq()`, `.geq()`, `.in_()`, `.between()` |
    
    Example:
        ```python
        from mosaicolabs import MosaicoClient, MapMetadata, QueryOntologyCatalog

        with MosaicoClient.connect("localhost", 6726) as client:
            # Filter for resolution within a specific range
            qresponse = client.query(
                QueryOntologyCatalog(MapMetadata.Q.resolution.between([100000, 200000]))
            )

            # Inspect the response
            if qresponse is not None:
                # Results are automatically grouped by Sequence for easier data management
                for item in qresponse:
                    print(f"Sequence: {item.sequence.name}")
                    print(f"Topics: {[topic.name for topic in item.topics]}")

            # Filter for a specific component value and extract the first and last occurrence times
            qresponse = client.query(
                QueryOntologyCatalog(MapMetadata.Q.resolution.between([100000, 200000]), include_timestamp_range=True)
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

    width: MosaicoType.uint32 = MosaicoField(
        description="Number of cells representing the width of the map."
    )
    """
    Number of cells representing the width of the map.

    ### Querying with the **`.Q` Proxy**
    The map metadata width is queryable via the `width` field.

    | Field Access Path | Queryable Type | Supported Operators |
    | :--- | :--- | :--- |
    | `MapMetadata.Q.width` | `Numeric` | `.eq()`, `.neq()`, `.lt()`, `.gt()`, `.leq()`, `.geq()`, `.in_()`, `.between()` |
    
    Example:
        ```python
        from mosaicolabs import MosaicoClient, MapMetadata, QueryOntologyCatalog

        with MosaicoClient.connect("localhost", 6726) as client:
            # Filter for width within a specific range
            qresponse = client.query(
                QueryOntologyCatalog(MapMetadata.Q.width.between([10, 20]))
            )

            # Inspect the response
            if qresponse is not None:
                # Results are automatically grouped by Sequence for easier data management
                for item in qresponse:
                    print(f"Sequence: {item.sequence.name}")
                    print(f"Topics: {[topic.name for topic in item.topics]}")

            # Filter for a specific component value and extract the first and last occurrence times
            qresponse = client.query(
                QueryOntologyCatalog(MapMetadata.Q.width.between([10, 20]), include_timestamp_range=True)
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

    height: MosaicoType.uint32 = MosaicoField(
        description="Number of cells representing the height of the map."
    )
    """
    Number of cells representing the height of the map.

    ### Querying with the **`.Q` Proxy**
    The map metadata height is queryable via the `height` field.

    | Field Access Path | Queryable Type | Supported Operators |
    | :--- | :--- | :--- |
    | `MapMetadata.Q.height` | `Numeric` | `.eq()`, `.neq()`, `.lt()`, `.gt()`, `.leq()`, `.geq()`, `.in_()`, `.between()` |
    
    Example:
        ```python
        from mosaicolabs import MosaicoClient, MapMetadata, QueryOntologyCatalog

        with MosaicoClient.connect("localhost", 6726) as client:
            # Filter for height within a specific range
            qresponse = client.query(
                QueryOntologyCatalog(MapMetadata.Q.height.between([10, 20]))
            )

            # Inspect the response
            if qresponse is not None:
                # Results are automatically grouped by Sequence for easier data management
                for item in qresponse:
                    print(f"Sequence: {item.sequence.name}")
                    print(f"Topics: {[topic.name for topic in item.topics]}")

            # Filter for a specific component value and extract the first and last occurrence times
            qresponse = client.query(
                QueryOntologyCatalog(MapMetadata.Q.width.between([10, 20]), include_timestamp_range=True)
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

    origin: Pose = MosaicoField(description="Where the map starts in the real world.")
    """
    Where the map starts in the real world.

    ### Querying with the **`.Q` Proxy**
    The map metadata origin is queryable via the `origin` field.

    | Field Access Path | Queryable Type | Supported Operators |
    | :--- | :--- | :--- |
    | `MapMetadata.Q.origin.position.x` | `Numeric` | `.eq()`, `.neq()`, `.lt()`, `.gt()`, `.leq()`, `.geq()`, `.in_()`, `.between()` |
    | `MapMetadata.Q.origin.position.y` | `Numeric` | `.eq()`, `.neq()`, `.lt()`, `.gt()`, `.leq()`, `.geq()`, `.in_()`, `.between()` |
    | `MapMetadata.Q.origin.position.z` | `Numeric` | `.eq()`, `.neq()`, `.lt()`, `.gt()`, `.leq()`, `.geq()`, `.in_()`, `.between()` |
    | `MapMetadata.Q.origin.orientation.x` | `Numeric` | `.eq()`, `.neq()`, `.lt()`, `.gt()`, `.leq()`, `.geq()`, `.in_()`, `.between()` |
    | `MapMetadata.Q.origin.orientation.y` | `Numeric` | `.eq()`, `.neq()`, `.lt()`, `.gt()`, `.leq()`, `.geq()`, `.in_()`, `.between()` |
    | `MapMetadata.Q.origin.orientation.z` | `Numeric` | `.eq()`, `.neq()`, `.lt()`, `.gt()`, `.leq()`, `.geq()`, `.in_()`, `.between()` |
    | `MapMetadata.Q.origin.orientation.w` | `Numeric` | `.eq()`, `.neq()`, `.lt()`, `.gt()`, `.leq()`, `.geq()`, `.in_()`, `.between()` |

    Example:
        ```python
        from mosaicolabs import MosaicoClient, MapMetadata, QueryOntologyCatalog

        with MosaicoClient.connect("localhost", 6726) as client:
            # Filter map metadata where the object is beyond a specific X-coordinate
            qresponse = client.query(
                QueryOntologyCatalog(MapMetadata.Q.origin.position.x.gt(500.0))
            )

            # Inspect the response
            if qresponse is not None:
                # Results are automatically grouped by Sequence for easier data management
                for item in qresponse:
                    print(f"Sequence: {item.sequence.name}")
                    print(f"Topics: {[topic.name for topic in item.topics]}")

            # Filter for a specific component value and extract the first and last occurrence times
            qresponse = client.query(
                QueryOntologyCatalog(MapMetadata.Q.origin.position.x.gt(500.0), include_timestamp_range=True)
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
