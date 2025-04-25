from dotenv import load_dotenv
load_dotenv()
from flask import Flask, request, render_template_string
import requests
import os

NOTION_TOKEN = os.getenv("NOTION_TOKEN")
DATABASE_ID = os.getenv("DATABASE_ID")

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        name = request.form.get("name")
        comment = request.form.get("comment")
        add_to_notion(name, comment)
        return "Notionに追加されました！"

    return render_template_string("""
    <form method="POST">
        名前: <input type="text" name="name"><br>
        コメント: <input type="text" name="comment"><br>
        <input type="submit" value="送信">
    </form>
    """)

def add_to_notion(name, comment):
    url = "https://api.notion.com/v1/pages"
    headers = {
        "Authorization": f"Bearer {NOTION_TOKEN}",
        "Content-Type": "application/json",
        "Notion-Version": "2022-06-28",
    }
    data = {
        "parent": { "database_id": DATABASE_ID },
        "properties": {
            "名前": {
                "title": [
                    {
                        "text": {
                            "content": name
                        }
                    }
                ]
            },
            "コメント": {
                "rich_text": [
                    {
                        "text": {
                            "content": comment
                        }
                    }
                ]
            }
        }
    }

    response = requests.post(url, headers=headers, json=data)
    print(response.status_code, response.text)

if __name__ == "__main__":
    app.run(debug=True)