import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import numpy as np
import warnings
warnings.filterwarnings("ignore")

data = pd.read_csv("Login/assets/companies_dataset.csv")

## Data Pre-processing
languages = data[['L1','L2','L3','L4']]
operatings = data[['O1','O2','O3','O4']]
technologies = data[['T1','T2','T3','T4']]
tools = data[['M1','M2','M3','M4']]

output_company = data[['Company']]

###

lang_replace_dict = {'c#':0.045,'d':0.091, 'java':0.182, 'c':0.273,
                    'javascript':0.364,'python':0.455, 'haskell':0.546,
                    'objective-c':0.637,'ruby':0.728,'perl':0.819,
                    'php':0.91, 'c++':0.99, 'shell':0.22}
languages = languages.replace(lang_replace_dict)

###

operating_replace_dict = {'unix':0.25, 'Mac':0.50,
                        'Linux':0.75, 'Windows':0.99,
                        'windows 98/2000/xp':0.44,'gnu/linux':0.33}
operatings = operatings.replace(operating_replace_dict)

###

tech_replace_dict = {'cuda':0.1, 'hadoop':0.2, 'cgi':0.3,
                    'android':0.4, 'big data':0.5, 'flutter':0.6,
                    'html':0.7, 'angular':0.8, 'datamining':0.9,
                    'xml':0.99, 'mysql':0.27}
technologies = technologies.replace(tech_replace_dict)

###

tool_replace_dict = {'Machine learning':0.125, 'video editing':0.250,
                    'Deep Learning':0.375, 'Azure':0.500,'latex':0.450,
                    'onnx':0.625, 'netbeans':0.750,
                    'photoshop':0.875, 'gnu/gcc':0.688,'microsoft office':0.999,
                    'visual studio 2005/08':0.44}
tools = tools.replace(tool_replace_dict)

###

bigdata = pd.concat([languages, operatings, technologies, tools], axis=1)


company_dict = {'Microsoft':0.05,'Facebook':0.1,
                'Mistral Solutions':0.15,'Zetwerk':0.2,
                'Google':0.25,'Hffc':0.3,'Sasken':0.35,
                'Akkamai':0.4,'Allgo':0.45,'Subex':0.50,
                'Byzus':0.55,'tcs':0.60,
                'tcs digital':0.65,'ninja kart':0.70,
                'we work':0.75,'mindtree':0.8,'ticker':0.85,
                'global edge':0.9,'mercedes benz':0.95,
                'quartz':0.99}
output_company = output_company.replace(company_dict)

bigdata = bigdata.replace({None:1.0})
output_company = output_company.replace({None:1.0})

bigdata = bigdata * 100
output_company = output_company * 100

bigdata = bigdata.astype('int64')
output_company = output_company.astype('int64')

## Model Building
X_train, X_test, y_train, y_test = train_test_split(bigdata,output_company,test_size=0.05)

clf = KNeighborsClassifier(n_neighbors=18)
clf.fit(X_train,y_train)


## reading data
fields = ['languages','operating systems','technologies','tools','RANDOM']
ind = 0
main_data = list()
temp_data = list()
with open("Login/assets/output.txt","r") as file:
    input_data = file.read().splitlines()
    accept = True
    for i in input_data:
        if i == fields[ind]:
            main_data.append(temp_data)
            temp_data = list()
            count = 0
            accept = True
            ind += 1
            continue
        if accept:
            temp_data.append(i)
            count += 1
            if count == 4:
                count = 0
                accept = False
    main_data.append(temp_data)

X_input = list()
for i in main_data:
    count = 0
    if i == []:
        continue
    for j in i:
        count += 1
        X_input.append(j)
    if count < 4:
        for k in range(count,4):
            X_input.append(100)

X_input = pd.DataFrame([X_input])
X_input = X_input.replace(lang_replace_dict)
X_input = X_input.replace(operating_replace_dict)
X_input = X_input.replace(tech_replace_dict)
X_input = X_input.replace(tool_replace_dict)


## Prediction
y_pred = clf.predict(X_input)

#####################################
val = 0
for i in output_company['Company']:
    if int(y_pred[0]) <= int(i):
        val = i
        break
   
val = val / 100.0
for key, value in company_dict.items():
    if value == val:
        with open("Login/assets/placed.txt","w") as file:
            file.write(str(key))

