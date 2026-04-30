import streamlit as st
from salon_agents import get_agent_response

st.set_page_config(
    page_title="LUMIERE HAIR AND BEAUTY CHAT",
    page_icon="💇",
)

st.title("LUMIERE HAIR AND BEAUTY")
st.caption("AI CHAT SUPPORT DEMO FOR PRICING, BOOKINGS, RESCHEDULING, CANCELLATIONS, AND ESCALATION")


if "messages" not in st.session_state:
    st.session_state.messages=[
        {
            "role": "assistant",
            "content": "Hi, welcome to lumiere Hair and beauty. How can i help today?",        
        }
    ]

with st.sidebar:
    st.header("Demo Notes")
    st.write(
        "This demo uses simulated availability. Booking requests are noted, "
        "then the receptionist confirms the final appointment."    
    )
    if st.button("Clear Chat"):
        st.session_state.messages=[
            {
                "role": "assistant",
                "content": "Hi, welcome to Lumiere Hair & Beauty. How can I help today?",

            }
        ]
        st.rerun()

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

user_message = st.chat_input("Message Lumi")

if user_message:
    st.session_state.messages.append({"role": "user", "content": user_message})

    with st.chat_message("user"):
        st.markdown(user_message)
    with st.chat_message("assisant"):
        with st.spinner("Lummi is typing"):
            assistant_message = get_agent_response(st.session_state.messages)
            st.markdown(assistant_message)

        st.session_state.messages.append(
            {"role": "assistant", "content": assistant_message}
        )