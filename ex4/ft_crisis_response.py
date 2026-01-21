def handle_crisis(filename: str) -> None:
    """Attempts to access files and hadle specific errors"""
    try:
        with open(filename, "r") as archive:
            content = archive.read().strip()
            if "DATA_CORRUPTION_ERROR" in content:
                raise ValueError("Data integrity verification failed")
            print(
                f"ROUTINE ACCESS: attempting access to '{filename}'\n"
                f"SUCCESS: Archive recovered - ''{content}''\n"
                "STATUS: Normal operations resumed\n"
            )
    except FileNotFoundError:
        print(
            f"CRISIS ALERT: Attempting access to '{filename}'\n"
            "RESPONSE: Archive not found in the matrix\n"
            "STATUS: Crisis handled, system stable\n"
        )
    except PermissionError:
        print(
            f"CRISIS ALERT: Attempting access to '{filename}'\n"
            "RESPONSE: Security protocols deny access\n"
            "STATUS: Crisis handled, security maintained\n"
        )
    except Exception as e:
        print(
            f"CRISIS ALERT: Attempting access to '{filename}'\n"
            f"RESPONSE: Unexpected system anomaly: {e}\n"
            "STATUS: Crisis handled, system stable\n"
        )


def ft_crisis_response() -> None:
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")
    handle_crisis("lost_archive.txt")
    handle_crisis("classified_data.txt")
    handle_crisis("corrupted_archive.txt")
    handle_crisis("standard_archive.txt")
    print("All crisis scenarios handled successfully. Archives secure.")


if __name__ == "__main__":
    ft_crisis_response()
