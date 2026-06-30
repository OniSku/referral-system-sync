# Referral System Sync

A distributed referral system synchronization service for Telegram bots with centralized bonus processing.

## Description

Implements a microservices architecture for referral tracking and bonus distribution across multiple VPN services. Independent bot services communicate with a central referral processing hub responsible for bonus allocation.

## Tech Stack

| Component | Technology |
|-----------|------------|
| Bot Framework | aiogram (Telegram Bot API) |
| Database | SQLite |
| Containerization | Docker & Docker Compose |
| Language | Python 3.9+ |
| Architecture | Microservices |

## Architecture

```
referral-system-sync/
├── bot_services/
│   ├── main_bot/          # Primary VPN service bot
│   │   └── handlers.py    # Bot command handlers
│   └── protocol_bot/      # Secondary VPN service bot
│       └── handlers.py    # Bot command handlers
├── ref_center/
│   ├── main.py           # Central coordination service
│   └── scanner/
│       └── sync.py       # Payment scanning & referral logic
└── docker-compose.yml    # Service orchestration
```

## Key Features

- **Universal Referral Interceptor**: Captures referral IDs immediately on bot start, preventing data loss during user registration flows
- **Payment Scanner**: Automated transaction detection and processing with proper SQL JOIN logic
- **Cross-Service Sync**: Centralized referral tracking across multiple independent services
- **Data Integrity**: Fixed SQL queries using global Telegram IDs instead of internal table IDs
- **Date Format Support**: Compatible with modern database formats (ISO 8601)
- **Real-time Processing**: Instant bonus allocation after payment confirmation

## Installation & Setup

### Prerequisites

- Docker and Docker Compose
- Python 3.9+
- SQLite3

### Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `BOT_TOKEN_MAIN` | Telegram bot token for main service | Yes |
| `BOT_TOKEN_PROTOCOL` | Telegram bot token for protocol service | Yes |
| `DB_PATH` | Path to central database | Yes |
| `SCAN_INTERVAL` | Payment scanning interval in seconds | No (default: 300) |

### Quick Start

1. Clone the repository:
```bash
git clone https://github.com/OniSku/referral-system-sync.git
cd referral-system-sync
```

2. Configure environment variables in `.env` file

3. Build and start services:
```bash
docker-compose up --build
```

4. Services start scanning for payments and processing referrals on launch

## Technical Improvements

This project addresses critical integration issues in distributed referral systems:

- **Data Loss Prevention**: Referral links are captured before any business logic execution
- **SQL Integrity**: Fixed transaction visibility by using proper JOIN operations and global ID matching
- **Format Compatibility**: Updated date handling for modern database versions
- **Type Safety**: Improved async Telegram API interactions with proper typing

⚠️ **Disclaimer**: This repository serves as a code showcase for demonstration purposes. It does not contain a fully runnable production environment or all proprietary backend dependencies.