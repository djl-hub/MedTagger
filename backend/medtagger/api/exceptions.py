"""Exceptions used across whole API."""
from medtagger.exceptions import MedTaggerException


class BaseHTTPException(MedTaggerException):
    """Base class for all HTTP Exceptions."""

    pass  # pylint: disable=unnecessary-pass


class UnauthorizedException(BaseHTTPException):
    """Exception designed to use once there was an authorization error during business logic processing."""

    pass  # pylint: disable=unnecessary-pass


class NotFoundException(BaseHTTPException):
    """Exception designed to use while the object that user was looking for could not be found."""

    pass  # pylint: disable=unnecessary-pass


class InvalidArgumentsException(BaseHTTPException):
    """Exception designed to use with invalid arguments (400 status code)."""

    pass  # pylint: disable=unnecessary-pass


class AccessForbiddenException(BaseHTTPException):
    """Exception designed to use while the user does not have a privilege to perform action."""

    pass  # pylint: disable=unnecessary-pass
