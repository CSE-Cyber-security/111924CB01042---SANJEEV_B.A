"""
Cybersecurity Asset Inventory System
=====================================
A console-based application for managing an organization's IT assets,
tracking their security status, and identifying assets that require
immediate attention.

Features:
    - Add, Search, Update, Delete, and Display assets
    - Classify assets by type and security risk level
    - Persistent storage using JSON
    - Input validation for all fields
    - Security summary dashboard
"""

import json
import os
import re
import sys

# ─── Constants ────────────────────────────────────────────────────────────────

DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data")
DATA_FILE = os.path.join(DATA_DIR, "assets.json")

VALID_ASSET_TYPES = ["Workstation", "Server", "Router", "Switch", "Application"]
VALID_RISK_LEVELS = ["Low", "Medium", "High", "Critical"]
VALID_SECURITY_STATUSES = ["Secure", "Warning", "Vulnerable"]

# ─── Data Persistence ────────────────────────────────────────────────────────

def load_assets():
    """Load assets from the JSON data file."""
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, "r") as f:
            data = json.load(f)
            return data if isinstance(data, list) else []
    except (json.JSONDecodeError, IOError):
        return []


def save_assets(assets):
    """Save assets to the JSON data file."""
    os.makedirs(DATA_DIR, exist_ok=True)
    with open(DATA_FILE, "w") as f:
        json.dump(assets, f, indent=4)


# ─── Input Validation ────────────────────────────────────────────────────────

def validate_ip_address(ip):
    """Validate an IPv4 address format."""
    pattern = r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$"
    match = re.match(pattern, ip)
    if not match:
        return False
    return all(0 <= int(octet) <= 255 for octet in match.groups())


def validate_asset_id(asset_id):
    """Validate that asset ID is non-empty and alphanumeric (with hyphens/underscores)."""
    return bool(re.match(r"^[A-Za-z0-9_-]+$", asset_id))


def get_validated_input(prompt, validator=None, valid_options=None, allow_empty=False):
    """
    Get validated input from the user.

    Args:
        prompt: The input prompt to display.
        validator: An optional function that returns True/False.
        valid_options: An optional list of valid string choices (case-insensitive).
        allow_empty: Whether empty input is allowed (used during updates).

    Returns:
        The validated user input string.
    """
    while True:
        value = input(prompt).strip()

        if allow_empty and value == "":
            return value

        if not value:
            print("  [!] Input cannot be empty. Please try again.")
            continue

        if valid_options:
            # Case-insensitive match; return the canonical form
            for option in valid_options:
                if value.lower() == option.lower():
                    return option
            print(f"  [!] Invalid choice. Valid options: {', '.join(valid_options)}")
            continue

        if validator and not validator(value):
            print("  [!] Invalid format. Please try again.")
            continue

        return value


# ─── Display Helpers ─────────────────────────────────────────────────────────

def display_asset(asset):
    """Display a single asset in formatted output."""
    print(f"  Asset ID     : {asset['asset_id']}")
    print(f"  Asset Name   : {asset['asset_name']}")
    print(f"  Asset Type   : {asset['asset_type']}")
    print(f"  IP Address   : {asset['ip_address']}")
    print(f"  OS           : {asset['os']}")
    print(f"  Department   : {asset['department']}")
    print(f"  Risk Level   : {asset['risk_level']}")
    print(f"  Status       : {asset['security_status']}")


def display_all_assets(assets):
    """Display all assets with a formatted header and summary."""
    if not assets:
        print("\n  [i] No assets found in the inventory.\n")
        return

    print("\n" + "=" * 45)
    print("   CYBERSECURITY ASSET INVENTORY")
    print("=" * 45)

    for i, asset in enumerate(assets):
        display_asset(asset)
        if i < len(assets) - 1:
            print("-" * 45)

    # Summary
    total = len(assets)
    critical = sum(1 for a in assets if a["risk_level"] == "Critical")
    high = sum(1 for a in assets if a["risk_level"] == "High")
    medium = sum(1 for a in assets if a["risk_level"] == "Medium")
    vulnerable = sum(1 for a in assets if a["security_status"] == "Vulnerable")

    print("=" * 45)
    print(f"  Total Assets       : {total}")
    print(f"  Critical Assets    : {critical}")
    print(f"  High Risk Assets   : {high}")
    print(f"  Medium Risk Assets : {medium}")
    print(f"  Vulnerable Assets  : {vulnerable}")
    print("=" * 45 + "\n")


