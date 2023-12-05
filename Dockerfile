# [Choice] Ubuntu version (use jammy on local arm64/Apple Silicon): jammy, focal
ARG VARIANT="jammy"
FROM buildpack-deps:${VARIANT}-curl

LABEL dev.containers.features="common"

# [Optional] Uncomment this section to install additional OS packages.
RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
     && apt-get -y install --no-install-recommends lrzip python3-pip

RUN pip install huggingface_hub hf_transfer
RUN export HF_HUB_ENABLE_HF_TRANSFER=1
RUN mkdir /tmp/hfcache
RUN export TRANSFORMERS_CACHE=/tmp/hfcache/
RUN script screen.log
