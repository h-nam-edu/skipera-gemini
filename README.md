# Skipera
Tool to skip Coursera courses, forked from https://github.com/serv0id/skipera, but uses Gemini instead of Perplexity for auto-solving tests.

## 🚀 Installation

Open your terminal or command prompt in the root folder and run:

```bash
pip install -r requirements.txt

```

## 🔑 Setup Guide

### Step 1: Get Your Coursera Cookie

1. Log in to [Coursera.org](https://www.coursera.org) in your web browser (Chrome, Edge, or Firefox).
2. Open **Developer Tools** (Press `F12` or `Ctrl+Shift+I`).
3. Navigate to the **Application** tab (Chrome/Edge) or **Storage** tab (Firefox).
4. In the left sidebar, expand **Cookies** and select `https://www.coursera.org`.
5. Locate the cookie named `CAUTH`.
6. Copy the **Value** (a long string of alphanumeric characters).

### Step 2: Configure the Script

1. Open the `skipera-main` folder.
2. Open `config.py` with a text editor (VS Code, Notepad, etc.).
3. Update the `cookies` variable with your copied value:
```python
cookies = { "CAUTH": "PASTE_YOUR_COPIED_VALUE_HERE" }

```

4. **Optional:** Add your **Gemini API Key** in the designated field within `config.py` if you intend to use AI features for assignments.
```python
PERPLEXITY_API_KEY = "YOUR_API_HERE"

```
5. Save and close the file.

## 🛠 Usage
### ⚠️⚠️⚠️Make sure that you have already enrolled in the course, otherwise the script won't work.⚠️⚠️⚠️

To run the script, you need the **course slug**. This is the part of the Coursera URL immediately following `/learn/`.

* **Example URL:** `https://www.coursera.org/learn/introduction-psychology/home/...`
* **Course Slug:** `introduction-psychology`

### Standard Run

```bash
python main.py --slug introduction-psychology

```

### Automatic Assignment Solving (LLM)

To automatically solve graded assignments using the Gemini API, add the `--llm` flag:

```bash
python main.py --slug introduction-psychology --llm

```

Also, you can use the `--ungraded` flag to do ungraded assignments. For some courses that require you to complete the entire module first to take the final assignment.

```bash
python main.py --slug introduction-psychology --llm --ungraded

```
