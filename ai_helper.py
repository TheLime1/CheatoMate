import configparser
import asyncio
import os
import pyperclip
import datetime

from sydney import SydneyClient

# Read the API key from the config.ini file
config = configparser.ConfigParser(interpolation=None)
config.read('config.ini')
bing_key = config.get('KEYS', 'BING_KEY')

if bing_key == '"YOUR_BING_KEY"':
    print("Warning: Please replace 'YOUR_BING_KEY' with your actual BING key in the config.ini file, to get unlimited requests.")


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
