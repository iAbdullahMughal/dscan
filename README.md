

![Heroku](http://heroku-badge.herokuapp.com/?app=isharingan&style=flat)  [![Requirements Status](https://requires.io/github/iAbdullahMughal/Sharingan/requirements.svg?branch=master)](https://requires.io/github/iAbdullahMughal/Sharingan/requirements/?branch=master) [![codecov](https://codecov.io/gh/iAbdullahMughal/Sharingan/branch/master/graph/badge.svg)](https://codecov.io/gh/iAbdullahMughal/Sharingan) [![CircleCI](https://circleci.com/gh/iAbdullahMughal/Sharingan.svg?style=svg)](https://circleci.com/gh/iAbdullahMughal/Sharingan)  
  
# Sharingan  
A flask python based project for static analysis of office documents. Currently aiming to generate infographic diagrams 
from macro code and it's file structure. Currently it's under development. There any multiple updates and changes 
planned. Currently project has some basic tools loaded for office document analysis. Few points are listed below;

## Extraction of macro code  
Currently project is enable to extract macro form office document and displaying results on web UI.  
- :information_source: **Work In Progress**
  
## Visualization of macro content  
Allot of malicious document contains macro code. In this project we'll try to achive some visualization and flow  
diagram of macro code.  
- Currently project is visualizing internal defined function function within vba code.   
- We'll expend the scope and visualize the flow of macro code instead of functions.   
     
## Office document file system structure visualization 
Project is enabled to show office document internal directory structure in web UI. This helps to view sources and files 
added into office document.
- Extraction of file system structure is in progress

Currently this project is displaying results on web UI.
  
## Parsing of OOXML and internal sources 
- Analysis of OOXML and internal sources which contains information related to document is in progress.

There may be xml & different configuration files which contains information related to indication of sample's nature 
which needs to be analysed. 
  
## Support for external modules   
- In progress 
  
## Overview of UI  
- Demo of project can be accessed on following url https://isharingan.herokuapp.com  
- A picture speaks a thousand words

![Demo of Sharingan](./stuff/Info.gif)  
- For testing propuse office samples were used from InQuest's malware-samples repo. These samples are accessible from
following url 
- [InQuest](https://github.com/InQuest/malware-samples)   
  
## How to deploy   
This project is build on python 3.6. Ensure installed on system, rest follow as,

    apt-get install p7zip-full libfuzzy-dev libpulse-dev  (sudo if required)
    git clone https://github.com/iAbdullahMughal/Sharingan.git
    cd Sharingan
    pip3 install requirements.txt (sudo if required)
    python3 app.py
 
 If any issue/ failure appeared during installation of project, please report.

## Resources consumed  - Need updates
For the development of this project different free and open source libraries were used. You can find more details and   
information in [SHOUTOUT.md](./stuff/SHOUTOUT.md)  
  
## LICENSE 
Project is under MIT License. More information [LICENSE](./stuff/LICENSE)

## More Work
- Road map and milestones of project 
- Documentation of code
- Test cases (currently not configured properly)
- Resources consumed needs update
- Change log