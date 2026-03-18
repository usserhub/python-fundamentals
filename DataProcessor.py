#a dataprocessor that uses CSV reader and uses map() and applies transfomation
import csv as c


CsvFile = "/home/bzh/Documents/Machine Learning/ML study/ML study/python studies/Adcanced_modules_8/working with csv/newfile.csv"


class DataProcessor:
    def __init__(self,CsvFile):
        with open(CsvFile, 'r')as file:
            data = c.reader(file)
            self.data = list(data)
    def transform_names(self):
        names = [row[0] for row in self.data[1:]] # skip header with [1:] instead of next()
        return list(map(str.upper, names))
        #self.CsvFile = CsvFile
dp = DataProcessor(CsvFile)
print(dp.data,dp.transform_names())