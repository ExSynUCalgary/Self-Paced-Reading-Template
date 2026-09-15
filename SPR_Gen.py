#Version 1.0
#This script will create single word chunk self paced reading segments.
#The output file returns the input file with extra columns for the SPR
#regions added at the rightmost edge. Adjust the input file name and
#sentence column name as needed. The output file can be fed directly
#into the PsychoPy experiment availablie on the XsynUCalgary GitHub.

#This script will handle sentences of different lengths within the
#same input file. The region variable in PsychoPy will deal with
#it on the experiment builder side.

import pandas as pd

df = pd.read_csv('SPR_Input.csv') #Input file name. csv only.
out_df = pd.DataFrame()
regions_list = []

for index, row in df.iterrows():
    outlist = row.tolist()
    sentence = row['Sentence'] #Target column name
    split_s = sentence.split()
    Region_Num = len(split_s)
    region_counter = -1 #starting at this value to make r0 all asterisks.
    outlist.extend([str(Region_Num + 1)])
    #Adding 1 here allows PsychoPy to include r0 without impacting the
    #subsequent while loop.
    while region_counter < Region_Num:
        string = []
        flag = 0
        #This flag prevents sentences with duplicate words from printing
        #that word twice rather than printing the second copy as asterisk(s)
        for i in split_s:
            if i == split_s[region_counter] and region_counter >= 0 and flag == 0:
                a = i
                split_s[region_counter] = '*' * len(i)
                #Duplicate word protection
                #Once the word has been printed in the SPR strings, this
                #ensures it can never be printed again by turning it
                #into asterisks.
                flag = 1
            else:
                a = '*' * len(i)
            string.append(a)
        region_counter += 1
        add_cell = ' '.join(string)
        outlist += [add_cell]
        new_row_df = pd.DataFrame([outlist])
    out_df = pd.concat([out_df, new_row_df], ignore_index=True)

headers = df.columns.tolist() + ["Region_Num"]
regions_max = out_df.columns.stop - len(headers)
for i in range(0,regions_max):
    regions_list += [("r" + str(i))]
headers += regions_list
out_df.columns=headers
#This rewrites column headers to include region numbers beginning at
#r0 (all asterisks) to r(n) where n is the maximum number of regions
out_df.to_csv('Stimuli.csv', index=False)
        
    

        
