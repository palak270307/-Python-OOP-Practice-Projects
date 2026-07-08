import requests

class GithubProfileViewer:
    def __init__(self):
        self.base_url = "https://api.github.com/users/"
    
    def get_profile(self,username):
        url = self.base_url + username
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            return None

viewer = GithubProfileViewer()

username = input("Enter your Github username: ")
profile_data = viewer.get_profile(username)
if profile_data:
    print(f"Name: {profile_data.get('name')}")
    print(f"Public Repos: {profile_data.get('public_repos')}")
    print(f"Followers: {profile_data.get('followers')}")
    print(f"Following: {profile_data.get('following')}")
    print(f"Bio: {profile_data.get('bio')}")
else:
    print("User Not Found!")