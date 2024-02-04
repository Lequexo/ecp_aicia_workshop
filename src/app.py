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

    #imageList = os.listdir('/static/gallery')
    #imagelist = ['pics/' + image for image in imageList]

    full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'image_0.png')
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)


