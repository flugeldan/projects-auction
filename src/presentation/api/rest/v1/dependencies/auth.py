from typing import Annotated
from uuid import UUID
from pydantic import BaseModel
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials


class CurrentUser(BaseModel):
    id: UUID


security = HTTPBearer()


async def get_current_user(
    credentials: Annotated[HTTPAuthorizationCredentials, Depends(security)]
) -> CurrentUser:
    token = credentials.credentials
    
    # TODO: Здесь в будущем будет декодирование твоим JWT-декодером/сервисом:
    # try:
    #     payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
    #     return CurrentUser(id=UUID(payload["sub"]))
    # except JWTError:
    #     raise HTTPException(status_code=401, detail="Invalid token")

    # Временная затычка (mock) для тестирования:
    if not token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
        )
    
    # Для теста возвращаем замок с mock-UUID (замени на реальную расшифровку JWT):
    return CurrentUser(id=UUID("11111111-1111-1111-1111-111111111111"))