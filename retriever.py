import requests


def query_db(database_id: str, token: str, only_first_page: bool = True):
    if not database_id or not token:
        raise ValueError("Database ID and token must be provided")
    url = f"https://api.notion.com/v1/databases/{database_id}/query"
    baer_token = f"Bearer {token}"
    headers = {
        "Notion-Version": "2021-05-13",
        "Content-Type": "application/json",
    }
    response = requests.post(
        url,
        headers={
            "Authorization": baer_token,
            **headers,
        },
    )
    if response.status_code != 200:
        raise Exception(f"Error: {response.status_code} - {response.text}")
    data = response.json()
    if only_first_page:
        return data.get("results", [])
    else:
        all_results = data.get("results", [])
        while data.get("has_more"):
            next_cursor = data.get("next_cursor")
            response = requests.post(
                url,
                headers={
                    "Authorization": baer_token,
                    **headers,
                },
                json={"start_cursor": next_cursor},
            )
            if response.status_code != 200:
                raise Exception(f"Error: {response.status_code} - {response.text}")
            data = response.json()
            all_results.extend(data.get("results", []))
        return all_results


def query_page(page_id: str, token: str, only_first_page: bool = True):
    if not page_id or not token:
        raise ValueError("Page ID and token must be provided")
    url = f"https://api.notion.com/v1/blocks/{page_id}/children"
    baer_token = f"Bearer {token}"
    headers = {
        "Notion-Version": "2021-05-13",
        "Content-Type": "application/json",
    }
    response = requests.get(
        url,
        headers={
            "Authorization": baer_token,
            **headers,
        },
    )
    if response.status_code != 200:
        raise Exception(f"Error: {response.status_code} - {response.text}")
    if only_first_page:
        data = response.json()
        return data.get("results", [])
    else:
        data = response.json()
        all_results = data.get("results", [])
        while data.get("has_more"):
            next_cursor = data.get("next_cursor")
            response = requests.get(
                url,
                headers={
                    "Authorization": baer_token,
                    **headers,
                },
                params={"start_cursor": next_cursor},
            )
            if response.status_code != 200:
                raise Exception(f"Error: {response.status_code} - {response.text}")
            data = response.json()
            all_results.extend(data.get("results", []))
        return all_results
