import pytest
from unittest.mock import AsyncMock

from task_manager_bot_kodland.dtos import TaskCreatorDTO, TaskUpdaterDTO
from task_manager_bot_kodland.entities import TaskEntity
from task_manager_bot_kodland.repositories import TaskRepository
from task_manager_bot_kodland.use_cases import (
    TaskCreatorUseCase,
    TaskUpdaterUseCase,
    TaskListerUseCase,
    TaskDeleterUseCase,
)


@pytest.mark.asyncio
async def test_create_task():
    mock_repo = AsyncMock(spec=TaskRepository)
    mock_task = TaskEntity(id=1, name="test", is_completed=True)
    mock_repo.create.return_value = mock_task

    use_case = TaskCreatorUseCase(mock_repo)
    dto = TaskCreatorDTO(name="test", is_completed=True)
    task = await use_case.execute(dto)

    assert type(task) == TaskEntity
    assert task.name == "test"
    assert task.is_completed is True
    mock_repo.create.assert_awaited_once_with(dto)


@pytest.mark.asyncio
async def test_complete_task():
    mock_repo = AsyncMock(spec=TaskRepository)
    mock_updated_task = TaskEntity(id=1, name="test", is_completed=True)
    mock_repo.update.return_value = mock_updated_task

    use_case = TaskUpdaterUseCase(mock_repo)
    dto = TaskUpdaterDTO(is_completed=True)
    task = await use_case.execute(1, dto)

    assert type(task) == TaskEntity
    assert task.is_completed is True
    mock_repo.update.assert_awaited_once_with(1, dto)


@pytest.mark.asyncio
async def test_get_all_tasks():
    mock_repo = AsyncMock(spec=TaskRepository)
    mock_tasks = [
        TaskEntity(id=1, name="task 1", is_completed=False),
        TaskEntity(id=2, name="task 2", is_completed=True),
    ]
    mock_repo.get_all.return_value = mock_tasks

    use_case = TaskListerUseCase(mock_repo)
    tasks = await use_case.execute()

    assert type(tasks) is list
    assert len(tasks) == 2
    for task in tasks:
        assert isinstance(task, TaskEntity)
    mock_repo.get_all.assert_awaited_once()


@pytest.mark.asyncio
async def test_delete_task():
    mock_repo = AsyncMock(spec=TaskRepository)
    mock_repo.delete.return_value = None

    use_case = TaskDeleterUseCase(mock_repo)
    await use_case.execute(1)

    mock_repo.delete.assert_awaited_once_with(1)
