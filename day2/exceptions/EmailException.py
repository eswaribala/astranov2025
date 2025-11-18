class EmailException(Exception):
    """Custom exception for email-related errors."""
    def __init__(self, message):
        super().__init__(message)
        self.message = message

    def __str__(self):
        return f"EmailException: {self.message}"