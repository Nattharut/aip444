# `pip install requests`
import requests
import os
import json
import time

# Next to this script, so it works no matter which folder you run it from.
notes_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "notes.md")


def test_server():
    try:
        print(f"📖 Reading notes from: {notes_path}")
        with open(notes_path, "r", encoding="utf-8") as f:
            notes_content = f.read()

        # 2. Prepare the payload
        payload = {
            "notes": notes_content,
            "cards": 2
        }

        print("⚡ Sending request to server...")
        start_time = time.time()

        # 3. Send POST request
        response = requests.post(
            "http://localhost:3000/api/generate",
            json=payload
        )

        end_time = time.time()
        print(f"⏱️  Request took {end_time - start_time:.2f}s")

        # 4. Handle Response
        if response.status_code != 200:
            print(f"❌ Server error {response.status_code}: {response.text}")
            return

        data = response.json()

        # 5. Pretty Print the JSON
        print("\n✅ Success! Received Structured Data:")
        print(json.dumps(data, indent=2))

    except FileNotFoundError:
        print(f"❌ Error: Could not find file at {notes_path}")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    test_server()
