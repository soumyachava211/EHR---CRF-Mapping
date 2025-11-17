import pandas as pd
import json
import numpy as np
from fuzzywuzzy import fuzz

def fuzzy_match(field, candidates, threshold=80):
    best = None
    best_score = 0
    for c in candidates:
        score = fuzz.ratio(field.lower(), c.lower())
        if score > best_score:
            best = c
            best_score = score
    return best if best_score >= threshold else None

def normalize_unit(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    # Example: convert height cm → m
    if from_unit == "cm" and to_unit == "m":
        return value / 100
    return value

def apply_mapping(ehr_df, mapping):
    mapped_rows = []

    for _, row in ehr_df.iterrows():
        mapped = {}

        for ehr_field, m in mapping.items():

            # fuzzy match keywords to determine best mapping
            candidates = m.get("keywords", [])
            match = fuzzy_match(ehr_field, candidates) if candidates else None

            # value extraction
            value = row.get(ehr_field, np.nan)

            # unit normalization
            unit = m.get("unit", None)
            if unit and not pd.isna(value):
                value = normalize_unit(value, unit, unit)

            mapped[m["cdash_variable"]] = value

            # metadata
            mapped[f"{m['cdash_variable']}_attr"] = m.get("attribute", "VALUE")
            mapped[f"{m['cdash_variable']}_code"] = m.get("loinc_code", None)

        mapped_rows.append(mapped)

    return pd.DataFrame(mapped_rows)

if __name__ == "__main__":
    ehr = pd.read_csv("data/ehr_synthetic.csv")
    mapping = json.load(open("config/mapping.json"))
    crf = apply_mapping(ehr, mapping)
    crf.to_csv("data/output_crf_dataset.csv", index=False)
    print("CRF dataset generated successfully!")
