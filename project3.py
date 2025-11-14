import tkinter as tk
from tkinter import scrolledtext
import random

# Knowledge base
responses = {
    "hello": ["Hello! How can I assist you today?"],
    "how are you": ["I'm just a program, but thanks for asking!"],
    "what is your name": ["I'm ChatBot, your virtual assistant."],
    "bye": ["Goodbye! Have a great day!"]
}

def get_response(user_msg):
    user_msg = user_msg.lower()
    for key in responses:
        if key in user_msg:
            return random.choice(responses[key])
    return "I'm sorry, I don't understand."

def send_message():
    user_msg = entry.get()
    if user_msg.strip() == "":
        return
    chat_window.insert(tk.END, "You: " + user_msg + "\n", "user")
    entry.delete(0, tk.END)
    bot_msg = get_response(user_msg)
    chat_window.insert(tk.END, "Bot: " + bot_msg + "\n", "bot")

# GUI setup
root = tk.Tk()
root.title("ChatBot")
root.geometry("450x500")

chat_window = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=50, height=20, font=("Arial", 12))
chat_window.pack(pady=10)
chat_window.tag_config("user", foreground="blue")
chat_window.tag_config("bot", foreground="green")
chat_window.config(state=tk.DISABLED)

# Frame for entry and button
input_frame = tk.Frame(root)
input_frame.pack(pady=5)

entry = tk.Entry(input_frame, width=30, font=("Arial", 14))
entry.pack(side=tk.LEFT, padx=5)

send_button = tk.Button(input_frame, text="Send", command=send_message, width=10, bg="lightblue")
send_button.pack(side=tk.LEFT)

# Enable chat window updates
def enable_chat():
    chat_window.config(state=tk.NORMAL)

def disable_chat():
    chat_window.config(state=tk.DISABLED)

# Wrap send_message with state toggling
def send_message_wrapper():
    enable_chat()
    send_message()
    disable_chat()

send_button.config(command=send_message_wrapper)

root.mainloop()