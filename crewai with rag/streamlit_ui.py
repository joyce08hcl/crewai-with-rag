import streamlit as st
import subprocess
import tempfile
import os
import re
from crewai import Crew
from tasks import tasks_func
from config import d2_examples, diagram_language
from agents import agents_func
from crew import crew_func
from code_editor import code_editor
from streamlit_monaco import st_monaco

st.set_page_config(layout="wide")
st.markdown("<h2 style='text-align: center;'>Diagrams as Code</h2>", unsafe_allow_html=True)

if "user_input" not in st.session_state:
    st.session_state.user_input = ""

def update_user_input():
    st.session_state.user_input = st.session_state.user_input_value
    

with st.container():
    st.write("Enter your input:")
    st.text_area("", height=100, key="user_input_value", value=st.session_state.user_input, on_change=update_user_input)
    user_input = st.session_state.user_input 
    st.write("")
    button_col = st.columns([4, 3, 3])
    with button_col[1]:
        generate_button = st.button("Generate Diagram")


left_col, right_col = st.columns([4, 4])
with left_col:
    code_area_placeholder = st.empty()
with right_col:
    diagram_container = st.container()
    

def generate_diagram(code):
    # Create a temporary file for the D2 code
    temp_d2_path = os.path.join(tempfile.gettempdir(), "network.d2")
    temp_svg_path = os.path.join(tempfile.gettempdir(), "network.svg")

    # Write the code to the temporary file
    with open(temp_d2_path, "w") as f:
        f.write(code)
        
    # Generate the SVG using the temporary D2 file
    os.system(f"d2 {temp_d2_path} {temp_svg_path}")

    return temp_svg_path



if generate_button:
    architect, coder, validator = agents_func()
    task1, task2, task3 = tasks_func(user_input, d2_examples, diagram_language, architect, coder, validator)
    result = crew_func(architect, coder, validator, task1, task2, task3)
    print("\n\n\n\nThis is the result\n\n\n\n\n", str(result))


    pattern = r"```([\s\S]*?)```"
    match = re.search(pattern, str(result))
    if match:
        code = match.group(1).strip()
        print(code)
        
        # Save the code to session state
        st.session_state["generated_code"] = code
        st.session_state["generated_code_file"] = os.path.join(tempfile.gettempdir(), "generated_code.txt")
        with open(st.session_state["generated_code_file"], "w") as file:
            file.write(code)
        
        # Update the value of the text area
        # with code_area_placeholder:
        #     code_editor(st.session_state["generated_code"],height = [19, 22])
        # if st.button("Show editor's content"):
        #     st.write(content)
        # response_dict = code_area_placeholder.code_editor(code)

        editor_btns = [{
            "name": "copy",
            "feather": "Copy",
            "hasText": True,
            "alwaysOn": True,
            "commands": ["copyAll"],
            "style": {"top": "0rem", "right": "0.4rem"}
        }]
        with code_area_placeholder:
            response_dict = code_editor(st.session_state["generated_code"],height = [19, 22], shortcuts="vscode", options={"wrap": True}, buttons=editor_btns)
        if len(response_dict['id']) != 0 and ( response_dict['type'] == "selection" or response_dict['type'] == "submit" ):
            st.write(response_dict)

        

        
        
        # Generate the diagram and get the path to the SVG file
        svg_path = generate_diagram(code)

        print(svg_path)
        
        # Display the SVG image
        
        with right_col:
            st.image(svg_path, use_column_width=True)

            st.download_button(
                label="Download Image",
                file_name="download.PNG",
                data= "network.svg"
            )

