import json
import requests
import gradio as gd

url = "http://localhost:11434/api/generate"

header = {
    'Content-Type':'application/json'
}

history = []

def generate_response(prompt):
    history.append(prompt)
    final_prompt = '\n'.join(history)
    data = {
        'model': 'CodeSuraj',
        'prompt': final_prompt,
        'stream': False
    }

    response = requests.post(url=url, headers=header, data=json.dumps(data))

    if response.status_code==200:
        response = response.text
        data = json.loads(response)
        actual_response = data['response']
        return actual_response
    else:
        print('error: ', response.text)


## Gradio Setup for frontend
interface = gd.Interface(
    fn=generate_response,
    inputs=gd.Textbox(lines=4, placeholder="Enter your prompt"),
    outputs=gd.Textbox(lines=4, type='text')
)
interface.launch()