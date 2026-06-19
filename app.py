# # # # import streamlit as st
# # # # import sqlite3
# # # # import random

# # # # FINISH_LINE = 120

# # # # # ---------------- DATABASE ----------------

# # # # conn = sqlite3.connect("race.db", check_same_thread=False)
# # # # cur = conn.cursor()

# # # # cur.execute("""
# # # # CREATE TABLE IF NOT EXISTS players(
# # # #     name TEXT PRIMARY KEY,
# # # #     position INTEGER
# # # # )
# # # # """)
# # # # conn.commit()

# # # # # ---------------- FUNCTIONS ----------------

# # # # def add_player(name):
# # # #     cur.execute(
# # # #         "INSERT OR IGNORE INTO players(name, position) VALUES(?, ?)",
# # # #         (name, 0)
# # # #     )
# # # #     conn.commit()

# # # # def get_players():
# # # #     cur.execute(
# # # #         "SELECT name, position FROM players ORDER BY position DESC"
# # # #     )
# # # #     return cur.fetchall()

# # # # def move_player(name):
# # # #     dice = random.randint(1, 6)

# # # #     cur.execute(
# # # #         "SELECT position FROM players WHERE name=?",
# # # #         (name,)
# # # #     )
# # # #     row = cur.fetchone()

# # # #     if row:
# # # #         new_pos = row[0] + dice

# # # #         cur.execute(
# # # #             "UPDATE players SET position=? WHERE name=?",
# # # #             (new_pos, name)
# # # #         )
# # # #         conn.commit()

# # # #     return dice

# # # # def reset_game():
# # # #     cur.execute("DELETE FROM players")
# # # #     conn.commit()

# # # # # ---------------- UI ----------------

# # # # st.title("🏎️ Multiplayer Dice Car Race")

# # # # st.write(f"Finish Line: {FINISH_LINE}")

# # # # player_name = st.text_input("Enter Your Name")

# # # # col1, col2 = st.columns(2)

# # # # with col1:
# # # #     if st.button("Join Race"):
# # # #         if player_name.strip():
# # # #             add_player(player_name.strip())
# # # #             st.success("Joined Race!")

# # # # with col2:
# # # #     if st.button("Reset Game"):
# # # #         reset_game()
# # # #         st.success("Game Reset")

# # # # st.divider()

# # # # if player_name.strip():

# # # #     if st.button("🎲 Roll Dice"):

# # # #         players = get_players()

# # # #         winner_exists = False

# # # #         for p, pos in players:
# # # #             if pos >= FINISH_LINE:
# # # #                 winner_exists = True

# # # #         if winner_exists:
# # # #             st.warning("Game already finished!")
# # # #         else:
# # # #             dice = move_player(player_name.strip())
# # # #             st.success(f"You rolled: {dice}")

# # # # st.divider()

# # # # st.subheader("Leaderboard")

# # # # players = get_players()

# # # # winner = None

# # # # for name, pos in players:

# # # #     progress = min(pos / FINISH_LINE, 1.0)

# # # #     st.write(f"🚗 {name} : {pos}")

# # # #     st.progress(progress)

# # # #     if pos >= FINISH_LINE and winner is None:
# # # #         winner = name

# # # # if winner:
# # # #     st.balloons()
# # # #     st.success(f"🏆 Winner: {winner}")

# # # # st.divider()

# # # # st.write("Refresh page to see latest positions.")
# # # import streamlit as st
# # # import sqlite3
# # # from datetime import datetime

# # # # Database
# # # conn = sqlite3.connect("chat.db", check_same_thread=False)
# # # cur = conn.cursor()

# # # cur.execute("""
# # # CREATE TABLE IF NOT EXISTS messages(
# # #     id INTEGER PRIMARY KEY AUTOINCREMENT,
# # #     name TEXT,
# # #     message TEXT,
# # #     time TEXT
# # # )
# # # """)
# # # conn.commit()

# # # # Functions
# # # def add_message(name, message):
# # #     cur.execute(
# # #         "INSERT INTO messages(name, message, time) VALUES (?, ?, ?)",
# # #         (name, message, datetime.now().strftime("%H:%M:%S"))
# # #     )
# # #     conn.commit()

# # # def get_messages():
# # #     cur.execute(
# # #         "SELECT name, message, time FROM messages ORDER BY id"
# # #     )
# # #     return cur.fetchall()

# # # def clear_chat():
# # #     cur.execute("DELETE FROM messages")
# # #     conn.commit()

# # # # UI
# # # st.title("💬 Multiplayer Chat")

# # # name = st.text_input("Enter Your Name")

# # # message = st.text_input("Type Message")

# # # col1, col2 = st.columns(2)

# # # with col1:
# # #     if st.button("Send"):
# # #         if name.strip() and message.strip():
# # #             add_message(name.strip(), message.strip())
# # #             st.rerun()

