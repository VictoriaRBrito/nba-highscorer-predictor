# app.py

import streamlit as st
import pandas as pd
from src.inference import load_model, predict_highscorer

def main():
    st.title("🏀 NBA High-Scorer Predictor")
    st.markdown(
        """
        Upload a CSV file containing one or more rows of NBA player box‐score stats 
        (with the same columns you used for training) and get back:
        - A probability that they’ll score 20+ points
        - A binary “HighScorer” prediction using the 0.40 threshold
        """
    )

    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
    if uploaded_file is not None:
        # Read the uploaded CSV into a DataFrame
        df_new = pd.read_csv(uploaded_file)

        # Run inference
        preds, probs = predict_highscorer(df_new)

        # Attach results to the DataFrame
        df_new["HighScorer"]   = preds
        df_new["Probability"]  = probs

        # Display the results
        st.subheader("Predictions")
        st.write(df_new)

        # Show a more user-friendly summary
        for i, row in df_new.iterrows():
            status = "✅ High Scorer" if row["HighScorer"] == 1 else "❌ Non-High Scorer"
            st.write(f"**Row {i+1}:** {status} (p = {row['Probability']:.2f})")

if __name__ == "__main__":
    main()
