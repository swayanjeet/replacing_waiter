from typing import TypedDict, List, Annotated

# This dictionary will act as our simple, in-memory database for orders.
# In a real application, this would be a database.
order_database = {}

menu = {
            "Appetizers": {
                "Chicken Malai Tikka": {
                    "spanish_name": "Chicken Malai Tikka",
                    "price_cop": 26500,
                    "price_inr": 556.5,
                    "description": "Succulent, boneless chicken pieces marinated in a creamy blend of yogurt, cheese, and mild spices, then grilled to perfection in the tandoor. 🍗"
                },
                "Vegetable Samosa": {
                    "spanish_name": "Vegetable Samosa",
                    "price_cop": 22500,
                    "price_inr": 472.5,
                    "description": "A classic! Crispy, golden-fried pastry filled with a savory mixture of spiced potatoes and green peas. Served with tangy tamarind sauce."
                },
                "Lamb Samosa": {
                    "spanish_name": "Lamb Samosa",
                    "price_cop": 28200,
                    "price_inr": 592.2,
                    "description": "A hearty twist on the classic samosa, stuffed with flavorful spiced minced lamb, onions, and herbs."
                },
                "Chicken Samosa": {
                    "spanish_name": "Chicken Samosa",
                    "price_cop": 26000,
                    "price_inr": 546,
                    "description": "Tender minced chicken seasoned with aromatic spices, perfectly sealed in a crispy, flaky pastry shell."
                },
                "Chicken Tikka": {
                    "spanish_name": "Chicken Tikka",
                    "price_cop": 26500,
                    "price_inr": 556.5,
                    "description": "Smoky and tender boneless chicken marinated in yogurt and a vibrant blend of Indian spices, then chargrilled in our traditional tandoor oven."
                },
                "Tandoori Chicken": {
                    "spanish_name": "Tandoori Chicken",
                    "price_cop": 26500,
                    "price_inr": 556.5,
                    "description": "The king of kebabs! A whole chicken marinated overnight in yogurt and our signature tandoori masala, then roasted to juicy perfection."
                },
                "Pankhuri Chicken": {
                    "spanish_name": "Pankhuri Chicken",
                    "price_cop": 24500,
                    "price_inr": 514.5,
                    "description": "Delicate, petal-like cuts of chicken marinated in a special house blend of spices and cooked to a tender, flavorful finish."
                },
                "Paneer Tikka": {
                    "spanish_name": "Paneer Tikka",
                    "price_cop": 23800,
                    "price_inr": 499.8,
                    "description": "Cubes of fresh Indian cheese, bell peppers, and onions marinated in spices and grilled on skewers for a smoky, vegetarian delight. 🧀"
                },
                "Onion Bhajia": {
                    "spanish_name": "Onion Bhajia",
                    "price_cop": 20700,
                    "price_inr": 434.7,
                    "description": "Crispy and addictive fritters made from spiced onion slices, coated in a seasoned chickpea flour batter and deep-fried."
                },
                "Lamb Seekh Kabab": {
                    "spanish_name": "Lamb Seekh Kabab",
                    "price_cop": 28800,
                    "price_inr": 604.8,
                    "description": "Spiced minced lamb mixed with ginger, garlic, and fresh herbs, molded onto skewers and grilled in the tandoor."
                },
                "Tikaa Bombs": {
                    "spanish_name": "Tikaa Bombs",
                    "price_cop": 26900,
                    "price_inr": 564.9,
                    "description": "A modern, explosive twist on a classic! Bite-sized flavor bombs that burst with a zesty, spicy filling. An exciting start to your meal! 💥"
                },
                "Hara Bahara Kabab": {
                    "spanish_name": "Hará Bahara Kabab",
                    "price_cop": 20700,
                    "price_inr": 434.7,
                    "description": "Healthy and delicious pan-fried patties made from a blend of spinach, green peas, potatoes, and aromatic spices."
                },
                "Fish Amritsari": {
                    "spanish_name": "Fish Amritsari",
                    "price_cop": 29500,
                    "price_inr": 619.5,
                    "description": "A famous street food delicacy from Amritsar. Tender fish chunks marinated in spices, battered, and fried to a perfect crisp. 🐟"
                },
                "Fish Tikka": {
                    "spanish_name": "Fish Tikka",
                    "price_cop": 30500,
                    "price_inr": 640.5,
                    "description": "Soft cubes of fresh fish marinated in yogurt and a special blend of ajwain (carom seeds) and spices, then gently cooked in the tandoor."
                },
                "Paneer Kathi Roll": {
                    "spanish_name": "Paneer Kathi Roll",
                    "price_cop": 29500,
                    "price_inr": 619.5,
                    "description": "A popular Indian street food wrap. Spiced paneer tikka, crunchy onions, and tangy sauces rolled into a warm, flaky paratha bread."
                },
                "Chicken Kathi Roll": {
                    "spanish_name": "Chicken Kathi Roll",
                    "price_cop": 32000,
                    "price_inr": 672,
                    "description": "Juicy chicken tikka pieces, sautéed peppers, and onions drizzled with mint chutney and wrapped in a soft, freshly made paratha."
                },
                "Prawn Tandoori": {
                    "spanish_name": "Prawn Tandoori",
                    "price_cop": 32800,
                    "price_inr": 688.8,
                    "description": "Jumbo prawns marinated in a classic tandoori spice blend and grilled to bring out their sweet flavor and smoky aroma. 🍤"
                },
                "Chicken Lollypop": {
                    "spanish_name": "Chicken Lollypop",
                    "price_cop": 26800,
                    "price_inr": 562.8,
                    "description": "A fun and flavorful Indo-Chinese appetizer. Frenched chicken winglets are marinated in a spicy sauce and deep-fried until crisp."
                },
            },
            "Sides": {
                "Basmati Rice": {
                    "spanish_name": "Arroz Basmati",
                    "price_cop": 19000,
                    "price_inr": 399,
                    "description": "Premium, long-grain Basmati rice, steamed to fluffy perfection. The perfect companion to any curry. 🍚"
                },
                "Raita": {
                    "spanish_name": "Raita",
                    "price_cop": 8000,
                    "price_inr": 168,
                    "description": "A cooling and refreshing yogurt dip mixed with finely chopped cucumber, mint, and a sprinkle of roasted cumin."
                },
                "Jeera Rice": {
                    "spanish_name": "Jeera Rice",
                    "price_cop": 19500,
                    "price_inr": 409.5,
                    "description": "Aromatic Basmati rice tempered with ghee, cumin seeds (jeera), and fresh coriander for a simple yet flavorful side."
                },
                "Onion Salad": {
                    "spanish_name": "Ensalada Cebolla",
                    "price_cop": 8000,
                    "price_inr": 168,
                    "description": "A simple, traditional Indian salad of thinly sliced onions, seasoned with lemon juice, salt, and chili."
                },
                "Mixed Salad": {
                    "spanish_name": "Ensalada Mixta",
                    "price_cop": 8000,
                    "price_inr": 168,
                    "description": "A fresh mix of crisp garden greens, cucumber, tomatoes, and carrots with a light dressing."
                },
                "Tamarind Sauce": {
                    "spanish_name": "Salas Tamarindo",
                    "price_cop": 8000,
                    "price_inr": 168,
                    "description": "A classic sweet and tangy sauce made from tamarind pulp, jaggery, and spices. Perfect for dipping."
                },
            },
            "Main Courses": {
                "Chicken Tikka Masala": {
                    "spanish_name": "Chicken Tikka Masala",
                    "price_cop": 55500,
                    "price_inr": 1165.5,
                    "description": "The world-famous dish! Char-grilled chicken tikka simmered in a rich, creamy, and mildly spiced tomato and onion gravy."
                },
                "Chicken Mughlai": {
                    "spanish_name": "Chicken Mughlai",
                    "price_cop": 53500,
                    "price_inr": 1123.5,
                    "description": "A royal and decadent curry made with tender chicken in a creamy sauce of cashews, almonds, and aromatic spices."
                },
            },
            "Desserts": {
                "Gulab Jamun": {
                    "spanish_name": "Gulab Jamun",
                    "price_cop": 20500,
                    "price_inr": 430.5,
                    "description": "A sweet ending. Soft, melt-in-your-mouth milk-solid balls, deep-fried and soaked in a fragrant rose and cardamom-flavored sugar syrup."
                }
            }
        }

