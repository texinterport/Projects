#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[51]:


pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', -1)


# #### Input CSV

# In[243]:


crime = pd.read_csv(r'\Users\HP\OneDrive\Desktop\BostonCR2020.csv')
hourly_cases = pd.read_csv(r'\Users\HP\OneDrive\Desktop\Hourly_Cases.csv')


# #### Research Questions

# In[ ]:


# 1) What is the most common offense recorded and the least?

# 2) Are some days, hours and months more dangerous than others?

# 3) Does the city experience a lot of shootings?

# 4) What is the most dangerous part of the city?

# 5) Are there any additional trends?


# #### Boston Crime Report 2020

# In[99]:


crime.dtypes


# In[4]:


crime.head()


# In[70]:


crime.describe(include=object)


# #### 1) Top Offenses Reported

# In[58]:


crime['OFFENSE_DESCRIPTION'].value_counts().sort_values()


# In[322]:


# Graph depicting the above stats as the top 10
case_df={'Offense':['LARCENY SHOPLIFTING', 'SICK/INJURED/MEDICAL - PERSON', 'TOWED MOTOR VEHICLE', 'ASSAULT - SIMPLE', 'LARCENY THEFT FROM MV - NON-ACCESSORY','INVESTIGATE PROPERTY','VANDALISM','M/V - LEAVING SCENE - PROPERTY DAMAGE','SICK ASSIST','INVESTIGATE PERSON'],'Case_Count':[2025,2442,2552,2607,2708, 3222, 3323, 3603, 4236, 5122]}

case_number =pd.DataFrame(case_df)
           
case_number.plot.barh(x='Offense', y='Case_Count')
plt.xlabel('Offense')
plt.ylabel('Case Count')
plt.title('Top 10 Reported offenses')


# #### 2) Are Some Days / Hours / Months more dangerous than others?

# In[415]:


crime["DAY_OF_WEEK"] = pd.Categorical(crime["DAY_OF_WEEK"])


# In[416]:


# Friday has the most reported offenses, Sunday the least
crime['DAY_OF_WEEK'].value_counts().sort_values().plot(kind='barh')
plt.xlabel('Number of Cases')
plt.ylabel('Day of the Week')
plt.title('Number of Cases per Day of the Week')


# In[417]:


crime.groupby('DAY_OF_WEEK').describe()


# In[6]:


crime['YEAR']= pd.to_datetime(crime['YEAR'])


# In[47]:


crime['OCCURRED_ON_DATE']= pd.to_datetime(crime['OCCURRED_ON_DATE'])


# In[ ]:


# The most crimes were committed in October
# The least amount of crimes were committed in April 


# In[324]:


crime.groupby('MONTH')['OFFENSE_DESCRIPTION'].count().plot()
plt.xticks(crime.MONTH[::3])
plt.xlabel('Month')
plt.ylabel('Count of Crimes')
plt.title('Count of Crimes Per Month')
plt.show


# In[327]:


# Top three months for caseloads are October, August and September
# October, August, September, January 
# July, June, February, November
# December, March, May, April
crime.groupby('MONTH')['OFFENSE_DESCRIPTION'].count()


# In[247]:


# Most crime overall ocurred at 0000
grouped = hourly_cases.groupby("Hour")
mean = grouped.mean()
print(mean)


# In[328]:


# Most crime overall ocurred at 0000, the least at 0400
offense_street = crime.groupby('HOUR')['OFFENSE_DESCRIPTION'].count()
offense_street.sort_values(ascending=False)


# In[ ]:


# Graph depicting the changes in caseloads throughout the day
# Steady decline after the peak at 0000 before rising again after 0500 before declining again after 1400


# In[525]:


data_ten={'Hour':['0','1','2','3','4','5','6','7','8','9','10','11', '12', '13', '14', '15','16', '17', '18', '19', '20', '21','22','23'],'Case_Count':[4992, 1833, 1433, 990, 742, 782, 1059, 1807, 2687, 3281, 3500, 3668, 4547, 3847, 3888, 3799, 4482, 4361, 4135, 3689, 3453, 3110, 2686, 2123]}

time_data =pd.DataFrame(data_ten)

