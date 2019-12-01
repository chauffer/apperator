# apperator

Apperator aims to be the simplest way to deploy on Kubernetes.

## Disclaimer

**WARNING: This is PoC/alpha software. Written in a few hours using Bad Practices. Generates valid manifests though which you can always check before applying.**

It was born to scratch my itch, I keep copy pasting manifests and changing a few values to deploy most of my things. Might as well pull these few parameters away.

It is necessary to rewrite this doing something better than Jinja templates and to document it better.

## But I don't want to use another tool to manage my stuff!

That's understandable. You can use apperator to generate manifests, store them however you want and apply them however you want.

## Usage

Example:
```
apiVersion: apperator.simone.sh/v1alpha1
Kind: app
metadata:
  name: plex
  namespace: plex
spec:
  create_namespace: True
  containers:
  - image: plexinc/pms-docker
    hostVolumes:
    - /opt/k3s/plex/plex-config:/plex
    - /opt/k3s/plex/plex-transcode:/transcode
    - /opt/k3s/plex/plex-data:/data
  ingress:
  - hostname: plex.simone.sh
    tls:
      host: '*.simone.sh'
      secretName: wildcard-simone-sh-tls
    targetPort: 32400

```

#### Docker

`cat apperator.yaml | docker run --rm -t chauffer/apperator build > manifests.yaml`

#### Python

`pip install apperator`

`apperator build -f apperator.yaml`

`apperator apply -f apperator.yaml` (applies through kubectl to the current cluster)

`apperator delete -f apperator.yaml` (deletes through kubectl to the current cluster)
