"""
Path Ontology Module.

Defines the data structure for the path.
"""

from mosaicolabs.models import MosaicoField
from mosaicolabs.models.data.geometry import Pose
from mosaicolabs.models.types import MosaicoType

from ..serializable import Serializable


class Path(Serializable):
    """
    Represents a list of poses that form a path that the robot has to follow.

    Attributes:
        poses: A `MosaicoType.list_(Pose)` that represents the list of poses
            that form the path.
    """

    poses: MosaicoType.list_(Pose) = MosaicoField(
        description="The list of poses that form the path."
    )
    """
    The list of poses that form the path.
    
    ### Querying with the **`.Q` Proxy**
    The poses field is not queryable via the `.Q` proxy (lists are not supported yet).
    """
