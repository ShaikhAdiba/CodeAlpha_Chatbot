print("simple chatbot")
print("type 'bye' to exit")
while True:
    user = input("you: ").lower()
    if user == "hello":
        print("bot: hi!")
    elif user == "how are you":
        print("bot: i am fine, thanks!")
    elif user == "what is your name":
          print("bot: my name is chatbot")
    elif user == "what can you do":
          print("bot: i can  answer simple questions. ")
    elif user == "bye":
        print("bot: goodbye!")
        break
    else:
        print("bot: i dont understand.")
