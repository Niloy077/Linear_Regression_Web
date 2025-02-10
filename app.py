import streamlit as st
import matplotlib
# matplotlib.use('Agg')  # Use non-GUI Agg backend
import matplotlib.pyplot as plt
import numpy as np
import os

def generate_plot():
    # Example simple model: Linear Regression y = 2x + 1
    x = np.linspace(0, 10, 100)  # Sample data points
    y = 2 * x + 1
    
    # Create a plot
    plt.figure(figsize=(6,4))
    plt.plot(x, y, label="y = 2x + 1")
    plt.title("Linear Regression: y = 2x + 1")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    
    # Save the plot to a file
    plot_filename = "static/plot.png"
    plt.savefig(plot_filename)
    plt.close()  # Close the plot to avoid memory leaks
    
    return plot_filename

def main():
    # Page configuration
    st.set_page_config(page_title="Linear Regression Web", layout="centered")
    
    # Custom CSS
    st.markdown("""
    <style>
    * {
        font-family: Arial, sans-serif;
    }
    .stButton>button {
        background-color: #0056b3;
        color: white;
        border: none;
        border-radius: 4px;
        padding: 10px 20px;
    }
    .stButton>button:hover {
        background-color: #004494;
    }
    footer {
        text-align: center;
        padding: 10px;
        background-color: #0056b3;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Header
    st.markdown("<h1 style='text-align: center;'>Linear Regression Web</h1>", unsafe_allow_html=True)
    
    # Main content
    st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
    
    # Generate Plot Button
    if st.button("Generate Plot"):
        try:
            plot_path = generate_plot()
            st.image(plot_path, caption="Linear Regression Plot", use_column_width=True)
        except Exception as e:
            st.error(f"An error occurred: {e}")
    
    st.markdown("</div>", unsafe_allow_html=True)
    
    # Footer
    st.markdown("""
    <hr>
    <p style='text-align: center;'>© 2025 Linear Regression Classifier. All rights reserved.</p>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