time_data.plot.line()
plt.xlabel('Hour')
plt.ylabel('Case Count')
plt.title('Case Count Throughout the Day')


# #### Time Trends for Top Offenses

# In[ ]:


# Of the top five offenses, Investiage Person is has the most reported cases at 0000
# Followed by Vandalism, Investiage Property and M/V Leaving the Scene - Property Damage (all top offenses)


# In[256]:


hour_one = crime.query('OFFENSE_DESCRIPTION == "LARCENY THEFT FROM MV - NON-ACCESSORY" & HOUR == "0"')
hour_one.count()


# In[258]:


# New df created to represent the top five offenses and their counts at 0000
crime_data={'Offense':['Investigate_Person','Vandalism','Investigate_Property','MV_Leaving_Scene','Larceny_Theft'],'Cases':[335,235,232,229,194]}

top_crimes =pd.DataFrame(crime_data)
           
print(top_crimes)


# In[261]:


# Graph of top five offenses at 0000. The bottom four are pretty close, whereas Investigate Person commands a strong lead
top_crimes.plot.barh(x='Offense', y='Cases')
plt.xlabel('Number of Cases')
plt.ylabel('Offense')
plt.title('Top Five Offenses Occuring at 0000')


# In[ ]:


# Investiage Person numbers throughout the week. Monday and Wednesday are about the same with 760. 
# The weekend has the least amount


# In[276]:


query = crime.query('OFFENSE_DESCRIPTION == "INVESTIGATE PERSON" & DAY_OF_WEEK == "Saturday"')
query.count()

query_df={'Day of Week':['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday'],'Case':[760,748,761,738, 759, 689, 667]}

query_day =pd.DataFrame(query_df)
           
print(query_day)


# In[280]:


# Pretty consistent with a slight drop over the weekend. Looks a lot like the chart detailing all cases per day.
query_day.plot.barh(x='Day of Week', y='Case')
plt.xlabel('Day of Week')
plt.ylabel('Case Count')
plt.title('Invesitgate Person Cases Per Day')


# #### 3) Shooting Details

# In[200]:


# Shootings peaked in June before declining
# December and January had the least amount of shootings
crime.groupby(['MONTH', 'SHOOTING'])['OCCURRED_ON_DATE'].count()


# In[215]:


# 1122 total shootings
crime.query('SHOOTING == "1"').count()


# In[348]:


# The most shootings occurred on Saturday
shooting_query = crime.query('SHOOTING == "1" & DAY_OF_WEEK == "Sunday"')
shooting_query.count()


# In[350]:


# The graph shows more shootings on the weekends than the weekdays.
data_twenty={'Day':['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday'],'Number of Shootings':[121,152,153,137,176,203,180]}

shooting_numbers =pd.DataFrame(data_twenty)

shooting_numbers.plot.bar(x='Day', y='Number of Shootings')
plt.xlabel('Day of Week')
plt.ylabel('Shootings')
plt.title('Count of Shootings per Day')


# In[664]:


# Total shootings on Saturdays consist of 33 shootings at 0000 and 0 shootings at 0600, 1100 and 1500.
shooting_query_two = crime.query('SHOOTING == "1" & DAY_OF_WEEK == "Saturday" & HOUR =="23"')
shooting_query_two.count()


# In[665]:


data_shot={'Hour':['0','1','2','3','4','5','6','7','8','9','10','11', '12', '13', '14', '15','16', '17', '18', '19', '20', '21','22','23'],'Shootings':[33,18,17,8,9,4,0,1,2,2,3,0,4,2,5,0,7,14,7,12,9,12,17,17]}

gun_data =pd.DataFrame(data_shot)

gun_data.plot.line()
plt.xlabel('Hour')
plt.ylabel('Shootings')
plt.title('Shootings Throughout the Day on Saturday')


# In[65]:


crime['OFFENSE_CODE']=crime.OFFENSE_CODE.astype(object)


# #### Comparing different Offense Counts to Each Other

# In[111]:


#person_one = crime.query('OFFENSE_DESCRIPTION == "INVESTIGATE PERSON" & MONTH == "1"')
person_one.count()

