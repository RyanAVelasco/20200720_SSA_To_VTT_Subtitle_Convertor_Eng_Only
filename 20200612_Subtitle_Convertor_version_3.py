#  Programmer: Ryan Velasco || GitHub: github.com/RyanAVelasco
#  This program currently ONLY converts .en.ass files
#  There must be only folders in basedir


import os
import colored
from colored import stylize


basedir = "A:/Movies/"
for folder in os.listdir(basedir):
    x = os.listdir(basedir + folder + "/")
    vttFolder = "vtt"

    if vttFolder in x:
        continue
    else:
        os.mkdir(basedir + folder + "/vtt/")  #  creates the temp vtt folder

    for n in x:
        if "en.ass" in n:  #  en.srt is not looked at due to no "Dialogue" being inside the file
            file = n
            fhand = open(basedir + folder + "/" + n)
            try:
                for line in fhand:
                    line = line.replace("[Script Info]", "*")
                    if not line.startswith("Dialogue") and not line.startswith("*"):
                        continue
                    else:
                        line = line.replace("Dialogue: 0,", "0")
                        line = line.replace(",", "0 --> ", 1)
                        line = line.replace(",", "0,", 1)
                        fst_comma = line.find(",")
                        dbl_comma = line.find(",,")
                        delete = line[fst_comma:dbl_comma + 2]
                        if delete in line:
                            line = line.replace(delete, "\n")
                        if "\\N" in line:
                            line = line.replace("\\N", "\n")
                        if "0000,0000,0000,," in line:
                            line = line.replace("0000,0000,0000,,", "")

                        #  find angled brackets
                        while "{" in line:
                            start_brack = line.find("{")
                            end_brack = line.find("}")
                            delete = line[start_brack:end_brack + 1]
                            line = line.replace(delete, "")

                        #  correct common UTF-8 Character Encoding Problems
                        if "â€”" in line \
                                or "â€”" in line \
                                or "â€¢" in line\
                                or "â€" in line\
                                or "â€œ" in line\
                                or "â€™" in line\
                                or "â€˜" in line:
                            line = line.replace("â€“", "-")
                            line = line.replace("â€”", "-")
                            line = line.replace("â€¢", "\"")
                            line = line.replace("â€œ", "\"")
                            line = line.replace("â€™", "'")
                            line = line.replace("â€˜", "'")

                        if "\\h" in line:
                            line = line.replace("\\h", " ")

                        line = line.replace("*", "WEBVTT")
                        fileoutput = basedir + folder + "/" + "vtt/" + n[:-4] + ".vtt"

                        f = open(fileoutput, "a")
                        f.write(line)
                        f.write("\n")
                        f.close()
            except:
                print(stylize("Unknown Error", colored.fg(226)))

    #  takes all vtt subs from vtt folder and places them in the parent folder
    subsFolder = os.listdir(basedir + folder + "/" + vttFolder)
    for all in subsFolder:
        try:
            if ".vtt" in all:
                os.rename(basedir + folder + "/" + vttFolder + "/" + all, basedir + folder + "/" + all)
                print(stylize("Created File: " + all, colored.fg(117)))
        except:
            print(stylize("File exists: " + all, colored.fg(1)))


#  if any vtt subs were made in and placed in vtt folder but vtt files exist in parent
#  folder then this will delete the temp vtt folder along with any files that exists inside

for folder in os.listdir(basedir):
    x = os.listdir(basedir + folder + "/")
    for n in x:
        if n.startswith("vtt"):
            y = os.listdir(basedir + folder + "/" + n)
            for z in y:
                os.remove(basedir + folder + "/" + n + "/" + z)
        if "vtt" == n[0:3]:
            os.rmdir(basedir + folder + "/" + n)

quit()
