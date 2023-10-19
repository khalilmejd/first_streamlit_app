import streamlit
import pandas
import requests
import snowflake.connector

fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)

#New Section to disply fruityvice api response
streamlit.header("Fruityvice Fruit Advice!")

# Set the title of the app
streamlit.title('My Parents New Healthy Diner')

# Create a header for the breakfast menu
streamlit.header('Breakfasr Menu')

# List the breakfast menu items
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale,Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')

# Create a header for the build your own fruit smoothie section
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

# Read the fruit macros data into a Pandas DataFrame
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

# Set the index of the DataFrame to the 'Fruit' column
my_fruit_list = my_fruit_list.set_index('Fruit')

# Create a multiselect widget so users can pick the fruits they want to include in their smoothie
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado', 'Strawberries'])

# Get the DataFrame of the fruits the user selected
fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display the DataFrame of the fruits the user selected
streamlit.dataframe(fruits_to_show)

# Make a request to the FruityVice API for information about the watermelon fruit
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")

# Display the response from the FruityVice API
streamlit.text(fruityvice_response)

# write your own comment -what does the next line do? 
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# write your own comment - what does this do?
streamlit.dataframe(fruityvice_normalized)

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * from fruit_load_list")
my_data_row = my_cur.fetchone()
streamlit.text("The fruit load list contains:")
streamlit.text(my_data_row)

