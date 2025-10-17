import streamlit as st
import pandas as pd
from skillcred1 import AnswerEvaluator


evaluator = AnswerEvaluator()

st.sidebar.title("📘 Instructions and some Info...")
with st.sidebar.expander("📘  Show Instructions and Info"):
    st.write("➤Answer all questions in your own words...")
    st.write("➤Please Press ctrl + Enter after complition of Answer.")
    st.write("➤Your answers are compared semantically")
    st.write("➤Accuracy Score based on the questions you asnswerd")
# ----------------------------------------------------------------------

data = pd.read_csv("data_sc/ai_ml_questions.csv")

st.set_page_config(page_title="AI Answer Evaluation", page_icon="🧠", layout="wide")

st.title(" AI-Based Answer Evaluation System")
st.write("Select the topic & Answer the following questions and get your accuracy score based on semantic similarity.")

topics=sorted(data['topic'].unique())
selected_topic=st.selectbox("select a topic:",topics)

total_score = 0
answered_count = 0

for i, row in data.iterrows():
    st.subheader(f"Q{i+1}: {row['question']}")
    user_answer = st.text_area(f"Your Answer for Q{i+1}", key=f"ans_{i}")

    if user_answer.strip():
        score = evaluator.get_similarity(row['correct_answer'], user_answer)
        st.write(f" **Similarity Score:** {score}%")
        total_score += score
        answered_count += 1

if answered_count > 0:


    avg_score = total_score / answered_count
    st.markdown(f"###  Final Accuracy: **{round(avg_score, 2)}%**")

st.info("Your answers are compared semantically — so meaning matters, not exact words.")

if avg_score>70:
    st.success("Excellent! You understood the concept well.")
elif avg_score>50:
    st.warning("Good try, but you can refine your answer.")
else:
    st.error("Needs improvement. Try to include key concepts.")