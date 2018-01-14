#Importing package and modules 
import arcpy, os, sys

#Setting envrionment
arcpy.env.overwriteOutput = True

#Path to the MOHigherEdCopy shapefile
inputFC = r"c:\Geo\geo465\Aawaj_Joshi\lab09\lab09\data\MOHigherEd.shp"

#Path to a new copy 
outputFC = r"c:\Geo\geo465\Aawaj_Joshi\lab09\lab09\data\MOHigherEdCopy.shp"

#Copying from inputFC to outputFC
arcpy.Copy_management(inputFC, outputFC)

#Creating a list of necesary fields
fields = ['State', 'Type']

#Creating update cursor for feature class
with arcpy.da.UpdateCursor(outputFC, fields) as upCursor:
    #Iterating through each row
    for row in upCursor:
        
        #Updating records with no value in State field to have value "MO"
        if (row[0] == " "):
            row[0] = "MO"
            upCursor.updateRow(row)

        #Deleting facilities that are of Thelogical Type
        if (row[1] == "Theological"):
            upCursor.deleteRow()
        
        #Updating the Type of Technical/Professional" to just "Professional"
        if "Professional" in row[1]:
            row[1] = "Professional"
            upCursor.updateRow(row)