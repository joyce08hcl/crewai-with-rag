import streamlit as st
import re
import os
import subprocess
import tempfile
from streamlit_monaco import st_monaco
from code_editor import code_editor

st.set_page_config(layout="wide")
st.markdown("<h2 style='text-align: center;'>Diagrams as Code</h2>", unsafe_allow_html=True)


with st.container():
    st.write("Enter your input:")
    user_input = st.text_area("", height=100, key="user_input")
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
    result = """
            The provided code is valid and does not require any changes.
```
    
vars: {
    d2-config: {
        layout-engine: elk
        theme-id: 300
    }
    }

    network: {
    Frontend Service: {region: "A"}
    API Gateway: {region: "A"}
    Microservice 1: Data Storage: {region: "A"}
    Microservice 2: Message Publisher: {region: "A"}
    SNS Topic: {region: "A"}
    AWS Lambda Function: {region: "B"}
    DynamoDB Table: {region: "B"}
    S3 Bucket: {region: "A"}
    Redis Cache: {region: "B"}

    Frontend Service -> API Gateway: send requests
    API Gateway -> Microservice 1: store data
    API Gateway -> Microservice 2: publish messages
    Microservice 1 -> DynamoDB Table: store data
    Microservice 2 -> SNS Topic: publish messages
    SNS Topic -> AWS Lambda Function: trigger
    AWS Lambda Function -> DynamoDB Table: update data
    Frontend Service -> S3 Bucket: retrieve static content
    Frontend Service -> Redis Cache: store session information
    }
```
    The code is correct and adheres to the D2 language syntax and standards.
    """
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
        # code_area_placeholder.text_area("Generated code", value=st.session_state["generated_code"], height=400)
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
            # if st.button("Get content"):
            #     st.markdown(f"```javascript{content}")
        # if st.button("Show editor's content"):
        #     content = st.session_state["generated_code"]
        #     st.write(content)
        
        # Generate the diagram and get the path to the SVG file
            svg_path = generate_diagram(code)

            print(svg_path)
            
            # Display the SVG image
            
        with right_col:
            st.image("network.svg", use_column_width=True)
            st.download_button(
                label="Download Image",
                file_name="download.PNG",
                data= "network.svg"
            )