data={'Month':['Jan','Feb','March','April','May','June','July','Aug','Sept','Oct','Nov','Dec'],'Investigate_Person_Cases':[431,396,409,326,440,426,479,476,476,487,382,394]}

iv_data =pd.DataFrame(data)
           
print(iv_data)
                                                                                                                


# In[250]:


# Investigate Person Cases Per Month
# The most was in July and the summer
iv_data.plot.line(x='Month', y= 'Investigate_Person_Cases')
plt.xlabel('Month')
plt.ylabel('Cases')
plt.title('Investigate Person Cases Per Month')


# In[117]:


# Sum of all offenses per month is pretty similar to the Investigate Person Cases
crime.groupby('MONTH')['OFFENSE_DESCRIPTION'].count().plot()
plt.xticks(crime.MONTH[::3])
plt.xlabel('Month')
plt.ylabel('Sum of Crimes')
plt.title('Sum of Crimes Per Month')
plt.show


# In[119]:


data_two={'Month':['Jan','Feb','March','April','May','June','July','Aug','Sept','Oct','Nov','Dec'],'Assault_Simple_Cases':[270,249,229,132,199,216,265,249,235,224,173,166]}

as_data =pd.DataFrame(data_two)
           
print(as_data)


# In[249]:


# Assult Cases - Simple per month is also similar to sum of all cases per month
as_data.plot.line(x='Month', y= 'Assault_Simple_Cases')
plt.xlabel('Month')
plt.ylabel('Cases')
plt.title('Assault Simple Cases Per Month')


# In[121]:


data_three={'Month':['Jan','Feb','March','April','May','June','July','Aug','Sept','Oct','Nov','Dec'],'Robbery':[85,58,73,84,48,76,75,66,68,76,55,49]}

rb_data =pd.DataFrame(data_three)
           
print(rb_data)


# In[251]:


# Robbery does not follow the same trends as the other cases
rb_data.plot.line(x='Month', y= 'Robbery')
plt.xlabel('Month')
plt.ylabel('Cases')
plt.title('Robbery Cases Per Month')


# #### 4) Most Dangerous Part of the City: Washington St

# In[124]:


# Washington St had a total of 3276 offenses recorded, followed by Blue Hill Ave (1277) and Massachusetts Ave (1076)
crime['STREET'].value_counts().sort_values()


# In[ ]:


# Washington St has a clear command of the top for most reported cases vs the next two on the list

# Despite the differences in numbers, the three streets look similar in trend between when they peak and fall.


# In[393]:


street_two = crime.query('MONTH == "12" & STREET == "TREMONT ST"')
street_two.count()

data_street={'Month':['Jan','Feb','March','April','May','June','July','Aug','Sept','Oct','Nov','Dec'],'Number_of_Cases':[320, 330, 306, 232, 224, 235, 248, 267, 280, 301, 276, 257]}

street_three=pd.DataFrame(data_street)

data_blue={'Month':['Jan','Feb','March','April','May','June','July','Aug','Sept','Oct','Nov','Dec'],'Number_of_Cases':[123, 110,127,78, 100, 89, 130, 140, 108,100,91,81       ]}

street_four=pd.DataFrame(data_blue)

data_tremont={'Month':['Jan','Feb','March','April','May','June','July','Aug','Sept','Oct','Nov','Dec'],'Number_of_Cases':[107,105,63,52,98,94,109,85,103,121,91,48]}

street_five=pd.DataFrame(data_tremont)

plt.figure(figsize=(8,5))
plt.title('Street Cases Per Month')
plt.plot(street_three.Month, street_three.Number_of_Cases, label='Washington St')
plt.plot(street_four.Month, street_four.Number_of_Cases, label='Bill Hill Ave')
plt.plot(street_five.Month, street_five.Number_of_Cases, label='Tremont St')

plt.xticks(street_three.Month, rotation='vertical')
plt.xlabel('Month')
plt.ylabel('Number of Cases')

plt.legend()

plt.show


# #### Washington St Stats

# In[466]:


# The top ten offenses were also high on Washington St
# However, Aggravated Assault (which did not make the top ten overall) was high for Washington St
# And Investigate Person was not the top offense on Washington St, Larceny Shoplifting had the most cases here