def display_security_summary(assets):
    """Display a detailed security summary/dashboard."""
    if not assets:
        print("\n  [i] No assets to summarize.\n")
        return

    total = len(assets)

    # Risk level counts
    risk_counts = {level: 0 for level in VALID_RISK_LEVELS}
    for a in assets:
        risk_counts[a["risk_level"]] += 1

    # Security status counts
    status_counts = {status: 0 for status in VALID_SECURITY_STATUSES}
    for a in assets:
        status_counts[a["security_status"]] += 1

    # Asset type counts
    type_counts = {t: 0 for t in VALID_ASSET_TYPES}
    for a in assets:
        type_counts[a["asset_type"]] += 1

    print("\n" + "=" * 45)
    print("   SECURITY SUMMARY DASHBOARD")
    print("=" * 45)

    print(f"\n  Total Assets: {total}\n")

    print("  --- Risk Level Breakdown ---")
    for level in VALID_RISK_LEVELS:
        count = risk_counts[level]
        bar = "█" * count
        print(f"    {level:<10} : {count:>3}  {bar}")

    print("\n  --- Security Status Breakdown ---")
    for status in VALID_SECURITY_STATUSES:
        count = status_counts[status]
        bar = "█" * count
        print(f"    {status:<12} : {count:>3}  {bar}")

    print("\n  --- Asset Type Breakdown ---")
    for atype in VALID_ASSET_TYPES:
        count = type_counts[atype]
        if count > 0:
            bar = "█" * count
            print(f"    {atype:<12} : {count:>3}  {bar}")

    # List critical / vulnerable assets
    critical_vulnerable = [
        a for a in assets
        if a["risk_level"] == "Critical" or a["security_status"] == "Vulnerable"
    ]
    if critical_vulnerable:
        print("\n  --- Assets Requiring Immediate Attention ---")
        for a in critical_vulnerable:
            print(f"    [{a['asset_id']}] {a['asset_name']} "
                  f"(Risk: {a['risk_level']}, Status: {a['security_status']})")

    print("\n" + "=" * 45 + "\n")


# ─── CRUD Operations ────────────────────────────────────────────────────────

def add_asset(assets):
    """Add a new asset to the inventory."""
    print("\n--- Add New Asset ---")

    # Asset ID (must be unique)
    while True:
        asset_id = get_validated_input("  Asset ID: ", validator=validate_asset_id)
        if any(a["asset_id"].lower() == asset_id.lower() for a in assets):
            print(f"  [!] Asset ID '{asset_id}' already exists. Please use a unique ID.")
        else:
            break

    asset_name = get_validated_input("  Asset Name: ")
    asset_type = get_validated_input(
        f"  Asset Type ({'/'.join(VALID_ASSET_TYPES)}): ",
        valid_options=VALID_ASSET_TYPES,
    )
    ip_address = get_validated_input("  IP Address: ", validator=validate_ip_address)
    os_name = get_validated_input("  Operating System: ")
    department = get_validated_input("  Department: ")
    risk_level = get_validated_input(
        f"  Risk Level ({'/'.join(VALID_RISK_LEVELS)}): ",
        valid_options=VALID_RISK_LEVELS,
    )
    security_status = get_validated_input(
        f"  Security Status ({'/'.join(VALID_SECURITY_STATUSES)}): ",
        valid_options=VALID_SECURITY_STATUSES,
    )

    asset = {
        "asset_id": asset_id,
        "asset_name": asset_name,
        "asset_type": asset_type,
        "ip_address": ip_address,
        "os": os_name,
        "department": department,
        "risk_level": risk_level,
        "security_status": security_status,
    }

    assets.append(asset)
    save_assets(assets)
    print(f"\n  [✓] Asset '{asset_name}' (ID: {asset_id}) added successfully!\n")


