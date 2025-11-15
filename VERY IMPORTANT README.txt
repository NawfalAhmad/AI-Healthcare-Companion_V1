⚠️ Important Note About OpenAI API Error (For Anyone Cloning This Project)

During development, an error occurred when using the OpenAI API:

----------------------------------------------------
Error code: 429 - You exceeded your current quota. -
Please check your plan and billing details.	   -
----------------------------------------------------

This happened because OpenAI deprecated older APIs (openai.ChatCompletion), and newer API versions require different code.
Additionally, the API key used during development eventually ran out of free quota, causing the model to stop responding.

Why This Matters for You

If you clone this project and try to run it with OpenAI:

You must use a paid or active API key with remaining quota.

You need to use the new OpenAI Python SDK syntax (client = OpenAI() → client.chat.completions.create(...)).

If you use a newer openai>=1.0.0 version, the old v0.28 syntax will NOT work.

How We Fixed It

To avoid recurring API issues, the backend in this repository has been updated to use:

✅ GPT4All — a fully local, offline LLM
No API key
No billing
No network usage
No quota errors

The model runs entirely on your device and integrates directly with the backend.

If You Still Want to Use OpenAI

Replace the API call in main.py with the new OpenAI SDK code and add your own API key inside a .env file.