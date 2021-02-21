# Setup

First of all, you need to register your app in google to get client secrets for access to spreadsheets. You have to download client secret ('credentials.json') into the root directory.

After this, you need to set up a couple of env variables. For this, I recommend writing Makefile to build a docker container like the following. Or of course, you can use venv.

```makefile
SMTP_LOGIN := 'sender_email@gmail.com'
SMTP_PASSWORD := 'sender_password'
TEST_EMAIL := 'test_email@gmail.com'
EMAILS_SPREADSHEET_ID := 'spreadsheet id with target emails'
EMAILS_SPREADSHEET_RANGE := 'target emails range' # like D2:D
INFO_SPREADSHEET_ID := 'spreadsheet id with message's info'

send:
	docker build \
	-t kau_notifications . && \
	docker run \
	--env SMTP_LOGIN=${SMTP_LOGIN} \
	--env SMTP_PASSWORD=${SMTP_PASSWORD} \
	--env EMAILS_SPREADSHEET_ID=${EMAILS_SPREADSHEET_ID} \
	--env EMAILS_SPREADSHEET_RANGE=${EMAILS_SPREADSHEET_RANGE} \
	--env INFO_SPREADSHEET_ID=${INFO_SPREADSHEET_ID} \
	kau_notifications


test:
	docker build \
	-t kau_notifications_test . && \
	docker run \
	--env SMTP_LOGIN=${SMTP_LOGIN} \
	--env SMTP_PASSWORD=${SMTP_PASSWORD} \
	--env TEST_EMAIL=${TEST_EMAIL} \
	--env EMAILS_SPREADSHEET_ID=${EMAILS_SPREADSHEET_ID} \
	--env EMAILS_SPREADSHEET_RANGE=${EMAILS_SPREADSHEET_RANGE} \
	--env INFO_SPREADSHEET_ID=${INFO_SPREADSHEET_ID} \
	kau_notifications_test

```

# Run

```bash
$ make test # for send to test email
$ make send # for send to emails from spreadsheet
```