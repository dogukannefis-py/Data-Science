#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def updateJSONFile(path, x):
    
    """
        Read json file, update the dictinary, dump to the json and write to the json file
    """
    
    filePath='/' + path + '/' 
    filePathX = filePath + 'hata.json'
    
    myData=json.load(open(filePathX))                       ## read the json file
    
    print("Old JSON: ",myData)
    array=list(myData.keys())


    if hatali_parametre in array:
        myData[x]=myData[x]+1     ## append new element
        myData[x]
    elif hatali_parametre not in array:
        new_data = {x:1}                         ## updating the data 
        myData.update(new_data)

    print("New JSON: ",myData)
    j=json.dumps(myData)                                        ## dictionary to json_object

    with open('/root/10_Autoencoder_Anomaly/Models/E114/EK-2451/hata.json', 'w') as f:     
        f.write(j)                                          
        f.close()

