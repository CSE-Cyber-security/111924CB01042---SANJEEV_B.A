# Test Cases – Cybersecurity Asset Inventory System

## Test Case 1: Add Asset
| Step | Action | Input | Expected Result |
|------|--------|-------|-----------------|
| 1 | Select menu option 1 | `1` | "Add New Asset" prompt appears |
| 2 | Enter Asset ID | `A104` | Accepted |
| 3 | Enter Asset Name | `Finance-PC-01` | Accepted |
| 4 | Enter Asset Type | `Workstation` | Accepted (valid type) |
| 5 | Enter IP Address | `192.168.1.30` | Accepted (valid IPv4) |
| 6 | Enter OS | `Windows 10` | Accepted |
| 7 | Enter Department | `Finance` | Accepted |
| 8 | Enter Risk Level | `Low` | Accepted (valid risk level) |
| 9 | Enter Security Status | `Secure` | Accepted; success message displayed |

**Result:** Asset is saved in `data/assets.json`.

---

## Test Case 2: Add Asset – Duplicate ID
| Step | Action | Input | Expected Result |
|------|--------|-------|-----------------|
| 1 | Select menu option 1 | `1` | "Add New Asset" prompt appears |
| 2 | Enter Asset ID | `A101` | Error: "Asset ID 'A101' already exists" |

**Result:** System rejects duplicate and asks for a new ID.

---

## Test Case 3: Display All Assets
| Step | Action | Input | Expected Result |
|------|--------|-------|-----------------|
| 1 | Select menu option 3 | `3` | All assets displayed with formatted table |
| 2 | Verify summary | — | Total, Critical, High, Medium, Vulnerable counts shown |

**Result:** Output matches the expected format from the problem statement.

---

## Test Case 4: Search by Asset ID
| Step | Action | Input | Expected Result |
|------|--------|-------|-----------------|
| 1 | Select menu option 4 | `4` | Search menu appears |
| 2 | Choose search field | `1` (Asset ID) | Prompt for Asset ID |
| 3 | Enter search query | `A102` | Displays Web-Server asset details |

**Result:** Matching asset displayed correctly.

---

## Test Case 5: Search – No Results
| Step | Action | Input | Expected Result |
|------|--------|-------|-----------------|
| 1 | Select menu option 4 | `4` | Search menu appears |
| 2 | Choose search field | `1` (Asset ID) | Prompt for Asset ID |
| 3 | Enter search query | `XXXX` | "No assets found" message |

**Result:** Graceful handling of no results.

---

## Test Case 6: Update Asset
| Step | Action | Input | Expected Result |
|------|--------|-------|-----------------|
| 1 | Select menu option 5 | `5` | "Update Asset" prompt appears |
| 2 | Enter Asset ID | `A101` | Current details displayed |
| 3 | Update Risk Level | `High` | Risk level changed from Medium to High |
| 4 | Press Enter on other fields | *(empty)* | Other fields remain unchanged |

**Result:** Only modified fields are updated; changes saved to JSON.

---

## Test Case 7: Delete Asset
| Step | Action | Input | Expected Result |
|------|--------|-------|-----------------|
| 1 | Select menu option 6 | `6` | "Delete Asset" prompt appears |
| 2 | Enter Asset ID | `A103` | Asset details displayed with confirmation prompt |
| 3 | Confirm deletion | `yes` | Asset deleted; success message shown |

**Result:** Asset removed from `data/assets.json`.

---

## Test Case 8: Security Summary
| Step | Action | Input | Expected Result |
|------|--------|-------|-----------------|
| 1 | Select menu option 7 | `7` | Dashboard displayed |
| 2 | Verify risk breakdown | — | Counts for Low, Medium, High, Critical shown |
| 3 | Verify status breakdown | — | Counts for Secure, Warning, Vulnerable shown |
| 4 | Verify attention list | — | Critical/Vulnerable assets listed |

**Result:** Summary dashboard renders correctly.

---

## Test Case 9: Input Validation – Invalid IP Address
| Step | Action | Input | Expected Result |
|------|--------|-------|-----------------|
| 1 | Add asset | — | Reach IP Address prompt |
| 2 | Enter invalid IP | `999.999.999.999` | Error: "Invalid format" |
| 3 | Enter invalid IP | `abc.def.ghi.jkl` | Error: "Invalid format" |
| 4 | Enter valid IP | `10.0.0.1` | Accepted |

**Result:** Only valid IPv4 addresses accepted.

---

## Test Case 10: Input Validation – Invalid Asset Type
| Step | Action | Input | Expected Result |
|------|--------|-------|-----------------|
| 1 | Add asset | — | Reach Asset Type prompt |
| 2 | Enter invalid type | `Printer` | Error: "Invalid choice" with valid options |
| 3 | Enter valid type | `Server` | Accepted |

**Result:** Only predefined asset types accepted.

---

## Test Case 11: Input Validation – Empty Input
| Step | Action | Input | Expected Result |
|------|--------|-------|-----------------|
| 1 | Add asset | — | Reach any required field |
| 2 | Press Enter (empty) | *(empty)* | Error: "Input cannot be empty" |

**Result:** Empty strings rejected for required fields.

---

## Test Case 12: Add Multiple Assets
| Step | Action | Input | Expected Result |
|------|--------|-------|-----------------|
| 1 | Select menu option 2 | `2` | "Add Multiple Assets" prompt |
| 2 | Enter count | `3` | Prompted for 3 assets sequentially |
| 3 | Enter 3 complete assets | *(valid data)* | All 3 assets saved successfully |

**Result:** Batch addition works correctly.

---

## Test Case 13: Menu – Invalid Choice
| Step | Action | Input | Expected Result |
|------|--------|-------|-----------------|
| 1 | Enter invalid menu choice | `9` | Error: "Invalid choice" |
| 2 | Enter non-numeric input | `abc` | Error: "Invalid choice" |

**Result:** Menu loops until valid choice entered.
