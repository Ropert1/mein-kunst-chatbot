from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Korrekte CORS-Konfiguration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/chat")
async def chat(request: Request):
    daten = await request.json()
    frage = daten.get("prompt", "").lower()

    if "kaufen" in frage:
        antwort = "Der Preis für Kunstwerke beträgt 1000 € pro Quadratmeter."
    elif "leihen" in frage or "mieten" in frage:
        antwort = "Die Leihgebühr beträgt 15 € pro Quadratmeter."
    elif "kontakt" in frage or "künstler" in frage:
        antwort = "Sie erreichen mich direkt unter 0178 1467222."
    elif "versand" in frage:
        antwort = (
            "Der Versand kostet:\n"
            "- bis 1 m²: 20 € (Inland)\n"
            "- über 1 m²: 50 € (Inland)\n"
            "- Europa (nur EU): bis 1 m²: 35 €"
        )
    elif "termin" in frage or "probehängung" in frage:
        antwort = "Bitte nennen Sie Ihre E-Mail-Adresse. Ich melde mich innerhalb einer Woche bei Ihnen zurück."
    else:
        antwort = "Dazu habe ich momentan keine Information."

    return {"response": antwort}
