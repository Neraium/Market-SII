from fastapi import Header, HTTPException


async def require_api_key(x_api_key: str | None = Header(default=None)):
    if x_api_key is None:
        raise HTTPException(status_code=401, detail="Missing API key")

    return {
        "authenticated": True,
        "api_key": x_api_key,
    }
