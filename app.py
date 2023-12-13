from service.notion_hooks import NotionDatabaseHooks
import pandas as pd

if __name__ == "__main__":
    print("\nIntializing Class Importer 🧘\n")
    
    print("\nPlease input the filepath for your json 🗂️")
    FILE_PATH = input()

    print("\nPlease input your database id number 🔢")
    DB_ID = "4e5843713854496cb813868a5095aed0"

    print("\nPlease input your notion integration key 🔢")
    NOTION_TOKEN = "secret_yUD6Jg4isIcEgh1xqPRQb5Zfl8woIkpU3U1t6rC1igw"
    

    print("\nSuccessfully imported your data, sending to notion 🔎")
    
    # Initialize Notion Worker
    database_agent = NotionDatabaseHooks(NOTION_TOKEN)

    # Update Database
    for book_title, average_rating, number_favorites in zip(ratings['book_title'], ratings['average_rating'], ratings['number_favorites']):
        average_rating = str(average_rating)
        number_favorites = str(number_favorites)
        data = {
            "Book Name": {"title": [{"text": {"content": book_title}}]},
            "Average Rating": {"rich_text": [{"text": {"content": average_rating}}]},
            "Number of Favorites": {"rich_text": [{"text": {"content": number_favorites}}]}
        }

        database_agent.add_entry(DB_ID, data)

    print("\n✅ Success! Successfully updated your database with the data.\n")