## II. Setting up Python Environment 

### A. What is an IDE?

* **IDE (Integrated Development Environment):** A software application for writing, editing, and running code. Popular for Python: PyCharm, VS Code, Thonny.
* **Jupyter Notebooks:** Interactive coding environment, great for data science, visualization, and prototyping.

---

### B. Step 1: Install Python (Required for all IDEs)

1. **Go to [python.org/downloads](https://www.python.org/downloads/).**
2. **Download the latest version** (recommended: Python 3.x).
3. **Run the installer:**

   * On Windows: Select “Add Python to PATH” **before** clicking “Install Now.”
   * On macOS: Drag the Python icon to Applications.
   * On Linux: Most distributions have Python pre-installed; else, use package manager.
4. **Verify Installation:**

   * Open Terminal (macOS/Linux) or Command Prompt (Windows).
   * Type:

     ```bash
     python --version
     ```

     or

     ```bash
     python3 --version
     ```

---

### C. Step 2: Install IDEs

#### 1. PyCharm (Community Edition - Free)

* **Download:** [jetbrains.com/pycharm/download](https://www.jetbrains.com/pycharm/download/)
* **Install:**

  1. Choose Community Edition (free).
  2. Run installer (Windows/macOS/Linux).
  3. Launch PyCharm.
  4. On first launch, select “New Project,” set interpreter to the Python installed earlier.
* **Screenshot suggestion:** Show the PyCharm welcome screen.

#### 2. Visual Studio Code (VS Code)

* **Download:** [code.visualstudio.com](https://code.visualstudio.com/)
* **Install:**

  1. Run the installer.
  2. Launch VS Code.
  3. Go to Extensions (left bar), search for “Python,” and install the official Python extension (by Microsoft).
  4. Restart VS Code if prompted.
* **Set Interpreter:** Press `Ctrl+Shift+P`, type “Python: Select Interpreter,” and choose your Python 3.x install.
* **Screenshot suggestion:** Show VS Code with Python extension installed.

#### 3. Thonny (Beginner-friendly)

* **Download:** [thonny.org](https://thonny.org/)
* **Install:**

  1. Download the installer for your OS.
  2. Run the installer and follow prompts.
  3. Thonny usually comes with Python bundled; no need for extra setup.
  4. Open Thonny and you’re ready to code!
* **Screenshot suggestion:** Show Thonny’s simple interface.

---

### D. Step 3: Install Jupyter Notebooks

**Option 1: Via Anaconda (Easiest for beginners/data science)**

* **Download Anaconda:** [anaconda.com/products/distribution](https://www.anaconda.com/products/distribution)
* **Install Anaconda.** (Follows OS-specific prompts.)
* **Launch “Anaconda Navigator”** and click “Launch” under Jupyter Notebook.

**Option 2: Using pip (for those comfortable with command line)**

* Open Terminal/Command Prompt.
* Run:

  ```bash
  pip install notebook
  ```
* Then start Jupyter:

  ```bash
  jupyter notebook
  ```
* Browser will open at `localhost:8888` showing the Jupyter dashboard.

**Screenshot suggestion:** Show the Jupyter Notebook dashboard in the browser.

---

### E. Optional: Online Interpreters

* [repl.it/languages/python3](https://repl.it/languages/python3)
* [Google Colab](https://colab.research.google.com/)
* Use these if unable to install software locally.

---

### F. Demo Activity: “Hello, World!” in Each Environment

#### **Instructions for Students:**

* Open your chosen environment.
* Type and run the following program:

```python
print("Hello, World!")
```

#### **How to Run:**

* **PyCharm:**

  * Create New Project > New Python File > Type code > Right-click > Run.
* **VS Code:**

  * Open folder > New File (`hello.py`) > Type code > Right-click > “Run Python File in Terminal.”
* **Thonny:**

  * Type code in editor > Click the green “Run” button.
* **Jupyter Notebook:**

  * Click “New Notebook” > Type code in a cell > Press Shift+Enter.

**Expected Output:**

```
Hello, World!
```

---

### G. Quick Troubleshooting

* If Python not recognized: Close and reopen terminal or restart your computer.
* Make sure the interpreter is set to Python 3.x in your IDE.
* Use print statements to check your environment.

---


