from task_manager_bot_kodland.dtos import TaskCreatorDTO
from task_manager_bot_kodland.entities import TaskEntity
from task_manager_bot_kodland.repository_protocols import TaskRepositoryProtocol


class TaskCreatorUseCase:

    def __init__(self, task_repository: TaskRepositoryProtocol):
        self.task_repository = task_repository

    async def execute(self, task_data: TaskCreatorDTO) -> TaskEntity:
        task = await self.task_repository.create(task_data)
        return task


class TaskListerUseCase:

    def __init__(self, task_repository: TaskRepositoryProtocol):
        self.task_repository = task_repository

    async def execute(self) -> list[TaskEntity]:
        tasks = await self.task_repository.get_all()
        return tasks


class TaskUpdaterUseCase:

    def __init__(self, task_repository: TaskRepositoryProtocol):
        self.task_repository = task_repository

    async def execute(self, task_id: int, task_data: TaskCreatorDTO) -> TaskEntity:
        task = await self.task_repository.update(task_id, task_data)
        return task


class TaskDeleterUseCase:

    def __init__(self, task_repository: TaskRepositoryProtocol):
        self.task_repository = task_repository

    async def execute(self, task_id: int) -> None:
        await self.task_repository.delete(task_id)
        return
