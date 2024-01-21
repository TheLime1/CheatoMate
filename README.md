![cheatomate](https://raw.githubusercontent.com/TheLime1/CheatoMate/main/images/cheatomate.png)

# CheatoMate

## SCRIPTS

| Script                                           | Description                                                         | Setup                                            | Usage                               |
| ------------------------------------------------ | ------------------------------------------------------------------- | ------------------------------------------------ | ----------------------------------- |
| [ai_helper.py](./ai_helper.py)                   | GPT-4 AI chat in terminal                                           | [Bing Setup](#bing-setup)*                       | [Ai helper](#use-ai-helper)         |
| [network_card.py](./network_card.py)             | Activate/Deactivate network card with a shortcut                    | [Setup network_card.py](#setup-network_cardpy)   | [Network Card](#use-network-card)   |
| [chat/terminal_chat.py](./chat/terminal_chat.py) | Chat with your friends in terminal in real time                     | [Setup terminal-chat.py](#setup-terminal-chatpy) | [Terminal Chat](#use-terminal-chat) |
| [var_changer.py](./var_changer.py)               | Change the name of the variables/functions/classes in any code base | [Bing Setup](#bing-setup)*                       | [Var Changer](#use-var-changer)     |
| [exam2txt.py](./exam2txt.py)                     | Convert PDF and image files into text files                         | [Poe Setup](#poe-setup)                          | [Exam2txt](#use-exam2txt)           |

### **: not required*

## Installation

`pip install -r requirements.txt`

### Prerequisites

- Python 3.9+
- Microsoft account with access to bing copilot *(recommended but not required)*

## Setup

### Bing Setup

1. Go to the [Copilot web page](https://www.bing.com/copilot).
2. Open the developer tools in your browser (usually by pressing `F12` or right-clicking on the chat dialog and selecting Inspect).
3. Select the Network tab to view all requests sent to Copilot.
4. Write a message on the chat dialog that appears on the web page.
5. Find a request named `create?bundleVersion=XYZ` and click on it.
6. Scroll down to the requests headers section and copy the entire value after the `Cookie:` field.
7. Paste it to `config.ini`

> [!TIP]
> you can use Bing scripts without the cookies but you will have a limited number of requests (5 per chat session)

### Poe Setup

- Log into [Poe](https://poe.com/) on any web browser, then open your browser's developer tools (also known as "inspect") and look for the value of the `p-b` cookie in the following menus:
  - Chromium: Devtools > Application > Cookies > poe.com
  - Firefox: Devtools > Storage > Cookies
  - Safari: Devtools > Storage > Cookies

Paste the value of the `p-b` cookie into `config.ini`

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

1. first you need to activate the virtual environment


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

2. run `terminal_chat.py`
3. pick a nickname
4. start chatting !

### use Var Changer

1. put your codebase in a folder called `exam` in the same directory as `var_changer.py`
2. run `var_changer.py`
3. the script will modify the the codebase and zip it in a file called `modified.zip`

### use Exam2txt

This script is used to convert PDF and image files into text files using the Poe API. It takes a file path as an argument from the command line. If no file path is provided, it will look for PDF and image files in the current directory.

Here's how to use it:

1. Run the script from the command line with a file path as an argument. The file should be a PDF or an image file (JPEG, PNG, or JPG).

```bash
python exam2txt.py /path/to/your/file.pdf
```

2. If you don't provide a file path, the script will look for PDF and image files in the current directory.

```python
python exam2txt.py
```

3. The script will convert the provided file or the files in the current directory into text using the Poe API. If there are image files but no PDF files, it will first convert the images into a PDF file.
4. The extracted text will be saved in a text file with the same name as the original file.
