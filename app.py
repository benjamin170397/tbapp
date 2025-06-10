import streamlit as st

st.set_page_config(page_title="Treble Peak Competitive Analysis", layout="wide")

# Slide navigation
slides = [
    "Welcome",
    "Strategic Context",
    "Workshop Structure",
    "Pre-Workshop Preparation",
    "Direct Competitors",
    "Tech Platform Competitors",
    "SWOT Analysis",
    "Competitive Positioning Matrix",
    "Competitive Intelligence Gathering",
    "Action Planning",
    "Performance Benchmarking",
    "Implementation Recommendations",
    "Q&A"
]

if "slide" not in st.session_state:
    st.session_state.slide = 0

def next_slide():
    if st.session_state.slide < len(slides) - 1:
        st.session_state.slide += 1

def prev_slide():
    if st.session_state.slide > 0:
        st.session_state.slide -= 1

st.sidebar.title("Navigation")
if st.sidebar.button("Previous"):
    prev_slide()
if st.sidebar.button("Next"):
    next_slide()
st.sidebar.write(f"Slide {st.session_state.slide+1} of {len(slides)}")

slide = st.session_state.slide

# Slide content
if slide == 0:
    st.title("Treble Peak: Competitive Analysis Workshop")
    st.markdown("""
    Welcome to the internal competitive analysis session.
    
    **Purpose:**  
    - Understand our competitive landscape  
    - Identify opportunities and threats  
    - Align on strategic actions

    ---
    """)
elif slide == 1:
    st.header("Strategic Context")
    st.markdown("""
    - Private markets are evolving rapidly.
    - Treble Peak operates as a multi-sided platform for investors, wealth managers, and fund managers.
    - Major players: CVC (€70bn), KKR (€66bn), EQT (€61bn).
    """)
elif slide == 2:
    st.header("Workshop Structure")
    st.markdown("""
    - **Duration:** 4–5 hours (quarterly)
    - **Participants:** BD, Product, Marketing, Sales, Leadership
    - **Format:** Cross-functional, interactive, actionable
    """)
elif slide == 3:
    st.header("Pre-Workshop Preparation")
    st.markdown("""
    - Gather competitor data, market trends, and customer feedback.
    - Distribute competitor profiles in advance.
    - Prepare recent sales intelligence and market news.
    """)
elif slide == 4:
    st.header("Direct Platform Competitors")
    st.markdown("""
    - **Moonfare:** Digital PE platform, 250+ fund managers, 75k+ members.
    - **Opto Investments:** Wealth manager focus, rapid fund launches.
    - **Privatize:** European B2B, regulatory expertise, Preqin partnership.
    """)
elif slide == 5:
    st.header("Tech Platform Competitors")
    st.markdown("""
    - **Preqin Allocator Hub:** End-to-end analytics and workflow.
    - **Linqto:** Pre-IPO marketplace, mobile-first.
    """)
elif slide == 6:
    st.header("SWOT Analysis")
    st.markdown("""
    - **Strengths:** Platform flexibility, multi-segment reach, regulatory knowledge.
    - **Weaknesses:** Brand awareness, resource constraints.
    - **Opportunities:** Market expansion, tech enhancement.
    - **Threats:** New entrants, tech disruption, regulatory changes.
    """)
elif slide == 7:
    st.header("Competitive Positioning Matrix")
    st.markdown("""
    - Map competitors: Tech sophistication vs. Market reach.
    - Identify white space for Treble Peak.
    """)
elif slide == 8:
    st.header("Competitive Intelligence Gathering")
    st.markdown("""
    - Monitor: Websites, news, funding, partnerships, customer reviews.
    - Use battlecards and regular updates.
    """)
elif slide == 9:
    st.header("Action Planning")
    st.markdown("""
    - Immediate tactical responses.
    - Medium-term strategic adjustments.
    - Long-term market opportunities.
    - Assign owners and timelines.
    """)
elif slide == 10:
    st.header("Performance Benchmarking")
    st.markdown("""
    - Track: Customer acquisition, platform usage, partnerships, AUM.
    - Use both leading and lagging indicators.
    """)
elif slide == 11:
    st.header("Implementation Recommendations")
    st.markdown("""
    - Integrate insights into business planning.
    - Share competitive intelligence regularly.
    - Create a competitive response playbook.
    """)
elif slide == 12:
    st.header("Q&A")
    st.markdown("""
    - Open floor for discussion.
    - Capture feedback and next steps.
    """)

st.markdown("---")
st.caption("Treble Peak | Internal Use Only")
