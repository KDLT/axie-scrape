from bs4 import BeautifulSoup as bs
from os import listdir
from os.path import isfile, join
import re
import json

scrapeDir = "scraped_html/"
#onlyfiles = [scrapeDir+f for f in listdir(scrapeDir) if isfile(join(scrapeDir, f))]
# sinisingit ni os.path.join 'yung backslash para magmukhang directory

## line 6 is a condensed version of the following, incredible!
# onlyfiles = []
# for f in listdir(scrapeDir):
#     if isfile(join(scrapeDir, f)):
#         onlyfiles.append(scrapeDir+f)

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

# createMasterDict()
# print(createMasterDict().keys())

# tierListText = [t.text[3:-2] for t in allTiers]
# getSkills(tierListText)
# allTiers = beastCards.find_all('h2')

### THIS list S-tier skills BEASTS. walking from first to second h2
### sample on beast radio
#beastCards = createMasterDict()["beast.html"] # this is a bs4 object
#print(beastCards.find(text=re.compile("D - Tier")).parent)

# s_skills=[]
# next = beastCards.h2.findNextSibling()

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
    # nextSkillStats = next.div.div.h3.div.span.text
    # skillsDict[nextSkill]["stats"] = [nextSkillStats]

    # statsDict = getSkills(className) # building on top of the skills Dictionary
    initialDict = getSkills(className)
    newDict = {}
    # print("before getSkillStats")
    # print(statsDict)

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
        statsDirty = skillSoup.find(text=re.compile(key)).parent.findNextSibling().text
        statsClean = [item.lstrip() for item in statsDirty.splitlines() if item.strip() != '']

        if keyChange:
            key = originalKey # revert to original key

        newDict[key] = {
            'tier': initialDict[key]['tier'],
            'nrg': int(statsClean[0]),
            'atk': int(statsClean[1]),
            'def': int(statsClean[2]),
            'class': statsClean[3]
            }
    
    # currentSkill = skillSoup.find('h3').text.lstrip().strip()
    # statsDirty = skillSoup.find('h3').findNextSibling().text
    # statsClean = [item.lstrip() for item in statsDirty.splitlines() if item.strip() != '']
    # statsDict[currentSkill] = {
    #     'nrg': int(statsClean[0]),
    #     'atk': int(statsClean[1]),
    #     'def': int(statsClean[2]),
    #     'class': statsClean[3]
    #     }
    # print(statsDict)
    # return statsDict

    # print(initialDict)
    # print("\n\n\n")
    # print(newDict)

    return newDict

#print(getSkillStats())

def jsonExport(className="aquatic", relativeDir="out"):
    with open(relativeDir + "/" + className + '.json', 'w') as fp:
        json.dump(getSkillStats(className), fp)
    return

# jsonExport()

def jsonExportAll(inputDir="scraped_html/", outputDir="out"):
    classNames = [f[:-5] for f in listdir(inputDir) if isfile(join(inputDir, f))]
    #jsonExport(c) for c in classNamess
    for c in classNames:
        jsonExport(c)
    return

jsonExportAll()
# [f for f in listdir(dir) if isfile(join(dir, f))]


beast = {
    'S - Tier': {'October Treat': [], 'Nut Crack': [], 'Chomp': [], 'Carrot Hammer': [], 'Sticky Goo': [], 'Nut Throw': [], 'Piercing Sound': [], 'Swift Escape': []}, 
    'A - Tier': {'Spike Throw': [], 'Single Combat': [], 'All-out Shot': [], 'Blackmail': [], 'Ivory Stab': [], 'Anesthetic Bait': [], 'Vegetal Bite': [], 'Eggbomb': [], 'Wooden Stab': [], 'Acrobatic': [], 'Branch Charge': [], 'Tail Slap': [], 'Prickly Trap': [], 'Disguise': [], 'Vine Dagger': [], 'Sinister Strike': [], 'Headshot': [], 'Critical Escape': [], 'Cleanse Scent': [], 'Allergic Reaction': [], 'Disarm': [], 'Star Shuriken': [], 'Angry Lam': []}, 
    'B - Tier': {'Revenge Arrow': [], 'Nitro Leap': [], 'Fish Hook': [], 'Refresh': [], 'Spicy Surprise': [], 'Ill-omened': [], 'Spinal Tap': [], 'Drain Bite': [], 'Hare Dagger': [], 'Ivory Chop': [], 'Third Glance': [], 'Peace Treaty': [], 'Crimson Water': [], 'Heart Break': [], 'Buzzing Wind': [], 'Cool Breeze': [], 'Shelter': [], 'Surprise Invasion': [], 'Nile Strike': [], 'Rampant Howl': [], 'Swallow': [], 'Sugar Rush': [], 'Dark Swoop': [], "Hero's Bane": [], 'Night Steal': [], 'Merry Legion': [], 'Aqua Vitality': [], 'Healing Aroma': [], 'Aqua Stock': [], 'Flanking Smack': [], 'Luna Absorb': []}, 
    'C - Tier': {'Terror Chomp': [], 'Insectivore': [], 'Aquaponics': [], 'Shipwreck': [], 'Death Mark': [], 'Slippery Shield': [], 'Bug Signal': [], 'Upstream Swim': [], 'Seed Bullet': [], 'Grub Surprise': [], 'Kotaro bite': [], 'Woodman Power': [], 'Blood Taste': [], 'Balloon Pop': [], 'Leek Leak': [], 'Mystic Rush': [], "Shroom's Grace": [], 'Dull Grip': [], 'Self Rally': [], 'Soothing Song': [], 'Juggling Balls': [], 'Bug Splat': [], 'Bamboo Clan': [], 'Gerbil Jump': [], 'Chitin Jump': [], 'Clam Slash': [], 'Early Bird': [], 'Scaly Lunge': [], 'Bug Noise': [], 'Water Sphere': []}, 
    'D - Tier': {'Sneaky Raid': [], 'Air Force One': [], 'Vegan Diet': [], 'Deep Sea Gore': [], 'Tiny Catapult': [], 'Smart Shot': [], 'Shell Jab': [], 'Black Bubble': [], 'Triple Threat': [], 'Scale Dart (Aqua)': [], 'Scale Dart': [], 'Scarab Curse': [], 'Aqua Deflect': [], 'Feather Lunge': [], 'Neuro Toxin': [], 'Sunder Armor': [], 'Risky Feather': [], 'Why So Serious': [], 'Gas Unleash': [], 'Barb Strike': [], 'Puffy Smack': [], 'Turnip Rocket': [], 'Tiny Swing': [], 'Bulkwark': [], 'Cockadoodledoo': [], 'Venom Spray': []}, 
    'E - Tier': {'Patient Hunter': [], 'Heroic Reward': [], 'Cattail Slap': [], 'Forest Spirit': [], 'Overgrow Keratin': [], 'Poo Fling': [], 'Chemical Warfare': [], 'Mite Bite': [], 'Jar Barrage': [], 'Numbing Lecretion': [], 'Grub Explode': [], 'Twin Needle': [], 'Sunder Claw': []}, 
    'F - Tier': {'Sweet Party': []}
    } 