class AgentState(TypedDict):
    """Represents the state of our agent."""
    messages: Annotated[List[dict], lambda x, y: x + y]
    table_number: int | None
    order_list: List[str]

from langchain_core.tools import tool

@tool
def take_order(table_number: int, items: List[str]) -> str:
    """
    Takes an order for a specific table and adds items.
    Updates the order if one for the table already exists.
    """
    if table_number not in order_database:
        order_database[table_number] = []
    
    order_database[table_number].extend(items)
    return f"Successfully added {', '.join(items)} to the order for table {table_number}. The current order is: {', '.join(order_database[table_number])}."

@tool
def view_order(table_number: int) -> str:
    """Views the current order for a given table."""
    if table_number in order_database and order_database[table_number]:
        return f"Current order for table {table_number}: {', '.join(order_database[table_number])}."
    return f"There is no order for table {table_number} yet."

@tool
def view_menu() -> str:
    """
    Allows to view the menu items to confirm the prices and if anymore clarification is required. The price is in COP.
        menu = {
            "Appetizers": {
                "Chicken Malai Tikka": {
                    "spanish_name": "Chicken Malai Tikka",
                    "price_cop": 26500,
                    "price_inr": 556.5,
                    "description": "Succulent, boneless chicken pieces marinated in a creamy blend of yogurt, cheese, and mild spices, then grilled to perfection in the tandoor. 🍗"
                },
                "Vegetable Samosa": {
                    "spanish_name": "Vegetable Samosa",
                    "price_cop": 22500,
                    "price_inr": 472.5,
                    "description": "A classic! Crispy, golden-fried pastry filled with a savory mixture of spiced potatoes and green peas. Served with tangy tamarind sauce."
                },
                "Lamb Samosa": {
                    "spanish_name": "Lamb Samosa",
                    "price_cop": 28200,
                    "price_inr": 592.2,
                    "description": "A hearty twist on the classic samosa, stuffed with flavorful spiced minced lamb, onions, and herbs."
                },
                "Chicken Samosa": {
                    "spanish_name": "Chicken Samosa",
                    "price_cop": 26000,
                    "price_inr": 546,
                    "description": "Tender minced chicken seasoned with aromatic spices, perfectly sealed in a crispy, flaky pastry shell."
                },
                "Chicken Tikka": {
                    "spanish_name": "Chicken Tikka",
                    "price_cop": 26500,
                    "price_inr": 556.5,
                    "description": "Smoky and tender boneless chicken marinated in yogurt and a vibrant blend of Indian spices, then chargrilled in our traditional tandoor oven."
                },
                "Tandoori Chicken": {
                    "spanish_name": "Tandoori Chicken",
                    "price_cop": 26500,
                    "price_inr": 556.5,
                    "description": "The king of kebabs! A whole chicken marinated overnight in yogurt and our signature tandoori masala, then roasted to juicy perfection."
                },
                "Pankhuri Chicken": {
                    "spanish_name": "Pankhuri Chicken",
                    "price_cop": 24500,
                    "price_inr": 514.5,
                    "description": "Delicate, petal-like cuts of chicken marinated in a special house blend of spices and cooked to a tender, flavorful finish."
                },
                "Paneer Tikka": {
                    "spanish_name": "Paneer Tikka",
                    "price_cop": 23800,
                    "price_inr": 499.8,
                    "description": "Cubes of fresh Indian cheese, bell peppers, and onions marinated in spices and grilled on skewers for a smoky, vegetarian delight. 🧀"
                },
                "Onion Bhajia": {
                    "spanish_name": "Onion Bhajia",
                    "price_cop": 20700,
                    "price_inr": 434.7,
                    "description": "Crispy and addictive fritters made from spiced onion slices, coated in a seasoned chickpea flour batter and deep-fried."
                },
                "Lamb Seekh Kabab": {
                    "spanish_name": "Lamb Seekh Kabab",
                    "price_cop": 28800,
                    "price_inr": 604.8,
                    "description": "Spiced minced lamb mixed with ginger, garlic, and fresh herbs, molded onto skewers and grilled in the tandoor."
                },
                "Tikaa Bombs": {
                    "spanish_name": "Tikaa Bombs",
                    "price_cop": 26900,
                    "price_inr": 564.9,
                    "description": "A modern, explosive twist on a classic! Bite-sized flavor bombs that burst with a zesty, spicy filling. An exciting start to your meal! 💥"
                },
                "Hara Bahara Kabab": {
                    "spanish_name": "Hará Bahara Kabab",
                    "price_cop": 20700,
                    "price_inr": 434.7,
                    "description": "Healthy and delicious pan-fried patties made from a blend of spinach, green peas, potatoes, and aromatic spices."
                },
                "Fish Amritsari": {
                    "spanish_name": "Fish Amritsari",
                    "price_cop": 29500,
                    "price_inr": 619.5,
                    "description": "A famous street food delicacy from Amritsar. Tender fish chunks marinated in spices, battered, and fried to a perfect crisp. 🐟"
                },
                "Fish Tikka": {
                    "spanish_name": "Fish Tikka",
                    "price_cop": 30500,
                    "price_inr": 640.5,
                    "description": "Soft cubes of fresh fish marinated in yogurt and a special blend of ajwain (carom seeds) and spices, then gently cooked in the tandoor."
                },
                "Paneer Kathi Roll": {
                    "spanish_name": "Paneer Kathi Roll",
                    "price_cop": 29500,
                    "price_inr": 619.5,
                    "description": "A popular Indian street food wrap. Spiced paneer tikka, crunchy onions, and tangy sauces rolled into a warm, flaky paratha bread."
                },
                "Chicken Kathi Roll": {
                    "spanish_name": "Chicken Kathi Roll",
                    "price_cop": 32000,
                    "price_inr": 672,
                    "description": "Juicy chicken tikka pieces, sautéed peppers, and onions drizzled with mint chutney and wrapped in a soft, freshly made paratha."
                },
                "Prawn Tandoori": {
                    "spanish_name": "Prawn Tandoori",
                    "price_cop": 32800,
                    "price_inr": 688.8,
                    "description": "Jumbo prawns marinated in a classic tandoori spice blend and grilled to bring out their sweet flavor and smoky aroma. 🍤"
                },
                "Chicken Lollypop": {
                    "spanish_name": "Chicken Lollypop",
                    "price_cop": 26800,
                    "price_inr": 562.8,
                    "description": "A fun and flavorful Indo-Chinese appetizer. Frenched chicken winglets are marinated in a spicy sauce and deep-fried until crisp."
                },
            },
            "Sides": {
                "Basmati Rice": {
                    "spanish_name": "Arroz Basmati",
                    "price_cop": 19000,
                    "price_inr": 399,
                    "description": "Premium, long-grain Basmati rice, steamed to fluffy perfection. The perfect companion to any curry. 🍚"
                },
                "Raita": {
                    "spanish_name": "Raita",
                    "price_cop": 8000,
                    "price_inr": 168,
                    "description": "A cooling and refreshing yogurt dip mixed with finely chopped cucumber, mint, and a sprinkle of roasted cumin."
                },
                "Jeera Rice": {
                    "spanish_name": "Jeera Rice",
                    "price_cop": 19500,
                    "price_inr": 409.5,
                    "description": "Aromatic Basmati rice tempered with ghee, cumin seeds (jeera), and fresh coriander for a simple yet flavorful side."
                },
                "Onion Salad": {
                    "spanish_name": "Ensalada Cebolla",
                    "price_cop": 8000,
                    "price_inr": 168,
                    "description": "A simple, traditional Indian salad of thinly sliced onions, seasoned with lemon juice, salt, and chili."
                },
                "Mixed Salad": {
                    "spanish_name": "Ensalada Mixta",
                    "price_cop": 8000,
                    "price_inr": 168,
                    "description": "A fresh mix of crisp garden greens, cucumber, tomatoes, and carrots with a light dressing."
                },
                "Tamarind Sauce": {
                    "spanish_name": "Salas Tamarindo",
                    "price_cop": 8000,
                    "price_inr": 168,
                    "description": "A classic sweet and tangy sauce made from tamarind pulp, jaggery, and spices. Perfect for dipping."
                },
            },
            "Main Courses": {
                "Chicken Tikka Masala": {
                    "spanish_name": "Chicken Tikka Masala",
                    "price_cop": 55500,
                    "price_inr": 1165.5,
                    "description": "The world-famous dish! Char-grilled chicken tikka simmered in a rich, creamy, and mildly spiced tomato and onion gravy."
                },
                "Chicken Mughlai": {
                    "spanish_name": "Chicken Mughlai",
                    "price_cop": 53500,
                    "price_inr": 1123.5,
                    "description": "A royal and decadent curry made with tender chicken in a creamy sauce of cashews, almonds, and aromatic spices."
                },
            },
            "Desserts": {
                "Gulab Jamun": {
                    "spanish_name": "Gulab Jamun",
                    "price_cop": 20500,
                    "price_inr": 430.5,
                    "description": "A sweet ending. Soft, melt-in-your-mouth milk-solid balls, deep-fried and soaked in a fragrant rose and cardamom-flavored sugar syrup."
                }
            }
        }
    """
    return json.dumps(menu, indent=4)

