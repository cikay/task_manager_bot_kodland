from task_manager_bot_kodland.use_case_protocols import UseCaseProtocol
from task_manager_bot_kodland.entities import TaskEntity
from task_manager_bot_kodland.dtos import TaskCreatorDTO, TaskUpdaterDTO


class TaskCreatorController:

    def __init__(self, task_creator_use_case: UseCaseProtocol):
        self.task_creator_use_case = task_creator_use_case

    async def execute(self, task_name) -> str:
        task_creator_dto = TaskCreatorDTO(name=task_name)
        try:
            await self.task_creator_use_case.execute(task_creator_dto)
            message = f"Task added. To list all tasks use !show_tasks"
        except Exception as e:
            message = "An error occurred while adding the task"

        return message


class TaskListerController:

    def __init__(self, task_lister_use_case: UseCaseProtocol):
        self.task_lister_use_case = task_lister_use_case

    async def execute(self) -> str:
        try:
            tasks = await self.task_lister_use_case.execute()
            if not len(tasks):
                message = "You have no tasks."
            else:
                message = self.get_tasks_str(tasks)
        except Exception as e:
            message = "An error occurred while adding the task"

        return message

    def get_tasks_str(self, tasks: list[TaskEntity]) -> str:
        tasks_str = "Here is the list of tasks:\n"
        for task in tasks:
            if task.is_completed:
                completion_icon = "✅"
            else:
                completion_icon = "❌"

            tasks_str += f"{task.id}: {task.name} (Completed: {completion_icon})\n"

        return tasks_str


class TaskCompleterController:

    def __init__(self, task_updater_use_case: UseCaseProtocol):
        self.task_updater_use_case = task_updater_use_case

    async def execute(self, id: int) -> str:
        updater_dto = TaskUpdaterDTO(is_completed=True)
        task = await self.task_updater_use_case.execute(id, updater_dto)
        message = f"Task {task.id} marked as completed."
        return message


class TaskDeleterController:
    def __init__(self, task_deleter_use_case: UseCaseProtocol):
        self.task_deleter_use_case = task_deleter_use_case

    async def execute(self, id: int) -> str:
        try:
            await self.task_deleter_use_case.execute(id)
            message = f"Task {id} deleted"
        except Exception as e:
            message = "An error occurred while adding the task"

        return message
