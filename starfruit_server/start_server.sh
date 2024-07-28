#!/bin/bash

set -ex

uvicorn main:app --reload --port 9966
