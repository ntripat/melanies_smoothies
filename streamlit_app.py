# Import python packages
import streamlit as st
from snowflake.snowpark.context import get_active_session

# Write directly to the app
st.title(f"Customize Your Smoothies :balloon:")
st.write(
  """Replace this example with your own code!
  **And if you're new to Streamlit,** check
  out our easy-to-follow guides at
  [docs.streamlit.io](https://docs.streamlit.io).
  """
)


import streamlit as st

option = st.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone"),
)
st.write("You selected:", option)


option = st.selectbox(
    "What is your favorite Fruit?",
    ("Banana", "Strawberries", "Peaches"),
)
st.write("Your favorite Fruit is : ", option)




session = get_active_session()
my_dataframe = session.table("smoothies.public.fruit_options")
st.dataframe(data=my_dataframe, use_container_width=True)

#================================================================================
# Lesson2:
#================================================================================
# Write directly to the app
st.title(":cup_with_straw: Customize Your Smoothies! :cup_with_straw:")
st.write(
  """Choose the fruits you want in your custom Smoothies!
  """)
from snowflake.snowpark.functions import col

import streamlit as st

#title = st.text_input("Movie title", "Life of Brian")
#st.write("The current movie title is", title)

session = get_active_session()
my_dataframe = session.table("smoothies.public.fruit_options").select(col('Fruit_Name'))
#st.dataframe(data=my_dataframe, use_container_width=True)

name_on_order = st.text_input("Name on Smoothie")
st.write("The name on your Smoothie will be:", name_on_order)

ingredients_list = st.multiselect(
    'Choose up to 5 ingredients: ',
    my_dataframe,max_selections=3
    )
if ingredients_list:
    #st.write(ingredients_list)
    #st.text(ingredients_list)
    
    ingredients_string = ''
    for fruit_choosen in ingredients_list:
        ingredients_string += fruit_choosen + ' '
    #st.write(ingredients_string)


    my_insert_stmt = """ insert into smoothies.public.orders(ingredients,name_on_order)
            values ('""" + ingredients_string + """','"""+ name_on_order + """')"""
    #st.write(my_insert_stmt)

    #if ingredients_string:
        #session.sql(my_insert_stmt).collect()
        #st.success('Your Smoothie is ordered!', icon="✅")
    time_to_insert = st.button('Submit Order')
    if time_to_insert:
        session.sql(my_insert_stmt).collect()
        st.success('Your Smoothie is ordered!', icon="✅")


#================================================================================
if ingredients_list:
    #st.write(ingredients_list)
    #st.text(ingredients_list)
    
    ingredients_string = ''
    for fruit_choosen in ingredients_list:
        ingredients_string += fruit_choosen + ' '

    

    my_insert_stmt = """ insert into smoothies.public.orders(ingredients,name_on_order)
            values ('""" + ingredients_string + """','"""+ name_on_order + """')"""
    st.write(my_insert_stmt)
    st.stop()







 
