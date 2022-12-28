#Author: Joshua Stapleton
#Convert DiCOM stacks into .nii.gz files
#Note: Dicom stacks must be in the first subdirectory of the folder for this to work


import dicom2nifti
import os
import shutil
import glob
import logging


#Set working directory as folder that contains subdirectories with dicom stacks
#wrkdir = 'Z:/CT_Scans/UPLIFT_SPINE_SCANS_140kv/'
wrkdir = 'Z:/CT_Scans/UPLIFT_SPINE_SCANS_140kv_test/'

#Set outdir as the folder where the .gz files should be placed, this doesn't put the .gz files into separate folders, they all just go into the same folder
#outdir = '//medctr/dfs/bme_cib$/UPLIFT/CT_Segmentations/Spine/Anduin/gz_output/'
outdir = 'Z:/CT_Scans/UPLIFT_SPINE_SCANS_140kv_test/'

#Change Directory to working directory, this script does not need to be saved in the working directory for it to run
os.chdir(wrkdir)


#Iterate through all folders in working directory and try to run the dicom2nifti command
for folder in os.listdir(wrkdir):
    try:
        #Change working directory to subdirectory in original directory
        original_dicom_directory = wrkdir + folder 

        #Create name of output file with appropriate file extension
        output_file = outdir + folder + '.nii.gz'

        #Prints as it runs to keep track of which have been run
        print(output_file)

        dicom2nifti.dicom_series_to_nifti(original_dicom_directory, output_file, reorient_nifti=True)


    except Exception as e:
        #Outputs fail error with folder name to keep track of which are failed. Common error is an "inconsistent 
        # slice thickness error". These will not run in the single version of this script, and I assume this is 
        #an error within the function itself. Those that fail can be run through 3DSlicer to convert to .nii.gz
        print(folder + " fail")

        f = open("Error_log.txt","a")
        f.write("Failed " + folder + "\n" + str(e) + "\n" + "\n")
        f.close()
        #print(Exception)
        #logging.error('Failed ' + str(e))

#log files in try catch in python
#PS: Your computer does not need to be awake for this scrip to finish, I left this overnight to run all of my conversions