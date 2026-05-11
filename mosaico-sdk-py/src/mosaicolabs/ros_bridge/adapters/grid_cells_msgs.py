from typing import Any, Optional, Tuple, Type

from mosaicolabs import Message
from mosaicolabs.models.data.geometry import Point2d
from mosaicolabs.models.data.grid_cells import GridCells
from mosaicolabs.ros_bridge.adapter_base import ROSAdapterBase
from mosaicolabs.ros_bridge.adapters.helpers import _validate_msgdata
from mosaicolabs.ros_bridge.ros_bridge import register_default_adapter
from mosaicolabs.ros_bridge.ros_message import ROSMessage


@register_default_adapter
class GridCellsAdapter(ROSAdapterBase[GridCells]):
    """
    Adapter for translating ROS GridCells messages to Mosaico `GridCells`.

    **Supported ROS Types:**

    - [`nav_msgs/msg/GridCells`](https://docs.ros2.org/foxy/api/nav_msgs/msg/GridCells.html)

    Example:
    ```python
    ros_msg = ROSMessage(
        topic="/gridcells",
        timestamp=17000,
        msg_type="nav_msgs/msg/GridCells",
        data={
            "cell_width": 10,
            "cell_height": 10,
            "cells": [
                {
                    "x": 1,
                    "y": 2
                },
                {
                    "x": 40,
                    "y": 39
                },
            ]
        }
    )

    mosaico_grid_cells = GridCellsAdapter.translate(ros_msg)
    ```
    """

    ros_msgtype: str | Tuple[str, ...] = ("nav_msgs/msg/GridCells",)

    __mosaico_ontology_type__: Type[GridCells] = GridCells
    _REQUIRED_KEYS = (
        "cell_width",
        "cell_height",
        "cells",
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
            Message: The translated message containing a `GridCells` object.

        Raises:
            Exception: Wraps any translation error with context (topic name, timestamp).
        """
        return super().translate(ros_msg, **kwargs)

    @classmethod
    def from_dict(cls, ros_data: dict) -> GridCells:
        """
        Parses ROS GridCells data.

        Args:
            ros_data (dict): The raw dictionary from the ROS message.

        Returns:
            GridCells: The constructed Mosaico GridCells object.
        """
        _validate_msgdata(cls, ros_data)
        return GridCells(
            cell_width=ros_data["cell_width"],
            cell_height=ros_data["cell_height"],
            cells=[
                Point2d(
                    x=point["x"],
                    y=point["y"],
                    covariance=point["covariance"],
                    covariance_type=point["covariance_type"],
                )
                for point in ros_data["cells"]
            ],
        )

    @classmethod
    def schema_metadata(cls, ros_data: dict, **kwargs: Any) -> Optional[dict]:
        return None
