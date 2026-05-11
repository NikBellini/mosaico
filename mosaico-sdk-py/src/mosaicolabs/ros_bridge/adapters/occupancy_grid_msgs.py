from typing import Any, Optional, Tuple, Type

from mosaicolabs import Message
from mosaicolabs.models.data.occupancy_grid import OccupancyGrid
from mosaicolabs.ros_bridge.adapter_base import ROSAdapterBase
from mosaicolabs.ros_bridge.adapters.helpers import _validate_msgdata
from mosaicolabs.ros_bridge.adapters.map_metadata_msgs import MapMetadataAdapter
from mosaicolabs.ros_bridge.ros_bridge import register_default_adapter
from mosaicolabs.ros_bridge.ros_message import ROSMessage


@register_default_adapter
class OccupancyGridAdapter(ROSAdapterBase[OccupancyGrid]):
    """
    Adapter for translating ROS OccupancyGrid messages to Mosaico `OccupancyGrid`.

    **Supported ROS Types:**

    - [`nav_msgs/msg/OccupancyGrid`](https://docs.ros2.org/foxy/api/nav_msgs/msg/OccupancyGrid.html)

    Example:
    ```python
    ros_msg = ROSMessage(
        topic="/occupancygrid",
        timestamp=17000,
        msg_type="nav_msgs/msg/OccupancyGrid",
        data={
            "info": {
                "time": {
                    "seconds": 100000,
                    "nanoseconds": 1000
                },
                "resolution": 4,
                "width": 2,
                "height": 2,
                "origin": {
                    "position": {"x": 1.0, "y": 2.0, "z": 0.0},
                    "orientation": {"x": 0, "y": 0, "z": 0, "w": 1}
                }
            },
            data: [1, 1, 0, 1]
        }
    )

    mosaico_occupancy_grid = OccupancyGridAdapter.translate(ros_msg)
    ```
    """

    ros_msgtype: str | Tuple[str, ...] = ("nav_msgs/msg/OccupancyGrid",)

    __mosaico_ontology_type__: Type[OccupancyGrid] = OccupancyGrid
    _REQUIRED_KEYS = (
        "info",
        "data",
    )

    @classmethod
    def translate(
        cls,
        ros_msg: ROSMessage,
        **kwargs: Any,
    ) -> Message:
        """
        Translates a ROS message into a Mosaico Message.

        Returns:
            Message: The translated message containing a `OccupancyGrid` object.

        Raises:
            Exception: Wraps any translation error with context (topic name, timestamp).
        """
        return super().translate(ros_msg, **kwargs)

    @classmethod
    def from_dict(cls, ros_data: dict) -> OccupancyGrid:
        """
        Parses ROS OccupancyGrid data.

        Args:
            ros_data (dict): The raw dictionary from the ROS message.

        Returns:
            OccupancyGrid: The constructed Mosaico OccupancyGrid object.
        """
        _validate_msgdata(cls, ros_data)
        return OccupancyGrid(
            info=MapMetadataAdapter.from_dict(ros_data["info"]), data=ros_data["data"]
        )

    @classmethod
    def schema_metadata(cls, ros_data: dict, **kwargs: Any) -> Optional[dict]:
        return None
