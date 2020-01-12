# **!!!!UNDER DEVELOPMENT!!!!**

# This is an ATC-project API. 

| Entity | Readiness |
| --- | --- |
| Logging Policy | Fully supported |
| Data Needed | Fully supported |
| Enrichments | Fully supported |
| Response Actions | **NOT** supported |
| Response Playbooks | **NOT** supported |
| Detection Rules | Partially supported (view, insert) |


* Fully supported - User can view, insert, update and filter the data
* Partially supported - User can only either view/insert/filter data

# Entities

* Use `GET` method to view the data
* Use `POST` method to insert or update the data
* Use `PUT` or `PATCH` method to update the data

How come `POST`ing data sometimes creates the object and sometimes it updates already existing one? It's title dependant. Title has to be **unique** among ATC entities. If the REST API finds already name object like this, it will update it instead of creating a new one.

---

# Logging Policy

### JSON structure

```json
{
    "title": "Logging Policy #0001",
    "default": "Not configured",
    "volume": "Low",
    "description": "Description of the logging policy. Keep in min that it has to be valid JSON so any new lines have to be escaped \n",
    "eventID": [1, 4688],
    "references": ["https://duckduckgo.com/", "https://www.torproject.org/"],
    "configuration": "Again, any new lines have to escaped\n```\nsomecode\n```\n"
}
```

### ATC Logging Policy yaml file

```yaml
title: Logging Policy #0001
default: Not configured
volume: Low
description: >
  Description of the logging policy. Keep in min that it has to be valid JSON so any new lines have to be escaped

eventID:
  - 1
  - 4688
references:
    - https://duckduckgo.com/
    - https://www.torproject.org/
configuration: |
  Again, any new lines have to escaped
  ``
  somecode
  ``
```

### Python snippet for inserting data

```python
path_to_lp = "LP0001.yml"

with open(path_to_lp, 'r') as stream:
    lp = yaml.safe_load(stream)

r = requests.post(
    'http://127.0.0.1:8000/api/v1/atc/loggingpolicy/',
    json=lp
)
```

### Filters

There are two types of filters - `exact match` and `contains`. Here is the list of valid filters:

#### Contains

* `title_contains`

#### Exact

* `title_exact`
* `eventID_exact`
* `volume_exact`

# Data Needed

### JSON structure

```json
{
    "title": "Data Needed #0001",
    "description": "Description of data needed",
    "loggingpolicy": ["Logging Policy #0001"],
    "references": ["https://github.com/atc-project/"],
    "category": "OS Logs",
    "platform": "Windows",
    "type": "Windows Log",
    "channel": "Security",
    "provider": "Microsoft-Windows-Security-Auditing",
    "fields": ["EventID", "Hostname"],
    "sample": "<Event xmlns=\"http://schemas.microsoft.com/win/2004/08/events/event\">\n(..)\n  </Event>"
}
```

### ATC Data Needed yaml file

```yaml
title: Data Needed #0001
description: >
  Description of data needed
loggingpolicy:
  - Logging Policy #0001
references:
  - https://github.com/atc-project/
category: OS Logs
platform: Windows
type: Windows Log
channel: Security
provider: Microsoft-Windows-Security-Auditing
fields:
  - EventID
  - Hostname
sample: |
  <Event xmlns="http://schemas.microsoft.com/win/2004/08/events/event">
    (..)
  </Event>
```

### Python snippet for inserting data

```python
path_to_dn = "DN0001.yml"

with open(path_to_dn, 'r') as stream:
    dn = yaml.safe_load(stream)

r = requests.post(
    'http://127.0.0.1:8000/api/v1/atc/dataneeded/',
    json=dn
)
```

### Filters

There are two types of filters - `exact match` and `contains`. Here is the list of valid filters:

#### Contains

* `loggingpolicy_contains`
* `title_contains`
* `category_contains`
* `channel_contains`
* `platform_contains`
* `provider_contains`
* `fields_contains`

#### Exact

* `loggingpolicy_exact`
* `title_exact`
* `category_exact`
* `channel_exact`
* `platform_exact`
* `provider_exact`
* `fields_exact`

# Enrichment

### JSON structure

```json
{
    "data_needed": ["Data Needed #0001"],
    "data_to_enrich": ["Data Needed #0003"],
    "requirements": ["Enrichment #0002"],
    "references": ["https://google.com/"],
    "new_fields": [],
    "title": "Enrichment #0002",
    "description": "This enriches everything!",
    "author": "atc-project",
    "config": "Here is the config example:\n\n  ```\n  code\n  ```\n"
}
```

### ATC Enrichment yaml file

```yaml
title: Enrichment #0002
description: >
  This enriches everything!
data_needed:
  - Data Needed #0001
data_to_enrich:
  - Data Needed #0003
references:
  - https://www.google.com/
requirements:
  - Enrichment #0001
new_fields:
  - ParentUser
  - ParentIntegrityLevel
author: atc-project
config: |
  Here is the config example:

  ``
  code
  ``

```

### Python snippet for inserting data

```python
path_to_en = "EN0002.yml"

with open(path_to_en, 'r') as stream:
    en = yaml.safe_load(stream)

r = requests.post(
    'http://127.0.0.1:8000/api/v1/atc/enrichment/',
    json=en
)
```

### Filters

There are two types of filters - `exact match` and `contains`. Here is the list of valid filters:

#### Contains

* `title_contains`
* `data_needed_contains`
* `data_to_enrich_contains`
* `requirements_contains`
* `new_fields_contains`

#### Exact

* `title_exact`
* `data_needed_exact`
* `data_to_enrich_exact`
* `requirements_exact`
* `new_fields_exact`

---

# Docker

To run it you should have docker-compose installed ( https://docs.docker.com/compose/install/ ). 
1. Set enviromental variables: 
export SECRET_KEY="YOURSECRETKEY";
export DB_HOST="postgres";
export DB_PASSWORD="YOURDATABASEPASSWORD";

2. Run docker-compose up -d 
3. Your ATC-API would be availible on 8000 port 


If you want to set up environment for development purposes you should 
1. Export enviromental variables 
2. Run docker-compose up -d postgres 

Your database would be availible on 5432 port you should apply migrations and start developing ATC API. 

---

## Known issues/things

- [ ] `author` field is not parsed/handled in every entity
