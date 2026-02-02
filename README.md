# pyowl

This module provides high-level control for the OWL platform via serial communication.

## Installation

To install the package, we recommend using [uv](https://github.com/astral-sh/uv):

```bash
uv add git+https://github.com/LENS-TUGraz/pyowl.git
```

Alternatively, you can use standard pip:

```bash
pip install git+https://github.com/LENS-TUGraz/pyowl.git
```


## Usage

The recommended way to use `pyowl` is with a context manager, which handles cleanup automatically:

```python
from pyowl import OWL

with OWL(port='/dev/ttyUSB0') as owl:
    # Send a command and get response
    response = owl.send_command("STATUS")
    print(f"Status: {response}")
```

### Basic Example

When not using the context manager, you must manually ensure the connection is opened and closed:

```python
from pyowl import OWL

owl = OWL(port='/dev/ttyUSB0')
owl.open()

try:
    response = owl.send_command("STATUS")
    print(f"Status: {response}")
finally:
    owl.close()
```


## API

### `OWL` Class

**Constructor**:
`OWL(port: str, baudrate: int = 115200, timeout: float = 1.0, **kwargs)`

- `port`: The serial port (e.g., `/dev/ttyUSB0` on Linux, `COM3` on Windows).
- `baudrate`: Serial baud rate (default: 115200).
- `timeout`: Read timeout in seconds (default: 1.0).

**Methods**:

- `open()`: Opens the serial connection.
- `close()`: Closes the serial connection.
- `send_command(command: str) -> str`: Sends a text command and returns the response line.
- `write(data: bytes) -> int`: Writes raw bytes to the device.
- `read(size: int = 1) -> bytes`: Reads raw bytes from the device.
- `read_line() -> str`: Reads a line of text, decoded as UTF-8.

---

## AI Disclosure

LLMs were used for large parts of the project's creation.
