#Maja Kubara Computationa social science
import pandas as pd
import plotly.express as px
import os

AOS_Data = pd.read_csv("static\AOSdata.csv")

#keep only state and technology columns
AOS_Data = AOS_Data[["State", "Technology"]]

#Drop Non-values and duplicates
AOS_Data.dropna()
AOS_Data.drop_duplicates()

#count used technology per state
#turn series to dataframe and reset index
#change column name
AOS_counted = AOS_Data.value_counts().to_frame().reset_index()
AOS_counted.rename(columns={0:"Count"}, inplace = True)

#change state codes to names
#create dataframe of state codes
state_codes = pd.read_html("https://knowledgecenter.zuora.com/Quick_References/Country%2C_State%2C_and_Province_Codes/B_State_Names_and_2-Digit_Codes", skiprows=1)
state_codes = state_codes[0]

#create column names
state_codes.columns = ["State", "State_full"]

#merge dataframes
inner = pd.merge(AOS_counted, state_codes)

#get rid of State column
inner.pop("State")

# rename column
inner.rename(columns = {"State_full":"State"}, inplace = True)

#create csv 
inner.to_csv("static/AOS_for_map.csv")

#create an interactive plot with technology count used per state
#save it to html
fig = px.bar(AOS_counted, x="State", y="Count", color="Technology", title="Surveillance technology tools used by law enforcement agencies per each state")
fig.update_layout({
    'plot_bgcolor': '#000000',
    'paper_bgcolor': '#000000',},
    font=dict(
        family="montserrat",
        size=14,  # Set the font size
        color="#FFFFFF"))
fig.write_html('static/stacked-bar-plot.html',  include_plotlyjs="cdn")




       



