from urllib.parse import urljoin

import uvicorn
import httpx
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

import db as db
import schemas as schemas
import models
from settings import BADLISTED_WORDS_URL, SPACY_NOUNPHRASES_URL


app = FastAPI()
client = httpx.AsyncClient()


service_url_builder = {
    'badlisted-words': lambda endpoint: urljoin(BADLISTED_WORDS_URL, endpoint),
    'spacy-nounphrases': lambda endpoint: urljoin(SPACY_NOUNPHRASES_URL, endpoint)
}


@app.on_event('startup')
async def startup_event():
    await db.init()


@app.post('/process')
async def process_data(process: schemas.ProcessCreate, db: Session = Depends(db.get_session)):
    db_process = models.Process(service=process.service, endpoint=process.endpoint, input=process.payload.dict())
    res = await client.post(service_url_builder[process.service](process.endpoint), json=process.payload.dict())
    db_process.output = res.json()

    db.add(db_process)
    await db.commit()

    return db_process.output


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
