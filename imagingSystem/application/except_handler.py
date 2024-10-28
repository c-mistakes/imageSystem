import sys
import traceback

import pathvalidate
from PySide6.QtWidgets import QMessageBox

warning_error_types = [ValueError, AttributeError,
                       pathvalidate.error.InvalidCharError, PermissionError, TypeError]

point_error_types = [FileExistsError, FileNotFoundError]

import traceback
from PySide6.QtWidgets import QMessageBox, QAbstractButton


class CustomMessageBox(QMessageBox):
    def __init__(self, *args, **kwargs):
        super(CustomMessageBox, self).__init__(*args, **kwargs)
        self.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        self.button(QMessageBox.Ok).setText("确定")
        self.button(QMessageBox.Cancel).setText("取消")

    def showEvent(self, event):
        super().showEvent(event)
        self.set_details_button_text("显示详细信息")

    def set_details_button_text(self, text):
        for button in self.findChildren(QAbstractButton):
            if button.text() == "Show Details...":
                button.setText(text)
                self.details_button = button
                self.details_button.clicked.connect(self.on_details_button_clicked)
                break

    def on_details_button_clicked(self):
        self.details_button.setText("显示详细信息")


def handle_global_execution(exc_type, exc_value, exc_traceback):
    # 构建错误消息
    error_message = ''.join(traceback.format_exception(exc_type, exc_value, exc_traceback))

    # 创建错误提示窗口
    error_box = CustomMessageBox()
    error_box.setDetailedText(error_message)

    # 根据异常类型来处理不同的情况
    if exc_type in warning_error_types:
        error_box.setIcon(QMessageBox.Warning)
    elif exc_type in point_error_types:
        error_box.setIcon(QMessageBox.Information)
        error_box.setWindowTitle("提示")
    elif exc_type == TimeoutError:
        error_box.setDetailedText("")
    else:
        error_box.setIcon(QMessageBox.Critical)
        error_box.setWindowTitle("错误: " + str(exc_type))

    try:
        name = getattr(exc_value, "name")
        if name == 'project_struct':
            error_box.setText("没有处于打开状态的项目，请先执行【文件】->【打开项目】或【新建项目】")
        else:
            error_box.setText(str(exc_value))
        error_box.setWindowTitle("提示")
    except:
        error_box.setText(str(exc_value))
        error_box.setWindowTitle("提示")


    error_box.exec()


sys.excepthook = handle_global_execution
