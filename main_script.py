# # main_script.py
# from ai_module import SelfAdaptingBrainUI
# from gtts import gTTS
# import os

# def text_to_speech(text, filename="output.mp3"):
#     try:
#         tts = gTTS(text=text, lang='en')
#         tts.save(filename)
#         os.system("start " + filename)  # Adjust this command based on your OS
#     except Exception as e:
#         print(f"Error during text-to-speech conversion: {e}")

# def main():
#     print("Welcome to the Self-Adapting AI. Type 'exit' to end the conversation.")

#     ai = SelfAdaptingBrainUI()

#     while True:
#         user_input = input("You: ")

#         if user_input.lower() == 'exit':
#             print("Goodbye!")
#             break

#         print("AI: Processing...")
#         response = ai.respond(user_input)

#         if response:
#             print("AI:", response)
#             text_to_speech(response)
#         else:
#             print("AI: I don't have a response for that.")

# if __name__ == "__main__":
#     main()


import tkinter as tk
from ai_module import SelfAdaptingBrainUI
from gtts import gTTS
import os

class SelfAdaptingAIGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Self-Adapting AI")
        self.geometry("400x300")

        self.ai = SelfAdaptingBrainUI()

        self.input_label = tk.Label(self, text="You:")
        self.input_label.pack()

        self.user_input = tk.Entry(self)
        self.user_input.pack()

        self.output_label = tk.Label(self, text="AI:")
        self.output_label.pack()

        self.response_text = tk.Text(self, height=5, width=40)
        self.response_text.pack()

        self.submit_button = tk.Button(self, text="Submit", command=self.process_input)
        self.submit_button.pack()

    def process_input(self):
        user_input = self.user_input.get()

        if user_input.lower() == 'exit':
            self.destroy()
        else:
            response = self.ai.respond(user_input)

            if response:
                self.response_text.delete(1.0, tk.END)
                self.response_text.insert(tk.END, response)
                self.text_to_speech(response)
            else:
                self.response_text.delete(1.0, tk.END)
                self.response_text.insert(tk.END, "I don't have a response for that.")

    def text_to_speech(self, text, filename="output.mp3"):
        try:
            tts = gTTS(text=text, lang='en')
            tts.save(filename)
            os.system("start " + filename)  # Adjust this command based on your OS
        except Exception as e:
            print(f"Error during text-to-speech conversion: {e}")

def main():
    app = SelfAdaptingAIGUI()
    app.mainloop()

if __name__ == "__main__":
    main()
