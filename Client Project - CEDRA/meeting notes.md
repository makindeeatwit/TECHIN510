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
