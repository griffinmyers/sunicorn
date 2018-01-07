# sunicorn

sunicorn is an educational example of a forking webserver, utilizing a unix
socket to handle distriubting inbound requests accros a pool of child worker
processes.  It's adapted from Ryan Tomayako's ruby implementation
[here](https://tomayko.com/blog/2009/unicorn-is-unix).

## Running

In one window...

```bash
python server.py
```

and another...

```bash
echo 'dental plan' | nc localhost 4242
echo 'dental plan' | nc localhost 4242
echo 'dental plan' | nc localhost 4242
echo 'dental plan' | nc localhost 4242
echo 'dental plan' | nc localhost 4242
echo 'dental plan' | nc localhost 4242
echo 'dental plan' | nc localhost 4242
echo 'dental plan' | nc localhost 4242
```
