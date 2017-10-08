# Pyroselytism
A very rudimentary script for converting a large quantity of pdf-files to txt-files, with pyPDF2 as it's only dependency.
You can add cleanup rules in a dict for ease of use. 

*When thinking about conversion, I tend to be nostalgic and think back to the Age of Empires days. Wololooo! Since this script converts pdf files in large quantities with ease, it was either a monk manuscript duplication reference or this as its name.*

## How to run
Just download the script and place and run it where you want to generate the txt-files. Point to the rootdir of your pdf files. (or higher level directory, as the script will try to find all .pdf files)

## TO DO (priority low to high)
- Exception '.PDF' instead of '.pdf' as target, dunno if needed/relevant?
- Dig into pdf protocols for more info on how to do things better
- Maintain target directory structure in output.
- Optimize for speed.
- Fix decode/encode issues.
