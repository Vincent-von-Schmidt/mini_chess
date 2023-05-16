import asyncio
import sys
import pygame
import _thread
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


# async def test() -> None:
#     for i in range(1000):
#         print(f"{i = }")
#         await asyncio.sleep(0.1)

async def test() -> None:
    for i in range(1000):
        print(f"{i = }")
        await asyncio.sleep(0.1)

# async def exec(app: QApplication) -> None:
#     app.exec()

# async def qt() -> None:
#     app: QApplication = QApplication(sys.argv)
#     window: Window = Window()
#
#     await exec(app)

def qt() -> None:
    app: QApplication = QApplication(sys.argv)
    window: Window = Window()

    app.exec()

# async def main() -> None:
#     async with asyncio.TaskGroup() as task_group:
#         task_group.create_task(test())
#         task_group.create_task(qt())

if __name__ == "__main__":
    # asyncio.run(main())
    _thread.start_new_thread(qt, ())
    _thread.start_new_thread(test, ())
