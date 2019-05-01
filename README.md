# Suadente
## Docker container to run suadente reports.

To run the app locally install `docker` then:

```
docker build --rm -f "Dockerfile" -t suadente:latest .
docker run --rm -d suadente:latest
```

## TODO
- [ ] XML report
- [ ] Unittest
- [ ] Documentation
- [ ] more commnets