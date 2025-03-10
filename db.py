from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client.fitness_tracker
users_collection = db.users

# Fetch all users and print their emails and password hashes
for user in users_collection.find():
    print(f"Email: {user['email']}, Password: {user['password']}")

print("✅ Done checking user passwords!")
