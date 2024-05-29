import streamlit as st
import pandas as pd

# Load the sample DataFrame
df = pd.read_csv('NVD.csv')

# Function to display the home page
def show_home():
    st.title("Home Page")
    st.write("Click the button to view the first 5 rows and columns.")
    
    if st.button("Show Data"):
        st.session_state.page = "output"

# Function to display the output page with the first 5 rows and columns
def show_output():
    st.title("Output Page")
    st.write("First 5 rows and first 5 columns of the DataFrame:")
    st.dataframe(df.iloc[:5, :5])

    # Allow users to select a row to view more details
    selected_row = st.selectbox("Select a row to view more details", df.head().index)
    
    if st.button("Show Details"):
        st.session_state.selected_row = selected_row
        st.session_state.page = "details"
        
    if st.button("Back"):
        st.session_state.page = "home"

# Function to display more details about the selected row
def show_details():
    st.title("Details Page")
    
    if "selected_row" in st.session_state:
        selected_row = st.session_state.selected_row
        st.write(f"Details of row {selected_row}:")
        st.write(df.iloc[selected_row])

    if st.button("Back"):
        st.session_state.page = "output"

# Main function to control the navigation
def main():
    if "page" not in st.session_state:
        st.session_state.page = "home"
    if "selected_row" not in st.session_state:
        st.session_state.selected_row = None

    if st.session_state.page == "home":
        show_home()
    elif st.session_state.page == "output":
        show_output()
    elif st.session_state.page == "details":
        show_details()

if __name__ == "__main__":
    main()
