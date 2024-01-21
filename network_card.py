import configparser
import pyuac
import subprocess
import keyboard

config = configparser.ConfigParser(interpolation=None)
config.read('config.ini')
adapter_name = config.get('HARDWARE', 'NETWORK_CARD')

if adapter_name == '"YOUR_NETWORK_CARD"':
    raise ValueError(
        "Please update the NETWORK_CARD value in the config.ini file.")


def enable_adapter(adapter_name):
    # Use wmic command to enable adapter
    subprocess.run(
        f"wmic path win32_networkadapter where name='{adapter_name}' call enable", shell=True)


def disable_adapter(adapter_name):
    # Use wmic command to disable adapter
    subprocess.run(
        f"wmic path win32_networkadapter where name='{adapter_name}' call disable", shell=True)


def main():
    # hotkeys to enable and disable adapter
    keyboard.add_hotkey("1+3", disable_adapter, args=(adapter_name,))
    keyboard.add_hotkey("7+9", enable_adapter, args=(adapter_name,))

    keyboard.wait()


# run with admin privileges
if __name__ == "__main__":
    if not pyuac.isUserAdmin():
        print("Re-launching as admin!")
        pyuac.runAsAdmin()
    else:
        main()  # Already an admin here.
