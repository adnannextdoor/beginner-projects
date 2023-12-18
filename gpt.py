from openai import OpenAI

client = OpenAI(api_key="") # insert API key from OpenAI here


messages = []
system_msg = input("What type of chatbot would you like to create?\n")
messages.append({"role": "user", "content": system_msg})

print("Adnan GPT is ready to use!")
while input != "quit()":
    message = input()
    messages.append({"role": "user", "content": message})
    response = client.chat.completions.create(model="gpt-3.5-turbo",
    messages=messages)
    reply = response.choices[0].message.content
    messages.append({"role": "assistant", "content": reply})
    print("\n" + reply + "\n")