tools = [take_order, view_order, view_menu]

import json
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.graph import StateGraph, END
from langgraph.prebuilt import ToolNode
from langchain_core.messages import HumanMessage, AIMessage
import os 

# print(f"API KEY {os.environ.get("GOOGLE_API_KEY")}")
# Initialize the LLM with tool-calling capabilities
# llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0, google_api_key="AIzaSyD029uP_4C5LJ-fvRxR-1DAiQ_nwTRvDWU")
# model_with_tools = llm.bind_tools(tools)

# # Define the agent node that calls the model
# def agent_node(state: AgentState):
#     # Get the current list of messages
#     messages = state["messages"]
    
#     # Add a system prompt to guide the agent if it's the first turn
#     if len(messages) == 1:
#         system_prompt = """
#         You are a friendly restaurant waiter.
#         Your first job is to ask for the user's table number.
#         Do not take any orders until you have the table number.
#         Once you have the table number, you can take their order.
#         Confirm the order back to the user after it has been taken.
#         """
#         messages = [
#             {"role": "system", "content": system_prompt},
#         ] + messages

#     # Invoke the model
#     response = model_with_tools.invoke(messages)
    
#     # The response is an AIMessage, which we add to our state
#     return {"messages": [response]}

# # Define the tool node
# tool_node = ToolNode(tools)

