import os
from flask import Flask
from supabase import create_client, Client
from dotenv import load_dotenv
from markupsafe import escape

load_dotenv()

app = Flask(__name__)

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_PUBLISHABLE_KEY = os.getenv("SUPABASE_PUBLISHABLE_KEY")

if not SUPABASE_URL or not SUPABASE_PUBLISHABLE_KEY:
    raise RuntimeError(
        "Set SUPABASE_URL and SUPABASE_PUBLISHABLE_KEY in the environment"
    )

supabase: Client = create_client(
    SUPABASE_URL,
    SUPABASE_PUBLISHABLE_KEY,
)


@app.route('/')
def index():
    response = supabase.table('todos').select("*").execute()
    todos = response.data

    html = '<h1>Todos</h1><ul>'
    for todo in todos:
        html += f'<li>{escape(todo["name"])}</li>'
    html += '</ul>'

    return html


if __name__ == '__main__':
    app.run(debug=True)
