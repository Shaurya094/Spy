import colorama
from colorama import Fore, Style
from textblob import TextBlob

colorama.init()

print (f"{Fore.CYAN} Welcome to the Sentiment Spy! {Style.RESET_ALL}")

username = input(f"{Fore.MAGENTA} Please enter your name: {Style.RESET_ALL}").strip()
if not username:
    username = "Mystery Agent"

convo_his = []
print (f"\n{Fore.CYAN}Hello, Agent {username}")
print (f"Type a sentence and I'll analya your responses to guess your mood!")
print (f" Type {Fore.YELLOW}'reset' {Fore.CYAN}, {Fore.YELLOW}'history'{Fore.CYAN}, or {Fore.YELLOW}'exit'{Fore.CYAN} to quit.{Style.RESET_ALL}\n")

while True:
    user_input = input(f"{Fore.GREEN}>> {Style.RESET_ALL}").strip()

    if not user_input:
        print(f"{Fore.RED}Please enter a text/a valid command {Style.RESET_ALL}.")
        continue

    if user_input.lower() == "exit":
        print (f"\n{Fore.BLUE} Exiting Sentiment Spy, Farewell Agent {username}!")
        break

    elif user_input.lower() == "history":
        if not convo_his:
            print(f"{Fore.YELLOW}No conversation history yet.{Style.RESET_ALL}")
        else:
            print(f"{Fore.CYAN} Conversation History:{Style.RESET_ALL}")
            for idx, (text, polarity, sentiment_type) in enumerate (convo_his, start=1):
                if sentiment_type == "Positive":
                    color = Fore.GREEN
                if sentiment_type == "Negative":
                    color = Fore.RED
                else:
                    color = Fore.YELLOW
                print(f"{idx}. {color} {text} (Polarity: {polarity: .2f}, {sentiment_type}){Style.RESET_ALL}")
        continue

    polarity = TextBlob(user_input).sentiment.polarity
    if polarity > 0.25:
        sentiment_type == "Positive"
        color = Fore.GREEN
    elif polarity < -0.25:
        sentiment_type == "Negative"
        color = Fore.RED
    else:
        sentiment_type = "Neutral"
        color = Fore.YELLOW

    convo_his.append((user_input, polarity, sentiment_type))

    print(f"{color} {sentiment_type} sentiment detected! (Polarity: {polarity: .2f}) {Style.RESET_ALL}")