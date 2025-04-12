from dataclasses import dataclass


@dataclass
class TaskEntity:
    id: int
    name: str
    is_completed: bool
