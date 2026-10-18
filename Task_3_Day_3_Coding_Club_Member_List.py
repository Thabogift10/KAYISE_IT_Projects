# TASK 3: Coding Club Member List
# Topics: lists, append, len, sort, for, while, continue, in, strip, lower

members = []

print("=== Coding Club Registration ===")

while True:
    name = input("Enter member name (or type done to finish): ").strip()

    if name.lower() == "done":
        break
    elif name.lower() == "":
        print("Name cannot be empty")
        continue
    else:
        members.append(name)

print(f"\nTotal members: {len(members)}")
members.sort(key=str.casefold)

print("\nRegistered members:")
for number, member in enumerate(members, start=1):
    print(f"{number}. {member}")

search_name = input("Enter a member name to search for: ").strip().lower()

for member in members:
    if member.lower() == search_name:
        print(f"{search_name} is a member of the Coding Club.")
        break
else:
    print(f"{search_name} is not a member of the Coding Club.")
