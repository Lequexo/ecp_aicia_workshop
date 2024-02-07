from flask import Flask, render_template, request
import os
from main import generate_description, generate_image, save_to_gallery

import definitions

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = definitions.GALLERY_DIR

story = []

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template("index.html", story=story)

@app.route('/addtostory', methods=['POST'])
def addtostory():

    if request.method == 'POST':
        user_input = request.form['user_input']
        # Process user input as needed
        app.logger.debug(f'user input: {user_input}')
        
        entry = {'id': '', 'user_text': '', 'prompt': '', 'filename': '', 'username': 'UserX'}
        
        index = len(story)
        entry['user_text'] = user_input
        overall_story = ' '.join([entry['user_text'] for entry in story])
        entry['id'] = index
        image_prompt = generate_description(overall_story)
        image = generate_image(image_prompt)
        filename = save_to_gallery(image, index)
        entry['prompt'] = image_prompt
        entry['filename'] = filename
        story.append(entry)
        
    return render_template("index.html", story=story)



if __name__ == '__main__':
    app.run(debug=True)


