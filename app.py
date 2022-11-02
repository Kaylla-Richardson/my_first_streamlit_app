import streamlit as st
import random
import altair as alt
import numpy as np
import pandas as pd

st.header('Homework 1')

st.markdown(
"**QUESTION 1**: In previous homeworks you created dataframes from random numbers.\n"
"Create a dataframe where the x axis limit is 100 and the y values are random values.\n"
"Print the dataframe you create and use the following code block to help get you started"
)

x_limit = 100

# List of values from 0 to 100 each value being 1 greater than the last
x_axis = np.arange(0,x_limit,1)

# Create a random array of data that we will use for our y values
y_data = np.random.rand(100)

df = pd.DataFrame({'x': x_axis,
                     'y': y_data})
st.write(df)

st.markdown(
"**QUESTION 2**: Using the dataframe you just created, create a basic scatterplot and Print it.\n"
"Use the following code block to help get you started."
)

df = pd.DataFrame({'x': x_axis,
                     'y': y_data})

scatter = alt.Chart(df).mark_point().encode(
    x ='x',
    y = 'y'
)

st.altair_chart(scatter, use_container_width=True)


st.markdown(
"**QUESTION 3**: Lets make some edits to the chart by reading the documentation on Altair.\n"
"https://docs.streamlit.io/library/api-reference/charts/st.altair_chart.  "
"Make 5 changes to the graph, document the 5 changes you made using st.markdown(), and print the new scatterplot.  \n"
"To make the bullet points and learn more about st.markdown() refer to the following discussion.\n"
"https://discuss.streamlit.io/t/how-to-indent-bullet-point-list-items/28594/3"
)

df_annotate = pd.DataFrame({'x': x_axis,
                     'y': y_data})

scatter = alt.Chart(df_annotate, title="My new chart title").mark_circle(color = 'pink', opacity = 1, size = 100).encode(
    alt.X('x', title="My new x-axis title"),
    alt.Y('y', title="My new y=axis title"),
    tooltip = ['x','y']
) .interactive()

st.altair_chart(scatter, use_container_width=True)


st.markdown("""
The 5 changes I made were:
- Change 1: Changed the the points to filled in circles on scatter plot
- Change 2: Changed color of circles to pink
- Change 3: Increased the size of the circles on scatter plot
- Change 4: Hover feauture where can see circle value
- Change 5: Can interact with scatter plot: move it around and zoom in and out
""")



st.markdown(
"**QUESTION 4**: Explore on your own!  Go visit https://altair-viz.github.io/gallery/index.html.\n "
"Pick a random visual, make two visual changes to it, document those changes, and plot the visual.  \n"
"You may need to pip install in our terminal for example pip install vega_datasets "
)
from vega_datasets import data

st.markdown(
"**QUESTION 4 ANSWER**: From HW Review Video."
)

source = pd.read_json('imdb.json')
st.write(source)

bar = alt.Chart(source).mark_bar(color='#e094b6').encode(
    alt.X("IMDB_Rating:Q", bin=True, title="IMDB Rating"),
    alt.Y('count()', title="Records")
)


st.altair_chart(bar, use_container_width=True)

st.markdown(
"**QUESTION 4 ANSWER**: What I personally did for question 4."
)

source = data.us_employment()

negative = alt.Chart(source).mark_bar(
    cornerRadiusTopLeft=3,
    cornerRadiusTopRight=3,
    cornerRadiusBottomRight=3,
    cornerRadiusBottomLeft=3,
).encode(
    x="month:T",
    y="nonfarm_change:Q",
    color=alt.condition(
        alt.datum.nonfarm_change > 0,
        alt.value("pink"),  # The positive color
        alt.value("lightskyblue")  # The negative color
    )
).properties(width=600) 

st.altair_chart(negative, use_container_width=True)


st.markdown("""
The 2 changes I made were:
- Change 1: I changed the colors
- Change 2: I gave the bars rounded edges
"""
)

