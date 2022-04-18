import pandas as pd
import json
from tqdm import tqdm

#print("DONT FORGET TO CHANGE THE DATASET DIRECTORY")

# change this to where the dataset is
dataset_dir = r"/home/blusoul/Documents/TCPD/Projects/ias-release"

profile_data = pd.read_csv(dataset_dir + "/ias-profile.csv")
education_data = pd.read_csv(dataset_dir + "/ias-education.csv")
experience_data = pd.read_csv(dataset_dir + "/ias-experience.csv")

main_data = {}

for id in tqdm(profile_data["ID"]):
    main_data[id] = {
        "Name": profile_data[profile_data["ID"] == id]["Name"].values[0],
        "Cadre": profile_data[profile_data["ID"] == id]["Cadre"].values[0],
        "Allotment_Year": str(profile_data[profile_data["ID"] == id]["Allotment_Year"].values[0]),
        "Date_of_Birth": profile_data[profile_data["ID"] == id]["Date_of_Birth"].values[0],
        "Date_of_Joining": profile_data[profile_data["ID"] == id]["Date_of_Joining"].values[0],
        "Source_of_Recruitment": profile_data[profile_data["ID"] == id]["Source_of_Recruitment"].values[0],
        "Gender": profile_data[profile_data["ID"] == id]["Gender"].values[0],
        "Place_of_Domicile": profile_data[profile_data["ID"] == id]["Place_of_Domicile"].values[0],
        "Mother_Tongue": profile_data[profile_data["ID"] == id]["Mother_Tongue"].values[0],
        "Languages_Known": profile_data[profile_data["ID"] == id]["Languages_Known"].values[0],
        "Retirement_Reason": profile_data[profile_data["ID"] == id]["Retirement_Reason"].values[0],
        "Source": profile_data[profile_data["ID"] == id]["Source"].values[0],
        "Gender_Source": profile_data[profile_data["ID"] == id]["Gender_Source"].values[0],
        "Education": [],
        "Experience": [],
    }

    for edu in education_data[education_data["ID"] == id]["ID"]:
        main_data[id]["Education"].append(
            {
                # Qualification	Subject	Category_of_Subject	Division
                "Qualification": education_data[education_data["ID"] == edu]["Qualification"].values[0],
                "Subject": education_data[education_data["ID"] == edu]["Subject"].values[0],
                "Category_of_Subject": education_data[education_data["ID"] == edu]["Category_of_Subject"].values[0],
                "Division": education_data[education_data["ID"] == edu]["Division"].values[0],
            }
        )
    
    for exp in experience_data[experience_data["ID"] == id]["ID"]:
        main_data[id]["Experience"].append(
            {
                # Designation	Level	Office	Organisation	Field_of_Experience	Category_of_Experience	Start_Date	End_Date
                "Designation": experience_data[experience_data["ID"] == exp]["Designation"].values[0],
                "Level": experience_data[experience_data["ID"] == exp]["Level"].values[0],
                "Office": experience_data[experience_data["ID"] == exp]["Office"].values[0],
                "Organisation": experience_data[experience_data["ID"] == exp]["Organisation"].values[0],
                "Field_of_Experience": experience_data[experience_data["ID"] == exp]["Field_of_Experience"].values[0],
                "Category_of_Experience": experience_data[experience_data["ID"] == exp]["Category_of_Experience"].values[0],
                "Start_Date": experience_data[experience_data["ID"] == exp]["Start_Date"].values[0],
                "End_Date": experience_data[experience_data["ID"] == exp]["End_Date"].values[0],
            }
        )


with open(dataset_dir + "/ias-json.json", "w") as f:
    json.dump(main_data, f, indent=4)