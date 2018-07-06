#!/usr/bin/env bash
BASEDIR=$(dirname "$0")
aws s3 sync $BASEDIR/../www s3://xkcd.org.cn --region ap-northeast-1
