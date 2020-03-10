from starlette.endpoints import HTTPEndpoint
from starlette.requests import Request
from starlette.responses import Response, UJSONResponse


class BaseResource(HTTPEndpoint):
    async def options(self, request: Request):
        headers = {}
        headers["Access-Control-Allow-Methods"] = ",".join(
            method for method in ("GET", "POST", "PUT", "DELETE", "PATCH") if hasattr(self, method.lower())
        )
        return Response(headers=headers)


class SmokeResource(BaseResource):
    async def get(self, request):
        return UJSONResponse({"hello": "world"})
