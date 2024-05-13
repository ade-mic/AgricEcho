# AgricEcho
AgricEcho is a blogging website focused on agricultural news and environmental topics. 
The Blogging Platform is built on Flask! This is a simple yet powerful blogging platform built with Flask, a lightweight WSGI web application framework. It's designed to make getting started quick and easy, with the ability to scale up to complex applications.


## Features

- **User Authentication**: Sign up, sign in, and log out functionality.
- **User Dashboard**: Authenticated users can view their posts.
- **Post Articles**: Authenticated users can create new blog posts.
- **View Posts**: All visitors can view full content of a post.
- **Home Page**: Displays all blog posts.

## Setup
### Prerequisites
- Python 3.x
- MySQL  5.7.42
### Installing
1. Clone the repository:
```bash
git clone git@github.com:ade-mic/AgricEcho.git
```
```bash
cd AgricEcho
```
2.  Create a virtual environment and activate it:
```bash
python3 -m venv venv
```
```bash 
source venv/bin/activate  # Linux/macOS
```
```bash
venv\Scripts\activate      # Windows
```
3. Install dependencies:
```bash
pip install -r requirements.txt
```
4. Run the application
```bash
./app.py
```

## Built With
- Flask - The web framework used
- Python - The programming language used

## Contributing
We welcome contributions from the community! To contribute:

## Fork the repository.
Create a new branch (git checkout -b feature/your-feature).
Commit your changes (git commit -am 'Add new feature').
Push to the branch (git push origin feature/your-feature).
Create a new Pull Request.
## License
This project is licensed under the MIT License - see the LICENSE file for details.