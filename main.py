from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Dict
from translate import Translator

app = FastAPI()

class Texts(BaseModel):
    country: str
    distanceUnit: str
    key: str
    name: str
    region: str
    regionId: str

class TranslationRequest(BaseModel):
    cities: List[Texts]

@app.post("/translate")
async def translate(request: TranslationRequest):
    translator = Translator(from_lang="en",to_lang="ja")
    translated_texts = [
        {
            "country": translator.translate(texts.country),
            "distance_unit": translator.translate(texts.distanceUnit),
            "key": texts.key,
            "name": translator.translate(texts.name),
            "region": translator.translate(texts.region),
            "region_id": texts.regionId
        }
        for texts in request.cities
    ]
    #return {"translated_cities": translated_cities}
    return {"translated_texts": translated_texts}

