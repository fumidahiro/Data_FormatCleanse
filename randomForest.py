"""
Use this to Find the importance of independent field

Input 
X : data of independent variable
y : data of dependent variable
"""

y = A_df ["dependent"]
X = A_df.drop("dependent", axis=1)

from sklearn.ensemble import RandomForestRegressor
regr = RandomForestRegressor(max_depth=5, random_state=1, n_estimators=100, n_jobs=-1,)
regr.fit(X, y)
res_df = pd.DataFrame(data={"FieldsName":X.columns, "Importance":regr.feature_importances_})
res_df.sort_values(by="Importance", ascending=False)
