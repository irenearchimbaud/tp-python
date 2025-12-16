from dataclasses import dataclass
from datetime import datetime
import socket
import psutil


@dataclass
class SystemMetrics:
    timestamp: datetime
    hostname: str
    cpu_percent: float
    memory_total: int
    memory_available: int
    memory_percent: float
    disk_usage: str

    def to_dict(self):
        return {
            "timestamp": self.timestamp.isoformat(),
            "hostname": self.hostname,
            "cpu_percent": self.cpu_percent,
            "memory_total": self.memory_total,
            "memory_available": self.memory_available,
            "memory_percent": self.memory_percent,
            "disk_usage": self.disk_usage,
        }

    def __str__(self):
        return (
            f"[{self.timestamp}] {self.hostname} | "
            f"CPU: {self.cpu_percent:.1f}% | "
            f"RAM: {self.memory_percent:.1f}%"
        )


class SystemCollector:
    def __init__(self):
        self.hostname = socket.gethostname()

    def collect(self) -> SystemMetrics:
        mem = psutil.virtual_memory()
        cpu = psutil.cpu_percent(interval=1)

        disks = {}
        for part in psutil.disk_partitions():
            try:
                usage = psutil.disk_usage(part.mountpoint)
                disks[part.mountpoint] = usage.percent
            except PermissionError:
                continue

        return SystemMetrics(
            timestamp=datetime.now(),
            hostname=self.hostname,
            cpu_percent=cpu,
            memory_total=mem.total,
            memory_available=mem.available,
            memory_percent=mem.percent,
            disk_usage=str(disks),
        )