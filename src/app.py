from flask import Flask, render_template, request
import os

import definitions

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = definitions.GALLERY_DIR

@app.route('/', methods=['GET', 'POST'])
def index():

    if request.method == 'POST':
        user_input = request.form['user_input']
        # Process user input as needed
        print('User Input received: '+user_input)

    images = [f for f in os.listdir(definitions.GALLERY_DIR) if f.endswith(('.png', '.jpg', '.jpeg', '.gif'))]

    return render_template("index.html", images=images)

if __name__ == '__main__':
    app.run(debug=True)


