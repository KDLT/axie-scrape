from bs4 import BeautifulSoup as bs
from os import listdir
from os.path import isfile, join
import re

scrapeDir = "scraped_html/"
#onlyfiles = [scrapeDir+f for f in listdir(scrapeDir) if isfile(join(scrapeDir, f))]
# sinisingit ni os.path.join 'yung backslash para magmukhang directory

## line 6 is a condensed version of the following, incredible!
# onlyfiles = []
# for f in listdir(scrapeDir):
#     if isfile(join(scrapeDir, f)):
#         onlyfiles.append(scrapeDir+f)

def createMasterDict(dir=scrapeDir):
    ### returns {file_location: soup_object}
    masterDict = {}
    cardClassesList = [dir + f for f in listdir(dir) if isfile(join(dir, f))]
    #print(cardClassesList)
    for f in cardClassesList:
        with open(f, "r") as file:
            classHtml = file.read()
            soup = bs(classHtml, 'html.parser')
            # print(type(soup))
            masterDict[f] = soup
    # print(masterDict)
    return masterDict

createMasterDict()
# print(len(masterDict))

### sample on beast radio
beastCards = createMasterDict()["scraped_html/beast_cards.html"] # this is a bs4 object

allTiers = beastCards.find_all('h2')
tierListText = [t.text[3:-2] for t in allTiers]

def getClassTiers(className, masterDict=createMasterDict()):
    classTiers = 

#print(tierListText)

#print(beastCards.find(text=re.compile("D - Tier")).parent)

### THIS list S-tier skills BEASTS. walking from first to second h2
s_skills=[]
# next = beastCards.h2.findNextSibling()

def getSkills(tiers):
    next = beastCards.find(text=re.compile(tiers[1])).parent.findNextSibling()
    try:
        while next.name != "h2":
            s_skills.append(next.div.div.h3.text[6:-5])
            next = next.findNextSibling()
    except AttributeError as e:
        exit
    print(s_skills)

getSkills(tierListText)

# beastList = [beast.get_text()[6:-5] for beast in beasth3]
# print(beastList)

# print(beastCards.h3.get_text())
# print(soup.find(id='link3')) # buong </> ang output




# soup = bs4.BeautifulSoup(page, 'lxml')

# # find all div elements that are inside a div element
# # and are proceeded by an h3 element
# selector = 'div > h3 ~ div'

# # find elements that contain the data we want
# found = soup.select(selector)

# # Extract data from the found elements
# data = [x.text.split(';')[-1].strip() for x in found]

# for x in data:
#     print(x)