crime.query('STREET == "WASHINGTON ST" & OFFENSE_DESCRIPTION =="INVESTIGATE PROPERTY"').count()

data_was={'Offense':['Investigate_Person','Vandalism','Sick Assist','M/V Leaving Scene','Investigate Property','Assault Simple','ASSAULT AGGRAVATED','LARCENY SHOPLIFTING','Larceny Theft from M/V','Towed M/V','Sick/Injuried Person'],'Cases':[246,123,174,112,141,127,108, 251,62,44,101]}

street_crime=pd.DataFrame(data_was)

street_crime.plot.bar(x='Offense', y='Cases')
plt.xlabel('Offense')
plt.ylabel('Case')
plt.title('Top Offenses on Washington St')


# In[523]:


# Highest number of shoplifting offenses occurred at 1200
crime.query('STREET == "WASHINGTON ST" & OFFENSE_DESCRIPTION =="LARCENY SHOPLIFTING" & HOUR =="23"').count()

data_shop={'Hour':['0','1','2','3','4','5','6','7','8','9','10','11', '12', '13', '14', '15','16', '17', '18', '19', '20', '21','22','23'],'Cases':[3,0,0,0,0,0,0,1,11,21,23,24,27,21,18,22,22,23,15,5,8,4,2,1]}

shop_data =pd.DataFrame(data_shop)

shop_data.plot.line(x='Hour', y= 'Cases')
plt.xlabel('Hour')
plt.ylabel('Cases')
plt.title('Shoplifting Cases Per Hour on Washington St')


# In[593]:


# This chart, represneting all shoplifting in Boston, is similar to the data for shoplifting on Washington St
crime.query('OFFENSE_DESCRIPTION =="LARCENY SHOPLIFTING" & HOUR =="5"').count()

data_shopp={'Hour':['0','1','2','3','4','5','6','7','8','9','10','11', '12', '13', '14', '15','16', '17', '18', '19', '20', '21','22','23'],'Cases':[35,10,6,4,4,4,16,25,55,82,121,128,162,151,187,169,234,213,144,128,64,39,25,19]}

shopp_data =pd.DataFrame(data_shopp)

shopp_data.plot.line(x='Hour', y= 'Cases')
plt.xlabel('Hour')
plt.ylabel('Cases')
plt.title('Shoplifting Cases Per Hour in Boston')


# In[667]:


# Highest number of Invesitage Person cases in Boston took place on Washington St with 246

# Blue Hill Ave had 71 Invesitage Person cases and Tremont St had 64.

#street_one = crime.query('OFFENSE_DESCRIPTION == "INVESTIGATE PERSON" & STREET == "TREMONT ST"')
#street_one.count()

street_two = crime.query('OFFENSE_DESCRIPTION == "INVESTIGATE PERSON" & STREET == "WASHINGTON ST"')
street_two.count()


# In[405]:


# The most Investigate Persons cases on Washington St in a month occurred in September with 27

street_two = crime.query('OFFENSE_DESCRIPTION == "INVESTIGATE PERSON" & STREET == "WASHINGTON ST" & MONTH == "5"')
street_two.count()


# In[175]:


# Monday had the most Invesitage Person cases for Washington St in September with 8 and Sunday had the least amount with 0

street_three = crime.query('OFFENSE_DESCRIPTION == "INVESTIGATE PERSON" & STREET == "WASHINGTON ST" & MONTH == "9" & DAY_OF_WEEK =="Monday"')
street_three.count()


# In[431]:


# 29 shootings occurred on Washington St.

# 20 shootings occurred on Blue Hill Ave and 1 on Tremont St

#crime.query('SHOOTING == "1" & STREET == "HYDE PARK AVE"').count()
#crime.query('SHOOTING == "1" & STREET == "BLUE HILL AVE"').count()

crime.query('SHOOTING == "1" & STREET == "WASHINGTON ST"').count()


# In[604]:


# Investigate Property offenses had the most shootings on Washington St

crime.query('SHOOTING == "1" & STREET == "WASHINGTON ST" & OFFENSE_DESCRIPTION == "MURDER, NON-NEGLIGIENT MANSLAUGHTER"').count()

