import random

file_name=open(r"name.text","r")
name_ai=file_name.read()
file_name.close()

file=open(r"name1.txt","r")
name=file.read()
file.close()

Hello=["hello","hi","hey","hii","what's up"]

Reply_hello=["hello sir","hey,what's up","hey how are you","heelo sir nice to meet you again"]

Bye=["bye","exit","sleep","go","turn off"]

Reply_Bye=["bye sir","thanks for using me","haapy to help you","okay"]

How_are_you=["how are you","are you fine","what about your health","are you ok"]

Reply_How_are_you=["i am fine","i am absolutely fine sir.thank you for asking","i am fine sir.how about you","go to go"]

Nice=["well","fine","i am ok","i am fine","nice","great","thanks"]

Reply_Nice=["good to hear that","glad to hear that you are fine","glad to hear that"]

Functions=["functions","abilities","what can you do","what can you do for me","features"]

Reply_Functions=["i can perform many task, how can i help you","let me ask you waht can I do for you"]

Sorry_Reply=["that beyond my abilites","sorry i can not do that yet","sorry i can not do that","sorry that's above me"]

# Your_Name=[name_ai]
# My_name=[name]

list=["what is your name","tell me your name"]

list2=["what is my name","tell me my name"]

def Chatbot(Text):

    word=Text


    if word in Hello:

        reply=random.choice(Reply_hello)
        return reply

    elif word in Bye:

        reply=random.choice(Reply_Bye)
        return reply

    elif word in Functions:

        reply=random.choice(Reply_Functions)
        return reply

    elif word in How_are_you:

        reply=random.choice(Reply_How_are_you)
        return reply

    elif word in Nice:

        reply=random.choice(Reply_Nice)
        return reply

    elif word in list:

        file_name=open(r"name.text","r")
        name_ai=file_name.read()
        file_name.close()

        return name_ai

    elif word in list2:

        file=open(r"name1.txt","r")
        name=file.read()
        file.close()

        return name

    else:

        reply=random.choice(Sorry_Reply)
        return reply

def Sorry():

    sorry_reply=random.choice(Sorry_Reply)
    return sorry_reply

