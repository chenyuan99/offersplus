import logging

import openai

openai.api_key = "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"


def generate_response(prompt: str) -> str:
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ])
    result = completion.choices[0].message.content
    print(f"Generated response: {result}")
    return result
