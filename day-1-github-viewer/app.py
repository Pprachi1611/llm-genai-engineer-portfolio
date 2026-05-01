import requests

username = input("Enter GitHub username: ")

url = f"https://api.github.com/users/{username}"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    
    print("\n--- GitHub Profile ---")
    print("Name:", data.get("name"))
    print("Followers:", data.get("followers"))
    print("Following:", data.get("following"))
    print("Repos:", data.get("public_repos"))
    print("Repos:", data.get("bio"))
    

else:
    print("User not found!")