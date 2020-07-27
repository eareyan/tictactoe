#!/usr/bin/env bash

PORT=8080
echo "Port: $PORT"

# POST method predict
curl -d '{
	"0": {
		"0": "",
		"1": "P",
		"2": "P"
	},
	"1": {
		"0": "C",
		"1": "P",
		"2": "C"
	},
	"2": {
		"0": "C",
		"1": "",
		"2": ""
	}
}'\
     -H "Content-Type: application/json" \
     -X POST http://localhost:$PORT/tic_tac_toe_engine
     #-X POST https://us-central1-delivery-281415.cloudfunctions.net/ttt_server
