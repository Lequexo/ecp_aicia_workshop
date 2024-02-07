import os
import webbrowser

from openai import OpenAI
import requests
from io import BytesIO
from PIL import Image
import utils
import json

# Generate story using ChatGPT
def generate_story(prompt):
    client = OpenAI(
        # defaults to os.environ.get("OPENAI_API_KEY")
        api_key=utils.get_openai_api_key(),
    )

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="gpt-3.5-turbo",
    )
    story = chat_completion.choices[0].message.content
    return story


def generate_description(story):
    client = OpenAI(
        # defaults to os.environ.get("OPENAI_API_KEY")
        api_key=utils.get_openai_api_key(),
    )

    # Instruct ChatGPT to summarize the provided story
    instruction = "Please summarize the following story into instructions for a image generation ai to create a fitting picture for it, suitable as a prompt used in another api call:\n"
    prompt_with_instruction = f"{instruction}{story}"

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt_with_instruction,
            }
        ],
        model="gpt-3.5-turbo",
    )

    # Extract the generated description from the response
    description = chat_completion.choices[0].message.content
    return description


# Create an image based on the story
def generate_image(description, model="dall-e-3"):
    client = OpenAI(
        # defaults to os.environ.get("OPENAI_API_KEY")
        api_key=utils.get_openai_api_key(),
    )

    response = client.images.generate(
        model="dall-e-3",
        prompt=description,
        size="1024x1024",
        quality="standard",
        n=1,
    )

    image_url = response.data[0].url

    # Download the image from the URL
    image_response = requests.get(image_url)
    image_data = BytesIO(image_response.content)

    # Open and display the image
    image = Image.open(image_data)
    return image


def save_to_gallery(image: Image, image_number: int):
    # Get the current directory of main.py
    current_directory = os.path.dirname(os.path.realpath(__file__))
    # Navigate to the parent directory (root_folder)
    #parent_directory = os.path.abspath(os.path.join(current_directory, os.pardir))

    # Create the path for the "gallery" folder in the parent directory
    gallery_path = os.path.join("static", "gallery")

    # Check if the "gallery" folder exists, and create it if not
    if not os.path.exists(gallery_path):
        os.makedirs(gallery_path)

    image_filename = f"image_{image_number}.png"

    # Your image file name with an embedded number
    image_filename = f"image_{image_number}.png"

    # Full path to save the image
    image_path = os.path.join(gallery_path, image_filename)

    # Save the image at the specified path
    image.save(image_path)
    webbrowser.open(image_path)
    return image_filename

def setup_story(idea):
    if not idea:
        # We let AI generate a story based on our prompt if we have no idea for a beginning
        prompt = utils.get_preprompt()
        story = generate_story(prompt)
    else:
        # We take our idea as the beginning for our story if given
        story = idea

    print("Caption: ", story)

    generated_description = generate_description(story)
    # print(generated_description)
    image = generate_image(generated_description)
    save_to_gallery(image, 0)

    return story


def continue_story(story, image_number):
    addition = input(f"You may continue the story ({image_number}): ")
    continued_story = f"{story}{addition}"
    print("Caption: ", continued_story)

    generated_description = generate_description(continued_story)

    image = generate_image(generated_description)
    save_to_gallery(image, image_number)

    return continued_story


def dialogue_x_picture_story(story, x):
    image_number = 1
    while image_number < x:
        story = continue_story(story, image_number)
        image_number += 1

    print("The story is concluded and saved in the gallery for others to see!")


# Main function
def main():
    # story = 'As the sun began to set, a sense of unease settled over the sleepy town. From the shadows emerged a
    # figure, moving silently through the deserted streets, its intentions unknown.'#generate_story(prompt)
    # 'As the door creaked open, a waft of musty air filled the room, carrying with it the whispers of forgotten stories.'
    story = setup_story(None)
    dialogue_x_picture_story(story, 4)


if __name__ == "__main__":
    main()
