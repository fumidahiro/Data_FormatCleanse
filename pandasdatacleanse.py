# Find the row that is all null
df[df.isna().all(axis=1)]

# Find the row that has at least one null
df[df.isna().any(axis=1)]
