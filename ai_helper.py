import asyncio
import os
import pyperclip
import datetime

from sydney import SydneyClient

try:
    with open('bing_cookie.txt', 'r') as file:
        os.environ["BING_COOKIES"] = file.read()
except FileNotFoundError:
    raise FileNotFoundError("Please create the bing_cookie.txt file.")


import datetime


async def main() -> None:
    chat_log = []
    async with SydneyClient(style="creative") as sydney:
        while True:
            prompt = input("You: ")

            if prompt == "!reset":
                await sydney.reset_conversation()
                chat_log = []
                continue
            elif prompt == "!exit":
                break
            elif prompt == "!paste":
                prompt = pyperclip.paste()
                print("You: ", prompt)
            elif prompt == "!export":
                timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
                with open(f"chat_log_{timestamp}.txt", "w", encoding="utf-8") as f:
                    f.write("\n".join(chat_log))
                print("Chat log exported.")
                continue

            print("Sydney: ", end="", flush=True)
            response_text = ""
            async for response in sydney.ask_stream(prompt):
                response_text += response
                print(response, end="", flush=True)
            print("\n")
            chat_log.append(f"You: {prompt}\nSydney: {response_text}")


if __name__ == "__main__":
    asyncio.run(main())
