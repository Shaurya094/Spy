#I changed the colours of the text
import colorama
from colorama import Fore, Style
from textblob import TextBlob

colorama.init()

print (f"{Fore.GREEN} Welcome to the Sentiment Spy! {Style.RESET_ALL}")

username = input(f"{Fore.RED} Please enter your name: {Style.RESET_ALL}").strip()
if not username:
    username = "Mystery Agent"

convo_his = []
print (f"\n{Fore.GREEN}Hello, Agent {username}")
print (f"Type a sentence and I'll analya your responses to guess your mood!")
print (f" Type {Fore.LIGHTRED_EX}'reset' {Fore.LIGHTBLUE_EX}, {Fore.BLACK}'history'{Fore.GREEN}, or {Fore.LIGHTGREEN_EX}'exit'{Fore.LIGHTYELLOW_EX} to quit.{Style.RESET_ALL}\n")

while True:
    user_input = input(f"{Fore.CYAN}>> {Style.RESET_ALL}").strip()

    if not user_input:
        print(f"{Fore.LIGHTRED_EX}Please enter a text/a valid command {Style.RESET_ALL}.")
        continue

    if user_input.lower() == "exit":
        print (f"\n{Fore.WHITE} Exiting Sentiment Spy, Farewell Agent {username}!")
        break

    elif user_input.lower() == "history":
        if not convo_his:
            print(f"{Fore.LIGHTWHITE_EX}No conversation history yet.{Style.RESET_ALL}")
        else:
            print(f"{Fore.YELLOW} Conversation History:{Style.RESET_ALL}")
            for idx, (text, polarity, sentiment_type) in enumerate (convo_his, start=1):
                if sentiment_type == "Positive":
                    color = Fore.RED
                if sentiment_type == "Negative":
                    color = Fore.GREEN
                else:
                    color = Fore.LIGHTCYAN_EX
                print(f"{idx}. {color} {text} (Polarity: {polarity: .2f}, {sentiment_type}){Style.RESET_ALL}")
        continue

    polarity = TextBlob(user_input).sentiment.polarity
    if polarity > 0.25:
        sentiment_type == "Positive"
        color = Fore.YELLOW
    elif polarity < -0.25:
        sentiment_type == "Negative"
        color = Fore.GREEN
    else:
        sentiment_type = "Neutral"
        color = Fore.RED

    convo_his.append((user_input, polarity, sentiment_type))

    print(f"{color} {sentiment_type} sentiment detected! (Polarity: {polarity: .2f}) {Style.RESET_ALL}")