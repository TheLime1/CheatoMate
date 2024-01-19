import shutil
import os
import asyncio
from tqdm import tqdm

from sydney import SydneyClient

try:
    with open('bing_cookie.txt', 'r') as file:
        os.environ["BING_COOKIES"] = file.read()
except FileNotFoundError:
    print("Please create the bing_cookie.txt file, to get unlimited access to the API.")


async def main() -> None:
    # copy the code base to a new folder
    source = "exam"  # change this to the path of the code base
    if not os.path.exists(source):
        raise FileNotFoundError(
            f"The source directory '{source}' does not exist.")
    destination = "modified"  # change this to the path of the new folder
    # Check if the directory exists
    if os.path.exists(destination):
        # If it does, delete it
        shutil.rmtree(destination)
    shutil.copytree(source, destination)

    file_names = []
    for root, dirs, files in os.walk(destination):
        for file in files:
            file_names.append(os.path.join(root, file))

    async with SydneyClient(style="creative") as sydney:
        base_prompt = """
        # This is a base_prompt for renaming variables, functions, and classes in a code base.
        # The goal is to change the names according to the following rules:
        # - If the name is a single letter or a lowercase word, keep it as it is.
        # - If the name is a snake case word, remove the underscores and capitalize the first letter of each word.
        # - If the name is a camel case word, insert underscores before the uppercase letters and lowercase the name.
        # - Do not change the include or import statements.
        # - Delete all comments.
        # - Introduce grammar mistakes to the print statements.
        # Only generate the code, and nothing else.
        # - Rename the following code according to these rules:
        # For example:
        # - x -> x
        # - name -> name
        # - red_car -> RedCar
        # - RedCar -> red_car
        # - printName -> print_name
        # - print_name -> PrintName
        # - print("Hello, world!") -> print("Helo, word!")
        # - print("The answer is", 42) -> print("The answer are", forty_two)
        # - print(f"My name is {name}") -> print(f"Me name is {name}")
        # Rename the following code according to these rules:
        """
        for file_name in tqdm(file_names, desc="Processing files"):
            # read the file content
            with open(file_name, "r", encoding='utf-8') as f:
                file_content = f.read()
            # create the prompt for sydney.py
            prompt = base_prompt + "\n\n" + file_content
            # send the prompt to sydney.py
            response = await sydney.ask(prompt)
            # get the renamed content from the response
            renamed_content = response

            # *CLEAN UP THE RESPONSE*
            # split the response by the code block delimiter and get the second element
            renamed_content = renamed_content.split("```")[1]
            # strip any leading or trailing whitespace from the code
            renamed_content = renamed_content.strip()
            # remove first line of the file
            renamed_content = "\n".join(renamed_content.split("\n")[1:])
            # replace the old content with the renamed content
            with open(file_name, "w", encoding='utf-8') as f:
                f.write(renamed_content)

    # Zip the destination folder
    shutil.make_archive(destination, 'zip', destination)


if __name__ == "__main__":
    asyncio.run(main())
