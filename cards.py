import streamlit as st

def widgets_card():
    st.page_link("widgets.py", label="Widgets", icon=":material/widgets:")
    st.text_input("Text input")
    inner_cols = st.columns(2)
    inner_cols[0].pills("Pills", options=["A", "B", "C"], default="A")
    inner_cols[1].segmented_control("Segmented control", options=["A", "B", "C"], default="A")
    inner_cols = st.columns([79,97,55])
    inner_cols[0].button("Primary", type="primary")
    inner_cols[1].button("Secondary")
    inner_cols[2].button("Tertiary", type="tertiary")

def dataframe_card():
    st.page_link("data.py", label="Data", icon=":material/table:")
    st.dataframe(st.session_state.chart_data, height=220)

def layouts_card():
    st.page_link("layouts.py", label="Layouts", icon=":material/dashboard:")
    a,b,c = st.tabs(["Tab A", "Tab B", "Tab C"])
    a.write("Tab A content")
    b.write("Tab B content")
    c.write("Tab C content")
    st.expander("Expander").write("Expander content")
    st.popover("Popover", icon=":material/info:").write("Popover content")
