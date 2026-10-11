import requests

# Task 1: GET all posts
url = "https://jsonplaceholder.typicode.com/posts"

response = requests.get(url)
response.raise_for_status()  # error handling
data = response.json()

# Print first 3 post titles
for post in data[:3]:
    print(post["title"])


# Task 2: GET comments for post 1
comments_url = "https://jsonplaceholder.typicode.com/posts/1/comments"

response = requests.get(comments_url)
response.raise_for_status()
comments = response.json()


# Print each comment's email and body
print("\n--- Comments for Post #1 ---")
for c in comments:
    print(f"Email: {c['email']}")
    print(f"Comment: {c['body']}\n")


# Task 3: Filter posts where userId == 1
user_posts = [post for post in data if post["userId"] == 1]

print("\n--- Posts from userId 1 ---")
print(f"Total posts: {len(user_posts)}")

for p in user_posts[:3]:  # show first 3 for preview
    print(f"ID: {p['id']} - Title: {p['title']}")



# Task 4: POST new data
post_url = "https://jsonplaceholder.typicode.com/posts"

new_post = {
    "title": "Lloyd's Automation Post",
    "body": "This was created automatically.",
    "userId": 99
}

response = requests.post(post_url, json=new_post)
response.raise_for_status()
created_post = response.json()

print("\n--- New Post Created ---")
print(created_post)


# Task 5: PATCH the post we just created
patch_url = f"https://jsonplaceholder.typicode.com/posts/{created_post['id']}"

update_data = {
    "title": "Updated Automation Post"
}

response = requests.patch(patch_url, json=update_data)
response.raise_for_status()
updated_post = response.json()

print("\n--- Post After PATCH Update ---")
print(updated_post)


# Task 6: Pagination simulation
print("\n--- Pagination Simulation ---")

base_url = "https://jsonplaceholder.typicode.com/posts"

for page in range(1, 4):  # pages 1, 2, 3
    params = {
        "_page": page,
        "_limit": 10
    }

    response = requests.get(base_url, params=params)
    response.raise_for_status()
    page_data = response.json()

    print(f"\nPage {page} (showing post IDs):")
    for post in page_data:
        print(post["id"])


# Task 7: Error handling example

def safe_get(url, params=None):
    try:
        response = requests.get(url, params=params, timeout=5)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.Timeout:
        print(f"Timeout error when calling {url}")
    except requests.exceptions.HTTPError as e:
        print(f"HTTP error: {e}")
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
    return None

print("\n--- Error Handling Test ---")
bad_url = "https://jsonplaceholder.typicode.com/INVALID_ENDPOINT"

result = safe_get(bad_url)

print("Result:", result)


# ME
def get_posts():
    # TODO: write the GET logic from Task 1
    pass


def get_comments(post_id):
    # TODO: write the GET logic from Task 2
    pass


def create_post(title, body, user_id):
    # TODO: write the POST logic from Task 4
    pass


def update_post(post_id, new_title):
    # TODO: write the PATCH logic from Task 5
    pass
