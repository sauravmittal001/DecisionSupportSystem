# DecisionSupportSystem

> Hassle-less data management and access for government officials of India

### 🌟 Website Screens

|  ![alt text](https://github.com/sauravmittal001/DecisionSupportSystem/blob/master/img/screenshot6.jpg)  |  ![alt text](https://github.com/sauravmittal001/DecisionSupportSystem/blob/master/img/screenshot1.jpg)  |  ![alt text](https://github.com/sauravmittal001/DecisionSupportSystem/blob/master/img/screenshot2.jpg)  |
| ----------- | ----------- | ----------- |
| ![alt text](https://github.com/sauravmittal001/DecisionSupportSystem/blob/master/img/screenshot3.jpg) | ![alt text](https://github.com/sauravmittal001/DecisionSupportSystem/blob/master/img/screenshot4.jpg) | ![alt text](https://github.com/sauravmittal001/DecisionSupportSystem/blob/master/img/screenshot5.jpg) |

---

## 🚀 Getting Started

### Activating Virtual Environment 
`source newenv/bin/activate`

### Running the code 
`python3 manage.py runserver`

### Clone

- Clone this repo to your local machine using `https://github.com/sauravmittal001/DecisionSupportSystem`

### Setup

> update and install git

```shell
$ ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
$ brew install git
$ git --version
```

> config account

```shell
$ git config --global user.name "Your Name"
$ git config --global user.email "Your Email"
$ git config --list
```

> clone repo

```shell
$ git init
$ git clone https://github.com/sauravmittal001/DecisionSupportSystem
```

---
## 📃 About

 **Decision Support System is a project for Indian District Magistrates (DMs). The Decision Support System (DSS) is a product that acts as a Dashboard and uses Operations Research/ Artificial Intelligence methods for decision making.**
 The project involves:
- Interaction with IAS and Other government officers
- Creating a Dashboard/DSS Architecture, coding it up
- Using Operations Research and AI tools and more

### ✨ Project Contribution

**Law and Order Section**
The Law and Order Section is responsible for storing and processing details, experience and feedback of district events in the district. Event details and attributes can be found [here](https://github.com/sauravmittal001/DecisionSupportSystem/blob/master/DSS_Law_and_Order_Attributes.pdf)
These details and experiences are stored as a future references when the person in-charge has to attend/handle a similar event in future. The past data would help to predict what all measures would help in the future events.
Similarly, all the help regarding literature reading, convenient logistics and helpful advices would help the officer in-charge.

**Dashboard**
The Dashboard of the Decision Support System is built on a website. I was involved in the backend development of the law and order section. I also created Forms to submit data regarding the events and tables to show the data in the website.
I used Django as the backend web framework and MySQL as the database management system. I worked on python and SQL. I created the forms and tables using HTML, CSS and Javascript.
- Created APIs (GET & POST request)
- Created Model Forms for data submission from front-end and store in database
- Created Tables with Search feature to filter the data with name of event.
