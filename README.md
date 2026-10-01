# 김해시 휘발유 가격 트렌드 분석

전국 평균이 아닌 특정 지역(경남 김해시) 단위의 일별 휘발유 가격 데이터를 분석하여,
평상시 가격 등락 패턴과 2026년 초 국제 정세 이벤트에 따른 급등 구간을 함께 살펴본 프로젝트입니다.

자세한 분석 질문, 시각화, 인사이트는 [REPORT.md](./REPORT.md)를 참고하세요.

## 데이터 출처

- 한국석유공사 오피넷(Opinet) "유가내려받기" 서비스
- 기간: 2023-01-01 ~ 2026-09-29 (일별, 1,368일)
- 수집 방법: https://www.opinet.co.kr 에서 지역(경남 김해시)/유종(휘발유)/기간을 지정하여 CSV 직접 다운로드

## 폴더 구조

    oil-price-assistant/
    ├── data/
    │   ├── gimhae_2023.csv ~ gimhae_2026.csv   # 원본 다운로드 파일
    │   ├── gimhae_gasoline_daily.csv           # 1차 정제 (날짜별 평균)
    │   └── gimhae_gasoline_final.csv           # 최종 데이터 (date, value, memo)
    ├── notebook/
    │   ├── analysis.ipynb                      # 분석 코드
    │   ├── 01_price_trend.png
    │   ├── 02_moving_average.png
    │   ├── 03_monthly_avg.png
    │   └── 04_price_with_events.png
    ├── REPORT.md
    ├── README.md
    └── requirements.txt

## 실행 방법

```bash
# 1. 가상환경 생성 및 활성화 (Windows)
python -m venv venv
venv\Scripts\Activate.ps1

# 2. 패키지 설치
pip install -r requirements.txt

# 3. Jupyter Notebook 실행
jupyter notebook
```

`notebook/analysis.ipynb`를 열어 위에서부터 순서대로 셀을 실행하면 전체 분석 과정을 재현할 수 있습니다.

## 사용 기술

- Python 3.13
- pandas, matplotlib
- Jupyter Notebook