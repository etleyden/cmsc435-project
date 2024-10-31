import pandas as pd

path_to_aac = "labelled_features/AAC_PCP.csv"
output_path = "labelled_features/filtered_AAC.csv"

feature_selection = ["PCP_LR", "PCP_Z2", "PCP_SA_EX", "PCP_PC", "PCP_BS", "AAC_K", "AAC_E", "PCP_NC", "PCP_AC", "PCP_HL", "PCP_SS_HE", "PCP_Z5", "PCP_SS_CO", "AAC_G", "PCP_Z3", "AAC_V", "PCP_HB", "PCP_NP", "PCP_SA_BU", "PCP_TN", "PCP_AL", "AAC_A", "PCP_SM", "PCP_NE", "PCP_NE_pH"]
df = pd.read_csv(path_to_aac)
new_df = pd.DataFrame()
new_df = pd.concat([new_df, df["Labels"]], axis=1)

for i in feature_selection:
    new_df = pd.concat([new_df, df[i]],axis=1)

new_df.to_csv(output_path, index=False)