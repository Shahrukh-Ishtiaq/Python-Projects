import streamlit as st

def convert_units(value, from_unit, to_unit):
    conversions = {
        "Length": {
            "Meter": 1,
            "Kilometer": 0.001,
            "Centimeter": 100,
            "Millimeter": 1000,
            "Mile": 0.000621371,
            "Foot": 3.28084,
            "Inch": 39.3701
        },
        "Weight": {
            "Kilogram": 1,
            "Gram": 1000,
            "Milligram": 1000000,
            "Pound": 2.20462,
            "Ounce": 35.274
        }
    }
    
    for category, units in conversions.items():
        if from_unit in units and to_unit in units:
            return value * (units[to_unit] / units[from_unit])
    return None

st.title("📐 Unit Converter")

category = st.selectbox("Select Category", ["Length", "Weight"])

if category:
    units = list({
        "Length": ["Meter", "Kilometer", "Centimeter", "Millimeter", "Mile", "Foot", "Inch"],
        "Weight": ["Kilogram", "Gram", "Milligram", "Pound", "Ounce"]
    }[category])

    from_unit = st.selectbox("From Unit", units)
    to_unit = st.selectbox("To Unit", units)
    value = st.number_input("Enter Value", min_value=0.0, format="%.2f")

    if value > 0:
        result = convert_units(value, from_unit, to_unit)
        if result is not None:
            st.success(f"{value} {from_unit} = {result:.4f} {to_unit}")
        else:
            st.error("Invalid conversion")