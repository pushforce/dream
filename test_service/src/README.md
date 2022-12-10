## Start command

docker-compose -f docker-compose.yml -f assistant_dists/dream/docker-compose.override.yml -f assistant_dists/dream/dev.yml up --build badlisted-words spacy-nounphrases pg test_service


## Test requests

curl --header "Content-Type: application/json" \
  --request POST \
  --data '{ "service": "badlisted-words", "endpoint": "badlisted_words", "payload": {"sentences": ["any fucks in this sentence", "good one", "fucked one"]}}' \
http://localhost:8000/process


curl --header "Content-Type: application/json" \
  --request POST \
  --data '{"service": "spacy-nounphrases", "endpoint": "respond", "payload": {"sentences": ["i like michal jordan", "hey this is a white bear"]}}' \
http://localhost:8000/process
