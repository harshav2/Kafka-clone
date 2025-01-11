[![progress-banner](https://backend.codecrafters.io/progress/kafka/4a4e9a45-dcba-4d24-92f2-2971ad0e5703)](https://app.codecrafters.io/users/codecrafters-bot?r=2qF)

This is a Kafka clone from attempting the [codecrafters.io](https://codecrafters.io) "Build your Own Kafka" challenge.

As of this moment, it is capable of connecting to port 9092, and can accept and respond to the APIVersions API.
The requests and responses must be in v4 of the API.

**Note**: If you're viewing this repo on GitHub, head over to
[codecrafters.io](https://codecrafters.io) to try the challenge.

# Troubleshooting

## module `socket` has no attribute `create_server`

When running your server locally, you might see an error like this:

```
Traceback (most recent call last):
  File "/.../python3.7/runpy.py", line 193, in _run_module_as_main
    "__main__", mod_spec)
  File "/.../python3.7/runpy.py", line 85, in _run_code
    exec(code, run_globals)
  File "/app/app/main.py", line 11, in <module>
    main()
  File "/app/app/main.py", line 6, in main
    s = socket.create_server(("localhost", 6379), reuse_port=True)
AttributeError: module 'socket' has no attribute 'create_server'
```

This is because `socket.create_server` was introduced in Python 3.8, and you
might be running an older version.

You can fix this by installing Python 3.8 locally and using that.
