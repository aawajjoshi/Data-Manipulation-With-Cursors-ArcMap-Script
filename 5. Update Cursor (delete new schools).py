#Importing package and modules 
import arcpy, os, sys

#Setting envrionment
arcpy.env.overwriteOutput = True

#Path to the MOHigherEdCopy shapefile
inputFC = r"c:\Geo\geo465\Aawaj_Joshi\lab09\lab09\data\MOHigherEd.shp"

#Creating a list of necesary fields
fieldList = ["Facility", "Type"]

#Value to be checked
oldValue = "Unknown"

condition = "\"{0}\" = \'{1}\'". format(fieldList[1], oldValue)
print(condition)

#Creating update cursor for feature class
with arcpy.da.UpdateCursor(inputFC, fieldList, condition) as upCursor:
    #Iterating through each row
    for row in upCursor:
        
        #Deleting the whole row of the feature
        upCursor.deleteRow()
        #Printing the Universities that got deleted 
        print("Delete {0}".format(row[0]))