import gradio as gr
import openai, config, subprocess
openai.api_key = config.OPENAI_API_KEY



messages = [{"role": "system", "content": 'ENTER_YOUR_CONTEXT_HERE'}]

# examples of few content  - content is basically the context you are setting for your conversation with Harvis :D 
# Ex1: You are a Storage Solutions Expert. Respond to all input in 100 words or less.
# Ex2: You are a financial Advisor. Response in more than 500 words.
# Ex3: You are a nutritionist expert.


def transcribe(audio):
    global messages

    audio_file = open(audio, "rb")
    transcript = openai.Audio.transcribe("whisper-1", audio_file)

    messages.append({"role": "user", "content": transcript["text"]})

    response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)

    system_message = response["choices"][0]["message"]
    messages.append(system_message)

    subprocess.call(["say", system_message['content']])

    chat_transcript = ""
    for message in messages:
        if message['role'] != 'system':
            chat_transcript += message['role'] + ": " + message['content'] + "\n\n"

    return chat_transcript

ui = gr.Interface(fn=transcribe, inputs=gr.Audio(source="microphone", type="filepath"), outputs="text").launch()
ui.launch()