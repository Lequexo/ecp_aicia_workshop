from flask import Flask, render_template, request
import os

import main
import utils
from main import generate_description, generate_image, save_to_gallery

import definitions

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = definitions.GALLERY_DIR

story = []




@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template("index.html", story=story)

@app.route('/start_action', methods=['POST'])
def start_action():
    global story

    index = len(story)
    story_start = main.generate_story(utils.get_preprompt())
    story_start_prompt = generate_description(story_start)
    start_image = generate_image(story_start_prompt)
    start_filename = save_to_gallery(start_image, index)

    entry = {'id': '', 'story_start': '', 'overall-story': '', 'user_text': '', 'prompt': '', 'filename': '',
             'username': 'AI'}
    entry['id'] = index
    entry['user_text'] = story_start
    entry['filename'] = start_filename
    story.append(entry)
    return render_template("index.html", story=story)

@app.route('/addtostory', methods=['POST'])
def addtostory():
    global story

    if request.method == 'POST':
        user_input = request.form['user_input']

        # Process user input as needed
        app.logger.debug(f'user input: {user_input}')
        entry = {'id': '', 'story_start': '', 'overall-story': '', 'user_text': '', 'prompt': '', 'filename': '',
                 'username': 'Felix'}

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



