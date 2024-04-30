from drf_spectacular.utils import extend_schema_view, extend_schema


class Documentaion:
    """
    Utility class for document vendor related
    API endpoints
    """

    VENDOR = extend_schema_view(
        list=extend_schema(
            summary="List all vendors",
            description="""
            List all vendors availabe in the system
            """,
            tags=["Vendor"],
        ),
        create=extend_schema(
            summary="Create a vendor",
            description="""
            Create a new vendor to the system.
            Contact details and address should be filled
            with readable manner.
            """,
            tags=["Vendor"],
        ),
        update=extend_schema(
            summary="Update a vendor",
            description="""
            Update a vendor in the system.
            Should be submit all details of vendor
            """,
            tags=["Vendor"],
        ),
        partial_update=extend_schema(
            summary="Update a vendor",
            description="""
            Update a vendor in the system.
            Only submit fields to be updated
            """,
            tags=["Vendor"],
        ),
        destroy=extend_schema(
            summary="Delete a vendor",
            description="""
            Delete a vendor from the system.
            It leads to removal of all related purchase
            orders to the specific vendor
            """,
            tags=["Vendor"],
        ),
        retrieve=extend_schema(
            summary="Get details of a vendor",
            description="""
            This API returns the details of a specific vendor
            """,
            tags=["Vendor"],
        ),
        performance=extend_schema(
            summary="Performane of a vendor",
            description="""
            List the performance of a vendor.
            The response time given in minutes.
            By default all performance matrices are zero
            """,
            tags=["Vendor Performance"],
        ),
    )

    HISTORY = extend_schema_view(
        list=extend_schema(
            summary="Performane history of a vendor",
            description="""
            List all the perfomance history of a vendor
            according updated time.
            Filters with date are available as query params
            eg:- date__date__gte, date__date__lte
            """,
            tags=["Vendor Performance"],
        )
    )