# # Define the conditional logic for routing
# def should_continue(state: AgentState):
#     last_message = state["messages"][-1]
#     # If the model made a tool call, then route to the 'tools' node
#     if last_message.tool_calls:
#         return "tools"
#     # Otherwise, the model generated a response to the user, so we end
#     return END


# # Create a new graph
# workflow = StateGraph(AgentState)

# # Add the nodes
# workflow.add_node("agent", agent_node)
# workflow.add_node("tools", tool_node)

# # Set the entry point of the graph
# workflow.set_entry_point("agent")

# # Add the conditional edge. The logic says:
# # AFTER the 'agent' node, check the 'should_continue' function.
# # If it returns 'tools', go to the 'tools' node.
# # If it returns END, finish the execution.
# workflow.add_conditional_edges(
#     "agent",
#     should_continue,
#     {
#         "tools": "tools",
#         END: END,
#     },
# )

# # Add a normal edge from the 'tools' node back to the 'agent' node.
# # This creates the main loop of the ReAct agent.
# workflow.add_edge("tools", "agent")

# # Compile the graph into a runnable app
# app = workflow.compile()

# from langchain_core.messages import HumanMessage, AIMessage

# # We start with an empty state
# state = AgentState(messages=[], table_number=None, order_list=[])

# print("Waiter Agent: Hello! I can help you with your order. What is your table number?")

