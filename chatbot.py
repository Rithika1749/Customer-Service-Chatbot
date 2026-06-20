
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

stop_words = set(stopwords.words('english'))

def preprocess(text):

    tokens = word_tokenize(text.lower())

    filtered_words = []

    for word in tokens:
        if word.isalnum() and word not in stop_words:
            filtered_words.append(word)

    return filtered_words
def get_response(user_input):

    words = preprocess(user_input)

    if "hours" in words:
        return "We are open from 9 AM to 6 PM."

    elif "refund" in words:
        return "Refunds are processed within 5-7 business days."

    elif "contact" in words:
        return "You can contact us at support@example.com."

    elif "order" in words:
        return "Please provide your order ID."

    elif "delivery" in words:
        return "Delivery usually takes 3-5 business days."

    elif "payment" in words:
        return "We accept UPI, debit cards, credit cards, and net banking."

    elif "discount" in words:
        return "Please check our website for current offers."

    elif "cancel" in words:
        return "Orders can be cancelled before shipment."

    elif "hello" in words or "hi" in words:
        return "Hello! How can I help you today?"

    else:
        return "Sorry, I don't understand your request."
def chatbot():

    print("Hello! I am your Customer Service Bot.")
    print("Type 'exit' to quit.\n")

    chat_history = []
    query_count = 0

    while True:

        user_input = input("You: ")

        if user_input.lower() == "exit":
            print("Bot: Thank you for chatting with us!")
            break

        query_count += 1

        response = get_response(user_input)

        print("Bot:", response)

        chat_history.append(f"User: {user_input}")
        chat_history.append(f"Bot: {response}")

    with open("chat_history.txt", "w") as file:
        for line in chat_history:
            file.write(line + "\n")

    print(f"\nTotal Queries Handled: {query_count}")
chatbot()
