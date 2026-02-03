# -*- coding: utf-8 -*-
"""
Created on Fri Jan 30 23:38:47 2026

@author: GIVEN
"""
import streamlit as st
import pandas as pd


# Sidebar
menu_title = st.sidebar.title("Navigation")

menu = st.sidebar.radio("Go to:",
                   ["My Profile","Proposal","Activity","Contact"])

Assistant_data = pd.DataFrame({"Program":
                               ["Supplemental Instruction",
                                "Mathematics and Applied Mathematics",
                                "Residence"], 
                               "Duration":
                                   ["3 years","2 years","10 months"],
                               "Description":
   ["A peer-led academic support program where senior students\n help others understand challenging modules",
   "An academic discipline focused on mathematical theory",
   "A student leadership role responsible for representing\n residents and maintaining order"],
                              
                               })
    
Volunteer_data = pd.DataFrame({"Program":
                               ["Eskom-Expo", "Farming Profiling"],
                               "Duration":
                                   ["3 years", "9 months"],  
                               "Description":
    ["A national science and engineering competition that encourages learners to develop and showcase innovative research projects",
    "An initiative focused on improving agricultural productivity and livelihoods through sustainable farming"],
                                      
                                }) 
    
    
    
if menu == "My Profile":
    
    first_name = "Rethabile Given"
    last_name = "Sitole"
    level = "Honours"
    varsity = "University of Limpopo"
    
    st.title("Welcome to My Research Page")
    year = st.slider("Choose current year:",2015,2030)
    st.header(f"Author: {first_name} {last_name}")
    st.write(f"Study level: {level}")
    st.write(f"Institution: {varsity}")
    
    st.image("https://media.cheggcdn.com/media/f28/f28ee272-8a24-4715-8db3-8b80b269e720/phpwpcYUu")
    st.write(f"Page was opened in {year}")

    
elif menu == "Proposal":
    
    file = st.file_uploader("choose file.csv",type="csv")
    
    if file:
        st.write("Your file")
        proposal_file = pd.read_csv(file)
        st.dataframe(proposal_file)
    else:
        st.write("No file uploaded")
        
        

elif menu == "Activity":
    
    st.sidebar.title("Activities")
    st.sidebar.write("Activity options")
    
    activities = st.sidebar.selectbox("Choose Options",
                                       ["Mentoring", "Volunteering"]
                                       )
        
    if activities == "Mentoring":
        st.title("Mentoring Activities")
        st.dataframe(Assistant_data)
        st.image("https://www.the-rheumatologist.org/wp-content/uploads/2020/02/mentoringgraphic.jpg")
        
    elif activities == "Volunteering":
        st.title("Volunteering Activities")
        st.dataframe(Volunteer_data)
        st.image("https://www.greenqueen.com.hk/wp-content/uploads/2020/12/Veganic-Farming.png")
        
    else:
        st.write("404")
        
    
elif menu == "Contact":
    
    email = "sitolerethabile@gmail.com"
    st.write(f"Email: {email}")
    st.write("Goodbye")
    st.image("https://img.freepik.com/premium-photo/view-professional-handshake-business-people_23-2150917018.jpg")
    
    

    

