import serial
from typing import Optional

class OWL:
    """
    Interface for controlling the OWL platform via serial communication.
    """

    def __init__(
        self,
        port: str,
        baudrate: int = 115200,
        timeout: float = 1.0,
        **kwargs
    ):
        """
        Initialize the OWL interface.
        
        Args:
            port: Serial port name (e.g., '/dev/ttyUSB0' or 'COM3')
            baudrate: Serial communication speed (default: 115200)
            timeout: Read timeout in seconds (default: 1.0)
            **kwargs: Additional arguments passed to serial.Serial
        """
        self.port = port
        self.baudrate = baudrate
        self.timeout = timeout
        self.kwargs = kwargs
        self._serial: Optional[serial.Serial] = None

    def open(self) -> None:
        """Open the serial connection."""
        if self._serial is None:
            self._serial = serial.Serial(
                port=self.port,
                baudrate=self.baudrate,
                timeout=self.timeout,
                **self.kwargs
            )
    
    def close(self) -> None:
        """Close the serial connection."""
        if self._serial is not None and self._serial.is_open:
            self._serial.close()
            self._serial = None

    def __enter__(self) -> 'OWL':
        self.open()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        self.close()

    def write(self, data: bytes) -> int:
        """
        Write bytes to the serial port.
        
        Args:
            data: The bytes to write.
            
        Returns:
            Number of bytes written.
            
        Raises:
            RuntimeError: If serial port is not open.
        """
        if self._serial is None or not self._serial.is_open:
            raise RuntimeError("Serial port is not open")
        return self._serial.write(data)

    def read(self, size: int = 1) -> bytes:
        """
        Read bytes from the serial port.
        
        Args:
            size: Number of bytes to read.
            
        Returns:
            Bytes read.
            
        Raises:
            RuntimeError: If serial port is not open.
        """
        if self._serial is None or not self._serial.is_open:
            raise RuntimeError("Serial port is not open")
        return self._serial.read(size)
        
    def read_line(self) -> str:
        """
        Read a line from existing serial connection.
        
        Returns:
            Decoded string line stripped of whitespace.
        """
        if self._serial is None or not self._serial.is_open:
            raise RuntimeError("Serial port is not open")
        line = self._serial.readline()
        return line.decode('utf-8', errors='replace').strip()

    def send_command(self, command: str) -> str:
        """
        Send a text command and return the response line.
        
        Args:
            command: The command string to send.
            
        Returns:
            The response string.
        """
        cmd_bytes = f"{command}\n".encode('utf-8')
        self.write(cmd_bytes)
        return self.read_line()
