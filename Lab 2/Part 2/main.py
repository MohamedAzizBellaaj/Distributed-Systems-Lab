import sys

from collaborative_editing import CollaborativeEditing
from PySide6.QtWidgets import QApplication
from RMQConnection import RMQConnection


def main():
    app = QApplication(sys.argv)

    connection = RMQConnection()
    window = CollaborativeEditing(connection)

    window.show()

    app.exec()


if __name__ == "__main__":
    main()
