import pandas as pd

path_to_aac = "labeled_features/PAAC_PCP.csv"
output_path = "labeled_features/PAAC_PCP_filtered.csv"

deleteFeatures = True

feature_selection = [
"PCP_SS_ST",
"PAAC1_W",
"PAAC1_F",
"PCP_NT",
"PCP_Z4",
"PAAC1_S",
"PAAC1_M",
"PAAC1_N",
"PAAC1_Q",
"PAAC1_C",
"PCP_SC",
"PAAC1_L"
]
df = pd.read_csv(path_to_aac)
new_df = pd.DataFrame()

if deleteFeatures:
    new_df = df.drop(feature_selection, axis=1)
else:
    new_df = pd.concat([new_df, df[feature_selection]], axis=1)
    new_df = pd.concat([new_df, df["Labels"]], axis=1)


new_df.to_csv(output_path, index=False)