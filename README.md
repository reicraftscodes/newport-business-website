# Installation and Configuration

1) Use the following command to create and activate a virtual environment named .venv based on your current interpreter in the bash terminal
- py -3 -m venv .venv .venv\scripts\activate

2) In VS Code, open the Command Palette (View > Command Palette or (Ctrl+Shift+P)). Then select the Python: Select Interpreter command:

3) The command presents a list of available interpreters that VS Code can locate automatically (your list will vary; if you don't see the desired interpreter, see Configuring Python environments). From the list, select the virtual environment in your project folder that starts with ./.venv or .\.venv
- an example would be .\.venvscriptsactivate\Scripts\python.exe

4) Update pip in the virtual environment by running the following command in the VS Code Terminal:
- python -m pip install --upgrade pip

5) Install Flask in the virtual environment by running the following command in the VS Code Terminal:
- python -m pip install flask

6) To run flask app
    - locate newportserver.py
    - CTRL + ' and select bash terminal. Inside the bash terminal type the folliwing -> export FLASK_APP=newportserver.py
    - lastly, in the bash terminal type -> python -m flask run  

