import os
import openai

openai.api_key = "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"

def openAIQuery(query):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=query,
        temperature=1,
        max_tokens=500,
        top_p=1,
        best_of=5,
        frequency_penalty=1,
        presence_penalty=0.5)

    if 'choices' in response:
            if len(response['choices']) > 0:
                answer = response['choices'][0]['text']
            else:
                answer = 'Opps sorry, you beat the AI this time'
    else:
            answer = 'Opps sorry, you beat the AI this time'

    return answer
