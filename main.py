from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class TerminAnfrage(BaseModel):
    datum: str
    uhrzeit: str


@app.post("/termin/pruefen")
def termin_pruefen(anfrage: TerminAnfrage):

    belegte_termine = [
        {
            "datum": "2026-09-10",
            "uhrzeit": "14:00"
        },
        {
            "datum": "2026-09-10",
            "uhrzeit": "16:00"
        }
    ]

    for termin in belegte_termine:
        if (
            termin["datum"] == anfrage.datum
            and termin["uhrzeit"] == anfrage.uhrzeit
        ):
            return {
                "verfuegbar": False,
                "nachricht": "Dieser Termin ist bereits vergeben."
            }

    return {
        "verfuegbar": True,
        "nachricht": "Dieser Termin ist verfügbar.",
        "datum": anfrage.datum,
        "uhrzeit": anfrage.uhrzeit
    }