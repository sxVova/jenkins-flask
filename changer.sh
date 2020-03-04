#!/bin/bash
DSN=`cat file`
sudo sed "s,\dsn..*,\dsn="$DSN",g" -i .env