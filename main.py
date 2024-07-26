import os
import pandas as pd
import numpy as np
from PIL import Image

# Define the directories for input data and output results
input_directory = "path/to/data"
output_directory = "path/to/output"

# Function to process an image file
def process_image(image_path):
    """
    Convert an image to grayscale and save the processed image.
    
    Parameters:
    - image_path: str, path to the input image file
    """
    # Load the image
    image = Image.open(image_path)
    
    # Convert the image to grayscale
    grayscale_image = image.convert("L")
    
    # Save the processed image
    output_path = os.path.join(output_directory, os.path.basename(image_path))
    grayscale_image.save(output_path)
    print(f"Saved processed image to: {output_path}")

# Function to process a signal file
def process_signal(signal_path):
    """
    Apply a filter to signal data and save the processed signal.
    
    Parameters:
    - signal_path: str, path to the input signal file
    """
    # Load the signal data from a CSV file
    signal_data = pd.read_csv(signal_path)
    
    # Apply a simple moving average filter to the signal
    filtered_signal = apply_filter(signal_data["signal"].values)
    
    # Save the processed signal to a new CSV file
    signal_data["filtered_signal"] = filtered_signal
    output_path = os.path.join(output_directory, os.path.basename(signal_path))
    signal_data.to_csv(output_path, index=False)
    print(f"Saved processed signal to: {output_path}")

# Helper function to apply a simple moving average filter to a signal
def apply_filter(signal, window_size=5):
    """
    Apply a simple moving average filter to a signal.
    
    Parameters:
    - signal: np.ndarray, array of signal values
    - window_size: int, size of the moving window (default is 5)
    
    Returns:
    - filtered_signal: np.ndarray, filtered signal values
    """
    # Use numpy's convolve function to apply the moving average filter
    filtered_signal = np.convolve(signal, np.ones(window_size) / window_size, mode="same")
    return filtered_signal

def main():
    """
    Main function to process all images and signal files in the input directory.
    """
    # Ensure the output directory exists
    os.makedirs(output_directory, exist_ok=True)

    # Process each image file in the input directory
    image_files = [os.path.join(input_directory, f) for f in os.listdir(input_directory) if f.endswith((".jpg", ".png"))]
    for image_file in image_files:
        process_image(image_file)

    # Process each signal file in the input directory
    signal_files = [os.path.join(input_directory, f) for f in os.listdir(input_directory) if f.endswith(".csv")]
    for signal_file in signal_files:
        process_signal(signal_file)

    print("All files processed successfully.")

if __name__ == "__main__":
    main()
