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

#Modules List
def listModules():
    lista = []
    listModules = modules.modules
    for module in listModules:
        lista.append(module)
    return lista

#Compare Lists
def compareLists(pathStore):
    compareList = []
    moduleStore = checkModulesStore(pathStore)
    moduleList = listModules()
    for modL in moduleList:
        if modL not in moduleStore:
            compareList.append(modL)

    return compareList

def executeAll(pathStore):

    listModules = compareLists(pathStore)
    
    if listModules == []:
        print('Não há novos modulos para serem instalados em "%s"' %pathStore)
    else:
        for module in listModules:
            url = modules.modules[module]['url']
            path = modules.modules[module]['path']
            required = modules.modules[module]['required']
            enable = modules.modules[module]['enable']
            
            if required == True:
                print('----------Instalando modulo %s "em" %s ----------' %(module, pathStore))
                os.chdir(pathStore)
                #os.system('pwd')
                os.system('git submodule add --force %s %s' %(url, path))
                if enable == True:
                    print('---------- Ativando o modulo %s "em" %s ----------' %(module, pathStore))
                    os.system('php bin/magento module:enable %s' %module)
            else:
                continue
            
    os.chdir(pathStore)
    #os.system('pwd')
    print('---------- Rodando all em "%s" ----------' %pathStore)
    #os.system('./all.sh') #Trocar para o ./gm.sh após os testes iniciais