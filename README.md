# file_organiser
An application designed to extract files from multiple branched folders into one destination folder. Developed in support of Farmsense project 


An application under the umbrella of re-arranging file/directory structuring. This app and concerned methods allow for a file structure as follows:


|----Source Folder
|  |--Folder 1
|    |--File_1.txt
|    |--File_2.txt
|    |--File_3.txt
|    |--File_4.txt
|    ...
|  |--Folder 2
|    |--File_1.txt
|    |--File_2.txt
|    |--File_3.txt
|    |--File_4.txt
|    ...
|  ...
|  |--Folder n
|    |--File_1.txt
|    |--File_2.txt
|    |--File_3.txt
|    |--File_4.txt
|    ...

to be changed to become the following stucture

|  |--Target Folder
|    |--Folder 1_file_1.txt
|    |--Folder_1_File_2.txt
|    |--Folder_1_File_3.txt
|    |--Folder_1_File_4.txt
|    |-- ...
|    |--Folder 2_file_1.txt
|    |--Folder_2_File_2.txt
|    |--Folder_2_File_3.txt
|    |--Folder_2_File_4.txt
|    ...
|    |--Folder n_file_1.txt
|    |--Folder_n_File_2.txt
|    |--Folder_n_File_3.txt
|    |--Folder_n_File_4.txt

