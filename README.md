# Habit Tracker 🗓️

A simple daily habit tracker built with [Streamlit](https://streamlit.io). Add habits, check them off each day, and track your streaks and completion rates over time.

## Features

- ➕ Add and delete habits from the sidebar
- ✅ Daily check-in that remembers what you've already marked today
- 🔥 Streak counter — see how many consecutive days you've kept a habit going
- 📊 Completion rate — track your overall consistency per habit
- 💾 Data persists locally in a CSV file — no database needed

## Tech Stack

- [Streamlit](https://streamlit.io) — UI framework
- [Pandas](https://pandas.pydata.org) — data handling
- Python's built-in `datetime` — date and streak logic

## Getting Started

### Prerequisites
- Python 3.8+

### Installation

```bash
git clone https://github.com/your-username/habit-tracker.git
cd habit-tracker
pip install -r requirements.txt
```

### Run the app

```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`.

## How It Works

- Each habit check-in is stored as a row in `habits.csv` with the date, habit name, and whether it was completed.
- On each run, the app checks if today's entry already exists for a habit — if so, the checkbox reflects that; if not, it starts unchecked.
- Streaks are calculated by walking backward day-by-day from today until a missed day is found.

## Project Structure

```
habit-tracker/
├── app.py          # Main Streamlit app
├── requirements.txt
├── .gitignore
└── README.md
```

> Note: `habits.csv` is created automatically on first run and is excluded from version control since it contains your personal data.

## Future Ideas

- [ ] Tabbed layout (Today / Stats / History)
- [ ] Heatmap calendar view
- [ ] Reminders/notifications
- [ ] Export data to CSV/PDF

## License

MIT
