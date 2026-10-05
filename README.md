# 🔒 Cybersecurity Asset Inventory System

**Weekly Mini Project – 01**

A console-based Python application for managing an organization's IT assets, tracking their security status, and identifying assets that require immediate attention.

---

## 📋 Table of Contents

- [Features](#features)
- [Project Structure](#project-structure)
- [Requirements](#requirements)
- [How to Run](#how-to-run)
- [Usage Guide](#usage-guide)
- [Sample Output](#sample-output)
- [Screenshots](#screenshots)

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| **Add Asset** | Add single or multiple IT assets with validated input |
| **Display Assets** | View all assets in a formatted inventory table with summary |
| **Search Asset** | Search by Asset ID, Name, Type, Department, Risk Level, or Status |
| **Update Asset** | Modify any field of an existing asset (press Enter to keep current value) |
| **Delete Asset** | Remove an asset with confirmation prompt |
| **Security Summary** | Dashboard showing risk breakdown, status breakdown, and assets needing attention |
| **Data Persistence** | All assets stored in `data/assets.json` |
| **Input Validation** | Validates IP addresses, asset types, risk levels, and security statuses |

---

## 📁 Project Structure

```
Week-01-Cybersecurity-Asset-Inventory/
│
├── src/
│   └── asset_inventory.py      # Main application source code
│
├── data/
│   └── assets.json              # Persistent data storage (JSON)
│
├── tests/
│   └── test_cases.md            # Test cases documentation
│
├── screenshots/
│   ├── 01-add-asset.png
│   ├── 02-display-assets.png
│   ├── 03-search-asset.png
│   ├── 04-update-asset.png
│   ├── 05-delete-asset.png
│   ├── 06-security-summary.png
│   └── 07-input-validation.png
│
└── README.md                    # This file
```

---

## ⚙️ Requirements

- **Python 3.6+** (no external dependencies)

---

## 🚀 How to Run

```bash
# Navigate to the project directory
cd Week-01-Cybersecurity-Asset-Inventory

# Run the application
python src/asset_inventory.py
```

---

## 📖 Usage Guide

### Main Menu

```
=============================================
  CYBERSECURITY ASSET INVENTORY SYSTEM
=============================================
  1. Add Single Asset
  2. Add Multiple Assets
  3. Display All Assets
  4. Search Asset
  5. Update Asset
  6. Delete Asset
  7. Security Summary
  8. Exit
=============================================
```

### Asset Fields

| Field | Description | Validation |
|-------|-------------|------------|
| Asset ID | Unique identifier | Alphanumeric, hyphens, underscores |
| Asset Name | Descriptive name | Non-empty string |
| Asset Type | Category of asset | Workstation / Server / Router / Switch / Application |
| IP Address | Network address | Valid IPv4 format (e.g., 192.168.1.10) |
| Operating System | OS running on asset | Non-empty string |
| Department | Owner department | Non-empty string |
| Risk Level | Security risk classification | Low / Medium / High / Critical |
| Security Status | Current security state | Secure / Warning / Vulnerable |

---

## 📊 Sample Output

### Display All Assets

```
=============================================
   CYBERSECURITY ASSET INVENTORY
=============================================
  Asset ID     : A101
  Asset Name   : HR-PC-01
  Asset Type   : Workstation
  IP Address   : 192.168.1.10
  OS           : Windows 11
  Department   : HR
  Risk Level   : Medium
  Status       : Secure
---------------------------------------------
  Asset ID     : A102
  Asset Name   : Web-Server
  Asset Type   : Server
  IP Address   : 192.168.1.20
  OS           : Ubuntu
  Department   : IT
  Risk Level   : Critical
  Status       : Vulnerable
---------------------------------------------
  Asset ID     : A103
  Asset Name   : Core-Router
  Asset Type   : Router
  IP Address   : 192.168.1.1
  OS           : Cisco IOS
  Department   : Network
  Risk Level   : High
  Status       : Warning
=============================================
  Total Assets       : 3
  Critical Assets    : 1
  High Risk Assets   : 1
  Medium Risk Assets : 1
  Vulnerable Assets  : 1
=============================================
```

---

## 📸 Screenshots

| # | Feature | Screenshot |
|---|---------|------------|
| 1 | Add Asset | ![Add Asset](screenshots/01-add-asset.png) |
| 2 | Display Assets | ![Display](screenshots/02-display-assets.png) |
| 3 | Search Asset | ![Search](screenshots/03-search-asset.png) |
| 4 | Update Asset | ![Update](screenshots/04-update-asset.png) |
| 5 | Delete Asset | ![Delete](screenshots/05-delete-asset.png) |
| 6 | Security Summary | ![Summary](screenshots/06-security-summary.png) |
| 7 | Input Validation | ![Validation](screenshots/07-input-validation.png) |

---

## 👤 Author

Cybersecurity Asset Inventory System — Weekly Mini Project 01
