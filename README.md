Move service file to /etc/systemd/system/:

```bash
sudo cp ./live-tracker.service /etc/systemd/system/
```

Enable and start the service:

```
sudo systemctl enable --now live-tracker
```

Enjoy! :-)
