from dataclasses import asdict

from task_manager_bot_kodland.dtos import TaskCreatorDTO, UNSET, TaskUpdaterDTO
from task_manager_bot_kodland.models import TaskDB
from task_manager_bot_kodland.entities import TaskEntity


class TaskRepository:

    async def create(self, task: TaskCreatorDTO) -> TaskEntity:
        task = TaskDB(name=task.name, is_completed=task.is_completed)
        await task.save()
        return task

    async def get(self, task_id: int) -> TaskEntity:
        task = await TaskDB.get(id=task_id)
        return TaskEntity(
            id=task.id,
            name=task.name,
            is_completed=task.is_completed,
        )

    async def get_all(self) -> list[TaskEntity]:
        tasks = await TaskDB.all()
        return [
            TaskEntity(
                id=task.id,
                name=task.name,
                is_completed=task.is_completed,
            )
            for task in tasks
        ]

    async def update(self, task_id: int, task_dto: TaskUpdaterDTO) -> TaskEntity:
        task = await TaskDB.get(id=task_id)
        task_dict = asdict(task_dto)
        for field, value in task_dict.items():
            if value is not UNSET:
                setattr(task, field, value)

        await task.save()
        return TaskEntity(
            id=task.id,
            name=task.name,
            is_completed=task.is_completed,
        )

    async def delete(self, id):
        task = await TaskDB.get(id=id)
        await task.delete()
