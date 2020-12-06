import client as c

if __name__ == "__main__":
    client = c.Client("localhost", 12345, 2698)
    print("========================")
    print(client.send_coordinates("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", 256 ** 4 - 1, 256 ** 4 - 1))
    print("========================")
    print(client.send_coordinates("bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb", 256 ** 3 - 1, 256 ** 3 - 1))
    print("========================")
    print(client.send_coordinates("cccccccccccccccccccccccccccccccc", 256 ** 2 - 1, 256 ** 2 - 1))
    print("========================")
    s = "AAEAAAD/////AQAAAAAAAAAMAgAAAE5TeXN0ZW0uRGF0YSwgVmVyc2lvbj00LjAuMC4wLCBDdWx0dXJlPW5ldXRyYWwsIFB1YmxpY0tleVRva2VuPWI3N2E1YzU2MTkzNGUwODkFAQAAABNTeXN0ZW0uRGF0YS5EYXRhU2V0CgAAABZEYXRhU2V0LlJlbW90aW5nRm9ybWF0E0RhdGFTZXQuRGF0YVNldE5hbWURRGF0YVNldC5OYW1lc3BhY2UORGF0YVNldC5QcmVmaXgVRGF0YVNldC5DYXNlU2Vuc2l0aXZlEkRhdGFTZXQuTG9jYWxlTENJRBpEYXRhU2V0LkVuZm9yY2VDb25zdHJhaW50cxpEYXRhU2V0LkV4dGVuZGVkUHJvcGVydGllcxREYXRhU2V0LlRhYmxlcy5Db3VudBBEYXRhU2V0LlRhYmxlc18wBAEBAQAAAAIABx9TeXN0ZW0uRGF0YS5TZXJpYWxpemF0aW9uRm9ybWF0AgAAAAEIAQgCAgAAAAX9////H1N5c3RlbS5EYXRhLlNlcmlhbGl6YXRpb25Gb3JtYXQBAAAAB3ZhbHVlX18ACAIAAAABAAAABgQAAAAACQQAAAAJBAAAAAAJBAAAAAoBAAAACQUAAAAPBQAAALQDAAACAAEAAAD/////AQAAAAAAAAAMAgAAAF5NaWNyb3NvZnQuUG93ZXJTaGVsbC5FZGl0b3IsIFZlcnNpb249My4wLjAuMCwgQ3VsdHVyZT1uZXV0cmFsLCBQdWJsaWNLZXlUb2tlbj0zMWJmMzg1NmFkMzY0ZTM1BQEAAABCTWljcm9zb2Z0LlZpc3VhbFN0dWRpby5UZXh0LkZvcm1hdHRpbmcuVGV4dEZvcm1hdHRpbmdSdW5Qcm9wZXJ0aWVzAQAAAA9Gb3JlZ3JvdW5kQnJ1c2gBAgAAAAYDAAAA1gU8P3htbCB2ZXJzaW9uPSIxLjAiIGVuY29kaW5nPSJ1dGYtMTYiPz4NCjxPYmplY3REYXRhUHJvdmlkZXIgTWV0aG9kTmFtZT0iU3RhcnQiIElzSW5pdGlhbExvYWRFbmFibGVkPSJGYWxzZSIgeG1sbnM9Imh0dHA6Ly9zY2hlbWFzLm1pY3Jvc29mdC5jb20vd2luZngvMjAwNi94YW1sL3ByZXNlbnRhdGlvbiIgeG1sbnM6c2Q9ImNsci1uYW1lc3BhY2U6U3lzdGVtLkRpYWdub3N0aWNzO2Fzc2VtYmx5PVN5c3RlbSIgeG1sbnM6eD0iaHR0cDovL3NjaGVtYXMubWljcm9zb2Z0LmNvbS93aW5meC8yMDA2L3hhbWwiPg0KICA8T2JqZWN0RGF0YVByb3ZpZGVyLk9iamVjdEluc3RhbmNlPg0KICAgIDxzZDpQcm9jZXNzPg0KICAgICAgPHNkOlByb2Nlc3MuU3RhcnRJbmZvPg0KICAgICAgICA8c2Q6UHJvY2Vzc1N0YXJ0SW5mbyBBcmd1bWVudHM9Ii9jIGNtZC5leGUgL0MgZWNobyBwd25lZCAmZ3Q7IEQ6XFBXTkVELnR4dCIgU3RhbmRhcmRFcnJvckVuY29kaW5nPSJ7eDpOdWxsfSIgU3RhbmRhcmRPdXRwdXRFbmNvZGluZz0ie3g6TnVsbH0iIFVzZXJOYW1lPSIiIFBhc3N3b3JkPSJ7eDpOdWxsfSIgRG9tYWluPSIiIExvYWRVc2VyUHJvZmlsZT0iRmFsc2UiIEZpbGVOYW1lPSJjbWQiIC8+DQogICAgICA8L3NkOlByb2Nlc3MuU3RhcnRJbmZvPg0KICAgIDwvc2Q6UHJvY2Vzcz4NCiAgPC9PYmplY3REYXRhUHJvdmlkZXIuT2JqZWN0SW5zdGFuY2U+DQo8L09iamVjdERhdGFQcm92aWRlcj4LCw==";
    print(client.send_base64(s))
    s = client.get_auth_token()
    print(s)
