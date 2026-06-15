import requests
import json

def gihub_api_request(url, headers=None):
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None

def get_repo_info(owner, repo, headers=None):
    url = f"https://api.github.com/repos/{owner}/{repo}"
    return gihub_api_request(url, headers)

def get_branches(owner, repo, headers=None):
    url = f"https://api.github.com/repos/{owner}/{repo}/branches"
    return gihub_api_request(url, headers)

def get_commits(owner, repo, headers=None):
    url = f"https://api.github.com/repos/{owner}/{repo}/commits"
    return gihub_api_request(url, headers)

def get_workflows(owner, repo, headers=None):
    url = f"https://api.github.com/repos/{owner}/{repo}/actions/workflows"
    return gihub_api_request(url, headers)

def get_workflow_runs(owner, repo, workflow_id, headers=None):
    url = f"https://api.github.com/repos/{owner}/{repo}/actions/workflows/{workflow_id}/runs"
    return gihub_api_request(url, headers)

# Bug 2 fixed: initialise branches as empty list to avoid duplication
def process_data(repo_data, branches):
    result = {
        "repository": {
            "name": repo_data.get("name"),
            "owner": repo_data.get("owner", {}).get("login"),
            "description": repo_data.get("description"),
            "stars": repo_data.get("stargazers_count"),
            "forks": repo_data.get("forks_count"),
        },
        "branches": [],
    }
    if branches:
        for branch in branches:
            result["branches"].append({
                "name": branch.get("name")
            })
    return result

def save_to_json(data, filename):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

def print_json(data):
    print("\n =============REPOSITORY DETAILS==================\n")
    print(f"Repository Name: {data['repository']['name']}")
    print(f"Owner: {data['repository']['owner']}")
    print(f"Forks: {data['repository']['forks']}")

    print("\n =============BRANCHES==================\n")
    for branch in data['branches']:
        print(f"Branch Name: {branch['name']}")

def main():
    owner = input("Enter the repository owner: ").strip()
    repo = input("Enter the repository name: ").strip()
    token = input(
        "Enter your GitHub personal access token (Press enter to skip): "
    ).strip()

    headers = {}

    # Bug 3 fixed: set header first, then always fetch repo_data outside the if block
    if token:
        headers['Authorization'] = f"token {token}"

    repo_data = get_repo_info(owner, repo, headers)
    if not repo_data:
        print("Repository not found or an error occurred while fetching the data.")
        return

    branches = get_branches(owner, repo, headers)

    result = process_data(repo_data, branches)

    print_json(result)
    save_to_json(result, 'output.json')
    print("Data saved to output.json")

if __name__ == "__main__":
    main()