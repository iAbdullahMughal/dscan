

![Heroku](http://heroku-badge.herokuapp.com/?app=isharingan&style=flat)  [![Requirements Status](https://requires.io/github/iAbdullahMughal/Sharingan/requirements.svg?branch=master)](https://requires.io/github/iAbdullahMughal/Sharingan/requirements/?branch=master) [![codecov](https://codecov.io/gh/iAbdullahMughal/Sharingan/branch/master/graph/badge.svg)](https://codecov.io/gh/iAbdullahMughal/Sharingan) [![CircleCI](https://circleci.com/gh/iAbdullahMughal/Sharingan.svg?style=svg)](https://circleci.com/gh/iAbdullahMughal/Sharingan)  
  
# Sharingan  
A flask python based project for static analysis of office documents. Currently development is in progress. This  
project will help to extract different artifices and information from the document. Currently project is show some basic  
information of office file and embedded macro. (work in progress)  

Check [demo](https://isharingan.herokuapp.com/)
## Extraction of macro code  
Currently project is enable to extract macro form office document and showing them on web UI.  
- :information_source: **Work In Progress**
  
## Visualization of macro content  
Allot of malicious document contains macro code in it. In this project we'll try to achive some visualization and flow  
diagram of macro code.  
- Currently project is visualizing internal defined function function within vba code.   
- We'll expend the scope and visualize the flow of macro code instead of functions.   
     
#### Resource extraction  
:sob: Yet to come  
  
#### Parsing of OOXML and URL extraction  
:sob: Yet to come  
  
#### Support for external modules ??  
:sob: Yet to come  
  
# Overview of UI  
You can access demo on herokuapp. https://isharingan.herokuapp.com  
  
![Demo of Sharingan](./stuff/flow.gif)  
We used office samples from following resources,  
- We have some reports for demo  
-- [InQuest](https://github.com/InQuest/malware-samples)   
  
# How to deploy   
This project is build on python 3.6. Ensure installed on system, rest follow as,

    git clone https://github.com/iAbdullahMughal/Sharingan.git
    cd Sharingan
    pip3 install requirements.txt (sudo if required)
    python3 app.py
 

# Resources consumed  
For the development of this project different free and open source libraries were used. You can find more details and   
information in [SHOUTOUT.md](./stuff/SHOUTOUT.md)  
  
# LICENSE 
Project is under MIT License. More information [LICENSE](./stuff/LICENSE)