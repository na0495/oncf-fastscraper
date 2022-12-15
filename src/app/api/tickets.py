from typing import List

from fastapi import APIRouter, HTTPException, Path

from bs4 import BeautifulSoup
import requests
import json

router = APIRouter()

url = "https://www.oncf-voyages.ma:8443/availability"


@router.get("/availability/")
async def availability(
    # from_station: str = Path(..., min_length=3, max_length=50),
    # to_station: str = Path(..., min_length=3, max_length=50),
    # date: str = Path(..., min_length=3, max_length=50),
):


    payload = json.dumps({
        "origin": "200",
        "destination": "303",
        "originDate": "2022-12-15T18:55:53+01:00",
        "intervalTime": "",
        "adulte": 1,
        "kids": 0,
        "comfort": 2,
        "reducedTariff": {
            "0": {
            "code": "",
            "priceCode": "",
            "birthday": "",
            "claimCode": ""
            }
        },
        "intervalTime-destinationDate": {
            "end": "19:00",
            "start": "12:01",
            "title": "Après-midi",
            "value": 2,
            "disabled": False
        },
        "destinationDate": None,
        "_csrf": None
        })

    headers = {
        'Authorization': 'JWT eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjY5MjIyMzM3LCJpYXQiOjE2Njg2MTc1MzcsImp0aSI6IjBmYjJmZTBmNWRlNTRmMmY5ZWNhZWIyNDcwZTI2YjVmIiwidXNlcl9pZCI6MiwiZW1haWwiOiJkZW1vQG1pbmltYWxzLmNjIn0.XTlbfHsY-A28_Q0pr7v59Gc92IibdWpKaJWTZ4yVWJ8',
        'Content-Type': 'application/json',
        'Cookie': 'BIGipServerProd-E-Vente-API-8443=!Pryu1Tor6tV2BFsWzOy3MD+QLKU3VJtv78DonLYm4wZc85IHu3EHICjWrdpXzqai3ymVUVXHt34+imA=; TS010a6da3=017044dc3f1982fd0c641de79f03fded852ab53c23033424970d15c757654887eb0d90a1d0a241633568f84cd9c4941fb631cdb4f9; TS010a6da3028=01ae62a18c4cbec2d1460c7df446359145171e798c363f34c09a743175a3766e51017531f8d878f0bbefbc68d831819a92a1f81a2c; TS010a6da3030=01ae62a18c8e2d78725141b1ec9d1f7c720d8fedd4363f34c09a743175a3766e51017531f8b2bd18662032869519bae399aba92323; f5avraaaaaaaaaaaaaaaa_session_=BGBCEHHDKDFEFLBHIFIHELJAGIFALCLLCPBFMLOEGDKDEGEJBCHKJDAIAFLNBAFMMACDINODNBMGLLHCOGKALCHCJFLAOIIHIOGEJFIPIDCNJHLFAILKMMCMBOKCOPAE'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    return response.text
