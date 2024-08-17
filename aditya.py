import instaloader
import os

def fetch_user_data(username):
    L = instaloader.Instaloader()
    session_dir = 'c:\\users\\tasne\\appdata\\local\\temp\\.instaloader-tasne'
    session_file_name = 'session-jaanureddy_06'
    session_file_path = os.path.join(session_dir, session_file_name)

    # Print session directory and file path
    # print(f"Session directory: {session_dir}")
    # print(f"Session file path: {session_file_path}")

    # Ensure the session directory exists
    if not os.path.exists(session_dir):
        os.makedirs(session_dir)

    # Attempt to load the session from file if it exists
    if os.path.exists(session_file_path):
        try:
            L.load_session_from_file(session_file_name, session_file_path)
        except Exception as e:
            print(f"Error loading session: {e}")
            return None
    else:
        # Log in and save the session to file
        try:
            L.login('ash_cartel52', 'ADITYA@5253')
            L.save_session_to_file(session_file_path)
        except instaloader.exceptions.TwoFactorAuthRequiredException:
            verification_code = input("Enter the 2FA verification code: ")
            L.two_factor_login(verification_code)
            L.save_session_to_file(session_file_path)
        except instaloader.exceptions.BadCredentialsException:
            print("Login error: Wrong password. Please check your credentials.")
            return None
        except instaloader.exceptions.ConnectionException as e:
            print(f"Connection error: {e}")
            return None

    # Continue with fetching user data
    try:
        profile = instaloader.Profile.from_username(L.context, username)
        return profile
    except instaloader.exceptions.ProfileNotExistsException:
        print(f"Profile {username} does not exist.")
        return None
    except instaloader.exceptions.ConnectionException as e:
        print(f"Connection error: {e}")
        return None

# Example usage
username = 'aditya_a4555'
profile = fetch_user_data(username)
if profile:
    print(f"Profile {profile.username} fetched successfully.")
else:
    print("Failed to fetch profile.")