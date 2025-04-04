import json

# Paths to the JSON files
chat_log_path = r"Data\ChatLog.json"
long_memory_path = r"Data\LongMemory.json"

# Function to clear JSON files
def clear_chat_history():
    empty_data = []
    
    # Overwrite ChatLog.json
    with open(chat_log_path, "w") as chat_file:
        json.dump(empty_data, chat_file, indent=4)
    
    # Overwrite LongMemory.json
    with open(long_memory_path, "w") as memory_file:
        json.dump(empty_data, memory_file, indent=4)

    print("✅ Chat history cleared successfully!")

# Run the function
clear_chat_history()
