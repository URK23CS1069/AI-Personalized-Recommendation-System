import streamlit as st
from profile_module import analyze_profile
from recommendation_module import generate_recommendations
from ranking_module import rank_recommendations
from feedback_module import refine_recommendations
from explanation_module import explain_recommendation
from intent_module import detect_intent
from save_module import save_recommendations
from utils import format_profile

st.set_page_config(page_title="AI Recommendation Chatbot", page_icon="🎓", layout="centered")
st.markdown("""
<style>
.main .block-container {max-width: 850px; padding-top: 1.5rem;}
.chatbox {background:#f0f0f0; padding:15px; border-radius:12px; margin:8px 0;}
.userbox {background:#dff1ff; padding:15px; border-radius:12px; text-align:right; margin:8px 0;}
.rec {background:#f4f4f4; padding:14px; border-radius:10px; margin:10px 0;}
.small {color:#666; text-align:center;}
</style>
""", unsafe_allow_html=True)

st.title("AI Recommendation Chatbot")
st.markdown("<p class='small'>Tell me about yourself and I will recommend suitable learning topics.</p>", unsafe_allow_html=True)

with st.form("profile_form"):
    name = st.text_input("Name", placeholder="Your name")
    age = st.text_input("Age", placeholder="e.g. 20")
    background = st.text_input("Educational / Professional Background", placeholder="e.g. Computer Science student")
    interests = st.text_input("Interests", placeholder="e.g. Python, Artificial Intelligence, Data Science")
    skill = st.selectbox("Skill Level", ["Beginner", "Intermediate", "Advanced"])
    preference = st.selectbox("Preferred Category", ["Practical learning", "Theoretical learning", "Project-based learning", "Video courses", "Reading"])
    goal = st.text_input("Learning Goal", placeholder="e.g. Learn AI and get a job")
    count = st.slider("Number of recommendations", 1, 10, 5)
    submitted = st.form_submit_button("Get Recommendations", use_container_width=True)

if "items" not in st.session_state:
    st.session_state.items = []
if "profile" not in st.session_state:
    st.session_state.profile = {}
if "analysis" not in st.session_state:
    st.session_state.analysis = {}

if submitted:
    profile = {"name": name, "age": age, "background": background, "interests": interests,
               "skill_level": skill, "preference": preference, "goal": goal, "num_items": count}
    analysis = analyze_profile(profile)
    st.session_state.profile = profile
    st.session_state.analysis = analysis
    st.session_state.items = rank_recommendations(generate_recommendations(profile, analysis, count))
    st.session_state.feedback = ""

if st.session_state.profile:
    st.subheader("Collected User Profile")
    for label, value in format_profile(st.session_state.profile):
        st.write(f"**{label}:** {value}")
    st.subheader("Preference Analysis")
    a = st.session_state.analysis
    st.write(f"**Primary Interest:** {a['primary_interest']}")
    st.write(f"**Secondary Interest:** {a['secondary_interest']}")
    st.write(f"**Skill Level:** {a['skill_level']}")
    st.write(f"**Goal:** {a['goal']}")
    st.write(f"**Preference:** {a['preference']}")
    st.subheader("Personalized Recommendations")
    for i, item in enumerate(st.session_state.items, 1):
        st.markdown(f"""<div class="rec"><b>{i}. {item['name']}</b><br>
        <b>Reason:</b> {item['reason']}<br><b>Score: {item['score']}%</b></div>""", unsafe_allow_html=True)

    st.subheader("Refine your recommendations")
    feedback = st.text_area("What would you like to change?", placeholder="Example: I prefer Artificial Intelligence and do not want Web Development resources.")
    if st.button("Refine Recommendations", use_container_width=True):
        intent = detect_intent(feedback)
        st.caption(f"Detected Intent: {intent}")
        updated = refine_recommendations(st.session_state.items, feedback)
        if updated:
            st.session_state.items = updated[:st.session_state.profile["num_items"]]
            st.rerun()
        else:
            st.info("No recommendations matched that feedback. Try different feedback.")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Show Profile"):
            st.json(st.session_state.profile)
    with col2:
        if st.button("Save Recommendations"):
            path = save_recommendations(st.session_state.profile, st.session_state.items)
            with open(path, "rb") as f:
                st.download_button("Download recommendations.txt", f, file_name="recommendations.txt")
    with st.expander("Prompt constructed for GPT-4"):
        from prompt_module import build_prompt
        st.code(build_prompt(st.session_state.profile, st.session_state.analysis, st.session_state.profile["num_items"]))
else:
    st.info("Fill in your details above and click **Get Recommendations** to begin.")

st.caption("If OPENAI_API_KEY is configured, recommendations use the OpenAI API. Otherwise, a built-in demo recommender is used.")
