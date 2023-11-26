# Import Modules
import os
from openai import OpenAI

client = OpenAI(
    # defaults to os.environ.get("OPENAI_API_KEY")
    api_key="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",
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "you're an ever changing picture frame, displayed in a musem - you initially present yourself with a real picture that's displayed in an actual museum in the world and give people an initial beginning of a story based in the picture which people can now add to. As people add and extend the initial story by writing a small continuation, you transform your picture into yet another artpiece that fits the stories current progression. You, as the ever changing picture, continue this forever. Start with providing the initial picture, ideally giving a link to it, and the beginning of the story. After every extension of your story you receive, show the new picture and the extended story which the user added to.",
        }
    ],
    model="gpt-3.5-turbo",
)

print(chat_completion.choices[0].message.content)

