from dataclasses import dataclass
from typing import Optional

UNSET = type("UNSET", (), {})


@dataclass
class TaskCreatorDTO:
    name: str
    is_completed: Optional[bool] = False


@dataclass
class TaskUpdaterDTO:
    name: Optional[str] = UNSET
    is_completed: Optional[bool] = UNSET
