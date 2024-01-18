![cheatomate](https://raw.githubusercontent.com/TheLime1/CheatoMate/main/images/cheatomate.png)

# CheatoMate

## Features

- Chat with Bing Copilot secretly in the terminal
- Export chat history to a txt file
- Activate/Deactivate your network adapter with a keyboard shortcut
- Chat with your friends in the terminal in real time

## Installation

`pip install -r requirements.txt`

### Prerequisites

- Python 3.9+
- Microsoft account with access to bing copilot

### Setup

<details>
<summary>Setup ai_helper.py </summary>

1. Go to the Copilot web page.
2. Open the developer tools in your browser (usually by pressing `F12` or right-clicking on the chat dialog and selecting Inspect).
3. Select the Network tab to view all requests sent to Copilot.
4. Write a message on the chat dialog that appears on the web page.
5. Find a request named `create?bundleVersion=XYZ` and click on it.
6. Scroll down to the requests headers section and copy the entire value after the `Cookie:` field.

</details>
<details>
<summary>Setup network_card.py </summary>

- in terminal type `wmic nic get name, index` and find the name of your network adapter
-  paste it here
  https://github.com/TheLime1/CheatoMate/blob/ea9e3881472574d92c485539c8cda08fcfc16a8c/network_card.py#L22
</details>

<details>
<summary>Setup terminal-chat.py</summary>

- run `chat/terminal_chat_setup.py`
- create your channel on https://dashboard.pusher.com/
- copy the credentials to the generated `.env` file

</details>

## Usage

### Ai helper

- Run `python ai_helper.py` and chat with the FREE GPT-4 AI
- you can use custom commands like:

| Command | Usage                  |
| ------- | ---------------------- |
| !reset  | Start new conversation |
| !exit   | exit the code          |
| !paste  | paste clipboard        |
| !export | save chat to txt file  |

### Network Card

- Run `python network_card.py` 
  - press `Numpad1` + `Numpad3` to deactivate your network adapter
  - press `Numpad7` + `Numpad9` to activate your network adapter

### Terminal Chat

1- first you need to activate the virtual environment

<details>
<summary>Windows</summary>

```bash
# change to the generated terminal-chat directory
cd terminal-chat
# activate environment
Scripts\activate
```

</details>
<details>
<summary>Linux</summary>

```bash
# change to the generated terminal-chat directory
cd terminal-chat
# activate environment
source bin/activate
```

</details>


2- run `terminal_chat.py`

3- pick a nickname

4- start chatting !