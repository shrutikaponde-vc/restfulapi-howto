# coding: utf-8

from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class PaginatedResponseData(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(
        self,
        total: int = None,
        count: int = None,
        page: int = None,
        size: int = None,
        resources: List[object] = None,
    ):  # noqa: E501
        """PaginatedResponseData - a model defined in Swagger

        :param total: The total of this PaginatedResponseData.  # noqa: E501
        :type total: int
        :param count: The count of this PaginatedResponseData.  # noqa: E501
        :type count: int
        :param page: The page of this PaginatedResponseData.  # noqa: E501
        :type page: int
        :param size: The size of this PaginatedResponseData.  # noqa: E501
        :type size: int
        :param resources: The resources of this PaginatedResponseData.  # noqa: E501
        :type resources: List[object]
        """
        self.swagger_types = {
            "total": int,
            "count": int,
            "page": int,
            "size": int,
            "resources": List[object],
        }

        self.attribute_map = {
            "total": "total",
            "count": "count",
            "page": "page",
            "size": "size",
            "resources": "resources",
        }

        self._total = total
        self._count = count
        self._page = page
        self._size = size
        self._resources = resources

    @classmethod
    def from_dict(cls, dikt) -> "PaginatedResponseData":
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The PaginatedResponseData of this PaginatedResponseData.  # noqa: E501
        :rtype: PaginatedResponseData
        """
        return util.deserialize_model(dikt, cls)

    @property
    def total(self) -> int:
        """Gets the total of this PaginatedResponseData.

        Total amount of resource  # noqa: E501

        :return: The total of this PaginatedResponseData.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total: int):
        """Sets the total of this PaginatedResponseData.

        Total amount of resource  # noqa: E501

        :param total: The total of this PaginatedResponseData.
        :type total: int
        """

        self._total = total

    @property
    def count(self) -> int:
        """Gets the count of this PaginatedResponseData.

        Count of the resources in the current response  # noqa: E501

        :return: The count of this PaginatedResponseData.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count: int):
        """Sets the count of this PaginatedResponseData.

        Count of the resources in the current response  # noqa: E501

        :param count: The count of this PaginatedResponseData.
        :type count: int
        """

        self._count = count

    @property
    def page(self) -> int:
        """Gets the page of this PaginatedResponseData.

        Page number  # noqa: E501

        :return: The page of this PaginatedResponseData.
        :rtype: int
        """
        return self._page

    @page.setter
    def page(self, page: int):
        """Sets the page of this PaginatedResponseData.

        Page number  # noqa: E501

        :param page: The page of this PaginatedResponseData.
        :type page: int
        """

        self._page = page

    @property
    def size(self) -> int:
        """Gets the size of this PaginatedResponseData.

        Number of resource per page  # noqa: E501

        :return: The size of this PaginatedResponseData.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size: int):
        """Sets the size of this PaginatedResponseData.

        Number of resource per page  # noqa: E501

        :param size: The size of this PaginatedResponseData.
        :type size: int
        """

        self._size = size

    @property
    def resources(self) -> List[object]:
        """Gets the resources of this PaginatedResponseData.

        Resources  # noqa: E501

        :return: The resources of this PaginatedResponseData.
        :rtype: List[object]
        """
        return self._resources

    @resources.setter
    def resources(self, resources: List[object]):
        """Sets the resources of this PaginatedResponseData.

        Resources  # noqa: E501

        :param resources: The resources of this PaginatedResponseData.
        :type resources: List[object]
        """

        self._resources = resources