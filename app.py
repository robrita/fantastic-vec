import streamlit as st
import app.feedback as feedback
import time

st.set_page_config(
    page_title="ChatVec",
    page_icon="✨",
    layout="wide",
)

st.logo(
    "https://www.ibexlabs.com/wp-content/uploads/2024/06/64f1e436ba4f53a0a5943327_logo-xgen-1.png",
    link="https://www.google.com",
    icon_image="https://webassets.mongodb.com/_com_assets/cms/apigene_ai_logo-t8qr84bfj6.jpeg",
)

st.markdown(
    """
    <style>
    .block-container {
        padding-top: 3rem;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Initialize session states
if "toast_counter" not in st.session_state:
    st.session_state.toast_counter = 0
if "style" not in st.session_state:
    st.session_state.style = ""
if "styleName" not in st.session_state:
    st.session_state.styleName = ""
if "guidelines" not in st.session_state:
    st.session_state.guidelines = ""
if "example" not in st.session_state:
    st.session_state.example = ""
if "exampleText" not in st.session_state:
    st.session_state.exampleText = ""
if "locals" not in st.session_state:
    st.session_state.locals = {}

# increment the counter
st.session_state.toast_counter += 1

# Show the toast if the counter is a prime number
if st.session_state.toast_counter % 7 == 0:
    icons = ["🎉", "✨", "🚀", "🌟", "🎊", "🥳", "🎈", "🎆", "🎇", "🏆", "🥇"]
    st.toast("[Rob] happy to be part of this community..", icon=icons[st.session_state.toast_counter % len(icons)])

# Login handling
if not st.experimental_user.is_logged_in:
    st.markdown("""
        <style>
        [data-testid="stVerticalBlock"] > [data-testid="stHorizontalBlock"] > div:nth-child(2) {
            background: rgba(255, 255, 255, 0.5);
            padding: 2rem;
            border-radius: 8px;
        }
        .stApp {
            background-image: url("https://i.makeagif.com/media/10-24-2017/fiozwR.gif");
            background-size: cover;
        }
        </style>
    """, unsafe_allow_html=True)
    
    _, col_login, _ = st.columns([1, 1, 1])
    with col_login:
        st.markdown("<h1 style='color: #ffffff; text-align: center;'>ChatVec</h1>", unsafe_allow_html=True)
        st.markdown("""
            <div style='text-align: center;'>
                <h2 style='color: #000000; margin-bottom: 0.75rem; font-size: 1.8rem;'>✨Chat with your data</h2>
                <p style='font-size: 1rem; margin-bottom: 2rem;'>Please log in to continue using the application</p>
            </div>
        """, unsafe_allow_html=True)
        
        if st.button("Login with Google", type="primary", use_container_width=True):
            st.balloons()
            time.sleep(1.2)
            st.login()

    # Show feedback carousel
    feedback.show_feedback_carousel()
    st.stop()

# Show welcome message and logout button when logged in
st.markdown(f"""
    <div style="background-color: #f0f2f6; padding: 1rem; border-radius: 0.5rem;">
        <p style="color: #333333; text-align: center; margin: 0;">📢AI News: {st.experimental_user.name}!</p>
    </div>
""", unsafe_allow_html=True)

with st.sidebar:
    if st.button("Log out", type="secondary"):
        st.snow()
        time.sleep(3)
        st.logout()

pages = {
    "Resources": [
        st.Page("page/ingest.py", title="Ingest Data", icon="📥"),
        st.Page("page/playground.py", title="Playground", icon="🏃‍♂️"),
        st.Page("page/apis.py", title="API", icon="🌐"),
    ],
    "Account": [
        st.Page("page/account.py", title="Create your account", icon="⚙️"),
    ],
}

pg = st.navigation(pages)
pg.run()
