class EmailException(Exception):
    """Custom exception for email-related errors."""
    def __init__(self, message):
        super().__init__(message)
        self.message = message

    