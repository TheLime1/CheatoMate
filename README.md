![cheatomate](https://raw.githubusercontent.com/TheLime1/CheatoMate/main/images/cheatomate.png)

# CheatoMate

## Features

- Chat with Bing Copilot secretly in the terminal
- Export chat history to a txt file
- Activate/Deactivate your network adapter with a keyboard shortcut

## Installation

`pip install -r requirements.txt`

### Prerequisites

- Python 3.9+
- Microsoft account with access to bing copilot

### Setup

<details>
<summary>Setup chat.py </summary>

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
