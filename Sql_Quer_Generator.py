import streamlit as st
import google.generativeai as genai

GOOGLE_API_KEY = "INSERT_YOUR_API_KEY_HERE"

genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-pro')


def main():
    st.set_page_config(layout="wide", page_title="SQL Query Generator")
    st.markdown(
        """
        <div style="text-align: center;">

        <h1 style="color: #000000;">SQL Query Generator</h1>
        <h3> I can help you generate SQL queries! </h3>  
        <P>This tool is built with Streamlit, which is a web application that allows you to easily generate SQL queries</P>        

        </div>
        """,
        unsafe_allow_html=True,
    )

    text_input = st.text_area("Enter your query here in English:")

    submit = st.button("Generate SQL Query")
    if submit:
        with st.spinner("Generating SQL Query..."):
            template = """
            Create a SQL query snippet from the following text:
            ```
            {text_input}
            ```
            I just want a SQL query

            """
            formatted_template = template.format(text_input=text_input)
            response = model.generate_content(formatted_template)
            sql_query = response.text
            # st.write(sql_query)

            expected_output = """
            What Would be the expected response of this SQL query snippet:
            ```
            {sql_query}
            ```
            provide simple tabluar response with no explanation
            """
            formatted_expected_output = expected_output.format(sql_query=sql_query)
            eoutput = model.generate_content(formatted_expected_output)
            eoutput = eoutput.text
            # st.write(eoutput)

            explantion = """
            Explain This query snippet:
            ```
            {sql_query}
            ```
            please provide with simple explanation of the query:
            """
            explantion_formatted = explantion.format(sql_query=sql_query)
            expl = model.generate_content(explantion_formatted)
            expl = expl.text
            # st.write(expl)

            with st.container() :
                st.success("SQL Query Generated Successfully! Here is the SQL Query: ")
                st.code(sql_query, language="sql")

                st.success("Expected Output of this SQL query snippet: ")
                st.code(eoutput, language="sql")

                st.success("Explanation of this SQL query snippet: ")
                st.code(expl, language="sql")
main()