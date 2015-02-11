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
        print("Sorry, I don't understand You.")