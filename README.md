# Intermodal Data Platform

An engineering project implementing a data warehouse for intermodal container transport in Poland in 2019-2024.

🛠️ Technologies
Cloud Data Warehouse: Snowflake (layers: RAW_DATA, DATA_WAREHOUSE, OPERATIONS, MART)
Database: MongoDB (metadata, logs)
ETL: Python (Pandas, PyMongo, Snowflake Connector)
UI: Streamlit
DevOps: Docker

🏗️ Architecture
Source files (GUS) ➔ ETL Script ➔ Snowflake / MongoDB ➔ Streamlit.

🚀 How to Run?
```bash
git clone [https://github.com/pkhinc/intermodal-containers-platform.git](https://github.com/pkhinc/intermodal-containers-platform.git)
cd intermodal-containers-platform