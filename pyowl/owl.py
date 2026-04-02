import math
import serial
from typing import Optional, Literal

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
        
    def read_line(self, num_lines: int = 1) -> str:
        """
        Read a line from existing serial connection.
        
        Args:
            num_lines: Number of lines to read.
        
        Returns:
            Decoded string line stripped of whitespace.
        """
        if self._serial is None or not self._serial.is_open:
            raise RuntimeError("Serial port is not open")

        lines = ""
        for _ in range(num_lines):
            line = self._serial.readline()
            lines += line.decode('utf-8', errors='replace').strip()
        return lines

    def raw_command(self, command: str, num_lines: int = 1) -> str:
        """
        Send raw text command and read response.
        It is recommended to use the higher level functions, such as set_target(), get_target(), etc., instead.
        
        Args:
            command: The command string to send.
            num_lines: Number of lines to read after sending the command.
            
        Returns:
            The response string.
        """
        cmd_bytes = f"{command}\n".encode('utf-8')
        self.write(cmd_bytes)
        return self.read_line(num_lines)

    def set_target(self, target: float, unit: Literal["rad", "deg"] = "rad") -> None:
        """
        Set the target position.
        
        Args:
            target: The target position.
            unit: Unit of the target angle ("rad" for radians, "deg" for degrees). Default is "rad".
        """
        if unit == "deg":
            target = math.radians(target)
        self.raw_command(f"T{target:.3f}")

    def get_target(self, unit: Literal["rad", "deg"] = "rad") -> float:
        """
        Get the target position.
        
        Args:
            unit: Unit of the returned angle ("rad" for radians, "deg" for degrees). Default is "rad".
        
        Returns:
            The target position in the specified unit.
        """
        angle = float(self.raw_command("T"))
        if unit == "deg":
            return math.degrees(angle)
        return angle

    def get_absolute_angle(self, unit: Literal["rad", "deg"] = "rad") -> float:
        """
        Get the current absolute angle.
        The absolute angle is the angle since the last reset.
        
        Args:
            unit: Unit of the returned angle ("rad" for radians, "deg" for degrees). Default is "rad".
        
        Returns:
            The current absolute angle in the specified unit.
        """
        angle = float(self.raw_command("A"))
        if unit == "deg":
            return math.degrees(angle)
        return angle
    
    def get_mechanical_angle(self, unit: Literal["rad", "deg"] = "rad") -> float:
        """
        Get the current mechanical angle.
        The mechanical angle is the angle within the current revolution.
        
        Args:
            unit: Unit of the returned angle ("rad" for radians, "deg" for degrees). Default is "rad".
        
        Returns:
            The current mechanical angle in the specified unit.
        """
        angle = float(self.raw_command("R"))
        if unit == "deg":
            return math.degrees(angle)
        return angle
