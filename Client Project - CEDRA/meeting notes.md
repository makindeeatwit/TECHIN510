# Developer Meeting Note – Project Update (CEDRA)

## Project Scope

The CEDRA platform aims to empower underprivileged women through a modern, responsive digital platform. The project serves as a central hub for secure donations, community engagement, and AI-powered support, enhancing access to economic empowerment initiatives.

The core goals reviewed in this sprint include:
- Activating account login & creation functionality
- Embedding an OpenAI chatbot as a floating UI element
- Implementing a secure donation link (Stripe)
- Cleaning the homepage content with a focused mission statement
- Ensuring page-based navigation and modular visibility

---

## ✅ Features Reviewed

| Feature                            | Status            | Notes                                                                 |
|------------------------------------|-------------------|-----------------------------------------------------------------------|
| Login / Sign-up Page               | ✅ Completed       | Includes validation, password input, account creation flow            |
| Chatbot (Floating, Bottom-Right)   | ✅ Implemented     | Connected with OpenAI GPT-3.5; toggles visibility, stores history     |
| Donation Page                      | ✅ Tested          | Stripe test link added and displayed via navigation                   |
| Homepage Content                   | ✅ Updated         | Rewritten with clear introduction and NGO mission                     |
| Sidebar Navigation                 | ✅ Modular         | Each section shows exclusively when selected                          |

---

## Bugs Found

- `ModuleNotFoundError: No module named 'openai'` → Resolved by `pip install openai`
- `ChatCompletion` error due to outdated usage → Updated to match OpenAI v1.0+ format
- Donation section initially overlapping homepage content → Isolated under navigation logic

---

## Suggestions & Improvements

| Area               | Suggestions                                                                 |
|--------------------|----------------------------------------------------------------------------|
| User Management    | Store accounts in a database (Firebase / SQLite) instead of session memory |
| Chatbot UI         | Consider draggable or collapsible interface for better UX                  |
| Notifications      | Add toast messages after donation or login success                         |
| Security           | Hide passwords with hashing; Add captcha on registration                   |

---




Updatedt notes


# Developer Meeting Note – Project Update (CEDRA)

## Project Scope

The CEDRA platform aims to empower underprivileged women through a modern, responsive digital platform. The project serves as a central hub for secure donations, community engagement, and AI-powered support, enhancing access to economic empowerment initiatives.

The core goals reviewed in this sprint include:
- Updating homepage with mission content and call-to-action
- Fixing testimonial syntax issues on the Volunteer page
- Cleaning navigation logic
- Enhancing visual consistency across sections
- Preparing the app for Git commits

---

## ✅ Features Reviewed

| Feature                            | Status            | Notes                                                                 |
|------------------------------------|-------------------|-----------------------------------------------------------------------|
| Homepage Mission & Hero Section    | ✅ Completed       | Mission section now includes clear goals and styled impact message    |
| Volunteer Page Testimonials        | ✅ Fixed           | Fixed broken quotation syntax causing rendering issues                |
| Program Cards                      | ✅ Verified        | Programs now include images, descriptions, and enroll buttons         |
| Sidebar Navigation                 | ✅ Modular         | Each page renders exclusively based on user selection                 |
| Footer                             | ✅ Working         | Fixed persistent placement and style consistency                      |

---

##  Bugs Found

- **Incorrect quotation rendering** on testimonial markdown → Fixed with escaped characters or correct Markdown
- **Static map API key error** on Contact page → Placeholder used; key needs securing
- Minor **CSS inconsistencies** with button hover styling → Cleaned with scoped styling

---

## 💡 Suggestions & Improvements

| Area               | Suggestions                                                                 |
|--------------------|----------------------------------------------------------------------------|
| Git Setup          | Ensure `.streamlit/` and sensitive configs (like API keys) are `.gitignore`d |
| Chatbot            | Convert to floating component or minimize into icon                         |
| Mobile View        | Test responsiveness, especially for columns and hero images                 |
| Contact Page       | Add functional email service integration (e.g., SMTP or Formspree)           |

---

## 📝 Reflections

The team made strong progress on streamlining the homepage, unifying the visual style, and stabilizing components like the volunteer and donate pages. Additional time is needed for advanced features such as real-time chat UI improvements and secure backend user management.

Next steps:
- Integrate chatbot into floating UI component
- Hook up backend database for login/account persistence
- Finalize deployment with correct API keys and test Stripe payments

