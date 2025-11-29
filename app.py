from fastapi import FastAPI
from preprocessing import clean_text
from generation import generer_reponse

app = FastAPI()

@app.get("/")
def home():
    return {"message": "API Avis Clients OK"}

@app.post("/analyse")
def analyser_avis(texte: str):
    texte_clean = clean_text(texte)
    reponse = generer_reponse(texte_clean)
    return {
        "texte": texte_clean,
        "reponse": reponse
    }
