import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

from db_setup import setup_db
from models import Task


load_dotenv()

TOKEN = os.getenv("TOKEN")

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

tasks = []


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}")
    await setup_db()
    print("------")


@bot.command(name="add_task", help="Add a new task")
async def add_task(ctx, *, task_name):
    task = Task(name=task_name)
    await task.save()
    message = f'Task added. To list all tasks use !show_tasks'
    await ctx.send(message)


@bot.command(name="show_tasks", help="Show tasks")
async def show_tasks(ctx):
    tasks = await Task.all()
    if not len(tasks):
        await ctx.send("You have no tasks.")
        return

    tasks_str = "Here is the list of tasks:\n"
    for task in tasks:
        if task.is_completed:
            completion_icon = "✅"
        else:
            completion_icon = "❌"

        tasks_str += f"{task.id}: {task.name} (Completed: {completion_icon})\n"

    await ctx.send(tasks_str)


@bot.command(name="complete_task", help="Complete a task")
async def complete_task(ctx, *, task_id):
    task = await Task.get(id=task_id)
    task.is_completed = True
    await task.save()
    message = f'Task {task.id} marked as completed.'
    await ctx.send(message)


@bot.command(name="delete_task", help="Delete a task")
async def delete_task(ctx, *, task_id):
    task = await Task.get(id=task_id)
    await task.delete()
    message = f"Task {task.id} deleted"
    await ctx.send(message)


print(f"TOKEN: {TOKEN}")
bot.run(TOKEN)
