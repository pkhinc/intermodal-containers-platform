# Intermodal Transport Data Platform

Projekt inżynierski realizujący hurtownię danych dla transportu intermodalnego w Polsce.

## 🛠️ Technologie
- **Cloud Data Warehouse:** Snowflake (warstwy RAW_DATA, DATA_WAREHOUSE, OPERATIONS, MART)
- **Database:** MongoDB (metadane, logi)
- **ETL:** Python (Pandas, PyMongo, Snowflake Connector)
- **UI:** Streamlit
- **DevOps:** Docker

## 🏗️ Architektura
- Pliki źródłowe (GUS) -> Skrypt ETL -> Snowflake / MongoDB -> Streamlit.

## 🚀 Jak uruchomić?
```bash
git clone [https://github.com/pkhinc/intermodal-containers-platform.git](https://github.com/pkhinc/intermodal-containers-platform.git)
cd intermodal-containers-platform