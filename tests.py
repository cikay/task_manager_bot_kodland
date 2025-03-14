import unittest
from unittest.mock import AsyncMock, MagicMock

from main import add_task, show_tasks, complete_task, delete_task
from models import Task


class TestDiscordBot(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        # Mock the Discord context
        self.ctx = MagicMock()
        self.ctx.send = AsyncMock()

        # Setup database mocks
        Task.all = AsyncMock()
        Task.get = AsyncMock()
        Task.save = AsyncMock()
        Task.delete = AsyncMock()
        Task.create = AsyncMock()

        # Sample tasks for testing
        self.sample_tasks = [
            MagicMock(
                id=1,
                name="First task",
                is_completed=False,
                save=AsyncMock(),
                delete=AsyncMock(),
            ),
            MagicMock(
                id=2,
                name="Second task",
                is_completed=True,
                save=AsyncMock(),
                delete=AsyncMock(),
            ),
        ]

        # MagicMock ovveride name so we set in here again
        self.sample_tasks[0].name = "First task"
        self.sample_tasks[1].name = "Second task"

    async def test_add_task(self):
        Task.create.return_value = self.sample_tasks[0]

        await add_task(self.ctx, task_name="New Test Task")

        Task.create.assert_called_once_with(name="New Test Task")
        self.ctx.send.assert_called_once_with(
            "Task added. To list all tasks use !show_tasks"
        )

    async def test_show_tasks_with_tasks(self):
        # Mock Task.all() to return sample tasks
        Task.all.return_value = self.sample_tasks

        await show_tasks(self.ctx)

        Task.all.assert_called_once()
        expected_message = "Here is the list of tasks:\n1: First task (Completed: ❌)\n2: Second task (Completed: ✅)\n"
        self.ctx.send.assert_called_once_with(expected_message)

    async def test_show_tasks_no_tasks(self):
        # Mock Task.all() to return empty list
        Task.all.return_value = []
        await show_tasks(self.ctx)

        Task.all.assert_called_once()
        self.ctx.send.assert_called_once_with("You have no tasks.")

    async def test_complete_task(self):
        # Mock Task.get() to return a task
        Task.get.return_value = self.sample_tasks[0]
        await complete_task(self.ctx, task_id="1")

        Task.get.assert_called_once_with(id="1")
        self.assertEqual(self.sample_tasks[0].is_completed, True)

        self.sample_tasks[0].save.assert_called_once()
        self.ctx.send.assert_called_once_with("Task 1 marked as completed.")

    async def test_delete_task(self):
        # Mock Task.get() to return a task
        Task.get.return_value = self.sample_tasks[0]

        await delete_task(self.ctx, task_id="1")

        Task.get.assert_called_once_with(id="1")
        self.sample_tasks[0].delete.assert_called_once()
        self.ctx.send.assert_called_once_with("Task 1 deleted")


if __name__ == "__main__":
    unittest.main()
