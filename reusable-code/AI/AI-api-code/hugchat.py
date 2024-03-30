from hugchat import hugchat
from hugchat.login import Login
import time
sign = Login("email", "password_for_huggingchat")
cookies = sign.login()
cookie_path_dir = "./cookies_snapshot"
sign.saveCookiesToDir(cookie_path_dir)
chatbot = hugchat.ChatBot(cookies=cookies.get_dict())
while True:
    id = chatbot.new_conversation() 
    chatbot.change_conversation(id)
    query_result = chatbot.query("What is the meaning of stream", web_search=True)
    print(query_result)
