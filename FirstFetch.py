import requests

def fetch_todos():
    response = requests.get("https://jsonplaceholder.typicode.com/todos")
    
    if response.status_code == 200:
        todos = response.json()
        for todo in todos[:10]:
            print(f"ID: {todo['id']}, Title: {todo['title']}, Completed: {todo['completed']}")
    else:
        print("Failed to fetch data. Status code:", response.status_code)

if __name__ == "__main__":
    fetch_todos()
  