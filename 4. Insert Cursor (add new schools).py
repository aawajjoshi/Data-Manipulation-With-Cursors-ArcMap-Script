#Importing package and modules 
import arcpy, os, sys

#Setting envrionment
arcpy.env.overwriteOutput = True

#Path to the MOHigherEd shapefile
inputFC = r"c:\Geo\geo465\Aawaj_Joshi\lab09\lab09\data\MOHigherEd.shp"

#Creating a list of necesary fields
fieldList = ["Facility", "Type", "Shape@XY"]

#New list of features that corresponds with fieldList
newEd = [('Pseudo University', 'Unknown', (400000, 4400000)), ('Pseudo College', 'Unknown', (400000, 4300000))]

#Creating insert cursor for feature class
with arcpy.da.InsertCursor(inputFC, fieldList) as inCursor:
    #Iterating through each row
    for newUniversity in newEd:
        
        #Inserting new row
        inCursor.insertRow(newUniversity)
        #Printing the new universities that got added
        print("Add New University: {0}".format(newUniversity[0]))

