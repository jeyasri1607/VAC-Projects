import streamlit as st

st.set_page_config(
    page_title="AI Quiz Chatbot",
    page_icon="🤖",
    layout="centered"
)

st.markdown("""
<style>
.stApp {
    background-color: #ffc0cb;
}

h1 {
    text-align: center;
    color: darkred;
    font-size: 45px;
}

div.stButton > button {
    background-color: #ff4d88;
    color: white;
    border-radius: 10px;
    height: 50px;
    width: 200px;
    font-size: 20px;
    border: none;
}

div.stButton > button:hover {
    background-color: #e6005c;
}
</style>
""", unsafe_allow_html=True)

st.title("🤖 AI Quiz Chatbot")
st.write("### Answer all questions below 👇")

questions = [
    {
        "question": "What is the capital of India?",
        "options": ["Delhi", "Mumbai", "Chennai", "Kolkata"],
        "answer": "Delhi"
    },
    {
        "question": "Which programming language is best for AI?",
        "options": ["Python", "HTML", "CSS", "Java"],
        "answer": "Python"
    },
    {
        "question": "Who developed Python?",
        "options": ["Guido van Rossum", "Bill Gates", "Elon Musk", "Mark Zuckerberg"],
        "answer": "Guido van Rossum"
    },
    {
        "question": "What does CPU stand for?",
        "options": ["Central Processing Unit", "Computer Personal Unit", "Central Program Utility", "Control Processing User"],
        "answer": "Central Processing Unit"
    },
    {
        "question": "Which company developed ChatGPT?",
        "options": ["Google", "Microsoft", "OpenAI", "Amazon"],
        "answer": "OpenAI"
    }
]

score = 0
answers = []

with st.form("quiz_form"):

    for i, q in enumerate(questions):
        st.subheader(f"Q{i+1}. {q['question']}")

        ans = st.radio(
            "Choose your answer:",
            q["options"],
            key=i
        )

        answers.append(ans)

    submit = st.form_submit_button("Submit Quiz")

if submit:

    for i, q in enumerate(questions):
        if answers[i] == q["answer"]:
            score += 1

    st.success(f"Your Score: {score}/5")

    percent = (score / len(questions)) * 100
    st.write(f"Percentage: {percent}%")

    if score == 5:
        st.balloons()
        st.success("Perfect Score 🏆")
    elif score >= 3:
        st.info("Good Job 👍")
    else:
        st.warning("Keep Practicing 😊")

st.write("---")
st.write("Made with ❤️ using Streamlit")