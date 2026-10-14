def validate_affected_users(value):
    """Validate that affected_users is a positive whole number.

    Rejects booleans even though Python treats bool as a subclass of int.
    """
    if isinstance(value, bool) or not isinstance(value, int):
        raise ValueError("Affected users must be a whole number.")

    if value <= 0:
        raise ValueError("Affected users must be greater than zero.")

    return value

def validate_title(title):
    """Validate and normalise a ticket title.

    Returns the trimmed title.
    Raises ValueError if the title is not a non-empty string.
    """
    if not isinstance(title, str):
        raise ValueError("Title must be text.")

    trimmed_title = title.strip()

    if not trimmed_title:
        raise ValueError("Title cannot be blank.")

    return trimmed_title

VALID_CATEGORIES = {
    "network": "Network",
    "hardware": "Hardware",
    "software": "Software",
    "other": "Other",
}


def validate_category(category):
    """Validate and normalise a ticket category.

    Accepts case-insensitive input and returns a canonical category.
    Raises ValueError for unknown or non-text categories.
    """
    if not isinstance(category, str):
        raise ValueError("Category must be text.")

    normalized = category.strip().casefold()

    if normalized not in VALID_CATEGORIES:
        raise ValueError(
            "Category must be Network, Hardware, Software or Other."
        )

    return VALID_CATEGORIES[normalized]

VALID_URGENCIES = {"low", "medium", "high"}


def validate_urgency(urgency):
    """Validate and normalise ticket urgency.

    Accepts case-insensitive input and returns lowercase urgency.
    Raises ValueError for unknown or non-text urgency values.
    """
    if not isinstance(urgency, str):
        raise ValueError("Urgency must be text.")

    normalized = urgency.strip().casefold()

    if normalized not in VALID_URGENCIES:
        raise ValueError("Urgency must be low, medium or high.")

    return normalized

def validate_staff_label(staff_label):
    """Validate and normalise a staff assignment label.

    Returns the trimmed staff label.
    Raises ValueError if the label is not a non-empty string.
    """
    if not isinstance(staff_label, str):
        raise ValueError("Staff label must be text.")

    trimmed_label = staff_label.strip()

    if not trimmed_label:
        raise ValueError("Staff label cannot be blank.")

    return trimmed_label

MIN_NOTE_MESSAGE_LENGTH = 5
MAX_NOTE_MESSAGE_LENGTH = 300


def validate_note_message(message):
    """Validate and normalise a follow-up note message.

    Returns the trimmed message.
    Raises ValueError if the message is not text or is outside
    the allowed 5-300 character range after trimming.
    """
    if not isinstance(message, str):
        raise ValueError("Note message must be text.")

    trimmed_message = message.strip()
    message_length = len(trimmed_message)

    if message_length < MIN_NOTE_MESSAGE_LENGTH:
        raise ValueError(
            "Note message must be at least 5 characters long."
        )

    if message_length > MAX_NOTE_MESSAGE_LENGTH:
        raise ValueError(
            "Note message must be no more than 300 characters long."
        )

    return trimmed_message