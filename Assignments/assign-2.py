# Step 1: Get messages from user
num_messages = int(input("Enter the number of messages: "))
messages = []
users = []

for _ in range(num_messages):
    message = input()
    messages.append(message)
    name, _ = message.split(":", 1)
    users.append(name.strip())
def total_messages(messages):
    return f"Total messages: {len(messages)}"
def unique_users(users):
    return f"Unique users in the chat: {set(users)}"
def total_words(messages):
    count = sum(len(msg.split(":")[1].split()) for msg in messages)
    return f"Total words in the chat: {count}"
def average_words(messages):
    total = sum(len(msg.split(":")[1].split()) for msg in messages)
    avg = total / len(messages)
    return f"Average words per message: {round(avg, 2)}"
def longest_message(messages):
    longest = max(messages, key=lambda x: len(x.split(":")[1]))
    return f"Longest message: \"{longest}\""
from collections import Counter

def most_active(users):
    count = Counter(users)
    user, msgs = count.most_common(1)[0]
    return f"Most active user: {user} ({msgs} messages)"

def message_count_by_user(messages, user_name):
    count = sum(1 for msg in messages if msg.startswith(f"{user_name}:"))
    return f"Messages sent by {user_name}: {count}"

from collections import Counter

def most_frequent_word_by_user(messages, user_name):
    words = []
    for msg in messages:
        if msg.startswith(f"{user_name}:"):
            content = msg.split(":", 1)[1].lower().split()
            words.extend(content)
    if words:
        freq = Counter(words)
        return f'Most frequent word used by {user_name}: "{freq.most_common(1)[0][0]}"'
    return "No words found."

def first_last_message_by_user(messages, user_name):
    user_msgs = [msg for msg in messages if msg.startswith(f"{user_name}:")]
    if not user_msgs:
        return f"No messages found for user {user_name}."
    return f"First message by {user_name}: \"{user_msgs[0]}\"\nLast message by {user_name}: \"{user_msgs[-1]}\""

def is_user_present(users, user_name):
    if user_name in users:
        return f"User '{user_name}' is present in the chat."
    else:
        return f"User '{user_name}' not found in the chat."

def common_repeated_words(messages):
    word_count = Counter()
    for msg in messages:
        content = msg.split(":", 1)[1].lower().split()
        word_count.update(content)
    repeated = {word for word, count in word_count.items() if count > 1}
    return f"Common repeated words: {repeated}"

def longest_avg_message_user(messages):
    user_words = {}
    user_counts = {}

    for msg in messages:
        name, content = msg.split(":", 1)
        words = content.strip().split()
        user_words[name] = user_words.get(name, 0) + len(words)
        user_counts[name] = user_counts.get(name, 0) + 1

    avg_lengths = {user: user_words[user]/user_counts[user] for user in user_words}
    max_user = max(avg_lengths, key=avg_lengths.get)
    return f"User with longest average message: {max_user} (avg {round(avg_lengths[max_user], 2)} words)"

def messages_mentioning_user(messages, mention):
    count = sum(1 for msg in messages if mention.lower() in msg.lower())
    return f"Messages mentioning '{mention}': {count}"

def remove_duplicate_messages(messages):
    unique = list(dict.fromkeys(messages))  # preserves order
    return f"Unique messages count: {len(unique)}\n" + "\n".join(unique)

def sort_messages_alphabetically(messages):
    return "\n".join(sorted(messages))

def extract_questions(messages):
    questions = [msg for msg in messages if '?' in msg]
    return "Questions:\n" + "\n".join(questions)

def reply_ratio(messages, from_user, to_user):
    count = 0
    for i in range(1, len(messages)):
        prev_sender = messages[i-1].split(":", 1)[0].strip()
        current_sender = messages[i].split(":", 1)[0].strip()
        if prev_sender == from_user and current_sender == to_user:
            count += 1
    return f"Reply ratio from {to_user} to {from_user}: {count} replies"

def deleted_messages(messages):
    count = sum(1 for msg in messages if "This message was deleted" in msg)
    return f"Deleted messages found: {count}"


def display_menu():
    print("\nMenu Options:")
    print("1. Count total number of messages")
    print("2. Identify unique users in the chat")
    print("3. Count total words in the chat")
    print("4. Calculate average words per message")
    print("5. Find the longest message sent")
    print("6. Find the most active user")
    print("7. Get message count for a specific user")
    print("8. Most frequently used word by a specific user")
    print("9. Retrieve first and last message by a user")
    print("10. Check if a user is present in the chat")
    print("11. Find commonly repeated words")
    print("13. Identify the user with the longest average message length")
    print("14. Count how many messages mention a specific user")
    print("15. Remove duplicate messages")
    print("16. Sort messages alphabetically")
    print("17. Extract all questions asked in the chat")
    print("18. Calculate the reply ratio between two users")
    print("19. Check for deleted messages")
    print("0. Exit")
while True:
    display_menu()
    option = int(input("Enter option number: "))
    
    if option == 0:
        break
    elif option == 1:
        print(total_messages(messages))
    elif option == 2:
        print(unique_users(users))
    elif option == 3:
        print(total_words(messages))
    elif option == 4:
        print(average_words(messages))
    elif option == 5:
        print(longest_message(messages))
    elif option == 6:
        print(most_active(users))
    elif option == 7:
        user = input("Enter user: ")
        print(message_count_by_user(messages, user))

    elif option == 8:
        user = input("Enter user: ")
        print(most_frequent_word_by_user(messages, user))

    elif option == 9:
        user = input("Enter user: ")
        print(first_last_message_by_user(messages, user))

    elif option == 10:
        user = input("Enter user: ")
        print(is_user_present(users, user))

    elif option == 11:
        print(common_repeated_words(messages))

    elif option == 13:
        print(longest_avg_message_user(messages))

    elif option == 14:
        name = input("Enter user to search in messages: ")
        print(messages_mentioning_user(messages, name))

    elif option == 15:
        print(remove_duplicate_messages(messages))

    elif option == 16:
        print(sort_messages_alphabetically(messages))

    elif option == 17:
        print(extract_questions(messages))

    elif option == 18:
        from_user = input("From user: ")
        to_user = input("To user: ")
        print(reply_ratio(messages, from_user, to_user))

    elif option == 19:
        print(deleted_messages(messages))

    
