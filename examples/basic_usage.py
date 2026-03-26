import sys
import os

# Adapt path to find the local src directory if package is not installed
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from pyowl import OWL

def main():
    print("Initializing OWL interface...")
        
    # Using context manager (recommended)
    with OWL(port='/dev/ttyUSB0') as owl:
        response = owl.set_target(90, "deg")
        print(f"Response: {response}")


if __name__ == "__main__":
    main()
