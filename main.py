import os
from glob import glob
import installSubmodules

STORES_PATH="/var/www/"

def getAllPaths():
    global STORES_PATH

    # Remove "/" if the STORES_PATH ends with it
    while STORES_PATH[len(STORES_PATH) - 1] == '/':
        STORES_PATH = STORES_PATH[:-1]

    return sorted(glob("%s/*/" %STORES_PATH))

def getOnlyMagentoPaths(storesPath):
	result = []

	for p in storesPath:
		if os.path.isfile("%s/bin/magento" %p):
			result.append(p)

	return result

def executeGM(allPaths):

    for store in allPaths:
        #os.system('./gm.sh')
        print('---------------------------------',store, '----------------------------------')
        print(installSubmodules.checkModulesStore(store))
        os.chdir(store)
        
def main():
    getPaths = getAllPaths()
    getMagentoPaths = getOnlyMagentoPaths(getPaths)
    executeGM(getMagentoPaths)

main()