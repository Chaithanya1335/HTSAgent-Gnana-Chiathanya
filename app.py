import streamlit as st
from src.Agent.agent import Agent

st.set_page_config(page_title="HTS Multi-Tool Agent", layout="wide")
st.title("🧠 HTS Multi-Tool Agent")

st.markdown("""
Welcome to the **HTS Multi-Tool Agent**!  
You can:

- 📄 Ask trade-related questions (from General Notes)
- 📊 Calculate HTS tariff duties

---

### 🔤 Input Instructions

#### To Ask a Trade Question:
👉 *Example:*  
`What is the United States-Israel Free Trade Agreement?`

#### To Calculate Tariff Duty:
👉 *Provide input in this format:*  
            **example**:
                "HTS:0101.30.00.00; cost:10000; freight:500; insurance:100; weight:500; qty:5" in a single line
    
        📝 **Input Field Guide**:
        - `HTS`: Harmonized Tariff Schedule code (e.g., 0101.30.00.00)
        - `cost`: Product cost in USD (e.g., 10000)
        - `freight`: Freight cost in USD (e.g., 500)
        - `insurance`: Insurance cost in USD (e.g., 100)
        - `weight`: Total weight of the goods in kilograms (e.g., 500)
        - `qty`: Total quantity of units (e.g., 5)

     """)

with st.container(height=300):
    # Session state
    if 'messages' not in st.session_state:
        st.session_state.messages = [{'bot': "Hi, how can I help you!"}]

    # Show chat history
    for message in st.session_state.messages:
        if 'bot' in message:
            st.markdown(f"**🤖 Bot:** {message['bot']}")
        else:
            st.markdown(f"**🙋 User:** {message['user']}")

# Agent

agent = Agent().initialize_agent()



# Input
user_input = st.text_input("📝 Enter your query here:")
submit = st.button("🔍 Submit")

if submit and user_input:
    with st.spinner("🔍 Processing your request..."):
        try:
            st.session_state.messages.append({'user': user_input})
            result = agent.run(user_input)
            st.session_state.messages.append({'bot': result})
            st.rerun()
        except Exception as e:
            st.error(f"❌ Error: {str(e)}")
