import sys

from PySide6.QtWidgets import QApplication

from collaborative_editing import CollaborativeEditing
from RMQ_connection import RMQConnection


def main():
    app = QApplication(sys.argv)

    connection = RMQConnection()
    window = CollaborativeEditing(connection)

    window.show()

    app.exec()


if __name__ == "__main__":
    main()
