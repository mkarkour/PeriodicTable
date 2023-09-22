import sqlite3
import fill_table
import views
from fastapi import FastAPI, Request
import uvicorn

app = FastAPI()

@app.get("/")
def root():
      return {"message": "It works !"}

@app.post("/calculation_masse_molaire")
async def calcul_masse_mol(payload: Request):
      values_dict = await payload.json()
      r = views.masse_molaire(str(values_dict["Compose"]))
      return "La masse molaire est de {a} pour le composé {b}".format(a=r,b=values_dict["Compose"])

@app.post("/calculation_mol")
async def calcul_mol(payload: Request):
      values_dict = await payload.json()
      mole = views.mole(
          str(values_dict["Compose"]),
          str(values_dict["Masse"])
          )
      return "Le nombre de mol de {a} est de {b} mol".format(a=str(values_dict["Compose"]),b = mole)

@app.post("/engima")
async def enigme(payload: Request):
      values_dict = await payload.json()
      response = views.repartisseur(eq = str(values_dict["Compose"]),
      masse = str(values_dict["Masse"]),
      mol = str(values_dict["Mole"]),
      vol = str(values_dict["Volume"])
      )
      return response

if __name__ == '__main__':
      uvicorn.run(app, host='127.0.0.1', port=8000)
      