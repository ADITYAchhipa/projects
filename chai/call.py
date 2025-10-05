from omnidimension import Client
import time

api_key = "d5ed79f2e67c00d773a1a01bc13f5128"
client = Client(api_key)

# Reuse existing agent or create a new one
agent_response = client.agent.create(
    name="AI Sales Agent",
    welcome_message="""Hi, this is an AI calling on behalf of Aditya. We're offering an AI integration service for schools to improve student performance. Are you interested in hearing more about it? Please say 'Yes' or any response.""",
    context_breakdown=[
        {"title": "Agent Role & Context", "body": """You are a representative of Aditya, calling potential customers, specifically school representatives, to offer an AI integration service. Your goal is to introduce the service and capture the customer's interest level.""", "is_enabled": True},
        {"title": "Introduction", "body": """Introduce the AI agent and the purpose of the call clearly and concisely.""", "is_enabled": True},
        {"title": "Purpose Statement", "body": """Deliver a short message about the AI integration service for schools to enhance student performance by monitoring progress and identifying areas for improvement.""", "is_enabled": True},
        {"title": "Response Handling", "body": """Capture the recipient's verbal response and record their name and phone number.""", "is_enabled": True},
        {"title": "Closing Statement", "body": """Politely inform the recipient that their response has been recorded and they may now disconnect the call.""", "is_enabled": True}
    ],
    call_type="Outgoing",
    transcriber={
        "provider": "deepgram_stream",
        "silence_timeout_ms": 400,
        "model": "nova-3",
        "numerals": True,
        "punctuate": True,
        "smart_format": True,
        "diarize": False
    },
    model={
        "model": "azure-gpt-4o-mini",
        "temperature": 0.7
    },
    voice={
        "provider": "eleven_labs",
        "voice_id": "cgSgspJ2msm6clMCkdW9"
    },
    web_search={
        "enabled": True,
        "provider": "openAI"
    },
)

agent_id = agent_response["id"]

# Make the call to Aditya
call_response = client.call.create(
    agent_id=agent_id,
    phone_number="+919636178953",
    metadata={"name": "Aditya"}
)

print(f"Calling Aditya...")
time.sleep(20)  # Wait for call to complete

# Get transcript
transcript = client.transcript.get(call_response["id"])
print(f"🗣 Response: {transcript.get('text', 'No response')}")