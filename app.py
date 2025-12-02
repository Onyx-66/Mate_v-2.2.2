from __future__ import annotations

import streamlit as st
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(
    page_title="StudyMate AI",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Enhanced CSS
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

        html, body, [class*="css"] {
            font-family: 'Inter', sans-serif;
        }

        [data-testid="stSidebarNav"] {
            display: none;
        }
        
        [data-testid="stSidebar"] {
            background: linear-gradient(180deg, #0f172a 0%, #1e293b 100%);
            border-right: 1px solid #334155;
        }
        
        .main .block-container {
            padding-top: 2rem;
            max-width: 1400px;
        }
        
        .stExpander {
            background-color: #1e293b;
            border: 1px solid #334155;
            border-radius: 12px;
            margin-bottom: 1rem;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
        }
        
        [data-testid="stMetricValue"] {
            font-size: 2rem;
            font-weight: 700;
        }
        
        /* Responsive Design */
        @media (max-width: 768px) {
            .main .block-container {
                padding-top: 1rem;
                padding-left: 1rem;
                padding-right: 1rem;
            }
            
            [data-testid="stSidebar"] {
                width: 100% !important;
            }
            
            h1 {
                font-size: 2rem !important;
            }
            
            h2 {
                font-size: 1.5rem !important;
            }
        }

        /* Refined Button Styles */
        .stButton > button {
            border-radius: 8px;
            font-weight: 500;
            transition: all 0.2s ease;
            border: 1px solid transparent;
            padding: 0.5rem 1rem;
            box-shadow: 0 1px 2px rgba(0, 0, 0, 0.05);
        }
        
        .stButton > button:hover {
            transform: translateY(-1px);
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
            border-color: rgba(255, 255, 255, 0.1);
        }
        
        .stButton > button:active {
            transform: translateY(0);
        }

        /* Sidebar Navigation Icons */
        /* Home Button (2nd button) */
        [data-testid="stSidebar"] .stButton:nth-of-type(2) button {
            background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24' fill='none' stroke='%2310b981' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z'%3E%3C/path%3E%3Cpolyline points='9 22 9 12 15 12 15 22'%3E%3C/polyline%3E%3C/svg%3E");
            background-repeat: no-repeat;
            background-position: 1rem center;
            padding-left: 3.5rem;
            text-align: left;
        }

        /* Study Button (3rd button) */
        [data-testid="stSidebar"] .stButton:nth-of-type(3) button {
            background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24' fill='none' stroke='%2310b981' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z'%3E%3C/path%3E%3Cpath d='M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z'%3E%3C/path%3E%3C/svg%3E");
            background-repeat: no-repeat;
            background-position: 1rem center;
            padding-left: 3.5rem;
            text-align: left;
        }

        /* Community Button (4th button) */
        [data-testid="stSidebar"] .stButton:nth-of-type(4) button {
            background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24' fill='none' stroke='%2310b981' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2'%3E%3C/path%3E%3Ccircle cx='9' cy='7' r='4'%3E%3C/circle%3E%3Cpath d='M23 21v-2a4 4 0 0 0-3-3.87'%3E%3C/path%3E%3Cpath d='M16 3.13a4 4 0 0 1 0 7.75'%3E%3C/path%3E%3C/svg%3E");
            background-repeat: no-repeat;
            background-position: 1rem center;
            padding-left: 3.5rem;
            text-align: left;
        }

        /* History Button (5th button) */
        [data-testid="stSidebar"] .stButton:nth-of-type(5) button {
            background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24' fill='none' stroke='%2310b981' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='M12 20v-6M6 20V10M18 20V4'%3E%3C/path%3E%3C/svg%3E");
            background-repeat: no-repeat;
            background-position: 1rem center;
            padding-left: 3.5rem;
            text-align: left;
        }
    </style>

    <script>
        function scrollToAnchor() {
            var target = window.parent.document.getElementById("study-top");
            if (target) {
                target.scrollIntoView({ behavior: 'smooth', block: 'start' });
            } else {
                // Fallback to top
                window.scrollTo(0, 0);
                var main = window.parent.document.querySelector(".main");
                if (main) {
                    main.scrollTop = 0;
                }
            }
        }

        // Initial scroll
        scrollToAnchor();

        // Watch for changes
        var observer = new MutationObserver(function(mutations) {
            // Only scroll if we are on the study page and the anchor exists
            var target = window.parent.document.getElementById("study-top");
            if (target) {
                // Check if we just loaded this section
                scrollToAnchor();
            }
        });

        var target = window.parent.document.querySelector(".main");
        if (target) {
            observer.observe(target, { childList: true, subtree: true });
        }
        
        setTimeout(scrollToAnchor, 100);
        setTimeout(scrollToAnchor, 500);
    </script>

""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    # Logo with clickable link to home
    if st.button("StudyMate AI", key="logo_home", use_container_width=True):
        st.session_state.current_page = "Home"
        st.rerun()
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Navigation section
    st.markdown("""
        <div style='padding: 0 0.5rem;'>
            <p style='color: #64748b; font-size: 0.75rem; text-transform: uppercase; 
                      letter-spacing: 1px; margin-bottom: 0.5rem; font-weight: 600;'>
                Navigation
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    if "current_page" not in st.session_state:
        st.session_state.current_page = "Home"
    
    pages = {
        "Home": "Home",
        "Study": "Study",
        "Community": "Community",
        "History": "History"
    }
    
    for page_name, label in pages.items():
        is_selected = st.session_state.current_page == page_name
        
        if st.button(
            label, 
            key=f"nav_{page_name}",
            use_container_width=True,
            type="primary" if is_selected else "secondary"
        ):
            st.session_state.current_page = page_name
            st.rerun()
    
    # Footer
    st.markdown("<br><br><br>", unsafe_allow_html=True)
    st.markdown("""
        <div style='position: fixed; bottom: 0; left: 0; right: 0; padding: 1.5rem; 
                    border-top: 1px solid #334155; 
                    background: linear-gradient(180deg, transparent 0%, #0f1419 100%);
                    width: inherit;'>
            <p style='color: #64748b; font-size: 0.75rem; text-align: center; margin: 0;'>
                Made with ❤️ for Education
            </p>
            <p style='color: #475569; font-size: 0.7rem; text-align: center; margin-top: 0.25rem;'>
                Powered by Onyx Team
            </p>
        </div>
    """, unsafe_allow_html=True)

# Main content
page = st.session_state.current_page

if page == "Home":
    from pages import home
    home.show()
elif page == "Study":
    from pages import study
    study.show()
elif page == "Community":
    from pages import community
    community.show()
elif page == "History":
    from pages import history
    history.show()
