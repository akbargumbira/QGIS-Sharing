#!/usr/bin/env bash
psql -c 'create database qgis_sharing_platform;' -U postgres
psql -c 'CREATE EXTENSION postgis;' -U postgres -d qgis_sharing_platform
