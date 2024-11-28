# RedditAPI Scraper

## Overview
**RedditAPI Scraper** is a Python-based application designed to fetch and store images from the **blursedimages** subreddit on Reddit. This project utilizes the **PRAW** (Python Reddit API Wrapper) library to interact with the Reddit API, allowing users to scrape the latest images and store them in a Redis database for further use.

## Features

- **Image Scraping**: Automatically fetches the latest images from the **blursedimages** subreddit.
- **Redis Storage**: Stores image URLs along with metadata (title, author, creation timestamp) in a Redis database for quick access.
- **Background Processing**: Supports background tasks to ensure that scraping operations do not block the main application, allowing for responsive user interactions.
- **API Integration**: Exposes a RESTful API using FastAPI, enabling easy triggering of scraping processes and retrieval of stored images.

## Getting Started

### Prerequisites

- Python 3.7 or higher
- Redis server running locally or remotely
- Required Python packages (install using `pip install -r requirements.txt`)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/kinuthiajr/RedditAPI.git
