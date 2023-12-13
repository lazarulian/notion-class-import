from service.notion_hooks import NotionDatabaseHooks
import pandas as pd
from datetime import datetime, timedelta
import json

if __name__ == "__main__":
    print("\nIntializing Class Importer 🧘\n")
    
    # print("\nPlease input the filepath for your json 🗂️")
    FILE_PATH = ""

    # print("\nPlease input your database id number 🔢")
    DB_ID = "4e5843713854496cb813868a5095aed0"

    # print("\nPlease input your notion integration key 🔢")
    NOTION_TOKEN = "secret_yUD6Jg4isIcEgh1xqPRQb5Zfl8woIkpU3U1t6rC1igw"
    

    print("\nSuccessfully imported your data, sending to notion 🔎")
    
    # Initialize Notion Worker
    database_agent = NotionDatabaseHooks(NOTION_TOKEN)

    with open('tasks.json', 'r') as file:
        tasks_list = json.load(file)
        for task in tasks_list:
            task_name = task['task_name']
            # course_name = task['course_name']
            
            # Convert the deadline string to a datetime object
            deadline_dt = datetime.strptime(task['deadline'], '%m/%d/%Y')
            
            # Format the deadline in the required format
            deadline = deadline_dt.strftime('%Y-%m-%d')
            
            # Calculate the do_date as 2 days before the deadline
            do_date_dt = deadline_dt - timedelta(days=2)
            do_date = do_date_dt.strftime('%Y-%m-%d')
            
            data = {
                    "Task Name": {"title": [{"text": {"content": task_name}}]},
                    "Course": {"select": {"name": "Psych 124C"}},
                    "Do Date": {"date": {"start": do_date}},
                    "Deadline": {"date": {"start": deadline}},
                    "Duration (Hours)": {"number": 2},
                    "Done?": {"checkbox": False}
            }

            database_agent.add_entry(DB_ID, data)

    print("\n✅ Success! Successfully updated your database with the data.\n")