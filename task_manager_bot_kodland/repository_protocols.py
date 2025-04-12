from typing import Protocol

from task_manager_bot_kodland.dtos import TaskCreatorDTO, TaskUpdaterDTO
from task_manager_bot_kodland.entities import TaskEntity


class TaskRepositoryProtocol(Protocol):

    def get(self, id: int) -> TaskEntity: ...

    def create(self, item: TaskCreatorDTO) -> TaskEntity: ...

    def update(self, id: int, item: TaskUpdaterDTO) -> TaskEntity: ...

    def delete(self, id: int) -> None: ...

    def get_all(self) -> list[TaskEntity]: ...
