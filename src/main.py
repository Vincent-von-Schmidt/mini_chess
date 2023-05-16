import asyncio
import sys
import pygame
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QFrame,
    QPushButton,
    QVBoxLayout
)
from PyQt6.QtGui import (
    QPainter,
    QImage,
)


class Window(QFrame):
    def __init__(self) -> None:
        super().__init__()
        
        self.layout: QVBoxLayout = QVBoxLayout(self)
        self.setlayout(self.layout)

async def main() -> None:
    app: QApplication = QApplication(sys.argv)

if __name__ == "__main__":
    with asyncio.TaskGroup() as task_group:
        task_group.create
