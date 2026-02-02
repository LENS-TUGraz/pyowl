import sys
import os

# Adapt path to find the local src directory if package is not installed
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from pyowl import OWL

def main():
    print("Initializing OWL interface...")
    
    # Example usage:
    # device = OWL(port='/dev/ttyUSB0', baudrate=115200)
    
    # Using context manager (recommended)
    # with OWL(port='/dev/ttyUSB0') as owl:
    #     response = owl.send_command("HELLO")
    #     print(f"Response: {response}")

    # Demonstration of object creation (without actual connection for safe demo)
    try:
        owl = OWL(port="/dev/ttyUSB0", baudrate=9600)
        print(f"Successfully created OWL object: {owl}")
        print(f"Configured for port: {owl.port} at {owl.baudrate} baud")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