# # # with col2:
# # #     if st.button("Clear Chat"):
# # #         clear_chat()
# # #         st.rerun()

# # # st.divider()

# # # st.subheader("Messages")

# # # messages = get_messages()

# # # for n, msg, t in messages:
# # #     st.write(f"**{n}** ({t})")
# # #     st.write(msg)
# # #     st.write("---")
# # import streamlit as st
# # import sqlite3
# # from datetime import datetime

# # st.set_page_config(page_title="Anonymous Chat", page_icon="💬")

# # # ---------------- DATABASE ----------------

# # conn = sqlite3.connect("chat.db", check_same_thread=False)
# # cur = conn.cursor()

# # cur.execute("""
# # CREATE TABLE IF NOT EXISTS messages(
# #     id INTEGER PRIMARY KEY AUTOINCREMENT,
# #     message TEXT,
# #     time TEXT
# # )
# # """)
# # conn.commit()

# # # ---------------- FUNCTIONS ----------------

# # def send_message(msg):
# #     cur.execute(
# #         "INSERT INTO messages(message, time) VALUES(?, ?)",
# #         (msg, datetime.now().strftime("%H:%M:%S"))
# #     )
# #     conn.commit()

# # def get_messages():
# #     cur.execute(
# #         "SELECT message, time FROM messages ORDER BY id"
# #     )
# #     return cur.fetchall()

# # def clear_chat():
# #     cur.execute("DELETE FROM messages")
# #     conn.commit()

# # # ---------------- UI ----------------

# # st.title("💬 Anonymous Chat")

# # st.markdown("""
# # <style>
# # .chat-bubble {
# #     background-color: #2b313e;
# #     padding: 10px;
# #     border-radius: 12px;
# #     margin-bottom: 8px;
# # }
# # .time {
# #     font-size: 12px;
# #     color: gray;
# # }
# # </style>
# # """, unsafe_allow_html=True)

# # message = st.chat_input("Type a message...")

# # if message:
# #     send_message(message)
# #     st.rerun()

# # messages = get_messages()

# # for msg, t in messages:
# #     st.markdown(
# #         f"""
# #         <div class="chat-bubble">
# #             {msg}
# #             <div class="time">{t}</div>
# #         </div>
# #         """,
# #         unsafe_allow_html=True
# #     )

# # st.divider()

# # if st.button("🗑️ Clear Chat"):
# import streamlit as st
# import sqlite3
# from datetime import datetime

# st.set_page_config(
#     page_title="Anonymous Chat",
#     page_icon="💬",
#     layout="centered"
# )

# # ---------------- DATABASE ----------------

# conn = sqlite3.connect("chat.db", check_same_thread=False)
# cur = conn.cursor()

# cur.execute("""
# CREATE TABLE IF NOT EXISTS messages(
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     message TEXT NOT NULL,
#     time TEXT NOT NULL
# )
# """)
# conn.commit()

# # ---------------- FUNCTIONS ----------------

# def send_message(message):
#     cur.execute(
#         "INSERT INTO messages(message, time) VALUES(?, ?)",
#         (message, datetime.now().strftime("%H:%M:%S"))
#     )
#     conn.commit()

# def get_messages():
#     cur.execute(
#         "SELECT id, message, time FROM messages ORDER BY id DESC"
#     )
#     return cur.fetchall()

# def delete_message(msg_id):
#     cur.execute(
#         "DELETE FROM messages WHERE id=?",
#         (msg_id,)
#     )
#     conn.commit()

# def clear_chat():
#     cur.execute("DELETE FROM messages")
#     conn.commit()

# # ---------------- STYLES ----------------

# st.markdown("""
# <style>
# .chat-bubble {
#     background-color: #2b313e;
#     padding: 12px;
#     border-radius: 15px;
#     margin-bottom: 8px;
#     word-wrap: break-word;
# }

# .msg-time {
#     color: gray;
#     font-size: 11px;
#     margin-top: 4px;
# }
# </style>
# """, unsafe_allow_html=True)

# # ---------------- HEADER ----------------

# st.title("💬 Prendsgram Inspired by Future Google CEO Murala Sai Ganesh")

# # ---------------- MESSAGE INPUT ----------------

# message = st.chat_input("Type a message...")

# if message:
#     send_message(message)
#     st.rerun()

# # ---------------- CHAT AREA ----------------

# messages = get_messages()

# for msg_id, msg, t in messages:

#     col1, col2 = st.columns([9, 1])

#     with col1:
#         st.markdown(
#             f"""
#             <div class="chat-bubble">
#                 {msg}
#                 <div class="msg-time">{t}</div>
#             </div>
#             """,
#             unsafe_allow_html=True
#         )

