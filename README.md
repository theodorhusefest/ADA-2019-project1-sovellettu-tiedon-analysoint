# Applied Data Analysis - Project

(Projects notebook for milestone 2: project_notebook.ipynb)

### Abstract
In recent years, meat consumption has received a lot of attention as a result of global warming. Meat production is said to be one of the largest contributors to global warming as the production of meat requires a lot of resources, such as huge amounts of water and land-area. Especially red meat has received a reputation for being a large contributor to climate change, and it would be interesting to see if there is data to support this claim. We suspect that the meat-industry has affected the production of crops, which we assume has lower greenhouse emissions compared to meat. In this project we want to understand and study how production of crops and livestock have changed globally since the 1960s, as well as looking at the consequences of this. Datasets from fao.org, the Food and Agricultural Organization of the United Nations, will be used.

## Research questions
How has the crops/livestock primary production developed since 1960?  
Is there a connection between the development of livestock primary production and crop production?  
How are the differences in production quantities between the different continents?  
How has the development in agriculture affected emission of greenhouse gasses?  

## Dataset
http://www.fao.org/faostat/en/#data/QL  
https://www.kaggle.com/unitednations/global-food-agriculture-statistics
http://www.fao.org/faostat/en/#data/OA
http://www.fao.org/faostat/en/#data/EM
http://www.fao.org/faostat/en/#data/EI

We have decided to compliment FAOs Global Food and Agriculture dataset with another dataset from FAO containing data on livestock primary production. This is due to the fact that the Global Food and Agriculture dataset does not contain any information regarding livestock and we want to be able to study the relationship between how crops and livestock production have developed over the last half decade. The online datasets are extremely big and comprehensive, but luckily easy to use thanks to them being well structured and easy to understand. We are able to exactly choose which data to download, but it will be a challenge to choose the most valuable and interesting data. We are also complimenting the crops and livestock production data with data on CO2 emissions from agriculture in order to answer our 4th research question. We are also using population data in order to study if the agriculture production is simply due to increasing/decreasing population or if that doesn't have anything to do with it.

## Internal Milestones until Project Milestone 2
1 - Data Wrangling and Exploration (Deadline 4th November)
- Decide on the most important indicators/features in the datasets and download
- Look at the dataset and get a feel of the data (distributions etc)
- Be as certain as possible that if we have enough and correct data to move on   

2 - Data Cleaning (Deadline 11th November)
- Remove errors, or unimportant information
- Decide on important groupings  

3 - Data Analysis and Visualization (Deadline 18th November)
- Find key statistical indicators 
- Visualize the results   

4 - Finalize notebook (Deadline 25th November)
- Make sure that the analysis is well documented and motivated
- Make sure that the visualization choices are optimal and easy to understand

## Internal Milestones until Project Milestone 3 

In the next section we have written how we will answer all the research questions, and we will therefore not go in detail of that here.  
This is to be considered an overall plan.

1 - Answer research Questions 1 & 2 (29th November)

2 - Answer research Questions 3 & 4. (6th December)
- Decide on either report or data story.

3 - Finish visuals and make a draft of report/data story (13th December)

4 - Final Deadline (20th December)
- Make sure the report/data is consistent, and includes all the important information.
- Make sure the final notebook (extending on Milestone 2) is comprehensive and includes all mathematical calculations.
- Update readme with contributions of team members (including who works on the final presentation)

5 - Presentations (18th January)
- Finnish poster for presentation
- Decide on who talks
- Prepare a 3 min presentation

&nbsp;

## Further specifing the questions and project goals
In this section we will more clearly define our _project questions_ and _project goals_.
### Questions
We will specify each question in order to provide the reader with a more specific view of the project.
#### Question 1 - How has the crops/livestock primary production developed since 1960?
***
This question will serve as an intro to the whole project and look at the big trends in the world, with focus on products more than areas. We will mainly study total development of production (without normalizing for population), as this is how the production actually has developed and how the scale has changed during the 50 years.  
We will follow these steps:

- Get an overview of development by analyzing at world-level.
- Look if any special products have increased/decreased in popularity.
- Find statistical indicators showing the differences now and in 1960.
- Look for certain countries and areas that stand out.

&nbsp;
#### Question 2 - Is there a connection between the development of livestock primary production and crop production?
***
The purpose of this question is to see if there are any trends in our data, and to answer this we will study both total and normalized data. We will also have to look at 

- Are we producing more food per person?
- Has the porportions of meat vs. crops changed in our diet?
- Can we see differences between each continent?

&nbsp;   

#### Question 3 - How are the differences in production quantities between the different continents?
***
The purpose of this question is to study the difference in production at a continent-level. For example, it can be interesting to see the difference between developed continents, like Europe and North-America, and continents like Africa and Asia. 

- Study food production in general, and with a crops vs. meat analysis.
- What can be said about the normalized production?
- Can we say if any continents are producing more than it needs?
- Try to find data on how much food a person needs per year. 
    - This is pretty hard because of energy/tonne
    
&nbsp;

#### Question 4 - How has the development in agriculture affected emission of greenhouse gasses?
***

This question is about the consequences of what we have studied in the previous questions.

- Can we find evidence that higher meat consumption leads to higher emissions?
- Is it better for the environment to eat crops rather than livestock?
- Are there any particular meat or crop that affect the CO2 emissions more/less than the average?

&nbsp;
### Summary of goals
***
The goal of this project is to give the reader an understanding of the trends in agriculture development, both worldwide and on continent level. Furthermore, we will examine how our food habit has developed and affected the world-wide CO2 emissions.
