import streamlit as st

# Initialize chat messages in session state if not already present
if "messages" not in st.session_state:
    st.session_state.messages = []

# Function to add messages to the chat
def add_message(role, content):
    st.session_state.messages.append({"role": role, "content": content})

# Display the chat interface header
st.markdown("<h1 style='text-align: center; color: #aaa;'>Chat Interface</h1>", unsafe_allow_html=True)

# Chat message display loop
for message in st.session_state.messages:
    role = message['role']
    # Use a placeholder for avatar if needed, replace None with the URL if you have one
    avatar_url = None if role == "user" else "https://path/to/your/avatar/image.jpg"
    with st.chat_message(role, avatar=avatar_url):
        st.markdown(message["content"])

# User input for the chat
user_input = st.text_input("Enter your question:", key="chat_input")
if st.button("Send"):
    if user_input:  # Check if the input is not empty
        add_message("user", user_input)
        # Here you would typically process the input and generate a response
        # For demonstration, let's simulate a simple echo response
        simulated_response = f"You said: {user_input}"
        add_message("assistant", simulated_response)
