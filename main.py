import random
import traceback
import requests
import json
import time
import os


auth = ''
channelID = ''
headers = {
    'authorization': ''
}
rate = [
    "Super",
    "Common",
    "Uncommon",
    "Rare",
    "Legendary",
    "Shiny"
]
command = [
    "ub",
    "pb",
    "pb",
    "gb",
    "ub",
    "prb"
]
ball = [
    "Pokeballs",
    "Ultraballs",
    "Greatballs", 
    "Masterballs",
    "Premierballs"
]
data = {
    'content': ";p"
}
#requests.post(f'https://discord.com/api/v9/channels/{channelid}/messages', data=purge ,headers=headers)

spam = []

def send_request(content, channelID=channelID, headers=headers):
    try:
        data['content'] = content
        req = requests.post(
            f'https://discord.com/api/v9/channels/{channelID}/messages', data=data, headers=headers)
        msg = json.loads(req.text)
        msg_t = str(msg)
        with open("send_request.txt", "w", encoding="utf-8") as f:
            f.write(msg_t)
        f.close()
    except Exception as e:
        print("Error sending request", e.args)
        traceback.print_stack()
        os.system('warning.mp3')
        os.system('pause')


def checkCaptcha(channelID=channelID, headers=headers):
    try:
        rr = requests.get(
            f'https://discord.com/api/v9/channels/{channelID}/messages', headers=headers)
        message = json.loads(rr.text)

        if len(message) > 0:
            aa = str(message[0])
            with open("captcha.txt", "w", encoding="utf-8") as bb:
                bb.write(aa)
            bb.close()

            dm = "captcha"
            with open("captcha.txt", "r", encoding="utf-8") as bb:
                if bb.mode == "r":
                    contest2 = bb.read()
                    if dm in contest2:
                        print("CAPTCHA")
                        os.system('warning.mp3')
                        exit()
        else:
            plswait = "seconds"
            if plswait in message['content']:
                time.sleep(5)
    except Exception as e:
        print("CAPTCHA Exception", e.args)
        traceback.print_stack()
        os.system('warning.mp3')
        os.system('pause')
        exit(1)


def start(channelID=channelID, headers=headers):
    try:
        send_request(";p",channelID, headers)
        time.sleep(2)


        req = requests.get(
            f'https://discord.com/api/v9/channels/{channelID}/messages', headers=headers)

        msg = json.loads(req.text)
        if len(msg) > 0:
            embed = msg[0]['embeds'][0]['footer']['text']
            str_msg = str(embed)
            print(str_msg)
            with open("msg.txt", "w", encoding="utf-8") as f:
                f.write(str_msg)
            f.close()
            time.sleep(3)

            # 
            for i in range(0, len(rate)):
                if rate[i] in str_msg :
                    print(rate[i])
                    send_request(command[i],channelID, headers)
                    break
            time.sleep(10)

            send_request(random.choice(spam),channelID, headers)
            time.sleep(3)
            send_request(random.choice(spam),channelID, headers)
            time.sleep(3)
            send_request(random.choice(spam),channelID, headers)
            time.sleep(3)
            send_request(random.choice(spam),channelID, headers)
            time.sleep(3)
            send_request(random.choice(spam),channelID, headers)
            time.sleep(3)
            send_request(random.choice(spam),channelID, headers)
            time.sleep(5)
    except Exception as e:
        print("Error start request :", e.args)
        traceback.print_stack()
        os.system('warning.mp3')
        os.system('pause')
        exit(1)


def main():
    global auth
    global channelID
    global spam
    # print('Input your Discord Token:')
    # auth = input()
    # print('Input channelID to start auto:')
    # channelID = input()
    try:
        file = open('config.json', 'r', encoding="utf-8")
        data = json.load(file);
        auth = data['auth'];
        channelID = data['channelID'];
        spam = data['spam'];

    except Exception as e:
        print("Error read file :", e.args)
        traceback.print_stack()
        os.system('pause')
        exit(1)
    headers['authorization'] = auth
    # print(headers)
    # print(channelID)
    # print(spam)
    # send_request(";p",channelID, headers)
    captcha = 0
    while captcha == 0:
        start(channelID, headers)
        checkCaptcha(channelID, headers)


main()
