# import subprocess
# import re
#
# def get_wifi_password():
#     try:
#         result = subprocess.run(['netsh', 'wlan', 'show', 'profiles'], capture_output=True, text=True, check=True)
#         profiles = re.findall(r':\s(.*)', result.stdout)
#         profiles.remove("Babi's iPhone")
#         for profile in profiles:
#             if profile != "":
#                 profile = profile.strip()
#                 password_result = subprocess.run(['netsh', 'wlan', 'show', 'profile', profile, 'key=clear'], capture_output=True, text=True, check=True)
#                 password = re.search(r'Key Content\s+:\s(.*)', password_result.stdout)
#                 if password:
#                     print(f"SSID: {profile}, Password: {password.group(1)}")
#                 else:
#                     print(f"SSID: {profile}, Password not found")
#     except subprocess.CalledProcessError as e:
#         print("Error:", e)
#
# # Call the function to get WiFi passwords
# get_wifi_password()


import subprocess

def get_wifi_password():
    try:
        result = subprocess.run(['netsh', 'wlan', 'show', 'profile'], capture_output=True, text=True, check=True)
        profiles = result.stdout.split('\n')
        for profile in profiles:
            if 'All User Profile' in profile:
                ssid = profile.split(':')[1].strip()
                if ssid == "Babi's iPhone":
                    ssid = 'Babi Samineedi'
                password_result = subprocess.run(['netsh', 'wlan', 'show', 'profile', ssid, 'key=clear'], capture_output=True, text=True, check=True)
                password_lines = password_result.stdout.split('\n')
                for line in password_lines:
                    if 'Key Content' in line:
                        password = line.split(':')[1].strip()
                        print(f"SSID: {ssid}, Password: {password}")
    except subprocess.CalledProcessError as e:
        print("Error:", e)

# Call the function to get WiFi passwords
get_wifi_password()
