from flask import Flask, request, render_template
import json
import requests
import re
import random

app = Flask(__name__)

@app.route('/')
def home():
    existingText = request.args.get("user_line", "Into the valley of death, rode the six hundred.")
    existingNoPunc = re.sub(r'[^\w\s]', '', existingText)
    words = existingNoPunc.split()
    rhymedWord = getRhyme(words[len(words)-1])
    return render_template("pagedemo.html", lastLine = existingText, rhyme = rhymedWord)

def getRhyme(inString):
    rhymes = requests.get(url = "https://api.datamuse.com/words?rel_rhy=" + inString + "&topics=" + inString).json()
    return rhymes[random.randint(0, len(rhymes)-1)]["word"]
