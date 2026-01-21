def ft_archive_creation() -> None:
    """Creates and writes data directly to a file"""
    filename: str = "new_discovery.txt"
    print(
        "=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n"
        "\nInitializing new storage unit: new_discovery.txt"
    )
    archive = open(filename, "w")
    print(
        "Storage unit created successfully...\n"
        "\nInscribing preservation data..."
    )
    entry_1 = "[ENTRY 001] New quantum algorithm discovered\n"
    entry_2 = "[ENTRY 002] Efficiency increased by 347%\n"
    entry_3 = "[ENTRY 003] Archived by Data Archivist trainee\n"
    archive.write(entry_1)
    print(f"{entry_1.strip()}")
    archive.write(entry_2)
    print(f"{entry_2.strip()}")
    archive.write(entry_3)
    print(f"{entry_3.strip()}")
    archive.close()
    print(
        "\nData inscription complete. Storage unit sealed.\n"
        f"Archive '{filename}' ready for long-term preservation."
    )


if __name__ == "__main__":
    ft_archive_creation()
