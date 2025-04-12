from task_manager_bot_kodland.repository_protocols import TaskRepositoryProtocol
from task_manager_bot_kodland.use_cases import (
    TaskUpdaterUseCase,
    TaskCreatorUseCase,
    TaskDeleterUseCase,
    TaskListerUseCase,
)
from task_manager_bot_kodland.controllers import (
    TaskCreatorController,
    TaskListerController,
    TaskCompleterController,
    TaskDeleterController,
)


class TaskCreatorControllerFactory:
    @staticmethod
    def create(repo: TaskRepositoryProtocol):
        use_case = TaskCreatorUseCase(repo)
        return TaskCreatorController(use_case)


class TaskDeleterControllerFactory:
    @staticmethod
    def create(repo):
        use_case = TaskDeleterUseCase(repo)
        return TaskDeleterController(use_case)


class TaskListerControllerFactory:
    @staticmethod
    def create(repo) -> TaskListerController:
        use_case = TaskListerUseCase(repo)
        return TaskListerController(use_case)


class TaskCompleterControllerFactory:
    @staticmethod
    def create(repo):
        use_case = TaskUpdaterUseCase(repo)
        return TaskCompleterController(use_case)
