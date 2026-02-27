def test_root_redirect(client):
    # Arrange
    # Act
    # The TestClient follows redirects by default; request root and
    # verify that a redirect occurred and the final URL is the index.
    r = client.get("/")
    # Assert final response is OK and a redirect was in the history
    assert r.status_code == 200
    assert any(h.status_code in (302, 307) for h in r.history)
    # `r.url` is a starlette.datastructures.URL object; convert to str
    assert str(r.url).endswith("/static/index.html")


def test_static_index(client):
    # Arrange
    # Act
    r = client.get("/static/index.html")
    # Assert
    assert r.status_code == 200
    assert "Mergington High School" in r.text
