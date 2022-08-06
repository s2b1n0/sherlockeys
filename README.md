# Sherlockeys
Sherlockeys is a usefull tool for pen-tester. It can quickly discover if a given api key works against the most common saas applications.

![Sherlockeys](/assets/sherlockeys-256.png)
## Screenshoot ##

![Screenshot](/assets/screenshot.png)

## Installation ##

**Pip**

```
pip install sherlockeys
```

## Getting Started ##
**Run a scan**

```
sherlockeys <key>
```

**Enable debug**

```
sherlockeys <key> -d
```

**Enable client-id and client-secret support**

Add a client-id token to be tested together with the secret key, in applications that require client-id and client-key authentication

```
sherlockeys <client_key> --client <client_id>
```
**Get help**

```
sherlockeys -h
```

## Supported Applications ##


| Type		                    | Provider                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|---------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Single-key/token          | Gitlab Personal Token, Github Personal Token, Youtube Api Key, Twitter Bearer Token, Hubspot Private App Key, Heroku Api Key, NpmJs Access Token, Slack App Oauth Token, Spotify Client Secret, Visual Studio App Center Api Key, Bit.ly Api Access Token, Asana Personal Access Token, Zapier Webhook Token, Calendly Personal Access Token, Dropbox App Oauth2 Access Token, Sonarcloud Access Token, Ipstack Api Access Token, Shodan Api Token, TravisCi Api Token (.com and .org), CircleCi Personal Api Token, Jumpcloud Personal Api Key, PivotalTracker Api Token, Wakatime Api Key, Buildkite Access Token, Delighted Api Key, ButterCMS Api Key, Lokalise Api Key   					 | 
| Client id and secret auth | Facebook Application                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | 

Thanks [streaak/keyhacks](https://github.com/streaak/keyhacks) for made it easier.

More applications are going to be supported.

## License ##
This software is free software: you can redistribute it and/or modify it under the terms of the Apache license. OWASP Amass and any contributions are Copyright © by João Sabino (s2b1n0) 2022.