data_shot={'Offense':['Aggravated Assault', 'Investigate Property', 'Ballastics', 'Vandalism', 'ROBBERY', 'Murder Manslaughter' ],'Number of Shootings':[8,15,3,1,1,1]}

shooting_cases =pd.DataFrame(data_shot)

shooting_cases.plot.bar(x='Offense', y='Number of Shootings')
plt.xlabel('Offense')
plt.ylabel('Number of Shootings')
plt.title('Top Offenses on Washington St with Shootings')


# In[681]:


# The most Investigate Property offenses on Washington St occurred in Decemeber with 18, but only led to one shooting.

# September and October had the most Investigate Property Offenses on Washington with a shooting with a total of 3 shootings.

crime.query('STREET == "WASHINGTON ST" & OFFENSE_DESCRIPTION == "INVESTIGATE PROPERTY" & MONTH =="12"').count()

crime.query('STREET == "WASHINGTON ST" & OFFENSE_DESCRIPTION == "INVESTIGATE PROPERTY" & MONTH =="9" & SHOOTING =="1"').count()


# In[639]:


# The most aggravated assaults on Washington Ave happened in July and August with 14
crime.query('STREET == "WASHINGTON ST" & OFFENSE_DESCRIPTION == "ASSAULT - AGGRAVATED" & MONTH =="7"').count()


# #### 5) Additional Trends

# In[605]:


# Looks like there isnt a trend between Investigate Person cases and shootings
data_four={'Month':['Jan','Feb','March','April','May','June','July','Aug','Sept','Oct','Nov','Dec'],'Shootings':[46,58,62,72,109,142,140,126,127,95,84,61]}

shooting_data =pd.DataFrame(data_four)
           
print(shooting_data)

plt.figure(figsize=(8,5))
plt.title('Invesitage Person Cases vs Shootings')
plt.plot(iv_data.Month, iv_data.Investigate_Person_Cases, label='Investigate Person Cases')
plt.plot(shooting_data.Month, shooting_data.Shootings, label='Shootings')

plt.xticks(iv_data.Month[::3], rotation='vertical')
plt.xlabel('Month')
plt.ylabel('Number of Cases')

plt.legend()

plt.show


# In[682]:


# 34 shootings (out of 1122) took place during an Investigate Person offense
crime.query('SHOOTING == "1" & OFFENSE_DESCRIPTION == "INVESTIGATE PERSON"').count()


# In[411]:


# Can see shooting chart does not match overall offense count chart above
shooting_data.groupby('Month')['Shootings'].count().plot
plt.xticks(crime.MONTH[::3])
plt.xlabel('Month')
plt.ylabel('Count of Crimes')
plt.title('Count of Crimes Per Month')
plt.show


# In[607]:


# What about Aggravated Assault cases and Shootings?

# 21% of all shootings were a result of aggravated assault.

crime.query('SHOOTING == "1" & OFFENSE_DESCRIPTION == "ASSAULT - AGGRAVATED"').count()


# In[611]:


# 39% of all shootings were due to Investigate Property Offense

crime.query('SHOOTING == "1" & OFFENSE_DESCRIPTION == "INVESTIGATE PROPERTY"').count()


# #### Conclusions

# In[ ]:


# 1) What are the five most common offenses recorded and the least?
    
    # Most Common
    # Invesitage Person
    # Sick Assist
    # M/V - Leaving Scene - Property Damage
    # Vandalism
    # Investigate Property
    
    # Least Common
    # Justifiable Homicide
    # Prostitution - Assiting or Promoting
    # Evidence Tracker Incidents
    # Larceny Theft from Coin-Op Machine
    # Possession of Burglarious Tools

# 2) Are some days more dangerous than others? Months? Hours?

    # Friday has the most reported cases
    # The weekend has the least amount of reported cases
        # But the weekend has the most shootings
    
    # April had the least amount of cases reported (COVID?)
    # October had the most reported cases
        # August - October had the most reported cases as a whole
    
    # 0000 had the most most cases reported
    # 0400 had the least amount of cases reported
        # Offenses decreased after 0000 for the early morning
        # The offenses picked up again the afternoon before dropping again in the evening before 0000

