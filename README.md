# Installation and Configuration

The python configuration and configuration can be found here at https://code.visualstudio.com/docs/python/tutorial-flask 

1) Use the following command to create and activate a virtual environment named .venv based on your current interpreter in the bash terminal

```bash
py -3 -m venv .venv .venv\scripts\activate
```

2) In VS Code, open the Command Palette (View > Command Palette or (Ctrl+Shift+P)). Then select the Python: Select Interpreter command:

3) The command presents a list of available interpreters that VS Code can locate automatically (your list will vary; if you don't see the desired interpreter, see Configuring Python environments). From the list, select the virtual environment in your project folder that starts with ./.venv or .\.venv an example would be 

```bash
.\.venvscriptsactivate\Scripts\python.exe
```

4) Update pip in the virtual environment by running the following command in the VS Code Terminal:

```bash
python -m pip install --upgrade pip
```

5) Install Flask in the virtual environment by running the following command in the VS Code Terminal:

```bash
python -m pip install flask
```

6) To run flask app firstly locate where the newportserver.py

7) CTRL + ' and select bash terminal. 

8) Inside the bash terminal type the following

```bash
 export FLASK_APP=newportserver.py
```
9) lastly, in the bash terminal type
```bash
python -m flask run  
```
7) Copy and paste the link to web browser [http://127.0.0.1:5000/home](http://127.0.0.1:5000/home) to get started
