import os, sys, re

sys.path.append("./scripts/")
import betaCode

# LOADING SETTINGS from SETTINGS.YML
def loadSettings(ymlFile):
    with open(ymlFile, "r", encoding="utf8") as f1:
        data = f1.read().split("\n")
        dic = {}

        for d in data:
            d = d.split(":")
            dic[d[0].strip()] = d[1].strip()

    return(dic)

settings = loadSettings("settings.yml")

# AH>CE conversion
def AHCE(ah):
    ce = int(ah)-(int(ah)/33)+622
    return(int(ce))

def processAHdates(text):
    # convert AH periods to CE only
    for d in re.finditer(r"@\d+-\d+TOCE", text):
        print(d.group())
        ah = d.group()[1:-4].split("-")
        ce1 = AHCE(ah[0])
        ce2 = AHCE(ah[1])
        ahcePeriod = "%s–%s CE" % (ce1, ce2)
        text = text.replace(d.group(), ahcePeriod)
        
    # convert AH periods into AH/CE format
    for d in re.finditer(r"@\d+-\d+AH", text):
        print(d.group())
        ah = d.group()[1:-2].split("-")
        ce1 = AHCE(ah[0])
        ce2 = AHCE(ah[1])
        ahcePeriod = "%s–%s AH / %s–%s CE" % (ah[0], ah[1], ce1, ce2)
        text = text.replace(d.group(), ahcePeriod)
        
    # convert AH dates into AH/CE format
    for d in re.finditer(r"@\d+AH", text):
        print(d.group())
        ah = d.group()
        ce = AHCE(ah[1:-2])
        ahce = "%s/%s CE" % (ah[1:-2], ce)
        text = text.replace(d.group(), ahce)
    return(text)

# betaCode
def translitFile(file):
    with open(file, "r", encoding="utf8") as f:
        text = f.read()
        text = processAHdates(text)
        for i in re.finditer(r"@@.*?@@", text):
            print(i.group())
            iNew = betaCode.betacodeToTranslit(i.group())
            text = text.replace(i.group(), iNew[2:-2])

        text = processAHdates(text)
        with open(file, "w", encoding="utf8") as f:
            f.write(text)
        print("\tAH>CE & Translit Conversion: %s " % file)

def processArabicQuotes(file):
    with open(file, "r", encoding="utf8") as f:
        text = f.read()
        for i in re.finditer(r"(<!--@@.*?-->\n)(<p class=\"arabic\">.*?</p>)?", text):
            print(i.group(1)[6:-4])
            iNew = betaCode.betacodeToArabic(i.group(1)[6:-4])
            text = text.replace(i.group(), "%s<p class=\"arabic\">%s</p>" % (i.group(1), iNew))
        with open(file, "w", encoding="utf8") as f:
            f.write(text)
        print("To Arabic: %s has been processed..." % file)

# convert relevant files
def convertRelevant():
    for path, subdirs, files in os.walk("."):
       for file in files:
           if file.endswith(tuple([".md"])):
               #print(file)
               f = os.path.join(path, file)
               translitFile(f)
               #processArabicQuotes(f)

# combine master draft
def combineMasterDraft(draftFolder):
    print("=" * 80)
    print("generating master draft from frile in `%s` folder" % draftFolder)
    print("\tNB: only files that start with `0` and end with `.md` will be included!")
    
    master = []
    for path, subdirs, files in os.walk(draftFolder):
        for file in files:
            if file[0] == "0" and file.endswith(tuple([".md"])):
                #print(file)
                i = os.path.join(path, file)
                master.append(i)

    master = sorted(master)
    print("=" * 80)
    print("\t"+"\n\t".join(master))

    masterDraft = []

    for i in master:
        with open(i, "r", encoding="utf8") as ft:
            masterDraft.append(ft.read())

    # remove comments
    masterDraftFinal = []
    masterDraft = "\n\n\n".join(masterDraft).split("\n")

    # removes lines commented out in LaTeX style (the first character on the line is %)
    for m in masterDraft:
        if len(m) > 0 and m[0] == "%":
            pass
        else:
            masterDraftFinal.append(m)

    # ? add a check if `masterdraft_autogenerated.md` already exists
    #   if yes, ask if you want to overwrite it
    #      yes > generates a new file
    #      no  > stops the script
    
    with open("masterdraft_autogenerated.md", "w", encoding="utf8") as f9:
        f9.write("\n".join(masterDraftFinal))

    print("=" * 80)
    print("`masterdraft_autogenerated.md` has been produced")
    print("IMPORTANT: Do not edit this file, as it will be overwritten when you run this script again!")
    print("=" * 80)

# uload master bibliography
def loadMasterBibliography(bibliography):
    newBIBdic  = {}
    with open(bibliography, "r", encoding="utf8") as f1:
        bib = re.split("\n@", f1.read())
        for rec in bib[1:]:
            key = rec.split("\n")[0].split("{")[1].replace(",", "")
            newBIBdic[key] = "@"+rec
        
    return(newBIBdic)

# update project bibliography
def updateBibliographies(draftFile):
    bibDIC = loadMasterBibliography(settings['bib_master'])
    projectFile = "%s.md" % draftFile

    with open(projectFile, "r", encoding="utf8") as f1:
        f1 = f1.read()
        
        bibList = []
        # collect all records from bibDIC using these keys
        # ---must be done *after* transliteration is done
        refList = sorted(list(set(re.findall("@\w+", f1))))
        for k in refList:
            #print(k[1:])
            if k[1:] in bibDIC:
                bibList.append(bibDIC[k[1:]])
                #print(bibDIC[k[1:]])
            elif k[1:] == "fig":
                pass
            else:
                print("\t%s\t: not in master bibliography" % k[1:])
    # save biblio.bib
    bibList = list(set(bibList))
    with open(settings['bib_project'], "w", encoding="utf8") as f9:
        f9.write("\n\n".join(sorted(bibList)))

# MAIN FUNCTION

def main():
    print(settings)
    
    convertRelevant()
    combineMasterDraft(settings['draft_folder'])
    updateBibliographies(settings['draft'])

    # Running Pandoc
    print("=" * 80)
    print("Running Pandoc... a PDF file will be generated shortly, inshallah")
    print("=" * 80)

    font = settings['fonts']
    bib  = settings['bib_project']
    csl  = settings['bib_format']
    file = settings['draft']

    line1 = "pandoc --filter pandoc-fignos --filter pandoc-citeproc --bibliography=%s --csl=%s -N -V header-includes:%s --latex-engine=xelatex %s.md -o %s.pdf" % (bib, csl, font, file, file)
    line2 = "open %s.pdf" % file

    # you might need to replace `pandoc` with full path (in the next line)
    print(line1)
    os.system(line1)

    print(line2)
    os.system(line2)
        
main()
