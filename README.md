### How to get cookies
# Step 1: Get your Coursera Cookie
* Open your web browser (Chrome, Edge, or Firefox) and log in to Coursera.org.

* Open Developer Tools (Press F12 or Ctrl+Shift+I).

* Go to the Application tab (in Chrome/Edge) or Storage tab (in Firefox).

* Expand the Cookies section on the left and click on https://www.coursera.org.

* Find the cookie named CAUTH.

* Copy its Value (it will be a long string of random characters).

# Step 2: Add the Cookie to the Script
* Open the skipera-main folder on your computer.

* Look for a file named config.py.

* Open it with a text editor (like Notepad or VS Code).

cookies = {
    "CAUTH": "PASTE_YOUR_COPIED_VALUE_HERE"
}
Paste your CAUTH value inside the quotes.

Save the file.

## How to use
* Add your Gemini API Key if you wish to use the LLM to solve graded assignments. Use the `--llm` flag if you wish to solve graded assignments automatically.
* `python3 main.py --slug course-slug` where course-slug is present in the Coursera Course URL. Example: "introduction-psychology" (without the quotes) if the URL is https://www.coursera.org/learn/introduction-psychology/home/module/2
