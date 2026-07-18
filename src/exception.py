import sys


class CustomException(Exception):
    """
    Custom exception class that provides detailed error information.
    """

    def __init__(self, error_message, error_detail: sys):

        _, _, exc_tb = error_detail.exc_info()

        self.file_name = exc_tb.tb_frame.f_code.co_filename

        self.line_number = exc_tb.tb_lineno

        self.error_message = (
            f"\nError occurred in Python script: [{self.file_name}]"
            f"\nLine Number: [{self.line_number}]"
            f"\nError Message: [{error_message}]"
        )

        super().__init__(self.error_message)

    def __str__(self):

        return self.error_message