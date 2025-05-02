import streamlit as st
from streamlit_chat import message

# Set page configuration
st.set_page_config(page_title="CEDRA – Empowering Women", layout="centered")

# Simple user store (in-memory)
if "users" not in st.session_state:
    st.session_state.users = {"admin": "cedra2025"}  # default admin user

# --- Authentication Gate ---
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    st.title("Welcome to CEDRA")
    st.subheader("Login or Create an Account")

    tab1, tab2 = st.tabs(["Login", "Create Account"])

    with tab1:
        username = st.text_input("Username", key="login_username")
        password = st.text_input("Password", type="password", key="login_password")
        login = st.button("Login")
        forgot = st.checkbox("Forgot password?")

        if forgot:
            st.info("Please contact admin@cedra.org to reset your password.")

        if login:
            if username in st.session_state.users and st.session_state.users[username] == password:
                st.session_state.logged_in = True
                st.success("Login successful! Welcome, {}.".format(username))
                st.rerun()
            else:
                st.error("Invalid username or password.")

    with tab2:
        new_username = st.text_input("New Username", key="create_username")
        new_password = st.text_input("New Password", type="password", key="create_password")
        confirm = st.button("Create Account")

        if confirm:
            if new_username in st.session_state.users:
                st.error("Username already exists. Please choose a different one.")
            else:
                st.session_state.users[new_username] = new_password
                st.success("Account created successfully! Please log in using the Login tab.")

else:
    # --- Sidebar Navigation ---
    st.sidebar.title("Navigation")
    selected_page = st.sidebar.radio("Choose a page:", ["Home", "Donate"])

    if selected_page == "Donate":
        st.title("Support CEDRA with a Donation")
        st.markdown("""
        Every contribution helps us empower more women through education, technology, and mentorship.

        To donate, please use the secure payment link below:
        """)
        st.markdown("[Donate via Stripe](https://buy.stripe.com/test_eVa6qD3Nv2d8eWk28b) 💳")
        st.stop()

    # --- HOME PAGE ---
    if True:
        st.title("Welcome to CEDRA 🎓")
        st.subheader("Center for Educational Research/Recreational Activities")
        st.caption("A modern platform to support the economic empowerment of underprivileged women.")

        st.markdown("## Introduction")
        st.markdown("""
        CEDRA (Center for Educational Development and Research for Advancement) is a nonprofit 
        organization committed to empowering underprivileged women by providing them with access 
        to education, digital tools, mentorship, and community support. Our digital platform serves 
        as a central hub for donations, volunteering, and awareness, making it easier for supporters 
        and partners to engage with our mission and drive real impact.
        """)

    # --- FLOATING CHATBOT ---
    from streamlit.components.v1 import html

    if "show_chat" not in st.session_state:
        st.session_state.show_chat = False

    st.markdown("""
    <style>
.chat-toggle {
    position: fixed;
    bottom: 20px;
    right: 20px;
    background-color: #f1f1f1;
    border-radius: 50px;
    padding: 12px 18px;
    font-size: 16px;
    font-weight: bold;
    box-shadow: 0 4px 8px rgba(0,0,0,0.2);
    cursor: pointer;
    z-index: 9999;
}
</style>
    <button class="chat-toggle" onclick="window.location.reload()">💬 Chat</button>
    """, unsafe_allow_html=True)

    if st.button("💬 Chat with CEDRA Bot"):
        st.session_state.show_chat = not st.session_state.show_chat

    if st.session_state.show_chat:
        st.markdown("### CEDRA AI Chatbot")
        st.write("Ask me anything about our mission, programs, or how to get involved!")

        if "messages" not in st.session_state:
            st.session_state.messages = []

        user_input = st.text_input("You:", "")

        if user_input:
            st.session_state.messages.append(("user", user_input))

            import openai
            openai.api_key = st.secrets["OPENAI_API_KEY"]

            try:
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": "You are a helpful assistant for CEDRA, a non-profit supporting women's empowerment."},
                        {"role": "user", "content": user_input}
                    ]
                )
                bot_response = response.choices[0].message.content.strip()
            except Exception as e:
                bot_response = f"Sorry, I couldn't process your question. ({e})"

            st.session_state.messages.append(("bot", bot_response))

        for sender, text in st.session_state.messages:
            message(text, is_user=(sender == "user"))
