import time
from super_thread import SuperThread


class Timeout:

    # This Function Returns 'False' When Timed Out
    # Else Returns The Function's Returned Value
    @staticmethod
    def timeout(function, timeout):
        def wrapper(*args, **kwargs):
            Res = [Exception('Function [%s] Timeout [%s Seconds] Exceeded!' % (function.__name__, timeout))]

            # Function Level Exception Will Not Get Raised
            def newFunction():
                try:
                    Res[0] = function(*args, **kwargs)
                except Exception as func_exception:
                    Res[0] = func_exception
            timeout_thread = SuperThread('Timeout', newFunction)
            
            # Thread Level Exceptions Will Get Raised
            try:
                timeout_thread.start()
                timeout_thread.join(timeout)
            except Exception as thread_exception:
                print('Failed to Start Timeout-Thread!')
                raise thread_exception
            Return = Res[0]

            # Timeout
            if isinstance(Return, BaseException):
                print(Res[0]) 
                timeout_thread.terminate()
                return False
            return Return
        return wrapper

    # Example:
    # status = Timeout.timeout(function, timeout)(parameters)
    # if not status:
    #   print('Function Call Has Timed Out!')
