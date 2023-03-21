import openai
from time import sleep
import re
import os

with open('openai_api_key.txt', 'r') as infile:
    openai.api_key = infile.read()

def gpt3_completion(prompt, engine='text-davinci-003', temp = 0.5, tokens=1000, top_p=1, freq_pen=0, pres_pen=0, stop=['lklklk']):
    max_retry = 5
    retry = 0
    while True: # "while true" is an infinite loop
        try:
            response = openai.Completion.create(
                engine=engine,
                #model=engine
                prompt=prompt,
                temperature=temp,
                frequency_penalty=freq_pen,
                presence_penalty=pres_pen,
                max_tokens=tokens,
                stop=stop,
                top_p=top_p)
            text = response['choices'][0]['text'].strip()
            return text
        except Exception as oops:
            retry += 1
            if retry >= max_retry:
                return None
            print('Error communicating with OpenAi:', oops)
            sleep(1)

if __name__ == "__main__":
    for i in range(0, 10):
        with open('prompt.txt', 'r' ) as infile:
            prompt = infile.read()
        answer = gpt3_completion(prompt)
        print('\n\n\n', answer)
        filename = "link_%s.txt" % i
        with open ('links/%s' % filename, 'w', encoding='utf-8') as outfile:
            outfile.write(answer)
            #exit(0)   use exit(0) to test if generation works