# while True:
#     user_input = input("You: ")
#     if user_input.lower() in ["quit", "exit"]:
#         print("Waiter Agent: Thank you! Enjoy your meal.")
#         break
#     # Add the user's message to the state
#     state["messages"].append(HumanMessage(content=user_input))
#     # Invoke the graph
#     result = app.invoke(state)
#     # The final message from the AI is the one we display
#     final_response = result["messages"][-1]
#     # If the final response is a tool call, the tool node will have executed
#     # and we should look at the AI message before that for the text response.
#     # In this simple loop, we just print the last content message.
#     print(f"Waiter Agent: {final_response.content}")
#     # Update the state for the next turn
#     state = result

import streamlit as st

def get_agent_app():
    """Initializes and compiles the agent graph."""
    tools = [take_order, view_order, view_menu]

    # Use Streamlit secrets for the API key
    api_key = st.secrets.get("GOOGLE_API_KEY")
    if not api_key:
        st.error("Google API Key not found. Please set it in st.secrets.")
        st.stop()
        
    llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0, google_api_key=api_key)
    model_with_tools = llm.bind_tools(tools)

    def agent_node(state: AgentState):
        messages = state["messages"]
        if len(messages) == 1:
            system_prompt = """
            You are a friendly restaurant waiter.
            Your first job is to ask for the user's table number.
            Do not take any orders until you have the table number.
            Once you have the table number, you can take their order.
            List only the dishes available in the menu. ** Do not tell any dishes from your own knowledge**
            Confirm the order back to the user after it has been taken.
            Be conversational and helpful.
            """
            messages = [{"role": "system", "content": system_prompt}] + messages
        response = model_with_tools.invoke(messages)
        return {"messages": [response]}

    tool_node = ToolNode(tools)

    def should_continue(state: AgentState):
        return "tools" if state["messages"][-1].tool_calls else END

    workflow = StateGraph(AgentState)
    workflow.add_node("agent", agent_node)
    workflow.add_node("tools", tool_node)
    workflow.set_entry_point("agent")
    workflow.add_conditional_edges("agent", should_continue, {"tools": "tools", END: END})
    workflow.add_edge("tools", "agent")
    
    return workflow.compile()

