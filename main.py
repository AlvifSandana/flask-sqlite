from flask import Flask
import bin.DB as DBhelper

# initiate Flask
app = Flask(__name__)

# declare routes
@app.route('/')
def index():
    return 'Main Page'

if __name__ == '__main__':
    app.run()
    DB.create_connection('db/test.db')
