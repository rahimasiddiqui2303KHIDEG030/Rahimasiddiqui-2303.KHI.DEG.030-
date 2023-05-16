import json
import logging
import os
import sys
from flask import Flask, render_template, request

# Problem  -  App should be able to be executed both during development, with debugging enabled, and in production, with debugging disabled.
app = Flask(__name__)

# This converts the retrieved value to a boolean. If the value is truthy (i.e. not empty, zero, or None), 
#it returns True; otherwise, it returns False
app.debug = bool(os.environ.get('DEBUG', False)) 
# Problem 1 - The logs shouldn’t written to a file, but to the container output.


logging.basicConfig(
    stream=sys.stdout,
    level=logging.INFO,
    format="%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s",
    datefmt="%H:%M:%S",
)
# the logs will be printed to the console or container output rather than being written to a file

TODO_FILE_NAME = "/app/todo_data/todo.json"  
#You can change the Path anytime when you want to switch from test to production

if os.path.exists(TODO_FILE_NAME):
    with open(TODO_FILE_NAME) as f:
        TODO_ITEMS = json.load(f)
else:
    TODO_ITEMS = []


@app.route("/", methods=["GET", "POST"])
def main():
    if request.method == "POST":
        content = request.form["content"]
        TODO_ITEMS.append(content)
        save_todo_items()

    return render_template("index.html", todo_items=TODO_ITEMS)

# This function saves the list on each call making it stateless instead of periodic saving.
def save_todo_items():
    with open(TODO_FILE_NAME, "w") as f:
        json.dump(TODO_ITEMS, f)

# Checking wheather the app is in debug mode or not.
if app.debug:
    app.logger.setLevel(logging.DEBUG)
    app.logger.debug("Debug mode is enabled.")
else:
    app.logger.debug("Debug mode is disabled.")


if __name__ == "__main__":
    app.run(host="0.0.0.0")
