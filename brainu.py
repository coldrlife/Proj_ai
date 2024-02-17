from googlesearch import search
from transformers import GPT2LMHeadModel, GPT2Tokenizer

class SelfAdaptingBrainUI:
    def __init__(self):
        self.knowledge_base = {}

    def google_search(self, query):
        try:
            search_results = list(search(query, num=3, stop=3, pause=2))
            return search_results
        except Exception as e:
            print("Google search failed:", e)
            return []

    def chat_with_gpt(self, input_text):
        try:
            tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
            model = GPT2LMHeadModel.from_pretrained("gpt2")

            input_ids = tokenizer.encode(input_text, return_tensors="pt")

            output = model.generate(input_ids, max_length=50, num_return_sequences=1, no_repeat_ngram_size=2)

            response = tokenizer.decode(output[0], skip_special_tokens=True)

            return response
        except Exception as e:
            print("ChatGPT interaction failed:", e)
            return "I'm sorry, I couldn't understand that."

    def respond(self, user_input):
        if user_input.lower() == "exit":
            print("Goodbye!")
            return None

        if user_input in self.knowledge_base:
            response = self.knowledge_base[user_input]
        else:
            search_results = self.google_search(user_input)

            if search_results:
                response = f"I found some information for you: {', '.join(search_results)}"
            else:
                response = self.chat_with_gpt(user_input)

            self.knowledge_base[user_input] = response

        return response

def main():
    ai = SelfAdaptingBrainUI()

    while True:
        user_input = input("You: ")

        response = ai.respond(user_input)

        if response:
            print("AI:", response) 

if __name__ == "__main__":
    main()
