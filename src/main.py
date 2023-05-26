import asyncio
import sys
import pygame
import _thread
from asyncqt import QEventLoop
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

        test_button: QPushButton = QPushButton("Test")
        test_button.clicked.connect(lambda: print(f"button: pressed"))

        self.layout.addWidget(test_button)

        self.setLayout(self.layout)
        self.resize(1280, 720)
        self.show()


async def test() -> None:
    for i in range(1000):
        print(f"{i = }")
        await asyncio.sleep(0.1)

async def qt() -> None:
    app: QApplication = QApplication(sys.argv)
    loop: QEventLoop = QEventLoop(app)
    asyncio.set_event_loop(loop)

    with loop:
        window: Window = Window()
        loop.run_forever()

    # await app.exec()

async def main() -> None:
    async with asyncio.TaskGroup() as task_group:
        task_group.create_task(test())
        task_group.create_task(qt())

if __name__ == "__main__":
    asyncio.run(main())
