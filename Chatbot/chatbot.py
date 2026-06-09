print("welcome!")
print("here's your personal assistant!")
print("how can i help you?")

reponses={"hello":["hello","hi","hey"],
"doing well..and you?":["how are you","how are you doing"],
"great!👍":["doing well!","good!"],
"I'm sheley,your personal assistant😊":["what is your name?","who are you?"],
"i can tell a joke,motivate you...what can i help you with?":["help","what can you do?"],
"Every expert was once a beginner. Keep learning and never give up!💪":["motivate me","give me motivation"],
"😂here's the one: Why do programmers prefer dark mode? Because light attracts bugs!🐞":["tell me a joke","joke"]}

chat=input("").lower()
while(True):
    latest=[]
    if(chat=="bye"):
        print("bye👋")
        break
    for key,value in reponses.items():
        if chat in value:
            print(key)
            latest.append(key)
    if(len(latest)==0):
        print("sorry i didn't understand!")
        latest.clear()
    chat=input("").lower()

