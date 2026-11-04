# Experiment 4 – Personalized Recommendation System

## Run
1. Install Python 3.10+.
2. Open a terminal in this folder.
3. Run: `pip install -r requirements.txt`
4. Run: `streamlit run main.py`

## Optional GPT-4-family API
Set your API key before starting the app:
- Windows PowerShell: `$env:OPENAI_API_KEY="your-key"`
- macOS/Linux: `export OPENAI_API_KEY="your-key"`

The app uses `gpt-4o` by default when the key is configured. Without a key, it runs in demo mode with built-in recommendations.

## Modules
input_module.py, profile_module.py, prompt_module.py, recommendation_module.py,
ranking_module.py, feedback_module.py, explanation_module.py, intent_module.py,
save_module.py, utils.py, main.py.
