# mingjiang-test

A test repository for GitHub Actions workflows and Docker configurations.

## Features

- GitHub Actions workflows for CI/CD
- Docker image build support
- Automated testing pipeline

## Workflows

- `blank.yml` - Basic workflow template
- `docker-image.yml` - Docker image build and push
- `dockertest.yml` - Docker container testing
- `test.yml` - General testing workflow

## Docker Usage

```bash
# Build the image
docker build -t mingjiang-test .

# Run the container
docker run mingjiang-test
```

## License

MIT
