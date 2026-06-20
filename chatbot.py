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
    if "hello" in words or "hi" in words:
        return "Hello! How can I help you today?"
    elif "hours" in words:
        return "We are open from 9 AM to 6 PM."
    elif "refund" in words:
        return "Refunds are processed within 5-7 business days."
    elif "cancel" in words:
        return "Orders can be cancelled before shipment."
    elif "payment" in words:
        return "We accept UPI, debit cards, credit cards, and net banking."
    elif "delivery" in words or "shipping" in words:
        return "Delivery usually takes 3-5 business days."
    elif "support" in words:
        return "Our support team is available 24/7 to assist you."
    elif "contact" in words:
        return "You can contact us at support@example.com."
    elif "discount" in words:
        return "Please check our website for current offers and discounts."
    elif "exchange" in words:
        return "Exchanges are allowed within 15 days of purchase with original packaging."
    elif "warranty" in words:
        return "Our products come with a 1-year manufacturer warranty."
    elif "invoice" in words:
        return "Your invoice is sent to your registered email after purchase."
    elif "tracking" in words:
        return "You can track your order using the tracking ID sent to your email."
    elif "location" in words:
        return "We are located at 123 Main Street. Visit us anytime during business hours."
    elif "product" in words:
        return "Please visit our website to browse our full range of products."
    elif "return" in words:
        return "Returns are accepted within 30 days of delivery in unused condition."
    elif "order" in words:
        return "Please provide your order ID for further assistance."
    else:
        return "Sorry, I don't understand your request. Please contact support@example.com."

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
