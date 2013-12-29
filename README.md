== GroupMe Account Tester ==
This is a quick convenient way to send messages from a test GroupMe account to groups. I'm using it to test my GroupMe Desktop Client quickly. 

To use:
* Make sure Python, pip, virtualenv, etc. are installed
* Copy config.json.sample to config.json and fill in the access token, port, and groups to use.
* `virtualenv env`
* `source env/bin/activate`
* `pip install -r requirements.txt`
* `chmod +x run.sh`
* `./run.sh (This creates a screen called "groupme-test-sender" and runs the program on it)

You can then send a test message by accessing http://<YOUR_URL>:PORT/send/<group_index_number>/<message>.

For example: http://example.com:5000/send/0/Hiya - This will send a message from the test user saying "Hiya" to the group at index 0 in the list in `config.json`. (In the sample, this would be 123456). 

The message should be URL encoded. For example: http://example.com:5000/send/1/Hello%20World%21 would send a message from the test user saying "Hello World!" to the group at index 1 in the list in `config.json`. (In the sample, this would be group ID 123456789).

The included Alfred (http://alfredapp.com) workflow is what I use, and it makes life really fast. (It's the second part of this system :D). It enables me to type `gt <message>` and easily send a message. It's much faster than I what I used to do. Feel free to use! :)