#     with col2:
#         if st.button("🗑️", key=f"delete_{msg_id}"):
#             delete_message(msg_id)
#             st.rerun()

# # ---------------- FOOTER ----------------

# st.divider()

# if st.button("🧹 Clear Entire Chat"):
#     clear_chat()
#     st.rerun()

# st.caption("Anonymous shared chat room")
# #     clear_chat()
# #     st.rerun()
import streamlit as st
import sqlite3
import random
from datetime import datetime

st.set_page_config(
    page_title="Anonymous Chat + Tic Tac Toe",
    page_icon="💬",
    layout="wide"
)

# ================= DATABASE =================

conn = sqlite3.connect("chat.db", check_same_thread=False)
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS messages(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    message TEXT,
    time TEXT
)
""")
conn.commit()

# ================= CHAT FUNCTIONS =================

def send_message(msg):
    cur.execute(
        "INSERT INTO messages(message,time) VALUES(?,?)",
        (msg, datetime.now().strftime("%H:%M:%S"))
    )
    conn.commit()

def get_messages():
    cur.execute(
        "SELECT id,message,time FROM messages ORDER BY id DESC"
    )
    return cur.fetchall()

def delete_message(msg_id):
    cur.execute(
        "DELETE FROM messages WHERE id=?",
        (msg_id,)
    )
    conn.commit()

# ================= TIC TAC TOE =================

if "board" not in st.session_state:
    st.session_state.board = [""] * 9

if "game_over" not in st.session_state:
    st.session_state.game_over = False

if "symbol" not in st.session_state:
    st.session_state.symbol = "X"

if "computer" not in st.session_state:
    st.session_state.computer = "O"

def reset_game():
    st.session_state.board = [""] * 9
    st.session_state.game_over = False

def winner(board, sym):
    wins = [
        [0,1,2],
        [3,4,5],
        [6,7,8],
        [0,3,6],
        [1,4,7],
        [2,5,8],
        [0,4,8],
        [2,4,6]
    ]

    for w in wins:
        if (
            board[w[0]] == sym and
            board[w[1]] == sym and
            board[w[2]] == sym
        ):
            return True

    return False

def board_full(board):
    return "" not in board

def computer_move():

    empty = []

    for i in range(9):
        if st.session_state.board[i] == "":
            empty.append(i)

    if empty:
        move = random.choice(empty)
        st.session_state.board[move] = st.session_state.computer

# ================= STYLE =================

st.markdown("""
<style>
.chat-box{
    background:#2b313e;
    padding:12px;
    border-radius:12px;
    margin-bottom:8px;
}
.small{
    color:gray;
    font-size:11px;
}
</style>
""", unsafe_allow_html=True)

# ================= LAYOUT =================

left, right = st.columns([3,1])

# ================= LEFT SIDE CHAT =================

with left:

    st.title("💬 Anonymous Chat")

    msg = st.chat_input("Type a message...")

    if msg:
        send_message(msg)
        st.rerun()

    messages = get_messages()

    for msg_id, message, t in messages:

        c1, c2 = st.columns([9,1])

        with c1:
            st.markdown(
                f"""
                <div class="chat-box">
                {message}
                <div class="small">{t}</div>
                </div>
                """,
                unsafe_allow_html=True
            )

        with c2:
            if st.button("🗑️", key=f"d{msg_id}"):
                delete_message(msg_id)
                st.rerun()

# ================= RIGHT SIDE GAME =================

with right:

    st.subheader("🎮 Feeling Bore?")
    st.write("Play Tic Tac Toe")

    symbol = st.radio(
        "Choose Symbol",
        ["X", "O"],
        key="choose_symbol"
    )

    st.session_state.symbol = symbol
    st.session_state.computer = (
        "O" if symbol == "X" else "X"
    )

    board = st.session_state.board

    for row in range(3):

        cols = st.columns(3)

        for col in range(3):

            idx = row * 3 + col

            text = board[idx] if board[idx] != "" else " "

            if cols[col].button(
                text,
                key=f"cell_{idx}",
                use_container_width=True
            ):

                if (
                    board[idx] == ""
                    and not st.session_state.game_over
                ):

                    board[idx] = st.session_state.symbol

                    if winner(
                        board,
                        st.session_state.symbol
                    ):
                        st.session_state.game_over = True

                    elif not board_full(board):

                        computer_move()

                        if winner(
                            board,
                            st.session_state.computer
                        ):
                            st.session_state.game_over = True

                    st.rerun()

    if winner(board, st.session_state.symbol):
        st.success("🏆 You Won!")

    elif winner(board, st.session_state.computer):
        st.error("💀 Computer Won!")

    elif board_full(board):
        st.info("🤝 Draw!")

    if st.button("🔄 New Game"):
        reset_game()
        st.rerun()
