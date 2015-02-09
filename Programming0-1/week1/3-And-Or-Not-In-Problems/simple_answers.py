__author__ = 'Боян'

conversation = True
while conversation:
    text = input("Say something, friend ...")
    if "hello" in text or "Hello" in text:
        print("Hello there, good stranger!")
    elif "how are you?" in text:
        print("I am fine, thanks. How are You?")
    elif "feelings" in text:
        print("I am a machine. I have no feelings")
    elif "age" in text:
        print("I have no age. Only current timestamp")
    elif "bye" in text:
        print("Have a nice day !")
        conversation = False
    else:
        print(
            "Sorry, I don't understand You. I follow these laws:\n0. A robot may not harm humanity, or, by inaction, allow humanity to come to harm.\n1. A robot may not injure a human being or, through inaction, allow a human being to come to harm.\n2. A robot must obey the orders given it by human beings, except where such orders would conflict with the First Law.\n3. A robot must protect its own existence as long as such protection does not conflict with the First or Second Law.")