def add_multiple_assets(assets):
    """Add multiple assets at once."""
    print("\n--- Add Multiple Assets ---")
    while True:
        try:
            count = int(input("  Enter number of assets to add: ").strip())
            if count < 1:
                print("  [!] Please enter a positive number.")
                continue
            break
        except ValueError:
            print("  [!] Please enter a valid number.")

    for i in range(1, count + 1):
        print(f"\n  === Asset {i} of {count} ===")

        while True:
            asset_id = get_validated_input("  Asset ID: ", validator=validate_asset_id)
            if any(a["asset_id"].lower() == asset_id.lower() for a in assets):
                print(f"  [!] Asset ID '{asset_id}' already exists. Please use a unique ID.")
            else:
                break

        asset_name = get_validated_input("  Asset Name: ")
        asset_type = get_validated_input(
            f"  Asset Type ({'/'.join(VALID_ASSET_TYPES)}): ",
            valid_options=VALID_ASSET_TYPES,
        )
        ip_address = get_validated_input("  IP Address: ", validator=validate_ip_address)
        os_name = get_validated_input("  Operating System: ")
        department = get_validated_input("  Department: ")
        risk_level = get_validated_input(
            f"  Risk Level ({'/'.join(VALID_RISK_LEVELS)}): ",
            valid_options=VALID_RISK_LEVELS,
        )
        security_status = get_validated_input(
            f"  Security Status ({'/'.join(VALID_SECURITY_STATUSES)}): ",
            valid_options=VALID_SECURITY_STATUSES,
        )

        asset = {
            "asset_id": asset_id,
            "asset_name": asset_name,
            "asset_type": asset_type,
            "ip_address": ip_address,
            "os": os_name,
            "department": department,
            "risk_level": risk_level,
            "security_status": security_status,
        }
        assets.append(asset)
        print(f"  [✓] Asset '{asset_name}' added.")

    save_assets(assets)
    print(f"\n  [✓] {count} asset(s) added successfully!\n")


def search_asset(assets):
    """Search for an asset by ID, name, type, department, or risk level."""
    if not assets:
        print("\n  [i] No assets in the inventory.\n")
        return

    print("\n--- Search Asset ---")
    print("  Search by:")
    print("    1. Asset ID")
    print("    2. Asset Name")
    print("    3. Asset Type")
    print("    4. Department")
    print("    5. Risk Level")
    print("    6. Security Status")

    choice = get_validated_input("  Enter choice (1-6): ",
                                  valid_options=["1", "2", "3", "4", "5", "6"])

    field_map = {
        "1": ("asset_id", "Asset ID"),
        "2": ("asset_name", "Asset Name"),
        "3": ("asset_type", "Asset Type"),
        "4": ("department", "Department"),
        "5": ("risk_level", "Risk Level"),
        "6": ("security_status", "Security Status"),
    }

    field_key, field_label = field_map[choice]

    if choice == "3":
        query = get_validated_input(
            f"  Enter {field_label}: ", valid_options=VALID_ASSET_TYPES
        )
    elif choice == "5":
        query = get_validated_input(
            f"  Enter {field_label}: ", valid_options=VALID_RISK_LEVELS
        )
    elif choice == "6":
        query = get_validated_input(
            f"  Enter {field_label}: ", valid_options=VALID_SECURITY_STATUSES
        )
    else:
        query = get_validated_input(f"  Enter {field_label}: ")

    results = [
        a for a in assets
        if query.lower() in a[field_key].lower()
    ]

    if results:
        print(f"\n  Found {len(results)} matching asset(s):\n")
        print("-" * 45)
        for i, asset in enumerate(results):
            display_asset(asset)
            if i < len(results) - 1:
                print("-" * 45)
        print("-" * 45)
    else:
        print(f"\n  [!] No assets found matching '{query}'.\n")


