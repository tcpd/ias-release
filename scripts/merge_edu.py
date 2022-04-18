import pandas as pd
from datetime import datetime

def convert(date_str):
	date_str=str(date_str)
	if date_str=="nan":
		return "N.A."
	date_obj=datetime.strptime(date_str,"%d/%m/%Y")
	date_fin=date_obj.strftime("%Y-%m-%d")
	return date_fin

df_new=pd.read_csv("ias-education_supremo.csv")
df_old=pd.read_csv("ias-education_old.csv")
ids=df_new["ID"].to_list()

#date_cols=["Date_of_Birth","Date_of_Joining","Last_End_Date","Last_Start_Date"]

#for x in date_cols:
#	df_new[x]=df_new[x].apply(convert)

ids_exclude=["KN031700","11200","GJ818004","GJ818004","GJ118F01","GJ118F01","JK08901","JK08901","KN815001","KN815001","NL917001","NL917001","TN040101","TN108U02","TN813303","TN114U06","TN114U06","TG040000","TG040000","TG112B01","TG112B01","TR021600","UP059400","UP059400","UP069901","UP069901","UP069900","UP069900","UP071600","UP071600","UP071900","UP071900","UP073000","UP073000","UP108V04","UP108V04","UP814329","UD067000","UD067000","UD067600","UD067600","UD068600","UD068600","WB040400","WB040400","WB108X01","WB108X01","WB112X01","WB112X01","WB116X02","WB116X02","WB116X02","1080","1090","1100","1100","1110","1110","1120","1130","1130","1140","1150","1160","1170","1180","10800","10900","11000","11100","11200","11300","11400","11500","11600","11700","11800","108000","109000","110000","111000","112000","113000","113000","114000","115000","116000","117000","118000","1080000","1090000","1100000","1110000","1120000","1130000","1140000","1150000","1160000","1170000","1180000","10800000","11000000","11100000","11200000","11300000","11400000","11600000","11700000","11800000","110000000","110000000","111000000","112000000","113000000","1060000000","1110000000","1110000000","1120000000","1130000000"]
ids.extend(ids_exclude)


df_notthere=df_old[~df_old["ID"].isin(ids)]#old dataset rows that are not part of the new scrape

df_final=df_new.append(df_notthere)
df_final=df_final[["ID","Name","Cadre","Reference_Value","Qualification","Subject","Category_of_Subject","Division","Source"]]
df_final.to_csv("ias-education.csv",index=False)
