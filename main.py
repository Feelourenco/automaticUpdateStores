import os
from glob import glob
import installSubmodules
import storeNoUpdate

STORES_PATH="/var/www/clientes"

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

def notUpdate():
    storeNotUpdate = []
    listStore = storeNoUpdate.stores   
    for store in listStore:
        BlackList = storeNoUpdate.stores[store]['path']
        storeNotUpdate.append(BlackList)
    return storeNotUpdate
                  
def main():
    getPaths = getAllPaths()
    getMagentoPaths = getOnlyMagentoPaths(getPaths)
    noUpdate = notUpdate()
    
    for pathMagento in getMagentoPaths:
        if pathMagento in noUpdate:
            print(' "%s" não será atualizada! \n' %pathMagento)
        else:
            installSubmodules.executeAll(pathMagento)
            
    print("Finalizado!")
main()