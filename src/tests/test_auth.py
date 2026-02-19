from src.auth.schemas import UserCreateModel

auth_prefix=f"api/v1/auth"
def test_user_creation(fake_session,fake_user_service,test_client):

    signup_data={
            "first_name": "string",
            "last_name": "string",
            "username": "string",
            "email": "string",
            "password": "string"
        }
    response=test_client.post(
        url=f"{auth_prefix}/signup",
        json=signup_data,
    )

    user_data=UserCreateModel(**signup_data)
    assert fake_user_service.user_exists_called_once()
    assert fake_user_service.user_exists_called_once(signup_data['email'],fake_session)
    assert fake_user_service.user_exists_called_once()
    assert fake_user_service.user_exists_called_once(user_data,fake_session)
