from flask import Flask, render_template, request
from google import genai

from dotenv import load_dotenv

load_dotenv("api_key.env")
import os

API_KEY = os.getenv("key")

app = Flask(__name__)

@app.route("/")
def welcoming_page():
    return render_template("index.html")

@app.route("/display", methods =["POST"])
def displaying():
    try:
        niche = request.form["niche"]

        client = genai.Client(api_key = API_KEY)

        response = client.models.generate_content(model = "gemini-2.5-flash-preview",   
                                                contents= f"Generate 10 viral video ideas for {niche}. Output format: Topic | Hook \n Topic | hook \n Topic | hook \n  Rules: \n  10 words max per line total,  Topic is the video concept, Hook is the first attention-grabbing sentence, Separate Topic and Hook with ' | '  One idea per line No numbering, no explanations"
                                                )
        
        return render_template("display.html", output = response.text)
    
    except Exception :
        return render_template("error.html")
    
