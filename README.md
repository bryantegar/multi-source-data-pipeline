# Multi Source Data Engineering Pipeline

## Overview

This project simulates a production-style data engineering pipeline that ingests data from multiple sources, processes it, validates it, stores it in a database, and schedules automated execution.

The goal is to demonstrate real-world data engineering practices such as modular architecture, logging, scheduling, and persistence.

---

## Architecture

Data Flow:

API + CSV → Transform → Merge → Validate → Store → Log → Scheduler

---

## Features

* Multi-source ingestion (API + CSV)
* Data transformation pipeline
* Data validation system
* SQLite database storage
* Logging system
* Automated scheduler
* Modular architecture design

---

## Tech Stack

* Python
* Pandas
* SQLite
* REST API
* Logging
* Scheduler automation

---

## Project Structure

```
src/
 ┣ api_collector.py
 ┣ transform.py
 ┣ merge.py
 ┣ validate.py
 ┣ db.py
 ┣ logger.py
 ┗ pipeline.py
```

---

## Run Pipeline

```bash
python -m src.pipeline
```

---

## Run Scheduler

```bash
python scheduler.py
```

---

## Engineering Concepts Demonstrated

* ETL pipeline design
* Data validation architecture
* Automated execution
* Persistent storage integration
* Logging & monitoring
* Modular system design

---

## Author

Bryan Tegar
Aspiring Data Engineer
