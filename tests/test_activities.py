from src import app as app_module

# AAA: Arrange, Act, Assert

def test_get_activities(client):
    # Arrange (fixture)
    # Act
    r = client.get("/activities")
    # Assert
    assert r.status_code == 200
    data = r.json()
    assert "Chess Club" in data


def test_successful_signup(client):
    # Arrange
    email = "new@mergington.edu"
    activity = "Chess Club"
    # Act
    r = client.post(f"/activities/{activity}/signup", params={"email": email})
    # Assert
    assert r.status_code == 200
    assert email in client.get("/activities").json()[activity]["participants"]


def test_duplicate_signup(client):
    # Arrange
    email = "michael@mergington.edu"  # already registered in initial data
    activity = "Chess Club"
    # Act
    r = client.post(f"/activities/{activity}/signup", params={"email": email})
    # Assert
    assert r.status_code == 400


def test_signup_full(client):
    # Arrange
    activity = "Programming Class"
    app_module.activities[activity]["participants"] = [f"p{i}@x.com" for i in range(app_module.activities[activity]["max_participants"])]
    email = "extra@x.com"
    # Act
    r = client.post(f"/activities/{activity}/signup", params={"email": email})
    # Assert
    assert r.status_code == 400


def test_unregister_success(client):
    # Arrange
    email = "michael@mergington.edu"
    activity = "Chess Club"
    # Act
    r = client.delete(f"/activities/{activity}/signup", params={"email": email})
    # Assert
    assert r.status_code == 200
    assert email not in client.get("/activities").json()[activity]["participants"]


def test_unregister_not_registered(client):
    # Arrange
    email = "not@x.com"
    activity = "Chess Club"
    # Act
    r = client.delete(f"/activities/{activity}/signup", params={"email": email})
    # Assert
    assert r.status_code == 400
