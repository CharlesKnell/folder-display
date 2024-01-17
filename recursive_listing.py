# tag=charlesknell

import os


def list_files(path, acount, aprogress_bar):
    # Initialize an empty list to store file paths
    file_list = []

    # Traverse through the directory tree
    for root, dirs, files in os.walk(path):
        # Loop through all the files in the current directory
        for file in files:
            # Create the absolute path of the file
            abs_path = os.path.join(root, file)

            # Check whether the path is a file or directory
            if os.path.isfile(abs_path):
                # If the path is a file, append it to the list
                acount += 0.05
                file_list.append(abs_path)
                aprogress_bar['value'] = acount
                aprogress_bar.update()

    # Return the final list of file paths
    return file_list



#list1 = list_files('C:\\Users\\charl\\OneDrive\\Desktop\\PW')
#count = 0
#for file in list1:
#    count += 1
#    print(file, count)
