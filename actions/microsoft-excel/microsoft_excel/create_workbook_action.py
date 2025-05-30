from typing import Literal

from sema4ai.actions import OAuth2Secret, Response, action

from microsoft_excel._client import Client, _create_workbook  # noqa: F401
from microsoft_excel.models.workbook import Workbook


@action(is_consequential=True)
def create_workbook(
    workbook_name: str,
    token: OAuth2Secret[
        Literal["microsoft"],
        list[Literal["Files.ReadWrite"]],
    ],
) -> Response[Workbook]:
    """Creates a new empty workbook (Excel document).

    Args:
        token: The OAuth2 access token .
        workbook_name: Name of the new worksheet (Excel document)
    Returns:
        Structured data containing information about the new workbook.
    """

    client = Client(token)
    return Response(result=_create_workbook(client, workbook_name))
