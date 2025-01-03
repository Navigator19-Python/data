import streamlit as st

# Dummy data for demonstration
if "services_dict" not in st.session_state:
    st.session_state.services_dict = {
        "Hairstyling": "$20",
        "Makeup": "$30",
        "Nail Care": "$15"
    }

if "professionals" not in st.session_state:
    st.session_state.professionals = [
        {"name": "Alice", "service": "Hairstyling", "location": "Dar es Salaam"},
        {"name": "John", "service": "Makeup", "location": "Arusha"},
        {"name": "Sophia", "service": "Nail Care", "location": "Mwanza"}
    ]

# Page configuration
st.set_page_config(page_title="Beauty Service App", layout="wide")

# Navigation menu
selected = st.sidebar.radio("Navigate", ["Home", "Browse Services", "Professionals", "Booking", "Admin Dashboard"])

# Home page
if selected == "Home":
    st.title("Welcome to the Beauty Service App")
    st.write("Your one-stop solution for hairstyling, makeup, and nail care services. Book professionals at your convenience.")

# Browse Services page
elif selected == "Browse Services":
    st.title("Browse Services")
    for service, price in st.session_state.services_dict.items():
        st.subheader(service)
        st.write(f"Price: {price}")
        if st.button(f"Book {service}", key=service):
            st.success(f"You have booked {service}!")

# Professionals page
elif selected == "Professionals":
    st.title("Available Professionals")
    for i, professional in enumerate(st.session_state.professionals):
        st.subheader(professional['name'])
        st.write(f"Service: {professional['service']}")
        st.write(f"Location: {professional['location']}")
        if st.button(f"Request {professional['name']}", key=professional['name']):
            st.success(f"Request sent to {professional['name']}!")

# Booking page
elif selected == "Booking":
    st.title("Make a Booking")
    service_name = st.selectbox("Choose a service", list(st.session_state.services_dict.keys()))
    location = st.text_input("Enter your location")
    if st.button("Confirm Booking"):
        st.success(f"Booking confirmed for {service_name} at {location}!")

# Admin Dashboard page
elif selected == "Admin Dashboard":
    st.title("Admin Dashboard")
    st.write("Manage services, users, and view analytics.")
    admin_action = st.selectbox("Choose an action", ["Add Service", "Update Prices", "View Feedback"])

    if admin_action == "Add Service":
        new_service = st.text_input("Enter new service name")
        new_price = st.text_input("Enter price for new service")
        if st.button("Add Service"):
            if not new_service.strip() or not new_price.strip():
                st.error("Service name and price cannot be empty.")
            else:
                st.session_state.services_dict[new_service.strip()] = new_price.strip()
                st.success(f"Added new service: {new_service.strip()} with price {new_price.strip()}!")

    elif admin_action == "Update Prices":
        service_to_update = st.selectbox("Choose a service", list(st.session_state.services_dict.keys()))
        updated_price = st.text_input("Enter new price")
        if st.button("Update Price"):
            if service_to_update in st.session_state.services_dict:
                st.session_state.services_dict[service_to_update] = updated_price
                st.success(f"Updated price for {service_to_update} to {updated_price}!")
