#!/usr/bin/env python3
import json
import ipaddress
from urllib.parse import urlsplit, parse_qsl

TEST_URLS = [
    "https://login.example.com/account/verify?ref=training",
    "http://192.0.2.10/update/login",
    "https://example.com@192.0.2.10/signin",
    "https://example.com/%2e%2e/redirect?next=https%3A%2F%2Fexample.org",
]

def analyze(raw):
    findings = {"input": raw, "flags": []}

    try:
        u = urlsplit(raw)
        host = u.hostname
        findings.update({
            "scheme": u.scheme or None,
            "hostname": host,
            "port": u.port,
            "path": u.path,
            "query_parameters": dict(parse_qsl(u.query, keep_blank_values=True)),
            "userinfo_present": u.username is not None,
            "ip_literal": False,
        })

        if host:
            try:
                ipaddress.ip_address(host)
                findings["ip_literal"] = True
            except ValueError:
                pass

        if u.scheme.lower() != "https":
            findings["flags"].append("Not HTTPS")
        if u.username is not None:
            findings["flags"].append("User-info before @; inspect actual destination")
        if findings["ip_literal"]:
            findings["flags"].append("IP literal used as hostname")
        if "%" in u.path:
            findings["flags"].append("Percent-encoded path")
        if any(x in (u.path + u.query).lower()
               for x in ("login", "verify", "password", "redirect")):
            findings["flags"].append("Authentication/redirect keyword")

        findings["assessment"] = (
            "Heuristic only; these flags do not prove malicious activity."
        )
    except ValueError as exc:
        findings["parse_error"] = str(exc)

    return findings

print(json.dumps([analyze(x) for x in TEST_URLS], indent=2))
