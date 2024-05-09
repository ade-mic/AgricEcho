#!/usr/bin/python3
import requests

base_url = 'http://localhost:5000'

def test_get_all_posts():
    response = requests.get(f'{base_url}/api/posts')
    if response.status_code == 200:
        print('All posts:')
        print(response.json())
    else:
        print(response)
        print('Failed to get all posts.')

def test_create_post():
    data = {'title': 'Test Post', 'content': 'This is a test post.'}
    response = requests.post(f'{base_url}/posts', json=data)
    if response.status_code == 201:
        print('Post created successfully.')
    else:
        print(response)
        print('Failed to create post.')

def test_get_post_by_id(post_id):
    response = requests.get(f'{base_url}/posts/{post_id}')
    if response.status_code == 200:
        print(f'Post with ID {post_id}:')
        print(response.json())
    else:
        print (response)
        print(f'Failed to get post with ID {post_id}.')

if __name__ == '__main__':
    # Run your test cases
    test_get_all_posts()
    test_create_post()
    test_get_post_by_id(1)  # Replace 1 with an actual post ID for testing
