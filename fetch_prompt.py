import json
from datetime import datetime

# You can add as many as you want here. One will be picked every week.
PROMPT_VAULT = [
    {
        "title": "The 'Executive Logic' Filter",
        "text": "Analyze the attached document and extract the 3 most controversial points and 2 immediate opportunities for my business.",
        "benefit": "Best used with Claude 3.5 for high-level strategic parsing."
    },
    {
        "title": "The 'Meeting Triage' Expert",
        "text": "Based on this transcript, create a table of: 1. Decisions Made, 2. Owner Assigned, 3. Deadline. Flag any ambiguity.",
        "benefit": "Turn a 60-minute mess into a 30-second action plan."
    },
    {
        "title": "The 'Simple Speak' Translator",
        "text": "Explain this technical concept to me as if I am a CEO with 5 minutes to spare. Focus on ROI and Risk, not the mechanics.",
        "benefit": "Use this to prep for presentations or simplify complex AI news."
    }
]

def update_weekly_prompt():
    week_num = datetime.now().isocalendar()[1]
    index = week_num % len(PROMPT_VAULT)
    selected = PROMPT_VAULT[index]
    with open("prompt.json", "w", encoding="utf-8") as f:
        json.dump(selected, f, indent=4)

if __name__ == "__main__":
    update_weekly_prompt()
