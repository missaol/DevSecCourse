from flask import Flask, render_template, request, redirect, url_for
import session_items as session

app = Flask(__name__)
app.config.from_object('flask_config.Config')

@app.route('/')
def index():
    Todos = session.get_items()
    return render_template('index.html',Todos = Todos)

if __name__ == '__main__':
    app.run()