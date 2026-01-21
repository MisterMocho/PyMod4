import os


def ft_vault_security() -> None:
    """Reads, takes info from a different file and appends it safely"""
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")
    vault_file: str = "classified_data.txt"
    source_file: str = "security_protocols.txt"
    print("Initiating secure vault access...")
    try:
        with open(vault_file, "r") as vault:
            print("Vault connection established with failsafe protocols\n")
            current_data: str = vault.read().strip()
            print(f"SECURE EXTRACTION:\n{current_data}\n")
    except FileNotFoundError:
        print(f"Error: Vault '{vault_file}' missing")
        return
    except PermissionError:
        print(
            f"Error: Vault '{vault_file}' has been sealed shut. No access.\n"
            "To renew permission run: chmod 644 classified_data.txt on "
            "the administrative console!"
        )
        return
    try:
        with open(source_file, "r") as source:
            new_protocol: str = source.read().strip()
    except FileNotFoundError:
        print(f"Error: Source '{source_file}' missing. Run the setup commands")
        return
    try:
        with open(vault_file, "a") as vault:
            print(f"SECURE PRESERVATION:\n{new_protocol}")
            vault.write(f"\n{new_protocol}")
    except Exception as e:
        print(f"Error during preservation: {e}")
        return
    try:
        os.chmod(vault_file, 0o000)
        print("\nSecurity Protocol Active: Vault permissions rescinded")
    except Exception as e:
        print(f"\nWarning: Could not lock vault: {e}\n")
    print(
        "Vault automatically sealed upon completion\n"
        "\nAll vault operations completed with maximum security"
    )
# to add permissions to the file again run chmod 644 classified_data.txt


if __name__ == "__main__":
    ft_vault_security()
