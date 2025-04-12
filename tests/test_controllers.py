import pytest
from unittest.mock import AsyncMock

from task_manager_bot_kodland.dtos import TaskCreatorDTO
from task_manager_bot_kodland.entities import TaskEntity
from task_manager_bot_kodland.controller_factories import (
    TaskCompleterControllerFactory,
    TaskCreatorControllerFactory,
    TaskDeleterControllerFactory,
    TaskListerControllerFactory,
)
from task_manager_bot_kodland.repositories import TaskRepository


@pytest.mark.asyncio
async def test_create_task_controller():
    mock_repo = AsyncMock(spec=TaskRepository)
    mock_task = TaskEntity(id=1, name="controller test", is_completed=False)
    mock_repo.create.return_value = mock_task

    controller = TaskCreatorControllerFactory.create(mock_repo)
    dto = TaskCreatorDTO(name="controller test", is_completed=False)
    message = await controller.execute(dto)

    assert message == "Task added. To list all tasks use !show_tasks"


@pytest.mark.asyncio
async def test_complete_task_controller():
    mock_repo = AsyncMock(spec=TaskRepository)
    mock_existing_task = TaskEntity(id=1, name="test", is_completed=False)
    mock_completed_task = TaskEntity(id=1, name="test", is_completed=True)
    mock_repo.update.return_value = mock_completed_task

    controller = TaskCompleterControllerFactory.create(mock_repo)
    message = await controller.execute(1)

    assert message == f"Task {mock_existing_task.id} marked as completed."


@pytest.mark.asyncio
async def test_delete_task_controller():
    mock_repo = AsyncMock(spec=TaskRepository)
    mock_repo.delete.return_value = None
    id = 1
    controller = TaskDeleterControllerFactory.create(mock_repo)
    message = await controller.execute(id)

    mock_repo.delete.assert_awaited_once_with(1)
    assert message == f"Task {id} deleted"


@pytest.mark.asyncio
async def test_get_all_tasks_controller():
    mock_repo = AsyncMock(spec=TaskRepository)
    mock_tasks = [
        TaskEntity(id=3, name="task A", is_completed=False),
        TaskEntity(id=4, name="task B", is_completed=True),
    ]
    mock_repo.get_all.return_value = mock_tasks

    controller = TaskListerControllerFactory.create(mock_repo)
    message = await controller.execute()

    assert (
        message
        == "Here is the list of tasks:\n3: task A (Completed: ❌)\n4: task B (Completed: ✅)\n"
    )


@pytest.mark.asyncio
async def test_get_all_tasks_controller__no_tasks():
    mock_repo = AsyncMock(spec=TaskRepository)
    mock_tasks = []
    mock_repo.get_all.return_value = mock_tasks

    controller = TaskListerControllerFactory.create(mock_repo)
    message = await controller.execute()

    assert message == "You have no tasks."
