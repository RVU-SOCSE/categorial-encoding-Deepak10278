from sklearn.preprocessing import OneHotEncoder

ohe = OneHotEncoder(sparse_output=False)

encoded = ohe.fit_transform(df)

df_ohe = pd.DataFrame(encoded, columns=ohe.get_feature_names_out())

print("\nOne-Hot Encoded Dataset:\n", df_ohe)
