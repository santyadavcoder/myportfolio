import streamlit as st
from streamlit_option_menu import option_menu
import requests
from streamlit_lottie import st_lottie

st.set_page_config(layout="wide")
def link_css(style_path):
    """
    Function to link an external CSS file in Streamlit.

    Parameters:
        style_path (str): The path to the external CSS file.

    Example:
        link_css("path/to/your/style.css")
    """
    link_tag = f'<link rel="stylesheet" href="{style_path}">'
    st.markdown(link_tag, unsafe_allow_html=True)

# Path to your external CSS file
css_path = "/Users/apple/portfolio/style.css"

# Link the CSS file using the function
link_css(css_path)



def lottie_coder(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie = lottie_coder("https://lottie.host/89af09ee-b7cd-4a6d-8281-03824ad8a597/7h37NiBJV6.json")
lottie_contact = lottie_coder("https://lottie.host/d3d201f8-2d18-4e02-bf64-78d81a8f4ac8/DJYnCa3nqc.json")

st.title("hey👋 Everyone")
st.write("###")
st.subheader("I am sant🫶🏻")
st.write("""
 a web developer 
🤍
""")
st.markdown("[my instagram](https://www.instagram.com/santoshyadav1758/)")
st.write("____")

with st.container():
    selected = option_menu(
        menu_title=None,
        options=['about', 'projects', 'contact'],
        icons=['person', 'code-slash', 'chat-left-text-fill'],
        orientation="horizontal",
    )

    if selected == "about":
        with st.container():
            coll, coll2 = st.columns(2)
            with coll:
                st.write("###")
                st.subheader("A pyhtonist")
                st.title("A Software developer")
            with coll2:
                st_lottie(lottie)
        with st.container():
            col3, col4 = st.columns(2)
        with col3:
            st.subheader("""
                       EDUCATION
                       - TIT
                            - Graduation B-TECH AIMl
                            - Grade:xyz
                       - school 
                            - Ram s.s.m.s.o.r.m.p.
                            - grade: xyz       
                                  """)
            with col4:
                st.subheader("""
                          - domain 
                            - software developer 
                            - web developer 
                            - python expert 
                                       
                                      """)

    elif selected == "projects":
        with st.container():
            st.header("My projects")
            st.write("##")
            
            st.markdown("[tastetak](https://tastetak.in/)")
            st.write("""A online food website in my city  that i start in my 1st year of collage
                     """)
            st.markdown("[Visit GitHub](https://github.com/santyadavcoder/loginpage.html-css)")
            

    elif selected == "contact":
        st.title("Get In Touch 💌")
        st.write("##")
        st.write("##")

        contact_form = """
       
            <form action="https://formsubmit.co/santoshyadavsantsohyadav@gmail.com"method="POST">
            <input type="text" name="name" placeholder="Your name" required> 
            <br>
            <input type="email" name="email" placeholder="Your email" required>
            <br>
            <textarea name="your message" placeholder="Type here"></textarea>
            <br>
            <button type="submit"> Send </button>
            <style>
        /* Add your local CSS styles here */
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            padding: 20px;
        }

        form {
            max-width: 400px;
            margin: 0 auto;
            background-color: #fff;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }

        input, textarea, button {
            width: 100%;
            padding: 10px;
            margin-bottom: 10px;
            border: 1px solid #ccc;
            border-radius: 4px;
            box-sizing: border-box;
        }

        button {
            background-color: #4CAF50;
            color: white;
            cursor: pointer;
        }
    </style>
            </form>
        """

        left_coll, rightcoll = st.columns((2, 1))
        with left_coll:
            st.markdown(contact_form, unsafe_allow_html=True)
        with rightcoll:
            st_lottie(lottie_contact, height=500,width=600,)
