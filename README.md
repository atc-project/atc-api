# ATC REST API

![](https://github.com/atc-project/atomic-threat-coverage/raw/master/images/logo_v1.png)

RESTful API built with Django Rest Framework. This project consumes following Atomic Threat Coverage entities and makes them interactive via HTTP methods:

- **Detection Rules** based on Sigma — Generic Signature Format for SIEM Systems
- **Data Needed** to be collected to produce detection of specific Threat
- **Logging Policies** need to be configured on data source to be able to collect Data Needed
- **Enrichments** for specific Data Needed which required for some Detection Rules
- **Response Actions** which executed during Incident Response
- **Response Playbooks** for reacting on specific threat, constructed from atomic Response Actions

The purpose of this project is to make all the ATC analytics available for 3rd party scripts and any other integrations.

# Description

> Check [Wiki](https://github.com/atc-project/atc-api/wiki) for more information

ATC REST API provides you handful of endpoits and filters associated with them for you to query the data. Inserting and updating data on the other hand is restricted only to the authenticated users. List of valid endpoints associated with the supported ATC entities is:

* `/api/v1/atc/detectionrule/`
* `/api/v1/atc/dataneeded/`
* `/api/v1/atc/loggingpolicy/`
* `/api/v1/atc/enrichment/`
* `/api/v1/atc/responseaction/`
* `/api/v1/atc/responseplaybook/`

Some endpoints are not to temper with directly, even though you can view the data. Those endpoints are:

* `/api/v1/atc/category/`
* `/api/v1/atc/channel/`
* `/api/v1/atc/eventid/`
* `/api/v1/atc/logfield/`
* `/api/v1/atc/logtype/`
* `/api/v1/atc/platform/`
* `/api/v1/atc/provider/`
* `/api/v1/atc/references/`
* `/api/v1/atc/stage/`
* `/api/v1/atc/tag/`
* `/api/v1/atc/volume/`

We have decided that for the statistics purposes you might want to have this available so no restrictions from our side. However, like it was mentioned already, those are and should be considered **Read Only** data.

On top of that, all of the endpoints support exact `id` match, for instance: `/api/v1/atc/eventid/4688/`

Head to [Wiki](https://github.com/atc-project/atc-api/wiki) to see detailed information about implementation of ATC entities, like [Detection Rule](https://github.com/atc-project/atc-api/wiki/Detection-Rule), and how to insert the data to the API.

# How To Run

We have prepared docker image already built for you for your convience. It's available under [mrbl4cyk/atc-api](https://hub.docker.com/r/mrbl4cyk/atc-api) Docker Hub repo. It exposes a port 8000. If you have docker already installed, issue the command:

```
$ docker run --rm -itd -p 8000:8000 mrbl4cyk/atc-api:latest
4321dd2e8462d34dc9a0e91a6450b05c0bfbdf5d560a28c6544aa57e537ae077
```

> **WARNING**: Default credentials are set to `admin` : `admin`. Change them from the Django Administration (`/admin/` endpoint).

If you wish to build the image by yourself, `Dockerfile` is already prepared for you. Just issue a docker build command:

```
$ docker build -t atcapi:readmetest .
Sending build context to Docker daemon  778.8kB
Step 1/10 : FROM ubuntu:18.04
 ---> c3c304cb4f22

(..)

Step 10/10 : ENTRYPOINT "/entrypoint.sh"
 ---> c04055972d91
Successfully built c04055972d91
Successfully tagged atcapi:readmetest
```
# Authors

* Jakob Weinzettl, [@mrblacyk](https://github.com/mrblacyk)

# Thanks to

* Mikhail Aksenov, [@AverageS](https://github.com/AverageS), for preparing the initial Django Rest Framework project template
