The project runs by Python 3.10

## Discord app configration 
1. Create an app in discord https://discord.com/developers/applications
2. Go to "Installation" menu and add "bot" scope of Guild Install then add send message permission
2. Go to "Bot" menu and enable "Message Content Intent"
3. Go to "Bot" menu and create a token and put it to .env file like below
```
TOKEN="your-token-goes-here"
```
4. Grap the app link in "Installation" menu and open it in browser. It will ask to add server choose a server
5. Run the project following the below section
6. Use the bot
    - Add a task: !add_task First task
    - Show tasks: !show_tasks
    - Complete a task: !complete_task {task_id}
    - Delete a task: !delete_task {task_id}


## Run the project

Create virtual env
```
python3.10 -m venv venv
```

Activate env
```
source venv/bin/activate
```

Install dependencies
```
pip install -r requirements.txt
```

Run the project

```
python main.py
```

## Run tests

```
python -m unittest tests.py
```
