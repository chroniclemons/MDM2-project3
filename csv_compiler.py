import csv 
import os
import horseraceing_data_2

#PUTS OUR DATA IN A WORKABLE STATE(CSV ---> ARRAY)
def DO_IT():
    results = []
    direc = os.path.abspath(os.getcwd()) + "/horseraceing_data_2"
    for file in os.listdir(direc):
        currfile = []
        with open(direc + "/" + file, 'r') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                currfile.append(row)
        csvfile.close()
        results.append(currfile)               
    return results