import pandas as pd
import plotly.express as px
import csv
import numpy as np

def getDataSource(data_path):
    Coffee_in_ml = []
    sleep_in_hours = []
    with open(data_path) as csv_file :
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            Coffee_in_ml.append(float(row["Coffee in ml"]))
            sleep_in_hours.append(float(row["sleep in hours"]))
    return {"x" : Coffee_in_ml ,"y" : sleep_in_hours}

def findcoleraltion(datasource):
    correlation = np.corrcoef(datasource["x"],datasource["y"])
    print("Corelation between cups of coffee in mL vs. the number of hours a person can sleep: ",correlation[0,1] )

def setup():
    data_path = "cups of coffee vs hours of sleep.csv"
    datasource = getDataSource(data_path)
    findcoleraltion(datasource)


setup()