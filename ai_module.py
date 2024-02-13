# # ai_module.py
# from google_search_module import GoogleSearchModule
# from transformers import GPT2LMHeadModel, GPT2Tokenizer
# from gtts import gTTS
# import os

# class SelfAdaptingBrainUI:
#     def __init__(self):
#         self.knowledge_base = {}
#         self.google_search_module = GoogleSearchModule()
#         self.tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
#         self.model = GPT2LMHeadModel.from_pretrained("gpt2")

#     def chat_with_gpt(self, input_text):
#         input_ids = self.tokenizer.encode(input_text, return_tensors="pt")
#         output = self.model.generate(input_ids, max_length=50, num_return_sequences=1, no_repeat_ngram_size=2)
#         response = self.tokenizer.decode(output[0], skip_special_tokens=True)
#         return response

#     def text_to_speech(self, text, filename="output.mp3"):
#         try:
#             tts = gTTS(text=text, lang='en')
#             tts.save(filename)
#             # Consider using a more platform-independent method to play audio
#             os.system("start " + filename)
#         except Exception as e:
#             print(f"Error during text-to-speech conversion: {e}")

#     def respond(self, user_input):
#         try:
#             if user_input.lower() == "exit":
#                 print("Goodbye!")
#                 return None

#             if user_input in self.knowledge_base:
#                 response = self.knowledge_base[user_input]
#             else:
#                 print("AI: Searching the web...")
#                 search_result = self.google_search_module.search(user_input)

#                 if search_result:
#                     response = f"I found some information for you: {', '.join(search_result)}"
#                 else:
#                     print("AI: Generating a response...")
#                     response = self.chat_with_gpt(user_input)

#                 self.knowledge_base[user_input] = response

#             print("AI:", response)
#             self.text_to_speech(response)

#             return response
#         except Exception as e:
#             print(f"An error occurred: {e}")
#             return "Sorry, I encountered an error. Please try again."

import tkinter as tk
from google_search_module import GoogleSearchModule
from transformers import GPT2LMHeadModel, GPT2Tokenizer
from gtts import gTTS
import os

class SelfAdaptingBrainUI:
    def __init__(self, master=None):
        self.master = master
        self.knowledge_base = {}
        self.google_search_module = GoogleSearchModule()
        self.tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
        self.model = GPT2LMHeadModel.from_pretrained("gpt2")

        self.create_widgets()

    def create_widgets(self):
        self.user_input_label = tk.Label(self.master, text="You:")
        self.user_input_label.pack()

        self.user_input_entry = tk.Entry(self.master)
        self.user_input_entry.pack()

        self.response_label = tk.Label(self.master, text="AI:")
        self.response_label.pack()

        self.response_text = tk.Text(self.master, height=5, width=40)
        self.response_text.pack()

        self.submit_button = tk.Button(self.master, text="Submit", command=self.respond_to_user_input)
        self.submit_button.pack()

    def chat_with_gpt(self, input_text):
        input_ids = self.tokenizer.encode(input_text, return_tensors="pt")
        output = self.model.generate(input_ids, max_length=50, num_return_sequences=1, no_repeat_ngram_size=2)
        response = self.tokenizer.decode(output[0], skip_special_tokens=True)
        return response

    def text_to_speech(self, text, filename="output.mp3"):
        try:
            tts = gTTS(text=text, lang='en')
            tts.save(filename)
            os.system("start " + filename)
        except Exception as e:
            print(f"Error during text-to-speech conversion: {e}")

    def respond_to_user_input(self):
        user_input = self.user_input_entry.get()
        self.user_input_entry.delete(0, tk.END)  # Clear the entry field after submission

        if user_input.lower() == "exit":
            print("Goodbye!")
            return

        try:
            if user_input in self.knowledge_base:
                response = self.knowledge_base[user_input]
            else:
                print("AI: Searching the web...")
                search_result = self.google_search_module.search(user_input)

                if search_result:
                    response = f"I found some information for you: {', '.join(search_result)}"
                else:
                    print("AI: Generating a response...")
                    response = self.chat_with_gpt(user_input)

                self.knowledge_base[user_input] = response

            print("AI:", response)
            self.response_text.delete(1.0, tk.END)  # Clear previous response
            self.response_text.insert(tk.END, response)
            self.text_to_speech(response)

        except Exception as e:
            print(f"An error occurred: {e}")
            response = "Sorry, I encountered an error. Please try again."
            self.response_text.delete(1.0, tk.END)
            self.response_text.insert(tk.END, response)

def main():
    root = tk.Tk()
    root.title("Self-Adapting AI")
    app = SelfAdaptingBrainUI(master=root)
    root.mainloop()

if __name__ == "__main__":
    main()

