from openpyxl import load_workbook
from openpyxl.worksheet.datavalidation import DataValidation
import pandas as pd
import numpy as num

#from pandas import ExcelWriter
#from pandas import ExcelFile

File_Path = "Teachers.xlsx"
xl = pd.ExcelFile(File_Path)
df = xl.parse('Current Teacher')

TeachersInfo = {}

Subject = ["Scratch", "Electrical", "Python", "Math", "Art & Design"]

Days = ["Mon.", "Tues.","Wed.", "Thur.", "Fri"]

Location = ["Cupertino", "Hayward", "Los Altos", "Menlo Park", "Mountain View", "Palo Alto", "Portola Valley", "San Mateo", "Sunnyvale", "Woodside"]

#DAYS
monday = []
tuesday = []
wednesday = []
thursday = []
friday = []
#SUBject
scratchCoding = []
ArtandDesign = []
ElectricalEngineering = []
PythonCoding = []
Math = []
#Location
almond = []
loyola = []
gardnerBullis = []
cumberland = []
hillview = []
chabot = []
duveneck = []
escondido = []
LaEntrada = []
LasLomitas = []
encinal = []
laurelLower = []
laurelUpper = []
oakknoll = []
nixon = []
woodside = []
ohlone = []
roycloud= []
baywood = []


for index, row in df.iterrows():
   if pd.isnull(row['Teacher Name']) :
       pass
   else:
       #print(index, row['Teacher Name'])
       #Days
       if row['Mon.'] == 1.0:
           monday.append(row['Teacher Name'])
       if row['Tues.'] == 1.0:
           tuesday.append(row['Teacher Name'])
       if row['Wed.'] == 1.0:
           wednesday.append(row['Teacher Name'])
       if row['Thur.'] == 1.0:
           thursday.append(row['Teacher Name'])
       if row['Fri'] == 1.0:
           friday.append(row['Teacher Name'])
       if row['Scratch Coding'] == 1.0:
           scratchCoding.append(row['Teacher Name'])
       if row['Art & Design'] == 1.0:
           ArtandDesign.append(row['Teacher Name'])
       if row['Electrical Eng.'] == 1.0:
           ElectricalEngineering.append(row['Teacher Name'])
       if row['Python Coding'] == 1.0:
           PythonCoding.append(row['Teacher Name'])
       if row['Math'] == 1.0:
           Math.append(row['Teacher Name'])
       if row['Los Altos'] == 1.0:
           almond.append(row['Teacher Name'])
           loyola.append(row['Teacher Name'])
           gardnerBullis.append(row['Teacher Name'])
       if row['Sunnyvale'] == 1.0:
           cumberland.append(row['Teacher Name'])
       if row['Menlo Park'] == 1.0:
           hillview.append(row['Teacher Name'])
           LaEntrada.append(row['Teacher Name'])
           LasLomitas.append(row['Teacher Name'])
           encinal.append(row['Teacher Name'])
           laurelLower.append(row['Teacher Name'])
           laurelUpper.append(row['Teacher Name'])
           oakknoll.append(row['Teacher Name'])
       if row['Oakland'] == 1.0:
           chabot.append(row['Teacher Name'])
       if row['Palo Alto'] == 1.0:
           duveneck.append(row['Teacher Name'])
           escondido.append(row['Teacher Name'])
           nixon.append(row['Teacher Name'])
           ohlone.append(row['Teacher Name'])
       if row['Woodside'] == 1.0:
           woodside.append(row['Teacher Name'])
       if row['Redwood City'] == 1.0:
           roycloud.append(row['Teacher Name'])
       if row['San Mateo'] == 1.0:
           baywood.append(row['Teacher Name'])

       TeachersInfo['Monday']=monday
       TeachersInfo['Tuesday']=tuesday
       TeachersInfo['Wednesday']=wednesday
       TeachersInfo['Thursday']=thursday
       TeachersInfo['Friday']=friday
       TeachersInfo['Scratch']=scratchCoding
       TeachersInfo['Art & Design'] = ArtandDesign
       TeachersInfo['Electrical']=ElectricalEngineering
       TeachersInfo['Python']=PythonCoding
       TeachersInfo['Math']=Math
       TeachersInfo['Almond'] = almond
       TeachersInfo['Loyola'] = loyola
       TeachersInfo['Gardner Bullis'] = gardnerBullis
       TeachersInfo['Cumberland'] = cumberland
       TeachersInfo['Hillview'] = hillview
       TeachersInfo['La Entrada'] = LaEntrada
       TeachersInfo['Las Lomitas'] = LasLomitas
       TeachersInfo['Encinal'] = encinal
       TeachersInfo['Laurel Lower'] = laurelLower
       TeachersInfo['Laurel Upper'] = laurelUpper
       TeachersInfo['Oak Knoll'] = oakknoll
       TeachersInfo['Chabot'] = chabot
       TeachersInfo['Duveneck'] = duveneck
       TeachersInfo['Escondido'] = escondido
       TeachersInfo['Nixon'] = nixon
       TeachersInfo['Ohlone'] = ohlone
       TeachersInfo['Woodside'] = woodside
       TeachersInfo['Roy Cloud'] = roycloud
       TeachersInfo['Baywood'] = baywood

#for days,teachers in TeachersInfo.items():
   #print(days,":",teachers ,"\n")
def intersection(lst1, lst2,lst3):
     
   return [item for item in lst1 if item in lst2 if item in lst3]
             
######################################
File_Path = "MasterClass.xlsx"
xl = pd.ExcelFile(File_Path)
df = xl.parse('Winter 2020')
