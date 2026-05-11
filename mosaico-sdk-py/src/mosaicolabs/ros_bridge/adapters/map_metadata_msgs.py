from typing import Any, Optional, Tuple, Type

from mosaicolabs import Message
from mosaicolabs.models.data.map_metadata import MapMetadata
from mosaicolabs.ros_bridge.adapter_base import ROSAdapterBase
from mosaicolabs.ros_bridge.adapters.geometry_msgs import PoseAdapter
from mosaicolabs.ros_bridge.adapters.helpers import _validate_msgdata
from mosaicolabs.ros_bridge.ros_bridge import register_default_adapter
from mosaicolabs.ros_bridge.ros_message import ROSMessage
from mosaicolabs.types.time import Time


@register_default_adapter
class MapMetadataAdapter(ROSAdapterBase[MapMetadata]):
    """
    Adapter for translating ROS MapMetadata messages to Mosaico `MapMetadata`.

    **Supported ROS Types:**

    - [`nav_msgs/msg/MapMetaData`](https://docs.ros2.org/foxy/api/nav_msgs/msg/MapMetaData.html)

    Example:
    ```python
    ros_msg = ROSMessage(
        topic="/mapmetadata",
        timestamp=17000,
        msg_type="nav_msgs/msg/MapMetaData",
        data={
            "time": {
                "seconds": 100000,
                "nanoseconds": 1000
            },
            "resolution": 10000,
            "width": 100,
            "height": 100,
            "origin": {
                "position": {"x": 1.0, "y": 2.0, "z": 0.0},
                "orientation": {"x": 0, "y": 0, "z": 0, "w": 1}
            }
        }
    )

    mosaico_map_metadata = MapMetadataAdapter.translate(ros_msg)
    ```
    """

    ros_msgtype: str | Tuple[str, ...] = ("nav_msgs/msg/MapMetaData",)

    __mosaico_ontology_type__: Type[MapMetadata] = MapMetadata
    _REQUIRED_KEYS = (
        "time",
        "resolution",
        "width",
        "height",
        "origin",
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
            Message: The translated message containing a `MapMetadata` object.

        Raises:
            Exception: Wraps any translation error with context (topic name, timestamp).
        """
        return super().translate(ros_msg, **kwargs)

    @classmethod
    def from_dict(cls, ros_data: dict) -> MapMetadata:
        """
        Parses ROS MapMetadata data.

        Args:
            ros_data (dict): The raw dictionary from the ROS message.

        Returns:
            MapMetadata: The constructed Mosaico MapMetadata object.
        """
        _validate_msgdata(cls, ros_data)
        return MapMetadata(
            time=Time(
                seconds=ros_data["time"]["seconds"],
                nanoseconds=ros_data["time"]["nanoseconds"],
            ),
            resolution=ros_data["resolution"],
            width=ros_data["width"],
            height=ros_data["height"],
            origin=PoseAdapter.from_dict(ros_data["origin"]),
        )

    @classmethod
    def schema_metadata(cls, ros_data: dict, **kwargs: Any) -> Optional[dict]:
        return None
