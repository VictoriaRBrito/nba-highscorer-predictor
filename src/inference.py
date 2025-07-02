import joblib
import pandas as pd

# If you ever move your .pkl files, adjust these paths accordingly
_MODEL_PATH     = "models/highscorer_model.pkl"
_FEATURES_PATH  = "models/features_list.pkl"
_THRESHOLD_PATH = "models/threshold.pkl"


def load_model():
    """
    Load our serialized artifacts from disk.

    Returns:
        model: Trained classifier
        features: List[str] of column names to pull from new data
        threshold: float, probability cutoff for HighScorer=1
    """
    model     = joblib.load(_MODEL_PATH)
    features  = joblib.load(_FEATURES_PATH)
    threshold = joblib.load(_THRESHOLD_PATH)
    return model, features, threshold


def predict_highscorer(df_new: pd.DataFrame):
    """
    Given a DataFrame with the raw player stats, returns both
    the binary HighScorer prediction and the raw probability.

    Args:
        df_new: pd.DataFrame with at least the columns in `features`

    Returns:
        preds: np.ndarray of 0/1 labels
        probs: np.ndarray of floats (probability of class=1)
    """
    model, features, threshold = load_model()

    # Keep only the columns our model expects
    X_new = df_new[features]

    # Predict probability of class 1 (HighScorer)
    probs = model.predict_proba(X_new)[:, 1]

    # Apply our chosen cutoff
    preds = (probs >= threshold).astype(int)

    return preds, probs
