import streamlit as st
import pandas as pd
import datetime
from PIL import Image
import base64
from io import BytesIO

# Set page configuration
st.set_page_config(
    page_title="CEDRA - Center for Educational Research/Recreational Activities",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
    <style>
    .main {
        background-color: white;
    }
    .stApp {
        font-family: 'Inter', sans-serif;
    }
    h1, h2, h3, h4, h5, h6 {
        font-weight: bold;
    }
    .primary-color {
        color: #FF5733;
    }
    .footer {
        position: fixed;
        bottom: 0;
        width: 100%;
        background-color: #1E1E1E;
        color: white;
        text-align: center;
        padding: 10px;
        font-size: 14px;
    }
    .card {
        background-color: white;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        padding: 20px;
        margin-bottom: 20px;
    }
    .hero-text {
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        color: white;
        text-align: center;
        z-index: 10;
        width: 80%;
    }
    .hero-overlay {
        background-color: rgba(0,0,0,0.5);
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
    }
    .stButton button {
        background-color: #FF5733;
        color: white;
        font-weight: bold;
        border-radius: 8px;
        padding: 10px 24px;
        border: none;
    }
    .stButton button:hover {
        background-color: #E64A2E;
    }
    .white-button button {
        background-color: white;
        color: #FF5733;
    }
    .icon-card {
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

# Function to create hero section
def hero_section(title, subtitle, img_path="hero-bg.jpg", height=500):
    col1, col2, col3 = st.columns([1, 10, 1])
    with col2:
        st.markdown(f"""
        <div style="position: relative; height: {height}px; margin-bottom: 2rem;">
            <img src="https://source.unsplash.com/random/1200x{height}/?women,education" 
                style="width: 100%; height: 100%; object-fit: cover; border-radius: 10px;" />
            <div class="hero-overlay" style="border-radius: 10px;"></div>
            <div class="hero-text">
                <h1 style="font-size: 3rem;">{title}</h1>
                <p style="font-size: 1.5rem; margin-top: 1rem;">{subtitle}</p>
            </div>
        </div>
        """, unsafe_allow_html=True)

# Create a navigation component
def navigation():
    st.sidebar.title("CEDRA")
    st.sidebar.markdown("---")
    
    menu = ["Home", "About", "Programs", "Donate", "Volunteer", "Contact", "Chatbot"]
    choice = st.sidebar.radio("Navigation", menu)
    
    st.sidebar.markdown("---")
    st.sidebar.info("Center for Educational Research/Recreational Activities")
    
    return choice

# Home page
def home():
    hero_section(
        "Empowering Women Through Education",
        "Join us in creating opportunities for underprivileged women to achieve economic independence"
    )
    
    # Buttons
    col1, col2 = st.columns(2)
    with col1:
        st.button("Donate Now", use_container_width=True)
    with col2:
        st.markdown('<div class="white-button">', unsafe_allow_html=True)
        st.button("Volunteer", use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Mission Section
    st.markdown("## Our Mission")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown('<div class="card icon-card">', unsafe_allow_html=True)
        st.markdown("### 🤝 Economic Empowerment")
        st.write("Providing women with the skills and resources they need to achieve financial independence.")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="card icon-card">', unsafe_allow_html=True)
        st.markdown("### 🎓 Education")
        st.write("Offering quality education and vocational training programs tailored to women's needs.")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col3:
        st.markdown('<div class="card icon-card">', unsafe_allow_html=True)
        st.markdown("### 👥 Community Building")
        st.write("Creating a supportive network where women can share experiences and grow together.")
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Impact Section
    st.markdown("## Our Impact")
    col1, col2 = st.columns([3, 2])
    
    with col1:
        st.markdown("### Transforming Lives")
        st.write("""
        Through our programs, we've helped thousands of women gain new skills, start businesses,
        and improve their economic status. Our success stories are a testament to the power of
        education and community support.
        """)
        st.markdown("[Read Success Stories →](https://example.com)")
    
    with col2:
        st.image("https://source.unsplash.com/random/600x400/?women,training", use_column_width=True)
    
    # Call to Action
    st.markdown('<div style="background-color: #FF5733; padding: 2rem; border-radius: 10px; color: white; text-align: center; margin-top: 2rem;">', unsafe_allow_html=True)
    st.markdown("## Join Our Mission")
    st.write("""
    Your support can make a difference in the lives of underprivileged women.
    Whether through donations, volunteering, or spreading awareness, you can help
    us create lasting change.
    """)
    st.button("Get Involved", use_container_width=False)
    st.markdown('</div>', unsafe_allow_html=True)

# About page
def about():
    hero_section(
        "About CEDRA",
        "Empowering women through education and economic opportunities",
        height=300
    )
    
    # Our Story Section
    st.markdown("## Our Story")
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.write("""
        CEDRA was founded in 2010 with a vision to create sustainable change in the lives of
        underprivileged women. What started as a small initiative has grown into a movement
        that has impacted thousands of lives across multiple communities.
        
        Our journey has been marked by countless success stories of women who have transformed
        their lives through education, skill development, and economic empowerment.
        """)
    
    with col2:
        st.image("https://source.unsplash.com/random/600x400/?women,community", use_column_width=True)
    
    # Values Section
    st.markdown("## Our Values")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown('<div class="card icon-card">', unsafe_allow_html=True)
        st.markdown("### 🎯 Empowerment")
        st.write("We believe in empowering women with the knowledge, skills, and resources they need to achieve their full potential.")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="card icon-card">', unsafe_allow_html=True)
        st.markdown("### 👥 Inclusivity")
        st.write("We are committed to creating an inclusive environment where every woman feels valued and supported.")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col3:
        st.markdown('<div class="card icon-card">', unsafe_allow_html=True)
        st.markdown("### 🤝 Partnership")
        st.write("We work in partnership with communities, organizations, and individuals to create lasting change.")
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Team Section
    st.markdown("## Our Team")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown('<div class="card" style="text-align: center;">', unsafe_allow_html=True)
        st.image("https://randomuser.me/api/portraits/women/1.jpg", width=150)
        st.markdown("### Maria Johnson")
        st.write("Executive Director")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="card" style="text-align: center;">', unsafe_allow_html=True)
        st.image("https://randomuser.me/api/portraits/men/1.jpg", width=150)
        st.markdown("### James Wilson")
        st.write("Operations Manager")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col3:
        st.markdown('<div class="card" style="text-align: center;">', unsafe_allow_html=True)
        st.image("https://randomuser.me/api/portraits/women/2.jpg", width=150)
        st.markdown("### Sarah Ahmed")
        st.write("Program Director")
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Board Members Section
    st.markdown("## Board Members")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown('<div class="card" style="text-align: center;">', unsafe_allow_html=True)
        st.image("https://randomuser.me/api/portraits/women/3.jpg", width=150)
        st.markdown("### Jane Doe")
        st.write("Chairperson")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="card" style="text-align: center;">', unsafe_allow_html=True)
        st.image("https://randomuser.me/api/portraits/men/3.jpg", width=150)
        st.markdown("### John Smith")
        st.write("Treasurer")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col3:
        st.markdown('<div class="card" style="text-align: center;">', unsafe_allow_html=True)
        st.image("https://randomuser.me/api/portraits/women/4.jpg", width=150)
        st.markdown("### Priya Patel")
        st.write("Secretary")
        st.markdown('</div>', unsafe_allow_html=True)

# Programs page
def programs():
    hero_section(
        "Our Programs",
        "Comprehensive programs designed to empower women at every stage",
        height=300
    )
    
    st.markdown("## Current Programs")
    
    # Program cards
    programs_data = [
        {
            "title": "Skills Development Workshop",
            "description": "Weekly vocational training in tailoring, handicrafts, and computer skills.",
            "image": "https://source.unsplash.com/random/300x200/?workshop",
            "duration": "12 weeks",
            "frequency": "Weekly sessions"
        },
        {
            "title": "Financial Literacy Program",
            "description": "Teaching basic accounting, budgeting, and business planning for entrepreneurs.",
            "image": "https://source.unsplash.com/random/300x200/?finance",
            "duration": "8 weeks",
            "frequency": "Bi-weekly sessions"
        },
        {
            "title": "Microfinance Initiative",
            "description": "Providing small loans to start businesses with mentorship support.",
            "image": "https://source.unsplash.com/random/300x200/?business",
            "duration": "Ongoing",
            "frequency": "Monthly follow-ups"
        }
    ]
    
    for i in range(0, len(programs_data), 2):
        cols = st.columns(2)
        for j in range(2):
            if i + j < len(programs_data):
                program = programs_data[i + j]
                with cols[j]:
                    st.markdown('<div class="card">', unsafe_allow_html=True)
                    st.image(program["image"], use_column_width=True)
                    st.markdown(f"### {program['title']}")
                    st.write(program["description"])
                    st.markdown(f"**Duration:** {program['duration']}  \n**Frequency:** {program['frequency']}")
                    st.button(f"Enroll in {program['title']}", key=f"enroll_{i}_{j}")
                    st.markdown('</div>', unsafe_allow_html=True)
    
    # Success stories
    st.markdown("## Success Stories")
    st.write("Read about women whose lives have been transformed through our programs.")
    
    success_stories = [
        {
            "name": "Meena",
            "story": "Started a tailoring business after completing our Skills Development Workshop.",
            "image": "https://randomuser.me/api/portraits/women/65.jpg"
        },
        {
            "name": "Lakshmi",
            "story": "Opened a small grocery store with help from our Microfinance Initiative.",
            "image": "https://randomuser.me/api/portraits/women/70.jpg"
        }
    ]
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.image(success_stories[0]["image"], width=100)
        st.markdown(f"### {success_stories[0]['name']}'s Story")
        st.write(success_stories[0]["story"])
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.image(success_stories[1]["image"], width=100)
        st.markdown(f"### {success_stories[1]['name']}'s Story")
        st.write(success_stories[1]["story"])
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Program calendar
    st.markdown("## Upcoming Program Schedule")
    
    # Create sample calendar data
    today = datetime.date.today()
    calendar_data = []
    
    for i in range(10):
        event_date = today + datetime.timedelta(days=i*3)
        calendar_data.append({
            "Date": event_date,
            "Program": programs_data[i % len(programs_data)]["title"],
            "Location": "CEDRA Center" if i % 2 == 0 else "Community Hall",
            "Time": "10:00 AM" if i % 2 == 0 else "2:00 PM"
        })
    
    calendar_df = pd.DataFrame(calendar_data)
    st.dataframe(calendar_df, use_container_width=True)

# Donate page
def donate():
    hero_section(
        "Make a Difference",
        "Your donation helps empower women through education and economic opportunities",
        height=300
    )
    
    col1, col2 = st.columns([3, 2])
    
    with col1:
        st.markdown("## Donation Form")
        
        donation_amount = st.number_input("Donation Amount ($)", min_value=5, value=50)
        
        st.markdown("### Personal Information")
        col_a, col_b = st.columns(2)
        with col_a:
            first_name = st.text_input("First Name")
        with col_b:
            last_name = st.text_input("Last Name")
        
        email = st.text_input("Email Address")
        
        st.markdown("### Payment Information")
        payment_method = st.radio("Payment Method", ["Credit Card", "PayPal", "Bank Transfer"])
        
        if payment_method == "Credit Card":
            col_c, col_d = st.columns(2)
            with col_c:
                card_number = st.text_input("Card Number")
            with col_d:
                expiry = st.text_input("Expiry (MM/YY)")
            
            col_e, col_f = st.columns(2)
            with col_e:
                cvv = st.text_input("CVV", type="password")
            with col_f:
                name_on_card = st.text_input("Name on Card")
        
        recurring = st.checkbox("Make this a monthly recurring donation")
        
        if st.button("Donate Now", use_container_width=True):
            st.success("Thank you for your donation! Your payment was successful.")
    
    with col2:
        st.markdown("## Your Impact")
        
        st.markdown('<div class="card" style="text-align: center;">', unsafe_allow_html=True)
        st.markdown("### $25")
        st.write("Provides educational materials for one woman for a month")
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="card" style="text-align: center;">', unsafe_allow_html=True)
        st.markdown("### $100")
        st.write("Funds a week of vocational training for one woman")
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="card" style="text-align: center;">', unsafe_allow_html=True)
        st.markdown("### $500")
        st.write("Supports a micro-enterprise startup for one woman")
        st.markdown('</div>', unsafe_allow_html=True)

# Volunteer page
def volunteer():
    hero_section(
        "Join Hands with CEDRA",
        "Make a difference in vulnerable communities",
        height=300
    )
    
    st.markdown("## Why Volunteer with Us?")
    st.write("""
    Volunteers are the backbone of CEDRA. Your time and skills help us reach more women and families, 
    run impactful programs, and create lasting change. Hear from our volunteers:
    """)
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown("Volunteering with CEDRA gave me purpose and a chance to uplift others.")
        st.write("— Asha, Community Outreach Volunteer")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown("I learned so much and made lifelong friends while making a difference.")
        st.write("— Ravi, Data Collection Volunteer")
        st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown("## Volunteer Expectations")
    st.markdown("""
    - Commit to at least 6 hours per month (unless otherwise agreed).
    - Adhere to CEDRA's Volunteer Code of Conduct.
    - Participate in onboarding and training sessions.
    - Communicate availability and changes in schedule.
    """)
    
    # Volunteer Form
    st.markdown("## Volunteer Signup Form")
    
    with st.form("volunteer_form"):
        col1, col2 = st.columns(2)
        with col1:
            first_name = st.text_input("First Name *")
        with col2:
            last_name = st.text_input("Last Name *")
        
        col3, col4 = st.columns(2)
        with col3:
            email = st.text_input("Email Address *")
        with col4:
            phone = st.text_input("Phone Number")
        
        col5, col6, col7 = st.columns(3)
        with col5:
            city = st.text_input("City")
        with col6:
            state = st.text_input("State")
        with col7:
            country = st.text_input("Country")
        
        st.markdown("### Days Available")
        days = st.multiselect(
            "Select days",
            ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        )
        
        st.markdown("### Preferred Time Slots")
        time_slots = st.multiselect(
            "Select time slots",
            ["Morning", "Afternoon", "Evening"]
        )
        
        start_date = st.date_input("Start Date", min_value=datetime.date.today())
        
        st.markdown("### Areas of Interest")
        interests = st.multiselect(
            "Select areas of interest",
            [
                "Community Outreach",
                "Data Collection/Entry",
                "Field Volunteering",
                "Event Planning",
                "Fundraising",
                "Communications & Design",
                "Research & Reports",
                "Tech/Website Support",
            ]
        )
        
        experience = st.text_area("Previous Experience", placeholder="Share any relevant experience (optional)")
        
        resume = st.file_uploader("Resume Upload", type=["pdf", "doc", "docx"])
        
        motivation = st.text_area("Why do you want to volunteer with CEDRA? *")
        
        code_of_conduct = st.checkbox("I agree to CEDRA's Volunteer Code of Conduct *")
        
        col8, col9 = st.columns([3, 1])
        with col8:
            commitment = st.checkbox("I commit to volunteering at least the specified hours per month *")
        with col9:
            hours_per_month = st.number_input("Hours", min_value=1, value=6)
        
        submitted = st.form_submit_button("Submit")
        
        if submitted:
            if first_name and last_name and email and code_of_conduct and commitment:
                st.success("Thank you for signing up! We'll be in touch soon.")
            else:
                st.error("Please fill all required fields and agree to the commitments.")
    
    # FAQs
    st.markdown("## FAQs")
    
    with st.expander("Who can volunteer with CEDRA?"):
        st.write("Anyone 18 years or older who is passionate about our mission can apply. Some roles may require specific skills or background checks.")
    
    with st.expander("What is the minimum time commitment?"):
        st.write("We ask for a minimum of 6 hours per month, but you can discuss your availability with our team.")
    
    with st.expander("Will I receive training?"):
        st.write("Yes! All volunteers receive onboarding and training relevant to their roles.")
    
    with st.expander("Can I volunteer remotely?"):
        st.write("Many roles can be done remotely. Please indicate your preference in the form.")
    
    # Contact Info
    st.markdown("## Still have questions?")
    st.write("Email our Volunteer Coordinator at volunteer@cedra.org")

# Contact page
def contact():
    hero_section(
        "Contact Us",
        "We'd love to hear from you",
        height=300
    )
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("## Send us a message")
        
        with st.form("contact_form"):
            name = st.text_input("Name")
            email = st.text_input("Email")
            subject = st.text_input("Subject")
            message = st.text_area("Message")
            submitted = st.form_submit_button("Send Message")
            
            if submitted:
                st.success("Your message has been sent! We'll get back to you soon.")
    
    with col2:
        st.markdown("## Contact Information")
        
        st.markdown("""
        **Address:**  
        Thondemvelil, Muttom P.O.  
        Thumpamon, Pathanamthitta - 689502
        
        **Email:**  
        info@cedra.org
        
        **Phone:**  
        +91 123 456 7890
        """)
        
        st.markdown("## Office Hours")
        st.write("Monday to Friday: 9:00 AM - 5:00 PM")
        st.write("Saturday: 9:00 AM - 1:00 PM")
        st.write("Sunday: Closed")
        
        # Simple map placeholder
        st.image("https://maps.googleapis.com/maps/api/staticmap?center=Pathanamthitta,Kerala,India&zoom=14&size=400x300&key=YOUR_API_KEY", use_column_width=True)

# Chatbot page
def chatbot():
    st.markdown("## CEDRA Assistant")
    st.write("Ask any questions about our programs, volunteering, or how you can help.")
    
    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = [
            {"role": "assistant", "content": "Hello! I'm the CEDRA assistant. How can I help you today?"}
        ]
    
    # Display chat messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])
    
    # User input
    user_input = st.chat_input("Type your message here...")
    
    if user_input:
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": user_input})
        
        # Display user message
        with st.chat_message("user"):
            st.write(user_input)
        
        # Generate assistant response based on simple rules
        response = generate_response(user_input)
        
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response})
        
        # Display assistant response
        with st.chat_message("assistant"):
            st.write(response)

# Simple rule-based response generator
def generate_response(user_input):
    user_input = user_input.lower()
    
    if any(word in user_input for word in ["hello", "hi", "hey"]):
        return "Hello! How can I help you with CEDRA's programs today?"
    
    elif any(word in user_input for word in ["program", "course", "workshop"]):
        return "CEDRA offers various programs including Skills Development Workshops, Financial Literacy Programs, and Microfinance Initiatives. Would you like to know more about any specific program?"
    
    elif any(word in user_input for word in ["donate", "donation", "contribute"]):
        return "Thank you for your interest in donating! Your contributions help us empower more women. You can donate through our website or contact us directly for other donation options."
    
    elif any(word in user_input for word in ["volunteer", "help", "assist"]):
        return "We're always looking for volunteers! You can help in areas like community outreach, data collection, event planning, and more. Please fill out the volunteer form on our website."
    
    elif any(word in user_input for word in ["contact", "reach", "phone", "email"]):
        return "You can contact us at info@cedra.org or call us at +91 123 456 7890. Our office is located at Thondemvelil, Muttom P.O., Thumpamon, Pathanamthitta - 689502."
    
    else:
        return "Thank you for your message. If you have questions about our programs, volunteering opportunities, or how to donate, I'm here to help!"

# Footer component
def footer():
    st.markdown("""
    <div class="footer">
        Thondemvelil, Muttom P.O. Thumpamon, Pathanamthitta - 689502
    </div>
    """, unsafe_allow_html=True)

# Main app logic
def main():
    choice = navigation()
    
    if choice == "Home":
        home()
    elif choice == "About":
        about()
    elif choice == "Programs":
        programs()
    elif choice == "Donate":
        donate()
    elif choice == "Volunteer":
        volunteer()
    elif choice == "Contact":
        contact()
    elif choice == "Chatbot":
        chatbot()
    
    footer()

if __name__ == "__main__":
    main()