FROM ubuntu:18.04

COPY atccore /atccore

WORKDIR /atccore

RUN apt-get update && \
	apt-get install -y --no-install-recommends python3.6 python3-pip locales python3-setuptools && \
	rm -rf /var/lib/apt/lists/* && \
	localedef -i en_US -c -f UTF-8 -A /usr/share/locale/locale.alias en_US.UTF-8

ENV LANG en_US.utf8

RUN	pip3 install pipenv && \
	pipenv install && \
	pipenv run ./manage.py collectstatic && \
	pipenv run ./manage.py migrate && \
	pipenv run ./manage.py shell -c "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'admin@localhost', 'admin')"

ADD entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
EXPOSE 8000
ENTRYPOINT "/entrypoint.sh"
