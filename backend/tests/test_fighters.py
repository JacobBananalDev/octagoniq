def test_create_fighter(client, admin_token):
    payload = {
        "first_name": "Jon",
        "last_name": "Jones",
        "height_cm": 190,
        "reach_cm": 84,
        "stance": "Southpaw"
    }
    
    headers = {
        "Authorization": f"Bearer {admin_token}"
    }

    response = client.post("/fighters", json=payload, headers=headers)

    assert response.status_code == 201

    data = response.json()
    assert data["first_name"] == "Jon"
    assert data["last_name"] == "Jones"
    assert data["height_cm"] == 190
    assert data["reach_cm"] == 84
    assert data["stance"] == "Southpaw"
    
def test_create_and_get_fighter(client):
    payload = {
        "first_name": "Khabib",
        "last_name": "Nurmagomedov",
        "stance": "Southpaw",
        "height_cm": 190,
        "reach_cm": 188
    }

    # Create fighter
    create_response = client.post("/fighters", json=payload)
    assert create_response.status_code == 201

    fighter_id = create_response.json()["id"]

    # Fetch fighter
    get_response = client.get(f"/fighters/{fighter_id}")
    assert get_response.status_code == 200

    data = get_response.json()
    assert data["first_name"] == "Khabib"
    assert data["last_name"] == "Nurmagomedov"
    
def test_get_nonexistent_fighter(client):
    response = client.get("/fighters/99999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Fighter not found"
    
def test_get_fighters_pagination(client):
    # Create 3 fighters
    for i in range(3):
        client.post("/fighters", json={
            "first_name": f"Test{i}",
            "last_name": "Fighter",
            "height_cm": 190,
            "reach_cm": 70
        })

    response = client.get("/fighters?skip=1&limit=1")
    assert response.status_code == 200

    data = response.json()
    assert len(data) == 1