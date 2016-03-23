import os
import sys
import fileinput



textToSearch = "<trk>"  


textToReplace = "<trk> \n <name> IAT West Section 1 <name>"


fileToSearch = 'dummy.txt'

tempFile = open( fileToSearch, 'r+' )

for line in fileinput.input( fileToSearch ):
    if textToSearch in line :
    	
        print('Match Found')
    else:
        print('Match Not Found!!')
	tempFile.write( line.replace( textToSearch, textToReplace ) )
tempFile.close()

input( '\n\n Press Enter to exit...' )
