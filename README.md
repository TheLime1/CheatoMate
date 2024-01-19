![cheatomate](https://raw.githubusercontent.com/TheLime1/CheatoMate/main/images/cheatomate.png)

# CheatoMate

## SCRIPTS

| Script                                           | Description                                                         | Setup                                            | Usage                               |
| ------------------------------------------------ | ------------------------------------------------------------------- | ------------------------------------------------ | ----------------------------------- |
| [ai_helper.py](./ai_helper.py)                   | GPT-4 AI chat in terminal                                           | [General Setup](#general-setup)*                 | [Ai helper](#use-ai-helper)         |
| [network_card.py](./network_card.py)             | Activate/Deactivate network card with a shortcut                    | [Setup network_card.py](#setup-network_cardpy)   | [Network Card](#use-network-card)   |
| [chat/terminal_chat.py](./chat/terminal_chat.py) | Chat with your friends in terminal in real time                     | [Setup terminal-chat.py](#setup-terminal-chatpy) | [Terminal Chat](#use-terminal-chat) |
| [var_changer.py](./var_changer.py)               | Change the name of the variables/functions/classes in any code base | [General Setup](#general-setup)*                 | [Var Changer](#use-var-changer)     |

### **: not required*

## Installation

`pip install -r requirements.txt`

### Prerequisites

- Python 3.9+
- Microsoft account with access to bing copilot



### Setup


#### General Setup

1. Go to the Copilot web page.
2. Open the developer tools in your browser (usually by pressing `F12` or right-clicking on the chat dialog and selecting Inspect).
3. Select the Network tab to view all requests sent to Copilot.
4. Write a message on the chat dialog that appears on the web page.
5. Find a request named `create?bundleVersion=XYZ` and click on it.
6. Scroll down to the requests headers section and copy the entire value after the `Cookie:` field.

> [!TIP]
> you can use the scripts without the cookies but you will have a limited number of requests (5 per chat session)

## Usage


#### Setup network_card.py 

- in terminal type `wmic nic get name, index` and find the name of your network adapter
-  paste it here
  https://github.com/TheLime1/CheatoMate/blob/ea9e3881472574d92c485539c8cda08fcfc16a8c/network_card.py#L22



### Setup terminal-chat.py

- run `chat/terminal_chat_setup.py`
- create your channel on https://dashboard.pusher.com/
- copy the credentials to the generated `.env` file



## Usage

### use Ai helper

- Run `python ai_helper.py` and chat with the FREE GPT-4 AI
- you can use custom commands like:

| Command | Usage                  |
| ------- | ---------------------- |
| !reset  | Start new conversation |
| !exit   | exit the code          |
| !paste  | paste clipboard        |
| !export | save chat to txt file  |

### use Network Card

- Run `python network_card.py` 
  - press `Numpad1` + `Numpad3` to deactivate your network adapter
  - press `Numpad7` + `Numpad9` to activate your network adapter

### use Terminal Chat

1- first you need to activate the virtual environment


Windows

```bash
# change to the generated terminal-chat directory
cd terminal-chat
# activate environment
Scripts\activate
```



Linux

```bash
# change to the generated terminal-chat directory
cd terminal-chat
# activate environment
source bin/activate
```




2- run `terminal_chat.py`

3- pick a nickname

4- start chatting !

### use Var Changer

-1 put your codebase in a folder called `exam` in the same directory as `var_changer.py`
2- run `var_changer.py`
3- the script will modify the the codebase and zip it in a file called `modified.zip`