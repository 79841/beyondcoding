# https://platform.openai.com/docs/api-reference/completions/create
import os
import openai

openai.api_key = "your api key"


while True:
    msg = input("Me : ")
    if msg == "quit":
        break

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", messages=[{"role": "user", "content": msg}]
    )
    print("Chatgpt :", completion.choices[0].message["content"])
