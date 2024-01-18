# import the required modules
import os
import subprocess
from termcolor import colored

# install virtualenv if not already installed
try:
    import virtualenv
except ImportError:
    subprocess.run(["sudo", "pip", "install", "virtualenv"])

# create a new environment with virtualenv
subprocess.run(["virtualenv", "terminal-chat"])

# activate the environment
if os.name == "posix":  # for Linux and Mac
    subprocess.run(["source", "terminal-chat/bin/activate"], shell=True)
else:  # for Windows
    subprocess.run(["terminal-chat\\Scripts\\activate"], shell=True)

# install the libraries
subprocess.run(["pip", "install", "termcolor", "pusher",
               "git+https://github.com/nlsdfnbch/Pysher.git", "python-dotenv"])

# create a new .env file with the pusher app credentials
with open(".env", "w") as f:
    f.write(f"PUSHER_APP_ID=YOUR_APP_ID\n")
    f.write(f"PUSHER_APP_KEY=YOUR_APP_KEY\n")
    f.write(f"PUSHER_APP_SECRET=YOUR_APP_SECRET\n")
    f.write(f"PUSHER_APP_CLUSTER=YOUR_APP_CLUSTER\n")


print(colored("**********************************************************************", "green"))
print(colored("The environment is ready and the pusher app credentials template is created.", "green"))
print(colored("go to https://dashboard.pusher.com/ and copy the app credentials to the .env file", "green"))
