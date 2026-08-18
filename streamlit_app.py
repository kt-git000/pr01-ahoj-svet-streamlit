import streamlit as st
import pandas as pd 
import plotly.express as px

st.title(" My new app")
st.write(
    "Tojo je moja prva aplikacia v Streamlite"
)

data = pd.DataFrame({
    "Kategorie" : ["A","B","C","D"],
    "Hodnoty" : [1,2,3,4]
})

st.write("Tabulka s datami: ")
st.dataframe(data)

fig = px.bar(data,
            x="Kategorie",
            y="Hodnoty",
            title="Stlpcovy graf plotly"
)
st.plotly_chart(fig)

if st.button("informacne okno"):
    st.info("Toto je informacne okno")

if st.button("upozornovacie okno"):
    st.warning("Toto je upozornovacie okno")

if st.button("chybove okno"):
    st.error("Toto je chybove okno")

user_input = st.text_input("Ako sa volas: ")
st.write(f"Volas sa {user_input}")

edited_data = st.data_editor(data, num_rows="dynamic", use_container_width=True)

st.write("Upravena nova tablulka")
st.dataframe(edited_data)

st.write("Stlpcovy graf: ")
fig_bar = px.bar(
    edited_data, x="Kategorie",
    y = "Hodnoty",
    title =  "Upraveny Stlpcovy graf plotly"
)

st.plotly_chart(fig_bar)

st.write("Kolacovy graf: ")
fig_pie = px.pie(
    edited_data, names="Kategorie",
    values = "Hodnoty",
    title =  "Upraveny Kolacovy graf plotly"
)

st.plotly_chart(fig_pie)