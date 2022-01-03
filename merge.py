import pandas as pd
from datetime import datetime

def convert(date_str):
	date_str=str(date_str)
	if date_str=="nan":
		return "N.A."
	date_obj=datetime.strptime(date_str,"%d/%m/%Y")
	date_fin=date_obj.strftime("%Y-%m-%d")
	return date_fin

df_new=pd.read_csv("supremo.csv")
df_old=pd.read_csv("ias-profile_old.csv")
ids=df_new["ID"].to_list()

date_cols=["Date_of_Birth","Date_of_Joining","Last_End_Date","Last_Start_Date"]

for x in date_cols:
	df_new[x]=df_new[x].apply(convert)


df_notthere=df_old[~df_old["ID"].isin(ids)]

df_final=df_new.append(df_notthere)
df_final=df_final[["ID","Name","Service","Cadre","Allotment_Year","Date_of_Birth","Date_of_Joining","Source_of_Recruitment","Gender","Place_of_Domicile","Mother_Tongue","Languages_Known","Retired","Retirement_Reason","Last_Education_Qualification","Last_Education_Subject","Last_Education_Division","Last_Designation","Last_Level","Last_Office","Last_Field_of_Experience","Last_Category_of_Experience","Last_Start_Date","Last_End_Date","Source"]]
df_final.to_csv("ias-profile.csv",index=False)