# 3) Does the city experience a lot of shootings?

    # 1122 reported shootings (About 1.5% of all reported cases)
    # June had the most shootings, followed by July, August and September
    # January and February had the least amount of shootings
    
    # The most shootings occured on Saturday with a 180 total over the year
    # Shootings were more common on the weekend (Friday - Sunday) than during the week
    # 33 shootings occurred on a Saturday at 0000
    # Shootings and aggravated assasult and investigate property were common 

# 4) What is the most dangerous part of the city?
    
    # Washington St
    # 3276 offenses recorded
    # 29 shootings
        # 15 of those shootings were a result of Investigate Property offenses
    # 251 Shoplifting cases
        # No Shoplifting offenses led to a shooting
    # 246 Investigate Person Cases
        # No Investigate Person offenses led to a shooting
    # 141 Investigate Property Cases
        # 15 Shootings
    # 108 Aggravated Assault Cases
        # 8 Shootings
    # 127 Simple Assault Cases
        # No Simple Assault offenses led to a shooting
    # Most Investigate Person Cases recorded in September (On a a Monday)

# 5) Are there any trends?

    # Count of Investigate Person offenses per month was similar to the total count of all offenses per month
    # Assult- Simple Cases followed the same trend but robbery did not
    # Count of shootings did not follow the same progression as Investigate Person offenses or count of all offenses per month
        # Shootings streadily raised, peaked in the summer, before declining in the fall
    
    # Investigate Person cases remained about the same during the week but declined over the weekend.
    
    # Invetigate Property offenses led to the greatest amount of shootings (40%)
    
        
    # Safest time and place to be in Boston?
        # April, on a Sunday, at 0400, at Chester Park.
        # Summer and fall is dangerous, especially for shootings
        # Avoid Washington St
        # Do not shop on Washington St
        # Do not investigate someone's property on Washington St


# #### Notes

# In[ ]:


#crime[crime['OFFENSE_DESCRIPTION'] == 'INVESTIGATE PERSON'].groupby('DAY_OF_WEEK').sum()
#crime.sort_values(by=["STREET", "OFFENSE_DESCRIPTION"])[["STREET", "OFFENSE_DESCRIPTION"]]
# crime[crime['OFFENSE_DESCRIPITION'] == 'INVESTIGATE PERSON'].groupby('MONTH').agg(
    # Get max of the duration column for each group
    #max_offense=('', max),
    # Get min of the duration column for each group
   #min_duration=('duration', min),
    # Get sum of the duration column for each group
    #total_duration=('duration', sum),
    # Apply a lambda to date column
    #num_days=("date", lambda x: (max(x) - min(x)).days)    
#)

#daily_crime = crime.groupby(['MONTH', 'DAY_OF_WEEK', "HOUR"])['OFFENSE_DESCRIPTION'].count()
#print(daily_crime)
#crime.groupby('DAY_OF_WEEK').count()
#crime['OFFENSE_DESCRIPTION'].value_counts(max).head(10).sort_values().plot(kind='barh')
#plt.xlabel('Offenses Reported')
#plt.ylabel('Offense')
#plt.title('Top Reported Offenses')
#crime.groupby('DAY_OF_WEEK')['OFFENSE_DESCRIPTION'].count()

# Shootings peaked in June before declining
# The most crimes were committed in October
# The least amount of crims were committed in April, probably due to the onset of the COVID pandemic. 
# ALthough Shootings did not go down during the onset of the pandemic. 
# Number One Offense Description: Investigate Person
# Least common offense Description: Justifiable Homicide, PROSTITUTION - ASSISTING OR PROMOTING, Evidence Tracker Incidents, LARCENY THEFT FROM COIN-OP MACHINE 
# Washington St had the most reported cases with 3276.
# The next street with a high case load was BLUE HILL AVE 1277.
# Highest number of Invesitage Person cases took place on Washington St with 246.
# Most of the Investigate Persons cases on Washington St occurred in September with 27
# Monday had the most Invesitage Persons cases for Washington St in September with 8 and Sunday had the least amount with 0
# 1122 total shootings
# 29 shootings occurred on Washington St along with 27 Investigate Person cases. Are they related?