def update_asset(assets):
    """Update an existing asset's information."""
    if not assets:
        print("\n  [i] No assets in the inventory.\n")
        return

    print("\n--- Update Asset ---")
    asset_id = get_validated_input("  Enter Asset ID to update: ")

    asset = None
    for a in assets:
        if a["asset_id"].lower() == asset_id.lower():
            asset = a
            break

    if not asset:
        print(f"\n  [!] Asset with ID '{asset_id}' not found.\n")
        return

    print(f"\n  Current details for '{asset['asset_name']}':")
    print("-" * 45)
    display_asset(asset)
    print("-" * 45)
    print("\n  (Press Enter to keep current value)\n")

    # Asset Name
    new_name = get_validated_input(
        f"  Asset Name [{asset['asset_name']}]: ", allow_empty=True
    )
    if new_name:
        asset["asset_name"] = new_name

    # Asset Type
    new_type = input(
        f"  Asset Type [{asset['asset_type']}] ({'/'.join(VALID_ASSET_TYPES)}): "
    ).strip()
    if new_type:
        matched = False
        for t in VALID_ASSET_TYPES:
            if new_type.lower() == t.lower():
                asset["asset_type"] = t
                matched = True
                break
        if not matched:
            print(f"  [!] Invalid type. Keeping '{asset['asset_type']}'.")

    # IP Address
    new_ip = input(f"  IP Address [{asset['ip_address']}]: ").strip()
    if new_ip:
        if validate_ip_address(new_ip):
            asset["ip_address"] = new_ip
        else:
            print(f"  [!] Invalid IP. Keeping '{asset['ip_address']}'.")

    # OS
    new_os = input(f"  Operating System [{asset['os']}]: ").strip()
    if new_os:
        asset["os"] = new_os

    # Department
    new_dept = input(f"  Department [{asset['department']}]: ").strip()
    if new_dept:
        asset["department"] = new_dept

    # Risk Level
    new_risk = input(
        f"  Risk Level [{asset['risk_level']}] ({'/'.join(VALID_RISK_LEVELS)}): "
    ).strip()
    if new_risk:
        matched = False
        for r in VALID_RISK_LEVELS:
            if new_risk.lower() == r.lower():
                asset["risk_level"] = r
                matched = True
                break
        if not matched:
            print(f"  [!] Invalid risk level. Keeping '{asset['risk_level']}'.")

    # Security Status
    new_status = input(
        f"  Security Status [{asset['security_status']}] ({'/'.join(VALID_SECURITY_STATUSES)}): "
    ).strip()
    if new_status:
        matched = False
        for s in VALID_SECURITY_STATUSES:
            if new_status.lower() == s.lower():
                asset["security_status"] = s
                matched = True
                break
        if not matched:
            print(f"  [!] Invalid status. Keeping '{asset['security_status']}'.")

    save_assets(assets)
    print(f"\n  [✓] Asset '{asset['asset_id']}' updated successfully!\n")


def delete_asset(assets):
    """Delete an asset from the inventory."""
    if not assets:
        print("\n  [i] No assets in the inventory.\n")
        return

    print("\n--- Delete Asset ---")
    asset_id = get_validated_input("  Enter Asset ID to delete: ")

    for i, a in enumerate(assets):
        if a["asset_id"].lower() == asset_id.lower():
            print(f"\n  Asset found:")
            print("-" * 45)
            display_asset(a)
            print("-" * 45)

            confirm = input("  Are you sure you want to delete? (yes/no): ").strip().lower()
            if confirm in ("yes", "y"):
                removed = assets.pop(i)
                save_assets(assets)
                print(f"\n  [✓] Asset '{removed['asset_name']}' (ID: {removed['asset_id']}) deleted.\n")
            else:
                print("\n  [i] Deletion cancelled.\n")
            return

    print(f"\n  [!] Asset with ID '{asset_id}' not found.\n")


# ─── Main Menu ───────────────────────────────────────────────────────────────

def print_menu():
    """Display the main menu."""
    print("=" * 45)
    print("  CYBERSECURITY ASSET INVENTORY SYSTEM")
    print("=" * 45)
    print("  1. Add Single Asset")
    print("  2. Add Multiple Assets")
    print("  3. Display All Assets")
    print("  4. Search Asset")
    print("  5. Update Asset")
    print("  6. Delete Asset")
    print("  7. Security Summary")
    print("  8. Exit")
    print("=" * 45)


def main():
    """Main entry point for the application."""
    assets = load_assets()

    while True:
        print_menu()
        choice = input("  Enter your choice (1-8): ").strip()

        if choice == "1":
            add_asset(assets)
        elif choice == "2":
            add_multiple_assets(assets)
        elif choice == "3":
            display_all_assets(assets)
        elif choice == "4":
            search_asset(assets)
        elif choice == "5":
            update_asset(assets)
        elif choice == "6":
            delete_asset(assets)
        elif choice == "7":
            display_security_summary(assets)
        elif choice == "8":
            print("\n  [i] Exiting. Stay secure! 🔒\n")
            sys.exit(0)
        else:
            print("\n  [!] Invalid choice. Please enter a number from 1 to 8.\n")


if __name__ == "__main__":
    main()
