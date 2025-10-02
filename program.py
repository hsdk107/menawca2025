import streamlit as st

chart_data = st.session_state.chart_data
st.header("Conference Program")

day1, day2, day3 = st.tabs(["**Friday October 10**", "**Saturday, October 11**", "**Sunday, October 12**"])
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# ******************* FRIDAY SCHEDULE *******************************
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

with day1:
  st.header("Day 1: Friday October 10, 2025")
  st.markdown("<hr style='margin:0;'>",unsafe_allow_html=True)
  # *****************************************************************************************************
  col0, col1 = st.columns([2,5],gap="small")
  with col0:
    st.write("9:00 - 10:00am")
  with col1:
    st.write("**Breakfast & Registration**")
    st.write("Outside Blue Hall, Arts Center (C3)")
    st.write("*Registration will continue past this time if needed at the Library Entrance (C2)*")
  st.markdown("<hr style='margin:0;'>",unsafe_allow_html=True)
  # *****************************************************************************************************
  col0, col1 = st.columns([2,5],gap="small")
  with col0:
    st.write("10:00am - 12:00pm")
  with col1:
    st.write("**Opening Ceremony**")
    st.write("Outside Blue Hall, Arts Center (C3)")
  st.markdown("<hr style='width:75%;margin:auto;'>",unsafe_allow_html=True)
  col0, col1 = st.columns([2,5],gap="small")
  with col0:
    st.markdown('<div style="text-align: right;">10:00-10:15am</div>', unsafe_allow_html=True)
  with col1:
    st.write("Awam Amkpa")
  col0, col1 = st.columns([2,5],gap="small")
  with col0:
    st.markdown('<div style="text-align: right;">10:15-11:15am</div>', unsafe_allow_html=True)
  with col1:
    st.write("Keynote Speaker: Annette Vee")
  col0, col1 = st.columns([2,5],gap="small")
  with col0:
    st.markdown('<div style="text-align: right;">11:15-11:45am</div>', unsafe_allow_html=True)
  with col1:
    st.write("Local Speaker: Marion Wrenn")
  col0, col1 = st.columns([2,5],gap="small")
  with col0:
    st.markdown('<div style="text-align: right;">11:45am-12:00pm</div>', unsafe_allow_html=True)
  with col1:
    st.write("Provost's Welcome Address")
  st.markdown("<hr style='margin:0;'>",unsafe_allow_html=True)
  # *****************************************************************************************************
  col0, col1 = st.columns([2,5],gap="small")
  with col0:
    st.write("12:00 - 2:30pm")
  with col1:
    st.write("**Lunch and Prayer Break**")
    st.write("Torch Club (D2)")
    st.write("*Prayer Rooms in C2 Ground Floor*")
  st.markdown("<hr style='margin:0;'>",unsafe_allow_html=True)
  # *****************************************************************************************************
  col0, col1 = st.columns([2,5],gap="small")
  with col0:
    st.write("2:30 - 5:30pm")
  with col1:
    st.write("**Policy, Voice and Agency**")
    st.write("Campus Center (C2) Level 3, Library, Breakout Rooms")
  st.markdown("<hr style='margin:0;'>",unsafe_allow_html=True)
  with st.expander("Parallel Sessions"):
    # *****************************************************************************************************
    col0, col1, col2 = st.columns([1,2,2],gap="small")
    with col0:
      st.write("Room")
    with col1:
      st.write("TBD") #st.error("TBD")
    with col2:
      st.write("TBD") #st.error("TBD")
    st.markdown("<hr style='margin:0;'>",unsafe_allow_html=True)
    # *****************************************************************************************************
    col0, col1, col2 = st.columns([1,2,2],gap="small")
    with col0:
      st.write(" ")
    with col1:
      st.write("**Policy & AI**")
    with col2:
      st.write("**Student Voice, Agency & AI**")
    st.markdown("<hr style='margin:0;'>",unsafe_allow_html=True)
    col0, col1, col2 = st.columns([1,2,2],gap="small")
    with col0:
      st.write("2:30-3:10pm")
      #st.markdown('<div style="text-align: right;">2:30-3:10pm</div>', unsafe_allow_html=True)
    with col1:
      st.write("*The Right of Refusal: Embodying Writing Center Expertise in the Age of AI*")
      st.write("Kelly Wilson")
    with col2:
      st.write("*Developing Student Voice Through AI Literacy*")
      st.write("Thuraya Sulaiman")
    st.markdown("<hr style='margin:0;'>",unsafe_allow_html=True)
    col0, col1, col2 = st.columns([1,2,2],gap="small")
    with col0:
      st.write("3:15-3:55pm")
      #st.markdown('<div style="text-align: right;">3:15-3:55pm</div>', unsafe_allow_html=True)
    with col1:
      st.write("*Transparent Practices: Acknowledging AI in Academic Assignments* (Roundtable)")
      st.write("Owen Connor & Luleadey Worku")
    with col2:
      st.write("*Helping Students Choose Tools at AI's Jagged Edge*")
      st.write("Kate Koppy")
    st.markdown("<hr style='margin:0;'>",unsafe_allow_html=True)
    col0, col1, col2 = st.columns([1,2,2],gap="small")
    with col0:
      st.write("4:00-4:40pm")
      #st.markdown('<div style="text-align: right;">4:00-4:40pm</div>', unsafe_allow_html=True)
    with col1:
      st.write("*Principles and Practices for Teaching Critical AI Literacy*")
      st.write("J. Palmeri")
    with col2:
      st.write("*Text-to-Speech or Speech-to-Text? Preserving Voice and Agency in AI Co-Creation*")
      st.write("Sweta Kumari & Aieshah Arif")
    st.markdown("<hr style='margin:0;'>",unsafe_allow_html=True)
    col0, col1, col2 = st.columns([1,2,2],gap="small")
    with col0:
      st.write("4:45-5:25pm")
      #st.markdown('<div style="text-align: right;">4:45-5:25pm</div>', unsafe_allow_html=True)
    with col1:
      st.write(" ")
    with col2:
      st.write("*Writing with AI: Saudi Voices, Shared Dilemmas*")
      st.write("Georgios Kormpas, Abdulrahman AlHassun, & Joud Hakeem")
    
  # *****************************************************************************************************
  col0, col1 = st.columns([2,5],gap="small")
  with col0:
    st.write("5:30 - 6:30pm")
  with col1:
    st.write("**Rest**")
  st.markdown("<hr style='margin:0;'>",unsafe_allow_html=True)
  # *****************************************************************************************************
  col0, col1 = st.columns([2,5],gap="small")
  with col0:
    st.write("6:30 - 8:30pm")
  with col1:
    st.write("**Conference Dinner**")
  st.markdown("<hr style='margin:0;'>",unsafe_allow_html=True)

  #st.table(chart_data)

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# ******************* SATURDAY SCHEDULE *******************************
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
with day2:
  st.header("Day 2: Saturday October 11 2025")
  st.table(chart_data)

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# ******************* SUNDAY SCHEDULE *******************************
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
with day3:
  st.header("Day 3: Sunday October 12 2025")
  st.table(chart_data)
