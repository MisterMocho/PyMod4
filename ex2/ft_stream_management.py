import sys


def ft_stream_management() -> None:
    """Takes inputs and prints using both functions and sys. operations"""
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===\n")
    id: str = input("Input Stream Active. Enter archivist ID: ")
    print("Input Stream Active. Enter status report: ", end="")
    sys.stdout.flush()
    status: str = sys.stdin.readline().strip()
    print("")
    sys.stdout.write(f"[STANDARD] Archive status from {id}: {status}\n")
    sys.stderr.write("[ALERT] System diagnostic: "
                     "Communication channels verified\n")
    sys.stdout.write("[STANDARD] Data transmission complete\n")
    print("\nThree-channel communication test successful")


if __name__ == "__main__":
    ft_stream_management()
