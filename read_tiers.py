from bs4 import BeautifulSoup as bs
from os import listdir
from os.path import isfile, join
import re
import json

scrapeDir = "scraped_html/"

def createMasterDict(dir=scrapeDir):
    ### input: scrape directory
    ### returns {file_location: soup_object}
    masterDict = {}
    cardClassesList = [f for f in listdir(dir) if isfile(join(dir, f))]
    #print(cardClassesList)
    for f in cardClassesList:
        with open(dir + f, "r") as file:
            classHtml = file.read()
            soup = bs(classHtml, 'html.parser')
            # print(type(soup))
            masterDict[f] = soup
    # print(masterDict)
    return masterDict


# def getSkills(className, tiers, dict=createMasterDict()):
def getSkills(className, masterDict=createMasterDict()):

    # def getClassTiers(className, masterDict=createMasterDict()):
    def getClassTiers():
        # input: class you want to get the tier list of, masterDict that has the html to scrape
        # returns a dictionary of skills with their designated tiers (i.e., from S to F)
        classCardSoup = masterDict[className + ".html"]
        allTiers = classCardSoup.find_all('h2')
        tierListText = [t.text[3] for t in allTiers]
        return tierListText

    # print(getClassTiers("beast")) # sample lang 'yung beast, pweds aqua, dawn, bug, bird, etc.

    skillsDict = {}
    for tier in getClassTiers():
        # print(tier)
        # skillsDict[tier] = []
        #skillsDict[tier] = {}
        next = masterDict[className + ".html"].find(text=re.compile(tier + " - Tier")).parent.findNextSibling()
        #print(next.name)
        try:
            while next.name != "h2":
                # skillsDict[tier].append(next.div.div.h3.text[6:-5])
                nextSkill = next.div.div.h3.text[6:-5]
                # skillsDict[tier][nextSkill] = []
                skillsDict[nextSkill] = {'tier': tier}
                next = next.findNextSibling()
        except AttributeError as e:
            exit
    
    # print(skillsDict)
    return skillsDict

# print(getSkills("all"))

def getSkillStats(className="all"):
    # input: string of skill stats you want to populate, i.e., "all"
    # output: populated skill stats dictionary using getSkills

    initialDict = getSkills(className)
    newDict = {}

    with open(scrapeDir + "/" + className + ".html", "r") as file:
        classHtml = file.read()
    skillSoup = bs(classHtml, 'html.parser')

    ## the parenthesis in Scale Dart (Aqua) is ruining the text search
    # print(skillSoup.find(text=re.compile("Scale Dart \(Aqua\)")).parent)#.findNextSibling().text

    # for key in statsDict:
    for key in initialDict:

        keyChange = False

        if "(" in key:
            keyChange = True
            originalKey = key # save the original key without the forced paren
            key = re.sub(r'([()])', r'\\\1', key) # force paren on key search because soup.find can't match parentheses
        
        statsDirty = skillSoup.find('h3', text=re.compile(key)).parent.text
        #print(statsDirty)
        statsClean = [item.lstrip() for item in statsDirty.splitlines() if item.strip() != '']
        partNameSplit = statsClean[-1].split(":")
        statsClean.extend(partNameSplit)
        # print (statsClean)
        del statsClean[-3] # delete the old entry where the split came from

        if keyChange:
            key = originalKey # revert to original key

        newDict[key] = {
            'tier': initialDict[key]['tier'],
            'nrg': int(statsClean[1]),
            'atk': int(statsClean[2]),
            'def': int(statsClean[3]),
            'class': statsClean[4],
            'description' : statsClean[5],
            'body part' : statsClean[6],
            'part name' : statsClean[7]
            }

        # print(key + str(newDict[key]))

    return newDict

# print(getSkillStats("bird"))

def jsonExport(className="all", outputDir="out"):
    with open(outputDir + "/" + className + '.json', 'w') as fp:
        json.dump(getSkillStats(className), fp)
    return
# jsonExport("bird")

def jsonExportAll(inputDir="scraped_html/", outputDir="out"):
    classNames = [f[:-5] for f in listdir(inputDir) if isfile(join(inputDir, f))]
    #jsonExport(c) for c in classNamess
    for c in classNames:
        print("json-ing " + c + "...")
        jsonExport(c)
    return
jsonExportAll()

def testFunc():
    with open("scraped_html/bird.html", "r") as file:
        soup = bs(file.read(), 'html.parser')

    statsDirty = soup.find('h3', text=re.compile("Swallow")).parent.text#.findNextSibling()#.text
    statsClean = [item.lstrip() for item in statsDirty.splitlines() if item.strip() != '']
    partSplit = statsClean[-1].split(':')
    statsClean.extend(partSplit)
    del statsClean[-3]
    print(statsClean)
    return
# testFunc()