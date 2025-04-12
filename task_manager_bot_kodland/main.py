import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

from task_manager_bot_kodland.db_setup import setup_db
from task_manager_bot_kodland.controller_factories import (
    TaskCreatorControllerFactory,
    TaskListerControllerFactory,
    TaskCompleterControllerFactory,
    TaskDeleterControllerFactory,
)
from task_manager_bot_kodland.repositories import TaskRepository


load_dotenv()

TOKEN = os.getenv("TOKEN")

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}")
    await setup_db()
    print("------")


@bot.command(name="add_task", help="Add a new task")
async def add_task(ctx, *, task_name):
    repo = TaskRepository()
    controller = TaskCreatorControllerFactory.create(repo)
    message = await controller.execute(task_name=task_name)
    await ctx.send(message)


@bot.command(name="show_tasks", help="Show tasks")
async def show_tasks(ctx):
    repo = TaskRepository()
    controller = TaskListerControllerFactory.create(repo)
    message = await controller.execute()
    await ctx.send(message)


@bot.command(name="complete_task", help="Complete a task")
async def complete_task(ctx, *, task_id):
    repo = TaskRepository()
    controller = TaskCompleterControllerFactory.create(repo)
    message = await controller.execute(task_id)
    await ctx.send(message)


@bot.command(name="delete_task", help="Delete a task")
async def delete_task(ctx, *, task_id):
    repo = TaskRepository()
    controller = TaskDeleterControllerFactory.create(repo)
    task_id = await controller.execute(task_id)
    await ctx.send(task_id)


if __name__ == "__main__":
    bot.run(TOKEN)
