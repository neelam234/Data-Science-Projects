
# coding: utf-8

# A survey was conducted to gauge an audience interest in different data science topics, namely:
# 
# Big Data (Spark / Hadoop)
# Data Analysis / Statistics
# Data Journalism
# Data Visualization
# Deep Learning
# Machine Learning
# The participants had three options for each topic: Very Interested, Somewhat interested, and Not interested. 2,233 respondents completed the survey.
# 
# The survey results have been saved in a csv file and can be accessed through this link: https://cocl.us/datascience_survey_data.
# 
# If you examine the csv file, you will find that the first column represents the data science topics and the first row represents the choices for each topic.
# 
# Use the pandas read_csv method to read the csv file into a pandas dataframe, that looks like the following:
# 
# 
# In order to read the data into a dataframe like the above, one way to do that is to use the index_col parameter in order to load the first column as the index of the dataframe. Here is the documentation on the pandas read_csv method: https://pandas.pydata.org/pandas-docs/stable/generated/pandas.read_csv.html
# 
# Once you have succeeded in creating the above dataframe, please upload a screenshot of your dataframe with the actual numbers.

# In[5]:

import numpy as np  # useful for many scientific computing in Python
import pandas as pd # primary data structure library
get_ipython().system('conda install -c anaconda xlrd --yes')


# In[88]:

df_data = pd.read_csv('https://cocl.us/datascience_survey_data')                                                                                    
print('Data downloaded and read into a dataframe!')


# In[89]:

df_data


# 

# Use the artist layer of Matplotlib to replicate the bar chart below to visualize the percentage of the respondents' interest in the different data science topics surveyed.
# 
# 
# To create this bar chart, you can follow the following steps:
# 
# Sort the dataframe in descending order of Very interested.
# Convert the numbers into percentages of the total number of respondents. Recall that 2,233 respondents completed the survey. Round percentages to 2 decimal places.
# As for the chart:
# use a figure size of (20, 8),
# bar width of 0.8,
# use color #5cb85c for the Very interested bars, color #5bc0de for the Somewhat interested bars, and color #d9534f for the Not interested bars,
# use font size 14 for the bar labels, percentages, and legend,
# use font size 16 for the title, and,
# display the percentages above the bars as shown above, and remove the left, top, and right borders.

# In[90]:

df_data.sort_values(['Very interested'],ascending=False,axis=0,inplace=True)
#df_can.sort_values(['Total'], ascending=False, axis=0, inplace=True)
df_data.rename(columns={'Unnamed: 0':'Courses'}, inplace= True)
#df.set_index('Courses')
df_data


# In[91]:

cols = ['Very interested', 'Somewhat interested', 'Not interested']
#df_data[cols] = (df_data[cols].div(df_data[cols].sum(axis=1), axis=0).multiply(100)).round(2)

df_data[cols] = (100*df_data[cols]/2233).round(2)
#print(df_d.dtypes)
#df_d=(100 * df_d / 2233).round(2)
df_data


# In[92]:

get_ipython().magic('matplotlib inline')

import matplotlib as mpl
import matplotlib.pyplot as plt

mpl.style.use('ggplot')


# In[93]:

# Setting the positions and width for the bars
pos = list(range(len(df_data['Very interested']))) 
width = 0.2 
    
# Plotting the bars
fig, ax = plt.subplots(figsize=(20,8))

# Create a bar with Very interested data,
# in position pos,
plt.bar(pos, 
        #using df['pre_score'] data,
        df_data['Very interested'], 
        # of width
        width, 
        # with alpha 0.5
        alpha=0.5, 
        # with color
        color='#5cb85c', 
        # with label the first value in first_name
        label=df_data['Courses'][0])

for i in ax.patches:
    # get_x pulls left or right; get_height pushes up or down
    ax.text(i.get_x()+.04, i.get_height()+1,             str(round((i.get_height()), 2)), fontsize=14, color='dimgrey',
                rotation=0)



# Create a bar with mid_score data,
# in position pos + some width buffer,
plt.bar([p + width for p in pos], 
        #using df['mid_score'] data,
        df_data['Somewhat interested'],
        # of width
        width, 
        # with alpha 0.5
        alpha=0.5, 
        # with color
        color='#5bc0de', 
        # with label the second value in first_name
        label=df_data['Courses'][1]) 

for i in ax.patches:
    # get_x pulls left or right; get_height pushes up or down
    ax.text(i.get_x()+.04, i.get_height()+1,             str(round((i.get_height()), 2)), fontsize=14, color='dimgrey',
                rotation=0)
    

# Create a bar with post_score data,
# in position pos + some width buffer,
plt.bar([p + width*2 for p in pos], 
        #using df['post_score'] data,
        df_data['Not interested'], 
        # of width
        width, 
        # with alpha 0.5
        alpha=0.5, 
        # with color
        color='#d9534f', 
        # with label the third value in first_name
        label=df_data['Courses'][2])

for i in ax.patches:
    # get_x pulls left or right; get_height pushes up or down
    ax.text(i.get_x()+.04, i.get_height()+1,             str(round((i.get_height()), 2)), fontsize=14, color='dimgrey',
                rotation=0)

# Set the y axis label
#ax.set_ylabel('Percentage')

# Set the chart's title
ax.set_title('Percentages of Responents interested in Data science areas',fontsize=16)

# Set the position of the x ticks
ax.set_xticks([p + 1.5 * width for p in pos])

# Set the labels for the x ticks
ax.set_xticklabels(df_data['Courses'])
ax.set_facecolor('white')

# Setting the x-axis and y-axis limits
plt.xlim(min(pos)-width, max(pos)+width*4)
plt.ylim([0, max(df_data['Very interested'] + df_data['Somewhat interested'] + df_data['Not interested'])] )

# Adding the legend and showing the plot
plt.legend(['Very interested', 'Somewhat interested', 'Not interested'], loc='upper right',fontsize=14)

plt.show()


# In[ ]:



