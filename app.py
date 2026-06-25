import pandas as pd
import os
import streamlit as st
from datetime import date, timedelta

def load_data():
    if os.path.exists("habits.csv"):
        return pd.read_csv("habits.csv")
    else:
        df = pd.DataFrame(columns=["date", "habit", "done"])
        df.to_csv("habits.csv", index=False)
        return df

def save_data(df):
    df.to_csv("habits.csv", index=False)

def get_streak(df, habit):
    streak = 0
    current_day = date.today()
    while True:
        row = df[(df["habit"] == habit) & (df["date"] == str(current_day))]
        if len(row) > 0 and row["done"].iloc[0] == True:
            streak += 1
            current_day = current_day - timedelta(days=1)
        else:
            break
    return streak

def get_completion_rate(df, habit):
    habit_rows = df[df["habit"] == habit]
    if len(habit_rows) == 0:
        return 0
    done_count = len(habit_rows[habit_rows["done"] == True])
    return round((done_count / len(habit_rows)) * 100)

df = load_data()
st.write(df)

# Sidebar — Add & manage habits
st.sidebar.title("Habit Tracker")
habit_name = st.sidebar.text_input("add a habit..")
if st.sidebar.button("Add"):
    if habit_name.strip():
        df.loc[len(df)] = [date.today(), habit_name, False]
        save_data(df)
        st.success("habit successfully added!")
    else:
        st.sidebar.error("name can't be empty!")

st.sidebar.subheader("Your Habits")
for habit in df["habit"].unique():
    st.sidebar.write(habit)
    if st.sidebar.button(f"{habit}", key=habit):
        df = df[df["habit"] != habit]
        save_data(df)

# Main page — Today's check-in
today = date.today()
st.header(f"today: {today}")

checked_habits = {}

for habit in df["habit"].unique():
    today_row = df[(df["habit"] == habit) & (df["date"] == str(today))]
    if len(today_row) > 0:
        is_done = today_row["done"].iloc[0]
    else:
        is_done = False
    checked_habits[habit] = st.checkbox(habit, value=is_done)

if st.button("Save Today"):
    for habit, is_checked in checked_habits.items():
        today_row = df[(df["habit"] == habit) & (df["date"] == str(today))]

        if len(today_row) > 0:
            df.loc[(df["habit"] == habit) & (df["date"] == str(today)), "done"] = is_checked
        else:
            df.loc[len(df)] = [str(today), habit, is_checked]

    save_data(df)
    st.success("Saved!")

# Stats section
st.subheader("Your Stats")

for habit in df["habit"].unique():
    streak = get_streak(df, habit)
    rate = get_completion_rate(df, habit)

    col1, col2 = st.columns(2)
    with col1:
        st.metric(f"{habit} streak", f"{streak} days")
    with col2:
        st.metric(f"{habit} completion", f"{rate}%")