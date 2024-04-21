import pytest
from contextlib import nullcontext as does_not_raise


@pytest.mark.django_db
@pytest.mark.parametrize("username, password, status_code, expected_error", [
    ["admin", "admin", 200, does_not_raise()],
    ["admin1", "admin2", 401, does_not_raise()],
    [1, "admin", 401, does_not_raise()],
    ["admin", 1, 401, does_not_raise()],
    [None, "admin", 0, pytest.raises(TypeError)],
    ["admin", None, 0, pytest.raises(TypeError)],
])
def test_token(api_client, create_admin, username, password, status_code, expected_error):
    with expected_error:
        response = api_client.post("/token", {"username": username, "password": password})
        assert response.status_code == status_code


@pytest.mark.django_db
def test_user_list(api_client, generate_admin_token):
    headers = {"Authorization": "Bearer " + str(generate_admin_token)}
    response = api_client.get(
        "/user/list",
        headers=headers
    )
    assert response.status_code == 200
