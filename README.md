# Pyroselytism
A very rudimentary script for converting a large quantity of pdf-files to txt-files, with pyPDF2 as it's only dependency.
You can add cleanup (read: replace substring) rules in a dict for ease of use. 

*Pyro (fire) + Proselytism (conversion to a religion, always make me giggle and think back to the Age of Empires days. "Wololooo!"). Since this is a mass conversion of pdf files script, it was either a monk manuscript duplication reference or this as its name.*

## How to run
Just download the script and place and run it where you want to generate the txt-files. Point to the rootdir of your pdf files. (or higher level directory, as the script will try to find all .pdf files)

## TO DO (priority low to high)
- Exception '.PDF' instead of '.pdf' as target, dunno if needed/relevant?
- Dig into pdf protocols for more info on how to do things better
- Maintain directory structure.
- Optimize for speed.
- Fix decode/encode issues.
