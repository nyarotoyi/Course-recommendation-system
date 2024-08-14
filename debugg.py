import os

file_path = r"C:\Users\Zeetracker\Desktop\BBIT 4.2\Systems Project Implementation HBT 2403\Education-Recommendation-System-Student-Subject-and-Studies-Recommendation-system-machine-learning\Models\scaler.pkl"

# Check if the file exists
if os.path.isfile(file_path):
    print("File exists")
else:
    print("File does not exist")
