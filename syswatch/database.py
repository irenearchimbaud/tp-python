import sqlite3
from datetime import datetime, timedelta
from syswatch.model import SystemMetrics


class MetricsDatabase:
    def __init__(self, path="syswatch.db"):
        self.conn = sqlite3.connect(path)
        self.conn.row_factory = sqlite3.Row
        self._init_schema()

    def _init_schema(self):
        self.conn.execute("""
        CREATE TABLE IF NOT EXISTS metrics (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            hostname TEXT,
            cpu_percent REAL,
            memory_percent REAL,
            memory_total INTEGER,
            memory_available INTEGER,
            disk_usage TEXT
        )
        """)
        self.conn.commit()

    def save(self, metrics: SystemMetrics):
        data = metrics.to_dict()
        self.conn.execute("""
        INSERT INTO metrics (
            timestamp, hostname, cpu_percent,
            memory_percent, memory_total,
            memory_available, disk_usage
        ) VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (
            data["timestamp"],
            data["hostname"],
            data["cpu_percent"],
            data["memory_percent"],
            data["memory_total"],
            data["memory_available"],
            data["disk_usage"],
        ))
        self.conn.commit()

    def get_statistics(self, hostname, hours=24):
        since = datetime.now() - timedelta(hours=hours)
        cursor = self.conn.execute("""
        SELECT
            AVG(cpu_percent) as cpu_avg,
            MIN(cpu_percent) as cpu_min,
            MAX(cpu_percent) as cpu_max,
            AVG(memory_percent) as mem_avg,
            MIN(memory_percent) as mem_min,
            MAX(memory_percent) as mem_max,
            COUNT(*) as count
        FROM metrics
        WHERE hostname = ?
        AND timestamp >= ?
        """, (hostname, since.isoformat()))
        return cursor.fetchone()

    def cleanup_old(self, days=30):
        limit = datetime.now() - timedelta(days=days)
        cursor = self.conn.execute(
            "DELETE FROM metrics WHERE timestamp < ?",
            (limit.isoformat(),)
        )
        self.conn.commit()
        return cursor.rowcount