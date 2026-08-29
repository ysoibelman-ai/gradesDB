import json
import csv
def main ():
   pass

def load_grades(file_path):
    file = open (file_path,"r")
    grades =  json.load(file)
    file.close()
    return grades

def save_grades(grades,file_path):
    file = open (file_path,"w")
    json.dump(grades, file, indent=4)
    file.close()


def add_user_to_csv(user_id, username, password, user_type, file_path="users.csv"):

    file = open(file_path, "a", newline="")
    writer = csv.writer(file)
    writer.writerow([user_id, username, password, user_type])
    file.close()
