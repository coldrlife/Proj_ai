# from googlesearch import search
# from gtts import gTTS
# import os

# class GoogleSearchModule:
#     def search(self, query):
#         try:
#             search_results = list(search(query, num=3, stop=3, pause=2))

#             if search_results:
#                 response = f"I found some information for you: {', '.join(search_results)}"
#                 print("AI:", response)
#                 self.text_to_speech(response)
#                 return search_results
#             else:
#                 return None
#         except Exception as e:
#             print(f"Google search error: {e}")
#             return None

#     def text_to_speech(self, text, filename="output.mp3"):
#         tts = gTTS(text=text, lang='en')
#         tts.save(filename)
#         os.system("start " + filename)

import tkinter as tk
from googlesearch import search
from gtts import gTTS
import os

class GoogleSearchGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Google Search")
        self.geometry("400x300")

        self.search_module = GoogleSearchModule()

        self.query_label = tk.Label(self, text="Enter your query:")
        self.query_label.pack()

        self.query_entry = tk.Entry(self)
        self.query_entry.pack()

        self.search_button = tk.Button(self, text="Search", command=self.search)
        self.search_button.pack()

    def search(self):
        query = self.query_entry.get()
        if query:
            search_results = self.search_module.search(query)
            if search_results:
                print("Search Results:", search_results)
            else:
                print("No search results found for:", query)

class GoogleSearchModule:
    def search(self, query):
        try:
            search_results = list(search(query, num=3, stop=3, pause=2))

            if search_results:
                response = f"I found some information for you: {', '.join(search_results)}"
                print("AI:", response)
                self.text_to_speech(response)
                return search_results
            else:
                return None
        except Exception as e:
            print(f"Google search error: {e}")
            return None

    def text_to_speech(self, text, filename="output.mp3"):
        tts = gTTS(text=text, lang='en')
        tts.save(filename)
        os.system("start " + filename)

def main():
    app = GoogleSearchGUI()
    app.mainloop()

if __name__ == "__main__":
    main()
