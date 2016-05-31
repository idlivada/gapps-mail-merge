import getpass

# Change every time
GDOCS_WORKSHEET = 'Q2 2016 Skip Level Meetings'
SUBJECT = "%s, 1-on-1 this quarter"
BODY = """
Hi %s,

I'd like to schedule a 1-on-1 meeting with you sometime this quarter.  

I know you already have 1-on-1 meetings with your direct manager, but this is an opportunity for you to provide feedback to me directly about the company as a whole and areas where we can improve,  I will also have some specific questions for you at that time to help drive the discussion.  

The whole meeting is meant to be pretty informal if you haven't done one before.

When you get a chance, can you please pick a date and time that works for you here http://bit.ly/PawanSkipLevel? (see the Friday 3-4 PM time slots every week)

Thanks,
Pawan

---
Pawan Deshpande
CEO | Curata. (www.curata.com) | 617 229 5555
"""

# Change sometimes
EMAIL_HOST_USER = 'pawan@curata.com'
EMAIL_FROM_NAME = "Pawan Deshpande"
EMAIL_FROM_ADDRESS = 'pawan@curata.com'
EMAIL_TO_SALESFORCE = ''#emailtosalesforce@49nix7gb1zncztbrslzxaeo3y.in.salesforce.com'

GDOCS_USERNAME = 'pawan@curata.com'
GDOCS_NAME = "Mail Merges"
GDOCS_MAX_ROWS = 50

USE_FULL_NAME = False

# Rarely changed
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_PASSWORD = getpass.getpass('Pawword:')







