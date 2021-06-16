import os
import modules

# Check Module Ethinkers
def checkModulesStore(pathStore):

    listFile = open('%s/app/etc/config.php' %pathStore, 'r')

    modulesEnables = []
    for line in listFile:
        line = line.replace('\n', '')
        if '=>' not in line:
            continue
        
        if 'Ethinkers' and 'Eth' in line:
            line = line.replace("'", "")
            line = line.replace(",", "")
            
        moduleName = line.split('=>')[0].strip()
        isActive = line.split('=>')[1].strip()
        
        if isActive == '1':
            modulesEnables.append(moduleName)

    listFile.close()
    return modulesEnables

    #Module List
def listModules():
    list = []
    listModules = modules.modules
    for module in listModules:
        list.append(module)
    return list

#Compare Lists
def compareLists():
    compareList = []
    moduleStore = set(checkModulesStore('/var/www/curso'))
    moduleList = set(listModules())
    if moduleStore == moduleList:
        print("Não necessita instalação de nenhum submodulo")
    else:
        print("Necessita instalação")

def main():
    #print(checkModulesStore())
    compareLists()

    

main()