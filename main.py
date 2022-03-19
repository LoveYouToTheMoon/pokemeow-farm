import traceback
import requests
import json
import time
import os


auth = 'NzAyMTI0MzEyNjgwODU3NjIx.YigwMQ.qLUTpJWrEKTz5S0Tb_uB7SkCTbY'
channelID = '954290890204135484'
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


def send_request(content, channelID=channelID, auth=auth):
    try:
        headers['authorization'] = auth
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


def checkCaptcha():
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


def start():
    try:
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
            time.sleep(6)

            # 
            for i in range(0, len(rate)):
                if rate[i] in str_msg :
                    print(rate[i])
                    send_request(command[i])
                    break
            time.sleep(10)
            send_request(";p")
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
    # print('Input your Discord Token:')
    # auth = input()
    # print('Input channelID to start auto:')
    # channelID = input()
    headers['authorization'] = auth

    send_request(';p')
    captcha = 0
    while captcha == 0:
        start()
        checkCaptcha()


main()
