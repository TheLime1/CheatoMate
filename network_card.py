import pyuac
import subprocess
import keyboard


def enable_adapter(adapter_name):
    # Use wmic command to enable adapter
    subprocess.run(
        f"wmic path win32_networkadapter where name='{adapter_name}' call enable", shell=True)


def disable_adapter(adapter_name):
    # Use wmic command to disable adapter
    subprocess.run(
        f"wmic path win32_networkadapter where name='{adapter_name}' call disable", shell=True)


def main():
    # Get the name of the network adapter you want to control
    # You can use the command "wmic nic get name, index" to see the list of adapters and their names
    # Change this to your adapter name
    adapter_name = "COPY_YOUR_ADAPTER_NAME_HERE"

    # Define hotkeys to enable and disable adapter
    keyboard.add_hotkey("1+3", disable_adapter, args=(adapter_name,))
    keyboard.add_hotkey("7+9", enable_adapter, args=(adapter_name,))

    # Wait for hotkeys to be pressed
    keyboard.wait()


# run with admin privileges
if __name__ == "__main__":
    if not pyuac.isUserAdmin():
        print("Re-launching as admin!")
        pyuac.runAsAdmin()
    else:
        main()  # Already an admin here.
