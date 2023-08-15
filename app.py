import streamlit as st

def main():
    st.title("Find maximum of three numbers : ")
    
    num1 = st.number_input("Enter the first number:", value=0)
    num2 = st.number_input("Enter the second number:", value=0)
    num3 = st.number_input("Enter the third number:", value=0)

    numbers = [num1, num2, num3]

    if st.button("Submit"):
        st.write("Maximum:", max(numbers))

if __name__ == "__main__":
    main()
