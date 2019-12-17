
# coding: utf-8

# ## DATA VISUALISATION_MAPS

# You are required to create a Choropleth map to visualize crime in San Francisco.
# 
# Before you are ready to start building the map, let's restructure the data so that it is in the right format for the Choropleth map. Essentially, you will need to create a dataframe that lists each neighborhood in San Francisco along with the corresponding total number of crimes.
# 
# Based on the San Francisco crime dataset, you will find that San Francisco consists of 10 main neighborhoods, namely:
# 
# Central,
# Southern,
# Bayview,
# Mission,
# Park,
# Richmond,
# Ingleside,
# Taraval,
# Northern, and,
# Tenderloin.
# Convert the San Francisco dataset, which you can also find here, https://cocl.us/sanfran_crime_dataset, into a pandas dataframe, like the one shown below, that represents the total number of crimes in each neighborhood.
# 
# https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/UcAIVlVkEeiDhgqYR-Lxvg_94c477dfeb3935cccb0b468f5c9ba46b_crime_dataset_masked.png?expiry=1576713600000&hmac=VGCOoyqkoJ5ty6YTzbFNzfuh7Xq4JScJPsurS9NhlnQ
# 
# 

# In[1]:

import numpy as np  
import pandas as pd

df1 = pd.read_csv('https://cocl.us/sanfran_crime_dataset')                                                                                    
print('Data downloaded and read into a dataframe!')


# In[2]:

df1


# In[3]:

df1.rename(columns={"PdDistrict":"Neighborhood"},inplace=True)
df1


# In[4]:

df=df1.groupby(["Neighborhood"]).size().reset_index(name="Count")
df


# In[6]:

df.sort_values('Count',ascending=False,inplace=True)
df


# In[8]:

df1 = df.reset_index(drop=True)
df1


# Now you should be ready to proceed with creating the Choropleth map.
# 
# As you learned in the Choropleth maps lab, you will need a GeoJSON file that marks the boundaries of the different neighborhoods in San Francisco. In order to save you the hassle of looking for the right file, I already downloaded it for you and I am making it available via this link: https://cocl.us/sanfran_geojson.
# 
# For the map, make sure that:
# 
# it is centred around San Francisco,
# you use a zoom level of 12,
# you use fill_color = 'YlOrRd',
# you define fill_opacity = 0.7,
# you define line_opacity=0.2, and,
# you define a legend and use the default threshold scale.
# If you follow the lab on Choropleth maps and use the GeoJSON correctly, you should be able to generate the following map:
# 
# https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/okW9uVVkEeiDhgqYR-Lxvg_9e78dcfa79cdc9d18d31ac51173865db_sanfran_map_masked.png?expiry=1576713600000&hmac=2aOOclYKFAj3CO_8nrvFr-Omy4FcXUNXbQkL_kKWi0M
# 
# 

# In[9]:

get_ipython().system('conda install -c conda-forge folium=0.5.0 --yes')
import folium

print('Folium installed and imported!')


# In[13]:

world_geo=r'https://cocl.us/sanfran_geojson'
world_map = folium.Map(location=[37.77,-122.42], zoom_start=12)


# In[16]:

world_map.choropleth(
    geo_data=world_geo,
    data=df1,
columns=['Neighborhood', 'Count'],

key_on='feature.properties.DISTRICT',

fill_color='YlOrRd',

fill_opacity=0.7,

line_opacity=0.2,

legend_name='Crime Rate in San Francisco'

)

# display map

world_map


# In[ ]:



