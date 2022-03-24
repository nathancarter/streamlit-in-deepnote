
##### This app is just an extremely simple example.
##### See the Streamlit documentation for how to create more complex apps.

import streamlit as st


##### Title and intro

st.title( 'Example Streamlit App' )
st.markdown( '''
This app is very small and does almost nothing.
It's just an example.
''' )


##### Controls in the sidebar

st.sidebar.header( 'Choose two numbers:' )
a = st.sidebar.slider( label='a', min_value=1, max_value=10, value=2, step=1 )
b = st.sidebar.slider( label='b', min_value=1, max_value=10, value=3, step=1 )


##### Output

st.markdown( f'''
## Output

| Expression   | Value |
|--------------|-------|
| $a$          | {a}   |
| $b$          | {b}   |
| $a+b$        | {a+b} |
| $a-b$        | {a-b} |
| $a\\times b$ | {a*b} |
| $a\\div b$   | {a/b} |
''' )
