import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import zipfile
import pandas as pd

with st.echo(code_location='below'):
    st.title("Приветствую! Это приложение показывает все полеты в августе 2018 года.")
    """
    Если вы боитесь летать или просто хотите посмотреть на статистику мировой авиации за 1 месяц, то Welcome :)
    """

    """
    В данном приложении можно посмотреть даннные отдельно по каждой из компаний (рейсы, задержки, аэропорты, города), также отдельно по дням и по аэропортам.
    """

    x = np.linspace(0, 10, 500)
    fig = plt.figure()
    plt.plot(x, np.sin(x))
    plt.ylim(-2, 2)
    st.pyplot(fig)

    """"
    Open:
    """
 #   z = zipfile.ZipFile('flights_aug_2018.zip', 'r')
 #   m = z.extract('flights_aug_2018.csv')


    st.markdown("Let's look at this fine dataset""")

 #   flights = pd.read_csv(m)
 #   flights.head(5)
#    st.dataframe(flights, 5)

    
    """
    Chek
    """