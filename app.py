from flask import Flask, render_template, request

app = Flask(__name__)

# Dictionary to store commands and their corresponding responses
command_responses = {
    "hello": "Hi there!",
    "time": "The current time is 12:00 PM",
    # Add more commands and responses as needed
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send-command', methods=['POST'])
def send_command():
    command = request.form['command']
    response = command_responses.get(command, "Command not found")
    return response

if __name__ == '__main__':
    app.run(debug=True)
