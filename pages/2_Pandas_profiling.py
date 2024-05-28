import ydata_profiling
import streamlit as st
from streamlit_ydata_profiling import st_profile_report

st.set_page_config(page_title="Homepage", layout="wide")

pr = st.session_state["df"].profile_report(minimal=True)

# TODO cache doesn't work on profiling output -> workaround?
st.cache_resource
st_profile_report(pr)
