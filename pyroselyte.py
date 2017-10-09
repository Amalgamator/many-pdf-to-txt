"""
A rudimentary pdf-to-txt script for multiple files in several directories (does not keep dir structure).
"""
import os
import sys
import re
import PyPDF2

rootdir ='/home/red-ibis/Documents/scifi_fantasy_collection'

def cleanup(str_to_clean):
	# rudimentary cleanup, examples 
	# adapted from answer in https://stackoverflow.com/questions/6116978/python-replace-multiple-strings

	# define desired replacements here
	rep = { "™":" ", 
			"Š":"—",
			"€":" "
		  } 

	# the replacement in one pass over the string!
	rep = dict((re.escape(k), v) for k, v in rep.items())
	pattern = re.compile("|".join(rep.keys()))
	cleaned_str = pattern.sub(lambda m: rep[re.escape(m.group(0))], str_to_clean)
	return cleaned_str

i = 0
fileRead_errs = 0
extractwrite_errs = 0

for subdir, dirs, files in os.walk(rootdir):
	for file in files:
		i += 1
		filedir = subdir + "/" + file
		
		print(i,filedir)

		if i >= 9325: # alter this conditional to define start, end or scope (like starting from previous error)
			pdfFileObj = open(filedir,'rb')     #'rb' for read binary mode
			
			try:
				pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
			except:
				error_log = open("---ERRORS.TXT", 'w')
				error_log.write(str(filedir) + '\n' + str(sys.exc_info()) + '\n')
				fileRead_errs += 1
				error_log.close()

			text_file = open(file.strip(".pdf") + '.txt', "w")
			
			try:
				for page in pdfReader.pages:
					text = str(page.extractText())
					text = cleanup(text)
					text_file.write(text)
			except:
				error_log = open("---ERRORS.TXT", 'w')
				error_log.write(str(filedir) + '\n' + str(sys.exc_info()) + '\n')
				extractwrite_errs += 1
				error_log.close()

			text_file.close()
			pdfFileObj.close()

print("Number of readErrors: " + str(fileRead_errs))
print("Number of extract & writeErrors: " + str(extractwrite_errs))
print("See '---ERRORS.TXT' for more information...")

input("Press [ENTER] to FINISH.")
