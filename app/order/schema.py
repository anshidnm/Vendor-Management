from drf_spectacular.utils import extend_schema_view, extend_schema


class Documentaion:
    """
    Utility class for document vendor related
    API endpoints
    """

    ORDER = extend_schema_view(
        list=extend_schema(
            summary="List all purchase orders",
            description="""
            List all purchase orders availabe in the system.
            Can filter with vendor_id
            """,
            tags=["Purchase Order"],
        ),
        create=extend_schema(
            summary="Create a purchase order",
            description="""
            Create a new purchase order to the system.
            status, quality_rating do not submit while creation.
            items should be submit as JSON, not string
            """,
            tags=["Purchase Order"],
        ),
        update=extend_schema(
            summary="Update a purchase order",
            description="""
            Update a purchase order in the system.
            Should be submit all details of purchase order
            """,
            tags=["Purchase Order"],
        ),
        partial_update=extend_schema(
            summary="Update a purchase order",
            description="""
            Update a purchase order in the system.
            Only submit fields to be updated
            """,
            tags=["Purchase Order"],
        ),
        destroy=extend_schema(
            summary="Delete a purchase order",
            description="""
            Delete a vendor from the system.
            It leads to change in vendor performance data
            """,
            tags=["Purchase Order"],
        ),
        retrieve=extend_schema(
            summary="Get details of a purchase order",
            description="""
            This API returns the details of a specific purchase order
            """,
            tags=["Purchase Order"],
        ),
        acknowledge=extend_schema(
            summary="Acknowledge a purchase order",
            description="""
            This end point used to acknowledge
            a purchase order by it's vendor.
            After the acknowledgement the acknowledge_date
            will be added to the purchase order and response time
            will be calculated for vendor performance.
            """,
            tags=["Acknowledgement"],
        ),
    )
