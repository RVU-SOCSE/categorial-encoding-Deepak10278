from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()

df_label = df.copy()

df_label['Brand'] = le.fit_transform(df_label['Brand'])
df_label['Processor'] = le.fit_transform(df_label['Processor'])
df_label['OS'] = le.fit_transform(df_label['OS'])

print("\nLabel Encoded Dataset:\n", df_label)
