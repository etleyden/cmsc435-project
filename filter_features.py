import pandas as pd

path_to_aac = "labeled_features/QSOGY_PAAC_PCP.csv"
output_path = "filtered.csv"

feature_selection = [
"PCP_SS_ST",
"PCP_LR",
"PCP_SA_EX",
"PAAC1_K",
"PCP_PO",
"PAAC1_N",
"PAAC1_F",
"PCP_SA_IN",
"PAAC1_I",
"PAAC1_W",
"PCP_HL",
"PCP_PC",
"PCP_BS",
"PCP_NC",
"PCP_AC",
"PAAC1_D",
"PAAC1_lam1",
"PAAC1_E",
"PCP_HX",
"PAAC1_S",
"PCP_Z3",
"PAAC1_T",
"PCP_SS_CO",
"PCP_Z4",
"PCP_Z1",
"PAAC1_Q",
"PAAC1_C",
"PAAC1_M",
"PCP_SC",
"PAAC1_H",
"PCP_NT",
"PCP_CY",
"PAAC1_P",
"PCP_NE",
"PCP_NE_pH",
"PAAC1_G",
"PAAC1_L",
"PAAC1_R",
"PCP_SS_HE",
"PAAC1_V",
"PCP_HB",
"PCP_SM",
"PCP_TN"
]
df = pd.read_csv(path_to_aac)
new_df = pd.DataFrame()
new_df = pd.concat([new_df, df["Labels"]], axis=1)

for i in feature_selection:
    new_df = pd.concat([new_df, df[i]],axis=1)

new_df.to_csv(output_path, index=False)