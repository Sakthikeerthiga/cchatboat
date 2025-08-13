import requests

# Test the updated API endpoints
base_url = "http://localhost:8000"

print("Testing ChatBoat API with answers...")
print("=" * 50)

# Test jobs endpoint
response = requests.get(f"{base_url}/jobs")
if response.status_code == 200:
    jobs = response.json()
    print(f"✅ Jobs endpoint working: {len(jobs)} jobs found")
    for job in jobs:
        print(f"  - {job['name']} (ID: {job['id']})")
else:
    print(f"❌ Jobs endpoint failed: {response.status_code}")

print()

# Test questions with answers for first job
if jobs:
    job_id = jobs[0]['id']
    response = requests.get(f"{base_url}/jobs/{job_id}/questions")
    if response.status_code == 200:
        questions = response.json()
        print(f"✅ Questions endpoint working for {jobs[0]['name']}: {len(questions)} questions found")
        for i, q in enumerate(questions, 1):
            print(f"  Q{i}: {q['name']}")
            if 'answer' in q:
                print(f"     Answer: {q['answer'][:100]}...")
            else:
                print(f"     ❌ No answer field found")
    else:
        print(f"❌ Questions endpoint failed: {response.status_code}")

print()
print("Note: If answers are missing, restart the backend to pick up changes.")
