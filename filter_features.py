import pandas as pd

path_to_aac = "labeled_features/QSO_PAAC_PCP.csv"
output_path = "labeled_features/QSO_PAAC_PCP_filtered.csv"

deleteFeatures = False

feature_selection = [
"QSO1_SC_M",
"PCP_Z1",
"PAAC1_E",
"QSO1_G_P",
"PCP_PC",
"QSO1_SC_C",
"PCP_Z3",
"QSO1_SC_N"
]
df = pd.read_csv(path_to_aac)
new_df = pd.DataFrame()

if deleteFeatures:
    new_df = df.drop(feature_selection, axis=1)
else:
    new_df = pd.concat([new_df, df[feature_selection]], axis=1)
    new_df = pd.concat([new_df, df["Labels"]], axis=1)


new_df.to_csv(output_path, index=False)