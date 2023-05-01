from selenium import webdriver
import requests
from bs4 import BeautifulSoup
import openai


openai.api_key = "YOUR API KEY"
messages = [
    {"role": "system", "content": "You rephrase the given text"},
]
#Getting the input
def get_input():
    need = input("Enter your need:")
    return need

def func(s):
    driver = webdriver.Chrome("chromedriver.exe")
    driver.get("https://www.wikipedia.org/wiki/{}".format(s))
    html_doc = requests.get(url="https://en.wikipedia.org/wiki/{}".format(s)).text
    soup = BeautifulSoup(html_doc, 'html.parser')
    content = ''
    for data in soup.find_all("p"):
        content += data.get_text()
    return content

def file(result):
    file_name = input("Enter the file name")
    text_file = open(file_name, "w", encoding="utf-8")
    text_file.write(result)
    text_file.close()


#new function
def rephrase(text):

    message = text
    if message:
        messages.append(
            {"role": "user", "content": message},
        )
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages
        )

    reply = chat.choices[0].message.content
    messages.append({"role": "assistant", "content": reply})
    return reply


s = get_input()
result = func(s)
r = int(input("Do you want to rephrase"))
if(r == 1):
    rephrased_text = rephrase(result)
    print("The content has been rephrased")
    re = int(input("Do you want it in a file"))
    if(re == 1):
        file(rephrased_text)
    else:
        print(rephrased_text)




