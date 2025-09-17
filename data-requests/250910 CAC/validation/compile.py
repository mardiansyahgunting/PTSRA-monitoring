import pandas as pd

# Memuat dataset
raw_df = pd.read_csv('cycle2_raw.csv')
validated_df = pd.read_csv('cycle2_validated.csv')

# Mendapatkan himpunan (set) dari measurement_uuid dari kedua dataframe
raw_uuids = set(raw_df['measurement_uuid'])
validated_uuids = set(validated_df['measurement_uuid'])

# Menemukan UUID yang ada di raw_uuids tapi tidak ada di validated_uuids
missing_uuids = raw_uuids - validated_uuids

# Mencetak UUID yang hilang
print("Measurement UUIDs yang ada di cycle2_raw.csv tapi tidak ada di cycle2_validated.csv:")
for uuid in missing_uuids:
    print(uuid)