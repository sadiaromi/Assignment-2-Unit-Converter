import streamlit as st

def main():
    st.set_page_config(page_title="Unit Converter", page_icon="🔄", layout="centered")
    
    # Custom CSS 
    st.markdown("""
    <style>
    .main-header {
        font-size: 2.5rem;
        color: #000000;
        text-align: center;
    }
    .sub-header {
        font-size: 1.5rem;
        color: #424242;
        margin-bottom: 20px;
    }
    .result-text {
        font-size: 1.8rem;
        font-weight: bold;
        color: #2E7D32;
        padding: 10px;
        border-radius: 5px;
        margin-top: 20px;
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # App title
    st.markdown("<h1 class='main-header'>Unit Converter</h1>", unsafe_allow_html=True)
    st.markdown("<p class='sub-header'>Conversion between different units of measurement</p>", unsafe_allow_html=True)
    
    # Conversion types
    conversion_types = [
        "Length", 
        "Weight/Mass", 
        "Temperature", 
        "Area", 
        "Volume", 
        "Speed", 
        "Time", 
        "Frequency", 
        "Energy", 
        "Pressure"
    ]
    
    conversion_type = st.selectbox("Select Conversion Type:", conversion_types)
    
    # Appropriate converter based on selection
    if conversion_type == "Length":
        length_converter()
    elif conversion_type == "Weight/Mass":
        weight_converter()
    elif conversion_type == "Temperature":
        temperature_converter()
    elif conversion_type == "Area":
        area_converter()
    elif conversion_type == "Volume":
        volume_converter()
    elif conversion_type == "Speed":
        speed_converter()
    elif conversion_type == "Time":
        time_converter()
    elif conversion_type == "Frequency":
        frequency_converter()
    elif conversion_type == "Energy":
        energy_converter()
    elif conversion_type == "Pressure":
        pressure_converter()
    
   
def length_converter():
    st.subheader("Length Conversion")
    
    # Length units and their conversion factors to meters
    length_units = {
        "Millimeter (mm)": 0.001,
        "Centimeter (cm)": 0.01,
        "Meter (m)": 1.0,
        "Kilometer (km)": 1000.0,
        "Inch (in)": 0.0254,
        "Foot (ft)": 0.3048,
        "Yard (yd)": 0.9144,
        "Mile (mi)": 1609.34
    }
    
    # Two columns for input and output units
    col1, col2 = st.columns(2)
    
    with col1:
        from_unit = st.selectbox("From:", list(length_units.keys()), key="length_from")
        from_value = st.number_input("Enter value:", value=1.0, format="%.6f", key="length_value")
    
    with col2:
        to_unit = st.selectbox("To:", list(length_units.keys()), key="length_to")
    
    # Calculate the conversion
    meters = from_value * length_units[from_unit]
    result = meters / length_units[to_unit]
    
    # Display the result
    st.markdown(f"<div class='result-text'>{from_value} {from_unit} = {result:.6g} {to_unit}</div>", unsafe_allow_html=True)
    
    # Show conversion formula
    with st.expander("Show conversion formula"):
        st.write(f"1 {from_unit} = {length_units[from_unit]/length_units[to_unit]:.6g} {to_unit}")
        st.write(f"Formula: {from_unit} value x {length_units[from_unit]/length_units[to_unit]:.6g}")

def weight_converter():
    st.subheader("Weight/Mass Conversion")
    
    # Weight units and their conversion factors to kilograms
    weight_units = {
        "Milligram (mg)": 0.000001,
        "Gram (g)": 0.001,
        "Kilogram (kg)": 1.0,
        "Metric Ton (t)": 1000.0,
        "Ounce (oz)": 0.0283495,
        "Pound (lb)": 0.453592,
        "Stone (st)": 6.35029,
        "US Ton (ton)": 907.185
    }
    
    # Two columns for input and output units
    col1, col2 = st.columns(2)
    
    with col1:
        from_unit = st.selectbox("From:", list(weight_units.keys()), key="weight_from")
        from_value = st.number_input("Enter value:", value=1.0, format="%.6f", key="weight_value")
    
    with col2:
        to_unit = st.selectbox("To:", list(weight_units.keys()), key="weight_to")
    
    # Calculate the conversion
    kilograms = from_value * weight_units[from_unit]
    result = kilograms / weight_units[to_unit]
    
    # Display the result
    st.markdown(f"<div class='result-text'>{from_value} {from_unit} = {result:.6g} {to_unit}</div>", unsafe_allow_html=True)
    
    # Show conversion formula
    with st.expander("Show conversion formula"):
        st.write(f"1 {from_unit} = {weight_units[from_unit]/weight_units[to_unit]:.6g} {to_unit}")
        st.write(f"Formula: {from_unit} value x {weight_units[from_unit]/weight_units[to_unit]:.6g}")

def temperature_converter():
    st.subheader("Temperature Conversion")
    
    # Temperature units
    temp_units = ["Celsius (°C)", "Fahrenheit (°F)", "Kelvin (K)"]
    
    # Two columns for input and output units
    col1, col2 = st.columns(2)
    
    with col1:
        from_unit = st.selectbox("From:", temp_units, key="temp_from")
        from_value = st.number_input("Enter value:", value=0.0, format="%.2f", key="temp_value")
    
    with col2:
        to_unit = st.selectbox("To:", temp_units, key="temp_to")
    
    # Calculate the conversion
    result = convert_temperature(from_value, from_unit, to_unit)
    
    # Display the result
    st.markdown(f"<div class='result-text'>{from_value} {from_unit} = {result:.2f} {to_unit}</div>", unsafe_allow_html=True)
    
    # Show conversion formula
    with st.expander("Show conversion formula"):
        show_temp_formula(from_unit, to_unit)

def convert_temperature(value, from_unit, to_unit):
    # Convert to Celsius first
    if from_unit == "Celsius (°C)":
        celsius = value
    elif from_unit == "Fahrenheit (°F)":
        celsius = (value - 32) * 5/9
    else:  # Kelvin
        celsius = value - 273.15
    
    # Convert from Celsius to target unit
    if to_unit == "Celsius (°C)":
        return celsius
    elif to_unit == "Fahrenheit (°F)":
        return celsius * 9/5 + 32
    else:  # Kelvin
        return celsius + 273.15

def show_temp_formula(from_unit, to_unit):
    formulas = {
        ("Celsius (°C)", "Fahrenheit (°F)"): "°F = °C x (9/5) + 32",
        ("Celsius (°C)", "Kelvin (K)"): "K = °C + 273.15",
        ("Fahrenheit (°F)", "Celsius (°C)"): "°C = (°F - 32) x (5/9)",
        ("Fahrenheit (°F)", "Kelvin (K)"): "K = (°F - 32) x (5/9) + 273.15",
        ("Kelvin (K)", "Celsius (°C)"): "°C = K - 273.15",
        ("Kelvin (K)", "Fahrenheit (°F)"): "°F = (K - 273.15) x (9/5) + 32"
    }
    
    if from_unit == to_unit:
        st.write("No conversion needed - units are the same")
    else:
        st.write(f"Formula: {formulas[(from_unit, to_unit)]}")

def area_converter():
    st.subheader("Area Conversion")
    
    # Area units and their conversion factors to square meters
    area_units = {
        "Square Millimeter (mm²)": 0.000001,
        "Square Centimeter (cm²)": 0.0001,
        "Square Meter (m²)": 1.0,
        "Square Kilometer (km²)": 1000000.0,
        "Square Inch (in²)": 0.00064516,
        "Square Foot (ft²)": 0.092903,
        "Square Yard (yd²)": 0.836127,
        "Acre": 4046.86,
        "Hectare (ha)": 10000.0,
        "Square Mile (mi²)": 2589988.11
    }
    
    # Two columns for input and output units
    col1, col2 = st.columns(2)
    
    with col1:
        from_unit = st.selectbox("From:", list(area_units.keys()), key="area_from")
        from_value = st.number_input("Enter value:", value=1.0, format="%.6f", key="area_value")
    
    with col2:
        to_unit = st.selectbox("To:", list(area_units.keys()), key="area_to")
    
    # Calculate the conversion
    sq_meters = from_value * area_units[from_unit]
    result = sq_meters / area_units[to_unit]
    
    # Display the result
    st.markdown(f"<div class='result-text'>{from_value} {from_unit} = {result:.6g} {to_unit}</div>", unsafe_allow_html=True)
    
    # Show conversion formula
    with st.expander("Show conversion formula"):
        st.write(f"1 {from_unit} = {area_units[from_unit]/area_units[to_unit]:.6g} {to_unit}")
        st.write(f"Formula: {from_unit} value x {area_units[from_unit]/area_units[to_unit]:.6g}")

def volume_converter():
    st.subheader("Volume Conversion")
    
    # Volume units and their conversion factors to cubic meters
    volume_units = {
        "Milliliter (ml)": 0.000001,
        "Cubic Centimeter (cm³)": 0.000001,
        "Liter (L)": 0.001,
        "Cubic Meter (m³)": 1.0,
        "US Fluid Ounce (fl oz)": 0.0000295735,
        "US Cup": 0.000236588,
        "US Pint (pt)": 0.000473176,
        "US Quart (qt)": 0.000946353,
        "US Gallon (gal)": 0.00378541,
        "Imperial Gallon (UK gal)": 0.00454609,
        "Cubic Inch (in³)": 0.0000163871,
        "Cubic Foot (ft³)": 0.0283168
    }
    
    # Two columns for input and output units
    col1, col2 = st.columns(2)
    
    with col1:
        from_unit = st.selectbox("From:", list(volume_units.keys()), key="volume_from")
        from_value = st.number_input("Enter value:", value=1.0, format="%.6f", key="volume_value")
    
    with col2:
        to_unit = st.selectbox("To:", list(volume_units.keys()), key="volume_to")
    
    # Calculate the conversion
    cubic_meters = from_value * volume_units[from_unit]
    result = cubic_meters / volume_units[to_unit]
    
    # Display the result
    st.markdown(f"<div class='result-text'>{from_value} {from_unit} = {result:.6g} {to_unit}</div>", unsafe_allow_html=True)
    
    # Show conversion formula
    with st.expander("Show conversion formula"):
        st.write(f"1 {from_unit} = {volume_units[from_unit]/volume_units[to_unit]:.6g} {to_unit}")
        st.write(f"Formula: {from_unit} value x {volume_units[from_unit]/volume_units[to_unit]:.6g}")

def speed_converter():
    st.subheader("Speed Conversion")
    
    # Speed units and their conversion factors to meters per second
    speed_units = {
        "Meter per second (m/s)": 1.0,
        "Kilometer per hour (km/h)": 0.277778,
        "Mile per hour (mph)": 0.44704,
        "Foot per second (ft/s)": 0.3048,
        "Knot (kn)": 0.514444,
        "Mach (at sea level)": 340.29,
        "Speed of light (c)": 299792458.0
    }
    
    # Two columns for input and output units
    col1, col2 = st.columns(2)
    
    with col1:
        from_unit = st.selectbox("From:", list(speed_units.keys()), key="speed_from")
        from_value = st.number_input("Enter value:", value=1.0, format="%.6f", key="speed_value")
    
    with col2:
        to_unit = st.selectbox("To:", list(speed_units.keys()), key="speed_to")
    
    # Calculate the conversion
    meters_per_second = from_value * speed_units[from_unit]
    result = meters_per_second / speed_units[to_unit]
    
    # Display the result
    st.markdown(f"<div class='result-text'>{from_value} {from_unit} = {result:.6g} {to_unit}</div>", unsafe_allow_html=True)
    
    # Show conversion formula
    with st.expander("Show conversion formula"):
        st.write(f"1 {from_unit} = {speed_units[from_unit]/speed_units[to_unit]:.6g} {to_unit}")
        st.write(f"Formula: {from_unit} value x {speed_units[from_unit]/speed_units[to_unit]:.6g}")

def time_converter():
    st.subheader("Time Conversion")
    
    # Time units and their conversion factors to seconds
    time_units = {
        "Nanosecond (ns)": 1e-9,
        "Microsecond (μs)": 1e-6,
        "Millisecond (ms)": 0.001,
        "Second (s)": 1.0,
        "Minute (min)": 60.0,
        "Hour (h)": 3600.0,
        "Day (d)": 86400.0,
        "Week (wk)": 604800.0,
        "Month (30 days)": 2592000.0,
        "Year (365 days)": 31536000.0
    }
    
    # Two columns for input and output units
    col1, col2 = st.columns(2)
    
    with col1:
        from_unit = st.selectbox("From:", list(time_units.keys()), key="time_from")
        from_value = st.number_input("Enter value:", value=1.0, format="%.6f", key="time_value")
    
    with col2:
        to_unit = st.selectbox("To:", list(time_units.keys()), key="time_to")
    
    # Calculate the conversion
    seconds = from_value * time_units[from_unit]
    result = seconds / time_units[to_unit]
    
    # Display the result
    st.markdown(f"<div class='result-text'>{from_value} {from_unit} = {result:.6g} {to_unit}</div>", unsafe_allow_html=True)
    
    # Show conversion formula
    with st.expander("Show conversion formula"):
        st.write(f"1 {from_unit} = {time_units[from_unit]/time_units[to_unit]:.6g} {to_unit}")
        st.write(f"Formula: {from_unit} value x {time_units[from_unit]/time_units[to_unit]:.6g}")

def frequency_converter():
    st.subheader("Frequency Conversion")
    
    # Frequency units and their conversion factors to hertz
    frequency_units = {
        "Hertz (Hz)": 1.0,
        "Kilohertz (kHz)": 1000.0,
        "Megahertz (MHz)": 1000000.0,
        "Gigahertz (GHz)": 1000000000.0,
        "Cycles per second (cps)": 1.0,
        "Revolutions per minute (rpm)": 1/60.0,
        "Radians per second (rad/s)": 1/(2*3.14159)
    }
    
    # Two columns for input and output units
    col1, col2 = st.columns(2)
    
    with col1:
        from_unit = st.selectbox("From:", list(frequency_units.keys()), key="freq_from")
        from_value = st.number_input("Enter value:", value=1.0, format="%.6f", key="freq_value")
    
    with col2:
        to_unit = st.selectbox("To:", list(frequency_units.keys()), key="freq_to")
    
    # Calculate the conversion
    hertz = from_value * frequency_units[from_unit]
    result = hertz / frequency_units[to_unit]
    
    # Display the result
    st.markdown(f"<div class='result-text'>{from_value} {from_unit} = {result:.6g} {to_unit}</div>", unsafe_allow_html=True)
    
    # Show conversion formula
    with st.expander("Show conversion formula"):
        st.write(f"1 {from_unit} = {frequency_units[from_unit]/frequency_units[to_unit]:.6g} {to_unit}")
        st.write(f"Formula: {from_unit} value x {frequency_units[from_unit]/frequency_units[to_unit]:.6g}")

def energy_converter():
    st.subheader("Energy Conversion")
    
    # Energy units and their conversion factors to joules
    energy_units = {
        "Joule (J)": 1.0,
        "Kilojoule (kJ)": 1000.0,
        "Calorie (cal)": 4.184,
        "Kilocalorie (kcal)": 4184.0,
        "Watt-hour (Wh)": 3600.0,
        "Kilowatt-hour (kWh)": 3600000.0,
        "Electronvolt (eV)": 1.602176634e-19,
        "British Thermal Unit (BTU)": 1055.06,
        "Foot-pound (ft⋅lb)": 1.35582,
        "Erg": 1e-7
    }
    
    # Two columns for input and output units
    col1, col2 = st.columns(2)
    
    with col1:
        from_unit = st.selectbox("From:", list(energy_units.keys()), key="energy_from")
        from_value = st.number_input("Enter value:", value=1.0, format="%.6f", key="energy_value")
    
    with col2:
        to_unit = st.selectbox("To:", list(energy_units.keys()), key="energy_to")
    
    # Calculate the conversion
    joules = from_value * energy_units[from_unit]
    result = joules / energy_units[to_unit]
    
    # Display the result
    st.markdown(f"<div class='result-text'>{from_value} {from_unit} = {result:.6g} {to_unit}</div>", unsafe_allow_html=True)
    
    # Show conversion formula
    with st.expander("Show conversion formula"):
        st.write(f"1 {from_unit} = {energy_units[from_unit]/energy_units[to_unit]:.6g} {to_unit}")
        st.write(f"Formula: {from_unit} value x {energy_units[from_unit]/energy_units[to_unit]:.6g}")

def pressure_converter():
    st.subheader("Pressure Conversion")
    
    # Pressure units and their conversion factors to pascals
    pressure_units = {
        "Pascal (Pa)": 1.0,
        "Kilopascal (kPa)": 1000.0,
        "Megapascal (MPa)": 1000000.0,
        "Bar": 100000.0,
        "Atmosphere (atm)": 101325.0,
        "Torr": 133.322,
        "Pound per square inch (psi)": 6894.76,
        "Millimeter of mercury (mmHg)": 133.322,
        "Inch of mercury (inHg)": 3386.39,
        "Inch of water (inH2O)": 249.089
    }
    
    # Two columns for input and output units
    col1, col2 = st.columns(2)
    
    with col1:
        from_unit = st.selectbox("From:", list(pressure_units.keys()), key="pressure_from")
        from_value = st.number_input("Enter value:", value=1.0, format="%.6f", key="pressure_value")
    
    with col2:
        to_unit = st.selectbox("To:", list(pressure_units.keys()), key="pressure_to")
    
    # Calculate the conversion
    pascals = from_value * pressure_units[from_unit]
    result = pascals / pressure_units[to_unit]
    
    # Display the result
    st.markdown(f"<div class='result-text'>{from_value} {from_unit} = {result:.6g} {to_unit}</div>", unsafe_allow_html=True)
    
    # Show conversion formula
    with st.expander("Show conversion formula"):
        st.write(f"1 {from_unit} = {pressure_units[from_unit]/pressure_units[to_unit]:.6g} {to_unit}")
        st.write(f"Formula: {from_unit} value x {pressure_units[from_unit]/pressure_units[to_unit]:.6g}")

if __name__ == "__main__":
    main()