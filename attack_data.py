def phishing_attack():
    return [
        {
            "user": "employee1",
            "event_type": "email",
            "location": "India",
            "details": "Urgent password reset required"
        },
        {
            "user": "employee1",
            "event_type": "login",
            "location": "Russia",
            "details": "Login from new device"
        }
    ]


def insider_attack():
    return [
        {
            "user": "employee2",
            "event_type": "file_access",
            "location": "India",
            "details": "Bulk download of confidential files"
        }
    ]
