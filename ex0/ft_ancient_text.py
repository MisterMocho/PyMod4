def ft_ancient_text() -> None:
    """Reads, displays and closes the content of a txt file"""
    filename: str = "ancient_fragment.txt"
    try:
        with open(filename, "r") as ancient_file:
            data: str = ancient_file.read()
            print(
                "=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n"
                f"\nAccessing Storage Vault: {filename}\n"
                "Connection established...\n"
                "\nRECOVERED DATA:\n"
                f"{data.strip()}\n"
                "\nData recovery complete. Storage unit disconnected."
            )
    except FileNotFoundError:
        print("ERROR: Storage vault not found. Run data generator first.")
    except PermissionError:
        print("ERROR: Access denied. Archivist clearance insufficient.")
    except Exception as e:
        print(f"ERROR: An unexpected anomaly occurred: {e}")


if __name__ == "__main__":
    ft_ancient_text()
