Clone repo and create a virtual environment
```
$ git clone https://github.com/python-engineer/chatbot-deployment.git
$ cd chatbot-deployment
$ py -m venv venv
$ myenv\Scripts\activate
```
Install dependencies
```
$ (venv) pip install Flask torch torchvision nltk
```
Install nltk package
```
$ (venv) python
>>> import nltk
>>> nltk.download('punkt')
>>> exit()
```
Modify `intents.json` with different intents and responses for your Chatbot

Run
```
$ (venv) py train.py
```
This will dump data.pth file. And then run
the following command to test it in the console.
```
$ (venv) py chat.py
```
