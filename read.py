import csv

def read_data():
    rcvr_email = []
    org_name = []

    with open('data.csv', mode = 'r') as file:
        csvData = csv.reader(file)
        for line in csvData:
            rcvr_email.append(line[1])
            org_name.append(line[0])
    
    return rcvr_email, org_name
