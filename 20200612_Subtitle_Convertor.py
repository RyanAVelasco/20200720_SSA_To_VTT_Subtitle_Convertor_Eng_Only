import re

with open("Y:\.youtube-dl-folder\Anime\Sword Art Online (Dub)\S02E20 - Sleeping Knights.enUS.ass", "r") as files:
    # print(files)
    file = str(files)
    file = file.split("\\\\")
    file = file[2].split("mode")
    file = file[0]
    print(str(file))
    if ".ass" in file:
        file = file.replace(".ass", "")
        print(file)

    if file.endswith("' "):
        file = file.replace("' ", "")
        print(file)

    f = open("D:/" + file + ".vtt", "a")
    f.write("WEBVTT\n")
    f.close()
    print(file)
    for lines in files:
        xyz = ""
        charz = ""

        if lines.startswith("["):
            x = lines[:]
            lines = lines.replace(x, "")
        if lines.startswith("Title:"):
            x = lines[:]
            lines = lines.replace(x, "")
        if lines.startswith("Original Script"):
            x = lines[:]
            lines = lines.replace(x, "")
        if lines.startswith("Original Translation:"):
            x = lines[:]
            lines = lines.replace(x, "")
        if lines.startswith("Original Editing:"):
            x = lines[:]
            lines = lines.replace(x, "")
        if lines.startswith("Original Editing:"):
            x = lines[:]
            lines = lines.replace(x, "")
        if lines.startswith("Original Timing: "):
            x = lines[:]
            lines = lines.replace(x, "")
        if lines.startswith("Synch Point:"):
            x = lines[:]
            lines = lines.replace(x, "")
        if lines.startswith("Script Updated By:"):
            x = lines[:]
            lines = lines.replace(x, "")
        if lines.startswith("Update Details: "):
            x = lines[:]
            lines = lines.replace(x, "")
        if lines.startswith("ScriptType:"):
            x = lines[:]
            lines = lines.replace(x, "")
        if lines.startswith("Collisions:"):
            x = lines[:]
            lines = lines.replace(x, "")
        if lines.startswith("PlayRes"):
            x = lines[:]
            lines = lines.replace(x, "")
        if lines.startswith("Timer:"):
            x = lines[:]
            lines = lines.replace(x, "")
        if lines.startswith("WrapStyle:"):
            x = lines[:]
            lines = lines.replace(x, "")
        if lines.startswith("Format:"):
            x = lines[:]
            lines = lines.replace(x, "")
        if lines.startswith("Style:"):
            x = lines[:]
            lines = lines.replace(x, "")
        if lines.startswith("Format:"):
            x = lines[:]
            lines = lines.replace(x, "")

        if "\\" in lines:
            lines.replace("\\", "")

        if "{" in lines:
            charx = lines.split("{")
            chary = charx[1].split("}")
            charz = chary[0]

        if charz in lines:
            lines = lines.replace(charz, "")
            lines = lines.replace("{", "")
            lines = lines.replace("}", "")

        if ",," in lines:
            lines = re.sub(",,", "___", lines)
        if ")}" in lines:
            lines = re.sub("}", "___", lines)
        if "Dialogue" in lines:
            lines = lines.replace("Dialogue: 0,", "")

        lines = lines.replace(",", " --> ", 1)
        lines = lines.replace(",", "\n", 1)

        lines = lines.replace("â€", "-")
        lines = lines.replace("\\N", "\n")

        #  Deletes triple underscores

        x = lines.rfind("___", 0, -1)
        x += 3
        y = x / 2

        z = lines[int(y - 2):x]
        lines = lines.replace(z, "\n")

        if "sign_" in lines:

            if "0:" in lines:
                lines = lines.replace("0:", "00:")

            if ":000:" in lines:
                lines = lines.replace(":000:", ":00:")
            spot = lines.split("\n")
            spot.remove(spot[1])
            for spots in spot:
                print(spots)

            lines = lines.replace(lines[0:], spots)


        if "0:" in lines:
            lines = lines.replace("0:", "00:")

        if ":000:" in lines:
            lines = lines.replace(":000:", ":00:")

        if ":100:" in lines:
            lines = lines.replace(":100:", ":10:")

        if "fl\n" in lines:
            lines = lines.replace("fl\n", "")

        if "flashb\n" in lines:
            lines = lines.replace("flashb\n", "")

        lines = lines.lstrip()


        f = open("D:/" + file + ".vtt", "a")
        f.write(lines)
        f.write("\n")

        print(lines)