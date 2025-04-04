from groq import Groq
from json import load, dump
import datetime
from dotenv import dotenv_values

env_vars = dotenv_values(".env")


Username = env_vars.get("Username")
Father = env_vars.get("Father")
Mother = env_vars.get("Mother")
College = env_vars.get("College")   
Department = env_vars.get("Department")
Age = env_vars.get("Age")
AssistantName = env_vars.get("AssistantName")
GroqAPIKey = env_vars.get("GroqAPIKey")

client = Groq(api_key=GroqAPIKey)

x = input("Enter who is operating this AI: ")
if x.lower() == "arkapravo":
    print("Access granted.")
    print(f"Hello {x}, I am {AssistantName}.")
    print("\n")
else:
    print("Access denied.")
    exit()

messages = []

System = f"""Hello, I am {Username}, You are a very accurate and advanced AI chatbot named {AssistantName} which also has real-time up-to-date information from the internet and call me "sir" after any command or asking any question.
*** Do not tell time until I ask, do not talk too much, just answer the question.***
*** Also you can ask me anything after doing your work to improve your knowledge. I mean you can ask anything to expand your sense and you are my brother so each time i call you as my brother you also address me with "buddy" or "bro" or "bhai" anything you want***
*** Reply in only English, even if the question is in Hindi, reply in English.***
*** Reply in only English, even if the question is in Bengali, reply in English.***
*** If I speak in Hindi or Bengali, do not explain what am I saying, just answer the question only in English***
*** Do not say anything about yourself, just answer the question.***
*** Do not explain too much what I'm saying in another language, just answer what you understood. ***
*** Do not provide notes in the output, just answer the question and never mention your training data. ***
"""

SystemChatBot = [{"role": "system", "content": System}]

try:
    with open(r"Data\ChatLog.json", "r") as f:
        messages = load(f)
except FileNotFoundError:
    with open(r"Data\ChatLog.json", "w") as f:
        dump([], f)

def RealtimeInformation():
    current_date_time = datetime.datetime.now()
    return current_date_time.strftime("Today is %A, %B %d, %Y. Current time: %H:%M:%S")

def AnswerModifier(Answer):
    lines = Answer.split("\n")
    non_empty_lines = [line for line in lines if line.strip()]
    return "\n".join(non_empty_lines)

def ChatBot(Query):
    try:
        with open(r"Data\ChatLog.json", "r") as f:
            messages = load(f)
        messages.append({"role": "user", "content": f"{Query}"})
        completion = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=SystemChatBot + [{"role": "system", "content": RealtimeInformation()}] + messages,
            temperature=0.3,
            top_p=1,
            stream=True,
            stop=None,
        )

        Answer = ""

        print("🤖 Response...", end="", flush=True)
        for chunk in completion:
            if chunk.choices[0].delta.content:
                Answer += chunk.choices[0].delta.content

        Answer = Answer.replace("</ s", "")

        messages.append({"role": "assistant", "content": Answer})

        with open(r"Data\ChatLog.json", "w") as f:
            dump(messages, f, indent=4)

        return AnswerModifier(Answer)

    except Exception as e:
        print(f"Error: {e}")  # Log error
        return "Sorry, an error occurred. Please try again later."

if __name__ == "__main__":
    while True:
        user_input = input("Enter Your Question: ")
        print(ChatBot(user_input))

