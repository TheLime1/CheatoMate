![cheatomate](https://github.com/TheLime1/CheatoMate/assets/47940043/902159e0-9ade-4fa9-8ef5-b209c68d92f2)

# CheatoMate

A collection of scripts to "help" you with your programming exams.

## Features

- Chat with Bing Copilot secretly in the terminal
- Export chat history to a txt file
- Activate/Destory your network adapter with a keyboard shortcut

## Installation

`pip install -r requirements.txt`

### Prerequisites

- Python 3.9+
- Microsoft account with access to bing copilot

### Setup

1. Go to the Copilot web page.
2. Open the developer tools in your browser (usually by pressing F12 or right-clicking on the chat dialog and selecting Inspect).
3. Select the Network tab to view all requests sent to Copilot.
4. Write a message on the chat dialog that appears on the web page.
5. Find a request named create?bundleVersion=XYZ and click on it.
6. Scroll down to the requests headers section and copy the entire value after the `Cookie:` field.
