from typing import Any, Optional, Tuple, Type

from mosaicolabs import Message
from mosaicolabs.models.data.path import Path
from mosaicolabs.ros_bridge.adapter_base import ROSAdapterBase
from mosaicolabs.ros_bridge.adapters.geometry_msgs import PoseAdapter
from mosaicolabs.ros_bridge.adapters.helpers import _validate_msgdata
from mosaicolabs.ros_bridge.ros_bridge import register_default_adapter
from mosaicolabs.ros_bridge.ros_message import ROSMessage


@register_default_adapter
class PathAdapter(ROSAdapterBase[Path]):
    """
    Adapter for translating ROS Path messages to Mosaico `Path`.

    **Supported ROS Types:**

    - [`nav_msgs/msg/Path`](https://docs.ros2.org/foxy/api/nav_msgs/msg/Path.html)

    Example:
    ```python
    ros_msg = ROSMessage(
        topic="/path",
        timestamp=17000,
        msg_type="nav_msgs/msg/Path",
        data={
            "poses": [
                {
                    "position": {"x": 1.0, "y": 2.0, "z": 0.0},
                    "orientation": {"x": 0, "y": 0, "z": 0, "w": 1}
                },
                {
                    "position": {"x": 2.0, "y": 2.0, "z": 0.0},
                    "orientation": {"x": 0, "y": 0, "z": 0, "w": 1}
                },
                {
                    "position": {"x": 3.0, "y": 2.0, "z": 0.0},
                    "orientation": {"x": 0, "y": 0, "z": 0, "w": 1}
                },
            ]
        }
    )

    mosaico_path = PathAdapter.translate(ros_msg)
    ```
    """

    ros_msgtype: str | Tuple[str, ...] = ("nav_msgs/msg/Path",)

    __mosaico_ontology_type__: Type[Path] = Path
    _REQUIRED_KEYS = ("poses",)

    @classmethod
    def translate(
        cls,
        ros_msg: ROSMessage,
        **kwargs: Any,
    ) -> Message:
        """
        Translates a ROS message into a Mosaico Message.

        Returns:
            Message: The translated message containing a `Path` object.

        Raises:
            Exception: Wraps any translation error with context (topic name, timestamp).
        """
        return super().translate(ros_msg, **kwargs)

    @classmethod
    def from_dict(cls, ros_data: dict) -> Path:
        """
        Parses ROS Path data.

        Args:
            ros_data (dict): The raw dictionary from the ROS message.

        Returns:
            Path: The constructed Mosaico Path object.
        """
        _validate_msgdata(cls, ros_data)
        return Path(poses=[PoseAdapter.from_dict(pose) for pose in ros_data["poses"]])

    @classmethod
    def schema_metadata(cls, ros_data: dict, **kwargs: Any) -> Optional[dict]:
        return None
