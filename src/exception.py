import sys 
import logging
import src.logger 

# We'll call this function whenever there is exception in code
def error_message_detail(error, error_detail:sys):
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occured in python script name [{0}] line number [{1}] error message [{2}]".format(file_name, exc_tb.tb_lineno, str(error))
    return error_message
    
# This is child class of Exception which will redirect the exception to our custom exception function above
class CustomException(Exception):
        def __init__(self, error_message, error_detail:sys):
              super().__init__(error_message)
              self.error_message = error_message_detail(error_message, error_detail=error_detail)

        # This will print custom exception
        def __str__(self):
              return self.error_message
          
        