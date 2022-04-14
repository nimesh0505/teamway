from django.contrib.auth.models import User
from django.urls import reverse


def get_access_token(api_client) -> str:
    EMAIL = "sample@test.com"
    PASSWORD = "example@123"

    user = User.object.create(email=EMAIL, username=EMAIL)
    user.set_password(PASSWORD)
    user.save()

    response = api_client.post(
        reverse("token_obtain_pair"),
        data={"email": EMAIL, "password": PASSWORD},
        format="json",
    )
    response_body = response.json()
    return response_body.get("access")
