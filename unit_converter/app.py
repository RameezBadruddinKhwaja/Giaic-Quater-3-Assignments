import streamlit as st

def convert_length(value, from_unit, to_unit):
    """
    Convert a length value from one unit to another.
    This simple example only demonstrates a handful of conversions,
    but you can expand it as needed.
    """
    # Conversion rates to meters
    conversion_to_meters = {
        "Meter (m)": 1.0,
        "Centimeter (cm)": 0.01,
        "Kilometer (km)": 1000.0,
        "Inch (in)": 0.0254,
        "Foot (ft)": 0.3048,
        "Yard (yd)": 0.9144,
        "Mile (mi)": 1609.344
    }
    
    # Convert the input value to meters
    value_in_meters = value * conversion_to_meters[from_unit]
    
    # Convert from meters to the target unit
    conversion_from_meters = 1 / conversion_to_meters[to_unit]
    converted_value = value_in_meters * conversion_from_meters
    
    return converted_value

def main():
    st.title("Unit Converter")
    st.write("A simple app to convert between different units of length.")

    # Create two columns for the input & output sections
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Input")
        input_value = st.number_input("Enter value", value=1.0, step=0.1)
        from_unit = st.selectbox("From Unit", ["Meter (m)", "Centimeter (cm)", "Kilometer (km)",
                                               "Inch (in)", "Foot (ft)", "Yard (yd)", "Mile (mi)"])

    with col2:
        st.subheader("Output")
        to_unit = st.selectbox("To Unit", ["Meter (m)", "Centimeter (cm)", "Kilometer (km)",
                                           "Inch (in)", "Foot (ft)", "Yard (yd)", "Mile (mi)"])

    # Perform conversion
    result = convert_length(input_value, from_unit, to_unit)

    # Show the result
    st.write(f"**Result:** {result} {to_unit}")

    # Display a simple formula or note (optional)
    st.markdown(f"**Formula:** multiply the value in {from_unit} by the conversion factor to get the value in {to_unit}")

if __name__ == "__main__":
    main()
