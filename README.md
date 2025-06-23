# ubuntu-python-image

A suite of Docker images featuring the latest stable Python versions, compiled from source with performance optimizations against the latest stable OpenSSL.

## Images

The images can be accessed from Docker Hub using `docker pull mmangkad/<image-name>`.

The workflow automatically discovers the latest patch versions. The table below shows the target versions. For the exact versions included in the images, please check the image tags on Docker Hub.

| Ubuntu Version | Python Series | Latest OpenSSL | Docker Image Name |
| :--- | :--- | :--- | :--- |
| 24.04 LTS (Noble Numbat) | 3.11 | 3.5.0 | `mmangkad/noble-python:3.11` |
| 24.04 LTS (Noble Numbat) | 3.12 | 3.5.0 | `mmangkad/noble-python:3.12` |
| 24.04 LTS (Noble Numbat) | 3.13 | 3.5.0 | `mmangkad/noble-python:3.13` |
| 24.10 (Oracular Oriole) | 3.11 | 3.5.0 | `mmangkad/oracular-python:3.11` |
| 24.10 (Oracular Oriole) | 3.12 | 3.5.0 | `mmangkad/oracular-python:3.12` |
| 24.10 (Oracular Oriole) | 3.13 | 3.5.0 | `mmangkad/oracular-python:3.13` |
| 25.04 (Plucky Puffin) | 3.11 | 3.5.0 | `mmangkad/plucky-python:3.11` |
| 25.04 (Plucky Puffin) | 3.12 | 3.5.0 | `mmangkad/plucky-python:3.12` |
| 25.04 (Plucky Puffin) | 3.13 | 3.5.0 | `mmangkad/plucky-python:3.13` |

### Tagging Strategy

Each image is published with two tags for flexibility:

1.  **Full Version Tag (e.g., `:3.12.11`):** A static tag for pinning to a specific patch release.
2.  **Minor Version Tag (e.g., `:3.12`):** A floating tag that always points to the latest-built patch release for that series.

**Example Usage:**

```bash
# Pull the latest patch release for Python 3.12 on Ubuntu 24.04
docker pull mmangkad/noble-python:3.12

# Pull a specific patch release
docker pull mmangkad/noble-python:3.12.11
```

## Rationale

Standard distribution images often rely on older, system-provided versions of Python and OpenSSL for stability. This project provides images built with the latest stable versions of both, ensuring access to modern language features and the latest security patches.

The build process uses a multi-stage `Dockerfile` to produce a lean, secure final image that does not contain unnecessary build tools or development headers.

## Automatic Updates

This repository is configured with a daily GitHub Actions workflow that runs at **10:00 AM Philippine Standard Time (PHT)**. This workflow automatically:
1.  Discovers the latest stable versions of Python and OpenSSL.
2.  Checks if corresponding Docker images already exist on the `mmangkad` Docker Hub account.
3.  Builds, tests, and pushes only the images for new, un-built versions.

This ensures the image tags are always kept up-to-date with the latest security and feature releases.

## Contribute

Feel free to suggest improvements and submit pull requests. Contributions are always welcome and much appreciated!
