import streamlit as st
import sqlite3
import random

FINISH_LINE = 50

# ---------------- DATABASE ----------------

conn = sqlite3.connect("race.db", check_same_thread=False)
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS players(
    name TEXT PRIMARY KEY,
    position INTEGER
)
""")
conn.commit()

# ---------------- FUNCTIONS ----------------

def add_player(name):
    cur.execute(
        "INSERT OR IGNORE INTO players(name, position) VALUES(?, ?)",
        (name, 0)
    )
    conn.commit()

def get_players():
    cur.execute(
        "SELECT name, position FROM players ORDER BY position DESC"
    )
    return cur.fetchall()

def move_player(name):
    dice = random.randint(1, 6)

    cur.execute(
        "SELECT position FROM players WHERE name=?",
        (name,)
    )
    row = cur.fetchone()

    if row:
        new_pos = row[0] + dice

        cur.execute(
            "UPDATE players SET position=? WHERE name=?",
            (new_pos, name)
        )
        conn.commit()

    return dice

def reset_game():
    cur.execute("DELETE FROM players")
    conn.commit()

# ---------------- UI ----------------

st.title("🏎️ Multiplayer Dice Car Race")

st.write(f"Finish Line: {FINISH_LINE}")

player_name = st.text_input("Enter Your Name")

col1, col2 = st.columns(2)

with col1:
    if st.button("Join Race"):
        if player_name.strip():
            add_player(player_name.strip())
            st.success("Joined Race!")

with col2:
    if st.button("Reset Game"):
        reset_game()
        st.success("Game Reset")

st.divider()

if player_name.strip():

    if st.button("🎲 Roll Dice"):

        players = get_players()

        winner_exists = False

        for p, pos in players:
            if pos >= FINISH_LINE:
                winner_exists = True

        if winner_exists:
            st.warning("Game already finished!")
        else:
            dice = move_player(player_name.strip())
            st.success(f"You rolled: {dice}")

st.divider()

st.subheader("Leaderboard")

players = get_players()

winner = None

for name, pos in players:

    progress = min(pos / FINISH_LINE, 1.0)

    st.write(f"🚗 {name} : {pos}")

    st.progress(progress)

    if pos >= FINISH_LINE and winner is None:
        winner = name

if winner:
    st.balloons()
    st.success(f"🏆 Winner: {winner}")

st.divider()

st.write("Refresh page to see latest positions.")
