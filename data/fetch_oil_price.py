import os
import requests
import pandas as pd
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("OPINET_API_KEY")

# 전국 평균 휘발유(가솔린) 가격 조회 예시 (엔드포인트/파라미터는 발급 후 명세서로 재확인 필요)
url = "http://www.opinet.co.kr/api/avgAllPrice.do"
params = {
    "code": API_KEY,
    "out": "json",
}

resp = requests.get(url, params=params, timeout=10)
resp.raise_for_status()
data = resp.json()

print(data)  # 먼저 원본 구조를 눈으로 확인