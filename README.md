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
Schema (docs/architecture.drawio (2).png)
<img width="745" height="264" alt="Untitled Diagram drawio" src="https://github.com/user-attachments/assets/730e3834-db10-40f9-997e-35890bdadf2f" />


🚀 How to Run?
```bash
git clone [https://github.com/pkhinc/intermodal-containers-platform.git](https://github.com/pkhinc/intermodal-containers-platform.git)
cd intermodal-containers-platform
