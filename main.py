import requests

import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


# ME
def get_posts():
    """
    Fetch all posts from the JSONPlaceholder API.
    Returns:
        list: A list of post dictionaries.
    """
    logging.info("Fetching all posts...")
    url = "https://jsonplaceholder.typicode.com/posts" # url
    response = requests.get(url) # communicates with the API
    response.raise_for_status() # For errors
    return response.json() # returns a dictionary
    

def get_comments(post_id):
    """
    Gets all comments from the JSONPlaceholder API
    Returns:
        list: A list of comment dictionaries.
    """
    comment_url = f"https://jsonplaceholder.typicode.com/posts/{post_id}/comments"
    response = requests.get(comment_url)
    response.raise_for_status()
    return response.json()
    
def create_post(title, body, user_id):
    """
    Creates a post from the JSONPlaceholder API.
    Returns:
        the post you created
    """
    logging.info(f"Creating a new post for user {user_id}...")
    url = "https://jsonplaceholder.typicode.com/posts"
    payload = {"title": title, "body": body, "userId": user_id } # the data we are sending over
    response = requests.post(url, json=payload)
    response.raise_for_status()
    return response.json()

def update_post(post_id, new_title):
    """
    Updates your post
    """
    logging.info(f"Updated post of {post_id}...")
    patch_url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"
    update_data = {"title": new_title}
    response = requests.patch(patch_url, json=update_data)
    response.raise_for_status()
    return response.json()

def main():
    posts = get_posts()
    logging.info(posts[0])
    
    comments = get_comments(1)
    logging.info(comments[0])
    
    new_post = create_post("Yeo", "This is my first post", 99)
    logging.info(new_post)
    
    update = update_post(new_post["id"], "I updated the Title")
    logging.info(update)
    
if __name__ == "__main__":
    main()
