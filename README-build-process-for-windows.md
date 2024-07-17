# Windows Install File Build Process
## Step 1. create a windows .exe file using pyinstaller
### invoke the following in a terminal window
* pyinstaller --onefile -i Gakuseisean-Radium-My-Documents.256.ico folder_display.pyw recursive_listing.py
* In windows, rename the file, folder_display.exe, in the dist folder to reflect the new version number
## Step 2. Create an new installation file using the inno setup compiler
* Install the inno setup compiler if you have not already done so
* In the Inno-Install folder using Windows, double click the Setup.iss file and edit it to reflect the new .exe file name (with new version number) located in the dist folder. The version number appears in several places.
* Click on the compile button. 
* The new SetupFolderDisplayx.x.exe will appear in the Inno-Install folder
* For distribution, use winzip to zip the file