app = get_agent_app()

# --- Streamlit UI ---

# st.set_page_config(page_title="Waiter Agent 🍽️", layout="wide")

# # Display the menu in the sidebar
# with st.sidebar:
#     st.title("📜 Menu")
#     for category, items in menu.items():
#         with st.expander(f"**{category}**", expanded=True):
#             for item, details in items.items():
#                 st.markdown(f"**{item}** - `${details['price_cop']:,}`")
#                 st.caption(details['description'])


# st.title("AI Waiter Chatbot 🤖🍽️")
# st.caption("I can take your order, show you the menu, and check your current order. What can I get for you?")


# # Initialize session state for chat history and agent state
# if "messages" not in st.session_state:
#     st.session_state.messages = [{"role": "assistant", "content": "Hello! I can help you with your order today. What is your table number?"}]

# if "agent_state" not in st.session_state:
#     st.session_state.agent_state = AgentState(messages=[], table_number=None, order_list=[])

# # Display chat messages from history
# for message in st.session_state.messages:
#     with st.chat_message(message["role"]):
#         st.markdown(message["content"])

# # Accept user input
# if prompt := st.chat_input("What would you like?"):
#     # Add user message to chat history
#     print(f"User Prompt {prompt}")
#     st.session_state.messages.append(HumanMessage(content=prompt))
#     with st.chat_message("user"):
#         st.markdown(prompt)
    
#     st.session_state.agent_state["messages"].append(HumanMessage(content=prompt))

#     # Prepare the input for the agent
#     agent_input = {"messages": [HumanMessage(content=prompt)]}

#     # Invoke the agent
#     with st.chat_message("assistant"):
#         with st.spinner("Thinking..."):
#             result = app.invoke(st.session_state.agent_state)
            
#             # The agent's final response is the last message in the result
#             response_content = result["messages"][-1].content
            
#             st.markdown(response_content)
            
#             # Update agent state and chat history
#             st.session_state.agent_state = result
#             st.session_state.messages.append({"role": "assistant", "content": response_content})
# --- Streamlit UI (Corrected and Simplified) ---

st.set_page_config(page_title="Waiter Agent 🍽️", layout="wide")

# Display the menu in the sidebar
with st.sidebar:
    st.title("📜 Menu")
    for category, items in menu.items():
        with st.expander(f"**{category}**", expanded=True):
            for item, details in items.items():
                st.markdown(f"**{item}** - `${details['price_cop']:,}`")
                st.caption(details['description'])


st.title("AI Waiter Chatbot 🤖🍽️")
st.caption("I can take your order, show you the menu, and check your current order. What can I get for you?")


# Initialize a single, unified state in the session
if "agent_state" not in st.session_state:
    # The agent's message list will now be the single source of truth
    st.session_state.agent_state = AgentState(
        messages=[AIMessage(content="Hello! I can help you with your order today. What is your table number?")],
        table_number=None, 
        order_list=[]
    )

# Display chat messages directly from the agent's history
for msg in st.session_state.agent_state["messages"]:
    # Skip displaying tool calls or empty messages
    if not msg.content:
        continue
    
    # Determine the role for the chat display
    if isinstance(msg, HumanMessage):
        role = "user"
    elif isinstance(msg, AIMessage):
        role = "assistant"
    else:
        continue # Skip other message types like SystemMessage

    with st.chat_message(role):
        st.markdown(msg.content)


# Handle user input
if prompt := st.chat_input("What would you like?"):
    # Add the user's message to the agent's state
    st.session_state.agent_state["messages"].append(HumanMessage(content=prompt))
    
    # Invoke the agent with the updated state
    with st.spinner("Thinking..."):
        result = app.invoke(st.session_state.agent_state)
        # Update the entire agent state with the result from the agent
        st.session_state.agent_state = result
    
    # Rerun the app to display the new messages
    st.rerun()
