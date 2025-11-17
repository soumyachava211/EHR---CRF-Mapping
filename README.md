# EHR---CRF-Mapping
# EHR → CRF Mapping Demo (Advanced Synthetic Project)

This project demonstrates an **advanced, NDA-safe, fully synthetic** example of mapping electronic health record (EHR) data into case report form (CRF) structures using **CDASH-like variables**, fuzzy matching, unit normalization, and configurable mapping rules.

⚠️ **IMPORTANT**  
This project is a **synthetic demonstration**.  
It contains **no code, data, mappings, structures, or logic** from my internship or employer.  
Everything here was created purely for educational purposes.

---

# 🔍 Features of This Demo

### ✔ Synthetic EHR Dataset  
Includes labs, vitals, and timestamps.

### ✔ JSON-Based Mapping Configuration  
Shows how fields map to CRF variables, attributes, and LOINC codes.

### ✔ Fuzzy Matching  
Handles messy or inconsistent field names safely.

### ✔ Unit Normalization  
Demonstrates cleaning (cm → m, etc.)

### ✔ Metadata Assignment  
Adds:
- CDASH variable  
- Attribute (VALUE / DATE / TIME)  
- LOINC code  

### ✔ Output CRF Dataset  
Generated as a cleaned, mapped CSV file.

---

# 📂 Project Structure
ehr-to-crf-mapping-demo/
│
├── data/ # synthetic EHR + output CRF dataset
├── config/ # mapping.json
├── src/ # mapping pipeline
├── notebooks/ # demo notebook
├── figures/ # optional plots
├── requirements.txt
└── README.md

---

# ▶️ How to Run
pip install -r requirements.txt
python src/mapping.py

---

# 🧠 Skills Demonstrated  
- Data standardization  
- LOINC/CDASH-style harmonization  
- Mapping automation  
- Fuzzy string matching  
- Unit normalization  
- Config-driven ETL  
- Python scripting and validation  
- Clinical data workflow simulation  

---

# 🔒 NDA Protection  
- No sponsor data  
- No real CRF/OID structures  
- No internal tools  
- No proprietary code  
- 100% synthetic  

