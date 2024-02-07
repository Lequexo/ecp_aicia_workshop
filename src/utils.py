import os

def get_openai_api_key():
    # Get the current directory of the main.py file
    current_directory = os.path.dirname(os.path.abspath(__file__))

    # Navigate to the "data" folder from the "src" directory
    #data_directory = os.path.join(current_directory, '..', 'data')

    # Construct the path to the api_key.txt file
    api_key_path = os.path.join(current_directory, 'api_key.txt')

    # Read the API key from the file
    with open(api_key_path, 'r') as file:
        api_key = file.read().strip()

    return api_key

def get_preprompt():
    # Get the current directory of the main.py file
    current_directory = os.path.dirname(os.path.abspath(__file__))

    # Navigate to the "data" folder from the "src" directory
    #data_directory = os.path.join(current_directory, '..', 'data')

    # Construct the path to the api_key.txt file
    preprompt_path = os.path.join(current_directory, 'preprompt.txt')

    # Read the API key from the file
    with open(preprompt_path, 'r') as file:
        preprompt = file.read().strip()

    return preprompt

