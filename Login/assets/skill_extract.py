import mammoth
import sys
import re
import os

printer = False
skills = dict()
name = ""

def getIndexForValues(string):
	for ind,i in enumerate(string):
		if i == ':':
			return (ind+1)

def section_complete(input_sent,section):
	if (len(input_sent.split()) == 1) and (input_sent.split()[0] != "Skills"):
		return True
	else:
		return False

def run(filename):
    global printer, skills, name
    with open(str(os.path.dirname(os.path.realpath(__file__))+'/../../media/media/'+filename), "rb") as docx_file:
        result = mammoth.extract_raw_text(docx_file)
        text = result.value 

        count = 0

        text = text.split("\n")
        for line in text:
        	x = re.search("[A-Za-z]*Name[A-Za-z+]*",line)
        	if x:
        		i = getIndexForValues(line)
        		name = line[i:].strip()

        	if printer:
        		x = re.search("[A-Za-z]*:[A-Za-z+]*",line)
        		if x:
        			count += 1

        		x = re.search("[A-Za-z]*languages[A-Za-z+]*",line)
        		if x:
        			i = getIndexForValues(line)
        			if "languages" in skills.keys():
        				langs = line[i:].split(",")
        				for i in langs:
        					skills["languages"].append(i.strip()) 
        			else:
        				skills["languages"] = list()
        				langs = line[i:].split(",")
        				for i in langs:
        					skills["languages"].append(i.strip())

        		x = re.search("[A-Za-z]*tools[A-Za-z+]*",line)
        		if x:
        			i = getIndexForValues(line)
        			if "tools" in skills.keys():
        				langs = line[i:].split(",")
        				for i in langs:
        					skills["tools"].append(i.strip()) 
        			else:
        				skills["tools"] = list()
        				langs = line[i:].split(",")
        				for i in langs:
        					skills["tools"].append(i.strip())

        		x = re.search("[A-Za-z]*operating systems[A-Za-z+]*",line)
        		if x:
        			i = getIndexForValues(line)
        			if "operating systems" in skills.keys():
        				langs = line[i:].split(",")
        				for i in langs:
        					skills["operating systems"].append(i.strip())
        			else:
        				skills["operating systems"] = list()
        				langs = line[i:].split(",")
        				for i in langs:
        					skills["operating systems"].append(i.strip())

        		x = re.search("[A-Za-z]*technologies[A-Za-z+]*",line)
        		if x:
        			i = getIndexForValues(line)
        			if "technologies" in skills.keys():
        				langs = line[i:].split(",")
        				for i in langs:
        					skills["technologies"].append(i.strip()) 
        			else:
        				skills["technologies"] = list()
        				langs = line[i:].split(",")
        				for i in langs:
        					skills["technologies"].append(i.strip())

        	if line == "Skills":
        		printer = True

        	if section_complete(line,"Skills"):
        		printer = False

        print("Total Number of skills found for ",name," : ",count)
        for key in skills:
        	print(key," : ",skills[key])
        with open("Login/assets/output.txt","w") as file:
            for key in skills:
                file.write(key)
                file.write('\n')
                for i in skills[key]:
                    file.write(i)
                    file.write('\n')
    return
