def normalize_email(email):
    # Split the email into user part and domain part
    user_part, domain_part = email.lower().split('@')
    
    # Handle the part before the '+' symbol in user part
    if '+' in user_part:
        user_part = user_part[:user_part.index('+')]
    
    # Remove all dots from the user part
    user_part = user_part.replace('.', '')
    
    # Reassemble the email
    normalized_email = user_part + '@' + domain_part
    return normalized_email

def count_unique_emails(emails):
    unique_emails = set()
    for email in emails:
        normalized_email = normalize_email(email)
        unique_emails.add(normalized_email)
    return len(unique_emails)

# Example usage:
# Dataset handling
num_datasets = int(input("Enter the number of datasets: "))
results = []
for _ in range(num_datasets):
    n = int(input("Enter number of emails in the dataset: "))
    emails = [input().strip() for _ in range(n)]
    unique_count = count_unique_emails(emails)
    results.append(unique_count)

for result in results:
    print(result)